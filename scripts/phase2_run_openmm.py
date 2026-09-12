#!/usr/bin/env python3
"""Phase 2 OpenMM entrypoint — FKBP first-run package (P2-A).

Do NOT launch a GPU pod or this script's production path until a human
approves the compute budget. `--dry-run` is CPU-only and imports no OpenMM.

After approval, on a CUDA box (see phase2-plan.md):

  python scripts/phase2_run_openmm.py --dry-run
  python scripts/phase2_run_openmm.py --system p2a_fkbp12_crystal --ns 100
  python scripts/phase2_run_openmm.py --system p2a_fkbp52_vina --ns 100
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLAN_PATH = ROOT / "docs" / "research" / "virtual" / "phase2" / "phase2-plan.json"
INPUTS = ROOT / "docs" / "research" / "virtual" / "phase2" / "inputs"

try:
    from openmm import LangevinMiddleIntegrator, MonteCarloBarostat, Platform, XmlSerializer
    from openmm import app, unit
    from openmmforcefields.generators import SystemGenerator
    from openff.toolkit import Molecule
    from pdbfixer import PDBFixer

    HAS_OPENMM = True
except ImportError:
    HAS_OPENMM = False


SYSTEMS = {
    "p2a_fkbp12_crystal": {
        "complex": INPUTS / "complexes" / "p2a_fkbp12_crystal_rap.pdb",
        "protein": INPUTS / "receptors" / "1FKB_A_protein.pdb",
        "ligand": INPUTS / "ligands" / "rapamycin_1fkb_crystal.pdb",
        "smiles_idx": INPUTS / "smiles_idx" / "rapamycin_fkbp12_calib.json",
        "smiles_override": None,  # use JSON SMILES (neutral macrolide)
        "role": "protocol_control",
    },
    "p2a_fkbp12_vina": {
        "complex": INPUTS / "complexes" / "p2a_fkbp12_vina_rap.pdb",
        "protein": INPUTS / "receptors" / "1FKB_A_protein.pdb",
        "ligand": INPUTS / "ligands" / "rapamycin_fkbp12_calib_top.pdb",
        "smiles_idx": INPUTS / "smiles_idx" / "rapamycin_fkbp12_calib.json",
        "smiles_override": None,
        "role": "vina_pose_control",
    },
    "p2a_fkbp52_vina": {
        "complex": INPUTS / "complexes" / "p2a_fkbp52_vina_rap.pdb",
        "protein": INPUTS / "receptors" / "1N1A_A_aligned_to_1FKB.pdb",
        "ligand": INPUTS / "ligands" / "rapamycin_fkbp52_top.pdb",
        "smiles_idx": INPUTS / "smiles_idx" / "rapamycin_fkbp52.json",
        "smiles_override": None,
        "role": "hypothesis",
    },
}


def load_plan() -> dict:
    if not PLAN_PATH.is_file():
        raise FileNotFoundError(PLAN_PATH)
    return json.loads(PLAN_PATH.read_text())


def dry_run() -> dict:
    plan = load_plan()
    missing = []
    present = []
    for name, spec in SYSTEMS.items():
        for key in ("complex", "protein", "ligand", "smiles_idx"):
            path = spec[key]
            if path.is_file():
                present.append(str(path.relative_to(ROOT)))
            else:
                missing.append(str(path.relative_to(ROOT)))
    recommended = plan.get("recommended_first_run", {}).get("system_ids", [])
    return {
        "ok": not missing,
        "openmm_importable": HAS_OPENMM,
        "budget_approved": False,
        "note": (
            "Production MD is gated on human budget approval. "
            "This dry-run does not start a simulator."
        ),
        "recommended_first_run": recommended,
        "inputs_present": present,
        "inputs_missing": missing,
        "plan": str(PLAN_PATH.relative_to(ROOT)),
    }


def _ligand_molecule(spec: dict) -> "Molecule":
    meta = json.loads(spec["smiles_idx"].read_text())
    smiles = spec["smiles_override"] or meta["smiles"]
    # from_pdb_and_smiles maps pose coordinates onto the OpenFF graph.
    return Molecule.from_pdb_and_smiles(str(spec["ligand"]), smiles)


def _fixed_protein(protein_pdb: Path):
    fixer = PDBFixer(filename=str(protein_pdb))
    fixer.findMissingResidues()
    # 1N1A is missing 72–75. Do not homology-model that loop on the first run:
    # Phase 1 docked the apo gap. Modelling it would change the receptor.
    fixer.missingResidues = {}
    fixer.findNonstandardResidues()
    fixer.replaceNonstandardResidues()
    fixer.removeHeterogens(keepWater=False)
    fixer.findMissingAtoms()
    fixer.addMissingAtoms()
    fixer.addMissingHydrogens(7.4)
    return fixer


def run_system(system_id: str, ns: float, outdir: Path, seed: int) -> None:
    if not HAS_OPENMM:
        raise RuntimeError(
            "OpenMM stack not installed. On the GPU box: conda install -c conda-forge "
            "openmm openff-toolkit openmmforcefields pdbfixer mdtraj numpy"
        )
    if system_id not in SYSTEMS:
        raise KeyError(f"unknown system {system_id}; choose from {sorted(SYSTEMS)}")
    spec = SYSTEMS[system_id]
    outdir.mkdir(parents=True, exist_ok=True)

    ligand = _ligand_molecule(spec)
    fixer = _fixed_protein(spec["protein"])

    modeller = app.Modeller(fixer.topology, fixer.positions)
    off_top = ligand.to_topology()
    modeller.add(off_top.to_openmm(), ligand.conformers[0].to_openmm())

    generator = SystemGenerator(
        forcefields=["amber14-all.xml", "amber14/tip3pfb.xml"],
        small_molecule_forcefield="openff-2.2.1",
        molecules=[ligand],
        forcefield_kwargs={
            "constraints": app.HBonds,
            "rigidWater": True,
            "removeCMMotion": False,
            "hydrogenMass": 1.5 * unit.amu,
        },
    )
    modeller.addSolvent(
        generator.forcefield,
        model="tip3pfb",
        padding=1.2 * unit.nanometer,
        ionicStrength=0.15 * unit.molar,
        neutralize=True,
    )
    system = generator.create_system(modeller.topology)
    system.addForce(MonteCarloBarostat(1.0 * unit.bar, 300.0 * unit.kelvin))

    integrator = LangevinMiddleIntegrator(
        300.0 * unit.kelvin, 1.0 / unit.picosecond, 4.0 * unit.femtoseconds
    )
    integrator.setRandomNumberSeed(seed)
    platform = Platform.getPlatformByName("CUDA")
    simulation = app.Simulation(modeller.topology, system, integrator, platform)
    simulation.context.setPositions(modeller.positions)

    pdb_out = outdir / f"{system_id}_solvated.pdb"
    with pdb_out.open("w") as handle:
        app.PDBFile.writeFile(modeller.topology, modeller.positions, handle)

    print(f"[{system_id}] minimizing", flush=True)
    simulation.minimizeEnergy(maxIterations=5000)
    simulation.context.setVelocitiesToTemperature(300.0 * unit.kelvin, seed)

    dcd = outdir / f"{system_id}_prod.dcd"
    log = outdir / f"{system_id}.log"
    simulation.reporters.append(app.DCDReporter(str(dcd), 25000))  # 100 ps @ 4 fs
    simulation.reporters.append(
        app.StateDataReporter(
            str(log),
            25000,
            step=True,
            time=True,
            potentialEnergy=True,
            temperature=True,
            volume=True,
            speed=True,
        )
    )
    chk = outdir / f"{system_id}.chk"
    simulation.reporters.append(app.CheckpointReporter(str(chk), 250000))  # 1 ns

    # Short NPT equilibration (1 ns) before production.
    eq_steps = int(1.0 * unit.nanoseconds / (4.0 * unit.femtoseconds))
    print(f"[{system_id}] NPT equilibration {eq_steps} steps", flush=True)
    simulation.step(eq_steps)

    prod_steps = int(ns * unit.nanoseconds / (4.0 * unit.femtoseconds))
    print(f"[{system_id}] production {ns} ns = {prod_steps} steps", flush=True)
    simulation.step(prod_steps)

    state = simulation.context.getState(getPositions=True)
    with (outdir / f"{system_id}_final.pdb").open("w") as handle:
        app.PDBFile.writeFile(simulation.topology, state.getPositions(), handle)
    with (outdir / f"{system_id}_system.xml").open("w") as handle:
        handle.write(XmlSerializer.serialize(system))
    print(f"[{system_id}] done → {outdir}", flush=True)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="validate inputs and print the package; no MD, no GPU",
    )
    parser.add_argument("--system", choices=sorted(SYSTEMS), help="P2-A system id")
    parser.add_argument(
        "--ns",
        type=float,
        default=100.0,
        help="production length in nanoseconds (default 100)",
    )
    parser.add_argument(
        "--outdir",
        type=Path,
        default=Path("phase2-runs"),
        help="output directory for this job",
    )
    parser.add_argument("--seed", type=int, default=20260912)
    parser.add_argument(
        "--i-understand-this-spends-gpu-budget",
        action="store_true",
        help="required to start production; confirms human budget approval",
    )
    args = parser.parse_args(argv)

    if args.dry_run or args.system is None:
        print(json.dumps(dry_run(), indent=2))
        return 0 if dry_run()["ok"] else 1

    if not args.i_understand_this_spends_gpu_budget:
        print(
            "Refusing to start production MD. Human budget approval is required.\n"
            "Re-run with --i-understand-this-spends-gpu-budget only after that approval.",
            file=sys.stderr,
        )
        return 3

    run_system(args.system, args.ns, args.outdir, args.seed)
    return 0


if __name__ == "__main__":
    sys.exit(main())
