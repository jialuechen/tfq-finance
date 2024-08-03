import tensorflow as tf
import tensorflow_quantum as tfq
import cirq
import sympy
import numpy as np

def preprocess_data(data, method='standard'):
    if method == 'standard':
        scaler = StandardScaler()
    elif method == 'minmax':
        scaler = MinMaxScaler()
    else:
        raise ValueError("Invalid method. Choose 'standard' or 'minmax'.")

    scaled_data = scaler.fit_transform(data)
    return pd.DataFrame(scaled_data, columns=data.columns)

def split_data(data, test_size=0.2):
    train_size = int((1 - test_size) * len(data))
    train_data = data[:train_size]
    test_data = data[train_size:]
    return train_data, test_data

if __name__ == "__main__":
    data = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [5, 6, 7, 8, 9],
        'C': [10, 11, 12, 13, 14]
    })

    print("Original Data:")
    print(data)

    scaled_data = preprocess_data(data, method='standard')
    print("\nScaled Data:")
    print(scaled_data)

    train_data, test_data = split_data(scaled_data, test_size=0.2)
    print("\nTrain Data:")
    print(train_data)
    print("\nTest Data:")
    print(test_data)