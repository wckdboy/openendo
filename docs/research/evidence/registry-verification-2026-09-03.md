# M3 registry verification — ClinicalTrials.gov (2026-09-03)

> Purpose: verify the M3 shortlist's novelty/clinical-usage claims against
> the trial registry itself (live query, 2026-09-03). Method:
> ClinicalTrials.gov API v2, `query.cond=endometriosis AND query.intr=<drug>`,
> pageSize=100, counted returned studies. Dienogest (established endo drug)
> used as query sanity control → 40 hits, method validated.

## Results

| Drug (M3 candidate) | Endo trials on CT.gov | Reading |
|---|---|---|
| **Sirolimus** | **0** | novelty claim confirmed — no registered endo trial |
| Rapamycin | 0 | same molecule, confirms |
| **Sulfasalazine** | **0** | novelty confirmed (watchlist/wrong-direction row stands on mechanism, not absence of data) |
| **Cetrorelix** | **2** (NCT04071574, NCT00244452) | confirms "already used in endometriosis" — supports VALIDATED-AXIS reading of the MRGPRX2 hit |
| Crizotinib | 0 | — |
| Dabrafenib | 0 | — |
| Cyclosporine | 0 | — |
| Tacrolimus | 0 | — |
| Estradiol | 50 | add-back/HRT context in GnRH trials — expected, not a repurposing signal |
| Dinoprostone | 1 (NCT03142035) | — |

## Implications for the shortlist (`m3-validation.md`)

1. **Sirolimus (TOP TIER):** novelty strengthened — zero registered endo
   trials despite independent mechanistic/animal evidence. Cleanest
   repurposing case on the board.
2. **Cetrorelix → MRGPRX2:** two endo trials exist (older GnRH-antagonist
   studies) — the drug is established in endo; the *target* (MRGPRX2 pain
   axis) is the novel element, not the drug.
3. **Sulfasalazine:** no trial data either way — consistent with the
   ferroptosis-direction verdict (mechanism risk, not data gap).
4. Caveat: CT.gov only — EU CTIS/older registry entries may differ;
   a full cross-registry check is out of scope for this pass.

*Verification by Percival (Hermes Agent), 2026-09-03. Live registry data;
research context, not clinical guidance.*
