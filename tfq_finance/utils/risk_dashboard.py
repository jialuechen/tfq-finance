import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_risk_dashboard(risk_metrics):
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))

    sns.barplot(x=list(risk_metrics.keys()), y=list(risk_metrics.values()), ax=axes[0, 0])
    axes[0, 0].set_title('Risk Metrics Bar Plot')

    sns.lineplot(x=list(risk_metrics.keys()), y=list(risk_metrics.values()), ax=axes[0, 1])
    axes[0, 1].set_title('Risk Metrics Line Plot')

    sns.heatmap(pd.DataFrame(list(risk_metrics.values())).T, annot=True, ax=axes[1, 0], cmap='coolwarm')
    axes[1, 0].set_title('Risk Metrics Heatmap')

    sns.boxplot(data=list(risk_metrics.values()), ax=axes[1, 1])
    axes[1, 1].set_title('Risk Metrics Box Plot')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    risk_metrics = {
        'VaR': 0.05,
        'CVaR': 0.07,
        'Max Drawdown': 0.2,
        'Sharpe Ratio': 1.5
    }

    plot_risk_dashboard(risk_metrics)