import numpy as np

RESIDUES = np.array([1,7,11,13,17,19,23,29])
RES_IDX = {r: i for i, r in enumerate(RESIDUES)}

def primes_mod_30(primes):
    return np.array([p % 30 for p in primes if p > 5])

def build_transition_matrix(seq):
    n = len(RESIDUES)
    P = np.zeros((n, n))

    for i in range(len(seq) - 1):
        a, b = seq[i], seq[i+1]
        if a in RES_IDX and b in RES_IDX:
            P[RES_IDX[a], RES_IDX[b]] += 1

    row_sums = P.sum(axis=1, keepdims=True)
    row_sums[row_sums == 0] = 1
    return P / row_sums

def build_two_step_matrix(seq):
    n = len(RESIDUES)
    P2 = np.zeros((n, n))

    for i in range(len(seq) - 2):
        a, b = seq[i], seq[i+2]
        if a in RES_IDX and b in RES_IDX:
            P2[RES_IDX[a], RES_IDX[b]] += 1

    row_sums = P2.sum(axis=1, keepdims=True)
    row_sums[row_sums == 0] = 1
    return P2 / row_sums
