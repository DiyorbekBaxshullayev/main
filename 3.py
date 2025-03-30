import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

colors = ['#2e86c1', '#f1c40f', '#e74c3c'] 
cmap = LinearSegmentedColormap.from_list('mycmap', colors)

x = np.random.randn(200)
y = x + np.random.randn(200) * 0.5
z = np.sqrt(x**2 + y**2)

fig = plt.figure(figsize=(9, 7), facecolor='#212f3d')
ax = fig.add_subplot(111, facecolor='#1c2833')

sc = ax.scatter(x, y, c=z, cmap=cmap, s=100, alpha=0.8, 
               edgecolor='w', linewidth=0.5)

ax.set_title("To'liq Sozlangan Fon va Scatter Plot", 
            color='white', fontsize=14, pad=20)
ax.set_xlabel("X qiymatlari", color='white', fontsize=12)
ax.set_ylabel("Y qiymatlari", color='white', fontsize=12)

ax.tick_params(axis='both', colors='white')
ax.spines['bottom'].set_color('white')
ax.spines['top'].set_color('white') 
ax.spines['right'].set_color('white')
ax.spines['left'].set_color('white')

cbar = plt.colorbar(sc)
cbar.set_label('Radial masofa', color='white')
cbar.ax.yaxis.set_tick_params(color='white')
plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color='white')

plt.tight_layout()
plt.show()