import numpy as np
import pandas as pd

def risk_adjusted_execution(trades, liquidity, risk_aversion, volatility):
    optimal_execution = trades / (1 + risk_aversion * volatility * trades / liquidity)
    return optimal_execution

if __name__ == "__main__":
    trades = np.array([100, 200, 150, 300])
    liquidity = 1000
    risk_aversion = 0.1
    volatility = 0.02

    optimal_execution = risk_adjusted_execution(trades, liquidity, risk_aversion, volatility)
    print("Risk-Adjusted Optimal Execution Quantities:")
    print(optimal_execution)