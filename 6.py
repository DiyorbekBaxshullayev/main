import numpy as np
import matplotlib.pyplot as plt

lambda_val = 41
sample_size = 6326
binlar_soni = 40

sample = np.random.poisson(lam=lambda_val, size=sample_size)

plt.figure(figsize=(10, 6))
plt.hist(sample, bins=binlar_soni, edgecolor='black', color='skyblue')
plt.title(f'Poisson taqsimoti bo\'yicha histogramma (λ={lambda_val}, n={sample_size})')
plt.xlabel('Qiymatlar')
plt.ylabel('Chiqlanishlar soni')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
