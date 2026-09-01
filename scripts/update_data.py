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
          "protocolSection.contactsLocationsModule.locations.country")


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


def trials_from(data, n=999):
    out = []
    for s in (data.get("studies") or [])[:n]:
        p = s.get("protocolSection", {})
        ident = p.get("identificationModule", {})
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
    return out


def ctg(query, params):
    url = ("https://clinicaltrials.gov/api/v2/studies?query.term="
           + urllib.parse.quote(query) + "&" + params
           + "&pageSize=50&fields=" + urllib.parse.quote(FIELDS))
    return fetch(url)


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
    with open(os.path.join(DATA, name), "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)


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

    # --- git: commit & push only on change ---
    r = git("status", "--porcelain", "--", "data")
    if not r.stdout.strip():
        return  # unchanged — stay silent
    git("add", "data")
    git("commit", "-m", f"data: refresh {TODAY.isoformat()}")
    pull = git("pull", "--ff-only")
    if pull.returncode != 0:
        git("pull", "--rebase")
    if git("push").returncode != 0:
        sys.stderr.write("git push fejlede\n")
        sys.exit(1)
    print(f"📊 Endometriosis Watch: data opdateret & skubbet "
          f"({len(t_glob)} rekrutterende globalt, {len(t_dk)} i DK, {len(papers)} artikler/7d)")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        sys.stderr.write(f"FEJL i update_data.py: {e}\n")
        sys.exit(1)
