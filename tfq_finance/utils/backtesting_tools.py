import pandas as pd

def backtest_strategy(prices, signals):
    returns = prices.pct_change().shift(-1)
    strategy_returns = signals.shift(1) * returns
    cumulative_returns = (1 + strategy_returns).cumprod()
    return cumulative_returns

if __name__ == "__main__":
    prices = pd.Series([100, 102, 101, 105, 107])
    signals = pd.Series([1, -1, 1, 1, -1])

    cumulative_returns = backtest_strategy(prices, signals)
    print("Cumulative Returns:")
    print(cumulative_returns)