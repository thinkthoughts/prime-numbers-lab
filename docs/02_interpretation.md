# Prime Gaps

## Constraint result

This notebook measured prime gaps

g_n = p_(n+1) - p_n

for primes below 1,000,000 and compared gap behavior to the logarithmic baseline log(p_n).

## Continues

The ordered prime sequence continues across scale. Gaps provide local measurements of that continuation.

## Remains under constraint

Mean gap behavior remains comparable to logarithmic scale. For p_n >= 100:

- mean gap = 12.741895
- mean log(p_n) = 12.722839
- median gap = 10.000000
- max gap = 114

## Drift

Drift was measured as |g_n - log(p_n)| / log(p_n).

- mean relative drift after 100 = 0.599699
- median relative drift after 100 = 0.533585

## CGCS score

CGCS_gap_logscale = 1 / (1 + mean relative drift)

Measured score:

- CGCS_gap_logscale = 0.625118

## Recoverability

The logarithmic baseline recovers coarse gap scale, especially in aggregate windows. It does not recover exact gaps.

## Caution

This notebook does not solve prime gaps, prove RH, or claim exact predictability. It measures gap structure and drift relative to a classical scale baseline.
