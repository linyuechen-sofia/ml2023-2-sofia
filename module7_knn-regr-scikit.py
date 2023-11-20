import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score

def knn_regression_and_r2(points, k, x_query):
    """Performs k-NN Regression and calculates R^2."""
    # Create and train the model
    model = KNeighborsRegressor(n_neighbors=k)
    model.fit(points[:, 0].reshape(-1, 1), points[:, 1])

    # Predicting for the given X value
    y_pred = model.predict(np.array([[x_query]]))

    # Calculating R^2
    r2 = r2_score(points[:, 1], model.predict(points[:, 0].reshape(-1, 1)))

    return y_pred[0], r2

# Main program
N = int(input("Enter N (positive integer): "))
k = int(input("Enter k (positive integer): "))

if k > N:
    print("Error: k cannot be greater than N.")
else:
    points = np.array([list(map(float, input(f"Enter x and y for point {i+1}: ").split())) for i in range(N)])
    X = float(input("Enter X value for prediction: "))
    Y, r2 = knn_regression_and_r2(points, k, X)
    print(f"Predicted Y value: {Y}")
    print(f"Coefficient of determination (R^2): {r2}")
