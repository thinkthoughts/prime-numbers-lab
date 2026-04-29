# Residual Scaling Law

## Constraint result

This notebook tests whether normalized prime-gap residuals decay by a log-scale law.

The fitted model is:

$$
\|\Delta(z,x)\| \sim C(\log x)^{-\alpha}.
$$

## Remains under constraint

The exponential envelope remains visible after normalization, and residual metrics can be fit by a compact scale model.

Fitted exponents:

- L1 alpha = 0.559588
- L2 alpha = 0.545420
- JS alpha = 0.806866

## Drift

Drift is measured by residual L1, residual L2, JS divergence, positive/negative residual mass, and tail bias.

## Recoverability

The residual trend is recoverable as a finite-scale diagnostic:

- residual norm vs scale
- log-scale power-law fit
- alpha comparison
- residual heatmap
- fit residuals

## CGCS score

The scaling agreement score is:

$$
CGCS_{scale} =
\frac{1}{1+\overline{\|\Delta\|_1}+\overline{JS}+\overline{|r_{fit}|}}.
$$

Measured score:

$$
CGCS_{scale} = 0.426777.
$$

## Caution

This notebook does not prove an asymptotic theorem.

It measures finite residual scaling relative to the exponential heuristic.

## Figures

### Figure 1 — 14 Residual Norm Vs Scale

![Figure 1](../figures/14_residual_norm_vs_scale.png)

### Figure 2 — 14 L1 Scaling Fit

![Figure 2](../figures/14_l1_scaling_fit.png)

### Figure 3 — 14 L2 Scaling Fit

![Figure 3](../figures/14_l2_scaling_fit.png)

### Figure 4 — 14 Js Scaling Fit

![Figure 4](../figures/14_js_scaling_fit.png)

### Figure 5 — 14 Alpha Comparison

![Figure 5](../figures/14_alpha_comparison.png)

### Figure 6 — 14 Fit Residuals

![Figure 6](../figures/14_fit_residuals.png)

### Figure 7 — 14 Residual Heatmap Across Scale

![Figure 7](../figures/14_residual_heatmap_across_scale.png)

### Figure 8 — 14 Positive Negative Residual Mass

![Figure 8](../figures/14_positive_negative_residual_mass.png)

### Figure 9 — 14 Distributional Convergence Score

![Figure 9](../figures/14_distributional_convergence_score.png)

### Figure 10 — 14 Tail Residual Bias Z Ge 3

![Figure 10](../figures/14_tail_residual_bias_z_ge_3.png)

### Figure 11 — 14 Final Window Pdf Vs Exp1

![Figure 11](../figures/14_final_window_pdf_vs_exp1.png)

