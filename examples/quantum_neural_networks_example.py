import numpy as np
from tfq_finance.ml.quantum_neural_networks import train_quantum_neural_network

def quantum_neural_networks_example():
    train_data = np.random.randn(100, 4)
    train_labels = np.random.randint(0, 2, size=100)

    model = train_quantum_neural_network(train_data, train_labels)
    print("Quantum Neural Network Trained")

if __name__ == "__main__":
    quantum_neural_networks_example()