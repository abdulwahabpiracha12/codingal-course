# Simulate Central Limit Theorem by generating samples of size 1, 10, 50, and 100
# and plotting histograms for each

import numpy as np
import matplotlib.pyplot as plt

num = [1, 10, 50, 100]   # sample sizes
means = []

for j in num:
    np.random.seed(1)
    
    # Generate 1000 samples and compute their means
    x = [np.mean(np.random.randint(-40, 40, j)) for _ in range(1000)]
    
    means.append(x)

k = 0

# Create 2x2 subplot
fig, ax = plt.subplots(2, 2, figsize=(6, 6))

for i in range(2):
    for j in range(2):
        ax[i, j].hist(means[k], bins=10, density=True)
        ax[i, j].set_title(f"Sample size = {num[k]}")
        k += 1

plt.show()