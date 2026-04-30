from src.transitions import primes_mod_30, build_transition_matrix, build_two_step_matrix
from src.residual import compute_delta

# Example: assume you already have primes list
primes = [...]  

seq = primes_mod_30(primes)
P = build_transition_matrix(seq)
P2 = build_two_step_matrix(seq)

delta = compute_delta(P, P2)

print(delta)
