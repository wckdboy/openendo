#!/usr/bin/env python3
"""Regenerate docs/data/ro-crate-metadata.jsonld from the actual data files.

FAIR manifest (RO-Crate 1.1) for the OpenEndo data layer. Scans docs/data/*.json
(excluding the manifest itself), derives contentSize + dateModified from the
real files and meta.json, and writes a deterministic, sorted manifest.

Why this exists: the manifest used to be hand-maintained and silently missed
new files (access.json, targets.json, repurposing_candidates.json were absent).
Now it is regenerated automatically:
  - by scripts/update_data.py on every weekly data refresh, and
  - checked by CI (security-scan.yml) so any PR touching docs/data must keep
    the manifest in sync (diff-verified).

Usage: python3 scripts/gen_ro_crate.py   (idempotent; writes in place)
"""
import json
import os
import sys
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "docs", "data")
MANIFEST = os.path.join(DATA, "ro-crate-metadata.jsonld")

# Human-readable names + provenance per curated/generated file. Files not
# listed here still get included with a generic name (no source annotation).
# Keys must match the actual filenames in docs/data/.
NAMES = {
    "access.json": "Country/postcode access: medications, specialised centres, organisations, care paths (schema openendo-access-v1)",
    "content.json": "Site content: stats, actions, resources (EN/DA)",
    "funding.json": "Endometriosis funding opportunities with deadlines",
    "meta.json": "Generation timestamp and counts",
    "pubmed_monthly.json": "Monthly endometriosis paper counts (6 months)",
    "pubmed_recent.json": "Endometriosis papers from the last 7 days",
    "repurposing_candidates.json": "Approved-drug repurposing candidates from the M3 screen",
    "targets.json": "Drug targets (58 total, 35 novel), ChEMBL-verified",
    "trials_denmark.json": "Endometriosis trials registered in Denmark",
    "trials_global_recruiting.json": "Recruiting endometriosis trials worldwide",
    "trials_recent.json": "Endometriosis trials new/updated in the last 7 days",
}

# External provenance per file -> isBasedOn @id. Omitted files get no
# isBasedOn (curated origin is the repo itself).
SOURCES = {
    "meta.json": "generated",
    "pubmed_monthly.json": "https://pubmed.ncbi.nlm.nih.gov/",
    "pubmed_recent.json": "https://pubmed.ncbi.nlm.nih.gov/",
    "trials_denmark.json": "https://clinicaltrials.gov/api/v2",
    "trials_global_recruiting.json": "https://clinicaltrials.gov/api/v2",
    "trials_recent.json": "https://clinicaltrials.gov/api/v2",
}

ORG = {
    "@id": "https://github.com/wckdboy/openendo",
    "@type": "Organization",
    "name": "OpenEndo (wckdboy/openendo)",
    "url": "https://github.com/wckdboy/openendo",
}


def updated_date() -> str:
    """Prefer meta.json's own 'updated' stamp; fall back to today."""
    try:
        with open(os.path.join(DATA, "meta.json"), encoding="utf-8") as f:
            meta = json.load(f)
        u = meta.get("updated") or meta.get("generated_at", "")[:10]
        if u:
            return u[:10]
    except (OSError, ValueError):
        pass
    return date.today().isoformat()


def build():
    stamp = updated_date()
    files = sorted(
        n for n in os.listdir(DATA)
        if n.endswith(".json") and n != "ro-crate-metadata.jsonld"
    )
    has_part = [{"@id": f"data/{n}"} for n in files]

    graph = [
        {
            "@id": "ro-crate-metadata.jsonld",
            "@type": "CreativeWork",
            "about": {"@id": "./"},
            "conformsTo": {"@id": "https://w3id.org/ro/crate/1.1"},
            "sdPublisher": {"@id": "https://github.com/wckdboy/openendo"},
        },
        {
            "@id": "./",
            "@type": "Dataset",
            "name": "OpenEndo — open endometriosis research data",
            "description": "Open, weekly-refreshed datasets on endometriosis: clinical trials (ClinicalTrials.gov), papers (PubMed), drug targets (ChEMBL), repurposing candidates, funding and site content. MIT licensed.",
            "license": {"@id": "https://spdx.org/licenses/MIT"},
            "publisher": {"@id": "https://github.com/wckdboy/openendo"},
            "url": "https://openendo.org/",
            "datePublished": stamp,
            "hasPart": has_part,
            "keywords": [
                "endometriosis",
                "clinical trials",
                "drug targets",
                "women's health",
                "open data",
            ],
        },
        ORG,
    ]

    for name in files:
        path = os.path.join(DATA, name)
        entity: dict[str, object] = {
            "@id": f"data/{name}",
            "@type": "File",
            "name": NAMES.get(name, f"OpenEndo dataset: {name}"),
            "encodingFormat": "application/json",
            "contentSize": str(os.path.getsize(path)),
            "dateModified": stamp,
        }
        src = SOURCES.get(name)
        if src is not None:
            entity["isBasedOn"] = {"@id": src}
        graph.append(entity)

    doc = {"@context": "https://w3id.org/ro/crate/1.1/context", "@graph": graph}
    with open(MANIFEST, "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
        f.write("\n")
    return len(files)


if __name__ == "__main__":
    try:
        n = build()
        print(f"ro-crate-metadata.jsonld regenereret ({n} datafiler)")
    except Exception as e:  # noqa: BLE001 — fail loudly for CI
        sys.stderr.write(f"FEJL i gen_ro_crate.py: {e}\n")
        sys.exit(1)
