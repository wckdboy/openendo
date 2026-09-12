#!/usr/bin/env python3
"""Phase 2 prep — convert Phase 1 PDBQT poses and assemble FKBP complexes.

CPU-only. No GPU, no cloud spend. Regenerates files under
docs/research/virtual/phase2/inputs/.

Usage:
  python3 scripts/phase2_prep.py --check
  python3 scripts/phase2_prep.py --assemble --pdb-cache /tmp/phase2-pdb
"""
from __future__ import annotations

import argparse
import json
import math
import re
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
PHASE1_POSES = ROOT / "docs" / "research" / "virtual" / "phase1" / "poses"
PHASE2 = ROOT / "docs" / "research" / "virtual" / "phase2"
INPUTS = PHASE2 / "inputs"
LIGAND_DIR = INPUTS / "ligands"
RECEPTOR_DIR = INPUTS / "receptors"
COMPLEX_DIR = INPUTS / "complexes"
IDX_DIR = INPUTS / "smiles_idx"

# Autodock atom type → element (meeko / Vina PDBQT).
AD_TYPE_ELEMENT = {
    "H": "H",
    "HD": "H",
    "HS": "H",
    "C": "C",
    "A": "C",
    "CG0": "C",  # meeko macrocycle-typed carbon
    "N": "N",
    "NA": "N",
    "NS": "N",
    "O": "O",
    "OA": "O",
    "OS": "O",
    "S": "S",
    "SA": "S",
    "P": "P",
    "F": "F",
    "CL": "CL",
    "BR": "BR",
    "I": "I",
    "MG": "MG",
    "MN": "MN",
    "ZN": "ZN",
    "CA": "CA",
    "FE": "FE",
}
# meeko dummy atoms used only for macrocycle ring-closure (not real chemistry)
DUMMY_AD_TYPES = {"G0"}

# Phase 1 docked FKBP52 against 1N1A superposed onto 1FKB using contact-defined
# pocket pairs (phase1.md: 14 pairs, 0.80 Å). Public 1N1A is missing residues
# 72–75 (the Arg42-loop homolog), so those pairs cannot be reproduced. The 11
# pairs below are present in both deposited structures and cover the named
# Phase 1 pocket (Tyr57/Phe67/Phe77/Val86/Ile87/Trp90/Tyr113).
POCKET_PAIRS = [
    # (1N1A resi, 1FKB resi, expected 3-letter name on both)
    (57, 26, "TYR"),
    (67, 36, "PHE"),
    (68, 37, "ASP"),
    (77, 46, "PHE"),
    (85, 54, "GLU"),
    (86, 55, "VAL"),
    (87, 56, "ILE"),
    (90, 59, "TRP"),
    (113, 82, "TYR"),
    (122, 90, "ILE"),
    (130, 99, "PHE"),
]

POSE_INVENTORY = [
    {
        "id": "sulfasalazine_xct",
        "pdbqt": "sulfasalazine_xct_top.pdbqt",
        "expected_atoms": 31,
        "vina_kcal": -8.524,
        "role": "watchlist_target",
    },
    {
        "id": "rapamycin_fkbp52",
        "pdbqt": "rapamycin_fkbp52_top.pdbqt",
        "expected_atoms": 68,  # 70 PDBQT records minus 2 meeko G0 dummies
        "vina_kcal": -6.378,
        "role": "top_tier_hypothesis",
    },
    {
        "id": "rapamycin_fkbp12_calib",
        "pdbqt": "rapamycin_fkbp12_calib_top.pdbqt",
        "expected_atoms": 68,
        "vina_kcal": -7.063,
        "role": "selectivity_control_vina",
    },
    {
        "id": "j9o_xct_calib",
        "pdbqt": "j9o_xct_calib_top.pdbqt",
        "expected_atoms": 39,
        "vina_kcal": -9.354,
        "role": "xct_native_calib",
    },
]


def _ad_element(token: str) -> str:
    key = token.strip().upper()
    if key in AD_TYPE_ELEMENT:
        return AD_TYPE_ELEMENT[key]
    if len(key) <= 2 and key.isalpha():
        return key
    raise ValueError(f"unrecognized Autodock atom type {token!r}")


