# BREAST CANCER DATA ANALYSIS

# Install seaborn if needed (Colab usually has it)
# !pip install seaborn

# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_breast_cancer

# Style
sns.set(style="whitegrid")

# =========================
# LOAD DATA
# =========================
data = load_breast_cancer()

# Convert to DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

# Map target to labels
df['label'] = df['target'].map({0: 'Malignant', 1: 'Benign'})

print("Dataset shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())

# =========================
# BASIC INFO
# =========================
print("\nInfo:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

# =========================
# CLASS DISTRIBUTION
# =========================
plt.figure()
sns.countplot(x='label', data=df)
plt.title("Class Distribution")
plt.show()

# =========================
# CORRELATION HEATMAP
# =========================
plt.figure(figsize=(12, 10))
corr = df.drop('label', axis=1).corr()
sns.heatmap(corr, cmap='coolwarm')
plt.title("Feature Correlation Heatmap")
plt.show()

# =========================
# HISTOGRAMS
# =========================
df.hist(figsize=(15, 12))
plt.suptitle("Feature Distributions")
plt.show()

# =========================
# BOXPLOTS (Outliers)
# =========================
plt.figure(figsize=(12, 6))
sns.boxplot(data=df.iloc[:, :10])
plt.xticks(rotation=45)
plt.title("Boxplot of First 10 Features")
plt.show()

# =========================
# PAIRPLOT (Important Features)
# =========================
selected_features = ['mean radius', 'mean texture', 'mean perimeter', 'mean area']

sns.pairplot(df[selected_features + ['target']], hue='target')
plt.show()

# =========================
# KDE PLOTS
# =========================
plt.figure()
sns.kdeplot(data=df, x='mean radius', hue='label', fill=True)
plt.title("KDE Plot - Mean Radius")
plt.show()

# =========================
# SCATTER PLOT
# =========================
plt.figure()
sns.scatterplot(data=df, x='mean radius', y='mean texture', hue='target')
plt.title("Scatter Plot")
plt.show()

# =========================
# SUMMARY STATISTICS
# =========================
print("\nSummary Statistics:")
print(df.describe())

# =========================
# INSIGHTS (PRINT)
# =========================
print("\nBasic Insights:")
print("- Dataset has no missing values.")
print("- Benign cases are more frequent than malignant.")
print("- Some features show strong correlation (check heatmap).")
print("- Certain features clearly separate classes (see pairplot).")