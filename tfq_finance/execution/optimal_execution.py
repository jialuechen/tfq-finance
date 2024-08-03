import numpy as np
import pandas as pd

def calculate_optimal_execution(trades, liquidity, risk_aversion):
    optimal_execution = trades / (1 + risk_aversion * trades / liquidity)
    return optimal_execution

if __name__ == "__main__":
    trades = np.array([100, 200, 150, 300])
    liquidity = 1000
    risk_aversion = 0.1

    optimal_execution = calculate_optimal_execution(trades, liquidity, risk_aversion)
    print("Optimal Execution Quantities:")
    print(optimal_execution)