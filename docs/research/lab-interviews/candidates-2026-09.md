---
title: "T7 Phase A — Danish Endometriosis Lab Shortlist (September 2026)"
created: "2026-09-03"
updated: "2026-09-03"
type: "research-planning"
tags: ["T7", "lab-interviews", "endometriosis", "denmark", "ELN", "digital-workflows"]
sources:
  - https://clin.au.dk/obgyn/research/endometriosis
  - https://pure.au.dk/portal/en/projects/finding-endometriosis-using-machine-learning/
  - https://research.regionh.dk/en/persons/mette-elkjaer-madsen/
  - https://portal.findresearcher.sdu.dk/en/persons/peter-martin-rudnicki/
  - https://www.rigshospitalet.dk/english/departments/juliane-marie-centre/fertility-department/laboratory-of-reproductive-biology/sider/default.aspx
confidence: medium
---

# T7 Phase A — Danish Endometriosis Lab Shortlist (September 2026)

> **Purpose:** Identify 3–5 Danish research groups with active endometriosis /
> pelvic-pain / women's-health programs as interview candidates for T7
> (lab-software modernization). The goal is to understand real ELN / digital
> workflow pain points in endometriosis research contexts — not general
> analytical chemistry labs. Phase B (human step) = conduct the interviews and
> publish anonymized write-ups.
>
> See also: [[lab-software-modernization]], [[interview-guide-dk]],
> [[danish-registries]]

---

## Selection criteria

1. **Active endometriosis / pelvic-pain / women's-health research** — ongoing
   projects, recent publications (2023–2026), not historical only.
2. **Lab-software surface** — clinical data pipelines, ELN or LIMS use,
   digital patient-reported outcomes, or omics/biobank workflows where
   tooling modernization is plausible.
3. **Reachability** — public institutional contact path; no personal emails or
   phones in this document.
4. **Geographic diversity** — cover more than one Danish city/region.

---

## Shortlist

### 1. Aarhus University — Department of Public Health, Epidemiology Group (Dorte Rytter group)

- **Institution / dept:** Department of Public Health — Epidemiology,
  Aarhus University (AU), Aarhus
- **City:** Aarhus
- **Research focus:** Registry-based endometriosis epidemiology using Danish
  national health registers (DNPR, Rx, MBR). EU Horizon 2020 FEMaLe project
  (2021–2025) — multi-omics platform, machine-learning diagnostics, 60,000+
  women surveyed (Cyklus2023 cohort). Current focus: causes and consequences of
  endometriosis, diagnostic delay, comorbidities.
- **Why a good fit:** Large-scale cohort and registry studies generate complex
  data management needs — data cleaning, linkage pipelines, analysis
  environments. Open-data ethos (FEMaLe used open protocol). Likely friction
  around research data management, version control, reproducibility tooling.
  Overlap with OpenEndo's registry analytics workstream.
- **Public source:** https://pure.au.dk/portal/en/projects/finding-endometriosis-using-machine-learning/
  and https://www.au.dk/en/show/person/dr@ph.au.dk

---

### 2. Aarhus University Hospital — Dept of Obstetrics and Gynaecology (FEMaLe / MY-ENDO)

- **Institution / dept:** Department of Clinical Medicine — Obstetrics and
  Gynaecology, Aarhus University Hospital (AUH), Aarhus N
- **City:** Aarhus
- **Research focus:** FEMaLe clinical decision-support tools; MY-ENDO RCT
  (NCT06211231, recruiting 2024–2026) — digital mindfulness/ACT-based
  self-management for chronic pelvic pain in endometriosis. Multi-site trial
  with AUH + Danish Endometriosis Patients Association (Billund).
- **Why a good fit:** Running a digital-health clinical trial with structured
  symptom data collection alongside conventional clinical EHR workflows — a
  setting where ELN / data-capture friction is acutely felt. Direct intersection
  with patient-outcome data management and trial software.
- **Public source:** https://clin.au.dk/obgyn/research/endometriosis
  and https://clinicaltrials.gov/study/NCT06211231

---

### 3. Rigshospitalet — Dept of Gynaecology, Fertility and Births (KU / Region H)

- **Institution / dept:** Department of Gynaecology, Fertility and Births,
  Rigshospitalet — Copenhagen University Hospital, Copenhagen
