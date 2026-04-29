# Design Notes — Residue-Class Residual Decomposition

## Notebook role

Notebook 15 follows Notebook 14 by localizing normalized prime-gap residuals to residue classes.

## Constraint

The residue-conditioned residual is:

$$
\Delta(z;r)=f_{emp}(z\mid r)-e^{-z}.
$$

## Measurement

Metrics include residual L1, residual L2, JS divergence, positive/negative residual mass, and tail exceedance by residue class.

## CGCS score

$$
CGCS_{residue} =
\frac{1}{1+\overline{\|\Delta_r\|_1}+\overline{JS_r}+\sigma(\|\Delta_r\|_1)}.
$$

## Handoff

Notebook 16 should compare residue-class residual structure against randomized or shuffled controls.
