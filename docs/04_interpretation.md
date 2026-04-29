# Sieve Constraints and Asymptotic Diagnostics

## 1. Empirical structure

Across sieve layers and increasing max filter prime Q:

- candidate count decreases monotonically  
- retention fraction follows a smooth decay  
- log-product exhibits near-linear structure in log log Q  

This suggests convergence toward a known asymptotic regime.

---

## 2. Product baseline comparison

We compare observed retention to the classical baseline:

M(Q) ≈ 1 / log Q

Observations:

- agreement is strong across all Q  
- deviations are small and structured  
- error is bounded and non-random  

---

## 3. Log–log linearization

We analyze:

-log M(Q) vs log log Q

Findings:

- near-linear relationship  
- fitted slope increases with Q  
- slope remains below 1 in finite range  

---

## 4. Slope vs max Q

Tracking the fitted slope:

- slope(Q) increases monotonically  
- observed range: ~0.64 → ~0.82  
- theoretical limit: 1  

Interpretation:

finite sieve depth underestimates asymptotic slope

---

## 5. Residual definition

R(Q) = -log M(Q) - log log Q

---

## 6. Residual convergence

Empirical behavior:

- R(Q) decreases and stabilizes  
- running mean smooths fluctuations  
- tail mean approaches constant ≈ 0.58  
- tail slope → ~0  

Matches:

-log M(Q) = log log Q + γ + o(1)

γ ≈ 0.57721 (Euler–Mascheroni constant)

---

## 7. Convergence diagnostics

- tail slope → near 0  
- tail standard deviation → small  
- tail range → bounded  

Score:

score = 1 / (1 + |slope| + std + range)

---

## 8. Core result

M(Q) ~ exp(-γ) / log Q

---

## 9. Summary

Finite sieve → asymptotic structure emerges:

- slope(Q) → 1  
- residual(Q) → γ  
- error(Q) → bounded  

---

Constraint → signal > noise

---

# Sieve Constraints and Asymptotic Diagnostics (Notebook 04)

## 1. Retention vs product baseline

![Retention vs baseline](../figures/04_retention_vs_q.png)

Observed retention closely follows the product baseline:

M(Q) ≈ 1 / log Q

Deviation remains small and structured.

---

## 2. Log–log decay structure

![Log-log decay](../figures/04_loglog_decay.png)

We examine:

-log M(Q) vs log log Q

This linearizes the asymptotic relation.

---

## 3. Slope fit and theoretical comparison

![Slope fit](../figures/04_loglog_fit.png)

Fitted slope:

slope ≈ 0.816 (finite Q)

Theoretical asymptotic slope:

slope → 1

Interpretation:
finite sieve depth underestimates asymptotic scaling.

---

## 4. Slope vs max Q

![Slope vs Q](../figures/04_slope_vs_Q.png)

Slope increases monotonically with Q:

~0.64 → ~0.82 → … → 1

---

## 5. Residual definition

R(Q) = -log M(Q) - log log Q

---

## 6. Residual convergence

![Residual vs Q](../figures/04_residual_vs_Q.png)

Observations:

- R(Q) stabilizes  
- running mean smooths noise  
- tail mean → constant ≈ 0.58  

Matches:

-log M(Q) = log log Q + γ + o(1)

γ ≈ 0.57721

---

## 7. Convergence diagnostics

Residual diagnostics confirm:

- tail slope → 0  
- variance → small  
- range → bounded  

---

## 8. Core result

M(Q) ~ exp(-γ) / log Q

---

## 9. Summary

Finite sieve reveals asymptotic structure:

- slope(Q) → 1  
- residual(Q) → γ  
- error(Q) bounded  

---

Constraint → signal > noise
