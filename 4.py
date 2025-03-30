import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 3, 4, 5])
y = np.array([2, 6, 8, 10])

def newton_interpolation(x, y, x_interp):
    n = len(x)
    F = np.zeros((n, n))
    F[:, 0] = y  

    for j in range(1, n):
        for i in range(n - j):
            F[i, j] = (F[i + 1, j - 1] - F[i, j - 1]) / (x[i + j] - x[i])

    result = F[0, 0]
    for j in range(1, n):
        term = F[0, j]
        for k in range(j):
            term *= (x_interp - x[k])
        result += term

    return result

x_interp = 4.2
y_interp = newton_interpolation(x, y, x_interp)

print(f"x = {x_interp} da Nyuton interpolyatsion polinom qiymati: {y_interp:.4f}")

x_range = np.linspace(1, 5, 100)
y_range = [newton_interpolation(x, y, xi) for xi in x_range]

plt.plot(x, y, 'o', label="Berilgan nuqtalar")
plt.plot(x_range, y_range, label="Nyuton Interpolyatsion Polinomi")
plt.scatter(x_interp, y_interp, color='red', label=f"x={x_interp} da y={y_interp:.4f}")
plt.legend()
plt.grid()
plt.title("Nyuton Interpolyatsion Polinomi")
plt.xlabel("x")
plt.ylabel("y")
plt.show()