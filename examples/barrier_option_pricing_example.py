from tfq_finance.pricing.exotic.exotic_option_pricing import price_barrier_option

def barrier_option_pricing_example():
    spot_price = 100
    strike_price = 105
    barrier_level = 110
    time_to_maturity = 1
    volatility = 0.2
    risk_free_rate = 0.05

    barrier_option_price = price_barrier_option(spot_price, strike_price, barrier_level, time_to_maturity, volatility, risk_free_rate)
    print("Barrier Option Price:", barrier_option_price)

if __name__ == "__main__":
    barrier_option_pricing_example()