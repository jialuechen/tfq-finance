from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def evaluate_regression_model(y_true, y_pred):
    mse = mean_squared_error(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)

    evaluation_metrics = {
        'Mean Squared Error': mse,
        'Mean Absolute Error': mae,
        'R-squared': r2
    }
    
    return evaluation_metrics

if __name__ == "__main__":
    y_true = [3, -0, 2, 7]
    y_pred = [2.5, 0.0, 2, 8]

    metrics = evaluate_regression_model(y_true, y_pred)
    print("Regression Model Evaluation Metrics:")
    for metric, value in metrics.items():
        print(f"{metric}: {value}")