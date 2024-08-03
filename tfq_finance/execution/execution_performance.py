import numpy as np

def evaluate_execution_performance(trades, market_prices, execution_prices):
    market_value = trades * market_prices
    executed_value = trades * execution_prices
    performance = executed_value / market_value - 1
    return performance

if __name__ == "__main__":
    trades = np.array([100, 200, 150, 300])
    market_prices = np.array([10.0, 10.1, 10.2, 10.3])
    execution_prices = np.array([10.05, 10.15, 10.25, 10.35])

    performance = evaluate_execution_performance(trades, market_prices, execution_prices)
    print("Execution Performance:")
    print(performance)