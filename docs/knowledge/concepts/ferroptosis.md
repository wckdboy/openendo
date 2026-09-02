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
confidence: medium
---

# Ferroptosis — an iron-dependent cell-death axis under investigation

Ferroptosis is a regulated, **iron-dependent form of cell death** driven by lipid peroxidation. Two of its best-known gatekeepers are **GPX4** (glutathione peroxidase 4) and **SLC7A11** (the cystine/glutamate antiporter xCT). Because endometriosis lesions bleed, accumulate iron and face oxidative stress, ferroptosis has become an active research question in the field.^[https://pubmed.ncbi.nlm.nih.gov/42660839/]

## Why it surfaced this week

- **SEMA3C → ferroptosis:** a 2026 paper reports that SEMA3C promotes endometriosis progression by inducing ferroptosis (and enhancing lesion survival).^[https://pubmed.ncbi.nlm.nih.gov/42678895/] A review of autophagy and ferroptosis in endometriosis was published the same week.^[https://pubmed.ncbi.nlm.nih.gov/42660839/]
- **Direct overlap with OpenEndo's target audit:** both **GPX4** and **SLC7A11** are among the 35 novel drug targets (no known drug mechanisms in ChEMBL) in the M1 fold-input pack.^[https://raw.githubusercontent.com/wckdboy/openendo/main/docs/research/structures/fold_input/README.md]
- **M3 screen convergence:** the ChEMBL-based repurposing screen flags **sulfasalazine** (an approved xCT/SLC7A11 inhibitor) against SLC7A11 — the same axis the mechanism literature points at. Hypothesis-generating, not clinical.^[https://raw.githubusercontent.com/wckdboy/openendo/main/docs/data/repurposing_candidates.json]

## Caveats

- Early-stage mechanism science: whether ferroptosis *induction* or *inhibition* is desirable likely depends on cell type, lesion stage and context — direction of effect is unresolved.
- In-vitro potency ≠ clinical efficacy; nothing here is treatment guidance.

## Related

[[computational-drug-repurposing]] · [[gnrh-antagonists]]
