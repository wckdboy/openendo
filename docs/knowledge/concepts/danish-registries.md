---
title: Danish Registries for Endometriosis Research
created: 2026-09-02
updated: 2026-09-02
type: concept
tags: [denmark, research, policy]
sources:
  - https://pubmed.ncbi.nlm.nih.gov/40795622/
  - https://pubmed.ncbi.nlm.nih.gov/35434780/
  - https://pubmed.ncbi.nlm.nih.gov/39704775/
  - https://pubmed.ncbi.nlm.nih.gov/37581901/
  - https://pubmed.ncbi.nlm.nih.gov/42295201/
  - https://pubmed.ncbi.nlm.nih.gov/35218204/
  - https://pubmed.ncbi.nlm.nih.gov/27743699/
confidence: high
---

# Danish Registries for Endometriosis Research

Denmark maintains a set of nationwide administrative and clinical registers that together form
one of the world's richest data infrastructures for population-scale health research. For
endometriosis, these registers are particularly valuable: the disease has a long diagnostic
delay (7–10 years on average), affects a large fraction of reproductive-aged women, and has
poorly understood long-term systemic consequences — all questions that require large, unselected,
longitudinal cohorts. Despite this potential, Danish registry data has been **underutilised**
for endometriosis to date, and the validation of key diagnostic codes is still recent work.

## Key registers

| Register | Content | Coverage |
|----------|---------|----------|
| **Danish National Patient Register (DNPR / LPR)** | Hospital diagnoses (ICD-10), procedures, outpatient contacts | Nationwide, 1977-present |
| **Danish Medical Birth Registry (MBR)** | Births, maternal diagnoses, obstetric outcomes | Nationwide, 1973-present |
| **Danish Prescription Register** | All redeemed prescriptions (ATC code, date, pharmacy) | Nationwide, 1994-present |
| **Danish Psychiatric Central Research Register** | Psychiatric diagnoses + contacts | Nationwide, 1969-present |
| **Danish Civil Registration System (CPR)** | Linkage key — all Danish residents have a unique CPR number | Nationwide, 1968-present |
| **Cause of Death Register** | Mortality causes | Nationwide, 1970-present |

All registers are linkable via the CPR number (anonymised for research), enabling multi-register
cohort designs without additional recruitment or consent burden. Statistics Denmark manages
access for approved research projects.

## Validity of the endometriosis diagnosis code

