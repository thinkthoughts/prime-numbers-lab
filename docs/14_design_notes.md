# Design Notes — Residual Scaling Law

## Notebook role

Notebook 14 follows Notebook 13 by fitting a scale law to residual magnitude.

## Constraint

The residual is:

$$
\Delta(z,x)=f_{emp}(z,x)-e^{-z}.
$$

The fitted scale law is:

$$
\|\Delta(z,x)\| \sim C(\log x)^{-\alpha}.
$$

## Measurement

Metrics include residual L1, residual L2, JS divergence, positive/negative residual mass, tail bias, and fit residuals.

## CGCS score

$$
CGCS_{scale} =
\frac{1}{1+\overline{\|\Delta\|_1}+\overline{JS}+\overline{|r_{fit}|}}.
$$

## Handoff

Notebook 15 should decompose residuals by residue class or local arithmetic structure.
