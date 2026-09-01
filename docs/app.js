/* Endometriosis Watch — dashboard app (EN/DA) */
"use strict";

const I18N = {
  en: {
    nav_dashboard: "Dashboard", nav_why: "Why", nav_funding: "Funding",
    nav_action: "Take action", nav_resources: "Resources",
    hero_title: "Open intelligence for a disease the world still ignores.",
    hero_sub: "Endometriosis Watch tracks clinical trials, research and funding in the open — updated weekly — so patients, relatives, researchers and politicians can see the real state of the fight.",
    sec_why_title: "Why this exists", sec_why_sub: "Four facts that should outrage everyone.",
    sec_dashboard_title: "Live research dashboard", sec_dashboard_sub: "Fresh data from ClinicalTrials.gov and PubMed — regenerated every week.",
    kpi_recruiting_global: "recruiting trials worldwide", kpi_recruiting_dk: "recruiting in Denmark",
    kpi_papers_7d: "new papers, last 7 days", kpi_funding_open: "funding opportunities open",
    chart_country_title: "Recruiting trials by country",
    chart_status_title: "All Denmark trials by status",
    chart_pubmed_title: "Endometriosis papers on PubMed (6 months)",
    tbl_global_title: "Recruiting trials — worldwide",
    tbl_denmark_title: "All registered trials — Denmark",
    tbl_papers_title: "New research — last 7 days",
    th_title: "Trial", th_status: "Status", th_phase: "Phase", th_sponsor: "Sponsor",
    th_countries: "Countries", th_date: "Date", th_journal: "Journal",
    sec_funding_title: "Funding watch", sec_funding_sub: "Deadlines that matter — grants that could change the field.",
    funding_deadline: "Deadline", funding_open: "Open", funding_closed: "Closed",
    days_left: "d left", days_overdue: "d overdue",
    sec_action_title: "Take action", sec_action_sub: "Concrete things you can do today — in Denmark and worldwide.",
    sec_resources_title: "Resources", sec_resources_sub: "Trusted places to go for help, diagnostics and knowledge.",
    footer_methodology_title: "Methodology & sources",
    footer_built: "Open source. MIT licensed — the data is a public good. Independent and unaffiliated, built for patients, researchers and policymakers.",
    footer_refreshed: "Data refreshed",
    loading: "Loading live data…", error: "Could not load data.",
    link_github: "GitHub", open: "open", status_col: "Status",
    hero_eyebrow: "Endometriosis · Open data, updated weekly",
    hero_title_1: "Open intelligence for a disease the world",
    hero_title_2: "still ignores.",
    hero_cta1: "Explore the data", hero_cta2: "Get involved",
    hero_trust_1: "No paywall", hero_trust_2: "No spin", hero_trust_3: "MIT-licensed data",
    live_badge: "Live · refreshed weekly",
    footer_tagline: "open data. real hope."
  },
  da: {
    nav_dashboard: "Dashboard", nav_why: "Hvorfor", nav_funding: "Funding",
    nav_action: "Gør noget", nav_resources: "Ressourcer",
    hero_title: "Åben intelligens for en sygdom, verden stadig ignorerer.",
    hero_sub: "Endometriosis Watch sporer kliniske forsøg, forskning og funding i det åbne — opdateret ugentligt — så patienter, pårørende, forskere og politikere kan se den reelle tilstand af kampen.",
    sec_why_title: "Hvorfor dette findes", sec_why_sub: "Fire fakta der burde oprøre alle.",
    sec_dashboard_title: "Live forsknings-dashboard", sec_dashboard_sub: "Friske data fra ClinicalTrials.gov og PubMed — genskabt hver uge.",
    kpi_recruiting_global: "rekrutterende forsøg på verdensplan", kpi_recruiting_dk: "rekrutterende i Danmark",
    kpi_papers_7d: "nye artikler, sidste 7 dage", kpi_funding_open: "åbne funding-muligheder",
    chart_country_title: "Rekrutterende forsøg fordelt på lande",
    chart_status_title: "Alle danske forsøg fordelt på status",
    chart_pubmed_title: "Endometriose-artikler på PubMed (6 måneder)",
    tbl_global_title: "Rekrutterende forsøg — verden over",
    tbl_denmark_title: "Alle registrerede forsøg — Danmark",
    tbl_papers_title: "Ny forskning — sidste 7 dage",
    th_title: "Forsøg", th_status: "Status", th_phase: "Fase", th_sponsor: "Sponsor",
    th_countries: "Lande", th_date: "Dato", th_journal: "Tidsskrift",
    sec_funding_title: "Funding-ur", sec_funding_sub: "Frister der betyder noget — bevillinger der kan ændre feltet.",
    funding_deadline: "Frist", funding_open: "Åben", funding_closed: "Lukket",
    days_left: "d tilbage", days_overdue: "d overskredet",
    sec_action_title: "Gør noget", sec_action_sub: "Konkrete ting du kan gøre i dag — i Danmark og på verdensplan.",
    sec_resources_title: "Ressourcer", sec_resources_sub: "Pålidelige steder at søge hjælp, diagnostik og viden.",
    footer_methodology_title: "Metode & kilder",
    footer_built: "Open source. MIT-licenseret — data er et fælles gode. Uafhængigt og uden tilknytning, bygget til patienter, forskere og beslutningstagere.",
    footer_refreshed: "Data opdateret",
    loading: "Henter live-data…", error: "Kunne ikke indlæse data.",
    link_github: "GitHub", open: "åben", status_col: "Status",
    hero_eyebrow: "Endometriose · Åbne data, opdateret ugentligt",
    hero_title_1: "Åben intelligens for en sygdom, verden",
    hero_title_2: "stadig ignorerer.",
    hero_cta1: "Udforsk data", hero_cta2: "Vær med",
    hero_trust_1: "Ingen betalingsmur", hero_trust_2: "Ingen spin", hero_trust_3: "MIT-licenserede data",
    live_badge: "Live · opdateret ugentligt",
    footer_tagline: "åbne data. ægte håb."
  }
};

