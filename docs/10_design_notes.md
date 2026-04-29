# Design Notes — Adaptive Window Reconstruction

## Notebook role

Notebook 10 converts window instability from Notebook 09 into adaptive reconstruction weights.

## Methods compared

1. raw
2. sieve_cleaned
3. density_only
4. local_gap_fixed
5. adaptive_window

## Adaptive rule

Instability increases gap weight and decreases density weight locally.

## Diagnostics

1. adaptive weights by window
2. instability profile
3. mean local density error
4. mean local gap drift
5. adaptive delta against fixed local-gap
6. unstable-window counts
7. stability heatmap

## Core claim

Adaptive window reconstruction treats local instability as feedback.

## Handoff

Notebook 11 should replace log(x) with a locally learned expected-gap model.
