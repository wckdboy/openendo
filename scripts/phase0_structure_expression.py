#!/usr/bin/env python3
"""Phase 0 — structure & expression coverage for OpenEndo virtual testing.

Checks:
1. AlphaFold DB coverage for the 35 M1 targets (UniProt accessions from fold_input FASTA)
2. RCSB PDB experimental structures (by UniProt accession) for key targets
3. GTEx median expression (Uterus / Ovary / Fallopian Tube) via GTEx Portal API v2
4. ChEMBL target existence for key targets + sirolimus/rapamycin mechanism

Writes docs/research/virtual/phase0.json
"""
import json
import os
import sys
import time
import gzip
import urllib.request
import urllib.parse
import urllib.error

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FASTA_DIR = os.path.join(ROOT, "docs", "research", "structures", "fold_input")
OUT = os.path.join(ROOT, "docs", "research", "virtual", "phase0.json")

KEY_TARGETS = {  # gene -> uniprot (M3-relevant + FKBP12 control)
    "FKBP4": "Q02790", "MRGPRX2": "Q96LB1", "SLC7A11": "Q9UPY5",
    "ACVR1B": "P36896", "GPER1": "Q99527", "SLCO2A1": "Q92959",
    "FKBP1A(FKBP12)": "P62942",
}

GTEX_TISSUES = ["Uterus", "Ovary", "Fallopian Tube"]


def get(url, timeout=40):
    req = urllib.request.Request(url, headers={"User-Agent": "OpenEndo-phase0/1.0 (research)"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode())


def fasta_targets():
    targets = {}
    for fn in sorted(os.listdir(FASTA_DIR)):
        if not fn.endswith(".fasta"):
            continue
        with open(os.path.join(FASTA_DIR, fn)) as f:
            head = f.readline().strip()
        gene = fn[:-6]
        acc = ""
        for part in head.split("|"):
            # UniProt canonical accession: [OPQ][0-9][A-Z0-9]{3}[0-9] (letters allowed in the middle 3 chars)
            if len(part) == 6 and part[0] in "OPQ" and part[1].isdigit() and part[5].isdigit():
                acc = part
                break
        targets[gene] = acc
    return targets


def afdb(acc):
    """Return AFDB entry status for a UniProt accession."""
    try:
        d = get(f"https://alphafold.ebi.ac.uk/api/prediction/{acc}")
        if isinstance(d, list) and d:
            e = d[0]
            return {"status": "afdb", "model_url": e.get("pdbUrl"), "uniprot": acc,
                    "created": e.get("entryPublicationDate", "")}
        return {"status": "none", "uniprot": acc}
    except urllib.error.HTTPError as e:
        return {"status": "missing" if e.code == 404 else f"error:{e.code}", "uniprot": acc}
    except Exception as e:
        return {"status": f"error:{type(e).__name__}", "uniprot": acc}


def rcsb(acc):
    """Count PDB polymer entities matching a UniProt accession (experimental structures)."""
    q = {
        "query": {
            "type": "terminal", "service": "text",
            "parameters": {
                "attribute": "rcsb_polymer_entity_container_identifiers.reference_sequence_identifiers.database_accession",
                "operator": "exact_match", "value": acc,
            },
        },
        "return_type": "polymer_entity",
        "request_options": {"paginate": {"start": 0, "rows": 3}},
    }
    try:
        req = urllib.request.Request("https://search.rcsb.org/rcsbsearch/v2/query",
                                     data=json.dumps(q).encode(),
                                     headers={"Content-Type": "application/json",
                                              "User-Agent": "OpenEndo-phase0/1.0"})
        with urllib.request.urlopen(req, timeout=40) as r:
            d = json.loads(r.read().decode())
        ids = [x.get("identifier", "") for x in d.get("result_set", [])]
        return {"count": d.get("total_count", len(ids)), "examples": ids[:3]}
    except Exception as e:
        return {"error": f"{type(e).__name__}: {e}"}


def ensembl_for(uniprot):
    try:
        d = get(f"https://mygene.info/v3/query?q=uniprot:{uniprot}&fields=ensembl.gene,symbol&species=human")
        hits = d.get("hits", [])
        for h in hits:
            eg = h.get("ensembl", {}).get("gene")
            if eg:
                return eg
        return None
    except Exception:
        return None


def hpa_summary(gene):
    """HPA RNA tissue specificity + distribution summary per gene."""
    url = ("https://www.proteinatlas.org/api/search_download.php?"
           f"search={urllib.parse.quote(gene)}&format=json&columns=g,eg,up,rnats,rdist")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "OpenEndo-phase0/1.0",
                                                   "Accept-Encoding": "identity"})
        with urllib.request.urlopen(req, timeout=60) as r:
            raw = r.read()
        try:
            data = json.loads(gzip.decompress(raw))
        except Exception:
            data = json.loads(raw)
        row = data[0] if data else {}
        return {"specificity": row.get("RNA tissue specificity"),
                "distribution": row.get("RNA tissue distribution")}
    except Exception as e:
        return {"error": f"{type(e).__name__}: {e}"}