const LANG = localStorage.getItem("endo-lang") || "en";
let charts = [];

function t(key) { return (I18N[LANG] && I18N[LANG][key]) || key; }

async function getJSON(path) {
  const r = await fetch(path, { cache: "no-store" });
  if (!r.ok) throw new Error(path + " -> " + r.status);
  return r.json();
}

function esc(s) {
  return String(s ?? "").replace(/[&<>"']/g, c => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
  }[c]));
}

function langObj(o) { return (o && (o[LANG] || o.en)) || ""; }

function applyStatic() {
  document.documentElement.lang = LANG;
  document.querySelectorAll("[data-i18n]").forEach(el => {
    el.textContent = t(el.dataset.i18n);
  });
  document.getElementById("lang-toggle").textContent = LANG === "en" ? "Dansk" : "English";
  document.title = LANG === "en"
    ? "Endometriosis Watch — open analytics on research, trials & funding"
    : "Endometriosis Watch — åben analyse af forskning, forsøg & funding";
}

/* ---------- renderers ---------- */

function renderStats(content) {
  const el = document.getElementById("stats");
  el.innerHTML = content.stats.map(s => `
    <div class="stat">
      <div class="value">${esc(s.value)}</div>
      <div class="label">${esc(langObj(s.label))}</div>
      ${s.source ? `<div class="src">${esc(s.source)}</div>` : ""}
    </div>`).join("");
}

function renderProblems(content) {
  document.getElementById("problems").innerHTML = content.problems.map(p => `
    <div class="card">
      <h4>${esc(langObj(p.title))}</h4>
      <p>${esc(langObj(p.body))}</p>
      <div class="src">Source: ${esc(p.source)}</div>
    </div>`).join("");
}

function renderActions(content) {
  document.getElementById("actions").innerHTML = content.actions.map(a => `
    <div class="card">
      <h4>${esc(langObj(a.title))}</h4>
      <p>${esc(langObj(a.body))}</p>
      <a class="cta" href="${esc(a.url)}" target="_blank" rel="noopener">${esc(langObj(a.cta))} ↗</a>
    </div>`).join("");
}

