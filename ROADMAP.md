# Roadmap — Prime Numbers Lab

This roadmap outlines next steps for development, outreach, and research expansion.

---

## 🚀 Outreach

### Goal
Engage researchers in number theory, probabilistic primes, and related fields.

### Targets (lol)

- Terence Tao
- James Maynard
- Andrew Granville
- Jon Keating
- Peter Sarnak

### Tweet

Residue-class transitions of consecutive primes (mod 30):

Δ = P^(2) − P^2 shows low-rank structure.

Not explained by iid or Markov controls.

Paper + figures:
[link]

Curious if this connects to known results on prime gaps / zeta / random matrix behavior.

### Email

Subject:
Residue-class transitions of primes (Δ = P^(2) − P^2)

Body:

Hi,

I’ve been analyzing residue-class transitions of consecutive primes modulo 30.

Defining Δ = P^(2) − P^2, I observe low-rank structure in Δ that persists across sample sizes and differs from iid / Markov controls.

I wrote a short note with figures here:
[link to PDF]

I’d be curious if this connects to any known results or directions in prime gaps or related models.

Best,
Dan Hawkley

---

## 🔗 Cross-Repository Expansion

Create:

docs/bridge_zeta.md

Content:

- Compare Δ structure in prime transitions with zeta-constraint-lab
- Relate to spacing statistics and spectral structure
- Highlight shared idea: structured deviation from baseline

Conceptual alignment:

prime transitions (finite, local)
↔
zeta zeros (global, spectral)

---

## 🧪 Repository Expansion

### Experiments

- Change modulus (30 → 210)
- Increase sample size (N scaling)
- Add additional control models:
  - Cramér-style
  - Poisson gaps
  - biased Markov
- Sliding window analysis of Δ
- Study singular vectors (interpretation of structure)

---

## 🧱 Repository Improvements

Add:

docs/
  overview.md
  bridge_zeta.md

scripts/
  run_experiments.py

---

## 📈 Success Criteria

- Meaningful feedback from researchers
- Identification of related literature or models
- New experiment directions based on responses