def parse_pdbqt(path: Path) -> dict:
    """Parse a meeko/Vina PDBQT (ligand-only MODEL 1) into atoms + remarks."""
    smiles = None
    idx_pairs: list[tuple[int, int]] = []
    vina = None
    atoms = []
    with path.open() as handle:
        for raw in handle:
            line = raw.rstrip("\n")
            if line.startswith("REMARK VINA RESULT:"):
                parts = line.split()
                vina = float(parts[3])
            elif line.startswith("REMARK SMILES ") and not line.startswith(
                "REMARK SMILES IDX"
            ):
                smiles = line.split("REMARK SMILES ", 1)[1].strip()
            elif line.startswith("REMARK SMILES IDX"):
                nums = [int(x) for x in line.split()[3:]]
                if len(nums) % 2:
                    raise ValueError(f"{path}: odd SMILES IDX token count")
                idx_pairs.extend(zip(nums[0::2], nums[1::2], strict=True))
            elif line.startswith(("ATOM  ", "HETATM")):
                serial = int(line[6:11])
                name = line[12:16]
                x = float(line[30:38])
                y = float(line[38:46])
                z = float(line[46:54])
                tail = line[66:].split()
                if len(tail) < 2:
                    raise ValueError(f"{path}: ATOM line missing charge/type: {line}")
                charge = float(tail[0])
                ad_type = tail[-1]
                if ad_type.upper() in DUMMY_AD_TYPES:
                    continue
                element = _ad_element(ad_type)
                atoms.append(
                    {
                        "serial": serial,
                        "name": name,
                        "x": x,
                        "y": y,
                        "z": z,
                        "charge": charge,
                        "element": element,
                        "ad_type": ad_type,
                    }
                )
    if not atoms:
        raise ValueError(f"{path}: no ATOM records")
    return {
        "smiles": smiles,
        "smiles_idx": [{"smiles_atom": s, "pdbqt_serial": p} for s, p in idx_pairs],
        "vina_kcal": vina,
        "atoms": atoms,
    }


def atoms_to_pdb(atoms: list[dict], resname: str = "UNL", chain: str = "L") -> str:
    lines = ["REMARK  OpenEndo Phase 2 ligand converted from Phase 1 PDBQT"]
    for i, atom in enumerate(atoms, start=1):
        element = atom["element"]
        lines.append(
            f"HETATM{i:5d} {atom['name']}{resname:3s} {chain}{1:4d}    "
            f"{atom['x']:8.3f}{atom['y']:8.3f}{atom['z']:8.3f}"
            f"  1.00  0.00          {element:>2s}"
        )
    lines.append("END")
    return "\n".join(lines) + "\n"


def centroid(atoms: list[dict]) -> tuple[float, float, float]:
    xs = [a["x"] for a in atoms]
    ys = [a["y"] for a in atoms]
    zs = [a["z"] for a in atoms]
    n = len(atoms)
    return (sum(xs) / n, sum(ys) / n, sum(zs) / n)


def parse_pdb_atoms(path: Path, record=("ATOM  ",), chain=None, heavy_only=True):
    atoms = []
    with path.open() as handle:
        for line in handle:
            if not line.startswith(record):
                continue
            ch = line[21]
            if chain is not None and ch != chain:
                continue
            name = line[12:16].strip()
            element = line[76:78].strip().upper() if len(line) >= 78 else ""
            if not element:
                element = re.sub(r"\d+", "", name)[:2].upper()
            if heavy_only and element == "H":
                continue
            atoms.append(
                {
                    "line": line[:80].ljust(80),
                    "name": name,
                    "resname": line[17:20].strip(),
                    "resi": int(line[22:26]),
                    "chain": ch,
                    "element": element,
                    "xyz": np.array(
                        [float(line[30:38]), float(line[38:46]), float(line[46:54])]
                    ),
                }
            )
    return atoms


def ca_of(atoms, resi: int, resname: str):
    hits = [
        a
        for a in atoms
        if a["name"] == "CA" and a["resi"] == resi and a["resname"] == resname
    ]
    if len(hits) != 1:
        raise ValueError(f"expected 1 CA {resname} {resi}, got {len(hits)}")
    return hits[0]["xyz"]


def kabsch(mobile: np.ndarray, target: np.ndarray) -> tuple[np.ndarray, np.ndarray, float]:
    """Rotate/translate mobile onto target. Returns R, t, RMSD (Å)."""
    if mobile.shape != target.shape or mobile.shape[0] < 3:
        raise ValueError("Kabsch needs ≥3 matched coordinates")
    c_m = mobile.mean(axis=0)
    c_t = target.mean(axis=0)
    h = (mobile - c_m).T @ (target - c_t)
    u, _s, vt = np.linalg.svd(h)
    r = vt.T @ u.T
    if np.linalg.det(r) < 0:
        vt = vt.copy()
        vt[-1, :] *= -1
        r = vt.T @ u.T
    t = c_t - r @ c_m
    fitted = (r @ mobile.T).T + t
    rmsd = float(math.sqrt(((fitted - target) ** 2).sum() / len(target)))
    return r, t, rmsd


