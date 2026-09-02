#!/usr/bin/env python3
"""repurpose_screen.py — M3 v1: approved drugs with measured activity
against the novel endometriosis targets.

For each of the 35 novel targets (zero drug MECHANISMS in ChEMBL):
  1. fetch potent activities (pchembl_value >= 6) from ChEMBL
  2. for each active molecule, look up whether it is an approved drug
     (max_phase == 4)
Output: docs/data/repurposing_candidates.json + printed summary.

Aligns with OpenEndo agenda track "Drug repurposing" (the simvastatin /
primaquine finding, PMID 42668641, is the template we extend).

Usage: python3 scripts/repurpose_screen.py [--pchembl 6]
"""
import argparse
import json
import os
import sys
import time
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "docs", "data")
CHEMBL = "https://www.ebi.ac.uk/chembl/api/data"
UA = {"User-Agent": "openendo/1.0 (github.com/wckdboy/openendo; repurpose)"}

NOVEL = """ABCC4 ACKR3 ACVR1B AOC3 CCR6 CCR8 CMKLR1 CX3CR1 ENTPD1 ENTPD2 F2RL1 FKBP4
FPR1 FPR2 GPER1 GPX4 HPGD HTRA1 ILK KLRK1 METTL3 MRGPRX2 NGFR PDK3 PFKFB3
PLAUR S1PR2 S1PR3 SLC7A11 SLCO2A1 SPHK1 SUCNR1 TPSAB1 TRPM3 YAP1""".split()


def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())


def target_id(gene):
    q = urllib.parse.quote(gene)
    d = fetch(f"{CHEMBL}/target.json?target_synonym={q}")
    return (d.get("targets") or [{}])[0].get("target_chembl_id")


def active_molecules(tid, pchembl):
    d = fetch(f"{CHEMBL}/activity.json?target_chembl_id={tid}"
              f"&pchembl_value__gte={pchembl}&limit=100")
    out = {}
    for a in d.get("activities") or []:
        mid = a.get("molecule_chembl_id")
        if not mid:
            continue
        pc = a.get("pchembl_value")
        if pc is not None and (mid not in out or float(pc) > out[mid]):
            out[mid] = float(pc)
    return out


def drug_info(mid):
    """Return (name, max_phase) for a molecule, or None if not a drug."""
    try:
        d = fetch(f"{CHEMBL}/drug.json?molecule_chembl_id={mid}&limit=1")
        drugs = d.get("drugs") or []
        if not drugs:
            return None
        dr = drugs[0]
        phase = dr.get("max_phase")
        return dr.get("pref_name") or dr.get("molecule_chembl_id"), \
            float(phase) if phase is not None else 0.0
    except Exception:
        return None


def molecule_name(mid):
    """Best-effort human-readable name for a molecule."""
    try:
        d = fetch(f"{CHEMBL}/molecule.json?molecule_chembl_id={mid}&limit=1")
        m = (d.get("molecules") or [{}])[0]
        return m.get("pref_name") or m.get("molecule_chembl_id")
    except Exception:
        return mid


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pchembl", type=float, default=6.0,
                    help="potency cutoff (default 6.0 = 1 uM)")
    ap.add_argument("--out", default=os.path.join(DATA, "repurposing_candidates.json"))
    args = ap.parse_args()

    candidates = []   # approved drugs active against >=1 novel target
    per_target = {}
    seen_molecules = {}

    for i, gene in enumerate(NOVEL, 1):
        tid = target_id(gene)
        if not tid:
            per_target[gene] = {"chembl": None, "candidates": []}
            print(f"[{i:02d}/{len(NOVEL)}] {gene:8s} ingen ChEMBL-target")
            continue
        mols = active_molecules(tid, args.pchembl)
        hits = []
        for mid, pc in mols.items():
            if mid in seen_molecules:
                info = seen_molecules[mid]
            else:
                info = drug_info(mid)
                seen_molecules[mid] = info
                time.sleep(0.3)
            if info and info[1] >= 4:  # approved
                hits.append({"molecule": mid, "name": molecule_name(mid),
                             "pchembl": pc, "phase": info[1]})
        per_target[gene] = {"chembl": tid,
                            "potent_actives": len(mols),
                            "candidates": hits}
        for h in hits:
            candidates.append({"target": gene, "target_chembl": tid, **h})
        n = len(hits)
        print(f"[{i:02d}/{len(NOVEL)}] {gene:8s} {len(mols):3d} potente "
              f"aktive -> {n} godkendte lægemidler")
        time.sleep(0.4)

    obj = {
        "updated": time.strftime("%Y-%m-%d"),
        "pipeline": "ChEMBL activity + drug max_phase join (repurpose_screen.py)",
        "pchembl_cutoff": args.pchembl,
        "note": ("Approved drugs (max_phase 4) with measured potency against "
                 "a novel endometriosis target. Hypothesis-generation only."),
        "per_target": per_target,
        "candidates": candidates,
    }
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)

    by_drug = {}
    for c in candidates:
        by_drug.setdefault(c["name"], []).append(c["target"])
    print(f"\n{len(candidates)} kandidat-par (godkendt lægemiddel × target)")
    print(f"{len(by_drug)} unikke godkendte lægemidler med aktivitet mod "
          f"novelle targets:")
    for name, tgts in sorted(by_drug.items(), key=lambda kv: -len(kv[1])):
        print(f"  {name:35s} -> {', '.join(sorted(tgts))}")
    print(f"\nWrote {args.out}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        sys.stderr.write(f"FEJL i repurpose_screen.py: {e}\n")
        sys.exit(1)
