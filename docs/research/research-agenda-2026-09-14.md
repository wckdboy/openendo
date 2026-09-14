# OpenEndo research agenda memo — 2026-09-14

> One-pager for DrDoc / human review. Corpus at `/workspace/openendo` @ `67db0b7`.
> Drafts only under `/workspace/openendo-drafts/` — **no git commit/push** this pass.
> Not medical advice.

## Top-3 lead status (after registry + literature refresh)

| # | Lead | Verdict | Δ since digest-2026-09-11 / registry-2026-09-03 |
|---|---|---|---|
| 1 | **Sirolimus / mTOR** (+ separate FKBP4/PR-resistance note) | **TOP TIER** | Registry still **0** endo trials (sirolimus/rapamycin/everolimus/temsirolimus/mTOR). New pathway papers (S1PR4→mTOR PMID 40532686; PI3K–AKT–mTOR SNPs PMID 40200774) reinforce biology, not clinical readiness. |
| 2 | **MRGPRX2 antagonism** *(not cetrorelix-as-drug)* | **VALIDATED AXIS** | Still **0** MRGPRX2-named endo trials; cetrorelix still 2 NCTs. Histamine landscape (PMID 41516088) + mast/JAK–STAT review (PMID 40948761) support the pain frame. Antagonist chemistry remains the gap. |
| 3 | **Sulfasalazine / xCT ferroptosis** | **WATCHLIST** | Still **0** trials. FIN56 (PMID 42698143) adds induction confirmation. EA papers claiming ferroptosis *suppression* (PMIDs 42081613, 42155249) flagged as **compartment contested** — do not upgrade or invert the lesion-cell induction lean without review. |

## Priorities (next tractable increments — no GPU / no OpenAI key required)

1. **Human-review merge path for drafts** — `registry-verification-2026-09-14.md`, `literature-packet-2026-09-14.md`, and `knowledge-updates/{sirolimus,mrgprx2-pain,ferroptosis}.md`. SCHEMA-compatible; uncertainty flagged; live PMIDs only.
2. **Ferroptosis contested note** — short append to `ferroptosis-direction.md` documenting EA/Nrf2–GPX4 “suppress ferroptosis” claims vs induction literature; keep MEDIUM confidence + `contested` until reconciled.
3. **MRGPRX2 antagonist landscape (literature-only)** — catalogue published MRGPRX2 antagonists from *non-endo* indications (urticaria / AD / itch) as *chemical starting points*, clearly labelled off-indication; no docking until GPU or CPU peptide workflow is defined.
4. **FKBP4 note hygiene** — keep PR-resistance chaperone thread visually separate from sirolimus TOP TIER on wiki/index so readers never read “sirolimus restores FKBP4.”
5. **Weekly evidence cadence without OpenAI** — continue PubMed E-utilities + Europe PMC + CT.gov API v2 (this packet proves the stack works on the box). Optional: thin local summarisation scripts; do **not** invent LLM-dependent steps.
6. **Danish / access threads (parallel, not lead-blocking)** — T7 Phase B interviews remain a human step; digest carry-overs (relugolix-CT PMID 42719373; IL16 pain signature PMID 42720599) for next M2 ingest.

## Blockers

| Blocker | Blocks | Workaround used this pass |
|---|---|---|
| **No GPU** | Phase 2 OpenMM (P2-A FKBP12 RAP control → FKBP52 pose; later xCT membrane; cetrorelix–MRGPRX2 peptide) | Literature/registry/knowledge drafts only; Phase 1.0 docking already done ($0 CPU) |
| **No OpenAI API key** | Any LLM-assisted abstract triage / embedding search the pipeline might assume | Direct E-utilities + Europe PMC + deterministic filtering by keyword/PMID |
| **Human budget approval** | Paid GPU cloud for Phase 2 (~$5–18 community / ~$10–18 secure per CHECKPOINT for first P2-A job) | Do not invent spend; leave job package ready in-repo |
| **Human review bar** | Patient-facing knowledge merges (AGENTS.md) | Drafts staged under `openendo-drafts/` for DrDoc |

## Next experiments (ordered by “can run without GPU/OpenAI”)

1. **Done this pass:** CT.gov API v2 re-query; PubMed/Europe PMC spot-check; draft packets.
2. **CPU-only follow-ups:**
   - Diff `repurposing_candidates.json` status text vs this packet (wording only; no status upgrade without review).
   - Optional ChEMBL refresh for MRGPRX2 antagonist chemotypes (public API) → table in drafts.
   - Optional FerrDb / GEO gene-set overlap for PMID 42728524 biomarker list vs OpenEndo SLC7A11/GPX4/ACSL4 set (scripted, no LLM).
3. **When GPU budget clears:** run **P2-A** exactly as `docs/research/virtual/phase2/phase2-plan.md` (100 ns FKBP12 + crystal RAP, then 100 ns FKBP52 Vina pose). Defer xCT membrane + cetrorelix peptide to second wave.
4. **Do not do:** push/commit into `/workspace/openendo` from this draft pass; fabricate citations; promote cetrorelix as the MRGPRX2 lead; move sulfasalazine off WATCHLIST based on bioinformatics alone.

## Deliverable index (this pass)

| Path | Content |
|---|---|
| `/workspace/openendo-drafts/registry-verification-2026-09-14.md` | CT.gov API v2 re-verification |
| `/workspace/openendo-drafts/literature-packet-2026-09-14.md` | What changed since digest-2026-09-11 |
| `/workspace/openendo-drafts/knowledge-updates/sirolimus.md` | SCHEMA draft entity update |
| `/workspace/openendo-drafts/knowledge-updates/mrgprx2-pain.md` | SCHEMA draft concept update |
| `/workspace/openendo-drafts/knowledge-updates/ferroptosis.md` | SCHEMA draft concept update (`contested: true`) |
| `/workspace/openendo-drafts/research-agenda-2026-09-14.md` | This memo |
| `/workspace/openendo-drafts/_ctgov_raw_2026-09-14.json` | Raw registry JSON |
| `/workspace/openendo-drafts/_pubmed_raw_2026-09-14.json` | Raw PubMed JSON |
| `/workspace/openendo-drafts/_pubmed_filtered_2026-09-14.json` | Filtered endo+lead subset |
| `/workspace/openendo-drafts/_epmc_spotcheck_2026-09-14.json` | Europe PMC corroboration |

---

*Galahad executor draft, 2026-09-14. Research infrastructure — not clinical guidance.*
