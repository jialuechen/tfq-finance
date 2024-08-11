from tfq_finance.pricing.equity.variance_swap_pricing import price_variance_swap

def variance_swap_pricing_example():
    spot_price = 100
    strike_price = 105
    time_to_maturity = 1
    volatility = 0.2
    risk_free_rate = 0.05

    variance_swap_price = price_variance_swap(spot_price, strike_price, time_to_maturity, volatility, risk_free_rate)
    print("Variance Swap Price:", variance_swap_price)

if __name__ == "__main__":
    variance_swap_pricing_example()