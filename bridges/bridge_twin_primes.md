# Bridge — Residue Transitions and the Twin Prime Conjecture

This note connects the residue-transition framework of this repository with the twin prime conjecture.

---

## Twin primes

A twin prime pair is:

\[
p,\; p+2
\]

with both values prime.

The twin prime conjecture states that infinitely many such pairs exist.

---

## Residue perspective modulo 30

For primes greater than \(5\),

\[
p \bmod 30 \in \{1,7,11,13,17,19,23,29\}.
\]

A twin prime pair corresponds to a residue transition

\[
r \to r+2 \pmod{30}.
\]

Among the reduced residue classes modulo \(30\), the twin-prime-compatible transitions are:

\[
11 \to 13,\quad 17 \to 19,\quad 29 \to 1.
\]

---

## Transition interpretation

In the transition operator \(P\),

\[
P_{ij} = \Pr(x_{n+1}=j \mid x_n=i),
\]

the twin-prime-compatible transitions correspond to the entries

\[
P_{11,13},\quad P_{17,19},\quad P_{29,1}.
\]

These entries measure how often consecutive-prime transitions align with twin-prime residue movement modulo \(30\).

---

## Residual operator

The residual operator is

\[
\Delta = P^{(2)} - P^2.
\]

This compares the observed two-step operator \(P^{(2)}\) with the first-order baseline \(P^2\).

---

## Twin-prime bridge

Twin-prime-compatible transitions can be tracked directly in \(P\), and related two-step structure can be tracked through the same entries or neighborhoods in \(\Delta\).

This does not prove the twin prime conjecture.

It provides a computational diagnostic for asking:

- how twin-prime-compatible transitions appear in the residue transition operator,
- how their frequencies compare with controls,
- how their behavior changes with sample size,
- whether local structure persists under block resampling.

---

## Operational experiment

The script

```text
scripts/twin_prime_transition_experiment.py
```

tracks the entries

```text
11 -> 13
17 -> 19
29 -> 1
```

across increasing prime sample sizes and saves:

```text
figures/twin_prime_transition_entries.png
```

---

## Summary

Twin primes correspond to specific residue transitions modulo \(30\).  
The transition framework gives a direct way to measure those entries and compare them with control sequences.
