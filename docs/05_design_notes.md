# Design Notes — Random vs Sieve

## Notebook role

Notebook 05 follows Notebook 04 by testing whether random removal can imitate sieve-retained prime structure.

Notebook 04 showed layered sieve mechanism.
Notebook 05 uses random controls to show that matched retention does not imply matched structure.

## Sets

1. sieve_primes
2. random_count_matched
3. random_layer_matched

## Measurements

1. residue distribution modulo 6
2. gap distribution
3. density by scale
4. layer retention
5. recovery score against prime set

## CGCS score

CGCS_recovery(S) = |S ∩ P_N| / |P_N|.

## Core claim

Same count does not imply same structure.

## Figures

1. residue comparison modulo 6
2. gap histogram comparison
3. density by scale
4. layer retention comparison
5. recovery score comparison

## Handoff

Notebook 06 should test recoverability under partial observation.
