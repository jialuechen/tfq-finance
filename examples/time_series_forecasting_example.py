import numpy as np
from tfq_finance.ml.time_series_forecasting import train_quantum_time_series_model

def time_series_forecasting_example():
    train_data = np.random.randn(100, 4)
    train_labels = np.random.randn(100)

    model = train_quantum_time_series_model(train_data, train_labels)
    print("Quantum Time Series Forecasting Model Trained")

if __name__ == "__main__":
    time_series_forecasting_example()