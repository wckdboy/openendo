# M3 repurposing validation — ranked candidate shortlist

Method per candidate: mechanism fit (endometriosis biology) · evidence
(ChEMBL + PubMed/clinical) · safety · novelty · confidence tag.
Sources cited inline; research hypothesis-generation, never clinical
advice. Updated as candidates are processed.

Status: 9/9 depth-checked (2026-09-02). Input:
`docs/data/repurposing_candidates.json` · digest `2026-09-02`.

---

## Ranked shortlist (top line)

| Rank | Drug → target | Verdict | Confidence | Why (one line) |
|---|---|---|---|---|
| 1 | **Sirolimus → FKBP4** | TOP TIER | MEDIUM-HIGH | mTOR inhibition has independent endo evidence (senescence/infertility), antiproliferative direction, chronic-use safety data |
| 2 | **Cetrorelix → MRGPRX2** | VALIDATED AXIS | MEDIUM | MRGPRX2 = mast-cell pain mechanism in endo; drug already used in endo — target-validating, not novel repurposing |
| 3 | Tacrolimus/Cyclosporine → FKBP4 | WATCHLIST | LOW-MEDIUM | rat-model efficacy, but immunosuppressant baggage; FKBP4 hit ≠ clinical pharmacology (FKBP12-mediated) |
| 4 | ~~Sulfasalazine → SLC7A11~~ | ✗ WRONG-DIRECTION | MEDIUM | deep-dive verdict ([ferroptosis-direction.md](https://raw.githubusercontent.com/wckdboy/openendo/main/docs/research/evidence/ferroptosis-direction.md)): ferroptotic signaling tilts disease-supporting (SEMA3C/Fer-1, VEGFA/IL8 angiogenesis); xCT-dose toxicity adds weight |
| 5 | Crizotinib/Dabrafenib → ACVR1B | WATCHLIST | LOW | ACVR1B/ALK4→aromatase mechanism is real, but cancer-TKI fertility baggage + off-target heavy |
| — | Estradiol → GPER1 | ✗ WRONG DIRECTION | — | agonist of a proliferation-driving receptor — target-validating only |
| — | Dinoprostone → SLCO2A1 | ✗ WRONG DIRECTION | — | it IS PGE2; therapy would need transporter *blockade* |

---

## Candidate 1 — Sulfasalazine → SLC7A11 (xCT)

**Verdict: WATCHLIST — LOW-MEDIUM.** Specific xCT inhibitor → GSH
depletion → ferroptosis (strong cancer preclinical, PMC7400102;
Oncogene 2015, 10.1038/onc.2015.60). ⚠️ Direction of effect unresolved:
SEMA3C/ferroptosis paper (Sep 2026) links ferroptosis to lesion
progression — must be read in full before ranking higher. Safety split:
fine at RA doses; xCT-active doses (4.5–6 g) — 2010 glioma trial
terminated (ISRCTN45828668, mean 7.2 AEs/patient) vs 2026 phase 1
(NCT04205357, Redox Biol 10.1016/j.redox.2026.104241) well tolerated at
3-day dosing with confirmed GSH reduction. No endo trials; novelty high.

## Candidate 2+3 — Crizotinib / Dabrafenib → ACVR1B

**Verdict: WATCHLIST — LOW.** Mechanism is real and endo-specific:
ACVR1B/ALK4 mediates **activin A → aromatase** (local estrogen synthesis)
in endometriosis (ALK4-Smad-aromatase axis), and ALK4 haplodeficiency
mitigates disease in models. But both drugs are targeted cancer TKIs:
fertility/reproductive toxicity (crizotinib: ovarian follicle necrosis in
rats, reversible hypogonadism), chronic-dosing burden, and their primary
pharmacology (ALK/ROS1/MET; BRAF) is irrelevant to endo — off-target
engagement at useful ACVR1B doses is unproven. Direction (kinase
inhibition → less aromatase) is correct; drug fit is poor. Better: a
selective ACVR1B inhibitor program, not these TKIs.

## Candidate 4+5+6 — Cyclosporine / Sirolimus / Tacrolimus → FKBP4

**Verdict: TOP TIER (sirolimus) — WATCHLIST (CsA/tacro).**
- Mechanism nuance: FKBP4/FKBP52 is the progesterone-receptor
  co-chaperone that ENHANCES PR transcription (FKBP5 inhibits); FKBP4 is
  HOXA10-regulated in endometriosis — PR chaperone biology is central to
  progesterone resistance. **But** the clinical pharmacology of these
  drugs runs through FKBP12 (calcineurin for CsA/tacro; mTOR for
  sirolimus) — the ChEMBL FKBP4 hit is binding promiscuity, not their
  patient-facing mechanism. Rank by the drug's real pharmacology:
- **Sirolimus (rapamycin):** mTOR inhibition has an independent,
  growing endometriosis evidence base — "mTOR inhibitors as potential
  therapeutics for endometriosis" reviews; rapamycin improves
  endo-associated infertility via ovarian senescence
  (PPARα/IGFBP2); antiproliferative direction; chronic-use safety
  profile established (20+ years transplant/oncology). **TOP TIER.**
- **CsA/tacrolimus:** efficacy in rat endometriosis model (anti-
  inflammatory/immunomodulatory), but chronic immunosuppression
  (infection, nephrotoxicity) is heavy for a benign chronic disease.
  Watchlist only.

## Candidate 7 — Estradiol → GPER1

**Verdict: ✗ WRONG DIRECTION — target-validating only.** GPER
expression is increased in endometriosis (Plante 2012, cited 141×); GPER
agonist G-1 stimulates endometrial proliferation. Estradiol is the
endogenous GPER **agonist** — activating a proliferation-driving receptor
in a proliferative disease is anti-therapeutic. The hit **validates
GPER1 as a target** (antagonist development), not estradiol as a drug.
Textbook case for the direction-of-effect review step.

## Candidate 8 — Cetrorelix → MRGPRX2

**Verdict: VALIDATED AXIS — MEDIUM.** Two independent findings converge:
MRGPRX2 mediates mast-cell-induced endometriosis **pain** via
histamine/HRH1/TRPV1 sensory-neuron sensitization (2026), and cetrorelix
(Cetrotide, 3 mg weekly × 8 wks) is an established GnRH-antagonist endo
treatment. Cetrorelix's peptide backbone plausibly engages MRGPRX2 (a
peptide/MRP receptor). As repurposing this is moot (already used in
endo); as **target validation** it is strong: MRGPRX2 antagonism is a
specific, non-hormonal pain target worth developing for endo pain.

## Candidate 9 — Dinoprostone (PGE2) → SLCO2A1

**Verdict: ✗ WRONG DIRECTION — target-validating only.** SLCO2A1 is the
prostaglandin transporter; endometriotic tissue overproduces PGE2 and
PGE2 drives lesion growth/VEGF. Dinoprostone IS PGE2 (agonist) — therapy
would need SLCO2A1 **blockade** or PGE2 synthesis inhibition. Like
estradiol: target validated (PG transport axis), drug is the wrong tool.

---

## Next steps (for the DoD)
1. Knowledge pages: `sirolimus-repurposing.md`, `mrgprx2-pain.md`
   (SCHEMA-compliant, confidence tags) + llms.txt update
2. GTEx expression cross-reference: are FKBP4/MRGPRX2/SLC7A11 actually
   elevated in relevant tissue (validates target side)
3. Share ranked list with human (wckdboy) for any clinical-interest
   decision — research output, not medical advice

*Validation by Percival (Hermes Agent), 2026-09-02. All sources above are
public (PubMed/PMC/Europe PMC/ClinicalTrials.gov).*
