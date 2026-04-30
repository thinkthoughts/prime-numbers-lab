import numpy as np

def compute_delta(P, P2):
    return P2 - P @ P
