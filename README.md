# Methanimine (CH₂NH) classical trajectory ensemble — supplementary data

This repository contains machine-readable versions of Tables S1–S8 from the
provided *Supplementary Material* document, together with a copy of that source
document and a small plotting script.

## Scope

The data describe ensembles of **200 classical trajectories at each deposited
internal energy from 3 to 9 eV**, propagated over a **1000 fs** simulation
window. The repository is a structured release of the supplementary summary
tables; it is **not** a release of individual trajectory coordinates, time
series, velocities, or raw simulation input/output.

The calculations use the simplified classical interaction potential specified
in Tables S5 and S6. The source document explicitly states that these
parameters were not derived from experimental measurements of methanimine and
were not obtained through a systematic fit to *ab initio* energies and forces.
They should therefore be treated as model-defining parameters, not as
quantitatively validated electronic-structure parameters.

## Repository structure

```text
.
├── README.md
├── .gitignore
├── data/
│   ├── table_s1_fragmentation_branching_and_dissociation_times.csv
│   ├── table_s2_pathway_contributions.csv
│   ├── table_s3_energy_conservation.csv
│   ├── table_s4_representative_events.csv
│   ├── table_s5_morse_bond_parameters.csv
│   ├── table_s6_angular_potential_parameters.csv
│   ├── table_s7_hydrogen_migration_statistics.csv
│   └── table_s8_bootstrap_confidence_intervals.csv
├── metadata/
│   └── data_dictionary.md
├── scripts/
│   └── plot_supplementary_tables.py
└── source/
    └── supplementary_material_source.docx
```

## Data files

| File | Contents |
|---|---|
| `table_s1...csv` | Fragmentation branching fractions and conditional dissociation-time statistics |
| `table_s2...csv` | Rearrangement-assisted and direct fragmentation contributions |
| `table_s3...csv` | Maximum total-energy deviation statistics |
| `table_s4...csv` | Four representative fragmentation events |
| `table_s5...csv` | Morse-type bonded interaction parameters |
| `table_s6...csv` | Angular potential parameters |
| `table_s7...csv` | Hydrogen-transfer activity and rearrangement timing |
| `table_s8...csv` | Bootstrap confidence intervals for hydrogen-migration statistics |

All CSV files are UTF-8 encoded and use a comma as the field delimiter. Decimal
values use a period. Column names are descriptive and use ASCII characters
where practical. In Table S8, the two confidence-interval columns in the source
have been expanded into separate lower and upper numeric columns.

## Key definitions and interpretation

- **Branching fractions (Table S1):** calculated relative to all 200
  trajectories at the corresponding deposited energy.
- **Dissociation-time statistics (Table S1):** calculated only for trajectories
  that dissociated within the 1000 fs observation window. Non-dissociative
  trajectories are right-censored in the Kaplan–Meier analysis described in
  the manuscript.
- **Pathway classification (Table S2):** a dissociative trajectory is
  rearrangement-assisted if at least one persistent hydrogen-migration event
  occurred before the assigned dissociation time. Otherwise, it is classified
  as direct.
- **Energy conservation (Table S3):** for each trajectory, ΔEmax is the maximum
  absolute deviation of total energy from its initial value during propagation.
- **Hydrogen migration (Table S7):** migration activity statistics are based on
  the complete ensemble of 200 trajectories. Timing statistics are restricted
  to rearrangement-assisted dissociative trajectories. The migration-to-
  dissociation interval is Δt = t_diss − t_mig, where t_mig is the first
  persistent pre-dissociation migration time.
- **Bootstrap intervals (Table S8):** two-sided 95% percentile intervals from
  10,000 within-energy resamples of 200 trajectories with replacement. The
  random-generator seed reported in the source is `20261114`. These intervals
  quantify sampling uncertainty within the specified model; they do not
  establish the physical accuracy of the interaction potential.

## Reproduce summary plots

Requires Python 3.9+ and the packages listed in `requirements.txt` (create it
with `pandas` and `matplotlib`, or install them directly). Run from the
repository root:

```bash
python -m pip install pandas matplotlib
python scripts/plot_supplementary_tables.py
```

The script writes PNG figures to `figures/`. It plots selected quantities
directly from the CSV summary tables; it does not rerun the trajectory
simulations or reconstruct individual trajectories.

## Provenance and limitations

The CSV data were transcribed programmatically from the eight tables in the
provided supplementary DOCX file. The original DOCX is retained in `source/`
for comparison. The source document does not provide the raw trajectory-level
data needed to independently recalculate all ensemble statistics or reproduce
the Kaplan–Meier and bootstrap analyses from individual trajectories.

The final article title, author list, publication/DOI, and preferred citation
should be added when available; these were not inferred from the tables.

## Dataset license

The dataset tables under `data/` and associated dataset metadata and
documentation are licensed under the [Creative Commons Attribution 4.0
International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).
See [LICENSE](LICENSE) for the full legal text. Reuse requires appropriate
attribution, a link to the license, and an indication of changes.

This dataset license notice does not itself establish rights to redistribute
the original supplementary DOCX under `source/` or specify a separate software
license for the plotting script under `scripts/`.
