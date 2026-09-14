# M3 registry verification — ClinicalTrials.gov (2026-09-14)

> Purpose: re-verify the M3 shortlist's novelty/clinical-usage claims against
> the trial registry itself (live query, 2026-09-14). Companion to
> `docs/research/evidence/registry-verification-2026-09-03.md`.
>
> **Method:** ClinicalTrials.gov API v2,
> `query.cond=endometriosis` AND `query.intr=<drug|term>`, `pageSize=100`,
> fields subset (`NCTId,BriefTitle,OverallStatus,Phase,InterventionName,StudyType`).
> Counted returned studies (`totalCount` matched returned length for all queries).
> **Sanity control:** dienogest (established endo drug) → **40** hits (same as
> 2026-09-03) — method still valid.
>
> Raw JSON: `/workspace/openendo-drafts/_ctgov_raw_2026-09-14.json`
> Queried at: 2026-09-14T13:48:13Z (UTC).

## Results (endometriosis + intervention)

| Drug / term (M3-relevant) | Endo trials on CT.gov | Δ vs 2026-09-03 | Reading |
|---|---|---|---|
| **Sirolimus** | **0** | unchanged | novelty claim confirmed — no registered endo trial |
| Rapamycin | 0 | unchanged | same molecule, confirms |
| mTOR (keyword) | 0 | *new this pass* | no mTOR-inhibitor endo trial under this intr query |
| Everolimus | 0 | *new this pass* | rapalog class also empty |
| Temsirolimus | 0 | *new this pass* | rapalog class also empty |
| **Sulfasalazine** | **0** | unchanged | novelty confirmed; WATCHLIST stands on selectivity, not absence of data |
| **MRGPRX2** | **0** | *new this pass* | no registered antagonist / target-named endo trial |
| Ferroptosis / erastin | 0 / 0 | *new this pass* | no interventional ferroptosis-inducer endo trial |
| **Cetrorelix** | **2** (NCT04071574, NCT00244452) | unchanged | confirms "already used in endometriosis" — VALIDATED-AXIS reading of the MRGPRX2 hit (drug ≠ novel; target antagonism is) |
| Dienogest (control) | 40 | unchanged | method validated |

### Cetrorelix hit detail (unchanged set)

| NCT | Status | Type / phase | Note |
|---|---|---|---|
| [NCT00244452](https://clinicaltrials.gov/study/NCT00244452) | COMPLETED | INTERVENTIONAL / PHASE2 | Cetrorelix SR single-administration endometriosis efficacy/safety (histologically confirmed) — primary endo indication study |
| [NCT04071574](https://clinicaltrials.gov/study/NCT04071574) | COMPLETED | INTERVENTIONAL / PHASE1–2 | ICSI ovarian-stimulation protocol comparison; lists GnRH antagonist among interventions (not an endo-disease efficacy trial) |

## Endometrioma condition cross-check

Same API, `query.cond=endometrioma` + `query.intr` for sirolimus, rapamycin, sulfasalazine, cetrorelix → **0 / 0 / 0 / 0**. No endometrioma-specific interventional signal for the M3 leads.

## Implications for the shortlist (`m3-validation.md`)

1. **Sirolimus (TOP TIER):** novelty **unchanged and still strong** — zero registered endometriosis or endometrioma trials for sirolimus/rapamycin/everolimus/temsirolimus/mTOR as intervention, despite independent mechanistic/animal (+ one retrospective IVF) evidence. Cleanest repurposing novelty case on the board remains open.
2. **MRGPRX2 antagonism (not cetrorelix-as-drug):** still **no** MRGPRX2-named endo trial. Cetrorelix remains the only related registry presence (2 hits), reinforcing that the *drug* is established/used and the *antagonist-target* path is the novel element.
3. **Sulfasalazine / xCT ferroptosis (WATCHLIST):** still **no** trial data either way — consistent with the ferroptosis-direction verdict (selectivity/toxicity is the open question, not missing registry entries).
4. Caveat (same as 2026-09-03): CT.gov only — EU CTIS / older national registries / investigator-initiated unregistered use may differ; cross-registry check out of scope for this pass.

## What did *not* change

No new interventional registration appeared between 2026-09-03 and 2026-09-14 for any top-3 lead. Registry packet does not move any M3 verdict.

---

*Verification draft for DrDoc / human review. Live registry data via ClinicalTrials.gov API v2.
Research infrastructure context — not clinical guidance. Do not merge without review.*
