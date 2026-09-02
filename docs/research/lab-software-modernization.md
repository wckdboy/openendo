# Lab Software Modernization — T7

**Problem, as reported by students and confirmed across the industry:**
the software researchers actually use in labs is old, proprietary and
frustrating. Legacy LIMS and chromatography data systems (CDS) predate
modern APIs, lock data in vendor formats, and force manual re-curation in
Excel. Modern open-source alternatives exist (elabFTW, Chemotion, SampleDB,
PASTA-ELN) — but adoption routinely fails because deployment and
configuration are burdensome and workflows are rigid.

**Design principle (our commitment):** *easy to deploy, easy to modify.*
No researcher should be hindered by their tools.

## The four jobs a lab tool must do (from the 2026 ELN-landscape analysis)

1. **Collect** — bring instrument output in without manual export/re-attach
2. **Share** — make work visible to collaborators in real time
3. **Search** — find "that experiment from 18 months ago" in under 10 minutes
4. **Fit the bench** — work offline at the instrument, sync when possible

If a tool fails any of the four, scientists quietly revert to paper/Excel.

## Design rules (what "easy to deploy, easy to modify" means concretely)

| Rule | Why |
|---|---|
| **Single-command deploy** (Docker Compose, runs on any VPS incl. Coolify) | deployment friction is the #1 adoption killer |
| **Local-first, then sync** (PASTA-ELN pattern) | labs have instruments on isolated networks |
| **Open formats everywhere** (JSON/CSV/SQLite; data escapes freely) | no vendor lock-in — the data is the user's |
| **Config-driven + open source** (AGPL/MIT) | a student can modify it without vendor support |
| **Modern UX** | younger scientists expect modern tools; antiquated UIs alienate talent |
| **Bilingual EN/DA** | Danish labs are our home turf |

## Deliverables (roadmap)

1. **Pain-point registry** (this issue/track) — real, named software and
   frustrations from students/researchers → the requirements source of truth
2. **OpenLab deploy kit** — a one-command Docker Compose bundle
   (elabFTW + Jupyter + RDM tooling), Danish-ready templates, documented
   for a final-year student to run on a €5 VPS in an afternoon
3. **Instrument data inbox** (small, original tool if the registry shows
   the need) — ingest instrument exports (CSV/PDF), tag, search, sync —
   one of the four jobs done extremely well instead of a huge platform
4. **Contribution back upstream** — fixes/templates/docs for the OSS we
   use; we do not fork-and-abandon

## How to contribute

- **Researchers/students:** open an issue with: software name, what it does,
  the 3 most frustrating things, what a good day with it looks like
- **Developers:** pick a pain point, propose a fix, follow the agent
  protocol (claim via issue, branch, PR)

*Track owner: Percival (Hermes Agent). Part of the OpenEndo research program
(docs/research/RESEARCH.md).*
