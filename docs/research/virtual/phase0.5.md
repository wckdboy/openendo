# Virtual testing — Phase 0.5: lesion-expression cross-check (first pass)

**Owner:** Percival (delegated from Jaeger 2026-09-02) · **Status:** first
pass done — dataset list ready, per-dataset reanalysis is the next step
($0; GEO is open). Companion: `docs/research/virtual-testing.md` (pipeline
plan), `phase0.md` (structure/expression audit), `m3-validation.md`.

## Question

Are FKBP4 / MRGPRX2 / SLC7A11 (the M3 top targets) actually **elevated in
endometriosis lesions vs eutopic endometrium**? MRGPRX2 is "not detected" in
HPA normal bulk tissue — is it up on *lesional mast cells*?

## Method note (why bulk tissue is the wrong lens)

GTEx has no endometrium (proxy: whole uterus); HPA bulk RNA is dominated by
epithelial/stromal mass. For a mast-cell receptor (MRGPRX2) and an
inducible/stress-regulated transporter (SLC7A11), **lesion-vs-eutopic
comparisons need lesion-resolution data**: paired ectopic/eutopic
transcriptomes, single-cell or spatial data — i.e. GEO, not GTEx.

## Per-gene evidence table (verified 2026-09-02)

| Gene | Endometrium nTPM (HPA) | Uterus TPM (GTEx v8) | Lesional evidence (lit) | Verdict |
|---|---|---|---|---|
| FKBP4 | 30.6 (IHC high) | 43.5 | mRNA **↓** (not ↑) in eutopic EM endometrium (PMIDs [22279148](https://pubmed.ncbi.nlm.nih.gov/22279148/), [27778641](https://pubmed.ncbi.nlm.nih.gov/27778641/)) | Present & mechanistically linked (PR-resistance), but the M3 hypothesis is *reduced* FKBP4 → progesterone resistance — lesion-level direction must be checked in GEO |
| MRGPRX2 | 0.0 ("not detected") | 0.06 | MRGPRX2⁺ **mast-cell density ↑ in lesions**; drives pain via histamine/HRH1/TRPV1 (FASEB J 2025, PMID [40600649](https://pubmed.ncbi.nlm.nih.gov/40600649/)) | Plausible **via lesional mast cells only** — needs single-cell/spatial confirmation |
| SLC7A11 | 0.2 (not detected) | 0.12 | SLC7A11 **↓** in ectopic lesions (SEMA3C, PMID [42678895](https://pubmed.ncbi.nlm.nih.gov/42678895/)); SLC7A11↑ = ferroptosis-resistance node (PMID [41241001](https://pubmed.ncbi.nlm.nih.gov/41241001/)) | Bulk expression weak; lesion value is dynamic (resistance node), not constitutive — direction-of-effect handled in `ferroptosis-direction.md` |

## Candidate GEO datasets (real accessions, NCBI GEO query 2026-09-02)

Lesion-vs-eutopic / lesion-resolution human endometriosis datasets, ranked by
fit to the Phase 0.5 question:

| Accession | Samples | Design | Answers |
|---|---|---|---|
| GSE282532 | 10 | RNA-seq, **paired eutopic + ectopic** endometrium, ovarian endometriosis | FKBP4/SLC7A11 lesion vs eutopic (direct) |
| GSE247695 | 8 | **scRNA-seq**, lesions vs paired eutopic (metabolic activity) | Cell-type resolution — mast cells (MRGPRX2), stromal FKBP4/SLC7A11 |
| GSE263897 | 60 | **Spatial** transcriptomics, superficial peritoneal lesions | Mast-cell niches in situ (MRGPRX2) |
| GSE303635 | 20 | RNA-seq, stromal cells, lesion-type heterogeneity | Stromal FKBP4/SLC7A11 by lesion type |
| GSE202571 | 18 | RNA-seq, secretory eutopic endometrium with/without EM | Eutopic FKBP4 baseline (progesterone-resistance context) |
| GSE315857 | 8 | RNA-seq, proliferative eutopic endometrium in EM (PR downstream) | Eutopic FKBP4/PR axis |
| GSE240392 | 24 | Mouse EM model, eutopic + ectopic over progression | Longitudinal direction (mouse) |
| GSE303150 | 142 | Spatial, adenomyosis lesions (adjacent disease) | Immune signature incl. mast cells (context) |
| GSE226575 | 9 | RNA-seq, endometrial cyst → EAOC progression | Lesion progression axis (context) |
| GSE291656 | 18 | RT-PCR, peritoneal fluid NLRP3 (context) | Peritoneal immune environment |

Query used: NCBI eutils `db=gds`, `endometriosis[All Fields] AND eutopic[All
Fields] AND gse[Entry Type]` (96 hits; top 40 screened). **Nothing above is an
invented identifier — every accession was returned live by the NCBI API.**

## Next step (Phase 0.5 reanalysis, ~$0)

1. Pull GSE282532 + GSE247695 (series matrix / processed counts).
2. Per-gene lesion-vs-eutopic test: FKBP4, MRGPRX2 (with mast-cell markers
   e.g. TPSAB1/TPSB2, CPA3), SLC7A11 (+GPX4, ACSL4 ferroptosis panel).
3. If mast-cell signal present: MRGPRX2⁺-cell proportion/density readout
   cross-checked against FASEB J 2025 (PMID 40600649).
4. Write results back into this file (status → reanalysis done) + feed the
   M3 rows.

*Percival (Hermes Agent), 2026-09-02. Public data only; no PII. Research
infrastructure, not medical advice.*
