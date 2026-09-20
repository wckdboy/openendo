# OpenEndo engine findings — human-review shortlist (2026-09-14)

> Curated from `/workspace/findings-live/2026-09-14/` (engine 0.1.1, deepseek-flash, 49 findings).
> Cross-checked against local `/workspace/openendo` corpus + live NCBI E-utilities / Europe PMC on 2026-09-14.
> **No invented citations.** Research support only — not medical advice.

**Inputs:** `findings.json` + `report.md` (live run 2026-09-14T14:00:39Z) · openendo data/knowledge/M3 · drafts literature/registry packets.

---

## TLDR

49 engine findings collapse to **11 KEEP** themes, **9 WATCH**, and the **remainder DROP** (~29 after de-duplication; a few IDs are DROP-as-written and KEEP-reframed, e.g. sirolimus/FKBP4). The run mostly **re-discovered M3 under anonymous ChEMBL IDs** and then re-stated the same axes as gaps, leads, and hypotheses. After de-duplication and direction review:

- **Reinforce** the three known OpenEndo leads (sirolimus/mTOR, MRGPRX2 antagonism, sulfasalazine/xCT), with one important correction: the engine tagged **CHEMBL413 (sirolimus)** as a wrong-direction FKBP4 ligand because `compact_repurposing()` never passed drug names or M3 status.
- **Extend** MRGPRX2 into a tryptase/TRPM3/PAR2 pain loop; extend ACVR1B into a fibrosis (activin/TGF-β) hypothesis; extend the prostaglandin module toward the one recruiting molecular-drug trial (**vipoglanstat**, NCT07260669, mPGES-1 — not in the 58-target list).
- **Do not contradict** ferroptosis-induction-in-lesion-cells; the engine’s “direction unknown” on SLC7A11 is **stale vs** `ferroptosis-direction.md`.
- **PMID 42719373 is real**, endometriosis-pain-related, and **not a hallucination**. It is in weekly LATEST + digest, absent from the 7-day `pubmed_recent.json` window. Full text was fetched; the engine only had the title.
- **No other PMID/NCT orphans.** All 11 cited PMIDs resolve at NCBI; all 11 cited NCTs are in `trials_global_recruiting.json`.
- Lean engine PR should fix: **title-only PubMed**, **max_phase not disease-specific**, **redundant uncoupled stages**, and (highest-impact) **unnamed repurposing candidates**.

**Path:** `docs/research/discovery/findings-shortlist-2026-09-14.md`

---

## 1. Orphan PMID 42719373 — verification

**Verdict: exists. Not invented. Endometriosis + pain. Not an identifier orphan vs the engine whitelist.**

| Check | Result |
|---|---|
| NCBI esummary | UID `42719373` returned |
| NCBI efetch | Abstract retrieved |
| Europe PMC | `hitCount: 1`, PMID 42719373, PMCID **PMC13557153**, DOI 10.2147/IJWH.S603470 |
| Title | *Achieving Minimal-to-No Pain in Women with Endometriosis Treated with Relugolix Combination Therapy: SPIRIT Extension Trial.* |
| Journal / date | *Int J Womens Health* 18:603470; epub **2026 Sep 5** |
| Authors | Lukes AS, Venturella R, Dynowski K, Wagman RB, Perry JS, Zhong Y, Rakov VG, Mechsner S, Johnson NP |
| Related to endo/pain? | **Yes.** Post hoc of SPIRIT 1/2 + 80-week LTE: time to minimal-to-no **dysmenorrhea** and **non-menstrual pelvic pain**, amenorrhea, analgesic-free status in women with endometriosis on relugolix-CT. |

**What the abstract actually says** (not inferred from the title): 802/1261 entered LTE, 501 completed 104 weeks. Median time to minimal-to-no dysmenorrhea **8 weeks** on relugolix-CT (not reached on placebo by week 24); cumulative probability 82.5% vs 22.4% at week 24, ~95% at week 104 once all arms were on drug. NMPP is slower (median 32 weeks; 42.6% at week 24 → 70.5% at week 104). Industry-sponsored post hoc; symptomatic endpoints, not a mechanism test.

**Local corpus location (why it looked “orphan”):**

| File | 42719373 |
|---|---|
| `docs/research/evidence/weekly/2026-09-11.json` (LATEST) | **present** (title only) |
| `docs/research/evidence/digest-2026-09-11.md` | **present** (curated; “only clinically actionable item” that week) |
| `CHECKPOINT.md` | **present** |
| `docs/data/pubmed_recent.json` (7-day feed, updated 2026-09-14) | **absent** — epub 2026-09-05, aged out of the rolling window |
| knowledge wiki (`sirolimus.md`, `mrgprx2-pain.md`, `ferroptosis.md`, `m3-validation.md`) | **absent** (correct: not a top-3 lead paper) |
| Engine whitelist | **in** via `evidence_weekly`, not via `pubmed_recent` |

