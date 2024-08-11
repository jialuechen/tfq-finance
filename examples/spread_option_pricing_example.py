from tfq_finance.pricing.commodities.spread_option_pricing import price_spread_option

def spread_option_pricing_example():
    spot_price1 = 50
    spot_price2 = 55
    strike_price = 5
    time_to_maturity = 1
    volatility1 = 0.2
    volatility2 = 0.25
    correlation = 0.5
    risk_free_rate = 0.05

    spread_option_price = price_spread_option(spot_price1, spot_price2, strike_price, time_to_maturity, volatility1, volatility2, correlation, risk_free_rate)
    print("Spread Option Price:", spread_option_price)

if __name__ == "__main__":
    spread_option_pricing_example()