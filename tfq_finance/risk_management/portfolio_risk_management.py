import numpy as np

def calculate_portfolio_risk(returns, weights):
    covariance_matrix = np.cov(returns.T)
    portfolio_variance = np.dot(weights.T, np.dot(covariance_matrix, weights))
    portfolio_risk = np.sqrt(portfolio_variance)
    return portfolio_risk

if __name__ == "__main__":
    returns = np.random.randn(100, 4)
    weights = np.array([0.25, 0.25, 0.25, 0.25])

    portfolio_risk = calculate_portfolio_risk(returns, weights)
    print(f"Portfolio Risk: {portfolio_risk}")