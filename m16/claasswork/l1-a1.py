# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Titanic Dataset.csv')

print(data.head())

print(data.info)

# Summary statistics for Age
print("Age Summary:\n", data['Age'].describe())

# Plot histogram of Age
plt.figure(figsize=(6,4))
sns.histplot(data['Age'].dropna(), bins=20, kde=True, color="skyblue")
plt.title("Distribution of Passenger Ages")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()