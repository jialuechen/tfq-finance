import numpy as np
from tfq_finance.optimization.trading_strategy_optimization import optimize_trading_strategy

def trading_strategy_optimization_example():
    historical_prices = np.random.randn(100)
    strategy_parameters = {'param1': 1.0, 'param2': 2.0}

    optimized_strategy = optimize_trading_strategy(historical_prices, strategy_parameters)
    print("Optimized Trading Strategy:", optimized_strategy)

if __name__ == "__main__":
    trading_strategy_optimization_example()