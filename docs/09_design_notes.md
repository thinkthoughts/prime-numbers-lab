# Design Notes — Windowed Reconstruction Stability

## Notebook role

Notebook 09 follows Notebook 08 by testing reconstruction stability across sliding windows.

## Motivation

Global F1 and global density can saturate. Windowed diagnostics expose local failures.

## Methods

1. raw observation
2. sieve-cleaned observation
3. density-only reconstruction
4. local-gap reconstruction

## Window diagnostics

1. window density error
2. window gap drift
3. window precision
4. window recovery
5. unstable density-window count
6. unstable gap-window count

## Core claim

Global reconstruction can look successful while local windows expose density, gap, and stability failures.

## Handoff

Notebook 10 should test adaptive reconstruction by modifying candidate scores in unstable windows.
