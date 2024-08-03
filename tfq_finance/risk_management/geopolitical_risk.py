import numpy as np

def calculate_geopolitical_risk(exposure, geopolitical_factor):
    risk_adjustment = exposure * geopolitical_factor
    adjusted_exposure = exposure + risk_adjustment
    return adjusted_exposure

if __name__ == "__main__":
    exposure = 1000000
    geopolitical_factor = 0.1

    adjusted_exposure = calculate_geopolitical_risk(exposure, geopolitical_factor)
    print(f"Adjusted Exposure: {adjusted_exposure}")