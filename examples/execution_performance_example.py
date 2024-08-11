from tfq_finance.execution.execution_performance import evaluate_execution_performance

def execution_performance_example():
    execution_data = {
        'executed_prices': [100.5, 101.0, 100.8, 100.7],
        'market_prices': [100.6, 101.2, 100.9, 100.6]
    }

    performance_metrics = evaluate_execution_performance(execution_data)
    print("Execution Performance Metrics:", performance_metrics)

if __name__ == "__main__":
    execution_performance_example()