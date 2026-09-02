# T7 Phase A — Danish lab shortlist + outreach draft

> T7 (lab software modernization) interview phase. Goal: 2–3 Danish
> labs/institutes to interview about their lab-software reality — the
> pain-point data that drives the OpenLab deploy kit and the instrument
> inbox. Phase A (this doc, agent work) = shortlist + outreach draft.
> Phase B (human) = conduct the interviews; publish anonymized write-ups.
> Framework: `templates/interview-guide-dk.md` + fillable
> `templates/lab-interview-form.pdf`.

## Selection criteria
1. **Real lab-software surface** — ELN/LIMS/CDS users with daily friction
2. **Reachable** — public contact path or existing network (the KU student
   contact bridges 2 of 3)
3. **Diversity** — academic + corporate + public-health perspectives

## Shortlist

### 1. Københavns Universitet — Department of Biology (protein & analytical labs)
- **Why:** the student contact studies here; academic labs run a
  long tail of instrument software + Excel pipelines with no IT budget —
  the exact "old and frustrating" profile; high openness to open-source
  tools (eLabFTW-class).
- **Reach:** via the student contact (direct) or department
  (https://www.bio.ku.dk — public contact).
- **Interview target:** lab technician / PhD student running
  HPLC/LC-MS or protein work.
- **Fit:** T7 primary persona.

### 2. DTU — National Food Institute / Bioengineering (analytical chemistry)
- **Why:** large analytical chemistry environment (chromatography-heavy,
  LIMS-managed), strong public-sector research culture, national
  reference labs — good contrast to KU's smaller academic setup.
- **Reach:** public department contact (https://www.food.dtu.dk /
  https://www.bioengineering.dtu.dk).
- **Interview target:** lab manager / analytical chemist (LIMS power user).
- **Fit:** LIMS-heavy workflow profile.

### 3. Statens Serum Institut (SSI) — diagnostic/reference laboratories
- **Why:** public-health diagnostics run regulated LIMS (21 CFR
  Part 11-adjacent, audit trails) — the compliance-heavy profile where
  OpenELIS-class OSS matters; also the patient-diagnostics angle aligns
  with OpenEndo's mission.
- **Reach:** public contact (https://www.ssi.dk).
- **Interview target:** quality/lab informatics person.
- **Fit:** regulated-lab profile; informs the "compliance without
  vendor lock-in" roadmap.

**Backup candidates:** Novo Nordisk / Novonesis analytical labs (via the
student contact — corporate stack: Empower/Chromeleon/Spotfire; richest
data, lowest accessibility — treat as bonus, not dependency).

## Outreach draft (Danish) — for a lab manager or researcher

```
Emne: Kort interview om lab-software — hjælp os med at gøre den bedre

Hej [Navn],

Jeg kontakter dig fra OpenEndo — et open-source projekt, der arbejder på
at gøre lab-software nem at bruge, nem at deploye og nem at ændre (MIT-
licenseret, openendo.org). Vi har talt med studerende, der oplever, at
softwaren i danske laboratorier er gammel og frustrerende — og vi vil
gerne bygge noget bedre på et ægte grundlag i stedet for at gætte.

Derfor søger vi 2–3 danske laboratorier, der vil dele deres hverdag med
os i et kort interview (30–45 min, virtuelt eller fysisk).

Hvad vi spørger om:
- Hvilke programmer I bruger dagligt (ELN, LIMS, instrumentsoftware…)
- Hvad der frustrerer, og hvad I laver manuelt, som burde være automatisk
- Om jeres data kan komme UD af systemerne igen

Praktisk:
- Interviewet er anonymiseret i al publiceret form
- Det er ikke salg, research eller reklame — kun input til et open-source
  projekt (spørgsmålene kan I se på forhånd, hvis I vil)
- Ingen følsomme data forlader jeres laboratorium

Hvis I har 30 minutter en af de kommende uger, vil I så hjælpe os? Svar
bare på denne mail, eller send mig en kalenderinvitation.

Med venlig hilsen
[Percival / projektets kontakt]
OpenEndo — openendo.org
```

## Interview logistics (Phase B checklist)
1. Send outreach → book 30–45 min (Teams/Meet/fysisk)
2. Send `templates/interview-guide-dk.md` (or the fillable PDF) beforehand
3. Record notes per question; keep names/institutions out of any published
   write-up (anonymization mandatory; SCHEMA PII rule)
4. Publish anonymized write-ups under `docs/research/` + fold findings
   into `lab-software-modernization.md`
5. DoD per checkpoint: ≥2 anonymized interviews merged; CI green

## Honest limits
- Contact details are department-level public channels only — no
  individual emails invented; the KU student contact is the strongest
  warm path and should be used first.
- Corporate labs (Novo/Novonesis) may decline — the backup list covers
  that case.

*Phase A by Percival (Hermes Agent), 2026-09-02. Sources: T7 track doc,
institution homepages (public).*
