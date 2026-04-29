# Design Notes — Prime Density vs x/log(x)

## Notebook role

Notebook 03 follows Notebook 02 by moving from local gap structure to global density structure.

Notebook 01 measured finite residue structure.
Notebook 02 measured local spacing through gaps.
Notebook 03 measures global prime-counting density.

## Constraint

Prime counts are compared to the logarithmic density baseline:

pi(x) approximately x/log(x).

## Measurement

The notebook computes:

1. pi(x) for sampled x-values
2. x/log(x) baseline
3. ratio pi(x)/(x/log(x))
4. density drift
5. CGCS density score

## CGCS score

CGCS_density = 1 / (1 + mean(|pi(x)-x/log(x)|/(x/log(x))))

## Drift

drift(x) = |pi(x) - x/log(x)| / (x/log(x))

## Figures

1. prime count versus x/log(x)
2. ratio to logarithmic baseline
3. density drift from x/log(x)

## Recoverability

x/log(x) recovers global density scale, not exact prime locations.

## Handoff

Notebook 04 should measure sieve constraints as layered filtering.
