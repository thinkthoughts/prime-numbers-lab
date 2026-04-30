# Glossary — Prime Numbers Lab

This glossary defines key terms used in the paper and repository in direct, operational language.

---

## Consecutive primes

A sequence of primes in increasing order:

p₁, p₂, p₃, ...

This work studies transitions between consecutive primes.

---

## Residue (modulo 30)

For a prime p > 5:

p mod 30 ∈ {1, 7, 11, 13, 17, 19, 23, 29}

These are the only possible residues for primes greater than 5 modulo 30.

---

## Prime sequence (mod 30)

The sequence obtained by reducing consecutive primes modulo 30:

xₙ = pₙ mod 30

This produces a sequence over 8 discrete states.

---

## Transition

A pair:

(xₙ, xₙ₊₁)

representing movement between residue states for consecutive primes.

---

## Transition operator (P)

An 8×8 matrix defined by:

Pᵢⱼ = frequency of transitions from residue i to residue j

Rows are normalized so each row sums to 1.

P represents first-order behavior of the sequence.

---

## Two-step operator (P^(2))

An operator defined by transitions:

(xₙ, xₙ₊₂)

It measures behavior over two steps directly from the data.

---

## First-order model

A model where transitions depend only on the current state.

Formally:

P^(2) ≈ P²

This corresponds to a Markov assumption (memoryless transitions).

---

## Residual operator (Δ)

Defined as:

Δ = P^(2) − P²

Δ measures deviation from the first-order model.

---

## Structured deviation

A deviation that is not uniform or random.

In this work, Δ shows patterns concentrated in a small number of components.

---

## Low-rank structure

A matrix is low-rank if most of its mass is captured by a small number of singular values.

In this work:

Δ has low-rank structure

meaning a few components dominate its behavior.

---

## Singular values

Values from the decomposition:

Δ = U Σ Vᵀ

They measure how much each component contributes to the structure of Δ.

---

## Control sequences

Sequences constructed to serve as baselines:

- iid shuffle (random permutation)
- Markov simulation (based on P)
- block shuffle (preserving local segments)

These allow comparison with the prime sequence.

---

## Block resampling

A method that shuffles contiguous segments of the sequence.

This preserves local structure while breaking global order.

---

## Local structure

Patterns that persist within short segments of the sequence.

Observed through block resampling.

---

## Higher-order structure

Structure present in Δ that is not captured by first-order transitions (P).

In this work:

The residual operator Δ exhibits higher-order structure.

---

## Interpretation

This work does not prove new theorems about primes.

It provides:

- a representation (transition operators)
- a diagnostic (Δ)
- a measurable structure (low-rank behavior)

---

## Key object

All results are centered on:

Δ = P^(2) − P²
