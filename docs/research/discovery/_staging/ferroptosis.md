---
title: Ferroptosis in endometriosis
created: 2026-09-02
updated: 2026-09-14
type: concept
tags: [research, drug, treatment]
sources:
  - https://pubmed.ncbi.nlm.nih.gov/42678895/
  - https://pubmed.ncbi.nlm.nih.gov/42660839/
  - https://pubmed.ncbi.nlm.nih.gov/42698143/
  - https://pubmed.ncbi.nlm.nih.gov/41146213/
  - https://pubmed.ncbi.nlm.nih.gov/41001371/
  - https://pubmed.ncbi.nlm.nih.gov/42234252/
  - https://pubmed.ncbi.nlm.nih.gov/41241001/
  - https://pubmed.ncbi.nlm.nih.gov/41722688/
  - https://pubmed.ncbi.nlm.nih.gov/41437396/
  - https://pubmed.ncbi.nlm.nih.gov/42728524/
  - https://pubmed.ncbi.nlm.nih.gov/40983106/
  - https://pubmed.ncbi.nlm.nih.gov/41422938/
  - https://pubmed.ncbi.nlm.nih.gov/41452077/
  - https://pubmed.ncbi.nlm.nih.gov/42081613/
  - https://pubmed.ncbi.nlm.nih.gov/42155249/
  - https://raw.githubusercontent.com/wckdboy/openendo/main/docs/research/evidence/digest-2026-09-11.md
  - https://raw.githubusercontent.com/wckdboy/openendo/main/docs/research/evidence/ferroptosis-direction.md
  - https://raw.githubusercontent.com/wckdboy/openendo/main/docs/data/repurposing_candidates.json
confidence: medium
contested: true
---

# Ferroptosis — an iron-dependent cell-death axis under investigation

<!-- DRAFT for DrDoc review — 2026-09-14. Diff intent vs live concepts/ferroptosis.md:
     + FIN56 (PMID 42698143) from digest-09-11 as further induction confirmation
     + new 2025–2026 mechanism PMIDs (MBOAT1, EGR1/HMOX1, USP33)
     + biomarker bioinformatics PMID 42728524
     + contested: EA papers claiming ferroptosis suppression (42081613, 42155249)
       — flag compartment nuance; do NOT silently overwrite induction-in-lesion verdict
     + CT.gov still 0 for sulfasalazine / erastin / ferroptosis (2026-09-14)
     Sulfasalazine remains WATCHLIST. Do NOT push to main without human review. -->

