# Bridges — Table of Contents

This section presents structured interfaces between residue-class transition operators and established mathematical questions.

Each bridge isolates a measurable object—typically the transition operator \(P\) or residual operator

\[
\Delta = P^{(2)} - P^2
\]

—and connects it to a specific domain such as prime gaps or spectral structure.

The goal is not to resolve these problems, but to define concrete, testable correspondences.

---

## Prime gap structure

### Twin primes

- [`bridge_twin_primes.md`](bridge_twin_primes.md)  
  Residue transitions modulo 30 identify and measure twin-prime-compatible gap \(+2\) structure.  
  _Twin primes → gap +2 residue transitions_

---

### Asymptotic twin primes

- [`bridge_asymptotic_twin.md`](bridge_asymptotic_twin.md)  
  Finite-scale operator \(\Delta = P^{(2)} - P^2\) tracks how twin-prime-compatible structure behaves as sample size increases.  
  _Asymptotic twin → scaling of \(\Delta\) under \(N\)_

---

## Spectral / zeta structure

### Zeta function

- [`bridge_zeta.md`](bridge_zeta.md)  
  Residue transition operators provide a finite-state proxy for studying structured deviations analogous to spectral correlations.  
  _Zeta → spectral-type structure in finite operators_

---

## Related notebooks

- `../scripts/twin_prime_transition_experiment.ipynb`  
- `../scripts/delta_twin_slice.ipynb`  

---

## Summary

Bridges define mappings of the form:

```text
residue transitions → operators (P, Δ) → domain-specific structure
```

They provide entry points for extending the framework through computation and comparison.
