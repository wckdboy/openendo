#!/usr/bin/env python3
"""GSE247695 reanalysis — FKBP4 / MRGPRX2 / SLC7A11 in endo lesions vs eutopic.

scRNA-seq, paired eutopic (E) vs peritoneal lesion (P) endometrium, 4
patients (002/398/421/432). Pipeline: 10x load -> QC -> normalize -> PCA
-> Leiden -> marker-based cell typing -> per-cell-type target expression
by condition. Output: JSON + printed summary.

Usage: python3 gse247695_analysis.py <data_dir> <out_dir>
"""
import json
import os
import sys

import scanpy as sc
import numpy as np
import pandas as pd

sc.settings.verbosity = 1

TARGETS = ["FKBP4", "MRGPRX2", "SLC7A11"]
MAST = ["CPA3", "TPSAB1", "MS4A2", "KIT", "FCER1A"]

MARKERS = {
    "Epithelial": ["EPCAM", "KRT18", "KRT8", "CD24"],
    "Stromal": ["DCN", "COL1A1", "LUM", "PDPN"],
    "Endothelial": ["PECAM1", "VWF", "CLDN5"],
    "Perivascular": ["RGS5", "ACTA2", "NOTCH3"],
    "T cells": ["CD3D", "CD3E", "IL7R"],
    "NK cells": ["NKG7", "GNLY", "KLRD1"],
    "B cells": ["MS4A1", "CD79A"],
    "Macrophage/Mono": ["LYZ", "CD68", "C1QB", "FCGR3A"],
    "Mast cells": ["CPA3", "TPSAB1", "MS4A2", "KIT"],
}


def load_samples(data_dir):
    import gzip
    from scipy.io import mmread
    import pandas as pd

    def read_tsv(path, header=None):
        return pd.read_csv(path, header=header, sep="\t")

    adatas = []
    for f in sorted(os.listdir(data_dir)):
        if not f.endswith("matrix.mtx.gz"):
            continue
        prefix = f[: -len("_matrix.mtx.gz")]  # GSM..._E_002_1
        bc_path = os.path.join(data_dir, prefix + "_barcodes.tsv.gz")
        fe_path = os.path.join(data_dir, prefix + "_features.tsv.gz")
        mx_path = os.path.join(data_dir, f)
        barcodes = read_tsv(bc_path)[0].astype(str).tolist()
        feats = read_tsv(fe_path)
        # 10x v2: 1 col (id); v3: 3 cols (id, name, type) -> prefer name col
        names = feats[1].astype(str).tolist() if feats.shape[1] >= 2 else feats[0].astype(str).tolist()
        with gzip.open(mx_path, "rt") as fh:
            mtx = mmread(fh).tocsr().T  # genes x cells -> cells x genes
        ad = sc.AnnData(X=mtx,
                        obs=pd.DataFrame(index=barcodes),
                        var=pd.DataFrame(index=names))
        parts = prefix.split("_")  # GSM <gsm> <cond=E|P> <patient> <n>
        ad.obs["sample"] = prefix
        ad.obs["condition"] = "lesion" if parts[1] == "P" else "eutopic"
        ad.obs["patient"] = parts[2]
        ad.var_names_make_unique()
        adatas.append(ad)
        print(f"  {prefix}: {ad.n_obs} celler, {ad.n_vars} gener")
    ad = sc.concat(adatas, join="outer")
    ad.obs["condition"] = ad.obs["condition"].astype("category")
    return ad


def qc(ad):
    ad.var_names_make_unique()
    ad.obs_names_make_unique()
    ad.var["mt"] = ad.var_names.str.startswith("MT-")
    sc.pp.calculate_qc_metrics(ad, qc_vars=["mt"], inplace=True, percent_top=None)
    sc.pp.filter_cells(ad, min_genes=200)
    sc.pp.filter_genes(ad, min_cells=3)
    if ad.var["mt"].any():
        ad._inplace_subset_obs(ad.obs["pct_counts_mt"] < 20)
    return ad


