import numpy as np

def news_based_trading_strategy(sentiment_scores, threshold=0.5):
    signal = np.where(sentiment_scores > threshold, 1, -1)
    return signal

if __name__ == "__main__":
    sentiment_scores = np.array([0.6, 0.4, 0.8, 0.3, 0.7])
    signal = news_based_trading_strategy(sentiment_scores)
    print("News Based Trading Signal:")
    print(signal)