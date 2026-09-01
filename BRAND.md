# BRAND.md — OpenEndo brand & contribution guide (for humans and AI agents)

This file is the machine-readable companion to the [visual style guide](https://openendo.org/styleguide.html). If you are an agent contributing to this repo, follow this file exactly.

## Identity

- **Name:** OpenEndo. Never "Endometriosis Watch" alone — the full name is fine for SEO contexts: "OpenEndo — Endometriosis Watch".
- **Tagline:** open data. real hope.
- **Mission:** make an invisible disease impossible to ignore. Everything ships under MIT as a public good.
- **Symbol:** the yellow awareness ribbon `#FFD60A` (the ribbon of endometriosis). Inline SVG only — the path is in `docs/index.html`. Never recolor, stretch, rotate or add effects.

## Color tokens (source of truth: `docs/style.css` `:root`)

| Token | Hex | Use |
|---|---|---|
| Ink | `#1D1D1F` | headings, brand |
| Text | `#3A3A3C` | body copy |
| Muted | `#6E6E73` | secondary text |
| BG / BG-alt | `#FFFFFF` / `#F5F5F7` | surfaces / alternating sections |
| Line | `#E8E8ED` | borders, dividers |
| Blue | `#0071E3` (+hover `#0077ED`, tint `#E8F1FD`) | actions, links, tags |
| Rose-deep / Lavender | `#E84A6F` / `#BF5AF2` | the signature gradient (hope) |
| Ribbon | `#FFD60A` | the mark ONLY |
| Green | `#34C759` | live, recruiting |
| Gold | `#FF9F0A` | warnings |
| Crimson | `#B0234A` | one-pager urgency only |

## Typography

- Display: **Fraunces** 500–700 (+ italics) — headlines, section titles, the wordmark.
- Everything else: **system sans** (`-apple-system, BlinkMacSystemFont, "SF Pro Display", "Segoe UI", Roboto`).
- One display accent: italic gradient (rose→lavender) on the emotional key word of a headline.

## Voice

Patient-first ("people with endometriosis"), evidence-first (every number sourced, every link verified), hope not hype ("promising" yes, "breakthrough" banned), plain language, never medical advice without pointing to a specialist.

## Layout

Container `1060px`; frosted sticky nav `64px`; section padding `88px` (64 on mobile); alternating white/`#F5F5F7`; card radius `18px`, KPI `14px`, pills `999px`; shadows `0 2px 8px` / hover `0 10px 34px`. Numbered eyebrows (`01`–`05`) with gradient underline; LIVE badge (pulsing green dot) only on the dashboard.

## Repository conventions

- **Data:** JSON in `docs/data/` — schemas: trials (`nct_id`, `title`, `status`, `phase`, `sponsor`, `countries`, `url`), papers (`date`, `title`, `journal`, `url`), funding (`id`, `name`, `org`, `country`, `url`, `deadline` ISO `YYYY-MM-DD` or `null`, `open`, `desc` EN/DA), content (`title`/`body`/`cta` as `{en, da}`, `url`).
- **i18n:** every user-facing string lives in `app.js` `I18N` (EN + DA at minimum) or as `{en, da}` in JSON. Never hardcode UI strings.
- **Assets:** bump `?v=N` in `index.html` for `app.js`/`style.css` changes — GitHub Pages caches aggressively.
- **Pipeline:** `scripts/update_data.py` regenerates `docs/data/`. ClinicalTrials.gov v2: use `filter.overallStatus=RECRUITING`, `query.locn=Denmark`, ISO dates in `RANGE[...]` — naive advanced filters return HTTP 400. Handle 429 with backoff (already in the script).
- **Pages:** site publishes from `/docs` on `main`. Canonical URL `https://openendo.org/`.

## Agent rules

1. Never invent or approximate a source — verify links (HTTP 200) before merging.
2. Keep JSON schemas stable; run `update_data.py` rather than hand-editing trial data.
3. When changing a token or component, update this file AND `styleguide.html` — the guide must always match reality.
4. Keep the MIT license and the mission. Patients first, always.
