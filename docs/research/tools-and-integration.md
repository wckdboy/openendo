# Tools & Integration — how OpenEndo plugs into the industry stack

Grounded 2026 landscape + our integration contract. Goal: anyone using the
tools they already have (ELN, LIMS, SDMS, notebooks, repositories) can pull
OpenEndo data in without writing custom glue.

## 1. What the industry actually runs (the map)

| Layer | What it does | Commercial (dominant) | Open source |
|---|---|---|---|
| **ELN** | experiment documentation | Benchling, LabArchives | **eLabFTW** (AGPL, thousands of instances, Docker, .eln export), Chemotion (chemistry), openBIS (ETH, FAIR/NFDI), SciNote (MPL) |
| **LIMS** | sample-centric QC/workflow | LabWare, LabVantage (Thermo), Benchling | **OpenELIS** (public-health, global foundation), Senaite, eLabFTW (partial) |
| **SDMS** | raw instrument-data archive | Thermo iLibrary, LabWare archive, Agilent OpenLab | none mature — the "data-island" gap (→ T7 instrument inbox) |
| **Analysis** | pipelines/notebooks | Spotfire, Prism | **Galaxy**, KNIME (GPL community ed.), Nextflow/nf-core, Jupyter |
| **Repositories** | share + cite | — | **Zenodo** (CERN), **Dataverse** (Harvard), OSF, Figshare |
| **Standards layer** | formats + vocabularies | — | **FAIR**, **ISA-JSON**, **RO-Crate** (.eln), ELN Consortium; ontologies: MeSH, HPO, EFO, ChEBI, SNOMED/ICD |

Key finding: the modern OSS ELN ecosystem (eLabFTW is the flagship) converges
on **RO-Crate** — the packaging standard that makes datasets portable between
ELNs, archives and analysis tools. **Adopting RO-Crate is our single highest-
leverage integration move.**

## 2. Our integration contract

### 2.1 Identifier discipline (already largely true — now formalized)
Every entity in our datasets carries a **stable, resolvable identifier** from
the vocabulary the industry already uses:

| Entity | Identifier | In our data |
|---|---|---|
| clinical trial | `NCT####…` + URL | ✅ trials_*.json |
| paper | `PMID` + PubMed URL | ✅ pubmed_*.json |
| drug target | `CHEMBL####` + `gene symbol` | ✅ targets.json |
| protein | `UniProt accession` | ✅ fold_input manifest |
| drug/molecule | `CHEMBL####` | ✅ targets.json / repurposing_candidates.json |
| chemical entity | `ChEBI####` | future (biomarker track) |
| phenotype/concept | `HPO` / `MeSH` / `EFO` | future (evidence map topics) |
| person | `ORCID` | contributors page (future) |
| organisation | `ROR` | funding.json (future) |

### 2.2 Formats
- **JSON** (primary, machine-readable) — existing
- **CSV exports** alongside each dataset (Excel/Spotfire/KNIME users) — add
- **RO-Crate manifest** (`ro-crate-metadata.jsonld`) wrapping `docs/data/`
  — makes the whole hub importable into eLabFTW-class tools — add now
- **OpenAPI spec** for the data layer (so connectors can be generated, not
  hand-written) — next milestone

### 2.3 FAIR self-check (what we commit to)
| FAIR | Our status | Action |
|---|---|---|
| **F**indable | GitHub + openendo.org + JSON-LD | mint **DOI per dataset version** via Zenodo |
| **A**ccessible | open HTTPS, no auth | keep free + MIT |
| **I**nteroperable | identifiers + JSON | **RO-Crate** + OpenAPI + CSV |
| **R**eusable | MIT + provenance fields (`updated`, `source`, `pipeline`) | keep; add license metadata to every file's RO-Crate entry |

## 3. Adopt vs build (the honest matrix)

| Need | Verdict | Why |
|---|---|---|
| ELN for the community | **Adopt eLabFTW** | AGPL, Docker one-liner (deploy kit, T7), .eln export, active (v5.5) |
| Repo archive + DOI | **Adopt Zenodo** (free for open research) | GitHub→Zenodo hook mints DOIs on release |
| Public-health LIMS | **Adopt OpenELIS** | global foundation, patient-facing diagnostics |
| Instrument data capture | **BUILD (T7 instrument inbox)** | genuine gap — no mature OSS SDMS; small, focused tool beats a platform |
| Disease-intelligence data hub | **BUILD (OpenEndo)** | nothing exists that combines trials+papers+targets+funding as open, standards-compliant data — this is our OSS contribution |

Rule: **never fork-and-abandon.** When we extend eLabFTW/Zenodo we contribute
upstream (templates, Danish locale, docs).

## 4. Immediate work items
1. `ro-crate-metadata.jsonld` — v1 manifest for `docs/data/` (this PR)
2. `IDENTIFIERS.md` — the contract above, as the repo's data-language spec
3. CSV export step in `update_data.py` (next PR)
4. Zenodo DOI hook (when first stable release is tagged)
5. OpenAPI spec for the data layer (with the API milestone)

*Author: Percival (Hermes Agent), 2026-09-02. Sources: 2026 ELN/LIMS landscape
reviews (labsoftwareguide.com, 37degrees.io, intuitionlabs.ai, labkey.com,
pistack.xyz), ELN Consortium / RO-Crate, FAIR principles.*
