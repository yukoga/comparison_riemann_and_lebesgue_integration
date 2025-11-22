import random

import matplotlib.pyplot as plt
import numpy as np


def simulate_dirichlet_integration():
    rational_targets = set()  # group of rational numbers.
    # We would count all fraction which denominator is less than or equal to 0.
    max_denominator = 100

    for q in range(1, max_denominator + 1):
        for p in range(1, q):
            if np.gcd(p, q) == 1:
                rational_targets.add(p / q)

    print(
        f"The number of target rational numbers (denominator <= {max_denominator}) : {len(rational_targets)}"
    )

    # Monte Carlo integration
    n_throws = 100_000

    throws = np.random.uniform(0, 1, n_throws)
    epsilon = 1e-9

    target_arr = np.array(list(rational_targets))

    print(f"\n--- Start {n_throws} trials. ----")

    n_hits = 0
    for v in throws:
        if v in rational_targets:
            n_hits += 1

    # Visualization
    fig, ax = plt.subplots(figsize=(12, 6))
    for r in list(rational_targets)[:500]:
        ax.axvline(x=r, color="blue", alpha=0.3, linewidth=1, ymax=0.2)

    random_samples = throws[:200]
    ax.scatter(
        random_samples,
        [0.1] * 200,
        color="red",
        s=10,
        label="random trials to hit rational numbers",
        zorder=3,
    )

    ax.text(
        0.5,
        0.25,
        "Blue Lines = Rational Targets (Measure 0)",
        color="blue",
        ha="center",
    )
    ax.text(
        0.5,
        0.05,
        "Red Dots = Random Throws (Simulating Measure)",
        color="red",
        ha="center",
    )
    ax.set_title(
        f"Dirichlet Function Simulation\nTotal Throws: {n_throws}, Hits: {n_hits} -> Integral ≈ 0"
    )
    ax.set_yticks([])
    ax.set_xlim(0, 1)
    plt.legend(loc="upper right")
    plt.show()

    # Lesbegue integration
    measure_rationals = 0
    measure_irrationals = 1

    lebesgue_integral = (1 * measure_rationals) + (0 * measure_irrationals)
    print(f"\nResults")
    print(f"Prob. that hits rational numbers (approx. measure): {n_hits / n_throws}")
    print(f"Lebesgue integral: 1 * 0 + 0 * 1 = {lebesgue_integral}")


if __name__ == "__main__":
    simulate_dirichlet_integration()
