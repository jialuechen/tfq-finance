import numpy as np
import pandas as pd

def risk_parity_weights(cov_matrix):
    inv_volatility = 1 / np.sqrt(np.diag(cov_matrix))
    weights = inv_volatility / np.sum(inv_volatility)
    return weights

if __name__ == "__main__":
    returns = pd.DataFrame({
        'Asset1': np.random.randn(100),
        'Asset2': np.random.randn(100),
        'Asset3': np.random.randn(100)
    })

    cov_matrix = returns.cov()
    weights = risk_parity_weights(cov_matrix)

    print("Covariance Matrix:")
    print(cov_matrix)
    print("\nRisk Parity Weights:")
    print(weights)