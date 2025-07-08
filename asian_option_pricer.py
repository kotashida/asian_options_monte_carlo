import numpy as np
import matplotlib.pyplot as plt
import os

# --- Model Parameters ---
# Stock details
S0 = 100      # Starting stock price
mu = 0.05     # Expected return (drift)
sigma = 0.2   # Volatility

# Option details
T = 1.0       # Time to maturity (in years)
K = 100       # Strike price

# Simulation settings
N_PATHS = 10000  # How many price paths to simulate
N_STEPS = 252    # Number of time steps (e.g., trading days in a year)
dt = T / N_STEPS # Size of each time step


def simulate_gbm_path(S0, mu, sigma, T, dt):
    """Simulates a single stock price path using Geometric Brownian Motion."""
    n_steps = int(T / dt)
    path = np.zeros(n_steps + 1)
    path[0] = S0
    for i in range(1, n_steps + 1):
        # This is the core GBM equation
        z = np.random.standard_normal()
        path[i] = path[i-1] * np.exp((mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z)
    return path


if __name__ == "__main__":
    print("Starting Monte Carlo simulation for Asian option pricing...")

    # --- Run the Simulation ---
    # We'll store the final payoff for each path here
    payoffs = []
    for _ in range(N_PATHS):
        path = simulate_gbm_path(S0, mu, sigma, T, dt)
        # For an Asian option, the payoff is based on the average price
        average_price = np.mean(path)
        # Calculate the payoff (it can't be negative)
        payoff = max(0, average_price - K)
        payoffs.append(payoff)

    # --- Calculate the Option Price ---
    # The option's value is the average of all simulated payoffs...
    average_payoff = np.mean(payoffs)
    # ...discounted back to its present value.
    option_price = average_payoff * np.exp(-mu * T)

    print(f"\nEstimated Asian Option Price: {option_price:.4f}")

    # --- Visualize the Results ---
    # Make a 'results' folder to save our plots
    if not os.path.exists("results"):
        os.makedirs("results")

    # Plot a handful of simulated price paths to see what they look like
    plt.figure(figsize=(10, 6))
    for i in range(5):
        path = simulate_gbm_path(S0, mu, sigma, T, dt)
        plt.plot(path)
    plt.title("Sample GBM Price Paths")
    plt.xlabel("Time Steps")
    plt.ylabel("Stock Price")
    plt.grid(True)
    plt.savefig("results/sample_paths.png")
    print("\nSaved sample paths plot to results/sample_paths.png")

    # Plot the distribution of all final payoffs
    plt.figure(figsize=(10, 6))
    plt.hist(payoffs, bins=50, edgecolor='black')
    plt.title("Distribution of Option Payoffs")
    plt.xlabel("Payoff")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.savefig("results/payoff_distribution.png")
    print("Saved payoff distribution plot to results/payoff_distribution.png")