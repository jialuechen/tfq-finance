import numpy as np

def calculate_model_risk(model_errors):
    model_risk = np.sqrt(np.mean(model_errors ** 2))
    return model_risk

if __name__ == "__main__":
    model_errors = np.random.randn(100) * 0.01

    model_risk = calculate_model_risk(model_errors)
    print(f"Model Risk: {model_risk}")