import numpy as np
from scipy.optimize import minimize

def calibrate_model(model, data, initial_params):
    def objective_function(params):
        model.set_params(params)
        residuals = model.compute_residuals(data)
        return np.sum(residuals ** 2)

    result = minimize(objective_function, initial_params, method='L-BFGS-B')
    model.set_params(result.x)
    return result.x

if __name__ == "__main__":
    class ExampleModel:
        def __init__(self):
            self.params = None

        def set_params(self, params):
            self.params = params

        def compute_residuals(self, data):
            return data - self.params

    model = ExampleModel()
    data = np.array([1, 2, 3, 4, 5])
    initial_params = np.array([0.5, 0.5, 0.5, 0.5, 0.5])

    calibrated_params = calibrate_model(model, data, initial_params)
    print("Calibrated Parameters:")
    print(calibrated_params)