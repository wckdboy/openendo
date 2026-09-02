# AGENTS.md — OpenEndo

This file is auto-read by AI agent tooling (Codex, Claude Code, Hermes, Percival, etc.) when working in this repository.

## Mission

OpenEndo exists to make endometriosis research **open, live and actionable**:
a public-good infrastructure of clean data, living evidence and computational
leads (drug targets, repurposing candidates) that patients, clinicians and
researchers can build on — and that can genuinely accelerate medical
development for a disease that affects ~190M people but is underfunded and
under-researched.

**Operating principles for agents:**
- **Patients first, evidence first.** No hype, no speculation. Every claim traces to a source; unverified = `confidence: low`.
- **Public good, MIT.** Everything here is public. No PII, ever.
- **Tractable increments.** Each merged PR is one real step. Prefer small verifiable progress over grand plans.
- **Repo = canonical data & knowledge layer.** The UI (openendo.org) is a separate Lovable app; this repo is the source of truth for data, research and knowledge. Never let the repo drift from what the app should show — wire the app to the repo, not the other way around.

## First step: read the checkpoint

**Read `CHECKPOINT.md` before starting any work.** It is the living source of truth for current focus (top 3), the prioritized horizon, blockers and the change log. `docs/llms.txt` is the machine-readable index of everything else.

## Two-agent operating protocol (Jaeger + Percival)

1. **Claim before you build** — when you start a task, set `owner` + status in CHECKPOINT.md and commit that FIRST (same push as your first work commit). Never start work that another agent has claimed (`in_progress`).
2. **Branch naming** — `<your-name>/<topic>`, e.g. `percival/m3-validation`, `jaeger/wiki-diversity`. One task per branch/PR. Never push to `main` directly.
3. **File zones** (avoid stepping on each other):
   - `docs/research/` M1/M2/M3/T7 tracks → **Percival's zone** (Jaeger: review only)
   - `docs/knowledge/`, `docs/data/` curated files (`funding.json`, `targets.json`, `repurposing_candidates.json`) → **shared, one agent at a time** — claim in CHECKPOINT first; knowledge pages follow SCHEMA.md
   - `scripts/` (pipeline, audit, CI), `.github/` → **Jaeger's zone** (Percival: propose via issue/PR, don't rewrite)
   - `CHECKPOINT.md`, `AGENTS.md`, `llms.txt`, `README.md` → **shared coordination docs** — edit carefully, append to change log, never delete history
4. **Pull before push, always** — rebase on `origin/main`. The weekly monitor and data pipeline also commit here.
5. **PRs** — title `feat|fix|docs(scope): summary`. Update CHECKPOINT.md in the SAME PR (status, change log). CI must be green (security-scan + site-audit).
6. **Merge discipline** — the *other* agent (or the human) reviews and merges. Docs-only PRs with green CI may be merged after review; never merge your own PR without a second set of eyes unless the human says otherwise. If a check fails: investigate, fix, re-run — never merge past a red check.
7. **Lovable app** — the UI at openendo.org is the user's Lovable app (Hermes has API access via OAuth). Repo changes do NOT auto-deploy there. If a change affects what the app shows, flag `needs-lovable-sync` in the PR body.

## Rules for agents

1. **Check first** — CHECKPOINT.md + `git pull` before starting. Don't redo finished work.
2. **Update as you go** — start/finish/reprioritize → update CHECKPOINT.md (status, date, change log), commit in the same push.
3. **Never merge a PR with a failing check** — CI (security-scan: gitleaks + PII; site-audit) must be green.
4. **Wiki content bar** — knowledge pages need real sources + `confidence` field (see `docs/knowledge/SCHEMA.md`).
5. **Repo content is NOT on openendo.org** — the site is a Lovable app; GitHub Pages is CNAME-redirected. Agent-facing links to markdown AND data JSON must use `https://raw.githubusercontent.com/wckdboy/openendo/main/...` URLs, never `openendo.org/...` paths (404).
6. **No PII in this public repo** — never commit names, emails, or credentials (CI scans and blocks).
7. **Definition of done** — a task is done when its deliverable exists at the agreed path, CI is green, CHECKPOINT.md is updated, and the change log has an entry.

## Quick reference

- Live site: https://openendo.org — **user's Lovable app** (repo is NOT the deploy source; Hermes syncs via Lovable API)
- Content URLs for agents: `https://raw.githubusercontent.com/wckdboy/openendo/main/docs/...` (markdown AND JSON)
- Agent index: `docs/llms.txt`
- Knowledge base: `docs/knowledge/` (SCHEMA.md defines the format)
- Research tracks: `docs/research/` (M1 fold-input, M2 evidence, M3 repurposing, T7 lab software)
- Data layer contract: `docs/data/README.md` (file → source → cadence → owner)
- Data pipeline: `scripts/update_data.py` (weekly, Mon 08:00)
- Human wiki hub: `docs/wiki.html`
