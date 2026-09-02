# Phase 0 — structure & expression coverage audit

Checked 2026-09-02 by Jaeger. Machine data: `phase0.json` (regenerate:
`python3 scripts/phase0_structure_expression.py`). Sources: AlphaFold DB,
RCSB PDB, Human Protein Atlas, ChEMBL — all public APIs.

## Result 1 — AlphaFold DB coverage (M1's 35 targets)

**27/35 already have AF2 models** — only **8 need folding** (ColabFold, Phase 1).
Coverage details per gene in `phase0.json` → `afdb`.

## Result 2 — Experimental structures exist for every M3-relevant target

| Target | PDB entries (UniProt match) | Example |
|---|---|---|
| FKBP4 (sirolimus) | 12 | 1N1A, 1P5Q |
| FKBP12 — selectivity control | 115 | 1A7X (classic FKBP12–rapamycin) |
| MRGPRX2 (cetrorelix) | 14 | 7S8L (cryo-EM) |
| SLC7A11/xCT (sulfasalazine) | 4 | 7CCS (cryo-EM), 7EPZ |
| ACVR1B (TKI watchlist) | 2 | 7MRZ |
| GPER1 / SLCO2A1 (wrong-direction) | 6 / 8 | 8XOF (cryo-EM) / 3MRR |

→ **Docking-ready without any folding** for the M3 validation set. AlphaFold
prediction is only needed for the 8 uncovered M1 targets.

## Result 3 — HPA RNA tissue summary (key targets)

| Gene | RNA tissue specificity | Note |
|---|---|---|
| FKBP4 | Low tissue specificity | broad expression (consistent with co-chaperone role) |
| FKBP12 | Low tissue specificity | broad |
| **MRGPRX2** | **Not detected** | expected in bulk tissue — mast-cell receptor; mast cells are a tiny fraction of bulk RNA. Single-cell/mast-cell data is the right check (Phase 0.5). Not evidence against the M3 pain hypothesis. |
| SLC7A11 | Tissue enhanced | consistent with expression in barrier/secretory tissues |
| ACVR1B | Low tissue specificity | broad (kinase) |
| GPER1 | Tissue enhanced | |
| SLCO2A1 | Tissue enhanced | |

Caveat: HPA here = healthy adult tissue, not endometriosis lesions. The
disease-relevant question (elevated in lesions vs eutopic?) needs endo omics
(GEO / single-cell) — Phase 0.5.

## Result 4 — ChEMBL registration

All key targets present in ChEMBL (FKBP4 CHEMBL4050 · FKBP12 CHEMBL1902 ·
MRGPRX2 CHEMBL5849 · SLC7A11 CHEMBL1075149 · ACVR1B CHEMBL5310) — so known
actives/similarity machinery is available for Phase 1/4 screens. Sirolimus
(CHEMBL413) and cetrorelix (CHEMBL2103735) are registered molecules.

## Bottom line

- Phase 1 docking is **structurally unblocked** — experimental structures for
  all three testable candidates, controls included.
- Folding budget shrinks from 35 → **8 targets** (≈ $1–3 on a 4090).
- MRGPRX2 "not detected" is a bulk-tissue artifact of mast-cell biology, not a
  red flag — but it sharpens the Phase 0.5 question: is MRGPRX2 elevated in
  endo lesion mast cells specifically?

Next: Phase 1 (docking) at ~$10–25, or Phase 0.5 (endo-lesion expression via
GEO) first at ~$0.
