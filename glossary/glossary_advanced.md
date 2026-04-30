# Glossary (Advanced) — Prime Numbers Lab

This glossary extends the base definitions with connections to established concepts in number theory, probability, and spectral analysis.

---

## Residue system (mod 30)

The reduction modulo 30 restricts primes > 5 to the multiplicative group:

(ℤ/30ℤ)× = {1, 7, 11, 13, 17, 19, 23, 29}

This is a finite state space of size 8.

Interpretation:
- A coarse-grained encoding of primes
- Filters out trivial divisibility constraints (2, 3, 5)
- Comparable to working in a reduced residue system modulo a primorial

---

## Transition operator (P)

P is an empirical stochastic matrix over (ℤ/30ℤ)×:

Pᵢⱼ = Prob(xₙ₊₁ = j | xₙ = i)

Interpretation:
- First-order Markov approximation to the prime residue process
- Analogous to transition kernels in Markov chains
- A coarse probabilistic model of prime gaps modulo 30

---

## Two-step operator (P^(2))

Defined empirically from (xₙ, xₙ₊₂), not by squaring P.

Interpretation:
- Measures actual second-order transitions
- Allows comparison between observed dynamics and Markov closure

---

## First-order closure

The identity:

P^(2) ≈ P²

represents closure under the Markov assumption.

Interpretation:
- Equivalent to assuming conditional independence:
  xₙ₊₂ ⟂ xₙ | xₙ₊₁
- Standard approximation in stochastic processes

---

## Residual operator (Δ)

Δ = P^(2) − P²

Interpretation:
- Measures failure of Markov closure
- Encodes second-order correlations
- Analogous to higher-order cumulants in probability
- Can be viewed as a discrete analogue of deviation from a product measure

---

## Low-rank structure

Δ is observed to be approximately low-rank.

Interpretation:
- Structure is concentrated in a small-dimensional subspace
- Suggests a small number of dominant modes
- Comparable to:
  - principal components (PCA)
  - low-rank perturbations in random matrix theory
  - structured deviations from random ensembles

---

## Singular value spectrum

Singular values of Δ:

Δ = U Σ Vᵀ

Interpretation:
- Measures strength of independent modes of deviation
- Rapid decay indicates compressibility
- Analogous to:
  - spectral gaps
  - effective rank
  - energy concentration in signal processing

---

## Control models

### iid shuffle
Destroys all sequential structure.

Interpretation:
- Baseline for independence
- Equivalent to sampling without temporal correlation

---

### Markov simulation
Generates sequences from P.

Interpretation:
- Enforces first-order structure
- Removes higher-order correlations

---

### Block resampling
Shuffles contiguous segments.

Interpretation:
- Preserves local correlations
- Tests scale at which structure exists
- Comparable to bootstrap methods in time series

---

## Local structure

Observed persistence under block resampling.

Interpretation:
- Structure exists at finite scales
- Not purely global or asymptotic
- Suggests short-range correlations

---

## Higher-order structure

Structure present in Δ.

Interpretation:
- Not captured by first-order transition probabilities
- Encodes dependencies across multiple steps
- Comparable to:
  - higher-order correlations
  - non-Markovian effects
  - deviations from simple probabilistic models

---

## Relation to prime gap models

### Cramér model
Treats primes as independent random variables with density ~1/log n.

Interpretation:
- Predicts gap distributions
- Does not model residue transition structure

Δ provides a diagnostic not captured by this framework.

---

## Relation to random matrix theory

Low-rank structure suggests:

- structured deviation from random ensembles
- possible analogy to signal + noise decomposition

However:
- no claim of direct correspondence
- operates at a different level (finite residue dynamics vs spectral statistics)

---

## Relation to zeta-constraint-lab

Conceptual bridge:

prime residue transitions → finite dynamical system  
zeta zeros → spectral object  

Shared theme:
- structured deviation from baseline models
- concentration in low-dimensional components

---

## Finite vs asymptotic

This work is finite-sample and computational.

Interpretation:
- Observations are empirical
- No asymptotic claims
- Intended as a diagnostic or exploratory framework

---

## Key interpretation

Δ = P^(2) − P² is:

- a measurable object
- a diagnostic of higher-order structure
- a bridge between combinatorial data and spectral analysis

---

## Scope

This work does NOT:

- prove new theorems about primes
- establish asymptotic laws

It DOES:

- provide a representation of prime transitions
- identify structured deviation from simple models
- suggest directions for further analysis
