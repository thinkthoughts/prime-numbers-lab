# Design Notes — Constraint Reconstruction

## Notebook role

Notebook 07 follows Notebook 06 by moving from recoverability diagnostics to staged reconstruction.

v2 adds stress tests so global density reconstruction is evaluated more honestly.

## Reconstruction stages

1. raw observation
2. residue filter
3. small-prime sieve filter
4. density-guided reconstruction

## Stress tests

1. biased range corruption
2. adversarial mod-6-passing composite noise
3. local gap diagnostics after reconstruction

## Measurements

1. recovery
2. precision
3. F1
4. density drift
5. mod 6 score
6. confusion counts
7. gap drift

## Core claim

Filtering restores precision; reconstruction trades precision for recovery.

## Caution

Candidate completions are hypotheses, not certified primes.

## Handoff

Notebook 08 should improve candidate completion using local prime-gap statistics.
