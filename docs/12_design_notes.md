# Design Notes — Normalized Gap Distribution

## Notebook role

Notebook 12 moves from reconstruction and window-stability diagnostics into normalized prime-gap distribution diagnostics.

## Constraint

Normalize consecutive prime gaps by local log scale:

$$
z_n = \frac{p_{n+1} - p_n}{\log(p_n)}.
$$

## Measurement

Measure histogram, ECDF, quantiles, tail exceedance, and Jensen--Shannon distance to an Exp(1) baseline.

## CGCS score

Notebook-specific CGCS:

$$
CGCS = \frac{1}{1 + JS(P_{empirical}, P_{Exp(1)})}.
$$

The final-window score is `0.977480`.

## Handoff

Next notebook should connect normalized gap distribution diagnostics back to sieve/reconstruction diagnostics:

- compare reconstructed candidates versus true primes under normalized-gap statistics
- test whether local reconstruction preserves Exp(1)-style normalized gaps
- quantify which reconstruction method best preserves both density and gap distribution
