#!/usr/bin/env python3
"""Generate public datasets for the Endometriosis Watch site (GitHub Pages).

Queries ClinicalTrials.gov API v2 + PubMed E-utilities, writes data/*.json,
commits and pushes to GitHub when anything changed. Silent when unchanged
(watchdog pattern: empty stdout = nothing to report).

Usage: python3 scripts/update_data.py
"""
import json, os, subprocess, sys, time, urllib.parse, urllib.request
from datetime import date, datetime, timedelta, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "docs", "data")
TODAY = date.today()
WEEK = TODAY - timedelta(days=7)

FIELDS = ("protocolSection.identificationModule.briefTitle,"
          "protocolSection.identificationModule.nctId,"
          "protocolSection.statusModule.overallStatus,"
          "protocolSection.designModule.phases,"
          "protocolSection.sponsorCollaboratorsModule.leadSponsor,"
          "protocolSection.contactsLocationsModule.locations.country,"
          "protocolSection.conditionsModule.conditions")


def fetch(url):
    last = None
    for attempt in range(6):
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": "openendo/1.0 (github.com/wckdboy/openendo)"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            last = e
            if e.code in (429, 500, 502, 503, 504):
                wait = (2 ** attempt) + 1
                if e.headers.get("Retry-After"):
                    try:
                        wait = int(e.headers["Retry-After"])
                    except ValueError:
                        pass
                time.sleep(min(wait, 30))
                continue
            raise
        except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
            last = e
            time.sleep((2 ** attempt) + 1)
    raise last


def _is_relevant(ident, p):
    """Keep only trials that actually study endometriosis — the free-text
    query.term matches any field (e.g. 'Danazol for cytopenias in cirrhosis'
    or pediatric surgery programs), which pollutes the dashboard with noise.
    Relevance = 'endometriosis' in title OR in the studied conditions."""
    title = (ident.get("briefTitle") or "").lower()
    conds = " ".join(p.get("conditionsModule", {}).get("conditions") or []).lower()
    return "endometriosis" in title or "endometriosis" in conds


def trials_from(data, n=999):
    out = []
    dropped = 0
    for s in (data.get("studies") or [])[:n]:
        p = s.get("protocolSection", {})
        ident = p.get("identificationModule", {})
        if not _is_relevant(ident, p):
            dropped += 1
            continue
        status = p.get("statusModule", {})
        des = p.get("designModule", {})
        spon = p.get("sponsorCollaboratorsModule", {})
        locs = p.get("contactsLocationsModule", {}).get("locations") or []
        countries = sorted({l.get("country", "") for l in locs if l.get("country")})
        nct = ident.get("nctId", "")
        out.append({
            "nct_id": nct,
            "title": ident.get("briefTitle", ""),
            "status": status.get("overallStatus", ""),
            "phase": "/".join(des.get("phases") or []) or "N/A",
            "sponsor": spon.get("leadSponsor", {}).get("name", ""),
            "countries": countries,
            "url": f"https://clinicaltrials.gov/study/{nct}",
        })
    if dropped:
        sys.stderr.write(f"  (filtreret {dropped} ikke-relevante forsøg)\n")
    return out


def ctg(query, params, page_size=1000):
    """Fetch ALL pages of a ClinicalTrials.gov v2 query (no silent truncation).

    CT.gov paginates with pageToken/nextPageToken; callers used to get at most
    50 studies (hardcoded pageSize) and never noticed when a registry outgrew
    it. Now: countTotal=true, pageSize up to 1000, loop until nextPageToken
    disappears (safety cap 20 pages / 20k studies).
    """
    studies, token, total = [], None, None
    for _ in range(20):
        url = ("https://clinicaltrials.gov/api/v2/studies?query.term="
               + urllib.parse.quote(query) + "&" + params
               + f"&pageSize={page_size}&countTotal=true"
               + ("&pageToken=" + urllib.parse.quote(token) if token else "")
               + "&fields=" + urllib.parse.quote(FIELDS))
        d = fetch(url)
        studies.extend(d.get("studies") or [])
        if d.get("totalCount") is not None:
            total = d["totalCount"]
        token = d.get("nextPageToken")
        if not token:
            break
    return {"studies": studies, "totalCount": total}


def pubmed_ids(mindate, maxdate, retmax=15):
    q = urllib.parse.quote("endometriosis[Title/Abstract]")
    url = (f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={q}"
           f"&datetype=pdat&mindate={mindate}&maxdate={maxdate}&retmax={retmax}&retmode=json")
    d = fetch(url)
    res = d.get("esearchresult", {})
    return res.get("idlist", []), int(res.get("count", 0))


def pubmed_summary(ids):
    if not ids:
        return {}
    url = (f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed"
           f"&id={','.join(ids)}&retmode=json")
    return fetch(url).get("result", {})


def save(name, obj):
    """Atomic write: temp file + os.replace, so a crash mid-run never leaves a
    truncated/corrupt JSON that the live site (or the weekly RO-Crate diff)
    would read."""
    path = os.path.join(DATA, name)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
    os.replace(tmp, path)


def _load_prev_list(name):
    """Return the previous run's top-level list (trials/papers) or None."""
    try:
        with open(os.path.join(DATA, name), encoding="utf-8") as f:
            d = json.load(f)
    except (OSError, ValueError):
        return None
    for key in ("trials", "papers"):
        if isinstance(d, dict) and isinstance(d.get(key), list):
            return d[key]
    return None


