import numpy as np
from tfq_finance.ml.quantum_regression import train_quantum_regression_model

train_data = np.random.randn(100, 4)
train_labels = np.random.randn(100)

model = train_quantum_regression_model(train_data, train_labels)
print("Quantum Regression Model Trained")