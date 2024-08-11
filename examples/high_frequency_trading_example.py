import numpy as np
from tfq_finance.execution.high_frequency_trading import high_frequency_trading_signal

def high_frequency_trading_example():
    prices = np.array([100, 101, 102, 101, 100, 99, 100])

    signal = high_frequency_trading_signal(prices)
    print("High Frequency Trading Signal:", signal)

if __name__ == "__main__":
    high_frequency_trading_example()