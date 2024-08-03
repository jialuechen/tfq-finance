import numpy as np
from scipy.stats import norm

def calculate_prob_of_default(credit_spread, recovery_rate, time_horizon):
    prob_of_default = 1 - np.exp(-credit_spread * time_horizon / (1 - recovery_rate))
    return prob_of_default

def calculate_credit_value_at_risk(exposure, prob_of_default, confidence_level=0.95):
    var = exposure * (1 - prob_of_default) + norm.ppf(confidence_level) * np.sqrt(exposure * prob_of_default * (1 - prob_of_default))
    return var

if __name__ == "__main__":
    credit_spread = 0.02
    recovery_rate = 0.4
    time_horizon = 1
    exposure = 1000000

    prob_of_default = calculate_prob_of_default(credit_spread, recovery_rate, time_horizon)
    cvar = calculate_credit_value_at_risk(exposure, prob_of_default)

    print(f"Probability of Default: {prob_of_default}")
    print(f"Credit Value at Risk: {cvar}")