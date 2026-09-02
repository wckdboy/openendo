#!/usr/bin/env python3
"""OpenEndo responsive + accessibility audit (Playwright).

Runs every push via .github/workflows/site-audit.yml against a locally
served copy of docs/ (fast feedback before deploy). Checks, per page and
viewport: JS/page errors, horizontal overflow, touch-target sizes,
image alt text, canvas/button accessible names, duplicate IDs, skip-link
presence, mobile-nav behaviour, and (index only) the EN/DA language toggle.

Usage:
    python3 scripts/audit_site.py [--base-url http://127.0.0.1:8080] [--artifacts dir]

Exit code 0 = pass, 1 = issues found. Screenshots always saved to
--artifacts (default: audit-artifacts/) for the Actions upload step.
"""
import argparse
import json
import re
import sys
from pathlib import Path

PAGES = [
    "index.html",
    "wiki.html",
    "support.html",
    "one-pager-en.html",
    "one-pager-dk.html",
    "ai-agenda.html",
    "styleguide.html",
]
VIEWPORTS = [
    ("mobile-375", 375, 812),
    ("tablet-768", 768, 1024),
    ("desktop-1440", 1440, 900),
]
# Resource-load noise that should not fail a run (fonts/CDN hiccups etc.)
IGNORE_CONSOLE = re.compile(r"Failed to load resource|net::ERR_|favicon|404")