def apply_floor(name, rows):
    """Empty-dataset floor: if a source comes back empty but we already have a
    non-empty dataset on disk (transient API hiccup / upstream reset), keep the
    previous rows and report on stderr — never publish a silently emptied
    registry. Returns the rows that should be published (caller saves them, so
    meta counts always match file contents). Watchdog pattern preserved:
    nothing on stdout when unchanged."""
    if not rows:
        prev = _load_prev_list(name)
        if prev:
            sys.stderr.write(f"  {name}: kilde tom — beholder tidligere data "
                             f"({len(prev)} rækker), opdatering sprunget over\n")
            return prev
    return rows


def git(*args):
    return subprocess.run(["git", "-C", ROOT, *args], capture_output=True, text=True)


def main():
    os.makedirs(DATA, exist_ok=True)

    # --- Clinical trials ---
    glob = ctg("endometriosis", "filter.overallStatus=RECRUITING")
    time.sleep(2)
    dk = ctg("endometriosis", "query.locn=Denmark")
    time.sleep(2)
    dkrec = ctg("endometriosis", "query.locn=Denmark&filter.overallStatus=RECRUITING")
    time.sleep(2)
    adv = urllib.parse.quote(f"AREA[LastUpdatePostDate]RANGE[{WEEK.isoformat()},{TODAY.isoformat()}]")
    rec = ctg("endometriosis", "filter.advanced=" + adv)
    time.sleep(2)

    t_glob = trials_from(glob)
    t_dk = trials_from(dk)
    t_dkrec = trials_from(dkrec)
    t_rec = trials_from(rec)
    t_glob = apply_floor("trials_global_recruiting.json", t_glob)
    t_dk = apply_floor("trials_denmark.json", t_dk)
    t_rec = apply_floor("trials_recent.json", t_rec)
    # t_dkrec is a meta count only (subset of t_dk) — no file, no floor
    save("trials_global_recruiting.json", {"updated": TODAY.isoformat(), "trials": t_glob})
    save("trials_denmark.json", {"updated": TODAY.isoformat(), "trials": t_dk})
    save("trials_recent.json", {"updated": TODAY.isoformat(), "trials": t_rec})

    # --- PubMed: recent papers ---
    ids, _ = pubmed_ids(WEEK.isoformat(), TODAY.isoformat(), retmax=15)
    summ = pubmed_summary(ids)
    papers = []
    for pmid in ids:
        v = summ.get(pmid, {})
        papers.append({
            "date": v.get("pubdate", ""),
            "pmid": pmid,
            "title": v.get("title", ""),
            "journal": v.get("fulljournalname", ""),
            "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
        })
    papers = apply_floor("pubmed_recent.json", papers)
    save("pubmed_recent.json", {"updated": TODAY.isoformat(), "papers": papers})

    # --- PubMed: monthly counts, last 6 months ---
    monthly = []
    y, m = TODAY.year, TODAY.month
    for k in range(5, -1, -1):
        total = y * 12 + (m - 1) - k
        yy, mm = divmod(total, 12)
        mm += 1
        first = date(yy, mm, 1)
        last = date(yy + 1, 1, 1) - timedelta(days=1) if mm == 12 else date(yy, mm + 1, 1) - timedelta(days=1)
        _, cnt = pubmed_ids(first.isoformat(), last.isoformat(), retmax=0)
        monthly.append({"month": f"{yy}-{mm:02d}", "count": cnt})
        time.sleep(1.5)
    save("pubmed_monthly.json", {"updated": TODAY.isoformat(), "months": monthly})

    # --- meta ---
    meta = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "updated": TODAY.isoformat(),
        "counts": {
            "recruiting_global": len(t_glob),
            "denmark": len(t_dk),
            "denmark_recruiting": len(t_dkrec),
            "recent": len(t_rec),
            "pubmed_7d": len(papers),
            "pubmed_max_month": max((x["count"] for x in monthly), default=0),
        },
    }
    save("meta.json", meta)

    # --- RO-Crate manifest: FAIR packaging must follow every data change ---
    r = subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "gen_ro_crate.py")],
                       capture_output=True, text=True)
    if r.returncode != 0:
        sys.stderr.write(f"gen_ro_crate fejlede: {r.stderr}\n")
        sys.exit(1)

    # --- git: commit & push only on change, and verify the push actually landed ---
    r = git("status", "--porcelain", "--", "docs/data")
    if not r.stdout.strip():
        return  # unchanged — stay silent
    git("add", "docs/data")
    if git("commit", "-m", f"data: refresh {TODAY.isoformat()}").returncode != 0:
        sys.stderr.write("git commit fejlede\n")
        sys.exit(1)
    pull = git("pull", "--ff-only")
    if pull.returncode != 0:
        rebase = git("pull", "--rebase")
        if rebase.returncode != 0:
            # Conflicts mid-rebase: abort loudly, never leave the repo dirty.
            git("rebase", "--abort")
            sys.stderr.write(f"git pull --rebase fejlede (konflikt?): {rebase.stderr}\n")
            sys.exit(2)
    if git("push").returncode != 0:
        sys.stderr.write("git push fejlede\n")
        sys.exit(1)
    # Green run ≠ pushed: confirm HEAD is actually on origin/main (server-side).
    head = git("rev-parse", "HEAD").stdout.strip()
    ls = subprocess.run(["git", "ls-remote", "origin", "refs/heads/main"],
                        capture_output=True, text=True).stdout.strip().split()
    remote = ls[0] if ls else ""
    if not remote or head != remote:
        sys.stderr.write(f"push ikke bekræftet: HEAD {head} != origin/main {remote}\n")
        sys.exit(3)
    print(f"📊 OpenEndo: data opdateret & skubbet "
          f"({len(t_glob)} rekrutterende globalt, {len(t_dk)} i DK, {len(papers)} artikler/7d)")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        sys.stderr.write(f"FEJL i update_data.py: {e}\n")
        sys.exit(1)
