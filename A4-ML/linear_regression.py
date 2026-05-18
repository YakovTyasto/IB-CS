import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Sample data
x = np.array([45, 48, 65, 68, 68, 10, 84, 22, 37, 88,
              71, 89, 89, 13, 59, 66, 40, 88, 47, 89])

y = np.array([98, 92, 134, 135, 136, 30, 175, 54, 70, 182,
              148, 169, 187, 20, 126, 142, 90, 186, 99, 176])

# Convert x from 1D array into 2D array
x = x.reshape(-1, 1)

# Create and train the model
model = LinearRegression()
model.fit(x, y)

# Get regression parameters
intercept = model.intercept_
slope = model.coef_[0]

# Predict value when x = 70
x_test = np.array([[70]])

y_test_predict = model.predict(x_test)

print(f"Prediction for independent variable value 70: {y_test_predict[0]}")

# Create regression line
x_line = np.array([[0], [100]])
y_line = intercept + slope * x_line

# Plot data points
plt.scatter(x, y, color="blue")

# Plot regression line
plt.plot(x_line, y_line, color="red", linewidth=2)

# Labels and title
plt.xlabel("Independent variable")
plt.ylabel("Dependent variable")
plt.title("Linear Regression Example")

# Show graph
plt.show()