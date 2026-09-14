# Literature / lead update packet — 2026-09-14

> Spot-check of key corpus PMIDs + new 2025–2026 PubMed/Europe PMC hits for
> the top-3 OpenEndo leads. Compared against `digest-2026-09-11.md`.
> **No invented papers.** Every PMID below was fetched live (E-utilities
> efetch and/or Europe PMC core) on 2026-09-14.
>
> Raw: `_pubmed_raw_2026-09-14.json`, `_pubmed_filtered_2026-09-14.json`,
> `_epmc_spotcheck_2026-09-14.json`

## Method

1. **Spot-check** 28 key PMIDs already cited on `entities/sirolimus.md`,
   `concepts/mrgprx2-pain.md`, `concepts/ferroptosis.md`, and
   `ferroptosis-direction.md` via PubMed efetch — all resolved to matching
   titles/years (list in raw JSON).
2. **New searches** (PubMed esearch, `datetype=pdat`, 2025-01-01..2026-12-31):
   - `(sirolimus OR rapamycin OR "mTOR inhibitor" OR everolimus OR temsirolimus) AND (endometriosis OR endometrioma)` → **9**
   - `(FKBP4 OR FKBP52 OR "FK506 binding protein 4") AND (endometriosis OR endometrioma OR "progesterone resistance")` → **1**
   - `(MRGPRX2 OR "Mas-related G-protein" OR "mas related GPCR") AND (endometriosis OR endometrioma OR mast)` → **131** (mostly non-endo MRGPRX2 allergy/itch literature; filtered to endo)
   - `(mast cell OR mastocyte) AND (endometriosis OR endometrioma) AND (pain OR hyperalgesia OR histamine)` → **11**
   - `(sulfasalazine OR sulphasalazine OR SLC7A11 OR xCT OR ferroptosis) AND (endometriosis OR endometrioma)` → **62**
3. **Post-digest window** `endometriosis[Title/Abstract]`, pdat 2026-09-12..2026-09-14 → **3** new records.
4. Europe PMC corroboration for 13 priority PMIDs — all found.

## What changed since digest-2026-09-11

### Post-digest clinical/general (not lead-moving)

