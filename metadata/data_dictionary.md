# Data dictionary and source notes

## General conventions

- Energy: deposited internal energy in eV.
- Time: femtoseconds (fs).
- Fractions: dimensionless proportions in the interval [0, 1].
- `ntraj`: number of trajectories in the energy ensemble (200 at each energy).
- `Ndiss`: number of trajectories dissociating within the 1000 fs observation window.

## Table-specific notes

### S1 — Fragmentation and dissociation times
`H loss fraction`, `Backbone fraction`, and `Non-dissociative fraction` are
fractions of the complete ensemble. Mean, median, and standard deviation of
dissociation time are conditional on observed dissociation.

### S2 — Pathway contributions
Fractions are calculated only among dissociative trajectories. Rearrangement-
assisted means at least one persistent H migration before dissociation;
otherwise the pathway is direct.

### S3 — Energy conservation
`Mean ΔEmax` is the ensemble average of trajectory-level maximum absolute
total-energy deviations. `Largest ΔEmax` is the largest such value in the
energy ensemble.

### S4 — Representative events
Four selected events are illustrative examples, not a statistically complete
sample of the ensembles.

### S5 — Morse-type bonded interactions
Columns contain interaction label, dissociation energy De (eV), equilibrium
distance re (Å), and inverse-length parameter a (Å⁻¹). Identical parameter
sets were applied to the atom-label groups described in the source note.

### S6 — Angular potential
Contains angular coordinate, equilibrium angle Θ0 (degrees), and angular
force constant k (eV rad⁻²). All listed angular terms are included continuously
during propagation. The C–N–H1 and C–N–H2 soft terms are not activated by a
migration criterion.

### S7 — Hydrogen-transfer activity and timing
Counts and fractions of trajectories with persistent H migration, mean
migration events per trajectory, counts of rearrangement-assisted dissociative
trajectories, and conditional median timing statistics.

### S8 — Bootstrap confidence intervals
The source presents two confidence intervals in bracket notation. The CSV
stores each lower and upper endpoint in separate numeric columns for easier
analysis. Resampling was performed independently within each energy group,
with 10,000 resamples of 200 trajectories with replacement and seed 20261114.

## Potential details recorded in the source

The short-range repulsive contribution is described in the source as a sum over
all atomic pairs, with A = 0.05 Eh (1.3606 eV) and ρ = 0.35 Å. The equation
itself should be checked against the original manuscript/source formatting
before implementing the potential; this repository does not implement the
interaction potential.
