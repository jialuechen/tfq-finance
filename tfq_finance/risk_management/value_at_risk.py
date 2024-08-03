import numpy as np

def historical_var(returns, confidence_level=0.95):
    var = np.percentile(returns, (1 - confidence_level) * 100)
    return var

def parametric_var(returns, confidence_level=0.95):
    mean = np.mean(returns)
    std_dev = np.std(returns)
    var = mean - std_dev * np.percentile(np.random.randn(10000), (1 - confidence_level) * 100)
    return var

def monte_carlo_var(initial_price, mu, sigma, num_simulations=10000, confidence_level=0.95):
    simulated_prices = initial_price * np.exp((mu - 0.5 * sigma ** 2) + sigma * np.random.randn(num_simulations))
    simulated_returns = np.log(simulated_prices / initial_price)
    var = np.percentile(simulated_returns, (1 - confidence_level) * 100)
    return var

if __name__ == "__main__":
    returns = np.random.randn(100) * 0.01

    hist_var = historical_var(returns)
    param_var = parametric_var(returns)
    mc_var = monte_carlo_var(100, 0.01, 0.02)

    print(f"Historical VaR: {hist_var}")
    print(f"Parametric VaR: {param_var}")
    print(f"Monte Carlo VaR: {mc_var}")