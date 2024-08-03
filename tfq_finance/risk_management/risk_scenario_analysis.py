import numpy as np

def perform_risk_scenario_analysis(portfolio_returns, scenarios):
    scenario_results = {}
    for scenario, adjustment in scenarios.items():
        scenario_results[scenario] = portfolio_returns + adjustment
    return scenario_results

if __name__ == "__main__":
    portfolio_returns = np.random.randn(100) * 0.01
    scenarios = {
        'Scenario A': -0.01,
        'Scenario B': 0.02,
        'Scenario C': -0.005
    }

    scenario_results = perform_risk_scenario_analysis(portfolio_returns, scenarios)
    for scenario, result in scenario_results.items():
        print(f"Scenario: {scenario}, Adjusted Returns: {result[:5]}")