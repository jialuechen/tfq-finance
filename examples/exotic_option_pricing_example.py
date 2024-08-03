from tfq_finance.pricing.exotic.exotic_option_pricing import price_exotic_option

def exotic_option_pricing_example():
    spot_price = 100
    strike_price = 105
    time_to_maturity = 1
    volatility = 0.2
    risk_free_rate = 0.05

    exotic_option_price = price_exotic_option(spot_price, strike_price, time_to_maturity, volatility, risk_free_rate)
    print("Exotic Option Price:")
    print(exotic_option_price)

if __name__ == "__main__":
    exotic_option_pricing_example()