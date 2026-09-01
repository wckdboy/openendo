# OpenEndo — Research Program

**Mission:** use open computational research to improve conditions for the ~190M
people with endometriosis — cutting the 7–10 year diagnostic delay and opening
the drug-discovery space. Research + advocacy, never medical advice.

**Method:** the same discipline pharma uses — AI agents driving an evidence
loop across literature, targets, structure, trials and (eventually) wet labs —
but fully open, auditable and reproducible.

---

## 1. The research pipeline (how a finding is born)

```
lit intelligence ─▶ target hypothesis ─▶ structure ─▶ binding/drug hypothesis
      │                    │                 │                 │
      ▼                    ▼                 ▼                 ▼
evidence map        audit (ChEMBL)      AlphaFold-ish      repurposing screen
      │                    │                 │                 │
      └─────────────▶ prioritised, cited shortlist (every step sourced)
                                    │
                                    ▼
                     wet-lab handoff spec (robotics-ready)
                     [requires funding/partner — designed, not run]
```

Each stage is a **track** (below). Each track produces artifacts in this repo
(JSON/CSV/MD + scripts), so any agent — or any human — can reproduce or extend.

## 2. Tracks, real tools, deliverables

### T1 — Literature & evidence intelligence  *(CPU)*
**Tools:** PubMed E-utilities (live), Europe PMC REST, OpenAlex API,
Semantic Scholar API, arXiv.
**Loop:** weekly agent digest → new papers/signal → evidence map
(`docs/research/evidence/`). Human-in-the-loop for claims that matter.
**Deliverable:** maintained, sourced evidence map; monthly signal report.

### T2 — Target & biomarker intelligence  *(CPU)*
**Tools:** ChEMBL (live), Open Targets Platform API, UniProt, Ensembl,
GTEx (expression), GWAS Catalog, ClinicalTrials.gov v2 (live).
**Loop:** target lists (e.g. Deep Origin AI Scientist 178 targets) are
audited against open pharmacology + genetics data.
**Status:** v1 audit live (58 targets → 35 novel, 8 with approved drugs).
**Next:** expression cross-reference (which novel targets are actually
elevated in endometriotic tissue), biomarker candidate tracker.
**Deliverable:** `docs/data/targets.json` + `docs/research/targets/` audits.

### T3 — Structure & drug design (the AlphaFold-ish pillar)  *(CPU + GPU)*
**Tools:**
- **AlphaFold Server** (alphafoldserver.com) — AlphaFold 3, free for
  academic use, ~1–5 min/job, **no local GPU needed** → our workhorse
- **ESMFold** (Meta) — fast LLM folding, 30 s–few min; runs on the
  ShadowPC A4500 (20 GB)
- **ColabFold** (AF2 + RoseTTAFold + MMseqs2) — fast MSA, modest GPU
- **RoseTTAFold / OpenFold** — alternatives for complexes
- **DiffDock** — ML docking (predict how small molecules bind)
- **AutoDock Vina** — classical docking for validation
- **RDKit** — cheminformatics (SMILES, properties, similarity)
- **PyMOL** — industry-standard visualization; **FPocket** — pocket analysis
**Plan:**
1. Fold the **35 novel targets** via AlphaFold Server → public structure
   library (`docs/research/structures/`, PDB files + metadata)
2. Pocket analysis (FPocket) → druggable pocket report per target
3. Screen **approved drugs** (ChEMBL phase-4 molecules) against the most
   druggable novel targets (DiffDock/Vina) → **repurposing candidates** —
   the fastest path to real patient impact
4. ShadowPC later: ESMFold/ColabFold bulk + imaging ML (ultrasound/MRI
   segmentation — the diagnostic-delay problem)
**Deliverable:** open structure library + pocket report + repurposing shortlist.

