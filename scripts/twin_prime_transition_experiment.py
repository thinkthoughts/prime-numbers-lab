"""
Twin-prime-compatible residue transition experiment.

Tracks the entries:

    11 -> 13
    17 -> 19
    29 -> 1

in the first-order transition operator P across increasing prime sample sizes.

Expected project structure:

    data/primes.npy
    src/transitions.py
    figures/

Run:

    python scripts/twin_prime_transition_experiment.py
"""

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

from src.transitions import primes_mod_30, build_transition_matrix, RESIDUES


FIG_DIR = Path("figures")
FIG_DIR.mkdir(exist_ok=True)

DATA_PATH = Path("data/primes.npy")

TWIN_TRANSITIONS = [
    (11, 13),
    (17, 19),
    (29, 1),
]


def load_primes(path=DATA_PATH):
    if not path.exists():
        raise FileNotFoundError(
            f"Missing {path}. Save a prime list as data/primes.npy "
            "or edit load_primes() to use your prime generator."
        )
    return np.load(path)


def transition_entry(P, src, dst):
    idx = {int(r): i for i, r in enumerate(RESIDUES)}
    return P[idx[src], idx[dst]]


def sample_sizes(n_total):
    candidates = [
        1_000,
        3_000,
        10_000,
        30_000,
        100_000,
        300_000,
        1_000_000,
        3_000_000,
        10_000_000,
    ]
    return [n for n in candidates if n <= n_total]


def main():
    primes = load_primes()
    sizes = sample_sizes(len(primes))

    if not sizes:
        raise ValueError("Need at least 1,000 primes for the default sample schedule.")

    results = {f"{a}->{b}": [] for a, b in TWIN_TRANSITIONS}

    for n in sizes:
        seq = primes_mod_30(primes[:n])
        P = build_transition_matrix(seq)

        for a, b in TWIN_TRANSITIONS:
            results[f"{a}->{b}"].append(transition_entry(P, a, b))

    plt.figure(figsize=(7.5, 4.8))

    for label, values in results.items():
        plt.plot(sizes, values, marker="o", label=label)

    plt.xscale("log")
    plt.xlabel("Number of primes used")
    plt.ylabel("Transition probability")
    plt.title("Twin-prime-compatible residue transitions modulo 30")
    plt.legend(title="Transition")
    plt.tight_layout()

    out = FIG_DIR / "twin_prime_transition_entries.png"
    plt.savefig(out, dpi=220)
    plt.close()

    print(f"Saved {out}")

    # Also save CSV
    csv_out = FIG_DIR / "twin_prime_transition_entries.csv"
    header = ["N"] + list(results.keys())
    rows = []
    for i, n in enumerate(sizes):
        rows.append([n] + [results[label][i] for label in results])

    with csv_out.open("w") as f:
        f.write(",".join(header) + "\n")
        for row in rows:
            f.write(",".join(map(str, row)) + "\n")

    print(f"Saved {csv_out}")


if __name__ == "__main__":
    main()
