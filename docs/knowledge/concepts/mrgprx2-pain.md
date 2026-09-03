---
title: "MRGPRX2 — mast-cell pain axis in endometriosis"
created: 2026-09-02
updated: 2026-09-03
type: concept
tags: [research, drug, treatment]
sources:
  - https://pubmed.ncbi.nlm.nih.gov/40600649/
  - https://pubmed.ncbi.nlm.nih.gov/17007852/
  - https://pubmed.ncbi.nlm.nih.gov/41079937/
  - https://pubmed.ncbi.nlm.nih.gov/40028674/
  - https://pubmed.ncbi.nlm.nih.gov/31998139/
  - https://pubmed.ncbi.nlm.nih.gov/12537785/
  - https://pubmed.ncbi.nlm.nih.gov/12470539/
  - https://pubmed.ncbi.nlm.nih.gov/28288109/
  - https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL5849/
  - https://www.ebi.ac.uk/chembl/compound/inspect/CHEMBL1200490
  - https://clinicaltrials.gov/study/NCT00244452
  - https://www.proteinatlas.org/ENSG00000183695-MRGPRX2/tissue
  - https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE282532
  - https://raw.githubusercontent.com/wckdboy/openendo/main/docs/research/evidence/m3-validation.md
confidence: medium
---

# MRGPRX2 — mast-cell pain axis in endometriosis

MRGPRX2 (Mas-related G-protein-coupled receptor X2) is a **mast-cell
receptor** increasingly implicated in endometriosis pain. It surfaced in
OpenEndo's M3 repurposing screen as the ChEMBL target hit for cetrorelix —
a pair that turned out to be *target-validating* (build an antagonist), not a
repurposing case. See [[computational-drug-repurposing]].

## The pain mechanism (2025, FASEB J)

A 2025 study (*FASEB J*, PMID 40600649) reports the axis end-to-end:
MRGPRX2⁺ mast-cell density is **increased in endometriotic lesions**;
endometriotic cells release HBD-2 (β-defensin 2), which triggers
MRGPRX2-dependent **histamine** release from mast cells; histamine then
sensitizes dorsal-root-ganglion sensory neurons via **HRH1/TRPV1** signalling,
driving pain/hyperalgesia. Mast-cell knockout, MRGPRX2 deficiency and H1
blockade each relieved the phenotype in models.^[https://pubmed.ncbi.nlm.nih.gov/40600649/]
(First published 2025 — earlier OpenEndo notes dated it 2026; corrected
2026-09-02.)

## Background: mast cells and endometriosis pain

Mast cells accumulate in peritoneal, ovarian and deep infiltrating lesions,
often near nerves, in pain-associated patterns (Anaf 2006);^[https://pubmed.ncbi.nlm.nih.gov/17007852/]
they are present in peritoneal fluid of endometriosis patients;^[https://pubmed.ncbi.nlm.nih.gov/31998139/]
and recent reviews position mast cells and oestrogen-driven histamine/FGF2
release at the centre of pain sensitization.^[https://pubmed.ncbi.nlm.nih.gov/41079937/]^[https://pubmed.ncbi.nlm.nih.gov/40028674/]

## The M3 hit: cetrorelix → MRGPRX2 (measured, but agonism)

- **Measured activity (real):** cetrorelix (CHEMBL1200490, max phase 4) has
  two ChEMBL activities against MRGPRX2 (CHEMBL5849) — EC50 617 nM /
  pChEMBL 6.21 (Ca²⁺ FLIPR) and EC50 813 nM / pChEMBL 6.09 (β-arrestin
  PRESTO-Tango), from probe-design/off-target profiling (Lansu et al., *Nat
  Chem Biol* 2017).^[https://pubmed.ncbi.nlm.nih.gov/28288109/]
- **But the measured effect is *agonism*** — activating MRGPRX2, the
  opposite of what the pain axis above would need. No clinical link between
  cetrorelix and mast-cell/MRGPRX2 action exists.
- Cetrorelix (Cetrotide) is an established GnRH antagonist used in
  endometriosis — the 3 mg once-weekly × 8-week regimen is documented in two
  small 2002 German reports (15 patients each).^[https://pubmed.ncbi.nlm.nih.gov/12537785/]^[https://pubmed.ncbi.nlm.nih.gov/12470539/]
  A registered phase-2 used a different sustained-release single-dose design
  and never posted results.^[https://clinicaltrials.gov/study/NCT00244452]
- **Conclusion:** the M3 pair validates MRGPRX2 as an endometriosis-relevant
  target (lesional mast cells + pain readout) but does *not* make cetrorelix
  a repurposing lead. The actionable direction is **MRGPRX2 antagonist**
  development for non-hormonal endometriosis pain.

## Expression cross-check (GTEx/HPA + GEO reanalysis)

Bulk-tissue RNA is essentially zero (HPA endometrium nTPM 0.0, "not
detected"; GTEx uterus 0.06 TPM) — expected for a receptor on a rare cell
type (mast cells; also subsets of immune cells and dorsal root ganglion).
The receptor is genuinely present at the lesion **on infiltrating mast
cells**, which bulk screens cannot see.^[https://www.proteinatlas.org/ENSG00000183695-MRGPRX2/tissue]

GEO reanalysis of GSE282532 (5 paired eutopic/ectopic RNA-seq samples;
Peking University First Hospital, public Nov 2025) corroborates this:
MRGPRX2 is below detection in all eutopic and nearly all ectopic bulk samples,
but canonical mast-cell markers are **11-15x enriched** in ectopic lesions
across all 5 pairs — CPA3 (13.6x), TPSAB1 (15.0x), TPSB2 (11.0x). This
provides independent quantitative support for elevated mast-cell density in
lesions. Source: NCBI GEO, GSE282532 (2026-09-03).^[https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE282532]

## Why it matters

Most endometriosis treatments are hormonal. A mast-cell/MRGPRX2 pain axis is
a **non-hormonal, mechanism-specific target** for the pain that dominates the
patient experience — relevant to the 7–10-year diagnostic-delay mission only
insofar as better-targeted research shortens the path to real options.
Hypothesis-generating research output; not medical advice.

## Related

[[computational-drug-repurposing]] · [[gnrh-antagonists]] · [[sirolimus]]
