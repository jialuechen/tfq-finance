import numpy as np
from scipy.stats import norm

def calculate_economic_capital(exposure, probability_of_default, loss_given_default, confidence_level=0.99):
    unexpected_loss = norm.ppf(confidence_level) * np.sqrt(exposure * probability_of_default * (1 - probability_of_default))
    expected_loss = exposure * probability_of_default * loss_given_default
    economic_capital = unexpected_loss + expected_loss
    return economic_capital

if __name__ == "__main__":
    exposure = 1000000
    probability_of_default = 0.02
    loss_given_default = 0.6

    economic_capital = calculate_economic_capital(exposure, probability_of_default, loss_given_default)
    print(f"Economic Capital: {economic_capital}")