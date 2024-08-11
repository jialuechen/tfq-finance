from tfq_finance.pricing.forex.foreign_exchange import price_forex_option

def foreign_exchange_example():
    spot_price = 1.2
    strike_price = 1.25
    time_to_maturity = 1
    volatility = 0.15
    risk_free_rate = 0.02

    forex_option_price = price_forex_option(spot_price, strike_price, time_to_maturity, volatility, risk_free_rate)
    print("Forex Option Price:", forex_option_price)

if __name__ == "__main__":
    foreign_exchange_example()