def chembl_target(gene):
    try:
        d = get(f"https://www.ebi.ac.uk/chembl/api/data/target/search?q={gene}&format=json")
        hits = d.get("targets", [])
        human = [t for t in hits if t.get("organism") == "Homo sapiens"]
        return {"present": bool(human), "chembl_id": human[0]["target_chembl_id"] if human else None,
                "n_hits": len(hits)}
    except Exception as e:
        return {"error": str(e)}


def chembl_molecule_mechanism(name):
    try:
        d = get(f"https://www.ebi.ac.uk/chembl/api/data/molecule/search?q={urllib.parse.quote(name)}&format=json")
        mols = d.get("molecules", [])
        out = []
        for m in mols[:3]:
            mechs = m.get("molecule_mechanisms", [])
            out.append({"name": m.get("pref_name"), "chembl": m.get("molecule_chembl_id"),
                        "mechanisms": [{"target": x.get("target_name"), "action": x.get("mechanism_of_action"),
                                        "target_chembl": x.get("target_chembl_id")} for x in mechs[:3]]})
        return out
    except Exception as e:
        return {"error": str(e)}


def main():
    targets = fasta_targets()
    print(f"targets in fold_input: {len(targets)}")
    results = {"targets": targets, "checked": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
               "afdb": {}, "pdb": {}, "hpa": {}, "chembl": {}}

    # 1) AFDB for all 35
    for gene, acc in sorted(targets.items()):
        results["afdb"][gene] = afdb(acc)
        time.sleep(0.15)

    # 2) PDB for key targets
    for gene, acc in KEY_TARGETS.items():
        results["pdb"][gene] = rcsb(acc)
        time.sleep(0.3)

    # 3) HPA RNA tissue summary for key targets
    for gene in KEY_TARGETS:
        results["hpa"][gene] = hpa_summary(gene)
        time.sleep(0.4)

    # 4) ChEMBL
    for gene in ["FKBP4", "FKBP1A", "MRGPRX2", "SLC7A11", "ACVR1B"]:
        results["chembl"][gene] = chembl_target(gene)
        time.sleep(0.3)
    results["chembl"]["sirolimus_rapamycin"] = chembl_molecule_mechanism("rapamycin")
    results["chembl"]["cetrorelix"] = chembl_molecule_mechanism("cetrorelix")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(results, f, indent=1)
    print("wrote", OUT)

    # compact console summary
    afdb_ok = sum(1 for v in results["afdb"].values() if v.get("status") == "afdb")
    print(f"AFDB coverage: {afdb_ok}/{len(targets)}")
    print("PDB:", {k: (v.get('count'), v.get('examples', [])[:2]) for k, v in results['pdb'].items()})
    print("HPA:", {k: (v.get('specificity'), v.get('distribution')) for k, v in results['hpa'].items()})
    print("ChEMBL:", {k: (v.get('present'), v.get('chembl_id')) for k, v in results['chembl'].items() if isinstance(v, dict) and 'present' in v})


if __name__ == "__main__":
    main()
