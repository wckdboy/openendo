---
title: Sirolimus (rapamycin)
created: 2026-09-02
updated: 2026-09-02
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
  - https://www.proteinatlas.org/ENSG00000004478-FKBP4/tissue
  - https://www.ema.europa.eu/en/medicines/human/EPAR/rapamune
  - https://raw.githubusercontent.com/wckdboy/openendo/main/docs/research/evidence/m3-validation.md
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

## Endometriosis evidence (verified 2026-09-02)

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
- **No registered interventional trial** of rapamycin/sirolimus/any mTOR
  inhibitor in endometriosis on ClinicalTrials.gov (checked 2026-09-02) —
  novelty is high, clinical evidence is absent.

## The FKBP4/progesterone-resistance link

FKBP52 (FKBP4) governs normal PR function: FKBP52 deficiency confers uterine
progesterone resistance *in vivo*,^[https://pubmed.ncbi.nlm.nih.gov/17571166/]
and *Fkbp52*⁻/⁻ mice develop progesterone-resistant endometriosis with
enhanced lesion growth.^[https://pubmed.ncbi.nlm.nih.gov/18988805/] In women,
FKBP4 mRNA is **reduced** in the endometrium of endometriosis patients, in
part via HOXA10^[https://pubmed.ncbi.nlm.nih.gov/22279148/] and
miR-29c^[https://pubmed.ncbi.nlm.nih.gov/27778641/] — a plausible contributor
to progesterone resistance. Caveat: restoring FKBP4 is a *different* drug
problem than mTOR inhibition; the two axes should not be conflated.

## Expression cross-check (GTEx/HPA)

FKBP4 is strongly expressed in normal endometrium (HPA consensus nTPM 30.6,
IHC high; GTEx uterus 43.5 TPM) and reduced — not absent — in disease. The
target is present at the disease site. Full table:
`docs/research/evidence/m3-validation.md`.^[https://www.proteinatlas.org/ENSG00000004478-FKBP4/tissue]

## Caveats

- Chronic immunosuppression, teratogenicity and drug-drug interactions make
  systemic sirolimus a heavy intervention for a benign chronic disease.
- Evidence is preclinical + one retrospective cohort — hypothesis-generating
  research output, **never treatment advice**. Talk to a specialist about
  actual endometriosis care (e.g. [[gnrh-antagonists]] such as [[ryeqo]]).

## Related

[[computational-drug-repurposing]] · [[gnrh-antagonists]] · [[ryeqo-vs-yselty]]
