# Protocol spec 01 — Sirolimus / mTOR (+ optional FKBP4/PR readout)

> **Status:** partner-ready *paper* protocol specification (not a DIY recipe; not medical advice).  
> **Audience:** organoid or animal partner lab (academic / CRO).  
> **OpenEndo corpus grounding:** `/workspace/openendo` (CHECKPOINT 2026-09-14; M3 TOP TIER).  
> **Draft location only:** `/workspace/openendo-drafts/wetlab/` — do **not** push to GitHub from this pass.  
> **Uncertainty flags** appear inline as `[UNCERTAIN]`.

---

## 1. Scientific question

1. **Primary (mTOR):** Does **mTORC1 inhibition** with sirolimus/rapamycin reduce endometriotic lesion burden and/or proliferative / senescence-oxidative phenotypes in a controlled **organoid or animal** endometriosis model, relative to vehicle and a hormonal-therapy comparator?
2. **Secondary / optional (FKBP4–PR readout — separate axis):** Independently of mTOR pharmacology, does the lesion model recapitulate **FKBP4 (FKBP52) down-regulation** and impaired **progesterone-receptor (PR)** transcriptional activity, and does mTOR inhibition *change* (or leave unchanged) that chaperone–PR state?

**Do not conflate axes.** OpenEndo ranks sirolimus on **mTOR** evidence. The ChEMBL FKBP4 hit is binding promiscuity across FKBPs, *not* a claim that sirolimus restores FKBP4 or reverses PR resistance (`docs/knowledge/entities/sirolimus.md`).

---

## 2. Rationale (in-repo paths + PMIDs)

| Claim | In-repo path | Key PMIDs / accessions |
|---|---|---|
| mTOR activated in endometriosis; inhibitors active in models | `docs/knowledge/entities/sirolimus.md`, `docs/research/evidence/m3-validation.md` | **39579091** (Mol Hum Reprod 2024 review); **27347023** (mouse lesion reduction) |
| Fertility / ovarian senescence angle | same | **41170754** (PPARα/IGFBP2, mouse); **37914557** (retrospective IVF follicular-fluid cohort — hypothesis-generating only; no CT.gov registration) |
| FKBP52 deficiency → PR resistance / lesion growth | `sirolimus.md`, Phase 0.5 | **17571166**, **18988805**, **22279148**, **27778641** |
| FKBP4 ↓ in ectopic lesions (computational corroboration) | `docs/research/virtual/phase0.5.md`, GSE282532 | FKBP4 **2.2× down** ectopic vs eutopic (FC 0.45, 5/5 pairs); stroma-down replicated GSE247695 / GSE263897 (epi up in GeoMx — compartment split) |
| Structural engagement FKBP4 ≈ FKBP12 (binding, not therapy claim) | `docs/research/virtual/phase1/` | rapamycin→FKBP52 **−6.38** vs FKBP12 **−7.06** kcal/mol (Vina); pose claims deferred to Phase 2 MD |
| Registry novelty | `docs/research/evidence/registry-verification-2026-09-03.md` (+ drafts `openendo-drafts/registry-verification-2026-09-14.md`) | **0** registered interventional endo trials for sirolimus/rapamycin/mTOR inhibitors (as of 2026-09) |

**Verdict context:** M3 **TOP TIER**, confidence medium–high on biology / novelty; **clinical evidence absent**.

---

## 3. Required samples / models

Partner chooses **one primary** track (A or B); optional readout C can attach to either.

### Track A — Patient-derived or immortalized organoids / explants
- Paired **eutopic endometrium** and **ectopic lesion** (prefer endometrioma and/or peritoneal; record lesion type).
- Culture as epithelial–stromal organoids or 3D explants under documented hormone conditions (E2 ± P4).
- Minimum design target: n ≥ 6 biological donors per lesion class `[UNCERTAIN: power — partner biostat to finalize]`.

### Track B — Animal endometriosis model
- Established autologous / syngeneic / xenograft lesion model already used by the partner (e.g. mouse peritoneal implant).
- Prefer models with published lesion-burden + fertility endpoints if fertility is in scope (aligns with PMID 41170754).
- Cycle stage / hormone status recorded.

### Optional panel C — FKBP4 / PR molecular readout (same tissues)
- Protein: FKBP4/FKBP52, PR-B/PR-A, phospho-S6 / phospho-4E-BP1 (mTORC1 activity).
- Transcript: *FKBP4*, *PGR*, HOXA10 / miR-29c axis genes (context only).
- Functional PR reporter or PRE-driven luciferase in organoids `[UNCERTAIN: assay availability at partner]`.

**Excluded from this spec:** human dosing, off-label patient protocols, compounding instructions.

---

## 4. Assay endpoints

### Primary efficacy (mTOR track)
| Endpoint | Method examples | Notes |
|---|---|---|
| Lesion burden | Organoid viability / growth AUC; animal lesion number, volume, weight, histology score | Pre-specify primary metric before unblinding |
| mTORC1 on-target | p-S6 / p-4E-BP1 IHC or Western; optional p-Akt (mTORC2 cross-talk) | Confirm pathway engagement at chosen exposure |
| Proliferation / apoptosis | Ki-67, cleaved caspase-3 | Standard panel |
| Senescence / oxidative (optional) | p16, p21, γH2AX, ROS / MDA | Aligns with PMID 41170754 / 37914557 themes |

### Optional FKBP4–PR panel
| Endpoint | Method | Pass criterion for “model valid for PR-resistance biology” |
|---|---|---|
| FKBP4 protein/mRNA vs matched eutopic | IHC / qPCR / Western | Directional ↓ in lesion compartment consistent with GEO (stroma) |
| PR transcriptional activity | Reporter or known PR target genes under P4 | Impaired vs eutopic control under same P4 |
| Effect of sirolimus on FKBP4/PR | Same assays ± drug | **Report even if null** — null supports axis separation |

