#!/usr/bin/env python3
"""Generate descriptive plots from the supplementary CSV summary tables.

Run from the repository root:
    python scripts/plot_supplementary_tables.py
This script visualizes published summary values; it does not rerun simulations.
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "figures"
OUT.mkdir(exist_ok=True)

def load(pattern):
    return pd.read_csv(DATA / pattern)

def save_line(x, ys, labels, ylabel, filename, markers="o"):
    fig, ax = plt.subplots()
    for y, label in zip(ys, labels):
        ax.plot(x, y, marker=markers, label=label)
    ax.set_xlabel("Deposited internal energy (eV)")
    ax.set_ylabel(ylabel)
    if len(labels) > 1:
        ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(OUT / filename, dpi=300)
    plt.close(fig)

s1 = load("table_s1_fragmentation_branching_and_dissociation_times.csv")
x = s1.iloc[:, 0]
save_line(x, [s1["H loss fraction"], s1["Backbone fraction"],
              s1["Non-dissociative fraction"]],
          ["H loss", "Backbone fragmentation", "Non-dissociative"],
          "Fraction of trajectories", "fig_s1_branching_fractions.png")

save_line(x, [s1["Mean dissociation time (fs)"],
              s1["Median dissociative time (fs)"]],
          ["Mean", "Median"], "Dissociation time (fs)",
          "fig_s1_dissociation_times.png")

s2 = load("table_s2_pathway_contributions.csv")
save_line(s2.iloc[:, 0],
          [s2.iloc[:, 1], s2.iloc[:, 2]],
          ["Rearrangement-assisted", "Direct"],
          "Fraction of dissociative trajectories", "fig_s2_pathway_contributions.png")

s3 = load("table_s3_energy_conservation.csv")
save_line(s3.iloc[:, 0],
          [s3.iloc[:, 1], s3.iloc[:, 2]],
          ["Mean maximum deviation", "Largest maximum deviation"],
          "Maximum total-energy deviation (eV)", "fig_s3_energy_conservation.png")

s7 = load("table_s7_hydrogen_migration_statistics.csv")
save_line(s7.iloc[:, 0],
          [s7["Fraction with persistent H migration"]],
          ["Persistent H migration"], "Fraction of all trajectories",
          "fig_s7_hydrogen_migration_fraction.png")

s8 = load("table_s8_bootstrap_confidence_intervals.csv")
fig, ax = plt.subplots()
xx = s8.iloc[:, 0].astype(float)
yy = s8["fraction_with_persistent_H_migration"]
lo = yy - s8["fraction_CI95_lower"]
hi = s8["fraction_CI95_upper"] - yy
ax.errorbar(xx, yy, yerr=[lo, hi], marker="o", capsize=3)
ax.set_xlabel("Deposited internal energy (eV)")
ax.set_ylabel("Fraction with persistent H migration")
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(OUT / "fig_s8_bootstrap_fraction_ci.png", dpi=300)
plt.close(fig)

print(f"Figures written to: {OUT}")
