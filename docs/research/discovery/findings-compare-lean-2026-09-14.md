# Findings compare: lean 0.1.2 vs prior live (2026-09-14)

**Do not push to GitHub.** Local compare only.

## Runs

| | Prior | Lean |
|---|---|---|
| Path | `/workspace/findings-live/2026-09-14/` | `/workspace/findings-live-lean/2026-09-14/` |
| Engine | 0.1.1 | **0.1.2** (`f75e87c` Lean Stage 4) |
| Model | deepseek-flash | deepseek-flash |
| Base URL | (same family) | `https://api.deepseek.com` |
| Source | local `/workspace/openendo` | local `/workspace/openendo` |
| Tracing | (prior run) | `--no-tracing` |
| Generated | 2026-09-14T14:00:39Z | 2026-09-14T14:15:15Z |

## Counts by category

| Category | Prior (0.1.1) | Lean (0.1.2) |
|---|---:|---:|
| research_gap | 13 | 5 |
| conflict | 8 | 3 |
| repurposing_lead | 9 | 9 |
| hypothesis | 19 | 7 |
| **Total** | **49** | **24** |
| dropped | 0 | 0 |
| warnings | 0 | 0 |

Lean is ~half the volume: fewer gaps/conflicts/hypotheses; same repurposing_lead count. Classification mix shifted away from untested-hypothesis flood (prior 33 → lean 8); documented-evidence and likely-association stayed at 8 each.

## Sirolimus / CHEMBL413

| | Prior | Lean |
|---|---|---|
| Named? | Mostly **CHEMBL413** (drug name missing) | **Sirolimus (rapamycin)** named correctly |
| Framing | REPU-0004: “wrong-direction risk” on FKBP4/PR | REPU-0001: **top-tier** lead; chronic-use safety flagged, **not** wrong-direction |
| Thesis | Ambiguous FKBP52 modulation / possible PR impairment | M3 top-tier via potency + independent **mTOR** endometriosis evidence; FKBP4 engagement treated as plausible but unproven |
| Related | Research gap on unnamed CHEMBL hits | Conflict CONF-0002 on FKBP4 promiscuity vs PR-chaperone; HYPO-0001 tests FKBP52 vs mTORC1 mediation |

**Verdict:** Lean 0.1.2 fixes the P0 naming / wrong-direction mislabel for CHEMBL413 → sirolimus aligns with shortlist K3 (“Sirolimus is TOP TIER via mTOR; the FKBP4 hit is not the drug thesis”).

## Overlap with prior shortlist themes

Aligned with `/workspace/openendo-drafts/findings-shortlist-2026-09-14.md` KEEP themes:

- **K1/K3/K9-ish:** MRGPRX2 / mast-cell proteases (TPSAB1, CMA1) as gaps; cetrorelix agonism conflict
- **K2:** SLC7A11 / GPX4 ferroptosis + sulfasalazine watchlist
- **K3:** Sirolimus top-tier (named), not wrong-direction
- **K4:** ACVR1B / activin → crizotinib & dabrafenib watchlist, poor drug-fit
- **K5:** Fibrosis mechanotransduction (YAP1 / ILK) hypothesis
- **K7:** Prostaglandin axis (SLCO2A1 / HPGD / PTGER4 / PTGFR); wrong-direction dinoprostone / estradiol correctly tagged target-validating only
- **K8:** Recruiting portfolio vs mechanism-annotated targets gap

Lean also surfaces ZEB1/EMT and symptomatic vs asymptomatic pain-split gaps. Prior-only noise themes (IL-6 flood, statin, CCR sprawl) largely absent — consistent with lean compaction.

## Token / stage behavior

- Architecture (0.1.2): **one LLM call** → four category reports (`run_all_stages` / `discovery_all_stages`); no per-category stage fan-out.
- `findings.json` meta: **no token/usage/cost fields** logged (neither prior nor lean).
- Wall time this lean live run: ~66s end-to-end; dropped=0; warnings=0.
- Tracing disabled (`--no-tracing`); LangSmith key unset → WARN only.

## Paths

- Lean findings: `/workspace/findings-live-lean/2026-09-14/findings.json`
- Lean report: `/workspace/findings-live-lean/2026-09-14/report.md`
- Prior: `/workspace/findings-live/2026-09-14/{findings.json,report.md}`
- This note: `/workspace/openendo-drafts/findings-compare-lean-2026-09-14.md`

## TLDR

Lean **0.1.2** live run produced **24** findings (vs 49 prior), correctly **names sirolimus** and ranks it **top-tier / not wrong-direction**, and overlaps the shortlist KEEP axes (ferroptosis, MRGPRX2/mast cell, mTOR/sirolimus, activin watchlist, fibrosis YAP/ILK, prostaglandin). No GitHub push. No API keys printed.