### PK / exposure (animal)
- Trough / tissue levels if partner has bioanalytical capacity `[UNCERTAIN]`.
- Otherwise justify dose from published endometriosis or transplant-adjacent rodent literature and measure on-target p-S6.

---

## 5. Controls

| Control | Purpose |
|---|---|
| Vehicle (matched solvent) | Baseline |
| No-treatment / time-zero tissue | Culture artifact check |
| Positive pathway control | Known mTORC1 inhibitor class comparator (e.g. everolimus) *or* published active dose of rapamycin in same model |
| Hormonal comparator (optional) | Progestin or GnRH-antagonist-class condition already used by lab — contextual, not superiority claim |
| Matched eutopic tissue / organoid | Compartment specificity |
| Isotype / secondary-only (IHC); loading controls (Western) | Technical |
| FKBP4 IHC on known high-expressing tissue (e.g. endometrium control block) | Antibody validation |
| Blinded lesion scoring | Reduce bias |

**Dose range:** exploratory multi-dose (low / mid / high) around published model-active exposures — partner documents rationale. Do **not** copy transplant trough targets into a patient-facing narrative.

---

## 6. Go / no-go criteria

| Decision | Criteria (pre-specify; adjust with partner stats) |
|---|---|
| **GO — mTOR biology supported in partner model** | (i) Significant ↓ lesion burden or growth vs vehicle at a tolerated exposure; **and** (ii) on-target ↓ p-S6 (or agreed mTORC1 marker); **and** (iii) no catastrophic toxicity stopping rule hit |
| **GO — expand FKBP4/PR deep-dive** | Model shows FKBP4 ↓ and/or impaired PR activity in lesion vs eutopic **before** treating as a co-primary program |
| **HOLD** | Efficacy signal without on-target marker, or on-target without efficacy → replicate once with tighter exposure control |
| **NO-GO for this model** | No efficacy across doses **and** failed pathway engagement; or toxicity precludes interpretable window |
| **NO-GO for “sirolimus restores FKBP4” story** | Any marketing/scientific claim that mTOR inhibition *fixes* FKBP4/PR — permanently out of scope unless a *different* modality is tested |

Registry / clinical translation remains out of scope until dedicated toxicology + ethics packages exist (OpenEndo notes **0** endo trials).

---

## 7. Ethics / safety notes

| Risk | Note for partner protocol / IACUC–ethics dossier |
|---|---|
| **Immunosuppression** | Sirolimus is a potent immunosuppressant (transplant / LAM label context). Animal studies: infection surveillance, sterile technique, endpoint criteria for opportunistic illness. |
| **Teratogenicity / reproductive toxicity** | Assume reproductive hazard; exclude mating endpoints unless study is explicitly fertility-focused with appropriate containment; no pregnancy exposure. |
| **Systemic toxicity** | Monitor weight, CBC if available, wound healing (mTOR), mucositis-like signs in rodents; define humane endpoints. |
| **Human subjects** | Tissue use only under approved biobank / IRB protocols; no patient self-administration guidance in any deliverable. |
| **Drug–drug / formulation** | Partner pharmacy SOPs for solubilization; document batch, purity, endotoxin if injectable. |
| **Communication** | All public text: *research priority / hypothesis-generating — not treatment advice*. |

---

## 8. Estimated complexity

| Dimension | Rating | Comment |
|---|---|---|
| Wet-lab skill | **Medium–high** | Organoid endometriosis culture or surgical animal model |
| Analytics | Medium | IHC/Western panel + quantitative pathology |
| Regulatory / ethics | Medium–high | Controlled substance handling varies by country; animal ethics |
| Cost band | Mid (organoid) / Mid–high (animal + PK) | `[UNCERTAIN: local pricing]` |
| Timeline | ~8–16 weeks organoid screen; ~4–6 months animal with histology | Depends on colony and IRBs |

---

## 9. Computational already done vs wet lab must answer

| OpenEndo already has (computational / literature) | Wet lab must answer |
|---|---|
| M3 TOP TIER ranking + ChEMBL FKBP4 binding context | Does **mTORC1 inhibition** shrink lesions *in partner’s* model with on-target PD? |
| Literature synthesis (animal + review + IVF cohort caveats) | Dose–response, therapeutic index, lesion-type dependence |
| GEO: FKBP4 ↓ ectopic; stroma/epithelium split | Protein-level FKBP4/PR activity in *same* samples as drug PD |
| Phase 1 docking: FKBP52 engages rapamycin similarly to FKBP12 | Whether FKBP4 engagement has **functional** PR consequences (Phase 2 MD still pending GPU) |
| Registry: 0 endo mTOR trials | Nothing clinical — wet lab does not replace trials |

**Phase 2 MD (P2-A)** may refine FKBP52 pose stability claims but is **not** a prerequisite to start organoid/animal mTOR efficacy work (`docs/research/virtual/phase2/phase2-plan.md`; budget blocker separate).

---

## 10. Suggested deliverables back to OpenEndo

1. Blinded endpoint table (CSV) + analysis notebook.  
2. Representative IHC/Western figures (CC-licensed or partner-owned).  
3. Short memo: GO/HOLD/NO-GO against §6.  
4. Explicit statement on FKBP4/PR axis separation (changed / unchanged / not assayed).

---

*OpenEndo draft protocol spec · 2026-09-14 · research infrastructure only · not medical advice.*
