import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import sys

# Print all command line arguments
print("Arguments:", sys.argv)

# Access individual arguments (sys.argv[0] is the script name)
if len(sys.argv) > 1:
    first_arg = sys.argv[1]
    print("First argument:", first_arg)

else:
    quit()

file_csv = first_arg + ".csv"
file_npy = first_arg + ".npy"

Y = pd.read_csv(file_csv)
X = np.load(file_npy)

X_train = X[:int(0.9*len(X))]
X_test = X[int(0.9*len(X)):]
y_train = Y[:int(0.9*len(Y))]
y_test = Y[int(0.9*len(Y)):]

y_train = y_train.values.ravel()
y_test = y_test.values.ravel()


# Hyperparameter lists
param_grid = {
    "n_estimators" : [50, 100, 200],
    "max_depth" : [None, 10, 20, 30],
    "min_samples_split" : [2, 5, 10],
    "max_features" : ['sqrt', 'log2', None, 0.8, 0.9]
}

model = RandomForestRegressor(random_state=91)
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, n_jobs=-1)
grid_search.fit(X_train, y_train)
best_params = grid_search.best_params_
best_model = grid_search.best_estimator_

y_pred = best_model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print the scores and current hyperparameters
print(first_arg)
print(best_params)
print(f"MSE: {mse}, MAE: {mae}, R²: {r2}")

