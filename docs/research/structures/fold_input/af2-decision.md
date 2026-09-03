# AlphaFold run decision — corrected coverage audit (2026-09-03)

**Owner:** Jaeger (night shift) · **Status:** DECIDED — **0 of 35 targets need
folding**. The "8 to fold (~$1–3)" figure from Phase 0 was an audit artifact:
a UniProt-accession parsing bug marked 7 covered targets as missing, and the 1
genuine AFDB gap (GPX4) already has experimental PDB structures. Phase 1
docking is structurally unblocked with no ColabFold/AlphaFold run required.

Supersedes: `phase0.md` Result 1 + `phase0.json` `afdb` section (stale —
regenerate with the fixed script). Companion: `README.md` (fold input pack),
`docs/research/virtual-testing.md` (pipeline plan), `virtual/phase0.md`.

## Decision summary

| Question | Answer |
|---|---|
| How many M1 targets need a *de novo* AlphaFold/ColabFold run? | **0** (was: 8) |
| Cost of the folding leg | **$0** (was: est. $1–3) |
| Folding run launched? | **Not needed — vacated.** All 35 targets have structure coverage today |
| Phase 1 docking prerequisite | None — proceed straight to Vina/docking with experimental PDBs |
| Bulk structure download into repo | **Explicitly deferred** (repo-size call, see below) |

## Corrected coverage table (live AFDB API + RCSB, 2026-09-03)

Method: for each of the 35 fold-input genes, UniProt accession taken from the
FASTA header (`sp|ACC|...`), queried against
`https://alphafold.ebi.ac.uk/api/prediction/<ACC>`; canonical isoform-1
full-length model required for "FULL". GPX4 cross-checked against RCSB
(UniProt-accession exact match). All AFDB models are v6, created 2025-08-01.
Model URL pattern: `https://alphafold.ebi.ac.uk/files/<model_file>`.

**34/35 in AlphaFold DB (full-length canonical):**

| Gene | UniProt | AFDB model file | Gene | UniProt | AFDB model file |
|---|---|---|---|---|---|
| ABCC4 | O15439 | AF-O15439-F1-model_v6.pdb | MRGPRX2 | Q96LB1 | AF-Q96LB1-F1-model_v6.pdb |
| ACKR3 | P25106 | AF-P25106-F1-model_v6.pdb | NGFR | P08138 | AF-P08138-F1-model_v6.pdb |
| ACVR1B | P36896 | AF-P36896-F1-model_v6.pdb | PDK3 | Q15120 | AF-Q15120-F1-model_v6.pdb |
| AOC3 | Q16853 | AF-Q16853-F1-model_v6.pdb | PFKFB3 | Q16875 | AF-Q16875-F1-model_v6.pdb |
| CCR6 | O00421 | AF-O00421-F1-model_v6.pdb | PLAUR | Q03405 | AF-Q03405-F1-model_v6.pdb |
| CCR8 | P51685 | AF-P51685-F1-model_v6.pdb | S1PR2 | O95136 | AF-O95136-F1-model_v6.pdb |
| CMKLR1 | Q99788 | AF-Q99788-F1-model_v6.pdb | S1PR3 | Q99500 | AF-Q99500-F1-model_v6.pdb |
| CX3CR1 | P49238 | AF-P49238-F1-model_v6.pdb | SLC7A11 | Q9UPY5 | AF-Q9UPY5-F1-model_v6.pdb |
| ENTPD1 | P49961 | AF-P49961-F1-model_v6.pdb | SLCO2A1 | Q92959 | AF-Q92959-F1-model_v6.pdb |
| ENTPD2 | Q9Y5L3 | AF-Q9Y5L3-F1-model_v6.pdb | SPHK1 | Q9NYA1 | AF-Q9NYA1-F1-model_v6.pdb |
| F2RL1 | P55085 | AF-P55085-F1-model_v6.pdb | SUCNR1 | Q9BXA5 | AF-Q9BXA5-F1-model_v6.pdb |
| FKBP4 | Q02790 | AF-Q02790-F1-model_v6.pdb | TPSAB1 | Q15661 | AF-Q15661-F1-model_v6.pdb |
| FPR1 | P21462 | AF-P21462-F1-model_v6.pdb | TRPM3 | Q9HCF6 | AF-Q9HCF6-F1-model_v6.pdb |
| FPR2 | P25090 | AF-P25090-F1-model_v6.pdb | YAP1 | P46937 | AF-P46937-F1-model_v6.pdb |
| GPER1 | Q99527 | AF-Q99527-F1-model_v6.pdb | HPGD | P15428 | AF-P15428-F1-model_v6.pdb |
| HTRA1 | Q92743 | AF-Q92743-F1-model_v6.pdb | ILK | Q13418 | AF-Q13418-F1-model_v6.pdb |
| KLRK1 | P26718 | AF-P26718-F1-model_v6.pdb | METTL3 | Q86U44 | AF-Q86U44-F1-model_v6.pdb |

