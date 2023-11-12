import numpy as np

def knn_regression(points, k, x_query):
    """Performs k-NN Regression."""
    distances = np.linalg.norm(points[:, 0] - x_query, axis=0)
    nearest_indices = np.argsort(distances)[:k]
    return np.mean(points[nearest_indices, 1])

# Main program
N = int(input("Enter N (positive integer): "))
k = int(input("Enter k (positive integer): "))

if k > N:
    print("Error: k cannot be greater than N.")
else:
    points = np.array([list(map(float, input(f"Enter x and y for point {i+1}: ").split())) for i in range(N)])
    X = float(input("Enter X value for prediction: "))
    Y = knn_regression(points, k, X)
    print(f"Predicted Y value: {Y}")
