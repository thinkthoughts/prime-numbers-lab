# Prime Numbers Lab — Residue-Class Transitions of Consecutive Primes

![banner](banner.svg)

This repository accompanies the paper:

👉 `paper/main.pdf`

---

## 📌 Summary

Reducing consecutive primes modulo 30 yields a sequence over 8 residue states:

{1, 7, 11, 13, 17, 19, 23, 29}

From this sequence, we construct a transition operator P and compare the two-step operator P^(2) to the baseline P^2.

The residual operator

Δ = P^(2) − P^2

exhibits higher-order structure and admits a low-rank representation.

---

## 📄 Paper

See:

```
paper/main.pdf
```

---

## 📊 Figures

All publication figures are available in:

```
figures/
```

These include:

- transition operator heatmap  
- residual operator visualization  
- singular value spectrum  
- statistical validation  
- summary ratios  

---

## 📁 Repository Structure

```
paper/        # LaTeX source and compiled PDF
figures/      # publication-ready figures
src/          # core computation modules
scripts/      # reproducibility scripts
notebooks/    # exploratory analysis
```

---

## ▶️ Reproducibility

Install dependencies:

```bash
pip install -r requirements.txt
```

Generate all figures:

```bash
python scripts/generate_figures.py
```

---

## 🧭 Reference

If you use this work, cite the paper in `paper/main.pdf`.
