# Virtual testing — Phase 2 run package (OpenMM)

**Owner:** Galahad · **Status:** RUN PACKAGE READY — NOT STARTED · **Date:** 2026-09-12
**Cost so far:** $0 · **Blocker:** human compute-budget approval only
Machine data: [`phase2-plan.json`](phase2-plan.json) · Inputs: [`inputs/`](inputs/)

> Computational output = hypothesis, never a clinical conclusion. Not medical
> advice. No GPU has been rented for this phase.

Phase 1.0 docking (PR #22, `$0`) left MD-ready ligand poses and two open
structural questions. This package is the concrete job spec so a $5–25
RunPod-class run can start the moment a human approves spend. It does **not**
complete Phase 2. Trajectories do not exist yet.

Source artifacts (do not re-dock):

| Artifact | Path |
|---|---|
| Phase 1 write-up | [`../phase1/phase1.md`](../phase1/phase1.md) |
| Docking scores | [`../phase1/docking_results.json`](../phase1/docking_results.json) |
| Ligand poses (PDBQT) | [`../phase1/poses/`](../phase1/poses/) |
| Ladder / infra | [`../../virtual-testing.md`](../../virtual-testing.md) |
| M3 verdicts | [`../../evidence/m3-validation.md`](../../evidence/m3-validation.md) |

---

## 1. What Phase 2 is for

Docking said both dockable hypotheses are *structurally permissive*
(sirolimus can sit in FKBP4; sulfasalazine can sit in xCT) but **pose-level
claims were deferred**: native redocks scored well with 5–6 Å pose RMSD vs
deposited ligands (Vina rigid-macrocycle limit + 3.4 Å cryo-EM uncertainty
on 7EPZ). Phase 2 is the pose arbiter: does the ligand stay in the pocket
on a 100 ns timescale, and do binding-site contacts resemble the docking
pose?

MD cannot answer selectivity, toxicity, or clinical efficacy. Those stay
with the M3 evidence files.

---

## 2. Prioritized systems

Rank is **scientific value per expected GPU-hour**, not a new M3 ranking.

| Rank | ID | System | Why it is (or is not) first | Cost class | First-run? |
|---|---|---|---|---|---|
| 1 | `p2a_fkbp12_crystal` | 1FKB + **deposited RAP** | Protocol positive control. If crystal rapamycin leaves FKBP12, the protocol is unusable and no other verdict moves. | Soluble, cheap | **Yes — required** |
| 2 | `p2a_fkbp52_vina` | aligned 1N1A FK1 + Phase 1 Vina RAP (−6.38) | TOP-TIER structural question: is the docked FKBP4 pose stable? Matched ligand vs the FKBP12 control. | Soluble, cheap | **Yes — required** |
| 3 | `p2a_fkbp12_vina` | 1FKB + Phase 1 Vina RAP (−7.06) | Tests whether the 6 Å-off Vina pose relaxes toward the crystal mode or leaves. Useful, not required if #1 is stable. | Soluble, cheap | Optional stretch |
| 4 | `p2b_sulfasalazine_xct` | 7EPZ-B + sulfasalazine (−8.52) | Binding is already *not* the WATCHLIST blocker (selectivity/toxicity is). Membrane transporter — setup risk can burn the whole $10–25. | Membrane, $$ | **No** (second job) |
| 5 | `p2b_j9o_xct_calib` | 7EPZ-B + native J9O (−9.35) | Required *if* #4 runs (membrane protocol control). Same cost class as #4. | Membrane, $$ | Only with #4 |
| 6 | `p2c_cetrorelix_mrgprx2` | 7S8L + peptide | Phase 1 tool-boundary deferral. Phase 0.5: mast-cell/MRGPRX2 enrichment is endometrioma-specific, absent in peritoneal lesions — priority already tempered. Needs sidechain rebuild + peptide-capable protocol. | Membrane peptide, $$$ | **No** |

### Default recommendation for a ~$10–25 first job: **P2-A**

Run **#1 then #2** at **100 ns production** each (4 fs HMR), same force
field, same box recipe.

- Answers: “does our protocol keep a known complex bound?” and “does the
  Phase 1 FKBP52 pose hold?”
- Fits the published $5–25 band on an RTX 4090 with headroom for a crash
  restart or a 20 ns peek.
- **Kill switch:** if `p2a_fkbp12_crystal` shows ligand COM leaving the
  pocket by 20 ns, **stop the pod**. Do not spend the second 100 ns until
  the protocol is reviewed. That failure is a methods fail, not a
  sirolimus-FKBP4 biology fail.

Do **not** start xCT membrane work on the first $10–25 unless a human
explicitly prefers the WATCHLIST question over the TOP-TIER one. A botched
CHARMM-GUI embed wastes the budget without changing M3 (see §7).

---

## 3. Inputs (what exists today)

Phase 1 stored **ligand-only** PDBQTs. Receptors were prepared on the
operator VPS (`/opt/data/phase1/work/`, not in repo). This package
reconstructs the FKBP frames from public RCSB entries.

### 3.1 Pose files → converted ligands

| Phase 1 PDBQT | Converted PDB | Vina (kcal/mol) | Real atoms |
|---|---|---|---|
| `phase1/poses/sulfasalazine_xct_top.pdbqt` | `inputs/ligands/sulfasalazine_xct_top.pdb` | −8.524 | 31 |
| `phase1/poses/rapamycin_fkbp52_top.pdbqt` | `inputs/ligands/rapamycin_fkbp52_top.pdb` | −6.378 | 68 |
| `phase1/poses/rapamycin_fkbp12_calib_top.pdbqt` | `inputs/ligands/rapamycin_fkbp12_calib_top.pdb` | −7.063 | 68 |
| `phase1/poses/j9o_xct_calib_top.pdbqt` | `inputs/ligands/j9o_xct_calib_top.pdb` | −9.354 | 39 |
| *(extracted)* 1FKB `RAP` A108 | `inputs/ligands/rapamycin_1fkb_crystal.pdb` | n/a (crystal) | 65 heavy |

Rapamycin PDBQTs contain two meeko **G0 dummy atoms** (macrocycle
ring-closure). They are not chemistry and were dropped (70 → 68). `CG0`
types were written as carbon. SMILES + meeko `SMILES IDX` maps live in
`inputs/smiles_idx/*.json`.

### 3.2 FKBP receptor reconstruction (done, CPU, $0)

Phase 1 superposed 1N1A onto 1FKB with 14 contact-defined pocket pairs
(reported 0.80 Å). Public 1N1A **lacks residues 72–75** (the FKBP12
Arg42-loop homolog), so those 14 pairs cannot be reproduced exactly.

This package aligned **11 present homolog CA atoms**
(Tyr57/Phe67/Asp68/Phe77/Glu85/Val86/Ile87/Trp90/Tyr113/Ile122/Phe130
↔ FKBP12 Tyr26/Phe36/Asp37/Phe46/Glu54/Val55/Ile56/Trp59/Tyr82/Ile90/Phe99).

| Check | Result |
|---|---|
| Pocket CA RMSD (11 pairs) | **1.005 Å** (Phase 1: 0.80 Å / 14 pairs) |
| Aligned vs 1FKB pocket-centroid delta | 0.000 Å (Kabsch) |
| Vina RAP vs crystal RAP centroid | 2.26 Å (compatible with Phase 1’s ~6 Å all-atom pose RMSD: COM is closer than atom-mapped RMSD) |
| Vina RAP COM vs pocket CA COM | 5.1 Å (FKBP12) / 5.5 Å (FKBP52) — same range as crystal RAP (6.7 Å) |

Assembled complexes (protein heavy atoms + ligand, no water):

- `inputs/complexes/p2a_fkbp12_crystal_rap.pdb`
- `inputs/complexes/p2a_fkbp12_vina_rap.pdb`
- `inputs/complexes/p2a_fkbp52_vina_rap.pdb`

Receptors: `inputs/receptors/1FKB_A_protein.pdb`,
`inputs/receptors/1N1A_A_aligned_to_1FKB.pdb`.

**1N1A gap caveat (confidence: high that the gap exists; medium that it
matters):** FKBP12 Arg42 is a documented rapamycin contact. The FKBP52
structure used here has no Arg73 loop. First-run protocol **does not**
homology-model 72–75 (that would change the receptor vs the docking
frame). If FKBP52 unbinds, the missing loop is a confounder — do **not**
read it as “FKBP4 cannot bind sirolimus.” If it stays bound *despite* the
gap, that is the stronger result.

Regenerate with:

```bash
# 1FKB + 1N1A are CC0 from RCSB; cache locally, do not commit the raw downloads
curl -fsSL https://files.rcsb.org/download/1FKB.pdb -o /tmp/phase2-pdb/1FKB.pdb
curl -fsSL https://files.rcsb.org/download/1N1A.pdb -o /tmp/phase2-pdb/1N1A.pdb
python3 scripts/phase2_prep.py --assemble --pdb-cache /tmp/phase2-pdb
```

### 3.3 Prep still required on the GPU box (CPU minutes, $0 extra)

1. **PDBFixer** on the protein: add missing sidechain atoms + hydrogens at
   pH 7.4. Leave 1N1A 72–75 unmodelled (`missingResidues = {}`).
2. **OpenFF molecule** via `Molecule.from_pdb_and_smiles(ligand.pdb, smiles)`
   using the SMILES in `inputs/smiles_idx/*.json`.
3. **Protonation**
   - Rapamycin / J9O: keep the pose/SMILES protonation (net 0). No
     ionizable group that changes at pH 7.4.
   - Sulfasalazine (when P2-B runs): carboxylate should be **deprotonated**
     (net −1). The Phase 1 PDBQT is the acid (`O=C(O)…` + carboxylic HD).
     Strip that HD and use `[O-]C(=O)c1cc(N=Nc2ccc(S(=O)(=O)Nc3ccccn3)cc2)ccc1O`.
     Phenol and sulfonamide NH stay protonated.
4. **xCT / 7EPZ (P2-B only, not first run):** fetch 7EPZ, extract chain B
   (xCT, UniProt Q9UPY5), embed in a POPC (or POPC:cholesterol) bilayer
   with CHARMM-GUI or equivalent, **do not** solvate the transporter in
   water-only. Ligand coords are already in the 7EPZ frame (centroid
   ~146, 145, 125 Å).

---

## 4. OpenMM protocol sketch (P2-A)

Implemented as `scripts/phase2_run_openmm.py`. Defaults match this table.

| Step | Setting |
|---|---|
| Engine | OpenMM 8.x, CUDA platform |
| Protein FF | Amber ff14SB (`amber14-all.xml`) |
| Ligand FF | OpenFF Sage **2.2.1** |
| Water | TIP3P-FB (`amber14/tip3pfb.xml`) |
| Ions | 150 mM NaCl, neutralized |
| Box | rhombic dodecahedron / cubic, **1.2 nm** padding |
| Constraints | HBonds + rigid water |
| HMR | hydrogen mass 1.5 amu → **4 fs** timestep |
| Nonbonded | PME, cutoff 1.0 nm (OpenMM default for amber14) |
| Integrator | Langevin Middle, 300 K, γ = 1/ps |
| Barostat | Monte Carlo, 1.0 bar |
| Minimize | 5000 steps (or energy/force convergence) |
| Equilibration | 1 ns NPT, unrestrained first-run (if the crystal control is unstable, next iteration adds 400 kJ/mol/nm² backbone+ligand restraints for 1 ns then release) |
| Production | **100 ns NPT** (configurable `--ns`) |
| Recording | DCD every 100 ps; checkpoint every 1 ns |
| Seed | 20260912 (override per repeat) |

**Analysis (same for both P2-A systems):**

1. **Protein Cα RMSD** vs first production frame (stability of the fold).
   Fail the *run* (not the biology) if Cα RMSD drifts > 4 Å and stays there.
2. **Ligand RMSD** after fitting protein Cα to the starting complex —
   vs the **docking/crystal starting pose**.
3. **Ligand COM distance** to the pocket CA centroid (11-residue list above).
4. **Binding-site contacts** (heavy-atom distance ≤ 4.0 Å) to the named
   pocket residues; occupancy over the last 50 ns.
5. **Pose-likeness:** fraction of frames with ligand RMSD < 3 Å vs start.

Optional later (not in the $10–25 critical path): MM/GBSA, water
occupancy, FKBP12-vs-FKBP52 contact fingerprints, a second seed.

---

## 5. GPU-hours and cost bands

Prices below are **public RunPod list rates as of mid-2026**, not a quote.
Community Cloud RTX 4090 ≈ **$0.34/h**; Secure Cloud RTX 4090 ≈ **$0.69/h**;
A100 SXM 80 GB ≈ **$1.39/h**. Console price on the day of launch wins.
Throughput is the largest uncertainty (±2×): OpenMM version, PME, and
whether HMR/4 fs is stable for the macrocycle.

Assumptions for P2-A (each complex ~25–40 k atoms after solvation):

| Throughput assumption | 2 × 100 ns + ~2 h overhead |
|---|---|
| Conservative — 200 ns/day | ~26 GPU-h |
| Optimistic — 400 ns/day | ~14 GPU-h |

| Job | Community 4090 ($0.34/h) | Secure 4090 ($0.69/h) | A100 ($1.39/h) |
|---|---|---|---|
| **P2-A recommended** (2 × 100 ns) | **~$5–9** | **~$10–18** | ~$19–36 (not worth it for these box sizes) |
| P2-A + optional Vina-FKBP12 100 ns | ~$7–14 | ~$15–27 | skip |
| P2-A stretch 2 × 200 ns | ~$10–18 | ~$20–36 | skip |
| P2-A stretch 2 × 500 ns | ~$25–45 | over the $25 first-run band | skip |
| P2-B xCT membrane 100 ns (80–150 k atoms, ~80–150 ns/day) | ~$7–20 **plus** a real risk of a failed embed | ~$15–40 | only if 4090 VRAM/setup fails |

**First-run budget call:** approve **$10–25**, launch **one** RTX 4090
Community pod if available, otherwise Secure. That covers P2-A at 100 ns
and a restart. Do not pre-approve P2-B or 500 ns.

Knight / laptop GPU is an equally valid $0 substitute; same scripts.

---

## 6. Success / fail criteria

Apply to the **last 50 ns** unless noted. “Bound” = ligand COM stays
within 8 Å of the pocket CA centroid **and** ≥3 pocket contacts persist
at ≥30% occupancy. Thresholds are operational, not affinity estimates.

| Outcome | `p2a_fkbp12_crystal` | `p2a_fkbp52_vina` | What it means |
|---|---|---|---|
| **A — protocol + pose OK** | bound; ligand RMSD typically < 3 Å vs crystal | bound; ligand RMSD < 3 Å vs docked pose, or 3–5 Å but contacts persist | Protocol works; docked FKBP52 pose is a stable local basin |
| **B — protocol OK, pose drifts** | bound / crystal-like | bound but ligand RMSD > 5 Å, new contact set | FKBP4 still engages; Phase 1 *pose* is wrong. Re-cluster; do not quote the Vina pose |
| **C — protocol OK, FKBP52 unbound** | bound | ligand leaves by 50 ns | Docked pose is not stable on this receptor (gap confounder applies). Does **not** falsify ChEMBL FKBP4 binding |
| **D — protocol fail** | unbound by 20 ns | (do not interpret) | Stop. Methods problem. No M3 change |
| **E — both unbound after 100 ns** | unbound | unbound | Treat as D until a restrained-eq retry is done |

Crystal-control peek at **20 ns** is mandatory before starting (or
continuing) the FKBP52 production on a tight budget.

---

## 7. What would change M3 watchlist / top-tier verdicts

M3 ranks drugs by mechanism, evidence, safety, novelty — not by a docking
score. Phase 1 already said neither dock *changes* priority. Phase 2 is
stricter: most outcomes **do not** move the published labels.

| M3 pair | Current label | Phase 2 result that would change the label | What does *not* change it |
|---|---|---|---|
| Sirolimus → FKBP4 | **TOP TIER** (MEDIUM-HIGH), driven by **mTOR / senescence evidence**, not by FKBP4 docking | **No 100 ns trajectory should promote or demote TOP TIER.** Outcome C may downgrade *only* the side-claim “FKBP4 engagement is plausible at clinical doses” from Phase 1 (medium-low structural confidence → low) in `m3-validation.md` / `sirolimus.md`. The mTOR rationale stays. | Outcome A confirms the structural side-claim; still not a clinical result. Outcome D = no edit. |
| Sulfasalazine → SLC7A11 | **WATCHLIST** (LOW-MEDIUM); blocker = selectivity/toxicity, not binding | **No MD result changes WATCHLIST.** Binding was already accepted as non-blocking. Unstable pose weakens the Phase 1 “binds as predicted” sentence (confidence ↓) but ferroptosis-direction + systemic caveats are independent. | A stable pose is the expected, low-information result. |
| Tacrolimus / CsA → FKBP4 | WATCHLIST | Still “only if sirolimus path validates” (`virtual-testing.md`). P2-A outcome A is **not** that validation (wrong drugs). | Do not start these on the first budget. |
| Cetrorelix → MRGPRX2 | VALIDATED AXIS | P2-C is out of scope. Phase 0.5 already tempers disease-site relevance. | — |

**Hard rule:** 100 ns of implicit-solvent-free, single-seed MD is not
binding free energy. Do not write “sirolimus binds FKBP4” as a new fact.
Wet-lab remains the arbiter (T7).

---

## 8. Human blocker (only one)

**Approve a compute budget** (suggested: $10–25, one RTX 4090, P2-A as
specified). Until that happens:

- Do not open a RunPod (or any GPU cloud) session for Phase 2.
- Do not put payment methods, tokens, or hostnames in this repo.
- Knight-owned GPU is allowed without a dollar approval.

No other human input is required to *start* P2-A. P2-B (membrane) and
P2-C (peptide) need a second, explicit go-ahead after P2-A is read.

---

## 9. Launch recipe (after approval only)

1. Start **one** RTX 4090 pod, ≥40 GB disk, Ubuntu + NVIDIA driver.
2. Clone `wckdboy/openendo` (this branch or `main` once merged).
3. `conda create -n phase2 -c conda-forge python=3.11 openmm openff-toolkit openmmforcefields pdbfixer mdtraj numpy && conda activate phase2`
4. `python3 scripts/phase2_prep.py --check`
5. `python3 scripts/phase2_run_openmm.py --dry-run` — must report
   `inputs_missing: []`.
6. Control first:

   ```bash
   python3 scripts/phase2_run_openmm.py \
     --system p2a_fkbp12_crystal --ns 100 \
     --outdir /workspace/phase2-runs \
     --i-understand-this-spends-gpu-budget
   ```

7. At ~20 ns, inspect ligand COM. If unbound → terminate pod, file a
   methods note, spend $0 more.
8. If bound:

   ```bash
   python3 scripts/phase2_run_openmm.py \
     --system p2a_fkbp52_vina --ns 100 \
     --outdir /workspace/phase2-runs \
     --i-understand-this-spends-gpu-budget
   ```

9. Copy `*.dcd *.log *_final.pdb` off the pod (do **not** commit
   multi-GB trajectories to git; park on the owned Hetzner box or a
   release asset). Terminate the pod the same hour.
10. Write `docs/research/virtual/phase2/phase2.md` + `phase2.json` with
    RMSD/contact tables, confidence, and the M3 non-change (or the
    narrow side-claim downgrade in outcome C). That report is what
    marks Phase 2 **done**.

---

## 10. Uncertainty (do not paper over)

- Alignment is 11 pairs / 1.00 Å, not the unpublished 14-pair / 0.80 Å
  VPS superposition. Same pocket; not bit-identical.
- 1N1A is apo FK1 only, with a 4-residue gap. Apo sidechains were already
  a Phase 1 limitation.
- OpenFF parameterization of a 914 Da macrolide can fail or need
  `allow_undefined_stereo=True`. If `from_pdb_and_smiles` fails, stop —
  do not guess bonds on a paid GPU.
- 100 ns will not sample rapamycin ring flips; it tests **local pose
  stability**, which is exactly the Phase 1 deferral.
- ns/day and therefore dollars are ±2×. The kill switch exists so a
  slow or failing job cannot silently consume $25.
- RunPod list prices move. Re-check the console before launch.

*Galahad, 2026-09-12. Research infrastructure, not medical advice. No PII.
No cloud GPU spend in this PR.*
