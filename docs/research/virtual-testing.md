# Virtual testing — computational validation pipeline

> How OpenEndo moves drug-target candidates (M1/M3) from literature hits to
> **computationally tested hypotheses** — structure, docking, dynamics, ML.
> Status: Phase 0 complete (2026-09-02). Machine data: `virtual/phase0.json`.

## Integrity rules (non-negotiable)

1. **Computational output = hypothesis, never a clinical conclusion.** Every
   artifact carries confidence + method + date. Nothing here is medical advice.
2. **Structures are models.** AlphaFold predictions get pLDDT; docking poses get
   scored + (for top hits) MD-validated. Experimental structures (PDB) outrank
   predictions when available.
3. **Controls matter.** Selectivity claims need a negative control (e.g.
   sirolimus→FKBP4 *and* sirolimus→FKBP12).
4. **Everything open + reproducible.** Scripts in `scripts/`, data in
   `virtual/`, regenerable, MIT.
5. **Wet-lab is the final arbiter.** A computational hit is a *reason* to test,
   not a result. (T7 lab contacts = future validation partners.)

## The validation ladder

| Tier | Question | Tools | Cost class |
|---|---|---|---|
| 0 | Does a structure exist? | AlphaFold DB (precomputed), PDB/RCSB (experimental) | free |
| 0.5 | Is the target expressed/relevant? | HPA, GTEx, OpenTargets; endo-omics (GEO/single-cell) | free |
| 1 | Predict missing structures | ColabFold (AF2), ESMFold, AlphaFold3 (heavy) | $ |
| 2 | Does the drug bind? | AutoDock Vina (CPU), DiffDock (GPU), Gnina | $ |
| 3 | Does the binding hold? | OpenMM / GROMACS MD (100–500 ns) | $$ |
| 4 | Properties & ML pre-screen | RDKit, ADMET-AI, Chemprop, DeepPurpose; ChEMBL API | free–$ |
| 5 | Broad virtual screen (later) | Vina/Gnina batch over ZINC subsets | $$$ |

## Candidate → tool map (current)

| Candidate | Target | Structure status (Phase 0) | Planned test |
|---|---|---|---|
| Sirolimus (rapamycin) | FKBP4 (Q02790) | AFDB ✅ + PDB 12 (1N1A…) | Vina docking FKBP4 **vs FKBP12 control** (PDB 115) → MD top pose |
| Cetrorelix | MRGPRX2 (Q96LB1) | AFDB ✅ + PDB 14 (7S8L cryo-EM) | peptide docking/peptide-MD against 7S8L; note mast-cell biology |
| Sulfasalazine | SLC7A11/xCT (Q9UPY5) | AFDB ✅ + PDB 4 (7CCS cryo-EM) | Vina docking; compare known xCT inhibitors |
| (watchlist) CsA/Tacro | FKBP4 | as FKBP4 | only if sirolimus path validates |
| (watchlist) TKIs | ACVR1B (P36896) | AFDB ✅ + PDB 2 (7MRZ) | skip — conclusion was *selective* inhibitor needed → Tier 5 later |
| (wrong direction) | GPER1, SLCO2A1 | structures exist (8XOF, 3MRR) | none — target-validating only |
| M1 35 targets | — | **27/35 in AFDB** → fold only 8 | ColabFold batch on RunPod |

## Infrastructure (prices live, RunPod community, 2026-09-02)

| Resource | Use | Price |
|---|---|---|
| RunPod RTX 4090 (24 GB) | ColabFold, DiffDock, OpenMM | $0.34/h (stock LOW) |
| RunPod A100 SXM 80 GB | heavy MD, AF3 | $1.39/h |
| RunPod H100 NVL | AlphaFold3 | $2.59/h |
| MacBook M3 Pro 36 GB | overnight local (ColabFold/OpenMM via Metal, Vina) | ~€0 |
| Netcup VPS | Vina (CPU), RDKit, ADMET, orchestration, APIs | owned |
| Hetzner BX41 20 TB | trajectories/artifacts (rclone) | owned |

Estimates: fold 8 targets ≈ $1–3 (4090) · docking 3 candidates + control ≈ <$1 CPU ·
MD 100–500 ns per complex ≈ $5–25 (4090). Phase 1 total ≈ **$10–25**.

## Phases

- **Phase 0 — coverage audit** ✅ 2026-09-02 (`virtual/phase0.json` + `phase0.md`):
  AFDB 27/35 · PDB experimental structures for all M3-relevant targets ·
  HPA expression summary · ChEMBL target registration.
- **Phase 1 — docking (~$10–25):** ColabFold for the 8 missing M1 targets ·
  Vina: sirolimus→FKBP4 + FKBP12 control, cetrorelix→MRGPRX2 (7S8L),
  sulfasalazine→xCT (7CCS) · ADMET-AI + RDKit profile of 9 M3 candidates.
  DoD: poses + scores + ADMET table in `virtual/phase1/`, top poses MD-ready.
- **Phase 2 — dynamics (~$50–150):** OpenMM 100–500 ns on top poses (RMSD/RMSF,
  binding stability); DiffDock cross-check; DeepPurpose/Chemprop DTI layer.
- **Phase 0.5/3 — expression + broad screen:** endo-lesion omics (GEO) for
  FKBP4/MRGPRX2/SLC7A11 · selective ACVR1B screen over ZINC (needs batch infra).

## Output conventions

- Machine data: `docs/research/virtual/phase{N}/…json` (+ scripts to regenerate)
- Human summary: `phase{N}.md` — verdict tables, confidence, caveats, next step
- All artifacts linked from `llms.txt`; CHECKPOINT tracks phase status
