from tfq_finance.risk_management.credit_risk import calculate_credit_value_at_risk

def credit_risk_example():
    exposure = 1000000
    probability_of_default = 0.02
    confidence_level = 0.95

    cvar = calculate_credit_value_at_risk(exposure, probability_of_default, confidence_level)
    print("Credit Value at Risk:", cvar)

if __name__ == "__main__":
    credit_risk_example()