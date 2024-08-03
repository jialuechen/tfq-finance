import numpy as np

def calculate_concentration_risk(exposures):
    total_exposure = np.sum(exposures)
    concentration_risk = np.sum((exposures / total_exposure) ** 2)
    return concentration_risk

if __name__ == "__main__":
    exposures = np.array([100000, 200000, 300000, 400000])
    
    concentration_risk = calculate_concentration_risk(exposures)
    print(f"Concentration Risk: {concentration_risk}")