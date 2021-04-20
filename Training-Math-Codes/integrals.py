import numpy as np
from scipy.integrate import simps


def calculate_integral(function, x_min, x_max, num_points=5000):
    x = np.linspace(x_min, x_max, num_points)
    y = np.vectorize(function)(x)
    dx = (x_max-x_min) / num_points
    return np.trapz(y, x, dx)

# def calculate_integral(function, x_min, x_max, num_points=5000):
#     x = np.linspace(x_min, x_max, num_points)
#     y = np.vectorize(function)(x)
#     return simps(y, x)


print(calculate_integral(lambda x: x ** 2, 0, 1)) # Should be close to 0.333
print(calculate_integral(lambda x: np.sin(x ** 2), 0, 5)) # Should be close to 0.528

circle_piece_area = calculate_integral(lambda x: np.sqrt(1 - x ** 2), 0, 1)
total_area = 4 * circle_piece_area
print(total_area)