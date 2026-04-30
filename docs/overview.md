# Overview — Residue-Class Transitions of Consecutive Primes

This repository presents a simple way to view consecutive primes as a finite dynamical system and measure where first-order models fail.

---

## Starting point

Take consecutive primes:

p₁, p₂, p₃, ...

Reduce them modulo 30:

xₙ = pₙ mod 30

For primes greater than 5, this produces a sequence over 8 states:

{1, 7, 11, 13, 17, 19, 23, 29}

---

## Transition view

From this sequence, construct a transition operator P:

Pᵢⱼ = frequency of transitions from residue i to residue j

This gives a first-order description of how residues evolve from one prime to the next.

---

## First-order expectation

If the process were memoryless (Markov), then two-step behavior would satisfy:

P^(2) ≈ P²

where:
- P^(2) is computed directly from (xₙ, xₙ₊₂)
- P² is the matrix square of P

---

## Residual operator

Define:

Δ = P^(2) − P²

Δ measures deviation from the first-order model.

---

## Observation

Across large samples of primes:

- Δ is not uniform
- Δ is low-rank
- a small number of components capture most of its mass

This indicates structured deviation from the first-order model.

---

## Interpretation

This is not a new theorem about primes.

It is a representation:

- primes → finite state sequence  
- transitions → operator P  
- deviation → operator Δ  

Δ provides a measurable object for studying higher-order structure in prime transitions.

---

## Controls

To test this structure, the same pipeline is applied to:

- iid shuffled sequences  
- Markov simulations based on P  
- block-resampled sequences  

These provide baselines for comparison.

---

## What this offers

This framework provides:

- a compact representation of prime transitions  
- a way to measure deviation from simple models  
- a bridge between combinatorial data and spectral structure  

---

## Relation to other work

This perspective can be compared with:

- probabilistic models of primes (e.g., Cramér-type models)  
- Markov approximations  
- spectral approaches (e.g., random matrix analogies)  

The goal is not to replace these, but to provide a compatible observable.

---

## Repository structure

- `paper/main.pdf` — main result  
- `figures/` — visualizations used in the paper  
- `src/` — core computations  
- `scripts/` — reproducibility tools  
- `notebooks/` — exploratory analysis  
- `docs/` — explanations and glossary  

---

## Key object

All results center on:

Δ = P^(2) − P²

---

## How to read this work

1. Read `paper/main.pdf` (short, complete statement)
2. View figures in `/figures/`
3. Use this document and the glossary for context
4. Explore `src/` or notebooks if needed

---

## Summary

This repository shows that residue-class transitions of consecutive primes can be studied through a small matrix system, and that deviations from first-order models appear as low-rank structure in the residual operator Δ.
