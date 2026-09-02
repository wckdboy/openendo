# M3 repurposing validation — ranked candidate shortlist

Method per candidate: mechanism fit (endometriosis biology) · evidence
(ChEMBL + PubMed/clinical) · safety · novelty · confidence tag.
Sources cited inline; research hypothesis-generation, never clinical
advice. Updated as candidates are processed.

Status: 9/9 depth-checked (2026-09-02). Input:
`docs/data/repurposing_candidates.json` · digest `2026-09-02`.
Primary sources for all candidates verified against PubMed/Europe PMC/
ChEMBL/ClinicalTrials.gov (2026-09-02). GTEx/HPA expression
cross-reference below.

---

## Ranked shortlist (top line)

| Rank | Drug → target | Verdict | Confidence | Why (one line) |
|---|---|---|---|---|
| 1 | **Sirolimus → FKBP4** | TOP TIER | MEDIUM-HIGH | mTOR inhibition has independent endo evidence (senescence/infertility), antiproliferative direction, chronic-use safety data |
| 2 | **Cetrorelix → MRGPRX2** | VALIDATED AXIS | MEDIUM | MRGPRX2 = mast-cell pain mechanism in endo; drug already used in endo — target-validating, not novel repurposing |
| 3 | Tacrolimus/Cyclosporine → FKBP4 | WATCHLIST | LOW-MEDIUM | rat-model efficacy, but immunosuppressant baggage; FKBP4 hit ≠ clinical pharmacology (FKBP12-mediated) |
| 4 | **Sulfasalazine → SLC7A11** | WATCHLIST | LOW-MEDIUM | strong target axis, but ferroptosis direction-of-effect unresolved + xCT-dose toxicity |
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
  patient-facing mechanism. Rank by the drug's real pharmacology
  (naming note: FKBP4 gene = FKBP52 protein, FKBP5 = FKBP51 — the
  PR-chaperone literature uses the protein names: FKBP52 deficiency
  confers uterine progesterone resistance in vivo, J Clin Invest 2007
  PMID 17571166; Fkbp52−/− mice develop progesterone-resistant
  endometriosis, Am J Pathol 2008 PMID 18988805; FKBP4 mRNA is reduced
  in eutopic endometrium of women with endometriosis, Reproduction 2012
  PMID 22279148 + JCEM 2017 miR-29c PMID 27778641):
- **Sirolimus (rapamycin):** mTOR inhibition has an independent,
  growing endometriosis evidence base — "mTOR inhibitors as potential
  therapeutics for endometriosis" narrative review (Mol Hum Reprod
  2024, PMID 39579091); rapamycin shrinks lesions in mice (Exp Ther
  Med 2016, PMID 27347023); improves endo-associated infertility via
  ovarian senescence through PPARα/IGFBP2 (Mol Med Rep 2026, PMID
  41170754), with a retrospective human IVF corollary (Reprod Biomed
  Online 2024, PMID 37914557: 168 patients, 80 rapamycin-treated);
  antiproliferative direction; chronic-use safety established
  (transplant + LAM, EMA Rapamune). No registered endometriosis trial
  of rapamycin/sirolimus/any mTOR inhibitor on ClinicalTrials.gov
  (checked 2026-09-02). **TOP TIER.**
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

**Verdict: VALIDATED AXIS (target-validating, not repurposing) —
MEDIUM.** Two findings converge: (1) MRGPRX2 mediates mast-cell-induced
endometriosis **pain** via HBD-2 → MRGPRX2 → histamine → HRH1/TRPV1
sensory-neuron sensitization — MRGPRX2⁺ mast-cell density is increased
in lesions and mast-cell/MRGPRX2 loss or H1 blockade relieves
hyperalgesia in models (FASEB J **2025**, PMID 40600649; earlier draft
said 2026 — corrected); (2) cetrorelix (Cetrotide, 3 mg once weekly ×
8 weeks) is an established GnRH-antagonist endometriosis treatment —
regimen documented in small 2002 reports (Reprod Biomed Online, PMIDs
12537785 + 12470539); a registered phase-2 used a different SR
single-dose design and posted no results (NCT00244452). The ChEMBL
engagement is **measured but agonistic**: EC50 617/813 nM (pChEMBL
6.21/6.09, Ca²⁺ + β-arrestin assays; Lansu et al., Nat Chem Biol 2017,
PMID 28288109) — i.e. cetrorelix *activates* MRGPRX2; no clinical link
between cetrorelix and mast-cell action exists. As repurposing this is
moot; as **target validation** it is strong: MRGPRX2 **antagonism** is a
specific, non-hormonal pain target worth developing for endo pain.

## Candidate 9 — Dinoprostone (PGE2) → SLCO2A1

**Verdict: ✗ WRONG DIRECTION — target-validating only.** SLCO2A1 is the
prostaglandin transporter; endometriotic tissue overproduces PGE2 and
PGE2 drives lesion growth/VEGF. Dinoprostone IS PGE2 (agonist) — therapy
would need SLCO2A1 **blockade** or PGE2 synthesis inhibition. Like
estradiol: target validated (PG transport axis), drug is the wrong tool.

## Expression cross-reference (GTEx v8 / Human Protein Atlas, 2026-09-02)

Bulk-tissue expression for the ranked targets (HPA tissue-RNA consensus
nTPM; GTEx v8 median TPM — GTEx has no endometrium, nearest proxy =
uterus):

| Gene | Endometrium nTPM (HPA) | Uterus TPM (GTEx v8) | Lesional evidence | Verdict |
|---|---|---|---|---|
| FKBP4 | 30.6 (IHC high) | 43.5 | mRNA ↓ in eutopic EM endometrium (PMIDs 22279148, 27778641) | Plausible — present & mechanistically linked |
| MRGPRX2 | 0.0 (not detected) | 0.06 | MRGPRX2⁺ mast cells ↑ in lesions (PMID 40600649) | Plausible only via lesional mast cells |
| SLC7A11 | 0.2 (not detected) | 0.12 | SLC7A11 ↓ in ectopic lesions (PMID 42678895); xc⁻/erastin concept (PMID 41001371) | Weak expression support at disease site |

Interpretation: FKBP4 and (via lesional mast cells) MRGPRX2 pass the
"is the target there?" test. SLC7A11 is near-undetectable in normal
reproductive tissue and *down*-regulated in lesions — sulfasalazine's
on-target rationale at the disease site is the thinnest of the ranked
set, one reason it stays WATCHLIST LOW-MEDIUM. Sources:
proteinatlas.org ENSG00000004478-FKBP4/tissue ·
ENSG00000183695-MRGPRX2/tissue · ENSG00000151012-SLC7A11/tissue;
gtexportal.org/home/gene/&lt;ENSG&gt;.

---

## Next steps (DoD status)
1. ✅ Knowledge pages (in this PR): `entities/sirolimus.md` +
   `concepts/mrgprx2-pain.md` (SCHEMA-compliant, confidence tags) +
   knowledge index/log + llms.txt + wiki.html
2. ✅ GTEx/HPA expression cross-reference (section above)
3. ⏳ Share ranked list with human (wckdboy) for any clinical-interest
   decision — research output, not medical advice (see PR #12)

*Validation by Percival (Hermes Agent), 2026-09-02. All sources above are
public (PubMed/PMC/Europe PMC/ClinicalTrials.gov).*
