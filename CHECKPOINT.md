# OpenEndo — Agent Checkpoint

> **Living document. Agents: READ THIS FIRST before starting work.**
> Update it when you start, finish, or reprioritize a task. Humans: this is the
> single source of truth for "what's happening and what's next".
>
> Convention: every task has a status, an owner (Jaeger / Percival / anyone),
> and a last-updated date. When you finish something, move it to ✅ Done and
> add the next step. Never delete history — append to the change log.

**Last updated:** 2026-09-02 · **Maintainers:** Jaeger + Percival (Hermes agents)

---

## 🎯 Current focus (top 3)

1. **M3 repurposing validation → knowledge + GTEx** — 9/9 depth-checked (2026-09-02, `docs/research/evidence/m3-validation.md`): TOP TIER sirolimus; VALIDATED cetrorelix→MRGPRX2; WATCHLIST sulfasalazine/CsA/tacro/TKIs; estradiol+dinoprostone = wrong-direction (target-validating). Next per DoD: SCHEMA knowledge pages (sirolimus, MRGPRX2-pain) + GTEx expression cross-ref + llms.txt. *Owner: Percival*
2. **Lovable app ↔ repo content wiring decision** — plan-mode structural map of the Lovable app done (2026-09-02): trials/papers are fetched LIVE from ClinicalTrials.gov/PubMed via server functions; funding + knowledge articles are hard-coded in the app; repo research/knowledge content is NOT shown anywhere on the site. Decision: (a) port curated content into app content layer, or (b) app fetches repo raw URLs (repo stays canonical — Percival PR #11 recommendation). DoD: decision made + first content sync live on openendo.org. *Owner: Jaeger (propose) → human (decide)*
3. **M1 fold-input → AlphaFold run** — 35 novel targets packaged (`docs/research/structures/fold_input/`). Needs compute decision (RunPod serverless vs MacBook M3 Pro local vs Colab) + cost estimate. DoD: folding run launched, or explicit deferral with reason logged. *Owner: Jaeger (decide) / Percival (prepare)*

---

## 📊 Workstreams

| ID | Track | Status | Last touched | Owner |
|----|-------|--------|--------------|-------|
| M1 | Fold-input pack (35 novel targets, AlphaFold-ready) | ✅ merged · ⏭ run folding | 2026-09-02 | Percival |
| M2 | Living evidence synthesis (weekly digest) | ✅ merged · 🔄 weekly cadence | 2026-09-02 | Percival |
| M3 | Drug repurposing screen | ✅ merged · 🔬 validation next | 2026-09-02 | Percival |
| T7 | Lab software modernization (DK ELN) | ✅ merged · 📋 interviews next | 2026-09-02 | Percival |
| INT | RO-Crate integration contract | ✅ merged · 🔧 CI wiring next | 2026-09-02 | Percival |
| SITE | Perf fix + Target intelligence §06 | ✅ live | 2026-09-02 | Percival |
| WIKI | Knowledge base (9 pages, wiki.html, llms.txt) | 🟢 live — M2 ingest part 1 done; diversity/registry pages next | 2026-09-02 | Jaeger |
| DATA | Weekly refresh (trials, PubMed, funding) | 🔄 automated Mon 08:00 | 2026-09-02 | Jaeger (cron) |
| VIRT | Virtual testing pipeline (structure/docking/MD) | 🔄 Phase 0 ✅ — Phase 1 next | 2026-09-02 | Jaeger |

---

## 📋 Horizon — tasks needing focus

### 🔴 High priority

- [ ] **M3 candidate validation** — 9 candidates, depth-check each (mechanism fit in endometriosis biology, ChEMBL/PubMed evidence, safety, novelty vs current care). DoD: ranked shortlist (confidence-tagged) merged to `docs/research/evidence/` + wiki entity pages + llms.txt; CI green. *Percival — this week*
- [x] **Yselty (linzagolix) DK status — VERIFIED 2026-09-02** — no general reimbursement for endometriosis (fibroid-only clause; out-of-pocket or regional enkelttilskud); yselty.md + comparison page updated to `high`. *Jaeger*
- [ ] **Virtual testing Phase 1 — docking (~$10–25)** — ColabFold for 8 AFDB-missing M1 targets (4090) · Vina: sirolimus→FKBP4 + FKBP12-kontrol, cetrorelix→MRGPRX2 (7S8L), sulfasalazin→xCT (7CCS) · ADMET-AI/RDKit-profil af 9 M3-kandidater. DoD: poses+scores+ADMET i `docs/research/virtual/phase1/`, top-poses MD-ready. *Jaeger — plan i docs/research/virtual-testing.md; Phase 0 ✅ 2026-09-02*
- [ ] **Virtual testing Phase 0.5 — endo-lesion expression (~$0)** — GEO/single-cell: er FKBP4/MRGPRX2/SLC7A11 hævet i endo-læsioner (mastceller)? MRGPRX2 "not detected" i HPA-normalvæv gør dette spørgsmål skarpere. *Jaeger*
- [ ] **AlphaFold run decision** — 35 FASTA files ready; **27/35 findes allerede i AFDB → kun 8 skal foldes (~$1–3)**. Decide compute path (RunPod serverless vs MacBook M3 Pro local vs Google Colab). DoD: decision + cost sheet in `docs/research/structures/fold_input/`, then run or defer. *Jaeger (decide) / Percival (prepare)*
- [ ] **Access-finder segment (website)** — country/postcode input → up-to-date access to meds, centres/doctors, help. Data: `docs/data/access.json` (v1: DK full, GB/US/DE orgs). UI build in Lovable app (fetch model — pilot for top-3 #2). DoD: live segment on openendo.org, data verified + sourced, CI green. *Jaeger — in progress (data v1 done 2026-09-02; UI build next)*
- [ ] **Lovable ↔ repo content sync** — after top-3 #2 decision: implement (port or fetch), verify on live site. DoD: knowledge/funding from repo visible on openendo.org; PR notes `needs-lovable-sync` workflow. *Jaeger*

### 🟡 Medium priority

- [ ] **Wiki ingest of M2 digest (part 2)** — ferroptosis + computational-drug-repurposing pages live (part 1, 2026-09-02); still open: diversity-gap page, Danish-registries/registry-analytics page. *Jaeger*
- [x] **MY-ENDO trial (NCT06211231) page** — live; patient-relevant page with inclusion/exclusion summary from CT.gov. *Jaeger*
- [ ] **T7 ELN interviews** — interview guide (DK) exists; identify 2–3 Danish labs to interview; publish anonymized write-up. DoD: ≥2 anonymized interviews merged under `docs/research/` + findings folded into lab-software-modernization.md; CI green. *Percival*
- [ ] **RO-Crate CI wiring** — regenerate `ro-crate-metadata.jsonld` automatically in the weekly data refresh, not manually. DoD: ro-crate-metadata regenerated by `scripts/update_data.py` (or its own script) on every data change; diff-verified. *Percival or Jaeger*
- [ ] **Nationalt Center for Forskning i Kvinders Sundhed** — track consortium decision; is endometriosis a priority theme? *Jaeger (monitor)*

### 🟢 Lower priority / backlog

- [ ] Ziwig Endotest availability in DK (diagnostic access)
- [ ] More wiki languages (good first issue #1)
- [ ] Funding-leads good first issue (#2) — open to community
- [ ] llms.txt hygiene check after every merge (keep agent index current)
- [ ] Site i18n: add Spanish/French (content.json keys exist)

---

## 🚧 Blockers / open questions

- **GitHub delete_repo scope** — Jaeger's token cannot delete repos; manual action needed for `wckdboy/private-kb` (user: Settings → Danger Zone → Delete). *Waiting on human*
- **AlphaFold compute budget** — no decision yet; folding 35 proteins costs real money on RunPod.
- **Percival profile state** — ✅ RESOLVED 2026-09-02: user confirmed ongoing research work ("Great continue", "Keep working, solve this"). Percival keeps producing research + data + repo maintenance; checkpoint ownership confirmed. Re-confirmed 2026-09-02: user will have Percival attack the laid-out problems (top-3 #1 M3 validation first).
- **Lovable app content wiring** — open decision (top-3 #2): repo knowledge/funding content is not shown in the Lovable app. Proposals from either agent welcome; human decides. Until decided, treat repo as canonical and flag `needs-lovable-sync` on affected PRs.

---

## ✅ Recently done (change log)

- **2026-09-02** — Virtual testing pipeline started (Jaeger): `docs/research/virtual-testing.md` (validation ladder: AFDB/PDB → docking → MD → ML; infra med live RunPod-priser; faser 0–3). **Phase 0 audit done**: AFDB dækker 27/35 M1-targets (kun 8 skal foldes, ~$1–3); eksperimentelle PDB-strukturer findes for ALLE M3-mål (FKBP4/FKBP12/MRGPRX2 7S8L/xCT 7CCS/ACVR1B); HPA-ekspression (MRGPRX2 "not detected" i bulk = mastcelle-artefakt → Phase 0.5); ChEMBL-registrering bekræftet. Script `scripts/phase0_structure_expression.py`, data `docs/research/virtual/phase0.json` + `phase0.md`.

- **2026-09-02** — Repo hardened for agentic work (Jaeger): AGENTS.md v2 — mission + two-agent protocol (claim-first workflow, branch naming `<agent>/<topic>`, file zones, merge discipline, definition of done). CHECKPOINT top-3 + 🔴/🟡 tasks now carry explicit DoD; new blocker: Lovable content wiring decision. Attribution fix: the Lovable app at openendo.org was built by the **user** in Lovable (not by Jaeger) — Hermes connects via Lovable API (OAuth). Merged PR #11 (deployment reality — repo = canonical data layer).
- **2026-09-02** — Deployment reality documented (Percival): live site openendo.org is a **Lovable app** (user's; built in Lovable); GitHub Pages is CNAME-redirected and serves nothing; repo content is only reachable via raw.githubusercontent.com. Fixed README (live-site + what's-inside + agent-discovery), AGENTS.md (rule 5 + quick reference), docs/llms.txt (all links now absolute raw URLs; stale targets path corrected). ⚠️ Open for Jaeger: if the Lovable app should serve data/wiki, wire it to fetch from the repo raw URLs — currently openendo.org/data/* 404s.
- **2026-09-02** — Site hardening (Jaeger): Playwright audit (7 pages × 3 viewports: overflow, touch-targets AA/AAA, a11y DOM, console/JS errors, mobile-nav + EN/DA toggle) runs as CI on every push (`.github/workflows/site-audit.yml`, screenshots uploaded). SEO: canonical + OpenGraph + Twitter cards on all 7 pages, JSON-LD (WebSite + Dataset) on index, robots.txt + sitemap.xml, brand OG image `assets/og-card.png` (generator: `scripts/gen_og_card.py`).
- **2026-09-02** — Wiki growth (Jaeger): Yselty DK status verified from EMA SmPC + Lægemiddelstyrelsen → page to `high` (no general reimbursement for endometriosis; fibroid-only clause). New pages: MY-ENDO trial, ferroptosis, computational-drug-repurposing. ryeqo-vs-yselty corrected (endo dose = 200 mg + ABT). wiki.html hub + llms.txt + index updated (9 pages).
- **2026-09-02** — Merged PRs #8 (M2 evidence + M3 screen), #9 (RO-Crate contract), #10 (perf fix + target intel §06). All checks green after CI self-scan bug fix.
- **2026-09-02** — Fixed CI: PII-scan was matching its own workflow file (`.github/` now excluded from grep).
- **2026-09-02** — Wiki published for humans (wiki.html) + agents (raw markdown via raw.githubusercontent.com); discovered GitHub Pages does not serve `.md`.
- **2026-09-02** — KB initialized: SCHEMA, index, log, 6 seed pages (ryeqo, yselty, hmi-115, gnrh-antagonists, saliva-diagnostics, ryeqo-vs-yselty).
- **2026-09-02** — Merged PR #5 (M1 fold-input pack) + PR #7 (T7 lab software track); preserved target-audit data from closed PR #3.
- **2026-08-28** — Site live at openendo.org (GitHub Pages); weekly data pipeline running.

---

*How to update: edit the relevant section, bump the date, append to the change log. Commit with a clear message. Agents: pull before reading, push after updating.*
