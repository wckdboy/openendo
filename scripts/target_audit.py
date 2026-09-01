#!/usr/bin/env python3
"""Generate the drug-target intelligence dataset for the OpenEndo hub.

Queries ChEMBL (public REST API) for the novel / high-druggability
endometriosis targets identified by Deep Origin's AI Scientist, verifies
each against known drug mechanisms, and writes docs/data/targets.json.

Silent-when-unchanged (watchdog pattern): only writes when the data
actually differs from what is already published.

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

# Novel / high-druggability targets (Deep Origin AI Scientist, public log)
TARGETS = """MIF NOS2 SPHK1 CCR8 EPHB4 PTGER4 SLCO2A1 BDKRB1 CMA1 CNR2 ENPP3
NLRP3 TGFBR1 YAP1 ALDH2 FN1 GPX4 LGALS3 PTGFR SUCNR1 TRPA1 AOC3 CMKLR1 METTL3
S1PR3 ENTPD1 ILK SLC7A11 TLR8 ABCC4 ACVR1B BMPR2 F2RL1 FKBP4 FPR2 GPER1 HCK
IRAK4 S1PR2 ACKR3 HPGD PDK3 CX3CR1 ENTPD2 EPHA2 HTRA1 KLRK1 PFKFB3 PLAUR
TPSAB1 TRPM3 CCR6 CXCL10 MRGPRX2 ADORA2B NGFR PLAU FPR1""".split()

UA = {"User-Agent": "openendo/1.0 (github.com/wckdboy/openendo)"}


def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())


def audit_target(gene):
    """Return dict for one gene: ChEMBL target id, name, drug mechanisms."""
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
    for i, gene in enumerate(TARGETS, 1):
        r = audit_target(gene)
        targets.append(r)
        print(f"[{i:02d}/{len(TARGETS)}] {gene:8s} "
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
