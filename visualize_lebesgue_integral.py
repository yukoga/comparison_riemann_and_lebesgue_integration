import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np


def visualize_integration_comparison():
    def f(x):
        return x**2

    x_min, x_max = 0, 1
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # --- 1. Riemann Sum ---
    # devide x-axis
    n_divisions = 10
    x = np.linspace(x_min, x_max, 100)
    x_bins = np.linspace(x_min, x_max, n_divisions + 1)

    riemann_sum = 0
    ax1.plot(x, f(x), "k-", linewidth=1.5, label="$f(x)=x^2$")

    for i in range(n_divisions):
        # Left riemann sum.
        xi = x_bins[i]
        width = x_bins[i + 1] - x_bins[i]
        height = f(xi)
        area = width * height
        riemann_sum += area

        # drar rectangle.
        rect = patches.Rectangle(
            (xi, 0),
            width,
            height,
            linewidth=1,
            edgecolor="r",
            facecolor="red",
            alpha=0.3,
        )
        ax1.add_patch(rect)

    ax1.set_title(f"Riemann Integration (Splitting X-axis)\nSum ≈ {riemann_sum:.4f}")
    ax1.set_xlabel("x (Domain)")
    ax1.set_ylabel("y (Value)")
    ax1.set_xlim(0, 1.05)
    ax1.set_ylim(0, 1.05)

    # --- 2. Lebesgue Sum ---
    # Devide y-axis - simple function approx.
    y_bins = np.linspace(0, 1, n_divisions + 1)
    lebesgue_sum = 0
    ax2.plot(x, f(x), "k-", linewidth=1.5)

    # define color map.
    cmap = plt.get_cmap("viridis")

    for i in range(n_divisions):
        y_lower = y_bins[i]
        y_upper = y_bins[i + 1]

        # Find the x range (inverse image) that corresponds to this y range
        # y = x^2 => x = sqrt(y)
        x_start = np.sqrt(y_lower)
        x_end = np.sqrt(y_upper)

        # Measure (in this case, the length of the x interval)
        measure = x_end - x_start

        # Lebesgue sum = value (approximated by lower limit) × measure
        term = y_lower * measure
        lebesgue_sum += term

        # Draw a horizontal area (visual image)
        # Fill the height of y with y_lower for the range of x
        rect = patches.Rectangle(
            (x_start, 0),
            measure,
            y_lower,
            linewidth=0,
            facecolor=cmap(i / n_divisions),
            alpha=0.5,
        )
        ax2.add_patch(rect)

        # A line indicating which range was calculated
        ax2.hlines(y_lower, 0, x_end, colors="gray", linestyles=":", alpha=0.5)

    ax2.set_title(
        f"Lebesgue-style Integration (Splitting Y-axis)\nSum ≈ {lebesgue_sum:.4f}"
    )
    ax2.set_xlabel("x (Measure Space)")
    ax2.set_ylabel("y (Value Partition)")
    ax2.set_xlim(0, 1.05)
    ax2.set_ylim(0, 1.05)

    plt.show()

    # Actual integral value 1/3 = 0.333...
    print(f"Riemann Sum:  {riemann_sum:.5f}")
    print(f"Lebesgue Sum: {lebesgue_sum:.5f}")
    print(f"True Value:   {1 / 3:.5f}")


if __name__ == "__main__":
    visualize_integration_comparison()
