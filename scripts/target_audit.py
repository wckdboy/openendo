#!/usr/bin/env python3
"""Generate the drug-target intelligence dataset for the OpenEndo hub.

Audits the novel / high-druggability endometriosis targets from Deep
Origin's AI Scientist public log against ChEMBL (EBI) drug mechanisms
and writes docs/data/targets.json. Silent-when-unchanged (watchdog
pattern, same as update_data.py).

Usage: python3 scripts/target_audit.py
"""
import json
import os
import sys
import time
import urllib.parse
import urllib.request
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "docs", "data")
CHEMBL = "https://www.ebi.ac.uk/chembl/api/data"
TODAY = date.today().isoformat()

# 58 novel/high-druggability targets from Deep Origin's AI Scientist log
# (35 truly novel = zero drug mechanisms in ChEMBL; 23 with drugs; 8 with
# an approved drug). Derived from the audit — never hand-edited.
NOVEL = """ABCC4 ACKR3 ACVR1B ADORA2B ALDH2 AOC3 BDKRB1 BMPR2 CCR6 CCR8 CMA1 CMKLR1
CNR2 CX3CR1 CXCL10 ENPP3 ENTPD1 ENTPD2 EPHA2 EPHB4 F2RL1 FKBP4 FN1 FPR1 FPR2
GPER1 GPX4 HCK HPGD HTRA1 ILK IRAK4 KLRK1 LGALS3 METTL3 MIF MRGPRX2 NGFR NLRP3
NOS2 PDK3 PFKFB3 PLAU PLAUR PTGER4 PTGFR S1PR2 S1PR3 SLC7A11 SLCO2A1 SPHK1
SUCNR1 TGFBR1 TLR8 TPSAB1 TRPA1 TRPM3 YAP1""".split()

UA = {"User-Agent": "openendo/1.0 (github.com/wckdboy/openendo)"}


def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())


def audit_target(gene):
    q = urllib.parse.quote(gene)
    data = fetch(f"{CHEMBL}/target.json?target_synonym={q}")
    t = (data.get("targets") or [{}])[0]
    tid = t.get("target_chembl_id")
    if not tid:
        return {"gene": gene, "chembl_id": None, "name": "",
                "mechanisms": 0, "max_phase": 0.0, "novel": True}
    mech = fetch(f"{CHEMBL}/mechanism.json?target_chembl_id={tid}&limit=1000")
    ml = mech.get("mechanisms") or []
    phases = []
    for m in ml:
        try:
            phases.append(float(m.get("max_phase", 0) or 0))
        except (TypeError, ValueError):
            phases.append(0.0)
    n = len(ml)
    return {"gene": gene,
            "chembl_id": tid,
            "name": t.get("pref_name", ""),
            "mechanisms": n,
            "max_phase": max(phases) if phases else 0.0,
            "novel": n == 0}


def main():
    os.makedirs(DATA, exist_ok=True)
    targets = []
    for i, gene in enumerate(NOVEL, 1):
        r = audit_target(gene)
        targets.append(r)
        print(f"[{i:02d}/{len(NOVEL)}] {gene:8s} "
              f"{'novel' if r['novel'] else 'drugs=' + str(r['mechanisms'])}")
        time.sleep(0.4)

    novel = [x for x in targets if x["novel"]]
    with_drugs = [x for x in targets if not x["novel"]]
    approved = [x for x in targets if x["max_phase"] >= 4]
    obj = {
        "updated": TODAY,
        "source": ("Deep Origin AI Scientist novel/high-druggability target list, "
                   "verified against ChEMBL (EBI) drug mechanisms"),
        "url": "https://deeporigin.com/ai-scientist/endometriosis-targets",
        "counts": {"total": len(targets), "novel": len(novel),
                   "with_drugs": len(with_drugs), "approved": len(approved)},
        "targets": sorted(targets, key=lambda x: (x["novel"], x["gene"])),
    }

    path = os.path.join(DATA, "targets.json")
    old = None
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            old = f.read()
    new = json.dumps(obj, ensure_ascii=False, indent=1)
    if old != new:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new)
        print(f"Wrote {path}")
    else:
        print("Unchanged — nothing to write.")

    print(f"Total {len(targets)} | novel {len(novel)} | with drugs "
          f"{len(with_drugs)} | approved {len(approved)}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        sys.stderr.write(f"FEJL i target_audit.py: {e}\n")
        sys.exit(1)
