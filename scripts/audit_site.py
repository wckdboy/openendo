#!/usr/bin/env python3
"""OpenEndo product + data-contract audit.

Decree 2026-09-04: this repo is data / research / analytics only. The public
UI lives in wckdboy/openendo-www (Lovable) at https://openendo.org. GitHub
Pages CNAME-redirects there; leftover docs/*.html is NOT the product.

This script used to Playwright-audit a locally served copy of docs/*.html
(index, wiki, support, one-pagers, ai-agenda, styleguide). That clung to
dead static pages after the site split. Playwright viewport/a11y of those
files is retired.

What we check instead:

  1. Local files the live app depends on (PR-relevant; no network).
     openendo-www fetches these from raw.githubusercontent.com on main —
     CI must validate the copies in THIS checkout, not the live raw URLs
     (those still point at main during a PR).
       - docs/what-we-know.html + docs/assets/fonts/* + what-we-know.pdf
         (/research iframe + PDF toolbar)
       - docs/data/funding.json   (Home funding section)
       - docs/data/access.json    (/access)
       - docs/data/content.json   (editorial contract; not yet live-fetched)
       - docs/knowledge/index.md  (/knowledge live catalog; bundled fallback)

  2. HTTPS smoke of live openendo.org key routes (product availability).
     Optional: --skip-live / --local-only when offline.

Usage:
    python3 scripts/audit_site.py [--artifacts dir] [--skip-live]

Exit 0 = pass, 1 = issues found, 2 = setup/usage error.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
DATA = DOCS / "data"

# Live product routes (Lovable). /da/* are the Danish locale twins.
LIVE_BASE = "https://openendo.org"
LIVE_ROUTES = [
    "/",
    "/dashboard",
    "/research",
    "/access",
    "/knowledge",
    "/da",
    "/da/dashboard",
    "/da/research",
    "/da/access",
    "/da/knowledge",
]

# Fonts referenced by what-we-know.html (live /research rewrites these to raw URLs).
FONT_RE = re.compile(r"assets/fonts/([A-Za-z0-9._-]+)")
USER_AGENT = "OpenEndo-site-audit/2.0 (+https://github.com/wckdboy/openendo)"


def _fail(issues: list[str], msg: str) -> None:
    issues.append(msg)


def check_what_we_know(issues: list[str]) -> dict:
    """Local contract for the /research live fetch."""
    html_path = DOCS / "what-we-know.html"
    pdf_path = DOCS / "what-we-know.pdf"
    info: dict = {"html": str(html_path), "ok": True}

    if not html_path.is_file():
        _fail(issues, "missing live-fetch target: docs/what-we-know.html")
        info["ok"] = False
        return info

    html = html_path.read_text(encoding="utf-8", errors="replace")
    info["bytes"] = html_path.stat().st_size
    if info["bytes"] < 2000:
        _fail(issues, f"docs/what-we-know.html is suspiciously small ({info['bytes']} bytes)")
        info["ok"] = False
    if "<html" not in html.lower():
        _fail(issues, "docs/what-we-know.html is not an HTML document")
        info["ok"] = False
    if "what we know" not in html.lower():
        _fail(issues, "docs/what-we-know.html missing expected explainer heading")
        info["ok"] = False

    fonts = sorted(set(FONT_RE.findall(html)))
    info["fonts"] = fonts
    if not fonts:
        _fail(issues, "docs/what-we-know.html references no assets/fonts/ (live iframe rewrites these)")
        info["ok"] = False
    missing_fonts = [name for name in fonts if not (DOCS / "assets" / "fonts" / name).is_file()]
    if missing_fonts:
        _fail(issues, f"what-we-know fonts missing on disk: {missing_fonts}")
        info["ok"] = False

    if not pdf_path.is_file():
        _fail(issues, "missing docs/what-we-know.pdf (openendo-www /research toolbar links RESEARCH_PDF_URL)")
        info["ok"] = False
    else:
        magic = pdf_path.read_bytes()[:5]
        info["pdf_bytes"] = pdf_path.stat().st_size
        if magic != b"%PDF-":
            _fail(issues, "docs/what-we-know.pdf does not start with %PDF-")
            info["ok"] = False
    return info


def check_funding(issues: list[str]) -> dict:
    path = DATA / "funding.json"
    info: dict = {"path": str(path), "ok": True}
    if not path.is_file():
        _fail(issues, "missing docs/data/funding.json (Home funding section fetches this live)")
        info["ok"] = False
        return info
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        _fail(issues, f"funding.json is not valid JSON: {e}")
        info["ok"] = False
        return info
    if not isinstance(data, list) or not data:
        _fail(issues, "funding.json must be a non-empty JSON array")
        info["ok"] = False
        return info
    bad = [i for i, row in enumerate(data) if not isinstance(row, dict) or not str(row.get("name") or "").strip()]
    if bad:
        _fail(issues, f"funding.json entries missing name at index {bad[:5]}")
        info["ok"] = False
    info["count"] = len(data)
    return info


def check_access(issues: list[str]) -> dict:
    path = DATA / "access.json"
    info: dict = {"path": str(path), "ok": True}
    if not path.is_file():
        _fail(issues, "missing docs/data/access.json (/access fetches this live)")
        info["ok"] = False
        return info
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        _fail(issues, f"access.json is not valid JSON: {e}")
        info["ok"] = False
        return info
    if not isinstance(data, dict):
        _fail(issues, "access.json must be a JSON object")
        info["ok"] = False
        return info
    if data.get("schema") != "openendo-access-v1":
        _fail(issues, f"access.json schema must be openendo-access-v1 (got {data.get('schema')!r})")
        info["ok"] = False
    countries = data.get("countries")
    if not isinstance(countries, dict) or not countries:
        _fail(issues, "access.json.countries must be a non-empty object")
        info["ok"] = False
        return info
    if "DK" not in countries:
        _fail(issues, "access.json.countries missing DK (full-coverage home market)")
        info["ok"] = False
    info["country_count"] = len(countries)
    return info


def check_knowledge_index(issues: list[str]) -> dict:
    """Local contract for the /knowledge live fetch (openendo-www #1)."""
    path = DOCS / "knowledge" / "index.md"
    schema = DOCS / "knowledge" / "SCHEMA.md"
    info: dict = {"path": str(path), "ok": True}
    if not path.is_file():
        _fail(issues, "missing docs/knowledge/index.md (/knowledge fetches this live)")
        info["ok"] = False
        return info
    text = path.read_text(encoding="utf-8")
    links = re.findall(r"\[\[([A-Za-z0-9._-]+)\]\]", text)
    info["pages"] = links
    if len(links) < 5:
        _fail(issues, f"docs/knowledge/index.md has too few [[wikilinks]] ({len(links)})")
        info["ok"] = False
    if not schema.is_file():
        _fail(issues, "missing docs/knowledge/SCHEMA.md")
        info["ok"] = False
    return info


def check_content(issues: list[str]) -> dict:
    path = DATA / "content.json"
    info: dict = {"path": str(path), "ok": True}
    if not path.is_file():
        _fail(issues, "missing docs/data/content.json (editorial contract)")
        info["ok"] = False
        return info
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        _fail(issues, f"content.json is not valid JSON: {e}")
        info["ok"] = False
        return info
    if not isinstance(data, dict):
        _fail(issues, "content.json must be a JSON object")
        info["ok"] = False
        return info
    for key in ("stats", "problems", "actions", "resources"):
        val = data.get(key)
        if not isinstance(val, list) or not val:
            _fail(issues, f"content.json.{key} must be a non-empty array")
            info["ok"] = False
    info["keys"] = sorted(data.keys())
    return info


def http_get(url: str, timeout: float = 20) -> tuple[int, bytes]:
    req = urllib.request.Request(
        url,
        method="GET",
        headers={"User-Agent": USER_AGENT, "Accept": "text/html,application/xhtml+xml,*/*"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            # Read enough to confirm a real document, not an empty 200.
            body = resp.read(4096)
            return int(resp.status), body
    except urllib.error.HTTPError as e:
        return int(e.code), b""
    except urllib.error.URLError as e:
        raise RuntimeError(f"network error: {e.reason}") from e


def check_live_routes(issues: list[str]) -> list[dict]:
    rows = []
    for route in LIVE_ROUTES:
        url = f"{LIVE_BASE}{route}"
        tag = f"live {route}"
        try:
            status, body = http_get(url)
        except Exception as e:  # noqa: BLE001 — surface any transport failure
            _fail(issues, f"{tag}: {e}")
            rows.append({"route": route, "status": "ERROR", "detail": str(e)})
            continue
        if status >= 400:
            _fail(issues, f"{tag}: HTTP {status}")
            rows.append({"route": route, "status": status, "detail": "HTTP error"})
            continue
        snippet = body.decode("utf-8", errors="replace")
        if "openendo" not in snippet.lower():
            _fail(issues, f"{tag}: HTTP {status} but body does not mention OpenEndo")
            rows.append({"route": route, "status": status, "detail": "unexpected body"})
            continue
        rows.append({"route": route, "status": status, "detail": "OK"})
    return rows


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--artifacts", default="audit-artifacts")
    ap.add_argument("--skip-live", "--local-only", dest="skip_live", action="store_true",
                    help="skip HTTPS smoke of openendo.org (offline / local-only)")
    # Kept so old CI invocations do not crash; ignored on purpose.
    ap.add_argument("--base-url", default=None, help=argparse.SUPPRESS)
    args = ap.parse_args()

    if args.base_url:
        print("note: --base-url is ignored — docs/ static HTML is no longer the product UI", file=sys.stderr)

    issues: list[str] = []
    report = {
        "product": "openendo.org (wckdboy/openendo-www)",
        "legacy_docs_html": "not audited (site-split decree 2026-09-04)",
        "what_we_know": check_what_we_know(issues),
        "funding": check_funding(issues),
        "access": check_access(issues),
        "content": check_content(issues),
        "knowledge": check_knowledge_index(issues),
        "live": None,
    }

    if not args.skip_live:
        report["live"] = check_live_routes(issues)
    else:
        report["live"] = "skipped"

    art = Path(args.artifacts)
    art.mkdir(exist_ok=True)
    (art / "audit-report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(json.dumps(report, indent=2, ensure_ascii=False))
    if issues:
        print("\n::error::audit issues found:")
        for i in issues:
            print(f"  - {i}")
        return 1
    n_live = 0 if args.skip_live or not isinstance(report["live"], list) else len(report["live"])
    print(f"\nContract checks passed (live routes: {n_live}) — report in {art}/audit-report.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
