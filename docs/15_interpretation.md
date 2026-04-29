# Residue-Class Residual Decomposition

## Constraint result

This notebook decomposes normalized prime-gap residuals by residue class.

The residue-conditioned residual is:

$$
\Delta(z;r)=f_{emp}(z\mid r)-e^{-z}.
$$

## Remains under constraint

The exponential envelope remains visible globally, while residue-conditioned buckets retain structured finite deviations.

## Drift

The strongest anchor-residue class by L1 residual is:

- anchor residue mod30 = 19
- L1 residual = 1.002344
- JS divergence = 0.206592

The strongest gap-residue class by L1 residual is:

- gap residue mod30 = 0
- L1 residual = 1.817942
- JS divergence = 0.562370

The strongest transition by L1 residual is:

- transition = 1->1
- L1 residual = 1.839074
- JS divergence = 0.573645

## Recoverability

Residual structure is recoverable as a finite residue-class diagnostic:

- anchor residue residual mass
- gap residue residual mass
- transition residual mass
- windowed residue heatmaps
- strongest residue residual curves

## CGCS score

The residue agreement score is:

$$
CGCS_{residue} =
\frac{1}{1+\overline{\|\Delta_r\|_1}+\overline{JS_r}+\sigma(\|\Delta_r\|_1)}.
$$

Measured score:

$$
CGCS_{residue} = 0.458698.
$$

## Caution

This notebook does not prove an asymptotic theorem.

It measures finite residue-class residual structure relative to the exponential heuristic.

## Figures

### Figure 1 — 15 Anchor Mod30 Residual Mass

![Figure 1](../figures/15_anchor_mod30_residual_mass.png)

### Figure 2 — 15 Gap Mod30 Residual Mass

![Figure 2](../figures/15_gap_mod30_residual_mass.png)

### Figure 3 — 15 Anchor Mod30 Js Divergence

![Figure 3](../figures/15_anchor_mod30_js_divergence.png)

### Figure 4 — 15 Tail Exceedance By Anchor Mod30

![Figure 4](../figures/15_tail_exceedance_by_anchor_mod30.png)

### Figure 5 — 15 Mean Z By Anchor Mod30

![Figure 5](../figures/15_mean_z_by_anchor_mod30.png)

### Figure 6 — 15 Transition Mod30 Residual Mass Top20

![Figure 6](../figures/15_transition_mod30_residual_mass_top20.png)

### Figure 7 — 15 Windowed Anchor Mod30 L1 Heatmap

![Figure 7](../figures/15_windowed_anchor_mod30_l1_heatmap.png)

### Figure 8 — 15 Strongest Residue Residual Curves

![Figure 8](../figures/15_strongest_residue_residual_curves.png)

### Figure 9 — 15 Windowed Js Divergence Vs Scale

![Figure 9](../figures/15_windowed_js_divergence_vs_scale.png)

### Figure 10 — 15 Residue Concentration Score

![Figure 10](../figures/15_residue_concentration_score.png)

### Figure 11 — 15 Final Window Residue Pdfs Vs Exp1

![Figure 11](../figures/15_final_window_residue_pdfs_vs_exp1.png)