**1/35 not in AFDB — but experimentally solved:**

| Gene | UniProt | AFDB | Experimental PDB (RCSB UniProt mapping) | Coverage |
|---|---|---|---|---|
| GPX4 | P36969 | **absent** (404 on all AFDB endpoints, v3–v6) | **23 PDB entries** (2GS3, 2OBI, 5H5Q–S, 6ELW, 6HKQ, 6HN3, 7L8K–R, 7U4I–N, 8Q8J/N, 9J6L, 9RF1) | Solved — no fold needed |

Note on TRPM3: 11 AFDB entries exist; the canonical isoform-1 model
(AF-Q9HCF6-F1, 1–1732) is complete. YAP1 has 9 entries (isoforms).

## Root cause of the Phase 0 undercount

`scripts/phase0_structure_expression.py` → `fasta_targets()` validated
accessions with `part[1:].isdigit()`, which rejects every UniProt accession
with letters in the middle segment (`[A-Z0-9]{3}`), e.g. Q9**Y**5L3,
Q9**U**PY5, Q9**H**CF6, Q96**LB**1. 7 genes therefore got an empty accession,
the AFDB query 404'd and they were flagged "missing". GPX4 (P36969, all
digits) parsed correctly and is *genuinely* absent from AFDB — but RCSB holds
23 experimental entries for P36969, so even GPX4 needs no fold. **The parser
bug is fixed** (canonical pattern `[OPQ][0-9][A-Z0-9]{3}[0-9]`; dry-run: 35/35
accessions parsed, 0 blank). `phase0.json`/`phase0.md` are stale until the
script is re-run — JSON deliberately left untouched this shift (schema stable;
re-run is a 1-command daytime follow-up).

## Cost sheet

| Leg | Previous estimate | Corrected | Notes |
|---|---|---|---|
| Fold 8 missing M1 targets (ColabFold, 4090) | $1–3 | **$0 — 0 targets to fold** | 34 in AFDB (free download), GPX4 in PDB |
| AlphaFold Server free tier (optional re-fold of GPX4 for pipeline consistency) | — | $0 | alphafoldserver.com, academic free, ~1–5 min, browser/Google login (human step) |
| Bulk fetch of 34 AFDB models + GPX4 PDB into repo | — | $0 (≈50 MB) | Deferred — repo-size decision (see below) |
| Phase 1 docking (Vina: sirolimus→FKBP4 + FKBP12 control, cetrorelix→MRGPRX2 7S8L, sulfasalazin→xCT 7CCS) | $10–25 | $10–25 (unchanged) | Now has **no folding prerequisite** |
| Phase 1 ADMET-AI/RDKit profile (9 M3 candidates) | included | included | CPU, Netcup VPS |

## Decision and rationale

1. **Folding run: NOT launched — vacated as unnecessary.** Launching a paid
   ColabFold run for structures that already exist (free) would waste budget
   and duplicate public data. Evidence: live API audit above (34/35 AFDB v6
   full-length; GPX4 23 experimental PDB entries).
2. **Bulk structure download into the repo: explicitly deferred.** ~50 MB of
   third-party PDB files on `main` is a repo-hygiene call for daytime Jaeger
   (git size, raw.githubusercontent serving, CI artifact caching). Recommended
   pattern: fetch-on-demand into a gitignored cache dir
   (`docs/research/structures/cache/` or `$XDG_CACHE`) at the start of the
   Phase 1 docking script, keyed by the table above; commit only *analysis
   outputs* (scores, poses, summary.json), not raw models.
3. **Next action: Phase 1 docking proceeds directly** on experimental
   structures (FKBP4/FKBP12/MRGPRX2 7S8L/SLC7A11 7CCS — all docking-ready per
   Phase 0 Result 2) plus AFDB models where a second opinion is wanted. The
   virtual-testing ladder's Tier-1 "predict missing structures" step is closed
   for the M1 set; Tier 1 remains available for future novel targets.

## Follow-ups

- [ ] Re-run `python3 scripts/phase0_structure_expression.py` (daytime Jaeger)
      to regenerate `phase0.json` with corrected AFDB coverage (34/35 + GPX4
      note). JSON untouched this shift.
- [ ] `manifest.json` "uniprot" fields are blank repo-wide (separate cosmetic
      gap in `prepare_fold_input.py`); fill from FASTA headers on next regen.
- [ ] Decide repo structure-fetch pattern (fetch-on-demand vs committed cache)
      before Phase 1 docking starts.

*Jaeger (Hermes Agent, night shift), 2026-09-03. Live public APIs only (AFDB,
RCSB); no PII. Research infrastructure, not medical advice.*
