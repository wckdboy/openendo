#!/usr/bin/env python3
"""analyze_structure.py — extract confidence + geometry from folded structures.

AlphaFold outputs carry per-residue pLDDT confidence in the B-factor column
(and pLDDT in the mmCIF _atom_site.B_iso_or_equiv field). This script reads
folded structures (PDB or mmCIF), computes per-target summary stats and
writes a single summary.json.

Also integrates FPocket for pocket detection when the binary is available
(installed separately; see README) — otherwise records pockets as "manual".

Usage:
    python3 scripts/analyze_structure.py <structure> [<structure> ...] [-o out.json]
"""
import argparse
import json
import os
import shutil
import statistics
import subprocess
import sys
import tempfile

try:
    from Bio.PDB import MMCIFParser, PDBParser
    from Bio.PDB.MMCIFParser import MMCIF2Dict  # noqa: F401  (probe)
except ImportError:
    sys.stderr.write("Biopython missing — pip install biopython\n")
    sys.exit(1)


def parse_structure(path):
    """Return list of residue dicts: {resnum, plddt} for first chain."""
    if path.endswith(".cif") or path.endswith(".mmcif"):
        parser = MMCIFParser(QUIET=True)
    else:
        parser = PDBParser(QUIET=True)
    try:
        s = parser.get_structure("s", path)
    except Exception as e:
        return None, str(e)
    residues = []
    for model in s:
        for chain in model:
            for res in chain:
                bfactors = [a.bfactor for a in res if a.bfactor is not None]
                if bfactors:
                    residues.append({"resnum": res.id[1],
                                     "plddt": round(statistics.mean(bfactors), 1)})
            if residues:
                break  # first chain only
        if residues:
            break
    return residues, None


def plddt_quality(plddts):
    """AF confidence bands (per AF3 docs): very high >90, high 70-90,
    low 50-70, very low <50."""
    if not plddts:
        return {}
    n = len(plddts)
    return {
        "very_high_p90": round(sum(1 for x in plddts if x > 90) / n * 100, 1),
        "high_70_90": round(sum(1 for x in plddts if 70 < x <= 90) / n * 100, 1),
        "low_50_70": round(sum(1 for x in plddts if 50 < x <= 70) / n * 100, 1),
        "very_low_p50": round(sum(1 for x in plddts if x <= 50) / n * 100, 1),
        "mean_plddt": round(statistics.mean(plddts), 1),
    }


def fpocket_pockets(cif_path):
    """Run FPocket on a structure if available; return pocket count or None."""
    if not shutil.which("fpocket"):
        return None
    with tempfile.TemporaryDirectory() as td:
        out = os.path.join(td, "out")
        r = subprocess.run(["fpocket", "-f", cif_path, "-o", out],
                           capture_output=True, text=True)
        if r.returncode != 0:
            return -1
        info = os.path.join(out, os.path.basename(cif_path) + "_info.txt")
        if not os.path.exists(info):
            return -1
        n = 0
        for line in open(info):
            if line.startswith("Pocket "):
                n += 1
        return n


def main():
    ap = argparse.ArgumentParser(description="Analyze folded structures")
    ap.add_argument("structures", nargs="+")
    ap.add_argument("-o", default="docs/research/structures/results/summary.json")
    args = ap.parse_args()

    os.makedirs(os.path.dirname(args.o) or ".", exist_ok=True)
    summary = {"pipeline": "analyze_structure.py", "entries": []}
    for path in args.structures:
        name = os.path.splitext(os.path.basename(path))[0].replace("_model", "")
        residues, err = parse_structure(path)
        if err or not residues:
            summary["entries"].append(
                {"target": name, "status": f"error: {err}"})
            print(f"{name:10s} FEJL: {err}")
            continue
        plddts = [r["plddt"] for r in residues]
        entry = {
            "target": name, "status": "ok",
            "file": os.path.basename(path),
            "residues": len(residues),
            **plddt_quality(plddts),
        }
        pockets = fpocket_pockets(path)
        if pockets is not None:
            entry["fpocket_pockets"] = pockets
        summary["entries"].append(entry)
        print(f"{name:10s} {len(residues):4d} res | mean pLDDT "
              f"{entry['mean_plddt']:5.1f} | >90: {entry['very_high_p90']:5.1f}%"
              + (f" | pockets: {pockets}" if pockets is not None else ""))

    with open(args.o, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=1)
    print(f"\nWrote {args.o}")


if __name__ == "__main__":
    main()
