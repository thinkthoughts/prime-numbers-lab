# Adaptive Window Reconstruction

## Constraint result

This notebook tests adaptive window reconstruction.

Notebook 09 showed that local-window diagnostics expose failures hidden by global metrics.

Notebook 10 uses local instability as feedback for candidate scoring.

## Adaptive rule

For a window W:

```text
instability(W) = alpha * density_error(W) + beta * gap_drift(W)
w_gap(W) = w_gap * (1 + lambda * instability(W))
w_density(W) = w_density / (1 + lambda * instability(W))
```

## Summary metrics

- mean density error, density-only = 0.008987
- mean density error, fixed local-gap = 0.009108
- mean density error, adaptive window = 0.009111
- mean gap drift, density-only = 0.588837
- mean gap drift, fixed local-gap = 0.585316
- mean gap drift, adaptive window = 0.588335
- adaptive minus fixed gap drift = 0.003019
- adaptive stability CGCS score = 0.625999

## Interpretation

Adaptive reconstruction uses local instability as feedback.

If adaptive reconstruction improves gap drift, local feedback adds value beyond fixed scoring.

If improvement is small, fixed density/local-gap reconstruction has saturated the log-gap model.

## Core statement

Adaptive window reconstruction treats local instability as feedback, converting reconstruction from a fixed global rule into a local correction process.

## Next limit

If adaptive feedback saturates, the next notebook should replace log(x) with a learned local expected-gap model.

## Figures

### Figure 1 — Adaptive weights by window

![Figure 1](../figures/10_adaptive_weights_by_window.png)

### Figure 2 — Window instability profile

![Figure 2](../figures/10_window_instability_profile.png)

### Figure 3 — Method density error

![Figure 3](../figures/10_method_density_error.png)

### Figure 4 — Method gap drift

![Figure 4](../figures/10_method_gap_drift.png)

### Figure 5 — Adaptive gap-drift delta

![Figure 5](../figures/10_adaptive_delta_gap_drift.png)

### Figure 6 — Unstable windows comparison

![Figure 6](../figures/10_unstable_windows_comparison.png)

### Figure 7 — Gap profile under adaptive reconstruction

![Figure 7](../figures/10_gap_profile_adversarial.png)

### Figure 8 — Adaptive stability map

![Figure 8](../figures/10_stability_map_adaptive.png)

### Figure 9 — Mean window F1 by method

![Figure 9](../figures/10_mean_window_f1_by_method.png)