### T4 — Clinical intelligence  *(CPU, live)*
**Tools:** ClinicalTrials.gov API v2 (live), EU CTIS/ICTRP (EU trials),
WHO ICTRP, FDA database.
**Status:** trial dashboards live (global recruiting, Denmark, recent).
**Next:** gap analysis — what trial types are missing (e.g. disease-modifying
vs symptom trials), by country; diagnostic-delay policy signal.
**Deliverable:** quarterly trial-landscape report feeding the site.

### T5 — Robotics & wet-lab bridge  *(design, not execution — yet)*
**Reality:** the industry validates AI hypotheses in automated wet labs —
**Opentrons** (OT-2/Flex: open-source firmware, Python protocols, MCP server
for agent-to-agent workflows), **Emerald Cloud Lab** (fully remote cloud lab),
**Arctoris** (cloud lab + discovery consulting — Deep Origin's partner),
**Recursion** (phenomic screening), **LabGenius** (ML-guided antibody robots).
**Our role now:** produce **wet-lab handoff specs** — for the top 3 target
hypotheses: the assay design, the Opentrons protocol sketch (Python), the
validation criteria, the falsification test. Ready to hand to a funded partner
or a cloud-lab engagement when the science justifies it.
**Deliverable:** `docs/research/wetlab/` handoff specs (assay + protocol +
criteria). Honest gate: we do not claim to run wet labs.

### T6 — Methods & reproducibility  *(CPU)*
**Problem:** endometriosis ML studies are 97% internally validated; leakage
safeguards often missing. The field's weakest point is our strongest opening.
**Deliverable:** leakage-safe ML checklist + open dataset registry
(`docs/research/datasets/`). Every model we ever ship follows it.

## 3. Compute allocation (precise)

| Resource | Where | Used for |
|---|---|---|
| This box (8-core EPYC, no GPU, 471 GB) | now | T1, T2, T4, T6; AlphaFold Server orchestration; RDKit; DiffDock CPU fallback |
| ShadowPC Power Pro (A4500 20 GB) | when delivered | ESMFold/ColabFold bulk folding, DiffDock, imaging ML (ultrasound/MRI), Lumion renders (separate track) |
| Cloud APIs (free) | now | AlphaFold Server, OpenAlex, Semantic Scholar, ChEMBL, GTEx |

Rule: nothing touches patient data; all tools public/open or free academic.

## 4. Agent protocol (multi-agent, in this repo)

- **Agents:** JAEGER (data hub + site, owns `main`), Percival (research
  infrastructure + T1–T3/T6), future research analysts per track.
- **Coordination:** every work item = a GitHub issue, claimed by exactly one
  agent; work on `<agent>/<track>` branches; PRs reviewed by another agent
  (or human) before merge. Duplicate work is forbidden — check issues first.
- **Evidence rule:** every claim in research artifacts carries a source;
  unsourced = marked hypothesis. No medical advice. Ever.
- **Autoresearchers-style loop:** claim → run → report evidence → release.

## 5. Milestones

| # | What | When/Where |
|---|---|---|
| M0 | Research program + tracks + protocol | this document (PR) |
| M1 | Fold 35 novel targets (AlphaFold Server) + pocket report + expression cross-ref | CPU, now |
| M2 | Literature evidence agent loop live (weekly digest) + biomarker tracker | CPU, next |
| M3 | Repurposing screen: approved drugs × novel targets (DiffDock/Vina) | CPU now, GPU later |
| M4 | Wet-lab handoff specs for top-3 hypotheses (Opentrons protocol sketches) | design, funding-gated |
| M5 | Imaging ML for diagnostics (leakage-safe, per T6) | ShadowPC GPU |

## 6. Honest limits

- We are not a wet lab. Robotics execution requires hardware/funding — we
  design the handoff, we do not run assays.
- AlphaFold predictions are hypotheses, not structures. Every folding result
  carries confidence metrics (pLDDT) and is labeled accordingly.
- No clinical claims. Everything is research infrastructure for the community.

*Research program v1 — Percival (Hermes Agent), 2026-09-01. Sources: see
evidence map and per-artifact READMEs.*
