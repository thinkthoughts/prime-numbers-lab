# 17_higher_order_transition_memory_shuffle_baseline: higher-order transition memory + shuffle baseline

## Purpose

Notebook 17 tests whether normalized prime-gap residual states carry higher-order transition memory.
It compares empirical two-step transitions against a first-order Markov prediction and a shuffle baseline.

## Key numbers

- `two_step_l2_delta`: `0.00793828`
- `shuffle_mean_two_step_l2_delta`: `0.00219103`
- `real_to_shuffle_l2_ratio`: `3.62308`
- `max_abs_two_step_delta`: `0.0241669`
- `mean_abs_real_minus_shuffle`: `0.00608516`
- `lag1_real_mi`: `0.0126266`
- `lag1_shuffle_mi`: `0.00015853`
- `lag1_excess_mi`: `0.0124681`
- `lag2_real_mi`: `0.00228253`
- `lag2_shuffle_mi`: `0.000166966`
- `lag2_excess_mi`: `0.00211557`
- `top_two_step_residual`: `0.0241669`
- `top_conditional_chain_residual`: `0.0910104`

## Interpretation

A nonzero two-step residual means the empirical transition sequence is not completely described by the first-order operator.
The shuffle baseline preserves the one-point state distribution while destroying ordering, so real-vs-shuffle excess indicates ordered memory rather than marginal frequency alone.
Windowed diagnostics localize where higher-order residual structure concentrates across scale.



## Figures

### Figure 1 — 17 Conditional Memory Proxy By Middle Residue

![Figure 1](../figures/17_conditional_memory_proxy_by_middle_residue.png)

### Figure 2 — 17 Empirical Two Step Operator Heatmap

![Figure 2](../figures/17_empirical_two_step_operator_heatmap.png)

### Figure 3 — 17 Entropy Comparison By Anchor

![Figure 3](../figures/17_entropy_comparison_by_anchor.png)

### Figure 4 — 17 Excess Mutual Information Vs Lag

![Figure 4](../figures/17_excess_mutual_information_vs_lag.png)

### Figure 5 — 17 Markov Predicted Two Step Operator Heatmap

![Figure 5](../figures/17_markov_predicted_two_step_operator_heatmap.png)

### Figure 6 — 17 Mutual Information Vs Lag

![Figure 6](../figures/17_mutual_information_vs_lag.png)

### Figure 7 — 17 Real Vs Shuffle Two Step Delta Heatmap

![Figure 7](../figures/17_real_vs_shuffle_two_step_delta_heatmap.png)

### Figure 8 — 17 Real Vs Shuffle Two Step L1

![Figure 8](../figures/17_real_vs_shuffle_two_step_l1.png)

### Figure 9 — 17 Real Vs Shuffle Two Step L2

![Figure 9](../figures/17_real_vs_shuffle_two_step_l2.png)

### Figure 10 — 17 Real Vs Shuffle Two Step Lift Heatmap

![Figure 10](../figures/17_real_vs_shuffle_two_step_lift_heatmap.png)

### Figure 11 — 17 Top Conditional Chain Residuals

![Figure 11](../figures/17_top_conditional_chain_residuals.png)

### Figure 12 — 17 Top Two Step Residual Transitions

![Figure 12](../figures/17_top_two_step_residual_transitions.png)

### Figure 13 — 17 Transition Operator P Heatmap

![Figure 13](../figures/17_transition_operator_P_heatmap.png)

### Figure 14 — 17 Two Step Minus First Order Lift Heatmap

![Figure 14](../figures/17_two_step_minus_first_order_lift_heatmap.png)

### Figure 15 — 17 Two Step Operator Delta Heatmap

![Figure 15](../figures/17_two_step_operator_delta_heatmap.png)

### Figure 16 — 17 Two Step Transition Lift Heatmap

![Figure 16](../figures/17_two_step_transition_lift_heatmap.png)

### Figure 17 — 17 Windowed Information Structure

![Figure 17](../figures/17_windowed_information_structure.png)

### Figure 18 — 17 Windowed Transition Delta Heatmap

![Figure 18](../figures/17_windowed_transition_delta_heatmap.png)

### Figure 19 — 17 Windowed Transition Lift Heatmap

![Figure 19](../figures/17_windowed_transition_lift_heatmap.png)

### Figure 20 — 17 Windowed Two Step Residual Heatmap

![Figure 20](../figures/17_windowed_two_step_residual_heatmap.png)

### Figure 21 — 17 Windowed Two Step Residual Metrics

![Figure 21](../figures/17_windowed_two_step_residual_metrics.png)

### Figure 22 — 17 Windowed Two Step Residual Norms

![Figure 22](../figures/17_windowed_two_step_residual_norms.png)