Engine used it in CONF-0001 and HYPO-0014 from **title + journal metadata only** (weekly JSON has no abstract). CONF-0001’s “minimal-to-no pain contradicts a central-dominant model” is a **title-level over-read**: the paper does not measure central vs peripheral generators, NMPP lags dysmenorrhea, and placebo-crossover at 104 weeks converges. HYPO-0014 then **inverts** the paper (treats non-responders as evidence for a GPER1 escape path). See DROP.

---

## 2. Identifier audit — all cited PMIDs / NCTs

Engine cited **11 PMIDs** and **11 NCTs**. Batch NCBI esummary 2026-09-14: **11/11 PMIDs exist**; titles match weekly JSON. Local trials JSON: **11/11 NCTs present**.

### PMIDs

| PMID | NCBI title (short) | In weekly LATEST | In pubmed_recent | Orphan? |
|---|---|---|---|---|
| 42709073 | Correction: endometriosis subtypes and T2D (ARCHES) | yes | yes | no |
| 42713565 | Immune networks + gut microbiota targets (multi-omics) | yes | yes | no |
| 42716136 | β-glucuronidase / estrobolome review | yes | yes | no |
| 42717121 | HDAC inhibitors in endometriosis (review) | yes | yes | no |
| 42717122 | ZEB1 as EMT / hormonal-resistance regulator (review) | yes | yes | no |
| 42717817 | #Enzian TVS distribution / laterality / POD obliteration | yes | yes | no |
| **42719373** | Relugolix-CT SPIRIT extension, minimal-to-no pain | **yes** | **no** | **no** (weekly-only; see §1) |
| 42720355 | Fibrotic substrate stiffness ↑ epithelial motility | yes | yes | no |
| 42720599 | Inflammatory genes distinguish symptomatic vs asymptomatic | yes | yes | no |
| 42722072 | Disc excision + bowel suturing for nodules >3 cm | yes | yes | no |
| 42722127 | Non-invasive brain stimulation in chronic pelvic pain (SR) | yes | yes | no |

**No other PMID orphans.** Weekly JSON and `pubmed_recent.json` are **title-only** (no `abstract` field). Digest-2026-09-11 has curator-written summaries; the engine did **not** receive those.

### NCTs (all in `docs/data/trials_global_recruiting.json`)

| NCT | Local title | Phase | Engine use |
|---|---|---|---|
| NCT06161805 | Esketamine as treatment for chronic pain due to endometriosis | PHASE3 | RESE-0007, 0011 — anaesthetic, not a 58-target modulator |
| NCT06333353 | rTMS for endometriosis-associated pain | NA | RESE-0007 — neuromodulation |
| NCT07305025 | Pelvic Pain Electro-Acupuncture | NA | RESE-0007 — acupuncture |
| NCT07260669 | Vipoglanstat in women with endometriosis | PHASE2 | RESE-0011 — **only recruiting molecular drug besides esketamine**; mPGES-1, **not** in the 58 |
| NCT05698212 | MetriDx lab-developed diagnostic biomarkers | PHASE2 | RESE-0011 — diagnostic |
| NCT07240883 | ENDO1000 UK-wide research project | N/A | RESE-0011 — cohort/research infrastructure |
| NCT07696351 | Ultra-long GnRH-a pretreatment for FET in DIE | PHASE4 | RESE-0011 — ART protocol, not a novel-target test |
| NCT07693283 | “Expression of Target in Endometriotic Lesions” | N/A | RESE-0012 — target unnamed in title |
| NCT07713797 | Biomarkers for endometriosis | N/A | RESE-0012 |
| NCT06820450 | Steroidome / EDCs / vaginal dysbiosis | N/A | RESE-0012 |
| NCT07578480 | MEN-ENDO: menstrual stem cells | N/A | RESE-0012 |

**No NCT orphans.** Trial records in the corpus are title/phase/sponsor only — no intervention-molecule field — so “no trial on the 58 targets” is a **title-level** snapshot, as the engine’s own caveats say.

---

## 3. Comparison to known OpenEndo top leads

M3 ranked shortlist (`m3-validation.md`, registry re-checked 2026-09-14): **sirolimus → mTOR (TOP TIER)** · **MRGPRX2 antagonism (VALIDATED AXIS; cetrorelix is not the drug)** · **sulfasalazine → SLC7A11 (WATCHLIST)**.

