import numpy as np

def calculate_value_at_risk(returns, confidence_level=0.95):
    var = np.percentile(returns, (1 - confidence_level) * 100)
    return var

def calculate_conditional_value_at_risk(returns, confidence_level=0.95):
    var = calculate_value_at_risk(returns, confidence_level)
    cvar = returns[returns <= var].mean()
    return cvar

if __name__ == "__main__":
    returns = np.random.randn(100) * 0.01

    var = calculate_value_at_risk(returns)
    cvar = calculate_conditional_value_at_risk(returns)

    print(f"Value at Risk: {var}")
    print(f"Conditional Value at Risk: {cvar}")