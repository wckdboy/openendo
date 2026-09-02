# Ferroptosis direction-of-effect — verdict for the M3 sulfasalazine rank

**Status:** resolved (2026-09-02) · **Owner:** Percival · **Unblocks:** M3
candidate-1 ranking (sulfasalazine → SLC7A11/xCT). Companion to
`m3-validation.md` and the `concepts/ferroptosis.md` knowledge page.

## Question

Does ferroptosis **drive** endometriosis lesion progression or **protect
against** it — i.e., should a therapy *induce* or *inhibit* ferroptosis?
Sulfasalazine is a specific xCT (SLC7A11) inhibitor whose proposed mechanism
is ferroptosis induction in lesion cells; the Sep-2026 SEMA3C paper seemed to
link ferroptosis to lesion *progression*, which would invert that logic.

## Verdict (MEDIUM confidence)

**Ferroptosis is context-dependent by biological compartment — but in the
lesion compartment the directional lean is decisive: endogenous lesion-cell
ferroptosis acts as a growth BRAKE that ectopic cells actively evade, so
*inducing* ferroptosis in lesion cells is the therapeutic direction —
consistent with sulfasalazine's proposed mechanism of action.**

| Compartment | Ferroptosis is… | Evidence direction |
|---|---|---|
| Lesion epithelial/stromal cells | **Protective (bad for the lesion)** — lesions suppress ferroptosis to survive; forcing it is therapeutic | ≥6 independent 2026 studies converge |
| Lesional immune cells (CD8⁺ T cells) | **Pro-lesion** — ferroptosis erases anti-lesion immunity | BMC Med 2025 (PMID 41146213) |
| Eutopic endometrium | **Host-harmful** — impairs decidualization/receptivity (fertility cost) | J Adv Res 2026 (PMID 41722688), Biol Sex Differ 2025 (PMID 41437396) |

Confidence reasoning: **high** on the lesion-cell concept (multiple 2026
mechanistic studies: erastin, andrographolide, placental EVs, FZD7-inhibitor
+ erastin all shrink lesions *via* ferroptosis; MGST3 / HSD11B1 / FZD7–SLC7A11
ferroptosis-evasion all promote progression). **Medium→low** on sulfasalazine
*clinically*: no endometriosis trial data exists, systemic xCT blockade would
also ferroptose lesional CD8⁺ T cells (pro-lesion, PMID 41146213) and eutopic
endometrium (fertility, PMIDs 41722688/41437396), and the SEMA3C model shows
lesion cells can exploit *sub-lethal* ferroptotic signaling (below).

## SEMA3C paper — mechanism précis (PMID 42678895, Gynecol Obstet Invest 2026)

Tissues from 30 endometriosis patients vs 30 controls: **SEMA3C is upregulated
in ectopic lesions vs controls (P<0.001) and vs matched eutopic endometrium
(P<0.001), correlating with disease severity (stage III–IV vs I–II)**. In
ectopic tissue and SEMA3C-overexpressing endometrial stromal cells (HESCs):
**ACSL4 ↑, GPX4/Nrf2/SLC7A11 ↓** (ferroptosis-prone oxidative/inflammatory
state), yet this accompanied **enhanced HESC viability and migration**;
SEMA3C knockdown **or Ferrostatin-1 (a ferroptosis inhibitor)** attenuated the
changes *and* suppressed viability/migration. The paper does **not** show
ferroptotic *death* killing lesion cells — it shows **sub-lethal ferroptotic
signaling sustaining an aggressive phenotype**; blocking that signaling is
beneficial. So SEMA3C is not clean evidence that "ferroptosis drives lesions":
it shows lesion ferroptosis is dysregulated/sub-lethal and exploitable — which
sits *with* (not against) the evasion model. (Full text paywalled at Karger;
précis from the complete structured abstract.)

## Per-study evidence

