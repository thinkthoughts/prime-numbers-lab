# Sieve Constraints and Asymptotic Diagnostics (Notebook 04)

## 1. Empirical structure

Across sieve layers and increasing max filter prime \(Q\):

- candidate count decreases monotonically  
- retention fraction follows a smooth decay  
- log-product exhibits near-linear structure in \(\log\log Q\)

This indicates convergence toward a known asymptotic regime.

---

## 2. Retained candidates by layer

![Retained candidates](../figures/04_retained_candidates_by_layer.png)

Candidate count decreases rapidly under early constraints, then stabilizes as only primes remain.

---

## 3. Removed candidates by prime filter

![Removed by filter](../figures/04_removed_by_filter.png)

Early primes dominate removal:

- removal strength scales ≈ \(1/p\)  
- most composite structure is eliminated early  

---

## 4. Retention and drift

![Retention and drift](../figures/04_retention_and_drift_by_layer.png)

- retention decreases smoothly  
- drift accumulates monotonically  

Interpretation:

> composite structure is progressively removed under layered constraints

---

## 5. Product baseline comparison

![Retention vs product baseline](../figures/04_retention_vs_product_baseline.png)

We compare observed retention to:

\[
M(Q) = \prod_{p \le Q} \left(1 - \frac{1}{p}\right)
\]

Observations:

- strong agreement across all \(Q\)  
- deviations are small and structured  

Interpretation:

> the product baseline is the first-order term in sieve estimates; deviations arise from correlations between divisibility constraints

---

## 6. Log–log linearization

![Log product vs log log](../figures/04_log_product_vs_loglog.png)

We analyze:

\[
-\log M(Q) \quad \text{vs} \quad \log\log Q
\]

Findings:

- near-linear relationship  
- slope < 1 in finite range  

---

## 7. Log–log slope fit

![Log-log fit overlay](../figures/04_loglog_fit_overlay.png)

Fit:

\[
-\log M(Q) \approx a \log\log Q + b
\]

Observed:

- slope ≈ 0.816  
- \(R^2 \approx 0.99\)

Theory:

\[
-\log M(Q) \sim \log\log Q
\]

Interpretation:

> slope < 1 indicates pre-asymptotic constraint accumulation

---

## 8. Slope vs max \(Q\)

![Slope vs max Q](../figures/04_slope_vs_max_q.png)

- slope increases monotonically (~0.64 → ~0.82)  
- theoretical limit: **1**

Interpretation:

> finite sieve depth underestimates asymptotic scaling, but converges toward it

---

## 9. Residual definition

\[
R(Q) = -\log M(Q) - \log\log Q
\]

This removes leading-order growth and isolates constant behavior.

---

## 10. Residual convergence

![Residual vs max Q](../figures/04_residual_vs_max_q.png)

Observations:

- residual stabilizes  
- running mean smooths fluctuations  
- tail mean → ≈ **0.58**  
- tail slope → ~0  

Matches:

\[
-\log M(Q) = \log\log Q + \gamma + o(1)
\]

where:

\[
\gamma \approx 0.57721
\]

---

## 11. Residual interpretation

- deviation from slope-1 is **systematic**, not noise  
- convergence is toward a **constant offset**  
- fluctuations shrink with increasing \(Q\)

---

## 12. Convergence diagnostics

- tail slope → ~0  
- tail standard deviation → small  
- tail range → bounded  

Score:

\[
\text{score} = \frac{1}{1 + |\text{slope}| + \text{std} + \text{range}}
\]

Higher score ⇒ stronger convergence to constant.

---

## 13. Product-baseline error

![Product baseline error](../figures/04_product_baseline_error.png)

Error remains:

- small  
- structured  
- bounded  

Interpretation:

> finite sieve correlations, not randomness

---

## 14. Core asymptotic result

\[
M(Q) \sim \frac{e^{-\gamma}}{\log Q}
\]

This includes:

- correct scaling (\(1/\log Q\))  
- correct constant (\(e^{-\gamma}\))  

---

## 15. Summary

Finite sieve reveals asymptotic structure:

- slope(Q) → 1  
- residual(Q) → γ  
- error(Q) → bounded  

---

## 16. Clean takeaway

> Multiplicative constraint filtering produces prime density through:
>
> - log-log scaling  
> - constant offset convergence  
> - structured (non-random) error

---

**Constraint → signal > noise**
