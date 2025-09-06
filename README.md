# Pricing Asian Options with Monte Carlo Simulation

## Project Overview

This project implements a Monte Carlo simulation in Python to price an Asian option, a type of exotic financial derivative. The payoff of an Asian option is dependent on the average price of the underlying asset over a specified period, making it a "path-dependent" option. This characteristic means that standard closed-form solutions like the Black-Scholes model are not applicable, necessitating the use of numerical methods like Monte Carlo simulation.

The simulation is built from the ground up, showcasing a strong foundation in stochastic calculus, numerical methods, and computational finance. It demonstrates the ability to model and solve complex financial problems without reliance on specialized, off-the-shelf software.

## Methodology

The core of this project is a Monte Carlo simulation designed to estimate the fair value of an Asian call option. The methodology is broken down into the following steps:

1.  **Stochastic Process Modeling:** The price of the underlying asset is modeled using the **Geometric Brownian Motion (GBM)** stochastic process. GBM is a widely accepted model for stock price dynamics, as it assumes that returns are normally distributed and prevents the stock price from becoming negative. The GBM is defined by the stochastic differential equation:

    *dS<sub>t</sub> = μS<sub>t</sub>dt + σS<sub>t</sub>dW<sub>t</sub>*

    where:
    *   *S<sub>t</sub>* is the stock price at time *t*
    *   *μ* is the drift (expected return)
    *   *σ* is the volatility
    *   *dW<sub>t</sub>* is a Wiener process or Brownian motion

2.  **Path Simulation:** The simulation generates a large number of potential future price paths for the underlying asset. In this project, **10,000 distinct paths** are simulated, each with **252 time steps** (representing daily price movements over a year). Each path provides a possible scenario for the asset's price evolution.

3.  **Payoff Calculation:** For each simulated path, the arithmetic average of the stock price is calculated. The payoff of the Asian call option is then determined using the formula:

    *Payoff = max(0, AveragePrice - K)*

    where *K* is the strike price.

4.  **Discounting and Estimation:** The payoffs from all 10,000 paths are averaged to find the expected payoff. This expected payoff is then discounted to its present value using the risk-free rate, yielding the estimated price of the Asian option. This approach is rooted in the **Law of Large Numbers**, which ensures that as the number of simulations increases, the estimated price converges to the true expected value.

## Quantified Results

The simulation was executed with the following parameters:
*   **Initial Stock Price (S0):** $100
*   **Strike Price (K):** $100
*   **Time to Maturity (T):** 1 year
*   **Drift (μ):** 5%
*   **Volatility (σ):** 20%
*   **Number of Simulations:** 10,000 paths
*   **Time Steps:** 252 (daily)

Based on these parameters, the Monte Carlo simulation yielded an **estimated Asian option price of $4.75**.

The simulation also generates two key visualizations:

*   **Sample Price Paths:** A plot of five sample GBM paths, illustrating the stochastic nature of the asset's price movements.
*   **Payoff Distribution:** A histogram of the 10,000 simulated payoffs, which shows that a significant number of paths result in a zero payoff, with a right-skewed distribution of positive payoffs.

## Key Quantitative Skills Demonstrated

*   **Stochastic Calculus:**
    *   Modeling asset price dynamics using the Geometric Brownian Motion (GBM) stochastic process.
    *   Discretizing and implementing the GBM formula for simulation.

*   **Monte Carlo Methods:**
    *   Designing and implementing a Monte Carlo simulation to solve a problem without a closed-form solution.
    *   Understanding the convergence properties of Monte Carlo estimators.

*   **Probability & Statistics:**
    *   Applying the Law of Large Numbers to ensure the convergence of the simulation.
    *   Generating random variables from a standard normal distribution to drive the simulation.
    *   Analyzing the distribution of simulated payoffs.

*   **Numerical Methods:**
    *   Applying computational techniques to price complex financial derivatives.
    *   Using numerical integration (via averaging) to estimate the expected payoff.

*   **Financial Engineering:**
    *   Deep understanding of exotic options, specifically path-dependent Asian options.
    *   Knowledge of option pricing theory and risk-neutral valuation.

*   **Python for Scientific Computing:**
    *   Proficient use of **NumPy** for high-performance numerical computations.
    *   Data visualization with **Matplotlib** to interpret simulation results.

## How to Run the Project

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/kotashida/asian_options_monte_carlo
    cd asian_options_monte_carlo
    ```

2.  **Set up a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute the simulation:**
    ```bash
    python asian_option_pricer.py
    ```