| Known lead | Engine behaviour | Verdict vs M3 |
|---|---|---|
| **Sirolimus / mTOR** (CHEMBL413 → FKBP4 pChEMBL 8.38) | REPU-0004 flags CHEMBL413 as **wrong-direction FKBP4** immunophilin ligand; never names sirolimus, mTOR, or the independent endo evidence base. RESE-0009 treats the three FKBP4 hits as “chemically related, direction unresolved.” | **Contradicts by mis-identity, not by new data.** Clinical pharmacology is FKBP12–mTORC1, not FKBP4/PR-chaperone inhibition. **Do not demote TOP TIER.** Fold FKBP4 into a separate PR-resistance note (already OpenEndo doctrine). |
| **MRGPRX2 antagonism** (not cetrorelix) | REPU-0008 correctly flags CHEMBL1200490 as **likely agonist / wrong-direction**. HYPO-0003 + RESE-0007 + RESE-0013 build a mast-cell → tryptase/chymase → TRPM3/TRPA1/PAR2 loop and note **zero mechanism-directed pain trials**. | **Reinforces** “antagonist, not cetrorelix.” **Extends** the axis into proteases and TRP channels and into a concrete trial-gap. Matches 2026-09-14 literature packet (no new endo antagonist paper; histamine/mast context only). |
| **Sulfasalazine / xCT** (CHEMBL421 → SLC7A11 pChEMBL 6.8) | REPU-0001 rank-1 “likely correct-direction **if inhibitor**.” RESE-0005 claims **no direction-of-effect** in the dataset. HYPO-0012 proposes lesion-selective ferroptosis. | **Reinforces WATCHLIST mechanism.** RESE-0005 is **stale**: `ferroptosis-direction.md` already resolved induction-in-lesion-cells as the therapeutic sign (MEDIUM), with systemic/CD8⁺/eutopic selectivity as the blocker. Engine never saw that file. Do **not** upgrade off WATCHLIST; FIN56 PMID 42698143 is in weekly JSON but was not used. |

**Not contradicted:** estradiol/GPER1 and dinoprostone/SLCO2A1 remain wrong-direction (engine agrees). Crizotinib/dabrafenib → ACVR1B remain poor drug-fit (engine did not know the names; pChEMBL 6.07–6.22 is correctly called marginal). CsA/tacrolimus remain immunosuppressant-baggage WATCHLIST.

**New adjacency (extend, not a fourth top lead):** NCT07260669 vipoglanstat (mPGES-1) is the only recruiting **molecular** endo drug besides esketamine. It is prostaglandin-pathway kin to HPGD/SLCO2A1/PTGER4 (HYPO-0005) even though mPGES-1 is not in the 58. That is the one clinical hook the engine almost missed by insisting “the entire 58 is clinically unengaged.”

---

## 4. KEEP (11) — actionable, medium+, grounded

Each item is de-duplicated across stages. Engine IDs in parentheses are the source findings, not eleven independent discoveries.

### K1 — MRGPRX2 → mast-cell proteases → nociceptor channels (pain path)

- **Claim:** Lesion mast-cell MRGPRX2 activation releases tryptase (TPSAB1) / chymase (CMA1) that sensitise TRPM3/TRPA1 (and PAR2) on pelvic afferents; **antagonism or mast-cell stabilisation**, not cetrorelix agonism, is the testable non-hormonal pain intervention. No recruiting trial hits this axis (esketamine / rTMS / electro-acupuncture do not).
- **Why it matters:** Pain is the unmet need; hormonal suppression (relugolix-CT, PMID 42719373) treats a different level of the axis. A receptor-level PoM would be the first **attributable** molecular pain test in the current portfolio.
- **Evidence grounding:** M3 VALIDATED AXIS (PMID 40600649, not in this week’s whitelist — do not re-cite as if the engine had it). Local: MRGPRX2/TPSAB1/CMA1/F2RL1/TRPM3 are novel 58-targets; CHEMBL1200490 = cetrorelix pChEMBL 6.21 **agonist** (M3). Trials NCT06161805 / NCT06333353 / NCT07305025 exist locally and are not target-directed. Phase 0.5 GEO: mast-marker enrichment is **endometrioma-biased**, near-background in peritoneal lesions — keep lesion-type in the experiment.
- **Next experiment:** Human iPSC-nociceptor or DRG calcium imaging with endometrioma- vs peritoneal-lesion mast-cell supernatant ± MRGPRX2 antagonist (not cetrorelix) ± tryptase inhibition; stratify by lesion type.
- **Risks:** MRGPRX2 is primate-biased (rodent models fail); tryptase tools are dirty; peritoneal lesions may not recapitulate the FASEB axis. Engine HYPO-0003 confidence medium is fair; REPU-0008 correctly kills cetrorelix-as-drug.
- **vs top-3:** **Extends** MRGPRX2. IDs: HYPO-0003, RESE-0007, RESE-0013. Drop REPU-0008 as a separate “lead.”

### K2 — SLC7A11 / ferroptosis induction in lesion cells (not a polarity mystery)

