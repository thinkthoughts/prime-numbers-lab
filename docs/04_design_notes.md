# Design Notes — Sieve Constraints

## Notebook role

Notebook 04 follows Notebook 03 by moving from density measurement to the finite filtering mechanism that recovers primes.

Notebook 01 measured residue constraints.
Notebook 02 measured gap structure.
Notebook 03 measured density scale.
Notebook 04 measures layered sieve filtering.

## Constraint

Each layer removes composite multiples of a prime filter q:

S_k = S_(k-1) \ {n : q_k divides n, n != q_k}.

## Measurement

The notebook computes:

1. retained candidate count by layer
2. removed candidate count by filter
3. retention share
4. drift share
5. exact recovery against the reference prime set

## CGCS score

CGCS_sieve = |S_final ∩ P_N| / |P_N| after filters q <= sqrt(N).

Expected result: exactly 1.0.

## Figures

1. retained candidates by sieve layer
2. removed candidates by prime filter
3. retention and drift by layer

## Recoverability

The full sieve recovers prime identity exactly up to N when all prime filters q <= sqrt(N) are applied.

## Handoff

Notebook 05 should compare prime structure against random candidate sets.
