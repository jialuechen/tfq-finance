import numpy as np
import pandas as pd

def calculate_annualized_return(daily_returns):
    cumulative_return = np.prod(1 + daily_returns) - 1
    num_days = len(daily_returns)
    annualized_return = (1 + cumulative_return) ** (252 / num_days) - 1
    return annualized_return

def calculate_annualized_volatility(daily_returns):
    daily_volatility = np.std(daily_returns)
    annualized_volatility = daily_volatility * np.sqrt(252)
    return annualized_volatility

def calculate_sharpe_ratio(daily_returns, risk_free_rate=0.01):
    annualized_return = calculate_annualized_return(daily_returns)
    annualized_volatility = calculate_annualized_volatility(daily_returns)
    sharpe_ratio = (annualized_return - risk_free_rate) / annualized_volatility
    return sharpe_ratio

if __name__ == "__main__":
    daily_returns = np.random.normal(0, 0.01, 252)

    annualized_return = calculate_annualized_return(daily_returns)
    annualized_volatility = calculate_annualized_volatility(daily_returns)
    sharpe_ratio = calculate_sharpe_ratio(daily_returns)

    print(f"Annualized Return: {annualized_return}")
    print(f"Annualized Volatility: {annualized_volatility}")
    print(f"Sharpe Ratio: {sharpe_ratio}")