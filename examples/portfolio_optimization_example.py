import numpy as np
from tfq_finance.optimization.portfolio_optimization import optimize_portfolio

def portfolio_optimization_example():
    returns = np.random.randn(100, 4)
    risk_aversion = 0.5

    optimal_weights = optimize_portfolio(returns, risk_aversion)
    print("Optimal Portfolio Weights:", optimal_weights)

if __name__ == "__main__":
    portfolio_optimization_example()