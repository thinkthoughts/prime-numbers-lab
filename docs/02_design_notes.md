# Design Notes — Prime Gaps

## Notebook role

Notebook 02 follows Notebook 01 by moving from residue constraints to ordered sequence structure.

Notebook 01 measured which residue classes remain under constraint.
Notebook 02 measures how prime order continues through gaps.

## Constraint

Prime gaps are compared to the logarithmic scale baseline:

g_n = p_(n+1) - p_n
E[g_n] approximately log(p_n)

## Measurement

1. all prime gaps below N_MAX
2. gap statistics
3. relative drift from log(p_n)
4. scale-window averages
5. coarse recoverability from bin-level logarithmic scale

## CGCS score

CGCS_gap_logscale = 1 / (1 + mean(|g_n - log(p_n)| / log(p_n)))

## Figures

1. gap histogram
2. gaps versus logarithmic baseline
3. mean gap versus logarithmic scale by bin

## Handoff

Notebook 03 should measure density versus x/log(x), connecting gap scale to prime-counting scale.
