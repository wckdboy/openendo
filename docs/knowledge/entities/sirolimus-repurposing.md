---
title: Sirolimus (rapamycin) — M3 repurposing candidate
created: 2026-09-02
updated: 2026-09-02
type: entity
tags: [treatment, drug, research]
sources:
  - https://raw.githubusercontent.com/wckdboy/openendo/main/docs/research/evidence/m3-validation.md
  - https://raw.githubusercontent.com/wckdboy/openendo/main/docs/data/repurposing_candidates.json
  - https://pubmed.ncbi.nlm.nih.gov/41170754/
confidence: medium
---

# Sirolimus (rapamycin) — rank-1 M3 repurposing candidate

mTOR inhibitor (immunosuppressant/anticancer, ~25 years of clinical use).
Surfaced by the M3 ChEMBL-activity screen against **FKBP4** — see
[[computational-drug-repurposing]].^[https://raw.githubusercontent.com/wckdboy/openendo/main/docs/data/repurposing_candidates.json]

## Key facts
- **Screen hit:** measured potency against FKBP4 (pchembl ≥ 6). Note: FKBP4
  (FKBP52) is the progesterone-receptor co-chaperone — but sirolimus'
  patient-facing pharmacology runs through **FKBP12 → mTORC1 inhibition**,
  not FKBP4. The ChEMBL hit is binding promiscuity; rank sirolimus by its
  real mechanism (mTOR).^[https://raw.githubusercontent.com/wckdboy/openendo/main/docs/research/evidence/m3-validation.md]
- **Endometriosis evidence (independent of our screen):** rapamycin
  improves endometriosis-related infertility via ovarian senescence —
  PPARα/IGFBP2 pathway (animal model, Mol Med Rep 2026).^[https://pubmed.ncbi.nlm.nih.gov/41170754/]
- **Direction:** antiproliferative (mTORC1) — consistent with suppressing
  lesion growth; distinct from hormonal mechanisms.
- **Safety:** chronic-use profile established over ~25 years
  (transplant/oncology); better tolerated than calcineurin inhibitors;
  class cautions: immunosuppression, metabolic effects, wound healing.
- **Novelty in endometriosis:** no registered endometriosis clinical trial
  found (verify on ClinicalTrials.gov before claiming) — repurposing
  opportunity is open.

## Why it matters
Rank-1 of the M3 validated shortlist: established drug, antiproliferative
direction, independent animal evidence in endometriosis, and a clean
mechanistic rationale (mTORC1) distinct from the hormonal standard of care.
Needs a human clinical-interest decision — research output, not medical
advice.^[https://raw.githubusercontent.com/wckdboy/openendo/main/docs/research/evidence/m3-validation.md]

## Related
[[computational-drug-repurposing]] · [[mrgprx2-pain]] · [[gnrh-antagonists]]