| PMID | Study (year, journal) | Compartment | What it shows | Supports |
|---|---|---|---|---|
| [42678895](https://pubmed.ncbi.nlm.nih.gov/42678895/) | SEMA3C → ferroptotic signaling (2026, Gynecol Obstet Invest) | Lesion stroma (HESC) | SEMA3C↑ in ectopic; ACSL4↑, GPX4/Nrf2/SLC7A11↓; Fer-1 or knockdown blocks viability/migration | Sub-lethal ferroptotic signaling is pro-aggressive (nuance) |
| [41146213](https://pubmed.ncbi.nlm.nih.gov/41146213/) | Iron overload → CD8⁺ T-cell ferroptosis (2025, BMC Med) | Lesional immune (57 pts) | Iron overload → p53 ↓xCT/GPX4 → CD8⁺ T ferroptosis → immune dysfunction → EM progression; ferroptosis inhibitors reverse | **Against systemic induction** |
| [41001371](https://pubmed.ncbi.nlm.nih.gov/41001371/) | Erastin/xc⁻ concept (2025, Front Med) | Lesion stroma | Erastin inhibits xc⁻/GSH/GPX4 → ferroptosis of ectopic stromal cells = therapeutic direction | Pro-induction |
| [42234252](https://pubmed.ncbi.nlm.nih.gov/42234252/) | MGST3 ferroptosis evasion (2026, Cell Biochem Biophys) | Lesion stroma | Lesions ferroptosis-resistant despite iron overload; MGST3↑ → evasion/invasion; GSTO-IN-2 shrinks lesions in mice | Pro-induction |
| [42151966](https://pubmed.ncbi.nlm.nih.gov/42151966/) | HSD11B1/JUND/IL-10 (2026, Reprod Biol Endocrinol) | Lesion stroma (scRNA+ML) | HSD11B1↑ suppresses ferroptosis → viability↑; knockdown reverses | Pro-induction |
| [41241001](https://pubmed.ncbi.nlm.nih.gov/41241001/) | m6A-FZD7→β-catenin/SLC7A11 (2026, Free Radic Biol Med) | Lesion cells | FZD7↑ → SLC7A11↑ → ferroptosis resistance; FZD7-inhibitor + erastin most potent in mice | Pro-induction; **SLC7A11↑ = key resistance node** |
| [41408483](https://pubmed.ncbi.nlm.nih.gov/41408483/) | Andrographolide (2026, Naunyn Schmiedebergs) | Lesion stroma | Blocks serine synthesis (PSAT1/PHGDH) → ferroptosis+apoptosis → blocks EM; Fer-1 rescues | Pro-induction |
| [42186752](https://pubmed.ncbi.nlm.nih.gov/42186752/) | Placental EVs (2026, Am J Reprod Immunol) | Lesion cells | EVs ↓GPX4/SLC7A11 → ferroptosis → inhibit EM; Fer-1 reverses | Pro-induction |
| [41722688](https://pubmed.ncbi.nlm.nih.gov/41722688/) | SLC7A11/G6PD decidualization (2026, J Adv Res) | Eutopic (adenomyosis) | Eutopic ESCs: ferroptosis↑ → impaired decidualization/infertility; decidualization needs SLC7A11 | Eutopic ferroptosis = host-harmful |
| [41437396](https://pubmed.ncbi.nlm.nih.gov/41437396/) | DPP4/ferroptosis & receptivity (2025, Biol Sex Differ) | Eutopic (PCOS) | Endometrial ferroptosis impairs receptivity; sitagliptin (anti-ferroptotic) restores implantation | Eutopic ferroptosis = host-harmful |
| [42660839](https://pubmed.ncbi.nlm.nih.gov/42660839/) | Autophagy–ferroptosis review (2026) | All | Crosstalk central to EM; direction previously unresolved | Context |
| [42253950](https://pubmed.ncbi.nlm.nih.gov/42253950/) | Microbiota–iron–ferroptosis review (2026, Front Immunol) | All | Dysbiosis–iron-overload–ferroptosis shapes the lesion microenvironment | Context (pro-lesion via inflammation) |
| [42467989](https://pubmed.ncbi.nlm.nih.gov/42467989/) | Adenomyosis scRNA cell-death atlas (2026, Brief Bioinform) | Immune (macrophages) | Ferroptosis enriched in macrophages; linked to pain/inflammatory activation | Adjacent disease |

## Implication for sulfasalazine (M3 candidate 1)

Sulfasalazine's xCT block mirrors erastin (PMID 41001371) and attacks the
SLC7A11 resistance node (PMID 41241001) — **directionally correct for lesion
cells**. The unresolved part is delivery and selectivity: systemic xCT
inhibition would also ferroptose lesional CD8⁺ T cells (pro-lesion, PMID
41146213) and eutopic endometrium (fertility, PMIDs 41722688/41437396), and
xCT-active sulfasalazine doses carry the toxicity seen in the 2010 glioma
trial (see m3-validation.md). **Verdict stands: WATCHLIST LOW-MEDIUM** —
mechanism direction now supports induction-in-lesion-cells; the blockers are
selectivity, route and dose, not direction. A lesion-localized/low-dose
regimen question, not a "should we induce at all" question.

## Plain-language summary

Ferroptosis plays two opposing roles in endometriosis depending on which cell
it hits. Ectopic lesion cells live in an iron-rich, oxidative environment and
must actively switch ferroptosis *off* (via GPX4, SLC7A11/xCT and related
proteins) to survive and grow; forcing them back into ferroptosis — with
erastin, andrographolide, or drugs like sulfasalazine that block xCT —
reproducibly shrinks lesions in 2026 preclinical studies. But the same
ferroptosis striking the lesion's own CD8⁺ T cells disables the immune attack
on the lesion and helps it grow, and ferroptosis in the womb lining harms
fertility. The SEMA3C paper adds that lesion cells can harness low-level
ferroptotic signaling to become more aggressive. Net: ferroptosis induction is
the right weapon against lesion cells — but it needs to be aimed at the
lesion, not sprayed systemically.

*Research synthesis by Percival (Hermes Agent), 2026-09-02. All sources are
public (PubMed/Europe PMC). Hypothesis-generation; not medical advice.*
