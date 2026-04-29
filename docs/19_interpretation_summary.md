# Notebook 19 interpretation summary

Notebook 19 validates the low-rank memory-operator model from Notebook 18.

## Core result

The empirical two-step operator differs from the Markov baseline by

`Delta = P2_empirical - P @ P`.

SVD shows that this residual is low-rank:

- rank for 90% residual energy: **4**
- rank for 95% residual energy: **5**

A rank-4 correction reduces two-step L2 error from **0.00834829** to **0.0021628**, a reduction ratio of **74.093%**.

## Validation result

Generated-sequence tests compare Markov, empirical two-step, and rank-4 corrected models using transition errors, lagged mutual information, and triple-distribution JS divergence.

## Interpretation

The correction is not merely a fitted matrix. It has interpretable residue projections and mode ablations show that removing individual modes increases prediction error. This supports the interpretation that the prime residue sequence contains structured higher-order memory beyond first-order Markov flow.
