import numpy as np
import matplotlib.pyplot as plt

n = 920

x = np.random.normal(loc=50, scale=10, size=n)  
y = np.random.normal(loc=30, scale=5, size=n) 

plt.figure(figsize=(10, 6))
plt.scatter(x, y, alpha=0.6, color='purple', edgecolor='k')
plt.title('Ikkita o\'zgaruvchi uchun tarqalish diagrammasi')
plt.xlabel('1-o\'zgaruvchi (X)')
plt.ylabel('2-o\'zgaruvchi (Y)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
