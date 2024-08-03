import numpy as np

def sentiment_based_trading_strategy(sentiment_data, threshold=0):
    signal = np.where(sentiment_data > threshold, 1, -1)
    return signal

if __name__ == "__main__":
    sentiment_data = np.array([0.1, -0.2, 0.3, -0.1, 0.2])
    signal = sentiment_based_trading_strategy(sentiment_data)
    print("Sentiment Based Trading Signal:")
    print(signal)