# Design Notes — Sieve Constraints

## Notebook role

Notebook 04 follows Notebook 03 by moving from density measurement to the finite filtering mechanism that recovers primes.

Notebook 01 measured residue constraints.
Notebook 02 measured gap structure.
Notebook 03 measured density scale.
Notebook 04 measures layered sieve filtering.

## Upgrade in v4

This version includes cumulative product baseline, log-product / log-log tracking, and product-baseline error tracking.

## Constraint

Each layer removes composite multiples of a prime filter q:

S_k = S_(k-1) \ {n : q_k divides n, n != q_k}.

## Measurement

The notebook computes:

1. retained candidate count by layer
2. removed candidate count by filter
3. retention share
4. drift share
5. product-model baseline
6. exact recovery against the reference prime set
7. log-product decay
8. log-log comparison
9. product-baseline error
10. log-log slope fit and theoretical slope-1 overlay

## CGCS score

CGCS_sieve = |S_final ∩ P_N| / |P_N| after filters q <= sqrt(N).

Expected result: exactly 1.0.

## Figures

1. retained candidates by sieve layer
2. removed candidates by prime filter
3. retention and drift by layer
4. observed retention versus product baseline
5. log-product decay versus log-log scale
6. fitted log-log overlay
7. product-baseline error

## Recoverability

The full sieve recovers prime identity exactly up to N when all prime filters q <= sqrt(N) are applied.

## Handoff

Notebook 05 should compare prime structure against random candidate sets.
