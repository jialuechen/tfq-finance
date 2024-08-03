import numpy as np

def detect_arbitrage_opportunity(prices, latency):
    price_diff = np.diff(prices)
    arbitrage_opportunity = price_diff > latency
    return arbitrage_opportunity

if __name__ == "__main__":
    prices = np.array([100, 100.1, 100.15, 100.2, 100.3])
    latency = 0.05

    arbitrage_opportunity = detect_arbitrage_opportunity(prices, latency)
    print("Arbitrage Opportunity Detected:")
    print(arbitrage_opportunity)