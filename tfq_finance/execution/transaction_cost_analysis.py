import numpy as np
import pandas as pd

def calculate_transaction_costs(trades, bid_ask_spread):
    costs = trades * bid_ask_spread
    return costs.sum()

def calculate_implementation_shortfall(trades, market_prices, execution_prices):
    market_value = trades * market_prices
    executed_value = trades * execution_prices
    shortfall = executed_value - market_value
    return shortfall.sum()

if __name__ == "__main__":
    trades = np.array([100, 200, 150, 300])
    bid_ask_spread = 0.01
    market_prices = np.array([10.0, 10.1, 10.2, 10.3])
    execution_prices = np.array([10.05, 10.15, 10.25, 10.35])

    transaction_costs = calculate_transaction_costs(trades, bid_ask_spread)
    implementation_shortfall = calculate_implementation_shortfall(trades, market_prices, execution_prices)

    print(f"Transaction Costs: {transaction_costs}")
    print(f"Implementation Shortfall: {implementation_shortfall}")