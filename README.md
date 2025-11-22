# Comparison of Riemann and Lebesgue Integration

This project provides Python scripts to visualize and simulate the fundamental differences between Riemann and Lebesgue integration, two core concepts in mathematical analysis.

- `visualize_lebesgue_integral.py`: Compares the two integration methods for a simple, well-behaved continuous function, `f(x) = x^2`.
- `dirichlet_integration.py`: Demonstrates the power of Lebesgue integration by applying it to the Dirichlet function, a classic case where the Riemann integral fails.

## Key Differences Illustrated by the Code

### 1. Partitioning Strategy: Domain vs. Range

The fundamental difference lies in how the area under the curve is partitioned and summed.

- **Riemann Integration (`visualize_lebesgue_integral.py`)**:
  - **Strategy**: Partitions the **domain** (the x-axis) into small vertical rectangles.
  - **Question**: "For each small interval on the x-axis, what is the function's height?"
  - **Calculation**: Sums the areas of these vertical rectangles (`height * width`). For a function `f(x)`, the integral is approximated by `Σ f(x_i) * Δx_i`.

  ![Riemann Integration](https://i.imgur.com/rSDRi7g.png)
  *(Image generated from `visualize_lebesgue_integral.py`)*

- **Lebesgue Integration (`visualize_lebesgue_integral.py`)**:
  - **Strategy**: Partitions the **range** (the y-axis) and measures the corresponding sets in the domain.
  - **Question**: "For a given small range of function values (y-values), what is the total size (measure) of the set of x-values that map into this range?"
  - **Calculation**: Sums the products of the function value and the measure of the corresponding set (`value * measure`). The integral is approximated by `Σ y_i * μ(A_i)`, where `μ(A_i)` is the measure of the set where `f(x)` is approximately `y_i`.

  ![Lebesgue Integration](https://i.imgur.com/rSDRi7g.png)
  *(Image generated from `visualize_lebesgue_integral.py`)*

For a simple continuous function like `f(x) = x^2`, both methods converge to the same result, as shown in `visualize_lebesgue_integral.py`. The Riemann sum and the Lebesgue-style sum both approximate the true value of 1/3.

### 2. Power and Applicability: The Dirichlet Function

The true strength of the Lebesgue integral becomes apparent with more complex, "pathological" functions.

- **The Dirichlet Function (`dirichlet_integration.py`)**:
  This function is defined as:
  - `f(x) = 1` if `x` is a rational number
  - `f(x) = 0` if `x` is an irrational number

- **Riemann Integral Failure**:
  The Riemann integral of the Dirichlet function **does not exist**. In any partition of the x-axis, no matter how small, each subinterval will contain both rational and irrational numbers.
  - The **upper sum** (using the supremum of `f(x)` in each interval) will always be `1`.
  - The **lower sum** (using the infimum) will always be `0`.
  Since the upper and lower sums never converge to the same value, the function is not Riemann-integrable.

- **Lebesgue Integral Success**:
  The Lebesgue integral handles this case elegantly by partitioning the range (`{0, 1}`).
  1.  It considers the value `y = 1`. The set of `x` where `f(x) = 1` is the set of rational numbers, **Q**. The "size" or **measure** of the rational numbers is **0** (`μ(Q) = 0`).
  2.  It considers the value `y = 0`. The set of `x` where `f(x) = 0` is the set of irrational numbers. The measure of the irrational numbers in the interval [0, 1] is **1**.

  The Lebesgue integral is therefore calculated as:
  `(value_1 * measure_of_set_1) + (value_2 * measure_of_set_2)`
  `= (1 * μ(Q)) + (0 * μ(Irrationals))`
  `= (1 * 0) + (0 * 1) = 0`

The simulation in `dirichlet_integration.py` confirms this by using a Monte Carlo method. It "throws" 100,000 random points at the interval [0, 1] and counts how many "hit" a rational number. The result is that virtually no throws land on a rational number, visually demonstrating that the measure of the set of rational numbers is zero.

![Dirichlet Simulation](https://i.imgur.com/jZ2x3Y0.png)
*(Image generated from `dirichlet_integration.py`)*