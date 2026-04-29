# Design Notes — Gap Distribution Residual Structure

## Notebook role

Notebook 13 follows Notebook 12 by moving from exponential distribution comparison to residual structure.

## Constraint

The constraint is the exponential baseline for normalized prime gaps:

$$
z = \frac{p_{n+1}-p_n}{\log p_n}, \quad f_0(z)=e^{-z}.
$$

## Measurement

The measured object is:

$$
\Delta(z,x)=f_{emp}(z,x)-e^{-z}.
$$

Metrics include residual L1, residual L2, JS divergence, signed residual mass, and tail bias.

## CGCS score

$$
CGCS_\Delta = \frac{1}{1+\overline{\|\Delta\|_1}+\overline{JS}}.
$$

## Handoff

Notebook 14 should test whether residual magnitude follows a scaling law such as $1/\log x$ or $1/(\log x)^\alpha$.
