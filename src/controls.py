import numpy as np

def iid_shuffle(seq):
    return np.random.permutation(seq)

def markov_simulate(P, length, start_idx=0):
    n = P.shape[0]
    seq = [start_idx]

    for _ in range(length - 1):
        current = seq[-1]
        next_state = np.random.choice(n, p=P[current])
        seq.append(next_state)

    return np.array(seq)

def block_shuffle(seq, block_size=50):
    blocks = [seq[i:i+block_size] for i in range(0, len(seq), block_size)]
    np.random.shuffle(blocks)
    return np.concatenate(blocks)
