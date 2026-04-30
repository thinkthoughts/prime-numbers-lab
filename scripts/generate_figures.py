import os
import numpy as np
import matplotlib.pyplot as plt

from src.transitions import (
    primes_mod_30,
    build_transition_matrix,
    build_two_step_matrix,
    RESIDUES
)
from src.residual import compute_delta
from src.spectrum import singular_values
from src.controls import iid_shuffle, block_shuffle

# ------------------------
# CONFIG
# ------------------------

FIG_DIR = "figures"
os.makedirs(FIG_DIR, exist_ok=True)

# TODO: replace with your actual prime loader
def load_primes():
    # Example placeholder
    # Replace with your actual prime list (file or generator)
    return np.load("data/primes.npy")

# ------------------------
# PLOTTING HELPERS
# ------------------------

def plot_heatmap(matrix, title, filename):
    plt.figure(figsize=(6,5))
    plt.imshow(matrix, cmap="viridis")
    plt.colorbar()
    plt.xticks(range(len(RESIDUES)), RESIDUES)
    plt.yticks(range(len(RESIDUES)), RESIDUES)
    plt.title(title)
    plt.tight_layout()
    plt.savefig(os.path.join(FIG_DIR, filename), dpi=200)
    plt.close()

def plot_singular_values(s_real, s_control, filename):
    plt.figure(figsize=(6,4))

    plt.plot(s_real, marker="o", label="Δ (prime sequence)")
    plt.plot(s_control, linestyle="--", label="control")

    plt.xlabel("Index")
    plt.ylabel("Singular value")
    plt.title("Singular value spectrum")
    plt.legend()
    plt.tight_layout()

    plt.savefig(os.path.join(FIG_DIR, filename), dpi=200)
    plt.close()

# ------------------------
# MAIN PIPELINE
# ------------------------

def main():
    print("Loading primes...")
    primes = load_primes()

    print("Building sequence...")
    seq = primes_mod_30(primes)

    print("Computing operators...")
    P = build_transition_matrix(seq)
    P2 = build_two_step_matrix(seq)
    delta = compute_delta(P, P2)

    # ------------------------
    # FIGURE 1: Transition matrix
    # ------------------------
    plot_heatmap(
        P,
        "Transition operator P",
        "transition_operator_P_heatmap.png"
    )

    # ------------------------
    # FIGURE 2: Residual Δ
    # ------------------------
    plot_heatmap(
        delta,
        "Residual Δ = P^(2) − P^2",
        "two_step_delta_heatmap.png"
    )

    # ------------------------
    # FIGURE 3: Singular spectrum
    # ------------------------
    s_real = singular_values(delta)

    # simple control: iid shuffle
    seq_iid = iid_shuffle(seq)
    P_iid = build_transition_matrix(seq_iid)
    P2_iid = build_two_step_matrix(seq_iid)
    delta_iid = compute_delta(P_iid, P2_iid)

    s_control = singular_values(delta_iid)

    plot_singular_values(
        s_real,
        s_control,
        "singular_spectrum_real_vs_null.png"
    )

    print("Figures generated in:", FIG_DIR)


if __name__ == "__main__":
    main()
