# Design Notes — Local Gap Reconstruction

## Notebook role

Notebook 08 follows Notebook 07 by improving candidate completion with local gap scoring.

Notebook 07 showed that density-only reconstruction repairs global count but can leave local spacing artifacts.

## Compared methods

1. raw observation
2. sieve-cleaned observation
3. density-only reconstruction
4. local-gap reconstruction

## Measurements

1. precision
2. recovery
3. F1
4. density drift
5. gap drift
6. gap residuals

## Core claim

Density restores missing mass; local gap scoring tests whether reconstructed mass lands in structurally plausible places.

## Caution

Candidate completions are hypotheses, not certified primes.

## Handoff

Notebook 09 should test windowed/local reconstruction and compare reconstruction stability across sliding intervals.
