import numpy as np

def singular_values(M):
    return np.linalg.svd(M, compute_uv=False)

def low_rank_approx(M, k):
    U, S, Vt = np.linalg.svd(M, full_matrices=False)
    S[k:] = 0
    return U @ np.diag(S) @ Vt
