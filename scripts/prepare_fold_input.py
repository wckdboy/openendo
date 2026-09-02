#!/usr/bin/env python3
"""prepare_fold_input.py — build the ready-to-fold input pack for M1.

For each NOVEL drug target (no known drug mechanisms in ChEMBL) from the
target audit, fetch the canonical reviewed human sequence from UniProt and
write:
  docs/research/structures/fold_input/<GENE>.fasta
  docs/research/structures/fold_input/manifest.json

Usage: python3 scripts/prepare_fold_input.py
"""
import json
import os
import sys
import time
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "docs", "research", "structures", "fold_input")
UA = {"User-Agent": "openendo/1.0 (github.com/wckdboy/openendo; M1 fold pack)"}
UNIPROT = "https://rest.uniprot.org/uniprotkb/search"

# Novel targets = zero drug mechanisms in ChEMBL (from the target audit,
# docs/data/targets.json after merge). Generated from the audited CSV —
# do not hand-edit; regenerate from the audit.
NOVEL = [g.strip() for g in """
ABCC4 ACKR3 ACVR1B AOC3 CCR6 CCR8 CMKLR1 CX3CR1 ENTPD1 ENTPD2 F2RL1 FKBP4
FPR1 FPR2 GPER1 GPX4 HPGD HTRA1 ILK KLRK1 METTL3 MRGPRX2 NGFR PDK3 PFKFB3
PLAUR S1PR2 S1PR3 SLC7A11 SLCO2A1 SPHK1 SUCNR1 TPSAB1 TRPM3 YAP1
""".split() if g.strip()]


def fetch(query, fmt, fields=None):
    params = {"query": query, "format": fmt}
    if fields:
        params["fields"] = fields
    url = UNIPROT + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode()


def uniprot_for(gene):
    q = f"gene_exact:{gene} AND organism_id:9606 AND reviewed:true"
    fasta = fetch(q, "fasta")
    if "No results" in fasta or not fasta.strip():
        # fallback: any human entry
        q2 = f"gene_exact:{gene} AND organism_id:9606"
        fasta = fetch(q2, "fasta")
        if "No results" in fasta or not fasta.strip():
            return None
        return fasta, "unreviewed-fallback"
    return fasta, "reviewed"


def parse_fasta(fasta):
    lines = fasta.strip().splitlines()
    header = lines[0][1:] if lines else ""
    seq = "".join(l.strip() for l in lines[1:] if not l.startswith(">"))
    acc = ""
    for part in header.split("|"):
        if part.startswith("sp|") or part.startswith("tr|"):
            acc = part.split("|")[1]
    return header, acc, len(seq)


def main():
    os.makedirs(OUT, exist_ok=True)
    manifest = {"updated": "", "source": "UniProtKB (reviewed human)",
                "folds": []}
    for i, gene in enumerate(NOVEL, 1):
        try:
            res = uniprot_for(gene)
            if not res:
                manifest["folds"].append(
                    {"gene": gene, "status": "no-uniprot-entry"})
                print(f"[{i:02d}/{len(NOVEL)}] {gene:8s} INGEN UniProt-post")
                continue
            fasta, provenance = res
            header, acc, ln = parse_fasta(fasta)
            with open(os.path.join(OUT, f"{gene}.fasta"), "w") as f:
                f.write(fasta)
            manifest["folds"].append({
                "gene": gene, "status": "ok", "uniprot": acc,
                "length": ln, "provenance": provenance,
                "file": f"{gene}.fasta",
            })
            print(f"[{i:02d}/{len(NOVEL)}] {gene:8s} {acc} len={ln} "
                  f"({provenance})")
        except Exception as e:
            manifest["folds"].append({"gene": gene, "status": f"error: {e}"})
            print(f"[{i:02d}/{len(NOVEL)}] {gene:8s} FEJL: {e}")
        time.sleep(0.5)

    with open(os.path.join(OUT, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=1)

    ok = [x for x in manifest["folds"] if x["status"] == "ok"]
    print(f"\n{len(ok)}/{len(NOVEL)} sequences ready — "
          f"{OUT}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        sys.stderr.write(f"FEJL i prepare_fold_input.py: {e}\n")
        sys.exit(1)
