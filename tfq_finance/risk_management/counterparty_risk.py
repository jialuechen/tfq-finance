import numpy as np
from scipy.stats import norm

def calculate_counterparty_risk(exposure, probability_of_default, loss_given_default, confidence_level=0.95):
    unexpected_loss = norm.ppf(confidence_level) * np.sqrt(exposure * probability_of_default * (1 - probability_of_default))
    expected_loss = exposure * probability_of_default * loss_given_default
    total_risk = unexpected_loss + expected_loss
    return total_risk

if __name__ == "__main__":
    exposure = 1000000
    probability_of_default = 0.02
    loss_given_default = 0.6

    counterparty_risk = calculate_counterparty_risk(exposure, probability_of_default, loss_given_default)
    print(f"Counterparty Risk: {counterparty_risk}")