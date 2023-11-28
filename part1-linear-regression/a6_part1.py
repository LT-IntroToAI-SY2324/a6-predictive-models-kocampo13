import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv("part1-linear-regression/blood_pressure_data.csv")
x = data["Age"].values
y = data["Blood Pressure"].values

# Use reshape to turn the x values into 2D arrays:
x = x.reshape(-1,1)

# Create the model
model = LinearRegression().fit(x, y)

# Find the coefficient, bias, and r squared values. 
# Each should be a float and rounded to two decimal places. 
coeff = round(float(model.coeff_), 2)
intercept = round(float(model.intercept_), 2)
r_squared = model.score(x, y)

# Print out the linear equation and r squared value
x_predict = 110

# Predict the the blood pressure of someone who is 43 years old.
# Print out the prediction
prediction = model.predict([[x_predict]])

# Create the model in matplotlib and include the line of best fit

print(f"Model's Linear Equation: y = {coef}x + {intercept}")
print(f"R Squared value: {r_squared}")
print(f"Prediction when x is {x_predict}: {prediction}")

plt.figure(figsize=(5, 4))

plt.scatter(x,y, c="purple")
plt.scatter(x_predict, prediction, c="blue")

plt.xlabel("Age")
plt.ylabel("Average Blood Pressure")
plt.title("Average Blood Pressure by Age")

plt.plot(x, coef*x + intercept, c="r", label="Line of Best Fit")

plt.legend()
plt.show()