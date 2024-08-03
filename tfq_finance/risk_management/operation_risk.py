import numpy as np

def calculate_operational_risk(losses, confidence_level=0.95):
    var = np.percentile(losses, (1 - confidence_level) * 100)
    return var

if __name__ == "__main__":
    losses = np.random.randn(100) * 10000

    operational_risk = calculate_operational_risk(losses)
    print(f"Operational Risk (VaR): {operational_risk}")