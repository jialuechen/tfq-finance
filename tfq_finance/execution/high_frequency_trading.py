import numpy as np

def high_frequency_trading_signal(prices):
    returns = np.diff(prices) / prices[:-1]
    signal = np.sign(returns)
    return signal

if __name__ == "__main__":
    prices = np.array([100, 101, 102, 101, 100, 99, 100])
    signal = high_frequency_trading_signal(prices)
    print("High Frequency Trading Signal:")
    print(signal)