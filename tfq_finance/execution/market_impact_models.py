import numpy as np
import pandas as pd

def calculate_linear_impact(trades, liquidity):
    impact = trades / liquidity
    return impact.sum()

def calculate_square_root_impact(trades, liquidity):
    impact = np.sqrt(trades / liquidity)
    return impact.sum()

if __name__ == "__main__":
    trades = np.array([100, 200, 150, 300])
    liquidity = 1000

    linear_impact = calculate_linear_impact(trades, liquidity)
    sqrt_impact = calculate_square_root_impact(trades, liquidity)

    print(f"Linear Market Impact: {linear_impact}")
    print(f"Square Root Market Impact: {sqrt_impact}")