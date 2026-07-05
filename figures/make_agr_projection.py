#!/usr/bin/env python3
"""
Figure: AGR agreement projection (COCA), illustrating corpus-rate-per-opportunity
as an estimator of C_t. Real KWIC-filtered data with Wilson 95% intervals.

Source: subprojects/evolutionary-dag-workbench/data/agr-coca-projection/uncertainty-summary.csv
Reproducible: python3 figures/make_agr_projection.py
"""
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path("/Users/brettreynolds/projects/LLM-CLI-projects/.house-style")))
import plot_style
import matplotlib.pyplot as plt

plot_style.setup()

CSV = Path(__file__).resolve().parents[1] / "subprojects/evolutionary-dag-workbench/data/agr-coca-projection/uncertainty-summary.csv"

# Human-readable labels, top-to-bottom in reading order
LABELS = {
    "animate_bunch_exact":       r"$\mathit{a\ bunch\ of}\;+\;\mathrm{animate\ pl.}$",
    "majority_exact":            r"$\mathit{the\ majority}\;+\;\mathrm{set\ (exact)}$",
    "majority_audit_augmented":  r"$\mathit{the\ majority}\;+\;\mathrm{set\ (audited)}$",
    "rest_people_exact":         r"$\mathit{the\ rest\ of\ the\ people}$",
}

rows = []
with open(CSV, newline="") as f:
    for r in csv.DictReader(f):
        rows.append(r)

# Preserve CSV order; plot bottom-up so first row sits at top
rows = list(reversed(rows))
ys = list(range(len(rows)))
shares = [float(r["plural_share"]) for r in rows]
los = [float(r["wilson_95_low"]) for r in rows]
his = [float(r["wilson_95_high"]) for r in rows]
labels = [LABELS.get(r["summary_id"], r["summary_id"]) for r in rows]
ns = [int(r["total_target_rows"]) for r in rows]

fig, ax = plt.subplots(figsize=(6.2, 2.9))

# Parity reference (no directional preference)
ax.axvline(0.5, color=plot_style.COLORS["dark"], lw=0.8, ls="--", zorder=1)
ax.text(0.5, len(rows) - 0.35, "parity", color=plot_style.COLORS["dark"],
        fontsize=8, ha="center", va="bottom")

for y, s, lo, hi in zip(ys, shares, los, his):
    ax.plot([lo, hi], [y, y], color=plot_style.COLORS["primary"], lw=2, solid_capstyle="round", zorder=2)
    ax.plot([s], [y], "o", color=plot_style.COLORS["primary"], ms=6, zorder=3)

ax.set_yticks(ys)
ax.set_yticklabels([f"{lab}\n($n$={n})" for lab, n in zip(labels, ns)], fontsize=8.5)
ax.set_xlim(0, 1)
ax.set_xlabel("Plural-agreement share (KWIC-filtered), Wilson 95% interval")
ax.set_ylim(-0.6, len(rows) - 0.2)
plot_style.remove_spines(ax)

fig.tight_layout()
plot_style.save_figure(fig, str(Path(__file__).resolve().parent / "fig_agr_projection"))
