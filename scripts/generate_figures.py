import os
import numpy as np
import matplotlib.pyplot as plt

from src.transitions import (
    primes_mod_30,
    build_transition_matrix,
    build_two_step_matrix,
    RESIDUES,
)
from src.residual import compute_delta
from src.spectrum import singular_values
from src.controls import iid_shuffle, block_shuffle

FIG_DIR = "figures"
os.makedirs(FIG_DIR, exist_ok=True)


def load_primes():
    # Preferred: save your prime list as data/primes.npy
    return np.load("data/primes.npy")


def delta_from_sequence(seq):
    P = build_transition_matrix(seq)
    P2 = build_two_step_matrix(seq)
    return P, P2, compute_delta(P, P2)


def fro_norm(M):
    return np.linalg.norm(M, ord="fro")


def plot_heatmap(matrix, title, filename, cmap="viridis"):
    plt.figure(figsize=(6, 5))
    plt.imshow(matrix, cmap=cmap)
    plt.colorbar()
    plt.xticks(range(len(RESIDUES)), RESIDUES)
    plt.yticks(range(len(RESIDUES)), RESIDUES)
    plt.title(title)
    plt.xlabel("Next residue")
    plt.ylabel("Current residue")
    plt.tight_layout()
    plt.savefig(os.path.join(FIG_DIR, filename), dpi=220)
    plt.close()


def plot_singular_values(spectra, filename):
    plt.figure(figsize=(6, 4))
    for label, values in spectra.items():
        plt.plot(values, marker="o", label=label)
    plt.xlabel("Component index")
    plt.ylabel("Value")
    plt.title("Low-rank structure of residual operator")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(FIG_DIR, filename), dpi=220)
    plt.close()


def make_controls(seq, P, n_controls=100, block_size=50, seed=42):
    rng = np.random.default_rng(seed)
    controls = {"iid": [], "markov": [], "block": []}

    n_states = P.shape[0]

    for _ in range(n_controls):
        controls["iid"].append(rng.permutation(seq))

        # Markov control in residue-index space, mapped back to residue labels
        idx_seq = [rng.integers(n_states)]
        for _ in range(len(seq) - 1):
            idx_seq.append(rng.choice(n_states, p=P[idx_seq[-1]]))
        controls["markov"].append(RESIDUES[np.array(idx_seq)])

        # Block shuffle
        blocks = [seq[i:i + block_size] for i in range(0, len(seq), block_size)]
        rng.shuffle(blocks)
        controls["block"].append(np.concatenate(blocks))

    return controls


def empirical_pvalue(real_value, null_values):
    null_values = np.asarray(null_values)
    return (np.sum(null_values >= real_value) + 1) / (len(null_values) + 1)


def main():
    primes = load_primes()
    seq = primes_mod_30(primes)

    P, P2, delta = delta_from_sequence(seq)

    # Figure 1
    plot_heatmap(
        P,
        "First-order transition operator P",
        "transition_operator_P_heatmap.png",
    )

    # Figure 2
    plot_heatmap(
        delta,
        r"Residual operator $\Delta = P^{(2)} - P^2$",
        "two_step_delta_heatmap.png",
        cmap="coolwarm",
    )

    # Controls
    controls = make_controls(seq, P, n_controls=100)

    control_deltas = {}
    for name, seqs in controls.items():
        control_deltas[name] = []
        for s in seqs:
            _, _, d = delta_from_sequence(s)
            control_deltas[name].append(d)

    # Figure 3: low-rank / singular value comparison
    spectra = {"prime": singular_values(delta)}
    for name, ds in control_deltas.items():
        spectra[name] = np.mean([singular_values(d) for d in ds], axis=0)

    plot_singular_values(
        spectra,
        "singular_spectrum_real_vs_null.png",
    )

    # Validation metrics
    real_l2 = fro_norm(delta)
    real_top = singular_values(delta)[0]

    metrics = {
        "L2 residual": {
            "real": real_l2,
            "nulls": {
                name: [fro_norm(d) for d in ds]
                for name, ds in control_deltas.items()
            },
        },
        "Top component": {
            "real": real_top,
            "nulls": {
                name: [singular_values(d)[0] for d in ds]
                for name, ds in control_deltas.items()
            },
        },
    }

    control_names = list(control_deltas.keys())
    metric_names = list(metrics.keys())

    p_matrix = np.zeros((len(metric_names), len(control_names)))
    ratio_matrix = np.zeros((len(metric_names), len(control_names)))

    for i, metric in enumerate(metric_names):
        real = metrics[metric]["real"]
        for j, control in enumerate(control_names):
            nulls = np.asarray(metrics[metric]["nulls"][control])
            p_matrix[i, j] = empirical_pvalue(real, nulls)
            ratio_matrix[i, j] = real / (np.mean(nulls) + 1e-12)

    # Figure 4: p-values
    plt.figure(figsize=(6, 4))
    plt.imshow(-np.log10(p_matrix), cmap="viridis")
    plt.colorbar(label=r"$-\log_{10}(p)$")
    plt.xticks(range(len(control_names)), control_names)
    plt.yticks(range(len(metric_names)), metric_names)
    plt.title("Statistical validation p-values")
    plt.tight_layout()
    plt.savefig(os.path.join(FIG_DIR, "stat_validation_pvalues.png"), dpi=220)
    plt.close()

    # Figure 5: summary ratios
    plt.figure(figsize=(6, 4))
    plt.imshow(ratio_matrix, cmap="viridis")
    plt.colorbar(label="real / null mean")
    plt.xticks(range(len(control_names)), control_names)
    plt.yticks(range(len(metric_names)), metric_names)
    plt.title("Summary ratios for empirical and control statistics")
    plt.tight_layout()
    plt.savefig(os.path.join(FIG_DIR, "publication_summary_ratios.png"), dpi=220)
    plt.close()

    print("Generated figures:")
    for name in [
        "transition_operator_P_heatmap.png",
        "two_step_delta_heatmap.png",
        "singular_spectrum_real_vs_null.png",
        "stat_validation_pvalues.png",
        "publication_summary_ratios.png",
    ]:
        print(" -", os.path.join(FIG_DIR, name))


if __name__ == "__main__":
    main()
