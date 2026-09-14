# Protocol spec 03 — Ferroptosis selectivity panel (lesion epi/stroma vs CD8⁺ / eutopic; sulfasalazine–xCT context)

> **Status:** partner-ready *paper* protocol specification (cell / organoid co-culture pharmacology).  
> **Audience:** wet-lab partner with endometriosis cell models + immune co-culture capacity.  
> **OpenEndo corpus grounding:** M3 **WATCHLIST** (sulfasalazine → SLC7A11/xCT); direction = **induce ferroptosis in lesion cells**; blocker = **selectivity**.  
> **In-repo path:** `docs/research/lab-protocols/03-ferroptosis-selectivity-coculture.md`.  
> **Not medical advice / not a patient recipe.** `[UNCERTAIN]` flags included.

---

## 1. Scientific question

Can **xCT (SLC7A11) inhibition** (sulfasalazine as tool compound; optional erastin-class comparator) **selectively** trigger ferroptosis in **lesion epithelial / stromal** compartments **without** equivalently killing:

1. **Lesional / autologous CD8⁺ T cells** (ferroptosis here is *pro-lesion* per PMID 41146213), and  
2. **Eutopic endometrial stromal/epithelial cells** (ferroptosis impairs decidualization / receptivity — PMIDs 41722688, 41437396)?

**Direction prior (resolved, MEDIUM confidence):** lesion-cell ferroptosis = growth brake lesions evade → induction is therapeutic *in lesion cells*; systemic non-selective induction is the WATCHLIST problem (`docs/research/evidence/ferroptosis-direction.md`).

---

## 2. Rationale (in-repo paths + PMIDs)

| Claim | Path | PMIDs / notes |
|---|---|---|
| Direction verdict + compartment table | `docs/research/evidence/ferroptosis-direction.md` | MEDIUM confidence; 13 PMIDs |
| Lesion induction shrinks models | same + `concepts/ferroptosis.md` | e.g. **41001371** (erastin), **42234252** (MGST3), **42151966** (HSD11B1), **41241001** (FZD7–SLC7A11), **41408483**, **42186752** |
| CD8⁺ ferroptosis → immune dysfunction | ferroptosis-direction | **41146213** |
| Eutopic ferroptosis → fertility harm | same | **41722688**, **41437396** |
| SEMA3C = sub-lethal signaling nuance | same | **42678895** (not anti-induction) |
| GEO: SLC7A11 / ACSL4 ↓ in lesions | `phase0.5.md` | GSE282532 SLC7A11 **2× down**, ACSL4 **2.4× down**; GSE247695/263897 no constitutive SLC7A11↑ |
| Binding not the blocker | `docs/research/virtual/phase1/` | sulfasalazine→xCT **−8.52** vs native J9O **−9.35** kcal/mol |
| Registry | registry-verification | **0** xCT-inhibitor endo trials |
| Contested EA / Nrf2–GPX4 “suppress ferroptosis” papers | `docs/knowledge/concepts/ferroptosis.md`, `ferroptosis-direction.md` 2026-09-14 addendum | PMIDs **42081613**, **42155249** flagged **contested** — do not invert induction lean without review `[UNCERTAIN]` |
| Newer induction context | digest / literature packet | FIN56 / ACACA axis **42698143** (context) |

---

## 3. Required samples / models

### Preferred panel architecture (3 compartments, parallel plates)

| Compartment | Model | Source |
|---|---|---|
| **L-epi / L-stroma** | Primary ectopic endometrial stromal cells (EESC) ± epithelial; or lesion-derived organoids | Surgical endometrioma and/or peritoneal — **record type** |
| **Eu-stroma / Eu-epi** | Patient-matched eutopic ESC / organoids | Same donor when possible |
| **CD8⁺** | Autologous TIL-like CD8 from lesion digest **or** allogeneic healthy donor CD8 with iron-overload stress condition approximating PMID 41146213 | Partner capability `[UNCERTAIN]` |

### Co-culture modes (run what partner can support)
1. **Parallel monocultures** (minimum viable product): same drug exposures, compare EC50 / ferroptosis markers across compartments.  
2. **Transwell** lesion stroma ↔ CD8.  
3. **Direct 2D/3D co-culture** with fluorescent lineage tags for compartment-specific death.

### Tool compounds
| Agent | Role |
|---|---|
| **Sulfasalazine** | xCT inhibitor (M3 candidate; clinical formulation not a dosing guide) |
| **Erastin** or imidazole ketone erastin | Positive ferroptosis inducer / xc⁻ benchmark |
| **Ferrostatin-1** and/or **Liproxstatin-1** | Rescue → ferroptosis-specificity control |
| **Deferoxamine** (optional) | Iron chelation rescue |
| Vehicle | Matched solvent |

**Out of scope:** patient oral sulfasalazine regimens; glioma-trial dose copying as endo advice.

---

## 4. Assay endpoints

