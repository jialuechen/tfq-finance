import numpy as np

def pairs_trading_strategy(asset1_prices, asset2_prices, window=5):
    spread = asset1_prices - asset2_prices
    moving_avg = np.mean(spread[-window:])
    moving_std = np.std(spread[-window:])
    z_score = (spread[-1] - moving_avg) / moving_std
    return z_score

if __name__ == "__main__":
    asset1_prices = np.array([100, 101, 102, 101, 100, 99, 100])
    asset2_prices = np.array([99, 100, 101, 100, 99, 98, 99])
    signal = pairs_trading_strategy(asset1_prices, asset2_prices)
    print("Pairs Trading Z-Score:")
    print(signal)