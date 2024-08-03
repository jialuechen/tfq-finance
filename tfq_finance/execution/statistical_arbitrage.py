import numpy as np

def statistical_arbitrage_strategy(asset1_returns, asset2_returns):
    spread = asset1_returns - asset2_returns
    mean_spread = np.mean(spread)
    std_spread = np.std(spread)
    signal = (spread - mean_spread) / std_spread
    return signal

if __name__ == "__main__":
    asset1_returns = np.random.randn(100)
    asset2_returns = np.random.randn(100)

    signal = statistical_arbitrage_strategy(asset1_returns, asset2_returns)
    print("Statistical Arbitrage Signal:")
    print(signal)