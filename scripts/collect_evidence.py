#!/usr/bin/env python3
"""collect_evidence.py — M2 v1: weekly living-evidence collector.

Pulls the last 7 days of endometriosis literature (PubMed + Europe PMC),
writes a structured weekly snapshot for agent synthesis into the evidence
map. Aligns with the OpenEndo agenda track "Living evidence synthesis".

Output: docs/research/evidence/weekly/<YYYY-MM-DD>.json
        docs/research/evidence/weekly/LATEST (pointer file)

Usage: python3 scripts/collect_evidence.py
"""
import json
import os
import sys
import time
import urllib.parse
import urllib.request
from datetime import date, timedelta

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "docs", "research", "evidence", "weekly")
UA = {"User-Agent": "openendo/1.0 (github.com/wckdboy/openendo; evidence)"}
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
TODAY = date.today()
WEEK = TODAY - timedelta(days=7)


def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode()


def pubmed_ids():
    q = urllib.parse.quote("endometriosis[Title/Abstract]")
    url = (f"{EUTILS}/esearch.fcgi?db=pubmed&term={q}"
           f"&datetype=pdat&mindate={WEEK.isoformat()}&maxdate={TODAY.isoformat()}"
           f"&retmax=20&retmode=json")
    d = json.loads(fetch(url))
    return d.get("esearchresult", {}).get("idlist", [])


def pubmed_summary(ids):
    if not ids:
        return {}
    url = (f"{EUTILS}/esummary.fcgi?db=pubmed&id={','.join(ids)}&retmode=json")
    return json.loads(fetch(url)).get("result", {})


def pubmed_abstract(pmid):
    url = (f"{EUTILS}/efetch.fcgi?db=pubmed&id={pmid}&rettype=abstract"
           f"&retmode=text")
    txt = fetch(url)
    return txt[:3000]


def epmc_recent():
    q = urllib.parse.quote(
        f'(TITLE:"endometriosis" OR ABSTRACT:"endometriosis") '
        f'AND PUB_DATE:[{WEEK.strftime("%Y-%m-%d")} TO {TODAY.strftime("%Y-%m-%d")}]')
    url = (f"{EPMC}?query={q}&format=json&pageSize=10")
    d = json.loads(fetch(url))
    out = []
    for r in (d.get("resultList", {}).get("result", []) or []):
        out.append({"pmid": r.get("pmid", ""), "title": r.get("title", ""),
                    "journal": r.get("journalTitle", ""),
                    "pubdate": r.get("pubYear", ""),
                    "doi": r.get("doi", ""),
                    "abstract": (r.get("abstractText") or "")[:3000],
                    "source": "EuropePMC"})
    return out


def main():
    os.makedirs(OUT, exist_ok=True)
    ids = pubmed_ids()
    summ = pubmed_summary(ids)
    papers = []
    for pmid in ids:
        v = summ.get(pmid, {})
        papers.append({"pmid": pmid,
                       "title": v.get("title", ""),
                       "journal": v.get("fulljournalname", ""),
                       "pubdate": v.get("pubdate", ""),
                       "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
                       "source": "PubMed"})
    # abstracts for the newest few (agent synthesis material)
    for p in papers[:5]:
        try:
            p["abstract"] = pubmed_abstract(p["pmid"])
        except Exception:
            p["abstract"] = ""
        time.sleep(0.5)

    papers += epmc_recent()
    # dedupe by pmid
    seen, uniq = set(), []
    for p in papers:
        k = p.get("pmid") or p.get("doi")
        if k and k not in seen:
            seen.add(k)
            uniq.append(p)
    uniq.sort(key=lambda x: x.get("pubdate", ""), reverse=True)

    snap = {"period": f"{WEEK.isoformat()}..{TODAY.isoformat()}",
            "collected": TODAY.isoformat(),
            "papers": uniq}
    fn = TODAY.isoformat() + ".json"
    with open(os.path.join(OUT, fn), "w", encoding="utf-8") as f:
        json.dump(snap, f, ensure_ascii=False, indent=1)
    with open(os.path.join(OUT, "LATEST"), "w") as f:
        f.write(fn)

    print(f"Uge {WEEK.isoformat()}..{TODAY.isoformat()}: "
          f"{len(uniq)} artikler -> {fn}")
    for p in uniq[:10]:
        print(f"  - {p.get('pubdate','')} {p.get('title','')[:70]}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        sys.stderr.write(f"FEJL i collect_evidence.py: {e}\n")
        sys.exit(1)
