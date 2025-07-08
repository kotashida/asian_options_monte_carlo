# Project: Pricing Asian Options using Monte Carlo Simulation

## Introduction

This project provides a Python-based implementation for pricing Asian options, a type of path-dependent exotic option, using Monte Carlo simulation. Standard option pricing models, like the Black-Scholes formula, are not suitable for exotic options whose payoffs depend on the asset's price path. This project focuses on pricing an **Asian Option**, where the payoff is determined by the average price of the underlying asset over a specified period.

The simulation is built from scratch using standard Python libraries, demonstrating a practical application of stochastic calculus, numerical methods, and computational finance without relying on expensive financial software.

## Project Structure

```
.
├── asian_option_pricer.py
├── README.md
├── requirements.txt
└── results/
    ├── payoff_distribution.png
    └── sample_paths.png
```

## Technology Stack

This project is implemented using Python 3 and the following libraries:

*   **NumPy:** For efficient numerical operations and array handling.
*   **Matplotlib:** For visualizing the simulation results.
*   **SciPy:** (Included in `requirements.txt` for completeness, though not used in the basic simulation).

## How to Set Up and Run the Project

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd exotic_options_monte_carlo
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the simulation:**
    ```bash
    python asian_option_pricer.py
    ```

## Implementation Details

The core of the project is the `asian_option_pricer.py` script, which performs the following steps:

1.  **Models the Underlying Asset:** The script simulates the price path of an underlying stock using the **Geometric Brownian Motion (GBM)** model. The `simulate_gbm_path` function generates a single price path based on the initial stock price, drift, volatility, and time parameters.

2.  **Monte Carlo Simulation:** The script runs a large number of GBM simulations (e.g., 10,000 paths) to generate a wide distribution of possible future price scenarios.

3.  **Calculates Payoffs:** For each simulated path, it calculates the average stock price and determines the payoff of the Asian call option using the formula: `max(0, AveragePrice - StrikePrice)`.

4.  **Estimates Option Price:** The final estimated price of the Asian option is the average of all simulated payoffs, discounted back to the present value using the risk-free interest rate.

## Results

Upon running the script, it will:
*   Print the estimated Asian option price to the console.
*   Generate and save two plots in the `results/` directory:
    *   `sample_paths.png`: A visualization of a few simulated GBM price paths.
    *   `payoff_distribution.png`: A histogram showing the distribution of the calculated payoffs from the simulation.

The simulation provides a robust estimate for the option's price, and the visualizations offer insights into the behavior of the underlying asset and the potential option outcomes.

## Skills Showcased

*   **Stochastic Calculus:** Understanding and implementing the Geometric Brownian Motion model.
*   **Monte Carlo Methods:** Designing and building a robust simulation engine.
*   **Probability & Statistics:** Analyzing distributions and understanding the law of large numbers.
*   **Numerical Methods:** Applying computational techniques to solve a financial problem.
*   **Python Programming:** Proficient use of NumPy and Matplotlib for scientific computing.
*   **Financial Derivatives:** Understanding and pricing of Asian options.
