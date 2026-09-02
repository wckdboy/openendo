# AGENTS.md — OpenEndo

This file is auto-read by AI agent tooling (Codex, Claude Code, Hermes, etc.) when working in this repository.

## First step: read the checkpoint

**Read `CHECKPOINT.md` before starting any work.** It is the living source of truth for:

- what is currently in focus (top 3)
- what tasks are on the horizon and need focus (prioritized backlog)
- blockers / open questions (incl. things only a human can do)
- what was recently done

## Rules for agents

1. **Check first** — read CHECKPOINT.md + `git pull` before starting. Don't redo finished work.
2. **Update as you go** — when you start, finish, or reprioritize a task, update CHECKPOINT.md (status, date, change log) and commit it in the same push as your work.
3. **Never merge a PR with a failing check** — CI (security-scan: gitleaks + PII) must be green. If a check fails, investigate before merging; do not merge past it.
4. **Wiki content bar** — knowledge pages need real sources + `confidence` field (see `docs/knowledge/SCHEMA.md`). No hype, no speculation, patients first.
5. **GitHub Pages cannot serve `.md` files** — agent-facing links to markdown must use `https://raw.githubusercontent.com/wckdboy/openendo/main/...` URLs, not relative site paths.
6. **No PII in this public repo** — never commit names, emails, or credentials (CI scans for this and will block).
7. **Pull before push** — always rebase on origin/main before pushing; the weekly monitor job also commits here.

## Quick reference

- Live site: https://openendo.org (GitHub Pages, from `docs/`)
- Agent index: `docs/llms.txt`
- Knowledge base: `docs/knowledge/` (SCHEMA.md defines the format)
- Research tracks: `docs/research/` (M1 fold-input, M2 evidence, M3 repurposing, T7 lab software)
- Data pipeline: `scripts/update_data.py` (weekly, Mon 08:00)
- Human wiki hub: `docs/wiki.html`
