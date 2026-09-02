# M3 repurposing validation — ranked candidate shortlist

Method per candidate: mechanism fit (endometriosis biology) · evidence
(ChEMBL + PubMed/clinical) · safety · novelty · confidence tag.
Sources are cited inline; nothing here is clinical advice. Hypothesis
generation for the research community. Updated as candidates are processed.

Status: 1/9 depth-checked (2026-09-02). Input:
`docs/data/repurposing_candidates.json` · digest `2026-09-02`.

---

## Candidate 1 — Sulfasalazine → SLC7A11 (xCT)

**Signal:** approved drug (RA/UC/Crohn's, decades of use) with measured
potency against SLC7A11 (pchembl ≥ 6, ChEMBL). SLC7A11/xCT is the
cystine-glutamate antiporter feeding glutathione synthesis — the
ferroptosis gatekeeper axis (with GPX4, also in our novel set).

### Mechanism fit: ⚠️ UNCERTAIN — direction of effect unresolved
- Sulfasalazine is a **specific xCT inhibitor** → GSH depletion →
  ferroptosis (extensively shown in cancer: glioma, uterine serous
  carcinoma, pancreatic/prostate/mammary — e.g. PMC7400102; Oncogene
  2015;10.1038/onc.2015.60).
- **But:** this week's endometriosis mechanism paper (SEMA3C, Sep 2026)
  reports ferroptosis induction as part of lesion *progression* — which
  would argue AGAINST a ferroptosis-inducing therapy. The endometriosis
  ferroptosis literature is genuinely split and must be read in full
  (does the disease resist ferroptosis, or exploit it?). **Resolve
  before any ranking above "watchlist".**
- Endometriotic cells share cancer-like features (survival, invasion,
  apoptosis resistance) — the killing rationale is plausible but
  unproven in endo tissue.

### Evidence: MEDIUM (other indications), LOW (endometriosis)
- ChEMBL potency: confirmed (screen hit).
- Cancer preclinical: strong and mechanistically coherent.
- Clinical: **two glioma trials with opposite lessons** —
  ISRCTN45828668 (2010) terminated at interim: no response, frequent
  grade 1–4 AEs, 2 deaths in debilitated patients (Europe PMC
  19840379); NCT04205357 phase 1 (Redox Biol 2026,
  10.1016/j.redox.2026.104241): 3-day pre-SRS dosing **well tolerated**
  (only 2× grade 3 transient lymphocytopenia), confirmed intratumoral
  GSH reduction + improved local control → phase II warranted.
- Endometriosis-specific: no trials found (verify on CT.gov) —
  novelty high, evidence nil.

### Safety: ⚠️ dose-dependent — the catch
- At standard anti-inflammatory doses (2–3 g/day): well tolerated
  chronic drug; monitoring needed (CBC, LFTs, creatinine).
- At xCT-inhibitory doses (~4.5–6 g/day, ~1.6× Crohn's dose): real
  toxicity — GI, hematologic (leukopenia/agranulocytosis), CNS,
  hypersensitivity (SJS/TEN/DRESS rare but serious), reversible
  oligospermia (males), G6PD hemolysis caution. The 2010 trial's AE
  burden (mean 7.2 AEs/patient) is the warning label.
- Population note: reproductive-age women — fertility/teratogenicity
  profile must be part of any assessment.

### Novelty: HIGH (for endometriosis)
No endo-specific clinical evidence located; not among the iScience
simvastatin/primaquine hits; first surfaced by our ChEMBL-activity
screen (converges with the SEMA3C/ferroptosis mechanism literature —
the two pipelines cross-validate the target axis, not the drug).

### Verdict: **WATCHLIST — not top-tier yet**
Strong target-axis convergence (SLC7A11/GPX4/ferroptosis + this week's
mechanism paper), proven drug, but (a) unresolved direction of effect in
endo biology and (b) xCT-inhibitory doses carry real toxicity. Priority
action: read the SEMA3C paper in full + search endo-specific ferroptosis
literature; if direction supports killing lesions, this climbs.

**Confidence: LOW-MEDIUM** (mechanism direction open · no endo evidence ·
toxicity at active dose).

---
*Next: candidates 2–9 (crizotinib, dabrafenib, cyclosporine, sirolimus,
tacrolimus, estradiol, cetrorelix, dinoprostone).*