def apply_rt(xyz: np.ndarray, r: np.ndarray, t: np.ndarray) -> np.ndarray:
    return (r @ xyz.T).T + t


def write_protein_pdb(atoms, path: Path, remark: str) -> None:
    lines = [f"REMARK  {remark}"]
    for i, atom in enumerate(atoms, start=1):
        xyz = atom["xyz"]
        src = atom["line"]
        lines.append(
            f"ATOM  {i:5d}{src[11:22]}{src[22:26]}    "
            f"{xyz[0]:8.3f}{xyz[1]:8.3f}{xyz[2]:8.3f}"
            f"  1.00  0.00          {atom['element']:>2s}"
        )
    lines.append("END")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n")


def convert_poses() -> list[dict]:
    LIGAND_DIR.mkdir(parents=True, exist_ok=True)
    IDX_DIR.mkdir(parents=True, exist_ok=True)
    reports = []
    for item in POSE_INVENTORY:
        src = PHASE1_POSES / item["pdbqt"]
        if not src.is_file():
            raise FileNotFoundError(src)
        parsed = parse_pdbqt(src)
        if len(parsed["atoms"]) != item["expected_atoms"]:
            raise ValueError(
                f"{src.name}: atom count {len(parsed['atoms'])} != {item['expected_atoms']}"
            )
        if parsed["vina_kcal"] is None or abs(parsed["vina_kcal"] - item["vina_kcal"]) > 0.02:
            raise ValueError(
                f"{src.name}: Vina score {parsed['vina_kcal']} != {item['vina_kcal']}"
            )
        pdb_name = item["pdbqt"].replace(".pdbqt", ".pdb")
        dest = LIGAND_DIR / pdb_name
        dest.write_text(atoms_to_pdb(parsed["atoms"]))
        idx_path = IDX_DIR / f"{item['id']}.json"
        idx_path.write_text(
            json.dumps(
                {
                    "id": item["id"],
                    "source_pdbqt": str(src.relative_to(ROOT)),
                    "smiles": parsed["smiles"],
                    "smiles_idx": parsed["smiles_idx"],
                    "vina_kcal": parsed["vina_kcal"],
                    "n_atoms": len(parsed["atoms"]),
                    "centroid_A": [round(x, 3) for x in centroid(parsed["atoms"])],
                },
                indent=2,
            )
            + "\n"
        )
        reports.append(
            {
                **item,
                "pdb": str(dest.relative_to(ROOT)),
                "n_atoms": len(parsed["atoms"]),
                "centroid_A": [round(x, 3) for x in centroid(parsed["atoms"])],
                "smiles": parsed["smiles"],
            }
        )
    return reports


