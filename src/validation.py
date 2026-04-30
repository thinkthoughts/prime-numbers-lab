import numpy as np

def frobenius_norm(M):
    return np.linalg.norm(M, ord="fro")

def compare_norms(delta_real, delta_controls):
    real_norm = frobenius_norm(delta_real)
    control_norms = [frobenius_norm(d) for d in delta_controls]
    return real_norm, control_norms
