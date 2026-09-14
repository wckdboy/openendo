---
title: Sirolimus (rapamycin)
created: 2026-09-02
updated: 2026-09-14
type: entity
tags: [treatment, drug, research]
sources:
  - https://pubmed.ncbi.nlm.nih.gov/39579091/
  - https://pubmed.ncbi.nlm.nih.gov/27347023/
  - https://pubmed.ncbi.nlm.nih.gov/41170754/
  - https://pubmed.ncbi.nlm.nih.gov/37914557/
  - https://pubmed.ncbi.nlm.nih.gov/22279148/
  - https://pubmed.ncbi.nlm.nih.gov/27778641/
  - https://pubmed.ncbi.nlm.nih.gov/17571166/
  - https://pubmed.ncbi.nlm.nih.gov/18988805/
  - https://pubmed.ncbi.nlm.nih.gov/40532686/
  - https://pubmed.ncbi.nlm.nih.gov/40200774/
  - https://www.proteinatlas.org/ENSG00000004478-FKBP4/tissue
  - https://www.ema.europa.eu/en/medicines/human/EPAR/rapamune
  - https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE282532
  - https://raw.githubusercontent.com/wckdboy/openendo/main/docs/research/evidence/m3-validation.md
  - https://raw.githubusercontent.com/wckdboy/openendo/main/docs/research/evidence/registry-verification-2026-09-14.md
  - https://raw.githubusercontent.com/wckdboy/openendo/main/docs/data/repurposing_candidates.json
confidence: medium
---

# Sirolimus (rapamycin)

Oral **mTOR inhibitor** (macrolide immunosuppressant). Rank **1 (TOP TIER)** in
OpenEndo's M3 repurposing screen for endometriosis — as a *research priority*,
not a treatment recommendation. See [[computational-drug-repurposing]].

## What it is

