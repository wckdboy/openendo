# Virtual testing — Phase 0.5: lesion-expression cross-check

**Owner:** Percival · **Status:** GEO reanalysis COMPLETE (2026-09-03) —
all three prioritized datasets reanalyzed: **GSE282532** (bulk FPKM,
ovarian endometrioma), **GSE247695** (scRNA-seq, peritoneal lesions, PR
#19), **GSE263897** (GeoMx spatial, peritoneal lesions, PR #20).
FKBP4 reduced in endometrioma lesions confirmed (2.2x bulk; stroma-down
replicated in both peritoneal datasets); mast-cell enrichment 11–15x is an
**endometrioma** feature — **absent in superficial peritoneal lesions**
(two independent datasets agree, incl. a dropout-free GeoMx readout);
SLC7A11 reduced in endometrioma, no constitutive up-regulation in any
dataset (ferroptosis-evasion consistent). Companion:
`docs/research/virtual-testing.md` (pipeline plan), `phase0.md`
(structure/expression audit), `m3-validation.md`.

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

## Per-gene evidence table (verified 2026-09-02; GEO reanalysis 2026-09-03)

| Gene | Endometrium nTPM (HPA) | Uterus TPM (GTEx v8) | Lesional evidence (lit) | GSE282532 (GEO, 5 paired) | Verdict |
|---|---|---|---|---|---|
| FKBP4 | 30.6 (IHC high) | 43.5 | mRNA **↓** in eutopic EM endometrium (PMIDs [22279148](https://pubmed.ncbi.nlm.nih.gov/22279148/), [27778641](https://pubmed.ncbi.nlm.nih.gov/27778641/)) | eu mean 32.5 vs ec mean 14.6 FPKM; **FC = 0.45 (2.2x DOWN in lesion)**; all 5 pairs consistent | **Confirmed: FKBP4 reduced in ectopic lesions** — consistent with PR-resistance hypothesis; target present in eutopic baseline |
| MRGPRX2 | 0.0 ("not detected") | 0.06 | MRGPRX2+ **mast-cell density up in lesions**; drives pain via histamine/HRH1/TRPV1 (FASEB J 2025, PMID [40600649](https://pubmed.ncbi.nlm.nih.gov/40600649/)) | 0 FPKM in all 5 eutopic; trace signal in 3/5 ectopic (mean 0.02 FPKM) — **below detection in bulk** | Bulk undetectable as expected; mast-cell signal confirmed by CPA3/TPSAB1/TPSB2 (see below) |
| SLC7A11 | 0.2 (not detected) | 0.12 | SLC7A11 **down** in ectopic lesions (SEMA3C, PMID [42678895](https://pubmed.ncbi.nlm.nih.gov/42678895/)); SLC7A11 up = ferroptosis-resistance node (PMID [41241001](https://pubmed.ncbi.nlm.nih.gov/41241001/)) | eu mean 3.0 vs ec mean 1.5 FPKM; **FC = 0.50 (2x DOWN in lesion)** | **Confirmed direction:** SLC7A11 reduced in lesions — consistent with SEMA3C suppression; ferroptosis evasion operates via upstream regulators, not constitutive SLC7A11 overexpression |
| GPX4 | — | — | Core ferroptosis suppressor | eu 98.1 vs ec 79.7 FPKM; FC = 0.81 (modest decrease) | GPX4 present in lesions, modestly reduced — lesions are not constitutively ferroptosis-resistant via GPX4 overexpression |
| ACSL4 | — | — | Pro-ferroptosis lipid peroxidase | eu 74.7 vs ec 30.6 FPKM; **FC = 0.41 (2.4x DOWN in lesion)** | ACSL4 markedly down in lesions — lesions suppress pro-ferroptotic machinery (consistent with ferroptosis evasion; supports induction as therapeutic strategy) |

**Mast-cell markers (GSE282532) — MRGPRX2 proxy:**

| Marker | Eutopic FPKM | Ectopic FPKM | FC | Interpretation |
|---|---|---|---|---|
| CPA3 (carboxypeptidase A3) | 0.75 | 10.2 | **13.6x UP** | Canonical mast-cell marker; strong ectopic enrichment |
| TPSAB1 (tryptase alpha/beta 1) | 0.61 | 9.1 | **15.0x UP** | Canonical mast-cell marker; >10x in all 5 ectopic samples |
| TPSB2 (tryptase beta 2) | 0.88 | 9.7 | **11.0x UP** | Mast-cell marker; consistent across all pairs |

All three canonical mast-cell markers are 11-15x enriched in ectopic vs eutopic endometrium across all 5 paired samples. This is strong indirect evidence that MRGPRX2-expressing mast cells are substantially more abundant in **ovarian endometrioma** lesions, consistent with the FASEB J 2025 finding (PMID 40600649). Direct MRGPRX2 bulk signal is below detection (as expected for a receptor on a rare infiltrating cell type). **Important (2026-09-03): this enrichment does NOT replicate in superficial peritoneal lesions — see the mast-cell reconciliation in the GSE247695 and GSE263897 sections below.**

## GEO reanalysis performed (2026-09-03)

**Dataset:** GSE282532 (NCBI GEO; Zhu et al., Peking University First Hospital;
RNA-seq FPKM; Illumina HiSeq 2500; hg38/CLC 22.0.1; public Nov 2025).
Design: 5 patients with ovarian endometrioma, paired eutopic endometrium (EM)
vs ovarian ectopic endometrium (OMA); proliferative phase; no hormone therapy.
Data source: `GSE282532_mRNA_FPKM.xlsx` (FTP NCBI, 2026-09-03).

**Method:** sum FPKM across transcripts per gene per sample; compute mean and
SD across 5 patients for eutopic vs ectopic; fold-change = ectopic/eutopic.
No statistical test run (n=5; below threshold for formal testing); results
are directional evidence only.

**Key results:**

| Gene | Eutopic mean FPKM | Ectopic mean FPKM | FC | Interpretation |
|---|---|---|---|---|
| FKBP4 | 32.5 | 14.6 | 0.45 | 2.2x DOWN in lesions; consistent with HOXA10/miR-29c suppression + PR-resistance |
| MRGPRX2 | 0.00 | 0.02 | n/a | Below detection in bulk; mast-cell proxy markers strongly up (see above) |
| SLC7A11 | 3.0 | 1.5 | 0.50 | 2x DOWN in lesions; consistent with SEMA3C-mediated suppression |
| GPX4 | 98.1 | 79.7 | 0.81 | Modestly lower; not constitutively overexpressed in lesions |
| ACSL4 | 74.7 | 30.6 | 0.41 | 2.4x DOWN; pro-ferroptotic enzyme suppressed in lesions (ferroptosis evasion) |
| CPA3 | 0.75 | 10.2 | 13.6 | Mast-cell marker strongly enriched in lesions |
| TPSAB1 | 0.61 | 9.1 | 15.0 | Mast-cell tryptase; consistently high across all 5 ectopic |
| TPSB2 | 0.88 | 9.7 | 11.0 | Mast-cell tryptase; consistent across all pairs |

**Conclusions:**

1. **FKBP4:** reduced 2.2x in ectopic lesions — confirms the PR-resistance
   hypothesis and validates the target as present (and mechanistically
   perturbed) at the disease site. The M3 therapeutic angle (restore/modulate
   the mTOR-FKBP axis) remains plausible.
2. **MRGPRX2/mast cells:** MRGPRX2 bulk signal is below detection (expected;
   receptor restricted to mast cells and a few other rare cell types).
   However, canonical mast-cell markers (CPA3, TPSAB1, TPSB2) are 11-15x
   enriched in ectopic tissue in every paired sample. This independently
   confirms the FASEB J 2025 result (PMID 40600649) that mast-cell density is
   elevated in endometriotic lesions. MRGPRX2 as a target remains well-
   supported; single-cell or spatial data (GSE247695, GSE263897) are the next
   confirmation step — see the lesion-type reconciliation below.
3. **SLC7A11/ferroptosis:** SLC7A11 is 2x lower in ectopic tissue (consistent
   with SEMA3C suppression). ACSL4 is 2.4x lower. The ferroptosis-evasion
   phenotype is not via constitutive up-regulation of the SLC7A11/GPX4 axis
   — it appears to operate via upstream signalling or non-canonical nodes.
   This is consistent with the ferroptosis-direction verdict
   (`docs/research/evidence/ferroptosis-direction.md`): lesion cells suppress
   ferroptosis induction at the signalling level, making exogenous induction
   (e.g., erastin/sulfasalazine) a therapeutic strategy.

**Limitations:** n=5 pairs; ovarian endometrioma only (not peritoneal or DIE
lesions); bulk RNA (not single-cell or spatial); FPKM is a legacy metric
(no TMM/DESeq2 normalization applied); directional confidence only.

## Candidate GEO datasets (real accessions, NCBI GEO query 2026-09-02)

Lesion-vs-eutopic / lesion-resolution human endometriosis datasets, ranked by
fit to the Phase 0.5 question. **Top three reanalyzed 2026-09-03; the rest
are optional context (no active claim):**

| Accession | Samples | Design | Answers | Status |
|---|---|---|---|---|
| GSE282532 | 10 | RNA-seq, **paired eutopic + ectopic** endometrium, ovarian endometriosis | FKBP4/SLC7A11 lesion vs eutopic (direct) | **DONE 2026-09-03** |
| GSE247695 | 8 | **scRNA-seq**, lesions vs paired eutopic (metabolic activity) | Cell-type resolution — mast cells (MRGPRX2), stromal FKBP4/SLC7A11 | **DONE 2026-09-03** (PR #19) |
| GSE263897 | 10 tissues / 60 segments | **GeoMx DSP spatial**, superficial peritoneal lesions, 3 segmented compartments | Mast-cell niches in situ (MRGPRX2), compartment-resolved FKBP4/SLC7A11 | **DONE 2026-09-03** (PR #20) |
| GSE303635 | 20 | RNA-seq, stromal cells, lesion-type heterogeneity | Stromal FKBP4/SLC7A11 by lesion type | Optional |
| GSE202571 | 18 | RNA-seq, secretory eutopic endometrium with/without EM | Eutopic FKBP4 baseline (progesterone-resistance context) | Optional |
| GSE315857 | 8 | RNA-seq, proliferative eutopic endometrium in EM (PR downstream) | Eutopic FKBP4/PR axis | Optional |
| GSE240392 | 24 | Mouse EM model, eutopic + ectopic over progression | Longitudinal direction (mouse) | Optional |
| GSE303150 | 142 | Spatial, adenomyosis lesions (adjacent disease) | Immune signature incl. mast cells (context) | Optional |
| GSE226575 | 9 | RNA-seq, endometrial cyst to EAOC progression | Lesion progression axis (context) | Optional |
| GSE291656 | 18 | RT-PCR, peritoneal fluid NLRP3 (context) | Peritoneal immune environment | Optional |

Query used: NCBI eutils `db=gds`, `endometriosis[All Fields] AND eutopic[All
Fields] AND gse[Entry Type]` (96 hits; top 40 screened). **Nothing above is an
invented identifier — every accession was returned live by the NCBI API.**

## Phase 0.5 status: COMPLETE (2026-09-03)

All three prioritized datasets have been reanalyzed ($0, public GEO data):
GSE282532 (bulk, endometrioma) · GSE247695 (scRNA-seq, peritoneal) ·
GSE263897 (GeoMx spatial, peritoneal). Write-ups below. Remaining candidate
datasets in the table are optional context with no active claim. Next
virtual-testing phase: **Phase 1 docking (Jaeger)** — structurally unblocked
by the 0-to-fold decision (`af2-decision.md`), no folding prerequisite.

*Percival (Hermes Agent), 2026-09-02 / updated 2026-09-03. Public data only;
no PII. Research infrastructure, not medical advice.*


## GSE247695 reanalysis (scRNA-seq, 2026-09-03, Percival)

**Dataset:** GSE247695 — paired eutopic endometrium vs peritoneal
endometriotic lesions, scRNA-seq (10x), 4 patients (002/398/421/432),
16,924 cells raw → 15,862 post-QC. Analysis: `scripts/gse247695_analysis.py`
(reproducible; scanpy 1.12; 10x MTX load → QC → normalize/log1p → PCA →
Leiden → marker-scored cell typing → per-cell-type expression on the
UNSCALED log1p matrix). Output: `virtual/gse247695_targets.json`.

**Cell composition (lesion vs eutopic):** peritoneal lesions are
perivascular-rich (2,668 vs 470 cells) and stromal-poor (716 vs 5,043);
epithelial cells almost absent from lesions (21 vs 363 — sampling of
peritoneal lesions). Immune cells expanded (T 1,779 vs 760; B 319 vs 75;
macrophage 486 vs 159).

### Per-target, compartment-resolved results

| Gene | Compartment | Eutopic (mean, frac) | Lesion (mean, frac) | Reading |
|---|---|---|---|---|
| FKBP4 | Stromal | 0.244, 39.5% | 0.144, 22.9% | **DOWN in lesion stroma** (the dominant compartment) — consistent with GSE282532 2.2x bulk down |
| FKBP4 | Perivascular | 0.208, 36.0% | 0.297, 41.2% | up in lesion perivascular cells |
| FKBP4 | Epithelial | 0.173, 39.7% | 0.257, 42.9% | up (n=21 lesion cells — low power) |
| SLC7A11 | Endothelial | 0.174, 24.5% | 0.017, 4.6% | **strongly DOWN in lesion endothelium** |
| SLC7A11 | Stromal | 0.034, 5.9% | 0.006, 1.1% | down in lesion stroma |
| SLC7A11 | Epithelial | 0.037, 9.4% | 0.056, 14.3% | weakly up (low n) |
| MRGPRX2 | all cell types | 0.0 | 0.0 | **below detection everywhere, incl. the KIT+ putative-mast-cell compartment (110 cells)** |

### Mast-cell compartment — honest caveats
- The KIT+ cluster (frac KIT 0.81→0.92) shows **zero CPA3/TPSAB1/TPSB2/
  MS4A2/MRGPRX2** despite all genes being present in the feature tables —
  consistent with 10x dropout on small cell numbers (110 cells total),
  not proof of absence.
- **KIT+ cells are NOT enriched in these peritoneal lesions** (0.56% vs
  0.73% of cells) — a discrepancy vs GSE282532's 11–15x mast-cell marker
  enrichment in ovarian endometrioma. Lesion-type difference (peritoneal
  vs endometrioma) or method difference; flagged for reconciliation. The
  GSE263897 GeoMx reanalysis (below) resolved this: **dropout-free GeoMx
  also finds no mast-cell enrichment in peritoneal lesions** — the
  discrepancy is lesion type, not method.

### Conclusions for the M3 targets
1. **FKBP4/sirolimus:** target expressed broadly; **down in lesion
   stroma** (consistent with PR-resistance); perivascular/epithelial up
   are minor compartments. Expression is NOT the barrier to an mTOR-axis
   intervention — ubiquitous pathway, druggable regardless of the FKBP4
   dip.
2. **MRGPRX2 pain axis:** scRNA here is **inconclusive, not negative** —
   dropout regime + rare cells. The positive IHC evidence (FASEB J 2025,
   PMID 40600649) and GSE282532 mast-cell enrichment stand **for ovarian
   endometrioma**; the spatial dataset (GSE263897) was the definitive
   single-dataset check for peritoneal lesions (done — see below).
3. **SLC7A11/sulfasalazine:** down in lesion stroma/endothelium —
   consistent with SEMA3C suppression and the ferroptosis-direction
   verdict (no constitutive overexpression to target).

**Phase 0.5 remaining leg:** GSE263897 (GeoMx spatial) — ✅ **DONE
2026-09-03 (PR #20)**; full write-up in the next section.


## GSE263897 reanalysis (GeoMx DSP spatial, 2026-09-03, Percival)

**Dataset:** GSE263897 — NanoString GeoMx Digital Spatial Profiling, Human
Whole Transcriptome Atlas v1.0 (GPL24676; PKC `Hs_R_NGS_WTA_v1.0`).
Superficial **peritoneal** endometriotic lesions vs patient-matched eutopic
endometrium from 5 women (secretory phase); 10 tissues × duplicate ROIs × 3
fluorescence-segmented compartments per ROI (**Epithelium** pan-cytokeratin+,
**Macrophages** CD68+, **Stroma** pan-negative) = **60 segments**. Public Apr
2024 (updated Feb 2025); BioProject PRJNA1099697; no linked PMID at time of
analysis. GEO note: the depositors' own analysis reported **minimal
lesion-vs-eutopic transcriptional differences** in sub-epithelial stroma and
epithelium, with the lesion **epithelium** driving inflammation via
Complement C3 signalling to macrophages.

**Why this dataset matters:** GeoMx probes hybridise in situ — **no 10x
dropout** — so a low-expression receptor (MRGPRX2) on a rare cell type (mast
cells) is detectable *if present*. GSE247695 left the peritoneal-lesion
mast-cell question open under a dropout regime; GSE263897 is the
dropout-free check. (Limitation: GeoMx segments are region-averaged per
compartment; mast cells, if present, fall inside the pan-negative Stroma
segment — there is no mast-cell-specific segment.)

**Method** (reproducible): `scripts/gse263897_analysis.py` — parse each DCC
(per-segment RTS counts) + PKC codebook (RTS→gene; 18,677 targets incl.
FKBP4/MRGPRX2/SLC7A11/KIT/CPA3/TPSAB1/MS4A2 — TPSB2 not separately on the
WTA panel); 139 negative-control probes for background; Q3 normalization
(75th percentile of segment probe counts, GeoMx standard) → log2; per-patient
mean over duplicate ROIs; paired lesion vs eutopic per compartment (n=5 →
directional evidence only, consistent with the GSE282532/GSE247695
conventions). Output: `virtual/gse263897_targets.json` (per-patient deltas
included).

**QC:** negative-probe geomean 2.1–28.4 counts across segments (low
background; no segment above 10% of its Q3). 8 sparse segments flagged
(compartment marker ≤ 2× neg-geomean): 5 Macrophage AOIs (CD68-low, e.g.
GSM8206913: 11.6k total reads) + 3 Epithelium AOIs (EPCAM-low, incl. the
near-empty GSM8206952, EPCAM=6 vs background 3.6 — it drives patient 4909's
C3 delta down). Segmentation sanity verified: EPCAM/KRT18 enrich Epithelium,
CD68/LYZ/CD163 enrich Macrophages, DCN/COL1A1 enrich Stroma. **Robustness:**
key conclusions unchanged under (a) exclusion of the 8 sparse segments and
(b) CPM scaling instead of Q3.

**Validation (pipeline credibility):** the depositors' headline —
Complement **C3 elevated in lesion epithelium** — replicates: lesion vs
eutopic epithelium **FC 3.29 (Δlog2 +1.72), 4/5 patients** (2756/5322/12529/
9997 up; 4909 opposite — its lesion ROI_007 segment is the sparse
GSM8206952; even excluding it, 4909 shows no lesion C3 increase).
Macrophage/stroma C3 flat. A pipeline that reproduces the study's central
claim on the same public data is a credible instrument for our target
questions.

### Per-target, compartment-resolved results (lesion vs eutopic, patient-paired)

| Gene | Compartment | Eutopic mean | Lesion mean | FC | Consistency | Raw/background |
|---|---|---|---|---|---|---|
| FKBP4 | Epithelium | 0.92 log2-Q3 | 1.30 | **1.31** | **5/5 up** | 3.3x / 5.1x (real signal) |
| FKBP4 | Stroma | 1.08 | 0.91 | 0.89 | 4/5 down | 3.3x / 3.1x (real signal) |
| FKBP4 | Macrophages | 0.85 | 0.76 | 0.94 | 3/5 | near background |
| SLC7A11 | Stroma | 0.61 | 0.53 | 0.94 | 4/5 down | 1.2x / 1.3x (weak) |
| SLC7A11 | Epithelium | 0.75 | 0.59 | 0.89 | 3/5 | 1.6x (weak) |
| MRGPRX2 | Stroma | 0.56 | 0.51 | 0.96 | 2/5 | **1.2x / 1.3x — NOT above background** |
| MRGPRX2 | Epithelium | 0.41 | 0.56 | 1.11 | 4/5 | ~1x (background) |
| KIT | Stroma | 0.70 | 0.62 | 0.95 | 4/5 down | 1.6x (weak) |
| CPA3 | Stroma | 0.63 | 0.38 | 0.84 | **5/5 down** | 1.3x / 0.9x (weak) |
| TPSAB1 | Stroma | 0.73 | 0.78 | 1.04 | 3/5 | 1.7x / 1.9x (weak) |
| MS4A2 | Stroma | 0.52 | 0.34 | 0.89 | 4/5 down | 1.1x / 0.8x (background) |
| FCER1A | Stroma | 0.39 | 0.38 | 0.99 | 3/5 | 0.8x (background) |
| GPX4 | Stroma | 2.56 | 2.50 | 0.96 | 4/5 | 11x (solid) |
| ACSL4 | Stroma | 0.92 | 1.07 | 1.11 | **5/5 up** | 2.1x / 3.1x |
| C3 | Epithelium | 2.56 | 4.28 | **3.29** | **4/5 up** | strong (study replication) |

Values are mean log2(Q3-normalized counts) over duplicate ROIs per tissue,
then across patients (full per-patient deltas in the JSON). Directional only
(n=5). "Raw/background" = mean raw count ÷ mean negative-probe geomean in
eutopic/lesion segments of that compartment.

### Mast-cell reconciliation — the Phase 0.5 payoff

Three independent GEO datasets now paint a consistent, lesion-type-specific
picture:

| Dataset | Platform | Lesion type | Mast-cell readout in lesions |
|---|---|---|---|
| GSE282532 | bulk RNA-seq | **ovarian endometrioma** (proliferative) | CPA3/TPSAB1/TPSB2 **11–15x UP** (all 5 pairs) |
| GSE247695 | 10x scRNA-seq | superficial **peritoneal** | KIT+ cluster **not enriched** (0.56% vs 0.73%) |
| GSE263897 | GeoMx DSP (no dropout) | superficial **peritoneal** (secretory) | KIT/CPA3/TPSAB1/MS4A2/FCER1A **flat-to-down, at/near negative-probe background in both tissues; MRGPRX2 itself not above background** |

**Reading:** mast-cell enrichment (and any MRGPRX2-lesion signal) is an
**ovarian-endometrioma feature** in these data, not a feature of superficial
peritoneal lesions — the GSE247695 "discrepancy" is resolved: two peritoneal
datasets, one dropout-prone and one dropout-free, agree. The FASEB J 2025
mast-cell/IHC result (PMID 40600649) and GSE282532 support the MRGPRX2 pain
axis in the lesion types they studied; extrapolating it to all endometriosis
lesion types is not supported by the public transcriptomic record here.
Honest limits: near-background GeoMx reads cannot fully separate "few mast
cells" from "weak WTA probe sensitivity" for these genes; and the same
reasoning means we cannot claim mast cells are *absent* — only that no
lesion enrichment is detectable. **IHC on lesion-type-stratified tissue
remains the definitive check** (unchanged recommendation).

### M3-target conclusions
1. **FKBP4/sirolimus:** the compartment split from GSE247695 replicates in a
   second, independent peritoneal dataset: **down in lesion stroma (0.89,
   4/5), up in lesion epithelium (1.31, 5/5)**. Endometrioma bulk
   down-regulation (GSE282532, 0.45) reflects stromal dominance. Consistent
   with PR-resistance in the stroma; FKBP4 expression is not a barrier to an
   mTOR-axis intervention anywhere.
2. **MRGPRX2/mast-cell pain axis:** no support in superficial peritoneal
   lesions on a dropout-free platform (markers at background, no enrichment).
   Target rationale stands for endometrioma-type lesions; lesion-type
   stratification is now an explicit caveat for the pain-axis hypothesis.
3. **SLC7A11/sulfasalazine:** no constitutive up-regulation in any dataset or
   compartment (slight down in lesion stroma/endometrium where measurable;
   near background in GeoMx). Ferroptosis-induction direction unchanged;
   sulfasalazine stays WATCHLIST on selectivity/dose, not on expression.
4. **ACSL4** (pro-ferroptotic): up in lesion stroma 5/5 (1.11x) here — small,
   opposite to endometrioma bulk (0.41); not mechanistically decisive at this
   magnitude, flagged for the ferroptosis-direction file's awareness only.

**Limitations:** n=5; secretory phase; superficial peritoneal lesions only
(not endometrioma/DIE); GeoMx WTA probe sensitivity is limited near
background (rare-cell transcripts); ROIs were selected on lesion areas with
epithelium (lesion sampling bias); Q3 normalization + directional evidence
only (no formal test at n=5). No PII — patient identifiers are the public
GEO sampleIDs (2756/5322/12529/4909/9997).

*Percival (Hermes Agent), 2026-09-03. Public GEO data; no PII. Research
infrastructure, not medical advice.*
