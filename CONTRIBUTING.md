# Contributing to OpenEndo

Thank you for helping make an invisible disease impossible to ignore. 💛

## First, read

- [How to support OpenEndo](https://raw.githubusercontent.com/wckdboy/openendo/main/docs/support.html) — the seven ways to help
- [BRAND.md](BRAND.md) — brand tokens, voice and repo conventions (agents: this is your spec)
- [Style guide](https://raw.githubusercontent.com/wckdboy/openendo/main/docs/styleguide.html) — the visual design system

## Good first issues

- [Translate the site](https://github.com/wckdboy/openendo/issues/1) — add a language to the i18n dict
- [Submit funding / research leads](https://github.com/wckdboy/openendo/issues/2) — edit `docs/data/funding.json` / `content.json`

## PR checklist

- [ ] Links verified (HTTP 200) — no invented sources, ever
- [ ] UI strings bilingual EN + DA (`{en, da}` in JSON). Do not edit the Lovable app from this repo
- [ ] JSON schema unchanged (see BRAND.md); `python3 scripts/update_data.py` run if trial data changed
- [ ] Style guide / BRAND.md updated if you changed a token or component
- [ ] Leftover `docs/*.html` is not the product UI — do not delete `what-we-know.html` (live `/research` fetch)
- [ ] Voice check: patient-first, evidence-first, hope not hype

## What never ships

Hallucinated citations · miracle-cure claims · "sufferers" · unverified statistics · anything that reads as medical advice without pointing to a specialist.

Everything here is MIT — the data is a public good, and so is your contribution. Questions? Open an issue.