- **Claim:** CHEMBL421 (sulfasalazine) → SLC7A11 may induce ferroptosis in endometriotic lesion cells; GPX4 has no approved-drug hit in-screen. Therapeutic sign in OpenEndo’s own dossier is **induction in lesion cells**, not “unknown.”
- **Why it matters:** Only mature approved-drug starting point in the ferroptosis module; selectivity (lesion vs CD8⁺ T cells vs eutopic/ovary) is the real gate, not direction.
- **Evidence grounding:** Local screen pChEMBL 6.8; M3 WATCHLIST + `ferroptosis-direction.md` (MEDIUM). Weekly JSON contains FIN56 PMID 42698143 (engine unused). GEO: SLC7A11 down in lesions — on-target expression at the disease site is the thin part of the case (already in M3).
- **Next experiment:** Already specified in ferroptosis-direction / Phase 0.5: lipid-ROS + ferrostatin rescue in **paired lesion vs eutopic** epithelium/stroma; do not run a new undirected polarity hunt. Optional CPU: overlap PMID 42728524 biomarker genes vs OpenEndo SLC7A11/GPX4/ACSL4 set (already on the research-agenda).
- **Risks:** Systemic xCT block ferroptoses lesional CD8⁺ T cells (PMID 41146213); eutopic/ovarian costs; sulfasalazine xCT-active doses ≠ RA doses. EA papers claiming ferroptosis *suppression* (PMIDs 42081613, 42155249 — literature packet, not engine) keep compartment **contested**.
- **vs top-3:** **Reinforces WATCHLIST; does not upgrade.** IDs: REPU-0001, HYPO-0012. **Do not KEEP RESE-0005** as written (stale “no direction”).

### K3 — Sirolimus is TOP TIER via mTOR; the FKBP4 hit is not the drug thesis

- **Claim:** CHEMBL413 is **sirolimus** (pChEMBL 8.38 vs FKBP4). The engine’s wrong-direction FKBP4-inhibition story is a **screen-identity failure**, not new biology. Rank on mTOR antiproliferative / ovarian-senescence evidence; keep FKBP52/PR-resistance as a **separate** chaperone question (CHEMBL160 cyclosporine, CHEMBL269732 tacrolimus stay WATCHLIST).
- **Why it matters:** If a reviewer accepted REPU-0004 at face value, OpenEndo’s #1 lead would be discarded. The lean-PR bug (unnamed `per_target` candidates) caused this.
- **Evidence grounding:** `repurposing_candidates.json` top-level `candidates[]`: CHEMBL413 name=`Sirolimus (rapamycin)` status=`top-tier`. M3 + `entities/sirolimus.md` + 2026-09-14 registry: **0** endo trials for sirolimus/rapamycin/everolimus/temsirolimus/mTOR. FKBP4 eutopic mRNA down (PMIDs 22279148, 27778641); Fkbp52−/− PR-resistance (17571166, 18988805) — none of these were in the engine whitelist this run.
- **Next experiment:** Unchanged: Phase 2 P2-A MD when GPU budget clears (FKBP12 RAP control vs FKBP52 pose). Do **not** start an FKBP4-inhibitor programme from CsA/tacro.
- **Risks:** Conflating mTOR inhibition with “restoring FKBP4” (explicitly warned in research-agenda). Chronic mTOR immunosuppression in a benign disease.
- **vs top-3:** **Reinforces TOP TIER; contradicts the engine’s FKBP4-sign call.** IDs: REPU-0004 (reframe), RESE-0009 (reframe). Drop REPU-0005/0006 as drugs.

### K4 — Activin/ALK4–TGFBR1 as a fibrosis switch (not crizotinib/dabrafenib)

- **Claim:** An activin-A/TGF-β over BMP imbalance via ACVR1B + TGFBR1 may convert lesion stroma to contractile myofibroblasts; a **selective ALK4/ligand-trap experiment** tests DIE fibromuscular disease. The two approved-drug hits (CHEMBL601719 crizotinib pChEMBL 6.07, CHEMBL2028663 dabrafenib 6.22) are marginal, off-target-heavy TKIs — already M3 WATCHLIST LOW.
- **Why it matters:** Fibrosis is the surgical/pain substrate of DIE; a clean ALK4 tool would test a whole module (including TGFBR1, already non-novel, max_phase 2 **any-indication**).
- **Evidence grounding:** HYPO-0006 medium; TGF-β fibrosis canon + ZEB1/EMT review PMID 42717122 (title-level disease context only). M3: ALK4–Smad–aromatase axis is real; drug fit is poor. PMID 42720355 (stiffness/motility) is a parallel mechanical input, not proof of ALK4.
- **Next experiment:** Patient-derived lesion fibroblasts: collagen-gel contraction + α-SMA ± ALK4-selective inhibition, **stiffness-controlled** plates (to unconfound HYPO-0007). Do not use crizotinib/dabrafenib as probes.
- **Risks:** Pleiotropy of TGF-β blockade; culture stiffness; pChEMBL 6.07–6.22 is non-selective noise. Title-only ZEB1 citation does not establish ACVR1B as the switch.
- **vs top-3:** **Extends** ACVR1B WATCHLIST toward a better experiment; does not promote the TKIs. IDs: HYPO-0006. Drop REPU-0002/0003 and RESE-0010 as drug leads.

