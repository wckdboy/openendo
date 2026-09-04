#!/usr/bin/env python3
"""GSE263897 GeoMx DSP reanalysis — FKBP4 / MRGPRX2 / SLC7A11 in endo lesions vs eutopic.

NanoString GeoMx digital spatial profiling, Human WTA v1.0 (GPL24676).
Superficial peritoneal endometriotic lesions vs patient-matched eutopic
endometrium, 5 women (secretory phase), 10 tissues, duplicate ROIs,
3 fluorescence-segmented compartments per ROI (Epithelium panCK+ /
Macrophages CD68+ / Stroma pan-negative) = 60 segments.

Pipeline: DCC parse -> RTS->gene map (PKC) -> segment QC (negative
probes, compartment-marker presence) -> Q3 normalisation (75th pct of
segment probe counts) -> log2 -> patient-paired lesion vs eutopic per
compartment (per-patient mean over duplicate ROIs; n=5 -> directional
evidence only, no formal test).

Why this dataset matters for Phase 0.5: GeoMx probes hybridise in situ
-- no 10x dropout -- so a low-expression receptor (MRGPRX2) on a rare
cell type (mast cells) is detectable IF present. GSE247695 (scRNA) left
the peritoneal-lesion mast-cell question open (KIT+ not enriched, but
dropout regime); GSE263897 is the dropout-free single-dataset check.

Usage: python3 gse263897_analysis.py <data_dir> <out_dir>
  data_dir: dir with dcc/ (GSM*_*.dcc.gz) + pkc/Hs_R_NGS_WTA_v1.0.pkc + sample_sheet.json
"""
import gzip, json, os, re, sys
import numpy as np

TARGETS = ["FKBP4", "MRGPRX2", "SLC7A11", "GPX4", "ACSL4"]
MAST = ["KIT", "CPA3", "TPSAB1", "MS4A2", "FCER1A", "MRGPRX2"]
SEG_MARKER = {  # one canonical marker per compartment for segment QC
    "Epithelium": "EPCAM", "Macrophages": "CD68", "Stroma": "DCN",
}
EXTRA = ["C3", "PTPRC", "ACTA2", "VWF", "PECAM1", "RGS5", "CD3D", "MS4A1", "NKG7",
         "KRT18", "LYZ", "COL1A1", "CD163"]
GENES_OF_INTEREST = list(dict.fromkeys(TARGETS + MAST + EXTRA))
COMPARTMENTS = ["Epithelium", "Macrophages", "Stroma"]


def parse_dcc(path):
    counts = {}
    with gzip.open(path, "rt", errors="replace") as fh:
        for line in fh:
            m = re.match(r"^(RTS\d+),(\d+)$", line.strip())
            if m:
                counts[m.group(1)] = int(m.group(2))
    return counts


def load_pkc(pkc_path):
    pkc = json.load(open(pkc_path))
    rts2gene, neg = {}, []
    for t in pkc["Targets"]:
        cc = str(t.get("CodeClass", ""))
        for p in t.get("Probes", []):
            rid = p.get("RTS_ID")
            if rid:
                rts2gene[rid] = t["DisplayName"]
                if "Negative" in cc:
                    neg.append(rid)
    return rts2gene, neg


