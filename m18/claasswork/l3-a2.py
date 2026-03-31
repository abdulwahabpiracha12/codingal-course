import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.datasets import make_regression, make_classification
from sklearn.metrics import mean_squared_error, accuracy_score

x, y = make_regression(n_samples=100, n_features=1, noise=15, random_state=42)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

print("Mse: ", mean_squared_error(y_test, y_pred))

plt.scatter(x, y)
plt.plot(x_test, y_pred)
plt.title("Regression: Data + Best Fit Line")
plt.xlabel("x")
plt.ylabel("y")
plt.show()