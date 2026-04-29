# 18_spectral_memory_low_rank_operator: spectral memory + low-rank operator correction

## Purpose

Notebook 18 tests whether the empirical two-step transition residual from Notebook 17 has low-rank spectral structure.
It decomposes M = P2_empirical - P1^2 and measures how much predictive error is removed by rank-k corrections.

## Key numbers

- `markov_l2_error`: `0.00793828`
- `rank1_l2_error`: `0.0052814`
- `rank4_l2_error`: `0.00124468`
- `rank4_error_reduction_fraction`: `0.843205`
- `top_singular_energy_share`: `0.557366`
- `rank90`: `3`
- `rank95`: `3`
- `real_top_singular_value`: `0.0474118`
- `shuffle_mean_top_singular_value`: `0.0113954`
- `top_singular_real_minus_shuffle_zscore`: `24.3493`
- `real_frobenius_residual`: `0.0635062`
- `shuffle_mean_frobenius_residual`: `0.0175282`

## Interpretation

A concentrated singular spectrum means the two-step residual is not merely diffuse noise.
A low-rank correction P^2 + M_k estimates how many memory modes are needed to explain the empirical two-step operator.
Residue projections connect dominant spectral modes back to anchor classes modulo 30.
Shuffle comparisons control for finite-sample effects and the one-point state distribution.



## Figures

### Figure 1 — 18 Corrected Two Step Operator Rank 1

![Figure 1](../figures/18_corrected_two_step_operator_rank_1.png)

### Figure 2 — 18 Corrected Two Step Operator Rank 2

![Figure 2](../figures/18_corrected_two_step_operator_rank_2.png)

### Figure 3 — 18 Corrected Two Step Operator Rank 3

![Figure 3](../figures/18_corrected_two_step_operator_rank_3.png)

### Figure 4 — 18 Corrected Two Step Operator Rank 4

![Figure 4](../figures/18_corrected_two_step_operator_rank_4.png)

### Figure 5 — 18 Cumulative Residual Energy

![Figure 5](../figures/18_cumulative_residual_energy.png)

### Figure 6 — 18 Empirical Two Step Operator Heatmap

![Figure 6](../figures/18_empirical_two_step_operator_heatmap.png)

### Figure 7 — 18 Markov Predicted Two Step Operator Heatmap

![Figure 7](../figures/18_markov_predicted_two_step_operator_heatmap.png)

### Figure 8 — 18 Predictive Error Vs Memory Rank

![Figure 8](../figures/18_predictive_error_vs_memory_rank.png)

### Figure 9 — 18 Real Vs Shuffle Residual Norm

![Figure 9](../figures/18_real_vs_shuffle_residual_norm.png)

### Figure 10 — 18 Real Vs Shuffle Top Singular Value

![Figure 10](../figures/18_real_vs_shuffle_top_singular_value.png)

### Figure 11 — 18 Remaining Residual After Rank 1

![Figure 11](../figures/18_remaining_residual_after_rank_1.png)

### Figure 12 — 18 Remaining Residual After Rank 2

![Figure 12](../figures/18_remaining_residual_after_rank_2.png)

### Figure 13 — 18 Remaining Residual After Rank 3

![Figure 13](../figures/18_remaining_residual_after_rank_3.png)

### Figure 14 — 18 Remaining Residual After Rank 4

![Figure 14](../figures/18_remaining_residual_after_rank_4.png)

### Figure 15 — 18 Residual Singular Value Spectrum

![Figure 15](../figures/18_residual_singular_value_spectrum.png)

### Figure 16 — 18 Residue Projection Memory Mode 1

![Figure 16](../figures/18_residue_projection_memory_mode_1.png)

### Figure 17 — 18 Residue Projection Memory Mode 2

![Figure 17](../figures/18_residue_projection_memory_mode_2.png)

### Figure 18 — 18 Residue Projection Memory Mode 3

![Figure 18](../figures/18_residue_projection_memory_mode_3.png)

### Figure 19 — 18 Residue Projection Memory Mode 4

![Figure 19](../figures/18_residue_projection_memory_mode_4.png)

### Figure 20 — 18 Transition Operator P Heatmap

![Figure 20](../figures/18_transition_operator_P_heatmap.png)

### Figure 21 — 18 Two Step Operator Prediction Error

![Figure 21](../figures/18_two_step_operator_prediction_error.png)

### Figure 22 — 18 Two Step Residual Operator Heatmap

![Figure 22](../figures/18_two_step_residual_operator_heatmap.png)

### Figure 23 — 18 Windowed Rank4 Residual Reduction

![Figure 23](../figures/18_windowed_rank4_residual_reduction.png)

### Figure 24 — 18 Windowed Rank Requirement

![Figure 24](../figures/18_windowed_rank_requirement.png)

### Figure 25 — 18 Windowed Remaining Rank4 Residual Heatmap

![Figure 25](../figures/18_windowed_remaining_rank4_residual_heatmap.png)

