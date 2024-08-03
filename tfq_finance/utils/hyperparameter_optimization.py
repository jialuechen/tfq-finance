from sklearn.model_selection import GridSearchCV

def optimize_hyperparameters(model, param_grid, X, y):
    grid_search = GridSearchCV(model, param_grid, cv=5)
    grid_search.fit(X, y)
    return grid_search.best_params_, grid_search.best_score_

if __name__ == "__main__":
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.datasets import load_iris

    X, y = load_iris(return_X_y=True)
    model = RandomForestClassifier()

    param_grid = {
        'n_estimators': [10, 50, 100],
        'max_depth': [None, 10, 20, 30]
    }

    best_params, best_score = optimize_hyperparameters(model, param_grid, X, y)
    print("Best Parameters:", best_params)
    print("Best Score:", best_score)