Ferroptosis is a regulated, **iron-dependent form of cell death** driven by lipid peroxidation. Two of its best-known gatekeepers are **GPX4** (glutathione peroxidase 4) and **SLC7A11** (the cystine/glutamate antiporter xCT). Because endometriosis lesions bleed, accumulate iron and face oxidative stress, ferroptosis has become an active research question in the field.^[https://pubmed.ncbi.nlm.nih.gov/42660839/]

## Why it surfaced for OpenEndo

- **SEMA3C → ferroptosis:** a 2026 paper reports that SEMA3C promotes endometriosis progression by inducing ferroptosis (and enhancing lesion survival).^[https://pubmed.ncbi.nlm.nih.gov/42678895/] A review of autophagy and ferroptosis in endometriosis was published the same period.^[https://pubmed.ncbi.nlm.nih.gov/42660839/]
- **Direct overlap with OpenEndo's target audit:** both **GPX4** and **SLC7A11** are among the 35 novel drug targets (no known drug mechanisms in ChEMBL) in the M1 fold-input pack.
- **M3 screen convergence:** the ChEMBL-based repurposing screen flags **sulfasalazine** (an approved xCT/SLC7A11 inhibitor) against SLC7A11 — the same axis the mechanism literature points at. Hypothesis-generating, not clinical.^[https://raw.githubusercontent.com/wckdboy/openendo/main/docs/data/repurposing_candidates.json]
- **Further induction confirmation (digest-2026-09-11):** FIN56 suppressed ectopic lesion growth in vitro/in vivo by raising mitochondrial ROS and lipid peroxidation via an ACACA/ARID5A/NOX4 axis.^[https://pubmed.ncbi.nlm.nih.gov/42698143/]

## Direction of effect — resolved lean with contested nuance (MEDIUM)

Detailed verdict: `docs/research/evidence/ferroptosis-direction.md`. In short:
ferroptosis is **compartment-dependent** — in lesion epithelial/stromal cells
it is a growth *brake* that lesions actively evade (MGST3, HSD11B1,
FZD7→SLC7A11 up-regulation), and forcing it back on (erastin, andrographolide,
FIN56, xCT blockade) reproducibly shrinks lesions in 2025–2026 models; but ferroptosis
striking lesional CD8⁺ T cells disables anti-lesion immunity and helps the
lesion,^[https://pubmed.ncbi.nlm.nih.gov/41146213/] and ferroptosis in eutopic
endometrium harms decidualization/fertility.^[https://pubmed.ncbi.nlm.nih.gov/41722688/]
The SEMA3C finding is sub-lethal ferroptotic *signaling* exploited by lesion
cells, not evidence that lethal ferroptosis drives lesions. For the M3 screen
this **supports the therapeutic direction of SLC7A11/xCT inhibition in lesion
cells** (sulfasalazine), while flagging that systemic (non-lesion-targeted)
induction carries immune-cell and fertility risks — one reason sulfasalazine
stays **WATCHLIST**.

### Additional 2025–2026 mechanism papers (live PMIDs; preclinical / computational)

- Estradiol–MBOAT1 regulation of ferroptosis in endometrial stromal cells and
  a mouse model.^[https://pubmed.ncbi.nlm.nih.gov/40983106/]
- EGR1 promotes ferroptosis via transcriptional activation of HMOX1
  (multi-GEO + validation).^[https://pubmed.ncbi.nlm.nih.gov/41422938/]
- USP33 / ferritinophagy / Hippo–YAP: USP33 loss confers ferroptosis resistance
  in ectopic stromal cells.^[https://pubmed.ncbi.nlm.nih.gov/41452077/]
- Bioinformatics nominating ferroptosis-related genes as diagnostic/predictive
  features.^[https://pubmed.ncbi.nlm.nih.gov/42728524/]

These enlarge the mechanistic map; none are sulfasalazine clinical trials.

### Contested / host-protective claims (do not overwrite)

Two 2026 electroacupuncture mouse papers report **suppressing** ferroptosis
(via Nrf2 / GPX4) with claimed benefit for ovarian function and for ectopic
*and* eutopic endometrium.^[https://pubmed.ncbi.nlm.nih.gov/42081613/]^[https://pubmed.ncbi.nlm.nih.gov/42155249/]
**Uncertainty flag:** if read as “ferroptosis is always bad in endometriosis,”
they appear to conflict with lesion-cell induction studies (erastin, FIN56,
MGST3/HSD11B1/FZD7–SLC7A11). OpenEndo’s working reconciliation — pending human
review — is the existing compartment model: eutopic/ovarian ferroptosis can be
host-harmful while lesion-cell ferroptosis remains a growth brake. EA is not an
xCT pharmacology study and does **not** clear systemic sulfasalazine.
`contested: true` until a clearer human/compartment synthesis is written.

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
transporter the lesion often keeps *low* — consistent with the therapeutic
direction (forcing ferroptosis back on), while low lesional expression
underlines that selectivity/toxicity, not target presence, is the open question.
Phase 1.0 docking (2026-09-04, PR #22) confirms sulfasalazine binds the xCT
substrate cavity (−8.52 vs native −9.35 kcal/mol).

## Registry / clinical status (re-checked 2026-09-14)

ClinicalTrials.gov API v2: **0** endometriosis interventional trials for
sulfasalazine, erastin, or “ferroptosis” as intervention (dienogest control
still 40). No human trial readout moves the WATCHLIST status.

## Caveats

- Mechanism science is 2025–2026 and largely preclinical; clinical evidence in
  endometriosis is absent (no registered xCT-inhibitor trial).
- Cell type and lesion stage matter: induction vs inhibition is not a
  one-size answer across compartments (lesion stroma/epithelium vs CD8⁺ T cells
  vs eutopic endometrium / ovary).
- In-vitro potency ≠ clinical efficacy; nothing here is treatment guidance.
- Systemic sulfasalazine doses that engage xCT carry historical toxicity
  baggage (see `m3-validation.md`); lesion-local delivery remains the open
  translational question.

## Related

[[computational-drug-repurposing]] · [[gnrh-antagonists]] · [[sirolimus]] · [[mrgprx2-pain]]