def main():
    data_dir, out_dir = sys.argv[1], sys.argv[2]
    os.makedirs(out_dir, exist_ok=True)
    rts2gene, neg_rts = load_pkc(os.path.join(data_dir, "pkc", "Hs_R_NGS_WTA_v1.0.pkc"))
    neg_set = set(neg_rts)
    print(f"PKC: {len(rts2gene)} RTS -> {len(set(rts2gene.values()))} genes; {len(neg_rts)} neg probes")

    sheet = json.load(open(os.path.join(data_dir, "sample_sheet.json")))
    segs = {s["geo_accession"]: s for s in sheet}
    dcc_dir = os.path.join(data_dir, "dcc")

    matrix, seg_meta, seg_ng = {}, {}, {}   # gene->{gsm:count}, gsm->meta, gsm->neg geomean
    for fn in sorted(os.listdir(dcc_dir)):
        if not fn.endswith(".dcc.gz"):
            continue
        gsm = fn.split("_")[0]
        if gsm not in segs:
            print("!! no metadata for", gsm)
            continue
        counts = parse_dcc(os.path.join(dcc_dir, fn))
        gc, negs = {}, []
        for rid, c in counts.items():
            g = rts2gene.get(rid)
            if g:
                gc[g] = gc.get(g, 0) + c
                if rid in neg_set:
                    negs.append(c)
        seg_ng[gsm] = float(np.exp(np.mean(np.log(np.array(negs) + 1)))) if len(negs) >= 3 else float("nan")
        seg_meta[gsm] = segs[gsm]
        for g, c in gc.items():
            matrix.setdefault(g, {})[gsm] = c
    gsms = sorted(seg_meta.keys())
    genes_all = sorted(matrix.keys())
    M = np.array([[matrix[g].get(gsm, 0) for gsm in gsms] for g in genes_all])
    print(f"segments: {len(gsms)}  matrix: {M.shape}")

    # ---- segment QC ----
    tot = M.sum(axis=0)
    q3 = np.percentile(M, 75, axis=0)
    ng = np.array([seg_ng[g] for g in gsms])
    seg_ids = np.array(gsms)
    print("\n== segment QC (tot / Q3 / neg-geomean) ==")
    print(f"  raw total endogenous: min {tot.min():.0f}  median {np.median(tot):.0f}  max {tot.max():.0f}")
    print(f"  neg-probe geomean   : min {np.nanmin(ng):.1f}  median {np.nanmedian(ng):.1f}  max {np.nanmax(ng):.1f}")
    # sparse segments: compartment marker not above 2x its segment's neg geomean
    sparse = []
    for i, gsm in enumerate(gsms):
        marker = SEG_MARKER[seg_meta[gsm]["celltype"]]
        if marker in matrix and matrix[marker].get(gsm, 0) <= 2 * ng[i]:
            sparse.append((gsm, seg_meta[gsm]["title"], int(tot[i]), round(float(ng[i]), 1),
                           int(matrix[marker].get(gsm, 0))))
    print(f"  sparse segments (compartment marker <= 2x neg-geomean): {len(sparse)}")
    for r in sparse:
        print(f"    {r[0]} {r[1]:38s} tot={r[2]:7d} ng={r[3]:4.1f} marker={r[4]}")

    # ---- normalise: Q3 (GeoMx standard), then log2 ----
    Mn = M / q3[np.newaxis, :]
    L = np.log2(Mn + 1)

    def tissue(m): return "lesion" if "lesion" in m["tissue"] else "eutopic"

    def gene_idx(g): return genes_all.index(g)

    def paired_summary(gene, celltype):
        gi = gene_idx(gene)
        per_pat = {}
        for gsm, meta in zip(gsms, [seg_meta[g] for g in gsms]):
            if meta["celltype"] != celltype:
                continue
            per_pat.setdefault(meta["sampleID"], {}).setdefault(tissue(meta), []).append(L[gi, gsms.index(gsm)])
        pairs = {p: (np.mean(v["eutopic"]), np.mean(v["lesion"]))
                 for p, v in per_pat.items() if "lesion" in v and "eutopic" in v}
        if len(pairs) < 4:
            return None
        eu = np.mean([v[0] for v in pairs.values()])
        le = np.mean([v[1] for v in pairs.values()])
        d = le - eu
        same = sum(1 for v in pairs.values() if (v[1] - v[0]) * d > 0)
        return {
            "gene": gene, "compartment": celltype, "n_patients": len(pairs),
            "eutopic_mean_log2q3": round(float(eu), 3),
            "lesion_mean_log2q3": round(float(le), 3),
            "delta_log2_lesion_minus_eutopic": round(float(d), 3),
            "fold_change_lesion_over_eutopic": round(float(2 ** d), 2),
            "patients_matching_direction": f"{same}/{len(pairs)}",
            "per_patient_delta_log2": {p: round(float(v[1] - v[0]), 3) for p, v in pairs.items()},
        }

    # above-background check: mean raw count / mean neg geomean per tissue+compartment
    def background_ratio(gene, celltype):
        gi = gene_idx(gene)
        out = {}
        for cond in ("eutopic", "lesion"):
            idx = [i for i, gsm in enumerate(gsms)
                   if seg_meta[gsm]["celltype"] == celltype and tissue(seg_meta[gsm]) == cond]
            if not idx:
                continue
            out[cond] = {"mean_raw": round(float(np.mean(M[gi, idx])), 2),
                         "mean_neg_geomean": round(float(np.mean(ng[idx])), 2),
                         "ratio_raw_to_background": round(float(np.mean(M[gi, idx]) / np.mean(ng[idx])), 2)}
        return out

    out = {"dataset": "GSE263897",
           "platform": "NanoString GeoMx DSP, Human WTA v1.0 (GPL24676); PKC Hs_R_NGS_WTA_v1.0",
           "design": "5 women (secretory phase), patient-matched eutopic endometrium vs superficial "
                     "peritoneal endometriotic lesion, duplicate ROIs, 3 segments per ROI "
                     "(Epithelium panCK+ / Macrophages CD68+ / Stroma pan-negative) = 60 segments",
           "n_segments": len(gsms),
           "analysis": "DCC raw counts -> Q3 normalisation (75th pct of segment probe counts) -> log2; "
                       "per-patient mean over duplicate ROIs; paired lesion vs eutopic; n=5 -> "
                       "directional evidence only (no formal test, consistent with GSE282532/GSE247695)",
           "qc": {"neg_probe_geomean": {"min": round(float(np.nanmin(ng)), 2),
                                        "median": round(float(np.nanmedian(ng)), 2),
                                        "max": round(float(np.nanmax(ng)), 2)},
                  "sparse_segments": [{"gsm": r[0], "title": r[1], "total_raw": r[2],
                                       "neg_geomean": r[3], "marker_raw": r[4]} for r in sparse]},
           "results": {}}

    for g in GENES_OF_INTEREST:
        if g not in matrix:
            out["results"][g] = {"on_panel": False}
            continue
        r = {"on_panel": True}
        for ct in COMPARTMENTS:
            s = paired_summary(g, ct)
            if s:
                r[ct] = s
        out["results"][g] = r

    out["background_context"] = {}
    for g in TARGETS + MAST:
        if g in matrix:
            out["background_context"][g] = {ct: background_ratio(g, ct) for ct in COMPARTMENTS}

    with open(os.path.join(out_dir, "gse263897_targets.json"), "w") as f:
        json.dump(out, f, indent=1, default=str)
    print("\nwrote", os.path.join(out_dir, "gse263897_targets.json"))

    print("\n=== HEADLINES (lesion vs eutopic; log2-Q3; patient-paired) ===")
    for g in TARGETS:
        r = out["results"][g]
        if not r.get("on_panel"):
            print(f"  {g}: NOT on panel")
            continue
        for ct in COMPARTMENTS:
            s = r.get(ct)
            if s:
                bc = out["background_context"][g][ct]
                print(f"  {g:9s} {ct:11s} d={s['delta_log2_lesion_minus_eutopic']:+.2f} "
                      f"FC={s['fold_change_lesion_over_eutopic']:.2f} {s['patients_matching_direction']} "
                      f"(bg-ratio eu/les {bc['eutopic']['ratio_raw_to_background']}/{bc['lesion']['ratio_raw_to_background']})")
    print("\n=== MAST SIGNATURE (Stroma = the pan-negative niche mast cells fall in) ===")
    for g in MAST:
        s = out["results"].get(g, {}).get("Stroma")
        if s:
            bc = out["background_context"][g]["Stroma"]
            print(f"  {g:9s} eu={s['eutopic_mean_log2q3']:5.2f} les={s['lesion_mean_log2q3']:5.2f} "
                  f"d={s['delta_log2_lesion_minus_eutopic']:+.2f} {s['patients_matching_direction']} "
                  f"(bg-ratio {bc['eutopic']['ratio_raw_to_background']}/{bc['lesion']['ratio_raw_to_background']})")
    print("\n=== C3 (study headline: lesion-epithelium complement signalling) ===")
    for ct in COMPARTMENTS:
        s = out["results"].get("C3", {}).get(ct)
        if s:
            print(f"  C3 {ct:11s} eu={s['eutopic_mean_log2q3']:5.2f} les={s['lesion_mean_log2q3']:5.2f} "
                  f"d={s['delta_log2_lesion_minus_eutopic']:+.2f} FC={s['fold_change_lesion_over_eutopic']:.2f} "
                  f"{s['patients_matching_direction']}")


if __name__ == "__main__":
    main()
