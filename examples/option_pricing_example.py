from tfq_finance.pricing.equity.option_pricing import price_option

def option_pricing_example():
    spot_price = 100
    strike_price = 105
    time_to_maturity = 1
    volatility = 0.2
    risk_free_rate = 0.05

    option_price = price_option(spot_price, strike_price, time_to_maturity, volatility, risk_free_rate)
    print("Option Price:")
    print(option_price)

if __name__ == "__main__":
    option_pricing_example()