def assemble_fkbp(pdb_cache: Path) -> dict:
    fkb = pdb_cache / "1FKB.pdb"
    n1a = pdb_cache / "1N1A.pdb"
    if not fkb.is_file() or not n1a.is_file():
        raise FileNotFoundError(
            f"need {fkb} and {n1a} — fetch from RCSB (CC0): "
            "https://files.rcsb.org/download/1FKB.pdb and 1N1A.pdb"
        )
    rec_1fkb = parse_pdb_atoms(fkb, chain="A", heavy_only=True)
    rec_1n1a = parse_pdb_atoms(n1a, chain="A", heavy_only=True)
    mobile = np.stack([ca_of(rec_1n1a, a, name) for a, _b, name in POCKET_PAIRS])
    target = np.stack([ca_of(rec_1fkb, b, name) for _a, b, name in POCKET_PAIRS])
    rot, trans, pocket_rmsd = kabsch(mobile, target)
    for atom in rec_1n1a:
        atom["xyz"] = apply_rt(atom["xyz"][None, :], rot, trans)[0]

    RECEPTOR_DIR.mkdir(parents=True, exist_ok=True)
    COMPLEX_DIR.mkdir(parents=True, exist_ok=True)
    write_protein_pdb(
        rec_1fkb,
        RECEPTOR_DIR / "1FKB_A_protein.pdb",
        "1FKB chain A protein heavy atoms (waters/RAP stripped). RCSB CC0.",
    )
    write_protein_pdb(
        rec_1n1a,
        RECEPTOR_DIR / "1N1A_A_aligned_to_1FKB.pdb",
        "1N1A chain A (FK1) aligned onto 1FKB via 11 pocket CA pairs. RCSB CC0.",
    )

    rap = parse_pdb_atoms(
        fkb, record=("HETATM",), chain="A", heavy_only=True
    )
    rap = [a for a in rap if a["resname"] == "RAP"]
    if len(rap) < 40:
        raise ValueError(f"1FKB RAP heavy atoms unexpectedly few: {len(rap)}")
    crystal_lig = LIGAND_DIR / "rapamycin_1fkb_crystal.pdb"
    crystal_atoms = [
        {
            "name": f"{a['name']:4s}",
            "x": float(a["xyz"][0]),
            "y": float(a["xyz"][1]),
            "z": float(a["xyz"][2]),
            "element": a["element"],
        }
        for a in rap
    ]
    crystal_lig.write_text(atoms_to_pdb(crystal_atoms, resname="RAP", chain="L"))

    vina_fkbp12 = parse_pdbqt(PHASE1_POSES / "rapamycin_fkbp12_calib_top.pdbqt")
    vina_cent = np.array(centroid(vina_fkbp12["atoms"]))
    crystal_cent = np.array(centroid(crystal_atoms))
    centroid_delta = float(np.linalg.norm(vina_cent - crystal_cent))

    def _combine(protein_atoms, ligand_pdb: Path, dest: Path, remark: str) -> None:
        protein_block = [
            line
            for line in (RECEPTOR_DIR / protein_atoms).read_text().splitlines()
            if line.startswith("ATOM  ")
        ]
        lig_block = [
            line.replace("HETATM", "HETATM")
            for line in ligand_pdb.read_text().splitlines()
            if line.startswith("HETATM")
        ]
        dest.write_text(
            f"REMARK  {remark}\n" + "\n".join(protein_block + lig_block) + "\nEND\n"
        )

    _combine(
        "1FKB_A_protein.pdb",
        crystal_lig,
        COMPLEX_DIR / "p2a_fkbp12_crystal_rap.pdb",
        "P2-A protocol control: 1FKB + deposited RAP.",
    )
    _combine(
        "1FKB_A_protein.pdb",
        LIGAND_DIR / "rapamycin_fkbp12_calib_top.pdb",
        COMPLEX_DIR / "p2a_fkbp12_vina_rap.pdb",
        "P2-A optional: 1FKB + Phase 1 Vina RAP pose.",
    )
    _combine(
        "1N1A_A_aligned_to_1FKB.pdb",
        LIGAND_DIR / "rapamycin_fkbp52_top.pdb",
        COMPLEX_DIR / "p2a_fkbp52_vina_rap.pdb",
        "P2-A hypothesis: aligned 1N1A FK1 + Phase 1 Vina RAP pose.",
    )

    return {
        "pocket_pairs_used": len(POCKET_PAIRS),
        "pocket_ca_rmsd_A": round(pocket_rmsd, 3),
        "phase1_reported_rmsd_A": 0.80,
        "note": (
            "1N1A residues 72-75 are absent in the deposited structure, so the "
            "Phase 1 14-pair list cannot be reproduced exactly. 11 present "
            "homolog CAs were used."
        ),
        "vina_vs_crystal_centroid_delta_A": round(centroid_delta, 3),
        "receptors": [
            "docs/research/virtual/phase2/inputs/receptors/1FKB_A_protein.pdb",
            "docs/research/virtual/phase2/inputs/receptors/1N1A_A_aligned_to_1FKB.pdb",
        ],
        "complexes": [
            "docs/research/virtual/phase2/inputs/complexes/p2a_fkbp12_crystal_rap.pdb",
            "docs/research/virtual/phase2/inputs/complexes/p2a_fkbp12_vina_rap.pdb",
            "docs/research/virtual/phase2/inputs/complexes/p2a_fkbp52_vina_rap.pdb",
        ],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="convert poses, verify inventory, write ligand PDBs",
    )
    parser.add_argument(
        "--assemble",
        action="store_true",
        help="also align 1N1A onto 1FKB and write P2-A complexes",
    )
    parser.add_argument(
        "--pdb-cache",
        type=Path,
        default=Path("/tmp/phase2-pdb"),
        help="directory containing 1FKB.pdb and 1N1A.pdb",
    )
    args = parser.parse_args(argv)
    if not (args.check or args.assemble):
        args.check = True

    reports = convert_poses()
    assembly = None
    if args.assemble:
        assembly = assemble_fkbp(args.pdb_cache)

    summary = {
        "ok": True,
        "phase1_poses": str(PHASE1_POSES.relative_to(ROOT)),
        "converted": reports,
        "assembly": assembly,
    }
    print(json.dumps(summary, indent=2))
    if assembly and assembly["pocket_ca_rmsd_A"] > 1.5:
        print("WARNING: pocket CA RMSD > 1.5 Å — inspect alignment", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
