# Design Notes — Residue Classes mod 6

## Notebook role

Notebook 01 is the first measurement notebook in prime-numbers-lab.

It establishes a direct finite constraint before moving into gaps, density, sieve structure, random comparisons, recoverability, or zeta bridges.

## Constraint

For primes greater than 3:

p mod 6 must be 1 or 5.

## Measurement

The notebook counts residues modulo 6 for:

1. all integers below N_MAX
2. primes greater than 3 below N_MAX

It compares residue shares and computes a direct CGCS score.

## CGCS score

CGCS_mod6 = #{p>3: p mod 6 in {1,5}} / #{p>3}

For this necessary residue constraint, the expected result is exactly 1.0.

## Drift

drift_mod6 = 1 - CGCS_mod6

The expected drift is exactly 0.0.

## Recoverability

Modulo 6 recovers candidate residue classes, not primes exactly. It is a necessary condition, not a sufficient condition.

## Handoff

Notebook 02 should measure prime gaps and show how ordered prime structure continues across scale.
