import numpy as np

def calculate_climate_risk(asset_values, climate_sensitivity, climate_scenario):
    climate_impact = climate_sensitivity * climate_scenario
    adjusted_values = asset_values - climate_impact
    return adjusted_values

if __name__ == "__main__":
    asset_values = np.array([100000, 200000, 300000])
    climate_sensitivity = np.array([0.1, 0.2, 0.3])
    climate_scenario = 0.05

    adjusted_values = calculate_climate_risk(asset_values, climate_sensitivity, climate_scenario)
    print(f"Adjusted Asset Values: {adjusted_values}")