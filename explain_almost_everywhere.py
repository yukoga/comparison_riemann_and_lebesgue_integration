import numpy as np


def explain_almost_everywhere():
    n_samples = 1_000_000  # 1 million trials

    # Random x values from 0 to 1
    x = np.random.uniform(0, 1, n_samples)

    # --- Function f(x): A standard constant function ---
    # f(x) = 1
    y_f = np.ones_like(x)

    # --- Function g(x): f(x) with "noise" added ---
    # Set a spike that becomes 100 million only when x = 0.5
    # Change the value for a tiny fraction of rational numbers (floating-point numbers on a computer)

    y_g = np.ones_like(x)

    # A simulation to forcibly overwrite a "specific value"
    # (Note: The mathematical probability of a random real number x being exactly 0.5 is zero)
    # Here, we confirm that "a dart does not hit a location with measure zero"

    # Logic to change the value if, by some miracle, x = 0.5 occurs
    spike_indices = np.where(x == 0.5)
    y_g[spike_indices] = 100_000_000  # 100 million

    # Integral value (mean value * interval length of 1)
    integral_f = np.mean(y_f) * 1.0
    integral_g = np.mean(y_g) * 1.0

    print(f"Integral of f(x) = 1: {integral_f}")
    print(f"Integral of g(x) = 1 (but 100 million at x=0.5): {integral_g}")

    if integral_f == integral_g:
        print("\n[Conclusion] The two integrals are exactly the same.")
        print("A random dart (the measure) does not hit a point with no width (x=0.5).")
        print(
            "In other words, changing the value on a set of measure zero does not affect the integration result."
        )
    else:
        print("A difference occurred (a very rare case, or a calculation error).")


explain_almost_everywhere()
