import numpy as np

def market_making_strategy(prices, spread):
    mid_price = (prices[:-1] + prices[1:]) / 2
    buy_prices = mid_price - spread / 2
    sell_prices = mid_price + spread / 2
    return buy_prices, sell_prices

if __name__ == "__main__":
    prices = np.array([100, 101, 102, 101, 100])
    spread = 0.1

    buy_prices, sell_prices = market_making_strategy(prices, spread)
    print("Market Making Buy Prices:")
    print(buy_prices)
    print("Market Making Sell Prices:")
    print(sell_prices)