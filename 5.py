import matplotlib.pyplot as plt
import numpy as np

cities = ['Toshkent', 'Samarqand', 'Buxoro', 'Andijon', 'Namangan', 
          'Farg\'ona', 'Qarshi', 'Nukus', 'Urganch', 'Jizzax']
population = np.array([2578, 546, 280, 441, 626, 288, 254, 136, 145, 179])  
avg_iq = np.array([98, 97, 96, 95, 94, 93, 92, 91, 90, 89])  
gdp = np.array([15.2, 8.7, 7.5, 6.8, 6.5, 5.9, 5.3, 4.8, 4.5, 4.2])  

plt.figure(figsize=(12, 8))
scatter = plt.scatter(
    x=avg_iq,  
    y=gdp,     
    s=population*2,  
    c=population,   
    cmap='plasma',  
    alpha=0.8,
    edgecolor='black',
    linewidth=0.5
)

for i, city in enumerate(cities):
    plt.text(avg_iq[i], gdp[i], city, fontsize=9, ha='center', va='bottom')

cbar = plt.colorbar(scatter)
cbar.set_label('Aholi soni (ming kishi)')

sizes = [500, 1000, 2000]
labels = ['250k', '500k', '1M']
for size, label in zip(sizes, labels):
    plt.scatter([], [], c='gray', alpha=0.5, s=size, label=label)
plt.legend(title='Aholi soni', loc='upper right')

plt.title('Shaharlar: IQ, GDP va Aholi Soni', pad=20)
plt.xlabel('O\'rtacha IQ darajasi')
plt.ylabel('Yalpi Ichki Mahsulot (mlrd $)')
plt.grid(True, linestyle='--', alpha=0.3)

plt.tight_layout()
plt.show()