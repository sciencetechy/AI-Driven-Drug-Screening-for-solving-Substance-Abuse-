import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

Y = pd.read_csv('MOR.csv')
X = np.load('MOR.npy')

X_train = X[:int(0.9*len(X))]
X_test = X[int(0.9*len(X)):]
y_train = Y[:int(0.9*len(Y))]
y_test = Y[int(0.9*len(Y)):]

y_train = y_train.values.ravel()
y_test = y_test.values.ravel()

# Hyperparameter lists
n_estimators = [50, 100, 200]
max_depth = [None, 10, 20, 30]
min_samples_split = [2, 5, 10]
max_features = ['sqrt', 'log2', None, 0.8, 0.9]

# Variables to store the best model and its score
best_score = float('inf')
best_params = None

# Loop through each combination of hyperparameters
for n in n_estimators:
    for depth in max_depth:
        for min_split in min_samples_split:
            for feature in max_features:

                # Initialize the RandomForestRegressor with current parameters
                model = RandomForestRegressor(
                    n_estimators=n,
                    max_depth=depth,
                    min_samples_split=min_split,
                    max_features=feature,
                    bootstrap=True,
                    random_state=42
                )

                # Train the model
                model.fit(X_train, y_train)

                # Evaluate the model on the test set
                y_pred = model.predict(X_test)

                # Calculate evaluation metrics
                mse = mean_squared_error(y_test, y_pred)
                mae = mean_absolute_error(y_test, y_pred)
                r2 = r2_score(y_test, y_pred)

                # Print the scores and current hyperparameters
                print(f"n_estimators: {n}, max_depth: {depth}, min_samples_split: {min_split}, max_features: {feature}")
                print(f"MSE: {mse:.4f}, MAE: {mae:.4f}, R²: {r2:.4f}")

                # If the current model has the best score, update the best parameters and score
                if mse < best_score:
                    best_score = mse
                    best_params = {
                        'n_estimators': n,
                        'max_depth': depth,
                        'min_samples_split': min_split,
                        'max_features': feature
                    }

# Print the best parameters and their corresponding evaluation metrics
print("\nBest Hyperparameters:")
print(best_params)
print(f"Best MSE: {best_score:.4f}")