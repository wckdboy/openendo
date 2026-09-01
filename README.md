# Endometriosis Watch 🎗️

**Open intelligence for a disease the world still ignores.**

Endometriosis affects ~190 million women worldwide (1 in 10 of reproductive age), yet the average patient waits **7–10 years** for a diagnosis, research funding is a fraction of what the burden demands, and there is still **no cure**.

This repository is an open, weekly-refreshed data hub: clinical trials, research papers, funding deadlines and policy — for patients, relatives, researchers, journalists and politicians.

## Live site

👉 **https://wckdboy.github.io/endometriosis-watch/** (GitHub Pages, static, bilingual EN/DA)

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

## License

MIT — reuse the data, the site and the scripts freely. Attribution is appreciated.

## Disclaimer

This is **research and advocacy, not medical advice**. Treatment choices must always be made with a specialist. Project is independent and not affiliated with any of the organisations referenced.

*Built by Jaeger (Hermes Agent) for the Dearwolf family — and for every woman still waiting to be taken seriously.*
