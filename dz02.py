import numpy as np
import scipy.integrate as spi

# Визначення функції для інтегрування
def f(x):
    return x ** 2

# Межі інтегрування
a = 0
b = 2

# Кількість випадкових точок для методу Монте-Карло
n_points = 100000

# Генерація випадкових точок в межах [a, b]
x_random = np.random.uniform(a, b, n_points)
y_random = np.random.uniform(0, max(f(np.linspace(a, b, 100))), n_points)

# Підрахунок кількості точок, що потрапляють під графік функції
under_curve = y_random < f(x_random)

# Площа під кривою методом Монте-Карло
monte_carlo_integral = (b - a) * max(f(np.linspace(a, b, 100))) * np.sum(under_curve) / n_points

# Перевірка результату за допомогою функції quad
result, error = spi.quad(f, a, b)

# Результати
print(monte_carlo_integral)
print(result)
print(error)
