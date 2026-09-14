# Protocol spec 02 — MRGPRX2 IHC / mast-cell stratification by lesion type

> **Status:** partner-ready *paper* protocol specification (histopathology / IHC).  
> **Audience:** pathology-capable endometriosis research lab or biobank partner.  
> **OpenEndo corpus grounding:** VALIDATED AXIS (antagonism target — **not** cetrorelix-as-drug).  
> **In-repo path:** `docs/research/lab-protocols/02-mrgprx2-ihc-mast-cell-stratification.md`.  
> **Not medical advice.** Uncertainty flagged `[UNCERTAIN]`.

---

## 1. Scientific question

Is **MRGPRX2⁺ mast-cell density** (and canonical mast-cell markers) **enriched in endometriotic lesions in a lesion-type–dependent way** — specifically:

| Lesion class | Computational prior (OpenEndo Phase 0.5) |
|---|---|
| Ovarian **endometrioma** | Mast markers CPA3 / TPSAB1 / TPSB2 **11–15× ↑** vs eutopic (GSE282532); consistent with FASEB J 2025 pain axis |
| Superficial **peritoneal** lesions | Mast markers + MRGPRX2 at / near background in scRNA (GSE247695) and GeoMx (GSE263897) — **no enrichment** |
| Deep infiltrating endometriosis (**DIE**) / other | **Not resolved** in OpenEndo GEO set `[UNCERTAIN]` |

**IHC stratified by lesion type is the definitive protein-level check** called out in CHECKPOINT / `phase0.5.md` / `m3-validation.md`.

Secondary question: Do MRGPRX2⁺ mast cells spatially associate with nerves (PGP9.5 / β3-tubulin) more in pain-enriched specimen subsets `[UNCERTAIN: clinical pain metadata availability]`?

---

## 2. Rationale (in-repo paths + PMIDs)