- **City:** Copenhagen
- **Research focus:** Clinical endometriosis research: diagnostic delay
  (including deep infiltrating and extra-pelvic disease), microbiome studies,
  Hugo robot-assisted surgery, Danish DSOG guideline development, phenome and
  biobanking harmonisation (WERF EPHect questionnaire — Danish translation and
  electronic migration). Active publications 2024–2026.
- **Why a good fit:** Biobank harmonization and electronic migration of
  research questionnaires are exactly the kind of digital-workflow problems that
  ELN/LIMS modernization addresses. The department handles biospecimen
  provenance, surgical data, and patient questionnaire data — high potential for
  tooling fragmentation.
- **Public source:** https://research.regionh.dk/en/persons/mette-elkjaer-madsen/
  and https://research.regionh.dk/en/publications/towards-deeper-understanding-of-endometriosis

---

### 4. OUH / SDU — Research Unit of Gynaecology and Obstetrics (Martin Rudnicki group)

- **Institution / dept:** KI, OUH, Research Unit of Gynaecology and Obstetrics,
  University of Southern Denmark (SDU) / Odense University Hospital (OUH), Odense
- **City:** Odense
- **Research focus:** Endometriosis digital patient-reported outcomes (telePROM
  — validated tele-PRO questionnaire + severity algorithm + "Mit Sygehus" app
  integration); pelvic organ prolapse; urogynecology RCTs. Active AI-diagnostics
  project (EndoMedBot, MedTech Odense, 2025–2026).
- **Why a good fit:** Already pioneering digital workflows in endometriosis
  follow-up (telePROM 2019–2025 validation; app-integrated PRO → medical record).
  This is the most digitally advanced endometriosis clinical unit in DK — a
  strong comparative reference for where lab/data tooling lags. Insight into
  what works and what the next friction layer is.
- **Public source:** https://portal.findresearcher.sdu.dk/en/persons/peter-martin-rudnicki/
  and https://www.sdu.dk/da/forskning/gynaekologiobstetrik

---

### 5. Rigshospitalet — Laboratory of Reproductive Biology (LRB)

- **Institution / dept:** Laboratory of Reproductive Biology, Juliane Marie
  Centre, Fertility Department, Rigshospitalet, Copenhagen
- **City:** Copenhagen
- **Research focus:** Non-invasive diagnostic test for endometriosis (Tanni
  Borgbo, "Endometriosis Uncovered" — Hans og Oda Svenningsen Foundation grant
  2025); epigenetic changes in endometriosis (MSc thesis 2026); ovarian
  physiology and fertility preservation. National tissue bank for cryopreserved
  gonadal tissue. Research publications 2025–2026.
- **Why a good fit:** Translational wet-lab research on endometriosis
  biomarkers — sample handling, assay data capture, biobank provenance — a
  classic ELN use-case. Small research unit (6–10 people), typical of the
  "no IT budget but real data" profile that OSS ELN addresses.
- **Public source:** https://www.rigshospitalet.dk/english/departments/juliane-marie-centre/fertility-department/laboratory-of-reproductive-biology/sider/default.aspx
  and LinkedIn: Laboratory of Reproductive Biology - Rigshospitalet

---

## Prioritization for outreach order

| Priority | Group | Key angle |
|----------|-------|-----------|
| 1 | OUH/SDU (Rudnicki) | Already digital — contrast/next-layer friction |
| 2 | LRB (Borgbo) | Wet-lab ELN classic use-case; small unit, accessible |
| 3 | Rigshospitalet Gyn (Madsen) | Biobank + questionnaire migration needs |
| 4 | AU Public Health (Rytter) | Registry/data management at scale |
| 5 | AUH Gyn/Obs (MY-ENDO) | Trial data + digital health friction |

---

## Honest limits and notes

- No personal email addresses or phone numbers in this document; all contacts
  via public institutional channels only.
- "Reach" paths are department-level public channels (contact forms /
  institutional email) unless an existing OpenEndo network contact exists.
- Corporate / pharma labs (Novo Nordisk, Lundbeck) were explicitly excluded —
  the endometriosis research angle is weak there and access barriers are high.
- Patient organisation Endometrioseforeningen (endometriose.dk) is a secondary
  contact path for warm introductions to clinical groups, not itself an
  interview subject.

---

*Phase A by Hermes (cron, 2026-09-03). Sources: institutional research portals,
ClinicalTrials.gov, Europe PMC, LinkedIn (public posts). No PII. See
[[lab-software-modernization]] for T7 context.*