function renderResources(content) {
  document.getElementById("resources-grid").innerHTML = content.resources.map(r => `
    <div class="card">
      <span class="tag">${esc(langObj(r.tag))}</span>
      <h4>${esc(r.name)}</h4>
      <p>${esc(langObj(r.desc))}</p>
      <a class="cta" href="${esc(r.url)}" target="_blank" rel="noopener">${esc(r.url.replace(/^https?:\/\/(www\.)?/, ""))} ↗</a>
    </div>`).join("");
}

function renderKPIs(meta, funding) {
  const c = meta.counts || {};
  const openFunding = (funding || []).filter(f => f.open).length;
  document.getElementById("kpis").innerHTML = `
    <div class="kpi"><div class="n gold">${c.recruiting_global ?? "–"}</div><div class="l">${t("kpi_recruiting_global")}</div></div>
    <div class="kpi"><div class="n gold">${c.denmark_recruiting ?? "–"}</div><div class="l">${t("kpi_recruiting_dk")}</div></div>
    <div class="kpi"><div class="n">${c.pubmed_7d ?? "–"}</div><div class="l">${t("kpi_papers_7d")}</div></div>
    <div class="kpi"><div class="n">${openFunding}</div><div class="l">${t("kpi_funding_open")}</div></div>`;
}

function statusBadge(s) {
  const st = String(s || "?").replace(/_/g, " ");
  return `<span class="status ${esc(String(s || "unknown"))}">${esc(st)}</span>`;
}

function renderTrials(id, trials, withStatus) {
  const rows = trials.slice(0, withStatus ? 50 : 15).map(x => {
    const countries = (x.countries || []).slice(0, 4).join(", ") + ((x.countries || []).length > 4 ? "…" : "");
    return `<tr>
      <td><a href="${esc(x.url)}" target="_blank" rel="noopener">${esc(x.title)}</a><br><span class="nct">${esc(x.nct_id)}</span></td>
      ${withStatus ? `<td>${statusBadge(x.status)}</td>` : ""}
      <td>${esc(x.phase)}</td>
      <td>${esc(x.sponsor || "–")}</td>
      ${id === "tbl-global" ? `<td>${esc(countries)}</td>` : ""}
    </tr>`;
  }).join("");
  document.getElementById(id).innerHTML = rows || `<tr><td colspan="5" class="loading">—</td></tr>`;
}

function renderPapers(papers) {
  document.getElementById("tbl-papers").innerHTML = papers.slice(0, 10).map(p => `
    <tr>
      <td style="white-space:nowrap">${esc(p.date)}</td>
      <td><a href="${esc(p.url)}" target="_blank" rel="noopener">${esc(p.title)}</a></td>
      <td style="color:var(--muted)">${esc(p.journal)}</td>
    </tr>`).join("") || `<tr><td colspan="3" class="loading">—</td></tr>`;
}

function renderFunding(funding) {
  const now = Date.now();
  document.getElementById("funding-cards").innerHTML = funding.map(f => {
    let dl = "";
    if (f.deadline) {
      const diff = Math.ceil((new Date(f.deadline + "T23:59:59") - now) / 86400000);
      const badge = diff >= 0
        ? `<span class="days">${diff} ${t("days_left")}</span>`
        : `<span class="days" style="background:var(--crimson)">${-diff} ${t("days_overdue")}</span>`;
      dl = `<div class="deadline">${t("funding_deadline")}: ${f.deadline}${badge}</div>`;
    } else if (f.open) {
      dl = `<div class="deadline"><span class="open-now">● ${t("funding_open")}</span></div>`;
    } else {
      dl = `<div class="deadline">${t("funding_closed")}</div>`;
    }
    return `<div class="card">
      <h4>${esc(f.name)}</h4>
      <div class="src">${esc(f.org)} · ${esc(f.country)}</div>
      <p>${esc(langObj(f.desc))}</p>
      ${dl}
      <a class="cta" href="${esc(f.url)}" target="_blank" rel="noopener">${esc(f.url.replace(/^https?:\/\/(www\.)?/, ""))} ↗</a>
    </div>`;
  }).join("");
}

/* ---------- charts ---------- */

function destroyCharts() { charts.forEach(c => c.destroy()); charts = []; }