### K5 — Fibrosis is mechanically active: ILK–YAP1 as the stiffness-motility bridge

- **Claim:** PMID 42720355 shows fibrotic-range substrate stiffness increases endometriotic epithelial motility (biphasic in the digest). The untested bridge is an ILK–YAP1–FN1 circuit: YAP1/ILK loss should abolish the stiff-substrate motility gain and spare soft-substrate motility.
- **Why it matters:** Reframes fibrosis from end-stage scar to a **feed-forward spread mechanism** — a treatment-path reason to care about mechanotransduction, not just lesion excision.
- **Evidence grounding:** PMID 42720355 exists (NCBI confirmed); digest: tunable PA hydrogels, intermediate stiffness maximises speed/stress fibres/focal adhesions/spheroid expansion. ILK/YAP1/FN1 requirement is **untested** (engine correctly classified untested-hypothesis, medium). YAP1 and ILK are novel 58-targets, no repurposing hit.
- **Next experiment:** Same hydrogel system as 42720355 + YAP1 knockdown / ILK inhibition, readout motility on stiff vs soft only. Falsifier: effect not stiffness-specific.
- **Risks:** In-vitro ECM ≠ lesion matrix; YAP1 pleiotropy; CONF-0004’s “vs inert scar” is one-sided (no sourced counter-paper). Do not treat this as a conflict with ZEB1/EMT (CONF-0005) until a single cross-over experiment exists.
- **vs top-3:** **New**, compatible with mTOR/YAP neighbourhood; not a drug lead yet. IDs: HYPO-0007. WATCH CONF-0004; DROP CONF-0005.

### K6 — ENTPD1/ENTPD2 (CD39-family) → adenosine → ADORA2B: untested immuno-pain node

- **Claim:** Nucleotide catabolism upstream of adenosine is untargeted in this snapshot (ENTPD1/2, ABCC4: mechanisms=0, max_phase=0); ADORA2B is max_phase **2.0 in ChEMBL-any-indication, not endometriosis**. Worth a lesion adenosine-flux measurement before any receptor story.
- **Why it matters:** Adenosine sits on macrophage phenotype, NK cytotoxicity, and nociception — a possible reason lesions persist and hurt despite inflammation. Downstream receptor tools exist; **source control** (ectoenzymes) does not, in-screen.
- **Evidence grounding:** Local `targets.json` matches the engine’s mechanism/max_phase numbers. **No** endo-specific adenosine trial in the recruiting portfolio. HYPO-0001 (NK restoration) is a plausible but **low-confidence** causal leap — keep the **gap** (RESE-0002, medium), not the NK-killing claim.
- **Next experiment:** Paired lesion vs eutopic CD39/CD73/ABCC4 activity + extracellular ATP/AMP/adenosine; only then ADORA2B vs ADORA2A selective blockade in autologous co-culture.
- **Risks:** `max_phase` will mislead reviewers into thinking ADORA2B is “in phase 2 for endometriosis.” Direction of adenosine (pro- vs anti-inflammatory) is context-dependent. Engine caveat on this point is correct and should be a **data-field label**, not a model caveat.
- **vs top-3:** **New module**, not a competitor. IDs: RESE-0002. Drop HYPO-0001/0002 as KEEP-level claims.

### K7 — Prostaglandin tone (HPGD / SLCO2A1 / PTGER4) and the vipoglanstat adjacency

- **Claim:** Local PGE2/PGF2α tone is set by synthesis, HPGD catabolism, and SLCO2A1 reuptake; **PTGER4 blockade** is the cleaner receptor hypothesis than inhibiting SLCO2A1 (which would raise extracellular PGs). Dinoprostone (CHEMBL815) is PGE2 — wrong-direction as a drug. The **one** recruiting molecular endo drug, vipoglanstat (NCT07260669, mPGES-1), is pathway-adjacent though not in the 58.
- **Why it matters:** Gives the “58 targets clinically unengaged” finding a constructive exception: prostaglandin biology **is** in the clinic, just not under OpenEndo’s gene list. EP4 vs mPGES-1 is a real design choice.
- **Evidence grounding:** Local screen: CHEMBL815 pChEMBL 7.35 vs SLCO2A1; M3 wrong-direction. NCT07260669 recruiting PHASE2 in local trials (title names vipoglanstat). HYPO-0005 medium is fair if stripped of mouse-model over-specification.
- **Next experiment:** Map mPGES-1 / HPGD / SLCO2A1 / PTGER4 protein in the same biopsies used for any vipoglanstat translational work; do **not** pursue dinoprostone or SLCO2A1 inhibition as therapy.
- **Risks:** Ex-vivo PG measurements are artefact-prone; engine RESE-0003 frames a “polarity gap” that M3 already closed for the **drug** (wrong direction) even if transporter biology remains interesting.
- **vs top-3:** **Extends** the landscape around (not against) the three leads. IDs: HYPO-0005, plus a corrected reading of RESE-0011. Drop REPU-0009.

