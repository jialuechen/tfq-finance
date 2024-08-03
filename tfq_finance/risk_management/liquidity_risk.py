import numpy as np

def calculate_liquidity_adjusted_var(returns, bid_ask_spread, holding_period, confidence_level=0.95):
    var = np.percentile(returns, (1 - confidence_level) * 100)
    liquidity_adjustment = bid_ask_spread * np.sqrt(holding_period)
    adjusted_var = var + liquidity_adjustment
    return adjusted_var

if __name__ == "__main__":
    returns = np.random.randn(100) * 0.01
    bid_ask_spread = 0.001
    holding_period = 5

    lav = calculate_liquidity_adjusted_var(returns, bid_ask_spread, holding_period)
    print(f"Liquidity Adjusted VaR: {lav}")