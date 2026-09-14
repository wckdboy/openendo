# OpenEndo wet-lab protocol specs (partner-ready drafts)

> **What this folder is:** paper-protocol *specifications* for partner organoid / animal / pathology labs — scientific questions, endpoints, controls, go/no-go, ethics.  
> **What it is not:** DIY recipes, patient self-treatment guides, or medical advice.  
> **Corpus:** grounded in `/workspace/openendo` (CHECKPOINT + knowledge + Phase 0.5/1 evidence).  
> **Git:** drafts live under `/workspace/openendo-drafts/` only — **do not push to GitHub** from this pass.  
> **Date:** 2026-09-14.

---

## Index — top research leads

| # | File | Lead | M3 / wiki status | Primary wet-lab modality |
|---|---|---|---|---|
| 1 | [`01-sirolimus-mtor-fkbp4-pr.md`](./01-sirolimus-mtor-fkbp4-pr.md) | Sirolimus / **mTOR** (+ optional **FKBP4/PR** readout panel) | **TOP TIER** — axes kept separate | Organoid or animal pharmacology + PD |
| 2 | [`02-mrgprx2-ihc-mast-cell-stratification.md`](./02-mrgprx2-ihc-mast-cell-stratification.md) | **MRGPRX2** IHC / mast-cell stratification by lesion type | **VALIDATED AXIS** (antagonism; not cetrorelix-as-drug) | Histopathology IHC / dual-IF |
| 3 | [`03-ferroptosis-selectivity-coculture.md`](./03-ferroptosis-selectivity-coculture.md) | Ferroptosis selectivity (lesion epi/stroma vs CD8⁺ / eutopic; **sulfasalazine–xCT**) | **WATCHLIST** — direction resolved; selectivity open | Primary cell / co-culture panel |

### Related draft packets (same parent folder)
- `../research-agenda-2026-09-14.md` — lead status after registry + literature refresh  
- `../registry-verification-2026-09-14.md` — CT.gov re-check (0 endo trials for these mechanisms)  
- `../literature-packet-2026-09-14.md` — PubMed/Europe PMC delta  
- `../knowledge-updates/{sirolimus,mrgprx2-pain,ferroptosis}.md` — SCHEMA wiki update drafts  

---

## T7 lab-interview context (partner outreach)

Wet-lab execution is expected via **partner labs**, not an OpenEndo wet bench. T7 (lab software modernization) already prepared Danish outreach / interview scaffolding — useful for finding partners who also care about ELN / data hygiene when running these protocols.

| Resource | Path (in `/workspace/openendo`) | Role |
|---|---|---|
| CHECKPOINT workstream **T7** | `CHECKPOINT.md` (M3/T7 rows; Phase A DONE, Phase B = human interviews) | Status: Phase A done 2026-09-03; Phase B waiting on human |
| Endometriosis-focused shortlist (5 DK groups) | `docs/research/lab-interviews/candidates-2026-09.md` | AUH/SDU Rudnicki, LRB Borgbo, RH Gyn Madsen, AU Rytter, AUH MY-ENDO |
| Danish outreach draft | `docs/research/lab-interviews/outreach-draft-dk.md` | 3-paragraph + bullet-ask; no PII |
| General lab shortlist (KU / DTU / SSI …) | `docs/research/lab-interview-shortlist.md` | Broader ELN personas |
| Interview guide (DK) | `docs/research/templates/interview-guide-dk.md` | Question bank |
| Fillable form | `docs/research/templates/lab-interview-form.pdf` | Capture template |
| T7 concept note | `docs/research/lab-software-modernization.md` | Why ELN/modernization matters |

**Phase B reminder (CHECKPOINT):** interviews are a **human** step; publish only anonymized write-ups. These wet-lab specs can be attached to outreach as “example collaborative protocol questions,” not as a demand to run drug studies.

---

## Cross-cutting caveats (all three specs)

1. **Not treatment advice** for individuals; no dosing for patients.  
2. **Sirolimus:** immunosuppression + teratogenicity + systemic toxicity — heavy for a benign chronic disease narrative.  
3. **MRGPRX2:** lesion-type dependence is the open wet-lab question; cetrorelix remains a *wrong-direction* pharmacological anecdote.  
4. **Ferroptosis / sulfasalazine:** induction-in-lesion-cells is the current lean; **selectivity** (CD8⁺, eutopic fertility) keeps WATCHLIST; contested “suppress ferroptosis” EA papers flagged uncertain.  
5. **Computational ceiling:** Phase 1 docking done; Phase 2 MD budget still human-gated — wet lab can proceed in parallel on questions docking cannot answer.  
6. **Uncertainty:** every spec marks `[UNCERTAIN]` where n, antibody clones, SI thresholds, or partner capabilities need local finalization.

---

## Suggested partner conversation order

1. **MRGPRX2 IHC** — fastest path to a protein-level go/no-go on lesion-type stratification (often histopathology cores).  
2. **Sirolimus / mTOR organoid PD** — if partner already runs endo organoids or animal lesions.  
3. **Ferroptosis selectivity co-culture** — highest complexity; only with immune + primary-cell strength.

---

*Galahad executor draft · 2026-09-14 · OpenEndo research infrastructure.*