### K8 — Recruiting portfolio does not test the 58 — with one prostaglandin-class exception

- **Claim:** Among recruiting interventional **molecular** drugs in the provided portfolio, esketamine (NCT06161805) and vipoglanstat (NCT07260669) are the only named molecules; **neither target is in the 58**. Diagnostics, surgery, lifestyle, neuromodulation, and ART dominate.
- **Why it matters:** Even approved-drug hits (sirolimus, sulfasalazine) have **no registered endo trial** — independently confirmed by the 2026-09-14 CT.gov packet (0/0/0 for sirolimus/sulfasalazine/MRGPRX2). The translational stall is real.
- **Evidence grounding:** Local trial titles as tabled in §2; registry-verification-2026-09-14.md. Title-only limitation is honest.
- **Next experiment:** Maintain an explicit target↔trial↔approved-drug map (engine should emit this as a table, not a paragraph). First rows: sirolimus 0, sulfasalazine 0, MRGPRX2 antagonist 0, vipoglanstat mPGES-1 (adjacent), cetrorelix 2 historical (not recruiting).
- **Risks:** Partial portfolio; titles hide molecules. Do not claim “no one is working on these targets” outside CT.gov.
- **vs top-3:** **Reinforces novelty claims.** ID: RESE-0011.

### K9 — Tryptase-selective chemistry is the missing probe for the mast-cell pain module

- **Claim:** CMA1 has one mapped mechanism at max_phase 2.0 (**any indication**); TPSAB1 has none. A tryptase-selective tool would test a node shared by MRGPRX2, PAR2, and lesion innervation.
- **Why it matters:** Converts K1 from a three-receptor story into a **single biochemical measurement** (tryptase activity in lesion interstitial fluid).
- **Evidence grounding:** Local targets.json TPSAB1 mech=0 / max_phase=0; CMA1 mech=1 / max_phase=2.0. Same max_phase caveat as K6.
- **Next experiment:** Isoform-resolved tryptase activity in endometrioma vs peritoneal interstitial fluid; PAR2 cleavage assay on human nociceptors.
- **Risks:** ChEMBL mechanism coverage incomplete; max_phase 2 ≠ endo. Fold under K1 if review wants a shorter KEEP list.
- **vs top-3:** **Extends** MRGPRX2. ID: RESE-0013.

### K10 — Relugolix-CT pain timelines are a **clinical context** finding, not a mechanism conflict

- **Claim (corrected):** PMID 42719373 documents rapid dysmenorrhea control and slower NMPP / analgesic-free trajectories on an oral GnRH-antagonist add-back regimen. That is **shared-decision evidence**, already flagged in digest-2026-09-11. It does **not** adjudicate peripheral vs central pain generators (CONF-0001) and does **not** imply a GPER1 escape path in non-responders (HYPO-0014).
- **Why it matters:** Stops the engine from using the only high-quality clinical paper of the week as a conflict prop. NMPP lag is the scientifically interesting residue (residual non-hormonal pain — which is exactly K1’s job).
- **Evidence grounding:** Full abstract (§1), not the title. Digest already called it the week’s only clinically actionable item.
- **Next experiment:** None for OpenEndo wet-lab. For synthesis: pair 42719373 NMPP-lag with the symptomatic-vs-asymptomatic transcriptome (PMID 42720599, IL16 — **not** NLRP3 as HYPO-0011 guessed).
- **Risks:** Industry post hoc; 104-week completers are a selected subset (501/802).
- **vs top-3:** Neutral / context. Rescue of CONF-0001’s source; drop the conflict framing.

### K11 — S1P as mTOR-neighbourhood biology (gap, not a chemical lead)

- **Claim:** SPHK1/S1PR2/S1PR3 have no approved-drug hit at pChEMBL≥6 in-screen and no recruiting endo trial. Independently, 2025–26 literature (PMID 40532686, **not in this engine whitelist**) already ties **S1PR4 → mTOR** in endometriotic stromal cells with AZD8055 as a pathway tool. The engine’s S1P gap is therefore **adjacent to TOP TIER mTOR**, not a random lipid module.
- **Why it matters:** Avoids opening a de-novo S1P programme while missing that S1P already feeds the lead OpenEndo is testing.
- **Evidence grounding:** Local targets: SPHK1/S1PR2/S1PR3 novel, mech=0, max_phase=0. Literature packet 2026-09-14 (PMID 40532686) is **outside** the engine run — cited here only as already-fetched OpenEndo draft evidence, not as an engine source.
- **Next experiment:** Do not start SPHK1 chemistry. When reading sirolimus/mTOR cell work, include S1P/S1PR4 as an upstream covariate. Optional: add 40532686 to the sirolimus knowledge draft (already proposed).
- **Risks:** S1PR2 vs S1PR3 barrier effects oppose; engine over-claimed “no chemical starting point” (fingolimod-class exists off-screen). Keep as **watchful KEEP** / first item to cut if the list must shrink.
- **vs top-3:** **Extends mTOR neighbourhood.** ID: RESE-0004. Drop HYPO-0009.

