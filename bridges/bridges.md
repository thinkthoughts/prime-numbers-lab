# Bridges — Table of Contents

This directory connects the residue-transition framework to specific problems and domains.

Each bridge isolates a concrete interface between:

- residue transitions  
- transition operators \(P\)  
- residual operator \(\Delta = P^{(2)} - P^2\)  

and a target question.

---

## Prime gap structure

### Twin primes

- [`bridge_twin_primes.md`](bridge_twin_primes.md)  
  Residue-level interpretation of twin-prime-compatible transitions.

- [`bridge_asymptotic_twin.md`](bridge_asymptotic_twin.md)  
  Finite-to-asymptotic interface via transition operators and Δ.

---

## Spectral / zeta structure

### Zeta function

- [`bridge_zeta.md`](bridge_zeta.md)  
  Connection between residue transitions and spectral structure.

---

## Notes

These bridges:

- define measurable correspondences  
- provide experiment paths via `scripts/`  

---

## Related notebooks

- `../scripts/twin_prime_transition_experiment.ipynb`  
- `../scripts/delta_twin_slice.ipynb`  

---

## Summary

Bridges map:

```text
residue transitions → operators (P, Δ) → domain-specific structure
