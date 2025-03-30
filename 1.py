import matplotlib.pyplot as plt
import numpy as np


x = np.random.rand(50)  
y = np.random.rand(50)  
colors = np.random.rand(50)  
sizes = 1000 * np.random.rand(50)  


plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='viridis')
plt.colorbar()  

plt.title("Tasodifiy Nuqtali Grafik")
plt.xlabel("X o'qi")
plt.ylabel("Y o'qi")

plt.show()