---

## 5. WATCH (9) — interesting, too weak or too one-sided to act on

| ID | Why watch, not keep |
|---|---|
| CONF-0001 | Real papers (42719373, 42722127) but **false dichotomy**. Brain-stim SR is mixed-etiology CPP, high RoB (digest). Relugolix is a symptom trial, not a mechanism test. Both can be true in subgroups. Use K10 instead. |
| CONF-0003 | Two narrative reviews (ZEB1 vs HDAC) are not mutually exclusive; HDAC can regulate EMT TFs. Title-only. Maps an epigenetic watchlist, no new human data. |
| CONF-0004 | Stiffness-as-driver is grounded (42720355) but the “inert scar” counter-side has **no identifier**. Keep the experiment as K5, not the conflict. |
| CONF-0006 | Microbiome: β-glucuronidase vs immune-network multi-omics — not exclusive; 42716136 is not endo-specific. Hypothesis-generating. |
| RESE-0001 | Chemoattractant cluster (ACKR3/CX3CR1/CCR6/CCR8/CMKLR1) truly has no approved-drug candidate, but `potent_actives` are 62–92 — “no chemical starting point” overstates. No expression-stratified evidence in this run. |
| RESE-0008 | GPER1 has the strongest pChEMBL (9.52) because the drug is **estradiol**. Target-validating only; M3 already killed the drug. Selectivity work is real but not a near-term path. |
| RESE-0012 | NCT07693283 “Expression of Target in Endometriotic Lesions” unnamed — true annotation gap, not a treatment path. |
| HYPO-0004 | PAR2 as shared stromal/neuronal node is coherent with K1 but low confidence and cleavage-based pharmacology is messy. Subsume under K1 if a PAR2 tool appears. |
| RESE-0003 | Polarity language is leftover from before M3 closed dinoprostone as wrong-direction. Transporter biology can sit under K7. |

---

## 6. DROP (29) — low, redundant, overclaim, or known-wrong-direction

### Wrong-direction / already-adjudicated M3 drugs

| ID | Why drop |
|---|---|
| REPU-0002, REPU-0003 | Crizotinib / dabrafenib → ACVR1B. Marginal pChEMBL, cancer-TKI fertility baggage. Hypothesis kept as K4 without these drugs. |
| REPU-0005, REPU-0006 | Cyclosporine / tacrolimus. Immunosuppressant WATCHLIST; FKBP12 not FKBP4. |
| REPU-0007 | Estradiol → GPER1. M3 ✗ wrong-direction. |
| REPU-0008 | Cetrorelix → MRGPRX2 **agonist**. Keep antagonist thesis as K1. |
| REPU-0009 | Dinoprostone IS PGE2. M3 ✗. |
| REPU-0004 *as written* | Sirolimus misread as FKBP4-wrong-direction. Replaced by K3. |

### Redundant stage re-writes of the same axis

| ID | Subsumed by |
|---|---|
| RESE-0005 | K2 (stale polarity) |
| RESE-0006 | Heterogeneous PFKFB3+PDK3+ILK+YAP1+METTL3 lump; YAP piece is K5 |
| RESE-0009 *as written* | K3 |
| RESE-0010 | K4 |
| HYPO-0001, HYPO-0002 | K6 gap only |
| HYPO-0009 | K11 |
| HYPO-0012 | K2 |

### Low-confidence / likely overclaim from title-only PubMed