| Claim | Path | PMIDs / accessions |
|---|---|---|
| End-to-end pain axis: HBD-2 → MRGPRX2 → histamine → HRH1/TRPV1 | `docs/knowledge/concepts/mrgprx2-pain.md` | **40600649** (FASEB J 2025) |
| Mast cells near nerves in lesions | same | **17007852** (Anaf 2006); reviews **41079937**, **40028674**; PF mast cells **31998139** |
| Cetrorelix→MRGPRX2 is *agonism* (validates target, wrong direction for drug) | `m3-validation.md` | **28288109**; cetrorelix endo regimens **12537785**, **12470539**; NCT00244452 |
| Bulk RNA cannot see MRGPRX2 | Phase 0.5 | HPA nTPM 0.0; GSE282532 MRGPRX2 below detection |
| Endometrioma vs peritoneal discrepancy | `docs/research/virtual/phase0.5.md` (PR #19, #20) | GSE282532 vs GSE247695 / GSE263897 |
| Registry | `registry-verification-*.md` | **0** MRGPRX2-named endo trials; cetrorelix ≠ antagonist lead |

**Program implication:** If IHC confirms endometrioma-selective enrichment, antagonist priority should be **stratified** (endometrioma / pain-biopsy enriched cohorts) rather than assumed for all peritoneal disease.

---

## 3. Required samples / models

### Tissue cohorts (human archival preferred)
Minimum design (partner may expand):

| Arm | Tissue | Target n (blocks) | Notes |
|---|---|---|---|
| A | Ovarian endometrioma cyst wall | ≥ 15 | Match phase / hormone therapy status where possible |
| B | Superficial peritoneal lesion | ≥ 15 | Explicitly label “peritoneal” |
| C | DIE (e.g. uterosacral / rectovaginal) | ≥ 10 | Optional but high value `[UNCERTAIN]` |
| D | Matched eutopic endometrium (same patient subset) | ≥ 10 pairs | Gold-standard control |
| E | Non-endo control endometrium / peritoneum | ≥ 8 | Surgical controls per ethics |

**Metadata to capture:** age, cycle phase, hormonal therapy (yes/no/type), rASRM or #Enzian stage, pain scores if available, fixation time, block age.

**Excluded:** live mast-cell challenge in patients; cetrorelix dosing studies framed as MRGPRX2 therapy.

---

## 4. Assay endpoints

### Core IHC / IF panel
| Marker | Role | Expected pattern |
|---|---|---|
| **MRGPRX2** | Primary | Membrane on mast cells; validate Ab (see controls) |
| **Tryptase** (TPSAB1) and/or **CPA3** | Mast-cell density | Cytoplasmic; count per mm² |
| **KIT** (CD117) | Mast / progenitor context | Cross-check; not MRGPRX2-specific |
| **PGP9.5** or β3-tubulin | Nerve proximity | Optional spatial analysis |
| **Tryptase + MRGPRX2** dual IF | Co-localization | % tryptase⁺ that are MRGPRX2⁺ |

### Quantitation
- Mast-cell density: cells/mm² in lesion stroma hotspots + random fields (pre-specify sampling).
- MRGPRX2⁺ fraction of tryptase⁺ cells.
- Nerve–mast distance histogram (if nerves stained).
- Blinded dual-reader or digital pathology with locked algorithm.

### Optional orthogonal
- RNAscope / BaseScope for *MRGPRX2* if Ab validation fails `[UNCERTAIN]`.
- qPCR panel on macrodissected lesion RNA: *CPA3*, *TPSAB1*, *TPSB2*, *MRGPRX2*, *KIT* — bridges to GSE282532.

---

## 5. Controls

| Control | Purpose |
|---|---|
| Positive tissue (skin / known MRGPRX2-rich mast-cell bed) | Ab / assay works |
| MRGPRX2 peptide block or KO/knockdown cell pellet if available | Specificity |
| Isotype + omit-primary | Background |
| Same-section serial: tryptase vs MRGPRX2 | Same cells |
| Eutopic internal control | Disease vs eutopic |
| Batch controls across staining runs | Technical drift |
| Blinded lesion-type labels until database lock | Bias control |

**Antibody caveat:** Commercial MRGPRX2 Abs vary; partner must document clone, dilution, retrieval, and validation images. `[UNCERTAIN: best clone — partner to pilot on 3–5 blocks]`

---

## 6. Go / no-go criteria

| Decision | Criteria |
|---|---|
| **GO — endometrioma mast/MRGPRX2 axis confirmed at protein level** | Endometrioma tryptase⁺ density and/or MRGPRX2⁺ mast density significantly ↑ vs matched eutopic **and** vs peritoneal arm (or peritoneal not enriched), aligning with Phase 0.5 |
| **GO — broaden to all lesion types** | Peritoneal **and** DIE also show significant MRGPRX2⁺ mast enrichment vs controls (would revise OpenEndo “peritoneal-negative” computational prior) |
| **HOLD** | Trend-only, Ab failure, or confounding by hormone therapy / phase — expand n or switch to RNAscope |
| **NO-GO for peritoneal-focused antagonist biomarker** | Confirmed null in peritoneal + DIE with validated assay → keep antagonist rationale **endometrioma / selected pain phenotypes**; do not drop target globally |
| **NO-GO for cetrorelix-as-MRGPRX2-drug narrative** | Permanent — agonism pharmacology unchanged |

---

## 7. Ethics / safety notes

| Topic | Note |
|---|---|
| **Human tissue** | IRB / biobank consent covering secondary research IHC; GDPR / Danish research ethics if DK partner (see T7 shortlist) |
| **No patient intervention** | Observational pathology only |
| **Identifiers** | De-identify; no re-identification in OpenEndo public drafts |
| **Sharps / formalin** | Standard histopathology safety |
| **Interpretation** | Pain mechanism hypothesis — not a diagnostic test claim without analytical validation |

---

## 8. Estimated complexity

| Dimension | Rating |
|---|---|
| Wet-lab skill | **Medium** (IHC core facility friendly) |
| Cohort assembly | Medium–high (lesion-type annotated blocks) |
| Analytics | Medium (digital path optional) |
| Cost | Low–mid relative to animal pharmacology |
| Timeline | ~6–12 weeks after blocks secured |

---

## 9. Computational already done vs wet lab must answer

| Already done | Wet lab must answer |
|---|---|
| Literature pain axis (PMID 40600649) | Protein-level MRGPRX2⁺ mast density **by lesion type** |
| GSE282532 mast marker enrichment (endometrioma) | Whether tryptase/CPA3 IHC matches bulk RNA magnitude |
| GSE247695 / GSE263897 peritoneal non-enrichment | Whether IHC agrees (RNA dropout vs true biology) |
| HPA/GTEx bulk “not detected” explained | Spatial co-localization with nerves / epithelium |
| Cetrorelix pharmacology classified | Nothing about cetrorelix dosing — antagonist chemistry remains separate literature task |

**Does not require:** Phase 2 peptide docking of cetrorelix–MRGPRX2 (deferred; tool boundary).

---

## 10. Suggested deliverables

1. Locked scoring SOP + raw counts CSV by lesion type.  
2. Representative dual-IF figures.  
3. Stats memo vs §6 GO rules.  
4. One-paragraph update suitable for future `concepts/mrgprx2-pain.md` (human-reviewed merge).

---

*OpenEndo draft protocol spec · 2026-09-14 · research infrastructure only · not medical advice.*
