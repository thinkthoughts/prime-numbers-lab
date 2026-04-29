# Notebook 21 Interpretation — Statistical Validation Layer

Notebook 21 validates the low-rank two-step memory signal using permutation, Markov-synthetic, block-bootstrap, and window-bootstrap null ensembles.

## Core real-sequence metrics

- Two-step residual L2: 0.0667863
- JS empirical vs Markov: 0.000747783
- Top singular value: 0.0413681
- Rank-4 improvement: 0.740929
- Mutual-information excess: 0.0401614 bits

## Main conclusion

The real prime-residue sequence shows statistically structured two-step deviation from its first-order Markov baseline. The strongest validation layers are residual magnitude, singular-spectrum dominance, and persistence of low-rank correction improvement across bootstrap/null comparisons.