### Death / ferroptosis specificity
| Endpoint | Method |
|---|---|
| Viability | CellTiter-Glo / MTT / Incucyte |
| Lipid peroxidation | C11-BODIPY, MDA, or equivalent |
| Iron dependence | Rescue by Fer-1 + optional DFO |
| Classical apoptosis distinction | Caspase-3/7 or Annexin — ferroptosis should be Fer-1 sensitive, caspase-poor |
| xCT pathway | GSH levels; SLC7A11 / GPX4 / ACSL4 protein or mRNA |

### Selectivity metrics (pre-define)
- **Selectivity index (SI)** = EC50(eutopic or CD8) / EC50(lesion stroma).  
- Time-matched % death at concentration that achieves ≥50% lesion-stroma ferroptotic death.  
- In co-culture: lesion-cell death ↑ while CD8 viability / IFNγ competence preserved (ELISPOT or supernatant IFNγ) `[UNCERTAIN: exact immune readout]`.

### Optional fertility-relevant eutopic functional assay
- In vitro decidualization (cAMP + MPA) ± drug → PRL / IGFBP1 — aligns with PMID 41722688 theme.

---

## 5. Controls

| Control | Purpose |
|---|---|
| Vehicle | Baseline |
| Erastin ± Fer-1 | Pathway authenticity |
| Sulfasalazine ± Fer-1 | Confirm ferroptosis vs off-mechanism cytotoxicity |
| Iron-overload media arm (CD8) | Reproduce disease-relevant stress (PMID 41146213 context) |
| Matched donor eutopic vs ectopic | Compartment genetics controlled |
| Non-endo control stroma (optional) | Specificity |
| Blank / media-only LDH | Toxicity artifact |

**Replication:** ≥3 biological donors; ≥2 technical replicates; pre-register analysis notebook structure.

---

## 6. Go / no-go criteria

| Decision | Criteria |
|---|---|
| **GO — selectivity hypothesis supported** | SI ≥ **3** (pre-agreed; adjustable) for lesion vs eutopic **and** lesion vs CD8 at Fer-1-rescuable exposures; lesion death is Fer-1 sensitive |
| **GO — formulation / targeting follow-up** | Monoculture SI marginal but co-culture / local delivery concept shows window → justifies lesion-localized delivery research (still not clinical advice) |
| **HOLD** | Sulfasalazine noisy / poorly soluble in partner system → switch emphasis to erastin-class tool + note sulfasalazine PK limits; or contested literature forces re-read of direction before scaling |
| **NO-GO for systemic xCT induction story** | Lesion EC50 ≈ CD8 ≈ eutopic (SI ~1) with authentic ferroptosis → reinforces WATCHLIST; do **not** promote sulfasalazine as systemic endo therapy |
| **NO-GO for direction reversal** | Only if partner + literature review jointly overturn lesion-induction evidence (high bar; contested EA papers alone insufficient) |

OpenEndo default if wet lab absent: **remain WATCHLIST**.

---

## 7. Ethics / safety notes

| Topic | Note |
|---|---|
| **Systemic toxicity context** | xCT blockade has historical systemic toxicity concerns (see m3-validation glioma-trial reference discussion); partner protocols stay *in vitro* unless separate animal tox exists |
| **Immune cell handling** | Blood / tissue biosafety; donor consent |
| **Reproductive toxicity framing** | Eutopic assays exist specifically because fertility risk is a *scientific* off-target, not a treatment suggestion |
| **Compound handling** | SDS for sulfasalazine / erastin; DMSO limits documented |
| **No patient guidance** | Do not translate µM culture exposures to mg oral doses in any public summary |
| **Immunosuppression** | Not primary for this lead (contrast sirolimus), but CD8 functional loss *is* the biological risk analogue |

---

## 8. Estimated complexity

| Dimension | Rating |
|---|---|
| Wet-lab skill | **High** (primary cells + immune co-culture + ferroptosis panel) |
| Analytics | High |
| Cost | Mid–high (primary tissue, fluorescent lipid probes, possible FACS) |
| Timeline | ~3–6 months including donor accrual |
| Dependency | Stronger if autologous CD8 required |

---

## 9. Computational already done vs wet lab must answer

| Already done | Wet lab must answer |
|---|---|
| Direction-of-effect synthesis (MEDIUM) | Quantitative **selectivity index** lesion vs CD8 vs eutopic |
| GEO: low lesional SLC7A11 / ACSL4 | Whether low xCT expression still yields inducer sensitivity (predicted yes if evasion is signaling-level) |
| Phase 1: sulfasalazine binds xCT pocket | Whether binding translates to Fer-1-rescuable death in *endo* cells |
| ADMET / RO5 notes for sulfasalazine | Local concentration achievable without eutopic/CD8 collapse |
| Contested suppress-ferroptosis papers flagged | Experimental reconciliation in same cell panel `[UNCERTAIN]` |
| Phase 2 xCT membrane MD | Optional later — **not** required to start selectivity panel (`phase2-plan.md` second wave) |

---

## 10. Suggested deliverables

1. EC50 / SI table across compartments + Fer-1 rescue.  
2. Co-culture immune competence readout.  
3. GO/HOLD/NO-GO memo mapped to §6.  
4. Optional short contested-literature experimental note for `ferroptosis-direction.md` append (human merge).

---

*OpenEndo draft protocol spec · 2026-09-14 · research infrastructure only · not medical advice.*
