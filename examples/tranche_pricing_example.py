from tfq_finance.pricing.credit.tranche_pricing import price_tranche

def tranche_pricing_example():
    tranche_notional = 1000000
    attachment_point = 0.03
    detachment_point = 0.07
    spread = 0.05
    maturity = 5

    tranche_price = price_tranche(tranche_notional, attachment_point, detachment_point, spread, maturity)
    print("Tranche Price:", tranche_price)

if __name__ == "__main__":
    tranche_pricing_example()