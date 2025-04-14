import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)

functions = [
    (1, 0),    # y = x
    (2, 1),    # y = 2x + 1
    (-1, 2),   # y = -x + 2
    (0.5, -3), # y = 0.5x - 3
    (-2, -1),  # y = -2x - 1
    (3, 0)     # y = 3x
]

fig, axs = plt.subplots(3, 2, figsize=(10, 10))

for i, ax in enumerate(axs.flat):
    k, b = functions[i]
    y = k * x + b
    ax.plot(x, y, label=f'y = {k}x + {b}')
    ax.set_title(f'Function {i+1}')
    ax.legend()
    ax.grid(True)

plt.tight_layout()
plt.show()
