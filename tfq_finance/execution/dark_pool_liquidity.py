import numpy as np

def estimate_dark_pool_liquidity(trades, market_liquidity):
    dark_pool_liquidity = trades * 0.2  # Assuming 20% of trades are executed in dark pools
    return dark_pool_liquidity

if __name__ == "__main__":
    trades = np.array([100, 200, 150, 300])
    market_liquidity = 1000

    dark_pool_liquidity = estimate_dark_pool_liquidity(trades, market_liquidity)
    print("Estimated Dark Pool Liquidity:")
    print(dark_pool_liquidity)