- Approved for **renal-transplant rejection prophylaxis** and
  **lymphangioleiomyomatosis (LAM)**.^[https://www.ema.europa.eu/en/medicines/human/EPAR/rapamune] Cancer indications belong to the
  rapalog *everolimus/temsirolimus*, not sirolimus itself.
- Mechanism: sirolimus binds the immunophilin **FKBP12**, and the
  sirolimus–FKBP12 complex inhibits **mTORC1**. The M3 ChEMBL screen hit
  (pchembl 8.38 vs FKBP4, CHEMBL4050) reflects binding promiscuity across the
  FKBP family — it is *not* the drug's patient-facing pharmacology.
- Naming note: **FKBP4** (gene) = **FKBP52** (protein); **FKBP5** = FKBP51.
  Sirolimus binds FKBP12 (gene *FKBP1A*), a different family member.

## Why it surfaced (M3)

The screen pairs approved drugs with measured potency against novel
endometriosis targets. The FKBP4 pair is mechanistically interesting —
FKBP52 is the **progesterone-receptor co-chaperone** that enhances PR
transcriptional activity, and PR resistance is central to endometriosis —
but sirolimus ranks on its **own** mechanism (mTOR), which has independent
endometriosis evidence.^[https://raw.githubusercontent.com/wckdboy/openendo/main/docs/data/repurposing_candidates.json]

## Endometriosis evidence (verified 2026-09-02; registry re-checked 2026-09-14)

- **Review:** mTOR pathway is activated in endometriosis; mTOR inhibitors show
  efficacy as monotherapy in models and may relieve hormonal-therapy
  resistance — narrative review, *Mol Hum Reprod* 2024.^[https://pubmed.ncbi.nlm.nih.gov/39579091/]
- **Animal model:** rapamycin reduces endometriosis lesions in mice, *Exp Ther
  Med* 2016.^[https://pubmed.ncbi.nlm.nih.gov/27347023/]
- **Infertility + ovarian senescence:** in a mouse endometriosis model,
  rapamycin improved endometriosis-related infertility via the
  **PPARα/IGFBP2 pathway** — reduced ovarian senescence markers (p16, p21,
  γH2AX) and oxidative stress, improved ovarian/fertility endpoints, *Mol Med
  Rep* 2026.^[https://pubmed.ncbi.nlm.nih.gov/41170754/]
- **Human corollary (retrospective):** in an IVF cohort of 168 endometriosis
  patients (80 treated), 3 months of rapamycin lowered senescence/oxidative
  markers in follicular fluid and improved oocyte/fertilization outcomes,
  *Reprod Biomed Online* 2024. No trial registration reported; reflects
  off-label use in one centre.^[https://pubmed.ncbi.nlm.nih.gov/37914557/]
- **Pathway context (2025–2026, not sirolimus trials):** S1PR4 promotes ectopic
  stromal-cell viability, invasion and glycolysis via mTOR signalling, with the
  mTOR inhibitor AZD8055 used as a pathway tool in vitro.^[https://pubmed.ncbi.nlm.nih.gov/40532686/]
  A preliminary Iranian case–control study reported associations between
  PIK3CA / AKT1 / mTOR SNPs and endometriosis susceptibility.^[https://pubmed.ncbi.nlm.nih.gov/40200774/]
  These support pathway relevance; they do **not** upgrade clinical evidence for
  sirolimus.
- **No registered interventional trial** of rapamycin/sirolimus/everolimus/
  temsirolimus/or “mTOR” as intervention in endometriosis (or endometrioma) on
  ClinicalTrials.gov — re-queried API v2 on **2026-09-14** (0 hits; dienogest
  control still 40). Novelty remains high; clinical trial evidence remains
  absent.^[https://raw.githubusercontent.com/wckdboy/openendo/main/docs/research/evidence/registry-verification-2026-09-14.md]

## The FKBP4/progesterone-resistance link *(separate axis — do not conflate)*

FKBP52 (FKBP4) governs normal PR function: FKBP52 deficiency confers uterine
progesterone resistance *in vivo*,^[https://pubmed.ncbi.nlm.nih.gov/17571166/]
and *Fkbp52*⁻/⁻ mice develop progesterone-resistant endometriosis with
enhanced lesion growth.^[https://pubmed.ncbi.nlm.nih.gov/18988805/] In women,
FKBP4 mRNA is **reduced** in the endometrium of endometriosis patients, in
part via HOXA10^[https://pubmed.ncbi.nlm.nih.gov/22279148/] and
miR-29c^[https://pubmed.ncbi.nlm.nih.gov/27778641/] — a plausible contributor
to progesterone resistance.

**Uncertainty flag:** restoring FKBP4 is a *different* drug problem than mTOR
inhibition. Phase 1.0 docking (2026-09-04) showed rapamycin can engage FKBP52
(−6.38 kcal/mol vs FKBP12 −7.06), which is consistent with ChEMBL binding
promiscuity, but that does **not** mean sirolimus clinically restores PR
signalling. Keep mTOR (TOP TIER) and FKBP4/PR-resistance as linked-but-separate
research notes.

## Expression cross-check (GTEx/HPA + GEO reanalysis)

FKBP4 is strongly expressed in normal endometrium (HPA consensus nTPM 30.6,
IHC high; GTEx uterus 43.5 TPM) and reduced — not absent — in disease. The
target is present at the disease site. Full table:
`docs/research/evidence/m3-validation.md`.^[https://www.proteinatlas.org/ENSG00000004478-FKBP4/tissue]

GEO reanalysis (GSE282532; 5 paired eutopic/ectopic RNA-seq; Peking University
First Hospital, public Nov 2025) confirms FKBP4 is **2.2x lower in ectopic
lesions** (mean 32.5 vs 14.6 FPKM; FC 0.45; consistent across all 5 pairs).
This independently confirms the HOXA10/miR-29c literature and validates that
FKBP4 reduction is a lesion-level feature, not an artifact of bulk-tissue
comparison. Source: NCBI GEO, GSE282532
(2026-09-03).^[https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE282532]

## Caveats

- Chronic immunosuppression, teratogenicity and drug-drug interactions make
  systemic sirolimus a heavy intervention for a benign chronic disease.
- Evidence is preclinical + one retrospective cohort + pathway genetics —
  hypothesis-generating research output, **never treatment advice**. Talk to a
  specialist about actual endometriosis care (e.g. [[gnrh-antagonists]] such as
  [[ryeqo]]).
- Phase 2 MD (FKBP12 crystal RAP control → FKBP52 Vina pose) remains blocked on
  GPU budget — docking alone does not settle pose claims. Partner-ready mTOR PD
  spec (no GPU): `docs/research/lab-protocols/01-sirolimus-mtor-fkbp4-pr.md`.

## Related

[[computational-drug-repurposing]] · [[gnrh-antagonists]] · [[ryeqo-vs-yselty]] · [[mrgprx2-pain]] · [[ferroptosis]]
