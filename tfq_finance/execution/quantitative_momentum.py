import numpy as np

def momentum_strategy(prices, window=5):
    momentum = prices[-window:] - prices[-window-1:-1]
    return np.sum(momentum)

if __name__ == "__main__":
    prices = np.array([100, 101, 102, 103, 104, 105, 106])
    signal = momentum_strategy(prices)
    print("Momentum Strategy Signal:")
    print(signal)