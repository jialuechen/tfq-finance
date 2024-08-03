import numpy as np
import pandas as pd

def historical_cvar(returns, confidence_level=0.95):
    if isinstance(returns, pd.Series):
        returns = returns.values
    var = np.percentile(returns, (1 - confidence_level) * 100)
    cvar = returns[returns <= var].mean()
    return cvar

def parametric_cvar(returns, confidence_level=0.95):
    mean = np.mean(returns)
    std_dev = np.std(returns)
    var = mean - std_dev * np.percentile(np.random.randn(10000), (1 - confidence_level) * 100)
    cvar = mean - std_dev * np.mean(np.random.randn(10000)[np.random.randn(10000) <= var])
    return cvar

def monte_carlo_cvar(initial_price, mu, sigma, num_simulations=10000, confidence_level=0.95):
    simulated_prices = initial_price * np.exp((mu - 0.5 * sigma ** 2) + sigma * np.random.randn(num_simulations))
    simulated_returns = np.log(simulated_prices / initial_price)
    var = np.percentile(simulated_returns, (1 - confidence_level) * 100)
    cvar = simulated_returns[simulated_returns <= var].mean()
    return cvar

if __name__ == "__main__":
    returns = np.random.randn(100) * 0.01

    hist_cvar = historical_cvar(returns)
    param_cvar = parametric_cvar(returns)
    mc_cvar = monte_carlo_cvar(100, 0.01, 0.02)

    print(f"Historical CVaR: {hist_cvar}")
    print(f"Parametric CVaR: {param_cvar}")
    print(f"Monte Carlo CVaR: {mc_cvar}")