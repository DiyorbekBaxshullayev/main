import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(150)  
y = x * 2 + np.random.randn(150) * 0.5 
sizes = np.abs(x) * 200  
colors = y  

plt.figure(figsize=(10, 7))
scatter = plt.scatter(
    x, y, 
    c=colors, 
    cmap='plasma', 
    s=sizes, 
    alpha=0.6,
    edgecolors='w',
    linewidth=0.5
)

cbar = plt.colorbar(scatter)
cbar.set_label('Y qiymati bo\'yicha gradient')

plt.title('Gradient Rangli va O\'lchami O\'zgaruvchan Scatter Plot')
plt.xlabel('X qiymatlari')
plt.ylabel('Y qiymatlari')
plt.grid(True, linestyle='--', alpha=0.5)

plt.show()