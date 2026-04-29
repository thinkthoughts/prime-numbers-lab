# Prime Numbers Lab — Residue Transition Structure

This repository studies higher-order structure in consecutive prime gaps via residue-class transitions modulo 30.

## Pipeline

- **Notebook 16** — Transition operator (first-order)
- **Notebook 17** — Higher-order memory (two-step)
- **Notebook 18** — Low-rank spectral decomposition
- **Notebook 19** — Operator dynamics + validation
- **Notebook 20** — Synthetic controls
- **Notebook 21** — Statistical validation layer
- **Notebook 22** — Publication figure pack
- **Notebook 23** — Full paper generator

## Key Result

We identify statistically significant higher-order structure in prime-gap residue transitions that is not explained by:

- iid shuffle
- first-order Markov models
- simple control baselines

The residual operator admits a low-rank decomposition, indicating structured memory beyond first-order dynamics.

## Figures

See `/figures/` for publication-ready outputs.

## Reproducibility

```bash
pip install -r requirements.txt
