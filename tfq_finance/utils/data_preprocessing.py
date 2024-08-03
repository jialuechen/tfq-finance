import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def preprocess_data(data, method='standard'):
    if method == 'standard':
        scaler = StandardScaler()
    elif method == 'minmax':
        scaler = MinMaxScaler()
    else:
        raise ValueError("Invalid method. Choose 'standard' or 'minmax'.")

    scaled_data = scaler.fit_transform(data)
    return pd.DataFrame(scaled_data, columns=data.columns)

def fill_missing_values(data, method='mean'):
    if method == 'mean':
        filled_data = data.fillna(data.mean())
    elif method == 'median':
        filled_data = data.fillna(data.median())
    elif method == 'mode':
        filled_data = data.fillna(data.mode().iloc[0])
    else:
        raise ValueError("Invalid method. Choose 'mean', 'median', or 'mode'.")

    return filled_data

if __name__ == "__main__":
    data = pd.DataFrame({
        'A': [1, 2, None, 4, 5],
        'B': [5, 6, 7, None, 9],
        'C': [10, 11, 12, 13, None]
    })

    print("Original Data:")
    print(data)

    filled_data = fill_missing_values(data, method='mean')
    print("\nFilled Missing Values (Mean):")
    print(filled_data)

    preprocessed_data = preprocess_data(filled_data, method='standard')
    print("\nPreprocessed Data (Standard Scaling):")
    print(preprocessed_data)