#!/usr/bin/env python3
"""Generate an RO-Crate v1.1 manifest for docs/data/.

RO-Crate (https://www.researchobject.org/ro-crate/) is the packaging
standard behind the ELN Consortium's .eln format — an RO-Crate manifest
makes our datasets importable into eLabFTW-class tools and archives.

Usage: python3 scripts/gen_ro_crate.py
"""
import json
import os
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "docs", "data")
HOME = "https://github.com/wckdboy/openendo"

FILE_META = {
    "trials_global_recruiting.json": ("Recruiting endometriosis trials worldwide",
                                      "https://clinicaltrials.gov/api/v2"),
    "trials_denmark.json": ("Endometriosis trials registered in Denmark",
                            "https://clinicaltrials.gov/api/v2"),
    "trials_recent.json": ("Endometriosis trials new/updated last 7 days",
                           "https://clinicaltrials.gov/api/v2"),
    "pubmed_recent.json": ("Endometriosis papers from the last 7 days",
                           "https://pubmed.ncbi.nlm.nih.gov/"),
    "pubmed_monthly.json": ("Monthly endometriosis paper counts (6 months)",
                            "https://pubmed.ncbi.nlm.nih.gov/"),
    "targets.json": ("Drug-target landscape: novel/high-druggability targets",
                     "https://www.ebi.ac.uk/chembl/"),
    "repurposing_candidates.json": ("Approved drugs with potency against novel targets",
                                    "https://www.ebi.ac.uk/chembl/"),
    "funding.json": ("Endometriosis funding opportunities with deadlines", "curated"),
    "content.json": ("Site content: stats, actions, resources (EN/DA)", "curated"),
    "meta.json": ("Generation timestamp and counts", "generated"),
}


def main():
    graph = [{
        "@id": "ro-crate-metadata.jsonld",
        "@type": "CreativeWork",
        "about": {"@id": "./"},
        "conformsTo": {"@id": "https://w3id.org/ro/crate/1.1"},
        "sdPublisher": {"@id": HOME},
    }, {
        "@id": "./",
        "@type": "Dataset",
        "name": "OpenEndo — open endometriosis research data",
        "description": ("Open, weekly-refreshed datasets on endometriosis: "
                        "clinical trials (ClinicalTrials.gov), papers "
                        "(PubMed), drug targets (ChEMBL), repurposing "
                        "candidates, funding and site content. MIT licensed."),
        "license": {"@id": "https://spdx.org/licenses/MIT"},
        "publisher": {"@id": HOME},
        "url": "https://openendo.org/",
        "datePublished": time.strftime("%Y-%m-%d"),
        "hasPart": [],
        "keywords": ["endometriosis", "clinical trials", "drug targets",
                     "women's health", "open data"],
    }, {
        "@id": HOME,
        "@type": "Organization",
        "name": "OpenEndo (wckdboy/openendo)",
        "url": HOME,
    }]

    for fn, (name, source) in sorted(FILE_META.items()):
        path = os.path.join(DATA, fn)
        if not os.path.exists(path):
            continue
        with open(path, encoding="utf-8") as f:
            obj = json.load(f)
        entry = {
            "@id": f"data/{fn}",
            "@type": "File",
            "name": name,
            "encodingFormat": "application/json",
            "contentSize": str(os.path.getsize(path)),
        }
        if source != "curated":
            entry["isBasedOn"] = {"@id": source}
        if isinstance(obj, dict) and obj.get("updated"):
            entry["dateModified"] = obj["updated"]
        graph[1]["hasPart"].append({"@id": f"data/{fn}"})
        graph.append(entry)

    crate = {"@context": "https://w3id.org/ro/crate/1.1/context",
             "@graph": graph}
    out = os.path.join(DATA, "ro-crate-metadata.jsonld")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(crate, f, ensure_ascii=False, indent=1)
    print(f"RO-Crate manifest: {len(graph[1]['hasPart'])} datasets -> {out}")


if __name__ == "__main__":
    main()
