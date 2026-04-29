# Notebook 22 Figure Captions

## Real versus control singular spectra

**Label:** `fig:singular-spectra`

**Files:** `figures/22_real_vs_control_singular_spectra.png`, `figures/22_real_vs_control_singular_spectra.pdf`

Singular spectra of the two-step residual operator $\Delta=P^{(2)}_{\mathrm{emp}}-P^2$ for the real sequence and synthetic controls. The leading real singular modes exceed iid and Markov controls, indicating structured higher-order memory beyond first-order transition statistics.

## Control metric summary

**Label:** `fig:control-summary`

**Files:** `figures/22_control_metric_summary.png`, `figures/22_control_metric_summary.pdf`

Normalized comparison of the principal validation metrics across real and control sequences. The real sequence dominates two-step residual magnitude, JS distance, leading singular value, and mutual-information excess, while iid and balanced controls remain near the noise floor.

## Statistical validation p-value heatmap

**Label:** `fig:pvalue-heatmap`

**Files:** `figures/22_statistical_validation_pvalue_heatmap.png`, `figures/22_statistical_validation_pvalue_heatmap.pdf`

Permutation and resampling validation summarized as $-\log_{10}(p)$ values. Structure-destroying iid and Markov nulls reject multiple real-sequence metrics, while block and window resampling retain local structure and therefore behave as conservative controls.

## Publication summary ratio heatmap

**Label:** `fig:ratio-heatmap`

**Files:** `figures/22_publication_summary_ratio_heatmap.png`, `figures/22_publication_summary_ratio_heatmap.pdf`

Effect-size summary showing real metrics divided by null means. Ratios above one indicate real-sequence excess relative to a null ensemble; clipped color scaling preserves readability while annotations retain numerical ratios.

## Residual energy rank requirement

**Label:** `fig:rank-requirement`

**Files:** `figures/22_residual_energy_rank_requirement.png`, `figures/22_residual_energy_rank_requirement.pdf`

Low-rank energy summary for the residual operator. The real sequence remains concentrated in a small number of singular modes, supporting a compact memory correction rather than high-dimensional noise fitting.

## Entropy rate and residual magnitude comparison

**Label:** `fig:entropy-residual`

**Files:** `figures/22_entropy_rate_and_residual_comparison.png`, `figures/22_entropy_rate_and_residual_comparison.pdf`

Entropy and two-step residual magnitude across real and control sequences. Randomizing controls increase entropy and suppress residual memory, while the real sequence retains measurable structured deviation from the first-order Markov baseline.

