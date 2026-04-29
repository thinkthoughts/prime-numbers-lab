# Design Notes — Recoverability Under Partial Observation

## Notebook role

Notebook 06 follows Notebook 05 by testing whether corrupted prime observations still contain recoverable constraint signal.

Notebook 05 showed random controls fail to recover structure.
Notebook 06 shows that damaged structure can still retain recoverable signal.

## Corruption scenarios

1. missing-prime observations
2. noisy observations
3. mixed corruption

## Measurements

1. recovery
2. precision
3. mod 6 constraint score
4. density drift
5. sieve-consistency
6. reconstruction after sieve-consistency filtering

## Core claim

Partial observation weakens count recovery but does not erase constraint signal.

## Figures

1. recovery vs keep fraction
2. precision vs noise level
3. mod 6 score by scenario
4. density drift by observation
5. sieve-consistency scores
6. reconstruction scores

## Handoff

Notebook 07 should reconstruct candidate prime structure from corrupted observations using constraints.
