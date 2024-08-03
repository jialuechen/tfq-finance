import numpy as np
import pandas as pd

def calculate_max_drawdown(returns):
    cumulative_returns = np.cumprod(1 + returns) - 1
    peak = np.maximum.accumulate(cumulative_returns)
    drawdown = (cumulative_returns - peak) / peak
    max_drawdown = np.min(drawdown)
    return max_drawdown

def calculate_sortino_ratio(returns, target_return=0):
    mean_return = np.mean(returns)
    downside_risk = np.std(returns[returns < target_return])
    sortino_ratio = (mean_return - target_return) / downside_risk
    return sortino_ratio

def calculate_treynor_ratio(returns, risk_free_rate, beta):
    excess_returns = returns - risk_free_rate
    treynor_ratio = np.mean(excess_returns) / beta
    return treynor_ratio

if __name__ == "__main__":
    returns = np.random.randn(100) * 0.01
    risk_free_rate = 0.01
    beta = 1.2

    max_drawdown = calculate_max_drawdown(returns)
    sortino_ratio = calculate_sortino_ratio(returns)
    treynor_ratio = calculate_treynor_ratio(returns, risk_free_rate, beta)

    print(f"Max Drawdown: {max_drawdown}")
    print(f"Sortino Ratio: {sortino_ratio}")
    print(f"Treynor Ratio: {treynor_ratio}")