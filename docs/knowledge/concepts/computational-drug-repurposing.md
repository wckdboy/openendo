---
title: Computational drug repurposing for endometriosis
created: 2026-09-02
updated: 2026-09-02
type: concept
tags: [research, drug, pipeline]
sources:
  - https://pubmed.ncbi.nlm.nih.gov/42668641/
  - https://raw.githubusercontent.com/wckdboy/openendo/main/docs/research/evidence/digest-2026-09-02.md
  - https://raw.githubusercontent.com/wckdboy/openendo/main/docs/data/repurposing_candidates.json
  - https://raw.githubusercontent.com/wckdboy/openendo/main/docs/research/targets/targets.json
confidence: medium
---

# Computational drug repurposing — new uses for approved drugs

**The idea:** approved drugs already have known safety profiles. Screening them against disease biology can shortcut the 10–15 year de-novo pipeline — attractive for a disease like endometriosis where dedicated drug development is underfunded.

OpenEndo's program runs **two complementary approaches**:

## 1. Transcriptomics-based (expression side)

A 2026 iScience proof-of-concept pipeline over approved drugs flagged **simvastatin** (statin; anti-inflammatory/anti-angiogenic) and **primaquine** (anti-malarial; oxidative stress) as endometriosis candidates from transcriptomic signatures.^[https://pubmed.ncbi.nlm.nih.gov/42668641/] This is the template for expression-driven repurposing: replicate hits against independent expression data (GTEx/GEO) before clinical follow-up.

## 2. Target-activity-based (our M3 screen)

A ChEMBL screen over the 35 novel targets (approved drugs, max phase 4, measured potency pChEMBL ≥ 6) produced **9 candidate pairs**.^[https://raw.githubusercontent.com/wckdboy/openendo/main/docs/data/repurposing_candidates.json] Highlights:

| Target | Approved drug(s) | Why it matters |
|---|---|---|
| SLC7A11 | Sulfasalazine | xCT inhibitor — converges with the [[ferroptosis]] mechanism literature |
| FKBP4 | Sirolimus, tacrolimus, cyclosporine | Progesterone-receptor chaperone; endometriosis is progesterone-resistant |
| MRGPRX2 | Cetrorelix | GnRH-antagonist class already used clinically — target validity support |
| GPER1 | Estradiol | Rapid-signaling estrogen receptor in an estrogen-driven disease |
| ACVR1B | Crizotinib, dabrafenib | TGF-β/activin signaling (fibrosis, lesion growth) |
| SLCO2A1 | Dinoprostone (PGE2) | Prostaglandin transporter — direction of effect needs review |

## Validation ladder

1. Cross-reference target expression in endometriosis tissue (GTEx/GEO).
2. Mechanism + direction-of-effect review per pair.
3. In-vivo / clinical follow-up only after 1–2.

In-vitro potency ≠ efficacy; the screen is **hypothesis generation**, and nothing here is treatment guidance. Current focus: depth-check each candidate (evidence, safety, novelty) → ranked shortlist.^[https://raw.githubusercontent.com/wckdboy/openendo/main/docs/research/evidence/digest-2026-09-02.md]

## Related

[[ferroptosis]] · [[gnrh-antagonists]] · [[ryeqo-vs-yselty]]
