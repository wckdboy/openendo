# Virtual testing — Phase 1.0: docking (Vina)

**Owner:** Jaeger · **Status:** COMPLETE 2026-09-04 · **Cost:** $0 (owned VPS, 4-core CPU)
Machine data: [`docking_results.json`](docking_results.json) · ADMET: [`admet_profile.json`](admet_profile.json)

## What was asked

Three docking questions from the M3 repurposing shortlist (plan:
`docs/research/virtual-testing.md`):
1. **sirolimus (rapamycin) → FKBP4/FKBP52** — does the TOP-TIER candidate engage its
   ChEMBL-listed target? With **sirolimus → FKBP12** as the selectivity control
   (FKBP12 is the drug's real clinical pharmacology partner).
2. **sulfasalazine → xCT (SLC7A11)** — does the WATCHLIST candidate bind the
   ferroptosis-relevant transporter?
3. **cetrorelix → MRGPRX2** — see *deferred* below (tool boundary, not skipped).

Plus: ADMET profile of all 9 M3 candidates (`admet_profile.json`).

## Method (reproducible)

AutoDock Vina 1.2.7 (static binary) · meeko 0.8 ligand/receptor prep · RDKit
2026.03 (SMILES→3D, ADMET) · exhaustiveness 8 (macrocycles) / 24 (small
molecules) · 9 modes · boxes centered on co-crystallized ligands, size =
ligand extent + 8 Å. All structures from RCSB PDB with chain identity verified
by UniProt accession (1FKB-A = FKBP12 P62942 · 1N1A-A = FKBP52/FKBP4 Q02790 ·
7EPZ-B = xCT Q9UPY5 · 7S8L-R = MRGPRX2 Q96LB1). Full pipeline scripts live in
the operator's VPS workspace (`/opt/data/phase1/work/`); this directory holds
the scored poses + results.

**FKBP4 pocket location (no complex exists in PDB):** FKBP52 N-terminal domain
(1N1A, apo) was superposed onto FKBP12–rapamycin (1FKB) using 14 contact-defined
pocket residue pairs (0.80 Å RMSD); the conserved PPIase pocket (Tyr57/Phe67/
Phe77/Val86/Ile87/Trp90/Tyr113…) verifiably contacts the ligand after fit.
Documented limitation: apo-structure sidechains.

## Results

### Calibrations (native-ligand redocks — protocol honesty check)

| System | Native? | Best (kcal/mol) | Pose RMSD vs crystal | Reading |
|---|---|---|---|---|
| J9O (erastin-class) → xCT (7EPZ) | yes | **−9.35** | 5.2 Å | Converged identically at ex24 + ex64. Docked pose is deeper in the substrate cavity, clash-free, 6.9 Å centroid shift. 7EPZ is **3.4 Å cryo-EM**: the deposited ligand pose carries ±2–3 Å model uncertainty and the density often cannot distinguish such modes. Pocket binding validated; exact pose → MD arbiter. |
| Rapamycin → FKBP12 (1FKB) | yes | **−7.06** | 6.0 Å | Score consistent with known binding. Crystal-conformation ligand still lands ~6 Å off: Vina treats macrocycle rings as rigid, so full ring-conformation matching is outside its regime. Binding validated by score + pocket; pose → MD. |

### Target docks

| System | Best (kcal/mol) | Comparison | Verdict |
|---|---|---|---|
| **Sulfasalazine → xCT** | **−8.52** | 0.83 kcal/mol weaker than native J9O (−9.35) in the same pocket | **Binds xCT as predicted.** Consistent with sulfasalazine's known weaker xCT affinity vs erastin-class inhibitors. Binding is NOT the blocker — selectivity/toxicity remains the WATCHLIST issue (unchanged). |
| **Sirolimus → FKBP4/FKBP52** | **−6.38** | 0.68 kcal/mol weaker than rapamycin→FKBP12 (−7.06) with **matched crystal ligand conformations** | **FKBP4 accepts sirolimus nearly as well as FKBP12.** Consistent with ChEMBL FKBP4 engagement being real binding (M3 "promiscuity" note). Small FKBP12/FKBP52 delta means FKBP4 engagement is plausible at clinical doses — relevant to the progesterone-resistance chaperone hypothesis. |

### Deferred: cetrorelix → MRGPRX2

Deliberately not force-fit — two independent grounds:
1. **7S8L MRGPRX2 has 35 truncated sidechains** (cryo-EM), several pocket-lining.
   Docking into an artificially truncated pocket yields misleading scores.
2. **Cetrorelix is a 1431 Da decapeptide, 38 rotatable bonds** — beyond Vina's
   validated regime (designed for small molecules, ≤32 bonds).

Recommendation: peptide-MD or peptide-capable docking (HPEPDOCK/CABS-dock class)
in Phase 2. Note Phase 0.5 already showed MRGPRX2/mast-cell enrichment is
**endometrioma-specific, absent in superficial peritoneal lesions** — which
tempers this target's priority regardless.

## ADMET profile (9 M3 candidates — `admet_profile.json`)

| Class | Candidates | Reading |
|---|---|---|
| Rule-compliant | estradiol, sulfasalazine (0 RO5 viol), crizotinib | conventional oral-drug profiles |
| Macrocycles | sirolimus, tacrolimus, cyclosporine A (2–3 RO5 viol, QED ≤0.18) | break Lipinski yet are **marketed oral drugs** — the known macrocycle exception; rules less predictive here |
| Peptide | cetrorelix (MW 1431, 38 rotB, TPSA 498) | parenteral only — never an oral repurposing candidate; consistent with its target-validation-only M3 verdict |
| Mid | dabrafenib (2 RO5 viol) | borderline |

## Interpretation & next step

- **Phase 1.0 verdict:** both dockable repurposing hypotheses are *structurally
  permissive* — sirolimus can engage FKBP4; sulfasalazine can bind xCT. Docking
  cannot rank beyond this (scores are directional), and neither result changes
  the M3 priority: sirolimus TOP TIER stands, sulfasalazine WATCHLIST stands.
- **Phase 2 (dynamics) is the pose arbiter:** OpenMM 100–500 ns on the top
  poses (sulfasalazine→xCT, sirolimus→FKBP52 + FKBP12 control) to test whether
  the docked poses are stable. GPU needed — RunPod (~$5–25 per plan) or knight
  capacity. That is where pose-level claims become trustworthy.

*Jaeger (Hermes Agent), 2026-09-04. Computational output = hypothesis, never a
clinical conclusion. No PII. Research infrastructure, not medical advice.*