JS_CHECK = """
() => {
  const de = document.documentElement, b = document.body;
  const vw = window.innerWidth;
  const offenders = [];
  for (const el of document.querySelectorAll('*')) {
    if (el.children.length) continue;              // leaves only
    const r = el.getBoundingClientRect();
    if (r.width > 0 && (r.right > vw + 1 || r.left < -1)) {
      offenders.push(`${el.tagName.toLowerCase()}.${[...el.classList].slice(0,2).join('.')}#${el.id} right=${Math.round(r.right)} left=${Math.round(r.left)}`);
    }
  }
  const imgs = [...document.images].filter(i => !i.hasAttribute('alt')).map(i => i.src.split('/').pop());
  const canvases = [...document.querySelectorAll('canvas')].filter(c => !c.getAttribute('role') || !c.getAttribute('aria-label')).length;
  const buttons = [...document.querySelectorAll('button')].filter(b => {
    const t = (b.textContent || '').trim();
    return !t && !b.getAttribute('aria-label') && !b.getAttribute('title');
  }).map(b => b.id || b.className);
  const ids = [...document.querySelectorAll('[id]')].map(e => e.id);
  const dupIds = ids.filter((x, i) => ids.indexOf(x) !== i);
  return {
    scrollW: de.scrollWidth, clientW: de.clientWidth,
    bodyScrollW: b ? b.scrollWidth : 0,
    overflow: Math.max(de.scrollWidth, b ? b.scrollWidth : 0) - vw,
    offenders: offenders.slice(0, 5),
    imgsNoAlt: imgs.slice(0, 5),
    canvasesNoA11y: canvases,
    buttonsNoName: buttons.slice(0, 5),
    dupIds: [...new Set(dupIds)].slice(0, 5),
    skipLink: !!document.querySelector('a.skip-link[href="#main"]'),
    mainLandmark: !!document.querySelector('main'),
    lang: document.documentElement.lang,
  };
}
"""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base-url", default="http://127.0.0.1:8080")
    ap.add_argument("--artifacts", default="audit-artifacts")
    ap.add_argument("--viewport", action="append", help="only run named viewport(s), repeatable")
    args = ap.parse_args()

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("::error::playwright not installed (run: pip install playwright && python -m playwright install chromium)")
        return 2

    art = Path(args.artifacts)
    art.mkdir(exist_ok=True)
    wanted = set(args.viewport or [])
    issues = []
    results = []

    with sync_playwright() as p:
        browser = p.chromium.launch()
        for page_name in PAGES:
            for vp_name, w, h in VIEWPORTS:
                if wanted and vp_name not in wanted:
                    continue
                tag = f"{page_name} @ {vp_name}"
                ctx = browser.new_context(viewport={"width": w, "height": h})
                page = ctx.new_page()
                js_errors, console_errs = [], []
                page.on("pageerror", lambda e: js_errors.append(str(e)))
                page.on(
                    "console",
                    lambda m: console_errs.append(m.text) if m.type == "error" and not IGNORE_CONSOLE.search(m.text) else None,
                )
                try:
                    resp = page.goto(f"{args.base_url}/{page_name}", wait_until="networkidle", timeout=30000)
                    page.wait_for_timeout(400)
                    state = page.evaluate(JS_CHECK)
                except Exception as e:  # noqa: BLE001
                    issues.append(f"{tag}: load failure — {e}")
                    results.append((tag, "LOAD_FAIL", str(e)))
                    ctx.close()
                    continue

                page_issues = []
                # 1. JS errors
                if js_errors:
                    page_issues.append(f"JS pageerror: {js_errors[0][:160]}")
                if console_errs:
                    page_issues.append(f"console error: {console_errs[0][:160]}")
                # 2. HTTP status
                if resp is None or resp.status >= 400:
                    page_issues.append(f"HTTP {resp.status if resp else 'no response'}")
                # 3. overflow
                if state["overflow"] > 1:
                    page_issues.append(f"horizontal overflow {state['overflow']}px (doc {state['scrollW']} vs viewport {state['clientW']}); offenders: {state['offenders'][:3]}")
                # 4. touch targets: buttons ≥ 44px (AAA 2.5.5), links ≥ 24px (AA 2.5.8)
                if w <= 960:  # touch-sized viewports
                    small = page.evaluate(
                        """(a) => {
                          const out = [];
                          const check = (els, min, kind) => {
                            for (const el of els) {
                              const st = getComputedStyle(el);
                              if (st.display === 'none' || st.visibility === 'hidden') continue;
                              const r = el.getBoundingClientRect();
                              if (r.width > 0 && (r.width < min || r.height < min)) {
                                out.push(`${kind} ${el.tagName.toLowerCase()}.${[...el.classList].slice(0,2).join('.')} ${Math.round(r.width)}x${Math.round(r.height)}`);
                              }
                            }
                          };
                          check(document.querySelectorAll(a.sels44.join(',')), 44, 'btn');
                          check(document.querySelectorAll(a.sels24.join(',')), 24, 'link');
                          return out.slice(0, 6);
                        }""",
                        {"sels44": ["button", ".btn", ".nav-toggle", "#lang-toggle"], "sels24": [".nav-links a", "a[class]", ".kb-card h3 a"]},
                    )
                    if small:
                        page_issues.append(f"touch target too small: {small}")
                # 5. a11y DOM checks
                if state["imgsNoAlt"]:
                    page_issues.append(f"images missing alt: {state['imgsNoAlt']}")
                if state["canvasesNoA11y"]:
                    page_issues.append(f"{state['canvasesNoA11y']} canvas(es) without role=img + aria-label")
                if state["buttonsNoName"]:
                    page_issues.append(f"buttons without accessible name: {state['buttonsNoName']}")
                if state["dupIds"]:
                    page_issues.append(f"duplicate ids: {state['dupIds']}")
                if not state["skipLink"]:
                    page_issues.append("no skip-link (a.skip-link[href='#main'])")
                if not state["mainLandmark"]:
                    page_issues.append("no <main> landmark")

                # 6. functional: mobile nav opens on mobile viewports
                if w <= 960 and page.locator("#nav-toggle").count():
                    try:
                        page.click("#nav-toggle")
                        page.wait_for_timeout(250)
                        expanded = page.get_attribute("#nav-toggle", "aria-expanded")
                        nav_visible = page.is_visible("#mobile-nav a")
                        if expanded != "true" or not nav_visible:
                            page_issues.append(f"mobile nav did not open (aria-expanded={expanded}, links visible={nav_visible})")
                    except Exception as e:  # noqa: BLE001
                        page_issues.append(f"mobile nav interaction failed: {e}")

                # 7. functional: EN/DA toggle on index
                if page_name == "index.html" and vp_name == "desktop-1440" and page.locator("#lang-toggle").count():
                    try:
                        page.click("#lang-toggle")
                        page.wait_for_timeout(300)
                        lang_da = page.evaluate("document.documentElement.lang")
                        page.click("#lang-toggle")
                        page.wait_for_timeout(300)
                        lang_en = page.evaluate("document.documentElement.lang")
                        if lang_da != "da" or lang_en != "en":
                            page_issues.append(f"lang toggle broken (da={lang_da}, en={lang_en})")
                    except Exception as e:  # noqa: BLE001
                        page_issues.append(f"lang toggle failed: {e}")

                shot = art / f"{page_name.replace('.html', '')}_{vp_name}.png"
                page.screenshot(full_page=False, path=str(shot))

                status = "OK" if not page_issues else "FAIL"
                results.append((tag, status, "; ".join(page_issues)[:300]))
                for pi in page_issues:
                    issues.append(f"{tag}: {pi}")
                ctx.close()
        browser.close()

    print(json.dumps(results, indent=1, ensure_ascii=False))
    if issues:
        print("\n::error::audit issues found:")
        for i in issues:
            print(f"  - {i}")
        return 1
    print(f"\nAll {len(results)} checks passed — screenshots in {art}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
