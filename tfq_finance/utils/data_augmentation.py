import numpy as np

def augment_data(data, augmentation_factor=0.1):
    augmented_data = data + augmentation_factor * np.random.randn(*data.shape)
    return augmented_data

if __name__ == "__main__":
    data = np.random.randn(100, 3)
    print("Original Data:")
    print(data[:5])

    augmented_data = augment_data(data)
    print("Augmented Data:")
    print(augmented_data[:5])