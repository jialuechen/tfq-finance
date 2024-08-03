import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_correlation_matrix(data, method='pearson'):
    correlation_matrix = data.corr(method=method)
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title(f'Correlation Matrix ({method.capitalize()} method)')
    plt.show()

def plot_time_series(data, columns=None):
    if columns is None:
        columns = data.columns
    plt.figure(figsize=(14, 7))
    for column in columns:
        plt.plot(data.index, data[column], label=column)
    plt.title('Time Series Plot')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.legend()
    plt.show()

def plot_distribution(data, columns=None):
    if columns is None:
        columns = data.columns
    plt.figure(figsize=(14, 7))
    for column in columns:
        sns.kdeplot(data[column], label=column, shade=True)
    plt.title('Distribution Plot')
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    data = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [5, 6, 7, 8, 9],
        'C': [10, 11, 12, 13, 14]
    }, index=pd.date_range(start='2021-01-01', periods=5, freq='D'))

    print("Data:")
    print(data)

    plot_correlation_matrix(data)
    plot_time_series(data)
    plot_distribution(data)