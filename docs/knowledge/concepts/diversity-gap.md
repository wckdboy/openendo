---
title: Diversity Gap in Endometriosis Research
created: 2026-09-02
updated: 2026-09-02
type: concept
tags: [research, policy, advocacy]
sources:
  - https://pubmed.ncbi.nlm.nih.gov/30738028/
  - https://pubmed.ncbi.nlm.nih.gov/40928122/
  - https://pubmed.ncbi.nlm.nih.gov/40841635/
  - https://pubmed.ncbi.nlm.nih.gov/38564184/
  - https://pubmed.ncbi.nlm.nih.gov/28417349/
confidence: high
---

# Diversity Gap in Endometriosis Research

Endometriosis affects an estimated 190 million people of reproductive age worldwide, yet the
evidence base that informs diagnosis and treatment has been built primarily on White, Western,
high-income-country populations. This under-representation of racial, ethnic, socioeconomic
and geographic diversity in research cohorts and clinical trials is the **diversity gap** — a
structural problem with direct consequences for diagnosis equity, treatment access and scientific
validity.

## Historical framing: "a White woman's disease"

Early epidemiological literature described endometriosis as more prevalent in White women and
rare in Black and Asian women — a claim that influenced clinical heuristics for decades. A 2019
review in AJOG revisited this framing and found it rested on **methodological and social bias**
rather than biology: the studies that established the race-prevalence association used hospital
registry data collected at a time when Black women had systematically less access to specialist
care and laparoscopic diagnosis.^[https://pubmed.ncbi.nlm.nih.gov/30738028/] The review
concluded there is no established biological basis for a racial difference in susceptibility;
observed disparities are better explained by differential access to diagnosis.^[https://pubmed.ncbi.nlm.nih.gov/30738028/]

A 2017 IVF-cohort study found a *higher* prevalence of endometriosis among Asian women than
White women in the same clinical setting, and endometriosis diagnosis did not worsen IVF
outcomes regardless of ethnicity — illustrating that apparent "racial" patterns shift depending
on access to care.^[https://pubmed.ncbi.nlm.nih.gov/28417349/]

## Clinical trial representation

A 2025 BJOG analysis examined racial and ethnic representation in clinical trials that supported
FDA approval of endometriosis treatments. The study found significant under-representation of
non-White participants relative to disease burden, meaning approved therapies have limited
evidence for their safety and efficacy profiles in the full patient population.^[https://pubmed.ncbi.nlm.nih.gov/40928122/]
This is not a minor gap: pharmacokinetic, comorbidity and pain-phenotype differences can
interact with treatment response in ways a homogeneous trial population cannot detect.

## Lived experience: Black women with endometriosis in the US

A 2025 qualitative study (BMC Women's Health) interviewed 16 Black women in the US diagnosed
with endometriosis. Participants described a pattern of dismissed symptoms, delayed diagnosis
and poor patient-provider communication — consistent with the broader literature on medical
racism, but compounding the already long (7–10 year) endometriosis diagnostic delay.^[https://pubmed.ncbi.nlm.nih.gov/40841635/]
Themes included feeling that their pain was not believed and difficulty navigating specialist
referral systems. The study highlights that the diversity gap is not only a data problem but
a care-delivery problem.

## Socioeconomic and geographic dimensions

A 2024 multinational study (Pain journal) of women with endometriosis from Latin America and
Spain found high pain-catastrophizing scores and significant variation in pain perception
associated with socioeconomic factors and self-identified race.^[https://pubmed.ncbi.nlm.nih.gov/38564184/]
The study underscored that endometriosis phenotype — particularly pain burden — is modulated
by context factors largely invisible to trials conducted in high-income Western settings.

## Why it matters for OpenEndo

The diversity gap is directly relevant to the OpenEndo mission in two ways:

1. **Data collection signals** — the OpenEndo data pipeline should track participant diversity
   (race/ethnicity, country, socioeconomic setting) when ingesting study metadata. Studies that
   restrict their sample to a single demographic should be flagged and their findings qualified.

2. **Translation agenda** — making research outputs available in multiple languages (patient
   tools, trial information, knowledge pages) is not cosmetic: it is evidence-backed advocacy
   for the communities most underserved by current research. The weekly digest notes (2026-09-01)
   that the diversity gap paper directly supports OpenEndo's multilingual access agenda.

## Open questions

- Does the diversity gap in trial populations affect the apparent efficacy of currently approved
  drugs (GnRH antagonists, progestins) in non-White and lower-income-country settings?
  *Confidence: low — no comparative effectiveness data available.*
- Are there differences in [[ferroptosis]] or mTOR-pathway activity across ancestry groups that
  would affect [[computational-drug-repurposing]] candidate translation? *Unknown; would require
  ancestry-stratified transcriptomic studies.*

## Related pages

- [[computational-drug-repurposing]] — M3 candidate screen should account for population diversity
- [[ferroptosis]] — mechanistic target; representation across ancestries not yet characterised
- [[saliva-diagnostics]] — non-invasive diagnostics could reduce access barriers that drive the gap
- [[gnrh-antagonists]] — approved on trials with limited diversity representation

## Sources

| PMID | Authors | Year | Title |
|------|---------|------|-------|
| 30738028 | Bougie et al. | 2019 | Behind the times: revisiting endometriosis and race (AJOG) |
| 40928122 | Meyer et al. | 2025 | Disparities in Racial and Ethnic Representation in Clinical Trials for FDA-Approved Treatments of Endometriosis (BJOG) |
| 40841635 | Rice et al. | 2025 | "It's like your body is fighting against you": QOL in U.S. Black women with endometriosis (BMC Women's Health) |
| 38564184 | Flores et al. | 2024 | Moderators of pain perception: sociodemographics, racial self-identity, pain catastrophizing in Latin America/Spain (Pain) |
| 28417349 | Yamamoto et al. | 2017 | Higher prevalence in Asian women does not contribute to poorer IVF outcomes (J Assist Reprod Genet) |