function makeChart(id, cfg) {
  if (typeof Chart === "undefined") return;
  Chart.defaults.font.family = "-apple-system,BlinkMacSystemFont,'SF Pro Display','Segoe UI',Roboto,Helvetica,Arial,sans-serif";
  Chart.defaults.font.size = 12;
  Chart.defaults.color = "#6e6e73";
  Chart.defaults.borderColor = "rgba(0,0,0,.06)";
  const ctx = document.getElementById(id);
  if (!ctx) return;
  charts.push(new Chart(ctx, cfg));
}

function renderCharts(glob, dk, monthly) {
  destroyCharts();

  const byCountry = {};
  glob.forEach(x => (x.countries || []).forEach(c => { byCountry[c] = (byCountry[c] || 0) + 1; }));
  const countryTop = Object.entries(byCountry).sort((a, b) => b[1] - a[1]).slice(0, 12);

  const byStatus = {};
  dk.forEach(x => { byStatus[x.status || "UNKNOWN"] = (byStatus[x.status || "UNKNOWN"] || 0) + 1; });

  const palette = ["#0071e3", "#34c759", "#ff375f", "#af52de", "#ff9f0a", "#5ac8fa", "#ffd60a", "#8e8e93"];

  makeChart("chart-country", {
    type: "bar",
    data: { labels: countryTop.map(c => c[0]), datasets: [{ data: countryTop.map(c => c[1]), backgroundColor: "#0071e3", borderRadius: 6, maxBarThickness: 34 }] },
    options: { plugins: { legend: { display: false } }, scales: { y: { beginAtZero: true, ticks: { stepSize: 1 } } } }
  });

  makeChart("chart-status", {
    type: "doughnut",
    data: { labels: Object.keys(byStatus), datasets: [{ data: Object.values(byStatus), backgroundColor: palette, borderWidth: 2, borderColor: "#ffffff" }] },
    options: { plugins: { legend: { position: "right", labels: { color: "#6e6e73", boxWidth: 12, padding: 14 } } } }
  });

  makeChart("chart-pubmed", {
    type: "line",
    data: { labels: monthly.map(m => m.month), datasets: [{ data: monthly.map(m => m.count), borderColor: "#0071e3", backgroundColor: "rgba(0,113,227,0.10)", fill: true, tension: 0.32, pointBackgroundColor: "#0071e3", pointRadius: 3, borderWidth: 2.5 }] },
    options: { plugins: { legend: { display: false } }, scales: { y: { beginAtZero: true, ticks: { stepSize: 1 } } } }
  });
}

function renderFreshness(meta) {
  const el = document.getElementById("freshness");
  el.innerHTML = `${t("footer_refreshed")}: <b>${esc(meta.updated || "–")}</b> (${esc(meta.generated_at || "")} UTC) · ` +
    `<a href="https://github.com/wckdboy/openendo" target="_blank" rel="noopener" style="color:var(--link)">github.com/wckdboy/openendo ↗</a>`;
}

/* ---------- boot ---------- */

async function load() {
  document.getElementById("methodology").textContent = t("loading");
  try {
    const [meta, glob, dk, recent, papers, monthly, funding, content] = await Promise.all([
      getJSON("data/meta.json"),
      getJSON("data/trials_global_recruiting.json"),
      getJSON("data/trials_denmark.json"),
      getJSON("data/trials_recent.json"),
      getJSON("data/pubmed_recent.json"),
      getJSON("data/pubmed_monthly.json"),
      getJSON("data/funding.json"),
      getJSON("data/content.json"),
    ]);

    renderStats(content);
    renderProblems(content);
    renderKPIs(meta, funding);
    renderTrials("tbl-global", glob.trials, false);
    renderTrials("tbl-denmark", dk.trials, true);
    renderPapers(papers.papers);
    renderFunding(funding);
    renderActions(content);
    renderResources(content);
    renderCharts(glob.trials, dk.trials, monthly.months);
    renderFreshness(meta);
    document.getElementById("methodology").textContent = langObj(content.methodology);
  } catch (e) {
    console.error(e);
    document.getElementById("methodology").textContent = t("error") + " " + e.message;
  }
}

document.getElementById("lang-toggle").addEventListener("click", () => {
  localStorage.setItem("endo-lang", LANG === "en" ? "da" : "en");
  location.reload();
});

applyStatic();
load();