def main():
    data_dir, out_dir = sys.argv[1], sys.argv[2]
    os.makedirs(out_dir, exist_ok=True)
    print("Indlæser prøver...")
    ad = load_samples(data_dir)
    print(f"Samlet: {ad.n_obs} celler x {ad.n_vars} gener")
    print(f"  conditioner: {dict(ad.obs['condition'].value_counts())}")
    print(f"  patienter: {sorted(ad.obs['patient'].unique())}")

    qc(ad)
    print(f"Efter QC: {ad.n_obs} celler")

    sc.pp.normalize_total(ad, target_sum=1e4)
    sc.pp.log1p(ad)
    ad_expr = ad.copy()  # unscaled log1p copy for expression queries
    sc.pp.highly_variable_genes(ad, n_top_genes=2000)
    sc.pp.scale(ad, max_value=10)
    sc.tl.pca(ad, svd_solver="arpack")
    sc.pp.neighbors(ad, n_neighbors=15)
    sc.tl.leiden(ad, resolution=0.8, flavor="igraph", n_iterations=2)

    # cell typing: score each cluster by marker overlap
    ad.obs["celltype"] = "Unknown"
    for ct, genes in MARKERS.items():
        present = [g for g in genes if g in ad.var_names]
        if present:
            sc.tl.score_genes(ad, present, score_name=f"score_{ct}")
    score_cols = [f"score_{ct}" for ct in MARKERS if f"score_{ct}" in ad.obs]
    for cl in ad.obs["leiden"].unique():
        sub = ad.obs[ad.obs["leiden"] == cl]
        if score_cols:
            best = sub[score_cols].mean().idxmax().replace("score_", "")
            ad.obs.loc[ad.obs["leiden"] == cl, "celltype"] = best

    print("\nCell-type sammensætning:")
    print(ad.obs.groupby(["celltype", "condition"], observed=True).size().unstack(fill_value=0))

    # target expression per celltype x condition (on UNSCALED log1p data)
    ad_expr.obs["celltype"] = ad.obs["celltype"].values  # sync annotations
    out = {"dataset": "GSE247695", "targets": {}, "mast_cells": {}}
    for g in TARGETS + MAST:
        if g not in ad_expr.var_names:
            out["targets"][g] = {"not_detected": True}
            continue
        rows = {}
        for ct in ad_expr.obs["celltype"].unique():
            for cond in ["eutopic", "lesion"]:
                mask = (ad_expr.obs["celltype"] == ct) & (ad_expr.obs["condition"] == cond)
                n = mask.sum()
                if n < 5:
                    continue
                expr = ad_expr[mask, g].X
                if hasattr(expr, "toarray"):
                    expr = expr.toarray().flatten()
                rows[f"{ct}|{cond}"] = {
                    "cells": int(n),
                    "mean_log1p": round(float(np.mean(expr)), 3),
                    "frac_detected": round(float(np.mean(expr > 0)), 3),
                }
        out["targets"][g] = rows

    # headline: mast-cell MRGPRX2 (lesion vs eutopic)
    mc = ad_expr[ad_expr.obs["celltype"] == "Mast cells"]
    if mc.n_obs > 0:
        for g in ["MRGPRX2", "CPA3", "TPSAB1"]:
            if g not in mc.var_names:
                continue
            vals = {}
            for cond in ["eutopic", "lesion"]:
                m = mc.obs["condition"] == cond
                e = mc[m, g].X
                if hasattr(e, "toarray"):
                    e = e.toarray().flatten()
                vals[cond] = {"cells": int(m.sum()),
                              "mean_log1p": round(float(np.mean(e)), 3),
                              "frac": round(float(np.mean(e > 0)), 3)}
            out["mast_cells"][g] = vals

    with open(os.path.join(out_dir, "gse247695_targets.json"), "w") as f:
        json.dump(out, f, indent=1, default=str)

    print("\n=== HOVEDLINJER ===")
    for g in TARGETS:
        if g not in ad.var_names:
            print(f"  {g}: ikke detekteret i datasættet")
            continue
        for key, v in out["targets"][g].items():
            if "Mast cells|" in key or "Stromal|" in key or "Epithelial|" in key:
                ct, cond = key.split("|")
                print(f"  {g:9s} {ct:13s} {cond:7s} mean={v['mean_log1p']:6.2f} frac={v['frac_detected']}")
    print("\n  Mastcelle-MRGPRX2:", json.dumps(out.get("mast_cells", {}).get("MRGPRX2", "ingen mastceller")))

    print(f"\nWrote {out_dir}/gse247695_targets.json")


if __name__ == "__main__":
    main()
