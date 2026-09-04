---
title: Ferroptosis in endometriosis
created: 2026-09-02
updated: 2026-09-04
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

## Direction of effect — resolved (2026-09-02, MEDIUM confidence)

Detailed verdict: `docs/research/evidence/ferroptosis-direction.md`. In short:
ferroptosis is **compartment-dependent** — in lesion epithelial/stromal cells
it is a growth *brake* that lesions actively evade (MGST3, HSD11B1,
FZD7→SLC7A11 up-regulation), and forcing it back on (erastin, andrographolide,
xCT blockade) reproducibly shrinks lesions in 2026 models; but ferroptosis
striking lesional CD8⁺ T cells disables anti-lesion immunity and helps the
lesion,^[https://pubmed.ncbi.nlm.nih.gov/41146213/] and ferroptosis in eutopic
endometrium harms decidualization/fertility.^[https://pubmed.ncbi.nlm.nih.gov/41722688/]
The SEMA3C finding is sub-lethal ferroptotic *signaling* exploited by lesion
cells, not evidence that lethal ferroptosis drives lesions. For the M3 screen
this **supports the therapeutic direction of SLC7A11/xCT inhibition in lesion
cells** (sulfasalazine), while flagging that systemic (non-lesion-targeted)
induction carries immune-cell and fertility risks — one reason sulfasalazine
stays WATCHLIST.

### Lesion-expression corroboration (GEO reanalysis, 2026-09-03/04)

Lesional transcriptomics (3 datasets; methods: `docs/research/virtual/phase0.5.md`)
support the "lesions evade ferroptosis" read at the expression level:

- **GSE282532** (endometrioma bulk, 5 patient-paired): **SLC7A11 2× down** and
  **ACSL4 2.4× down** in ectopic vs eutopic tissue — ferroptosis evasion via
  *suppression of effector genes*, not overexpression of the SLC7A11 resistance
  node.^[https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE282532]
- **GSE247695** (scRNA-seq) + **GSE263897** (GeoMx spatial): SLC7A11 down / no
  constitutive up-regulation in lesion compartments — consistent across
  platforms.^[https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE247695]^[https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE263897]

Implication for the M3 screen: xCT inhibition (sulfasalazine) targets a
transporter the lesion keeps *low* — consistent with the therapeutic direction
(forcing ferroptosis back on), while the low lesional expression underlines that
selectivity/toxicity, not target presence, is the open question. Phase 1.0
docking (2026-09-04, PR #22) confirms sulfasalazine binds the xCT substrate
cavity (−8.52 vs native −9.35 kcal/mol).

## Caveats

- Mechanism science is 2025–2026 and largely preclinical; clinical evidence in
  endometriosis is absent (no registered xCT-inhibitor trial).
- Cell type and lesion stage matter: induction vs inhibition is not a
  one-size answer across compartments.
- In-vitro potency ≠ clinical efficacy; nothing here is treatment guidance.

## Related

[[computational-drug-repurposing]] · [[gnrh-antagonists]]
