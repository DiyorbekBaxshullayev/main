import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1.63, -2.39, 400)
y = np.linspace(-0.9, -1.49, 400)

X, Y = np.meshgrid(x, y)

Z = np.sin(X**2 + Y**2)

plt.figure(figsize=(8, 6))
contour = plt.contour(X, Y, Z, levels=19, cmap='viridis')
plt.colorbar(contour)
plt.title("2D Kontur Diagrammasi")
plt.xlabel("X o‘qi")
plt.ylabel("Y o‘qi")
plt.grid(True)
plt.tight_layout()
plt.show()