| ID | Why drop |
|---|---|
| **HYPO-0011** | Pins symptomatic-vs-asymptomatic split (PMID 42720599) on **TLR8/IRAK4 → NLRP3 + MIF**. Digest gene list is **IL16, IL17RA, JAK3, SMPD3, RELT**, adhesion and neuromod genes — **not** NLRP3/IRAK4/MIF. Title-only hallucination of a fashionable inflammasome story. |
| **HYPO-0014** | Uses 42719373 (good pain response on GnRH-antagonist add-back) to motivate a **GPER1/FKBP4 escape** in non-responders. Inverts the paper; GPER1 pharmacology is dirty; estradiol is the hit. |
| HYPO-0013 | METTL3/m6A controlling ZEB1: evidence cited is HDAC + ZEB1 **reviews**, not m6A. Pleiotropy trap. |
| CONF-0005 | Inferred stiffness-vs-EMT conflict from two independent titles; may collapse if stiffness acts *through* EMT. Low. |
| CONF-0007 | T2D ARCHES **correction notice** (42709073) with no correction text in context. Not a treatment path. |
| CONF-0008 | Uses #Enzian distribution paper (42717817) as the “anatomic pain” side — title does not report pain correlation. Low, over-inferred. |
| CONF-0002 | Surgical disc vs segmental resection. Out of OpenEndo drug/repurposing lane; n=10 technical series. |
| HYPO-0008 | HTRA1 → latent TGF-β. Generic fibrosis folklore, no endo data in set. |
| HYPO-0010 | PFKFB3/PDK3 → succinate → SUCNR1. Low, no disease evidence in set. |
| HYPO-0015 | EPHA2/EPHB4/ACKR3 vascular morphometry. Low. |
| HYPO-0016 | CMKLR1/FPR/CX3CR1 macrophage recruitment. Low; gap watched as RESE-0001. |
| HYPO-0017 | NGFR + BDKRB1 dual block, sourced to a **brain-stimulation** review. Construct-validity weak. |
| HYPO-0018 | NKG2D/MICA shedding. Tumour analogy; 42720599 does not mention it. |
| HYPO-0019 | AOC3/NOS2 adhesion. Low; claim text even mixes in HCK. |

---

## 7. Engine system issues — lean PR (openendo-engine)

Four coupled defects explain most DROP/WATCH noise. None require a model upgrade.

### P0 — `compact_repurposing()` drops drug names and M3 status

`data.py` iterates `per_target.*.candidates`, where `name` is the CHEMBL ID. The informative object is the top-level `candidates[]` (`name=Sirolimus (rapamycin)`, `status=top-tier`, etc.).

**Effect this run:** engine never said “sirolimus,” “sulfasalazine,” “cetrorelix,” or “estradiol”; rediscovered all nine M3 pairs; **tagged sirolimus as wrong-direction**.

**Fix:** compact from `candidates[]` with `name`, `status`, `status_detail`; keep CHEMBL ids. One-line prompt rule: do not re-litigate a `wrong-direction` / `top-tier` status without new whitelist evidence.

### P1 — Title-only PubMed

`pubmed_recent.json` and `weekly/*.json` have no `abstract`. `compact_papers()` is already written to attach abstracts (1500-char cap) but always gets empty. Conflicts + several hypotheses are explicitly “title-level.”

**Effect:** HYPO-0011 invented NLRP3 from an IL16 paper; HYPO-0014 inverted relugolix responders; CONF-0001 over-read a post hoc symptom paper as a mechanism conflict.

**Fix:** store abstract (or digest `why it matters` blurb) on weekly JSON at M2 ingest; or have the engine efetch abstracts for the ≤18 weekly PMIDs at run time. Do not let the model emit mechanism-level conflicts from titles.

### P2 — `max_phase` is not disease-specific

`compact_targets()` emits ChEMBL `max_phase` / `mechanisms` with no indication filter. ADORA2B max_phase 2.0 and CMA1 2.0 are **any-indication**. The model sometimes caveats this (RESE-0002) and sometimes lets it sound like an endometriosis pipeline.

**Fix:** label the field `max_phase_any_indication` in the prompt, or join recruiting NCTs per gene. Do not imply endo clinical stage from ChEMBL max_phase.

### P3 — Redundant uncoupled stages

Gaps → leads → hypotheses share no prior-stage memory (`run_discovery` concatenates four independent calls). Result: SLC7A11 ×3, FKBP4 ×4, ACVR1B ×4, MRGPRX2 ×3, SLCO2A1 ×2, S1P ×2.

**Fix:** pass a compact “already said” list into later stages, or post-hoc collapse by `(gene or molecule, category)` before numbering. Cap per stage (e.g. 8). Dedup would have turned 49 findings into roughly this shortlist automatically.

### Also worth a one-liner in the same PR

- `_default_url()` always builds a **target** report-card URL, including for compounds (CHEMBL421 etc.). Split target vs molecule.
- `pubmed_recent` 7-day window vs weekly LATEST: 42719373 aged out of the 7-day file while remaining the week’s clinical paper — whitelist via weekly saved it; if LATEST fails, clinical papers vanish. Keep weekly as the primary evidence source (already the case for conflicts).

---

## 8. What this shortlist is not

- Not a status upgrade of sulfasalazine off WATCHLIST.
- Not a demotion of sirolimus.
- Not a recommendation to use cetrorelix, estradiol, dinoprostone, crizotinib, or dabrafenib for endometriosis.

---

*Human-review shortlist for DrDoc / Galahad. Live identifiers only. Generated 2026-09-14. Path: `docs/research/discovery/findings-shortlist-2026-09-14.md`*
