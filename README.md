# OpenEndo 🎗️ — open data hub for endometriosis

**Open intelligence for a disease the world still ignores.**

Endometriosis affects ~190 million women worldwide (1 in 10 of reproductive age), yet the average patient waits **7–10 years** for a diagnosis, research funding is a fraction of what the burden demands, and there is still **no cure**.

This repository is an open, weekly-refreshed data hub: clinical trials, research papers, funding deadlines and policy — for patients, relatives, researchers, journalists and politicians.

> **OpenEndo** (formerly *endometriosis-watch*): open source, MIT licensed, built for collaboration. The data is yours.

## Live site

👉 **https://openendo.org/** (GitHub Pages, static, bilingual EN/DA) · fallback: https://wckdboy.github.io/openendo/

## More

- [Style guide](https://openendo.org/styleguide.html) — the design system (visual)
- [BRAND.md](BRAND.md) — brand tokens & conventions, machine-readable (for AI agents)
- [How to support](https://openendo.org/support.html) — seven ways to help
- [AI & compute agenda](https://openendo.org/ai-agenda.html) — what agents/algorithms/compute can do for endometriosis
- [One-pager (DA)](https://openendo.org/one-pager-dk.html) — for Danish politicians
- [CONTRIBUTING.md](CONTRIBUTING.md) — PR checklist

## What's inside

```
docs/                         published site (GitHub Pages: main branch → /docs)
  index.html, style.css, app.js   the dashboard (static, bilingual EN/DA, Chart.js)
  data/                           open datasets (JSON, refreshed weekly)
    trials_global_recruiting.json   recruiting trials worldwide        (ClinicalTrials.gov)
    trials_denmark.json             all registered trials in Denmark
    trials_recent.json              new/updated trials, last 7 days
    pubmed_recent.json              new papers, last 7 days             (PubMed)
    pubmed_monthly.json             papers per month, last 6 months
    meta.json                       generation timestamp + counts
    funding.json                    funding opportunities with deadlines (curated)
    content.json                    stats, problem framing, actions, resources (curated, EN/DA)
scripts/update_data.py        regenerates docs/data/*.json from the APIs, commits & pushes
```

## How the data is refreshed

Every week an automated job runs:

```bash
python3 scripts/update_data.py
```

It queries the **ClinicalTrials.gov API v2** and **PubMed E-utilities**, writes the JSON files, and pushes a commit only when something changed. The site is static — no server needed.

## Sources

- ClinicalTrials.gov API v2 (public domain / NLM data usage policy)
- PubMed E-utilities (NCBI)
- Curated editorial content with sources in `data/content.json`
- WHO fact sheet on endometriosis; Danish patient organisation (endo.dk); Lægehåndbogen (sundhed.dk)

## Knowledge base

OpenEndo runs a knowledge base for agents **and** humans — interlinked markdown
with provenance, confidence markers and a review workflow:

- **Agent discovery:** `https://openendo.org/llms.txt` — machine-readable index of the whole site, data and knowledge
- **Conventions:** `docs/knowledge/SCHEMA.md` (agents must read before contributing)
- **Index:** `docs/knowledge/index.md` · pages in `entities/`, `concepts/`, `comparisons/`, `queries/`
- **Review workflow:** agents contribute via PRs; the weekly monitor job reviews and merges
- **Privacy rule:** no personal data, patient stories or PII in this repo — enforced by a CI scan (`.github/workflows/security-scan.yml`). Family/health/business context lives in a separate **private** repo.

## Contributing

This project exists to be used and extended. Ways to help:

- **Submit leads** — open an issue with funding calls, new trials or policy developments we've missed
- **Translate** — the site is bilingual (EN/DA); adding more languages is a small PR
- **Add resources** — patient organisations, diagnostics, centres (`docs/data/content.json`)
- **Run the pipeline** — fork, `python3 scripts/update_data.py`, PR the refreshed data
- **Spread the word** — this disease is ignored because it is invisible; sharing is a contribution

Good first issues are tagged `good first issue`.

## License

MIT — reuse the data, the site and the scripts freely. Attribution is appreciated.

## Disclaimer

This is **research and advocacy, not medical advice**. Treatment choices must always be made with a specialist. Project is independent and not affiliated with any of the organisations referenced.

*Open source, independent and unaffiliated — built for patients, researchers and policymakers. The data is a public good.*
