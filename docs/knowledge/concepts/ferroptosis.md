---
title: Ferroptosis in endometriosis
created: 2026-09-02
updated: 2026-09-02
type: concept
tags: [research, drug, treatment]
sources:
  - https://pubmed.ncbi.nlm.nih.gov/42678895/
  - https://pubmed.ncbi.nlm.nih.gov/42660839/
  - https://raw.githubusercontent.com/wckdboy/openendo/main/docs/research/evidence/digest-2026-09-02.md
  - https://raw.githubusercontent.com/wckdboy/openendo/main/docs/data/repurposing_candidates.json
  - https://raw.githubusercontent.com/wckdboy/openendo/main/docs/research/evidence/ferroptosis-direction.md
confidence: medium
---

# Ferroptosis — an iron-dependent cell-death axis under investigation

Ferroptosis is a regulated, **iron-dependent form of cell death** driven by lipid peroxidation. Two of its best-known gatekeepers are **GPX4** (glutathione peroxidase 4) and **SLC7A11** (the cystine/glutamate antiporter xCT). Because endometriosis lesions bleed, accumulate iron and face oxidative stress, ferroptosis has become an active research question in the field.^[https://pubmed.ncbi.nlm.nih.gov/42660839/]

## Why it surfaced this week

- **SEMA3C → ferroptosis:** a 2026 paper reports that SEMA3C promotes endometriosis progression by inducing ferroptosis (and enhancing lesion survival).^[https://pubmed.ncbi.nlm.nih.gov/42678895/] A review of autophagy and ferroptosis in endometriosis was published the same week.^[https://pubmed.ncbi.nlm.nih.gov/42660839/]
- **Direct overlap with OpenEndo's target audit:** both **GPX4** and **SLC7A11** are among the 35 novel drug targets (no known drug mechanisms in ChEMBL) in the M1 fold-input pack.^[https://raw.githubusercontent.com/wckdboy/openendo/main/docs/research/structures/fold_input/README.md]
- **M3 screen convergence:** the ChEMBL-based repurposing screen flags **sulfasalazine** (an approved xCT/SLC7A11 inhibitor) against SLC7A11 — the same axis the mechanism literature points at. Hypothesis-generating, not clinical.^[https://raw.githubusercontent.com/wckdboy/openendo/main/docs/data/repurposing_candidates.json]

## Direction deep-dive verdict (2026-09-02)

Full analysis: [ferroptosis-direction.md](https://raw.githubusercontent.com/wckdboy/openendo/main/docs/research/evidence/ferroptosis-direction.md)

**Double-edged — and the balance tilts toward ferroptosis-related signaling
being disease-SUPPORTING:**
- SEMA3C model: pro-ferroptotic shift (↑ACSL4, ↓GPX4/SLC7A11) co-occurs with
  **enhanced** viability/migration; **Ferrostatin-1 (ferroptosis inhibitor)
  suppressed the phenotype** (PMID 42678895).
- Ferroptotic endometrial stromal cells promote **angiogenesis via paracrine
  VEGFA/IL8** (Nature) — a feed-forward risk for blunt inducers.
- Ferroptosis jointly promotes progression via **immune-microenvironment
  remodeling** (bioinformatics).
- The erastin school (ferroptosis *induction* to kill ectopic cells) is real
  but has no lesion-level demonstration accounting for paracrine effects.

**Consequence for the M3 screen:** sulfasalazine (xCT inhibitor, ferroptosis
inducer) is **downgraded to wrong-direction (confidence MEDIUM)** as an
endometriosis monotherapy — the SLC7A11/GPX4 axis remains a valid target,
but blunt induction is the wrong tool on current evidence.

## Caveats

- Model-level mechanism science; cell-type/lesion-stage context matters;
  no clinical data in endometriosis. Nothing here is treatment guidance.

## Related

[[computational-drug-repurposing]] · [[gnrh-antagonists]]