The DNPR uses ICD-10 N80.x codes for endometriosis. A 2025 validation study (Thomsen et al.,
Eur J Obstet Gynecol) assessed the **positive predictive value (PPV)** of endometriosis codes
in the DNPR for the period 1995–2018 using a sample of 300 patient records.^[https://pubmed.ncbi.nlm.nih.gov/40795622/]
This study is the prerequisite for any register-based endometriosis research: without knowing
the PPV, observed associations may be confounded by misclassification. The finding that overall
data quality in the DNPR is high, but that code accuracy varies across ICD chapters and time
periods, means researchers must account for period-specific PPV when using historical data.

## What Danish registry research has found

### Diagnostic delay in healthcare utilization

A 2023 Danish case-control study (Melgaard et al., Human Reproduction) showed women later
diagnosed with endometriosis had *significantly higher* healthcare utilisation in **all 10 years
prior to diagnosis** compared to controls without endometriosis — across both primary and
secondary care.^[https://pubmed.ncbi.nlm.nih.gov/37581901/] A 2025 follow-up (same group)
used ICD-10 chapter-level analysis to show that the excess contacts spanned nearly all
diagnostic categories, suggesting diffuse, poorly characterised pre-diagnosis morbidity — not
a specific symptom cluster.^[https://pubmed.ncbi.nlm.nih.gov/39704775/] These are the most
comprehensive quantifications of the diagnostic delay burden available for Denmark.

### Incidence: temporal and regional variation

A 2022 population-based study (Illum et al., Acta Obstet Gynecol Scand) found significant
**temporal and regional differences** in hospital-diagnosed endometriosis incidence across
Denmark, linked to varying awareness, socioeconomic factors, distance to specialised referral
centres and diagnostic capacity.^[https://pubmed.ncbi.nlm.nih.gov/35434780/] This is direct
evidence that "incidence" in registry data is partly a measure of diagnostic access — a
critical caveat for any trend analysis.

### Obstetric and perinatal outcomes

Using the DNPR linked to the Medical Birth Registry:

- **Preterm birth**: Women with endometriosis had higher risk of preterm birth across multiple
  gestational-age categories, with distinct pathways (spontaneous preterm labour, PPROM, and
  medically indicated).^[https://pubmed.ncbi.nlm.nih.gov/35218204/] (Breintoft et al. 2022,
  Aarhus Birth Cohort, n = large DK singleton cohort.)
- **Pregnancy complications**: Women with endometriosis had elevated risk of pre-eclampsia,
  caesarean section, postpartum haemorrhage, preterm birth and small-for-gestational-age, even
  after adjusting for fertility treatment.^[https://pubmed.ncbi.nlm.nih.gov/27743699/]
  (Glavind et al. 2017, Aarhus Birth Cohort, n = 82,793 pregnancies.)

### Mental health burden

A 2026 registry-based study (Josiasen et al., Human Reproduction) quantified antidepressant
and anxiolytic prescriptions and psychiatric hospital contacts in women with and without
endometriosis. Women with endometriosis redeemed more prescriptions for antidepressants and
anxiolytics **both before and after** the endometriosis diagnosis, and had more psychiatric
contacts for depression and anxiety.^[https://pubmed.ncbi.nlm.nih.gov/42295201/] The pre-
diagnosis excess mirrors the healthcare-utilisation pattern and suggests that mental health
burden is part of the uncharacterised pre-diagnostic period, not merely a consequence of
receiving the diagnosis.

## Underutilisation and opportunity

The weekly digest (2026-09-01) notes that Denmark's national registries are "among the world's
best for population-scale endometriosis research — barely used for this disease." The recent
work cited above (2022–2026) represents a growing but still thin evidence base relative to the
registry infrastructure available. Key open questions include:

- Long-term systemic comorbidities (cardiovascular, autoimmune) with registry ascertainment
- Pharmacoepidemiology of GnRH antagonist and progestin treatment patterns at population scale
- Linkage to biobank data (DBDS, Danish Blood Donor Study) for -omics integration
- Socioeconomic stratification of diagnostic delay and care access
- Nordic cross-registry cohorts (Denmark + Sweden/Norway/Finland linkage via NOMESKO protocols)

## Relevance to OpenEndo

The OpenEndo agenda explicitly includes a **registry and EHR analytics** workstream (high
impact). The Danish registry infrastructure is the primary entry point because:

1. Code validity has been recently established (Thomsen 2025 PPV study)
2. Key outcome associations (obstetric, psychiatric, pre-diagnostic utilisation) are mapped
3. Linkage to the Prescription Register enables treatment-outcome studies at zero recruitment cost
4. CPR-based linkage eliminates loss-to-follow-up for long-term studies
5. Nordic collaboration potential amplifies sample size for rare outcomes

OpenEndo's data pipeline should track new DNPR-based endometriosis studies (weekly PubMed
search: "endometriosis[tiab] AND Denmark[tiab]") and flag registry study metadata (sample size,
registers used, PPV applied) for the living evidence synthesis.

## Related pages

- [[my-endo-trial]] — active Danish trial (NCT06211231) recruiting now
- [[diversity-gap]] — registry-based evidence is essential to close the diversity gap in endo research
- [[gnrh-antagonists]] — first-line treatment class; treatment-pattern pharmaepidemiology feasible via DNPR + Rx register
- [[saliva-diagnostics]] — non-invasive diagnostics could shorten the delay documented in DK registry studies

## Sources

| PMID | Authors | Year | Title |
|------|---------|------|-------|
| 40795622 | Thomsen et al. | 2025 | Validation of endometriosis diagnosis code in DNPR 1995-2018 (Eur J Obstet Gynecol) |
| 35434780 | Illum et al. | 2022 | Temporal and regional differences in incidence of hospital-diagnosed endometriosis in Denmark (AOGS) |
| 39704775 | Melgaard et al. | 2025 | Pre-diagnosis hospital contacts using ICD-10: Danish case-control (Human Reprod) |
| 37581901 | Melgaard et al. | 2023 | Healthcare utilisation prior to endometriosis diagnosis: Danish case-control (Human Reprod) |
| 42295201 | Josiasen et al. | 2026 | Endometriosis and mental health burden: registry-based prescriptions + psychiatric contacts (Human Reprod) |
| 35218204 | Breintoft et al. | 2022 | Endometriosis and preterm birth: Danish cohort study (AOGS) |
| 27743699 | Glavind et al. | 2017 | Endometriosis and pregnancy complications: Danish cohort study (Fertil Steril) |
