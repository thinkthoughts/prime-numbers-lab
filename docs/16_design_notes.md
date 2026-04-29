# Design Notes — Transition Operator, Entropy, and Mixing

## Notebook role

Notebook 16 follows Notebook 15 by turning residue-class residual structure into a transition operator.

## Constraint

The main object is:

$$
P_{ij}=\Pr(r_{n+1}=j\mid r_n=i).
$$

## Measurement

Metrics include stationary distribution, entropy, spectral gap proxy, mixing distance, transition lift, transition-conditioned residuals, residual-weighted transition mass, and windowed transition drift.

## CGCS score

$$
CGCS_{transition} =
\frac{1}{1+d(\pi,U)+(1-\overline{H})+\lambda_2}.
$$

## Handoff

Notebook 17 should test higher-order transitions or compare first-order transition memory against shuffled baselines.
