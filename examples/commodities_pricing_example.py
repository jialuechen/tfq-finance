from tfq_finance.pricing.commodities.commodities_pricing import price_commodity

def commodities_pricing_example():
    spot_price = 70
    strike_price = 75
    time_to_maturity = 1
    volatility = 0.3
    risk_free_rate = 0.05

    commodity_price = price_commodity(spot_price, strike_price, time_to_maturity, volatility, risk_free_rate)
    print("Commodity Price:", commodity_price)

if __name__ == "__main__":
    commodities_pricing_example()