# Residue Classes mod 6

## Constraint result

This notebook tested the residue constraint

p > 3 => p mod 6 in {1,5}.

For primes below 1,000,000, the measured score was:

- CGCS_mod6 = 1.000000
- drift_mod6 = 0.000000

## Remains under constraint

Every prime greater than 3 remained in residue classes 1 or 5 modulo 6.

## Drift

Invalid residue classes 0, 2, 3, and 4 modulo 6 had zero representation among primes greater than 3. They drift out by divisibility.

## Recoverability

Modulo 6 recovers prime candidate classes, not primes exactly. Many integers congruent to 1 or 5 modulo 6 are composite.

## Caution

This notebook does not prove RH and does not provide a sufficient primality test. It provides the first direct measurement of structure remaining under a finite residue constraint.
