import numpy as np

def stress_test_portfolio(portfolio_returns, stress_scenarios):
    stressed_returns = {}
    for scenario, shock in stress_scenarios.items():
        stressed_returns[scenario] = portfolio_returns + shock
    return stressed_returns

if __name__ == "__main__":
    portfolio_returns = np.random.randn(100) * 0.01
    stress_scenarios = {
        'Market Crash': -0.05,
        'Interest Rate Hike': -0.02,
        'Credit Event': -0.03
    }

    stressed_returns = stress_test_portfolio(portfolio_returns, stress_scenarios)
    for scenario, returns in stressed_returns.items():
        print(f"Scenario: {scenario}, Stressed Returns: {returns[:5]}")