# Knowledge Log

> Chronological record of knowledge base actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete

## [2026-09-02] create | Knowledge base initialized
- Domain: endometriosis research, treatment, diagnostics, funding, policy + project
- Structure: SCHEMA.md, index.md, log.md, entities/, concepts/, comparisons/, queries/, raw/
- Seeded from verified research of 2026-09-01/02 (European approvals, Danish access, pipeline)
- Pages: ryeqo, yselty, hmi-115, gnrh-antagonists, saliva-diagnostics, ryeqo-vs-yselty

## [2026-09-02] update | yselty — DK status verified → confidence high
- Primary sources: EMA product information (SmPC), Medicintilskudsnævnets indstilling (Nov 2023), NICE TA1067
- Verified: EU endometriosis approval 20 Dec 2024; endometriosis dose 200 mg + ABT; DK generelt klausuleret tilskud covers fibroids only — no general reimbursement for endometriosis

## [2026-09-02] create | my-endo-trial (entity) — NCT06211231
- Aarhus University; digital mindfulness/acceptance self-management; recruiting; inclusion/exclusion summary from CT.gov

## [2026-09-02] create | ferroptosis (concept)
- SEMA3C→ferroptosis paper (PMID 42678895) + autophagy/ferroptosis review (PMID 42660839); GPX4/SLC7A11 target overlap; sulfasalazine M3 convergence

## [2026-09-02] create | computational-drug-repurposing (concept)
- Oskotsky simvastatin/primaquine POC (PMID 42668641) + M3 ChEMBL screen (9 pairs); validation ladder

## [2026-09-02] update | ryeqo-vs-yselty — DK access + no-hormone claim corrected per EU SmPC

## [2026-09-02] create | sirolimus (entity) — M3 repurposing rank 1
- mTOR inhibitor; FKBP12→mTORC1 pharmacology (FKBP4 ChEMBL hit = family promiscuity, not mechanism)
- Sources verified: mTOR review Mol Hum Reprod 2024 (PMID 39579091); rapamycin mouse model Exp Ther Med 2016 (PMID 27347023); PPARα/IGFBP2 ovarian-senescence mouse study Mol Med Rep 2026 (PMID 41170754); retrospective IVF cohort RBMO 2024 (PMID 37914557); FKBP52/PR-resistance papers (PMID 17571166, 18988805, 22279148, 27778641); EMA Rapamune EPAR
- Cross-checked: no registered mTOR-inhibitor trial in endometriosis on ClinicalTrials.gov (2026-09-02)

## [2026-09-02] create | mrgprx2-pain (concept) — mast-cell pain axis
- FASEB J 2025 (PMID 40600649): MRGPRX2⁺ mast cells ↑ in lesions; HBD-2→MRGPRX2→histamine→HRH1/TRPV1 DRG sensitization drives pain (year corrected from 2026)
- Mast-cell/pain background: Anaf 2006 (PMID 17007852), IJBS 2025 (PMID 41079937), AJRI 2025 (PMID 40028674), Front Physiol 2019 (PMID 31998139)
- M3 cetrorelix pair resolved: measured µM *agonism* vs MRGPRX2 (Lansu, Nat Chem Biol 2017, PMID 28288109) → target-validating for antagonist development, not repurposing; cetrorelix 3 mg/weekly regimen rests on 2002 studies (PMID 12537785, 12470539); NCT00244452 no results

## [2026-09-03] update | sirolimus + mrgprx2-pain — GEO reanalysis (GSE282532)
- Dataset: NCBI GEO GSE282532 (Zhu et al., Peking Univ First Hospital; 5 paired eutopic/ectopic RNA-seq FPKM; public Nov 2025)
- FKBP4: eutopic 32.5 FPKM vs ectopic 14.6 FPKM (FC 0.45; 2.2x DOWN in lesions); consistent across all 5 pairs — confirms PR-resistance literature (HOXA10/miR-29c suppression)
- MRGPRX2: below detection in bulk as expected; mast-cell markers CPA3 (13.6x), TPSAB1 (15.0x), TPSB2 (11.0x) all strongly enriched in ectopic tissue — independent confirmation of FASEB J 2025 mast-cell density finding
- SLC7A11: 2x down; ACSL4: 2.4x down — consistent with ferroptosis evasion via suppression (not overexpression of resistance nodes)
- phase0.5.md status updated: dataset done, GSE247695/263897 remain open

## [2026-09-02] create | diversity-gap (concept) — wiki ingest part 2
- 5 PMIDs (2017-2025): Bougie 2019 AJOG (race bias in historical literature); Meyer 2025 BJOG (FDA trial representation); Rice 2025 BMC (Black women QOL); Flores 2024 Pain (Latin America/Spain); Yamamoto 2017 (Asian women IVF cohort)
- Key finding: no established biological basis for racial prevalence difference; disparities explained by access, not biology
- OpenEndo implications: diversity signals in data pipeline + multilingual translation agenda

## [2026-09-02] create | danish-registries (concept) — wiki ingest part 2
- 7 PMIDs (2017-2026): Thomsen 2025 PPV validation; Illum 2022 temporal/regional incidence; Melgaard 2023 + 2025 pre-diagnosis utilisation; Josiasen 2026 mental health; Breintoft 2022 preterm birth; Glavind 2017 pregnancy complications
- CPR-linkage + DNPR/Rx/MBR/psychiatric register overview; code validity caveats; underutilisation for endo highlighted
- OpenEndo agenda: registry+EHR analytics workstream entry point