| PMID | Title (short) | Relevance to leads |
|---|---|---|
| [42732853](https://pubmed.ncbi.nlm.nih.gov/42732853/) | Predictors of segmental resection for isolated rectal endometriosis | Surgical pathway only |
| [42731417](https://pubmed.ncbi.nlm.nih.gov/42731417/) | Compartment-specific inflammation–metabolism remodeling (scRNA + bulk) | Mechanism context; not mTOR/MRGPRX2/xCT drug signal |
| [42730566](https://pubmed.ncbi.nlm.nih.gov/42730566/) | WHO infertility guideline commentary | Policy/access; not repurposing |

**None of these change M3 verdicts.**

### Lead-adjacent in the Sep 4–14 window

| PMID | Already in digest-09-11? | Note |
|---|---|---|
| [42698143](https://pubmed.ncbi.nlm.nih.gov/42698143/) FIN56 ferroptosis | **Yes** | Third independent induction confirmation; sulfasalazine WATCHLIST unchanged |
| [42728524](https://pubmed.ncbi.nlm.nih.gov/42728524/) Ferroptosis-related genes as diagnostic/predictive biomarkers (bioinformatics) | **No — new** | Computational biomarker paper; abstract frames ferroptosis as contributing to ectopic migration. Hypothesis-generating only; does **not** overturn lesion-cell induction vs immune/eutopic caveats in `ferroptosis-direction.md` |

---

## Lead 1 — Sirolimus / mTOR (+ FKBP4 / PR-resistance note)

### Corpus spot-check (still live)

All prior sirolimus/FKBP4 PMIDs resolve: 39579091 (narrative mTOR review), 27347023 (mouse rapamycin), 41170754 (PPARα/IGFBP2 infertility), 37914557 (retrospective IVF cohort), 22279148 / 27778641 / 17571166 / 18988805 (FKBP4/FKBP52 PR-resistance axis).

### New / under-cited 2025–2026 endo+mTOR hits (filtered)

| PMID | What it actually says | Effect on OpenEndo claim |
|---|---|---|
| [40532686](https://pubmed.ncbi.nlm.nih.gov/40532686/) | **S1PR4** promotes EESC viability/invasion/glycolysis via **mTOR**; AZD8055 (mTOR inhibitor) used as pathway tool in cells | Strengthens **mTOR pathway relevance** in lesion stroma; **not** a sirolimus clinical study |
| [40200774](https://pubmed.ncbi.nlm.nih.gov/40200774/) | Iranian case–control: PIK3CA / AKT1 / mTOR SNPs associated with endometriosis susceptibility (preliminary) | Genetic backdrop for PI3K–AKT–mTOR; low clinical weight |
| [41483374](https://pubmed.ncbi.nlm.nih.gov/41483374/) | Fucoxanthin modulates macrophage pyroptosis via PI3K/AKT/mTOR (endo among disease contexts) | Adjacent natural-product / macrophage note — not sirolimus |
| [41603922](https://pubmed.ncbi.nlm.nih.gov/41603922/) | Ramipril repurposing vs EMT via PI3K/AKT/S6K1 in rat endo model | Different drug; same pathway neighbourhood |

**FKBP4/PR-resistance:** the dedicated 2025–2026 FKBP4/FKBP52 + endometriosis search returned essentially the known axis (no new human interventional FKBP4-restoring drug paper in this pass). Keep the existing separation: **mTOR inhibition ≠ restoring FKBP4**.

**Net vs digest-09-11:** no new sirolimus/rapamycin endo trial; pathway papers reinforce mTOR biology without upgrading clinical evidence. TOP TIER novelty (zero CT.gov) still holds.

---

## Lead 2 — MRGPRX2 antagonism (not cetrorelix-as-drug)

### Corpus spot-check (still live)

PMID 40600649 (FASEB J MRGPRX2→HBD-2→histamine→HRH1/TRPV1) remains the end-to-end pain axis paper. Mast-cell background PMIDs 17007852, 41079937, 40028674, 31998139 resolve. Cetrorelix agonism off-target PMID 28288109 resolves.

### New endo+mast / histamine hits (not MRGPRX2 antagonists)

| PMID | What it actually says | Effect on OpenEndo claim |
|---|---|---|
| [40948761](https://pubmed.ncbi.nlm.nih.gov/40948761/) | Review: neuroinflammation / JAK–STAT + **mast-cell activation** as pain drivers; discusses JAK inhibitors and mast-cell stabilizers as **repurposing** candidates | Supports mast-cell pain framing; does **not** deliver an MRGPRX2 antagonist |
| [41516088](https://pubmed.ncbi.nlm.nih.gov/41516088/) | Histamine landscape across lesion subtypes: HDC↑; HRH1–4 protein on epithelial/immune/nerve; transcript levels of HRH1–4 not differentially expressed | Strengthens **histamine** arm of the axis OpenEndo already tracks downstream of MRGPRX2 |
| [42511984](https://pubmed.ncbi.nlm.nih.gov/42511984/) | Neuroimmune pain framework (endo ↔ lipedema); mast cells / TRPV1 / CGRP | Context review |
| [42515755](https://pubmed.ncbi.nlm.nih.gov/42515755/) | Immune-network review including mast cells / emerging immunomodulation | Context review |

**Important filter:** most 2025–2026 PubMed hits for “MRGPRX2” are **non-endo** (urticaria, itch, atopic dermatitis, headache, UTI). Do **not** import those as endometriosis evidence. No new endo-specific MRGPRX2-antagonist efficacy paper found in this pass.

**Net:** VALIDATED AXIS unchanged — build/find an **antagonist**; do not promote cetrorelix as the lead.

---

## Lead 3 — Sulfasalazine / xCT ferroptosis (WATCHLIST)

### Corpus spot-check (still live)

Direction verdict PMIDs in `ferroptosis-direction.md` all resolve, including SEMA3C 42678895, CD8⁺ T-cell ferroptosis 41146213, erastin concept 41001371, MGST3 42234252, HSD11B1 42151966, FZD7–SLC7A11 41241001, andrographolide 41408483, placental EVs 42186752, eutopic fertility costs 41722688 / 41437396. Digest FIN56 paper 42698143 resolves.

### New ferroptosis papers that matter for the WATCHLIST

**Reinforce lesion-cell induction / ferroptosis dysregulation (directionally consistent with WATCHLIST mechanism):**

| PMID | Note |
|---|---|
| [42698143](https://pubmed.ncbi.nlm.nih.gov/42698143/) | FIN56 induction shrinks lesions (already in digest-09-11) |
| [40983106](https://pubmed.ncbi.nlm.nih.gov/40983106/) | Estradiol–MBOAT1–ferroptosis axis in ESC models + mouse |
| [41422938](https://pubmed.ncbi.nlm.nih.gov/41422938/) | EGR1→HMOX1 promotes ferroptosis in EM (bioinformatics + validation) |
| [41452077](https://pubmed.ncbi.nlm.nih.gov/41452077/) | USP33 / ferritinophagy / Hippo–YAP; USP33 loss → ferroptosis resistance in EESCs |
| [42728524](https://pubmed.ncbi.nlm.nih.gov/42728524/) | Ferroptosis-related gene biomarker bioinformatics |

**Compartment / host caveats (why systemic xCT block stays WATCHLIST) — newly salient:**

| PMID | Note |
|---|---|
| [42081613](https://pubmed.ncbi.nlm.nih.gov/42081613/) | Electroacupuncture claimed to **inhibit ovarian ferroptosis** (↑GPX4 via Nrf2) and improve ovarian function in an endo mouse model — **eutopic/ovarian protection narrative** |
| [42155249](https://pubmed.ncbi.nlm.nih.gov/42155249/) | Electroacupuncture claimed to **suppress ferroptosis** in ectopic *and* eutopic murine endometrium via Nrf2 — appears to **conflict** with “always induce in lesions” if read naively |

**How to read the EA papers without inventing resolution:** they are preclinical modality papers (electroacupuncture), not sulfasalazine trials. They underscore the existing `ferroptosis-direction.md` point that **compartment matters** (ovary / eutopic vs lesion epithelium-stroma) and that “ferroptosis good/bad” is not a single switch. They do **not** create a registered xCT-inhibitor endo trial, and they do **not** clear sulfasalazine’s selectivity/toxicity problem. Flag as **contested nuance** for wiki update; do not silently overwrite the MEDIUM induction-in-lesion-cells verdict.

**Sulfasalazine itself:** still **zero** PubMed interventional endo trial hits in this pass; still **zero** CT.gov.

**Net:** WATCHLIST unchanged. Induction-in-lesion-cells remains the mechanistic lean; selectivity + eutopic/immune/ovarian costs remain the blockers. New biomarker/EA papers belong in a caveats paragraph, not a status upgrade.

---

## Digest carry-overs still open

- Relugolix-CT 104-week post hoc (PMID 42719373) — clinical shared-decision item; not a top-3 lead.
- Pain transcriptomic signature / IL16 (PMID 42720599) — complementary to mast/MRGPRX2 pain thread.
- No follow-up yet to dienogest PROM study (PMID 42692407) flagged in digest-09-11.

---

*Literature packet draft for DrDoc. Live PMIDs only. Not medical advice.
Prefer merging knowledge updates only after human review of the flagged EA/compartment nuance.*
