import matplotlib.patches as patches
import matplotlib.pyplot as plt


def visualize_measure_as_base():
    fig, ax = plt.subplots(figsize=(10, 4))

    # Assume the function value (height) is 2 over two disjoint intervals.
    # Interval 1: [1, 3] (length 2)
    # Interval 2: [5, 6] (length 1)
    height = 2
    x_intervals = [(1, 3), (5, 6)]

    # Mathematical description of Set A
    # A = [1, 3] U [5, 6]
    # mu(A) = (3-1) + (6-5) = 3

    # Plotting the graph
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 3)
    ax.set_xlabel("x")
    ax.set_ylabel("Function Value")

    # 1. Draw the disjoint blocks (the actual shape of the function)
    total_width = 0
    colors = ["skyblue", "lightgreen"]

    for i, (start, end) in enumerate(x_intervals):
        width = end - start
        total_width += width

        # Rectangle
        rect = patches.Rectangle(
            (start, 0),
            width,
            height,
            linewidth=1.5,
            edgecolor="blue",
            facecolor=colors[i],
            alpha=0.6,
        )
        ax.add_patch(rect)

        # Annotation for width
        ax.text(
            start + width / 2,
            -0.3,
            f"Width={width}",
            ha="center",
            va="top",
            color="blue",
        )
        ax.text(
            start + width / 2,
            height / 2,
            f"Part {i + 1}",
            ha="center",
            va="center",
            color="white",
            fontweight="bold",
        )

    # 2. Conceptual diagram of the "base" (Measure mu(A))
    # This illustrates the conceptual image for the integration calculation.

    # Use an arrow to show the "summing up" process
    ax.annotate(
        r"Summing up widths\n(Measure $\mu(A)$)",
        xy=(3.5, height),
        xytext=(3.5, height + 0.5),
        ha="center",
        va="bottom",
        fontsize=10,
        arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
    )

    # Display formulas
    info_text = (
        f"Function Value (Height) = {height}\n"
        f"Set $A = [1, 3] \\cup [5, 6]$\n"
        f"Measure $\\mu(A) = (3-1) + (6-5) = {total_width}$ (Total Base)\n\n"
        f"Integral Contribution = Height $\\times$ $\\mu(A)$\n"
        f"                      = {height} $\\times$ {total_width} = {height * total_width}"
    )

    # Position the text box
    props = dict(boxstyle="round", facecolor="wheat", alpha=0.3)
    ax.text(
        0.05,
        0.95,
        info_text,
        transform=ax.transAxes,
        fontsize=12,
        verticalalignment="top",
        bbox=props,
    )

    ax.set_title(r'Why $\mu(A)$ is the "Base": Summing disjoint intervals')

    # Ground line
    ax.axhline(0, color="black", linewidth=1)

    plt.tight_layout()
    plt.savefig("measure_visual.png")
    plt.show()


visualize_measure_as_base()
