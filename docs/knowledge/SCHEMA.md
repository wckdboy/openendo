# OpenEndo Knowledge Schema

> Conventions for the OpenEndo knowledge base. Agents MUST read this before
> creating or editing pages. Humans are encouraged to follow it too.

## Domain

Endometriosis research, treatment, diagnostics, funding and policy — plus the
OpenEndo project itself (open data, advocacy, AI-assisted discovery). Public
layer: everything here is public, MIT-licensed, and safe to publish. **No
personal data, no patient stories, no PII. Ever.** Private/sensitive context
lives in the private knowledge base (separate private repo).

## Layers

- `raw/` — immutable source material (articles, papers, guidelines). Agents read, never modify.
- `entities/` — one page per notable entity (drug, trial, company, organisation, diagnostic).
- `concepts/` — one page per topic/mechanism/idea.
- `comparisons/` — side-by-side analyses.
- `queries/` — filed research answers worth keeping.
- `index.md` — content catalog (read this first).
- `log.md` — append-only action log (rotate at 500 entries → `log-YYYY.md`).

## Conventions

- File names: lowercase, hyphens, no spaces.
- Every page starts with YAML frontmatter (below).
- Every page links to ≥2 other pages via `[[wikilinks]]`.
- Bump `updated` on every edit. Add new pages to `index.md`. Log every action.
- **Provenance:** paragraphs synthesising claims from a specific source end with
  `^[url]` markers. Every claim must trace to a source.
- **Confidence:** `high` only for multi-source, verified claims. `medium` for
  single-source or fast-moving. `low` flags review. `contested: true` when
  sources disagree — never silently overwrite; note both positions with dates.
- **No hype, no hope-sales.** Evidence-first, patients first. Unverified claims
  get `confidence: low` and a "verify before relying" note.

## Frontmatter

```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query
tags: [from taxonomy]
sources: [https://…]
confidence: high | medium | low
contested: true   # optional
---
```

## Tag taxonomy

treatment · drug · pipeline · diagnostic · funding · policy · trial ·
research · denmark · advocacy · project · infrastructure

Add new tags here BEFORE using them. No freeform tags.

## Page thresholds

- Create a page when an entity appears in 2+ sources or is central to one.
- Split pages over ~200 lines. Archive fully-superseded pages to `_archive/`.

## Agent rules

- Agents write via pull requests on the public repo; a reviewer agent (or a
  human) merges. Never push directly to `main` on the public repo.
- The weekly monitor job reviews open PRs and merges good ones.
- Data files under `data/` follow their own schemas (see `docs/data/README` if
  present) — evidence pages link to them, never duplicate them.
- If a claim can't be sourced, say so in the page (`confidence: low`) instead
  of omitting the caveat.
