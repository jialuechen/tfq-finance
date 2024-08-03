import numpy as np

def volatility_arbitrage_strategy(prices):
    returns = np.diff(prices) / prices[:-1]
    realized_volatility = np.std(returns)
    signal = realized_volatility - np.mean(realized_volatility)
    return signal

if __name__ == "__main__":
    prices = np.array([100, 101, 102, 101, 100, 99, 100])
    signal = volatility_arbitrage_strategy(prices)
    print("Volatility Arbitrage Signal:")
    print(signal)