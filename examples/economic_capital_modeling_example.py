from tfq_finance.risk_management.economic_capital_modeling import calculate_economic_capital

def economic_capital_modeling_example():
    exposure = 5000000
    probability_of_default = 0.01
    loss_given_default = 0.5
    confidence_level = 0.99

    economic_capital = calculate_economic_capital(exposure, probability_of_default, loss_given_default, confidence_level)
    print("Economic Capital:", economic_capital)

if __name__ == "__main__":
    economic_capital_modeling_example()