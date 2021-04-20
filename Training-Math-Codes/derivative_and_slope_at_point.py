from celluloid import Camera
from IPython.display import HTML
import matplotlib.pyplot as plt
import numpy as np


def calculate_derivative_at_point(function, point, precision=1e-7):
    # forward
    # return (function(point+precision)-function(point)) / precision
    # backward
    # return (function(point)-function(point-precision)) / precision
    # forward and backward
    return (function(point+precision)-function(point-precision)) / (2 * precision)


def plot_derivative(function, derivative=None, min_x=-10, max_x=10):
    x = np.linspace(min_x, max_x, 1000)
    y = np.vectorize(function)(x)

    if derivative is None:
        dy = np.vectorize(calculate_derivative_at_point)(function, x)
    else:
        dy = np.vectorize(derivative)(x)

    plt.plot(x, y, label="Function", color="blue")
    plt.plot(x, dy, label="Derivative", color="red")
    plt.xlabel("x", fontsize="x-large")
    plt.ylabel("y", fontsize="x-large")
    plt.legend(loc="lower right")
    plt.title("Function and its Derivative")
    plt.grid()
    plt.show()


plot_derivative(lambda x: x ** 2, lambda x: 2 * x)  # The derivative is calculated by hand
plot_derivative(lambda x: x ** 2)  # The derivative is not pre-calculated, should be calculated inside the function
plot_derivative(np.sin)


def plot_derivative_at_point(function, point, derivative=None, min_x=-10, max_x=10):
    x = np.linspace(min_x, max_x, 1000)
    y = np.vectorize(function)(x)

    if derivative is None:
        slope = calculate_derivative_at_point(function, point)
    else:
        slope = derivative(point)

    intercept = function(point)-slope * point
    tangent_line_x = np.linspace(point-2, point+2, 10)
    tangent_line_y = slope * tangent_line_x+intercept

    plt.plot(x, y, label="Function", color="blue")
    plt.plot(tangent_line_x, tangent_line_y, label="Tangent", color="red")
    plt.scatter(point, function(point), label="Contact point", color="green")
    plt.xlabel("x", fontsize="x-large")
    plt.ylabel("y", fontsize="x-large")
    plt.legend(loc="lower right")
    plt.title("Function and its Tangent Line")
    plt.grid()
    plt.show()


plot_derivative_at_point(lambda x: x ** 2, 2)
plot_derivative_at_point(lambda x: x ** 2, 2, min_x=0, max_x=4)
for x in np.arange(-8, 10, 2):
    plot_derivative_at_point(lambda x: x ** 2, x)
for x in np.arange(-8, 10, 2):
    plot_derivative_at_point(np.sin, x)


def animated_plot_derivative_at_point(function, point, derivative=None, min_x=-10, max_x=10):
    x = np.linspace(min_x, max_x, 1000)
    y = np.vectorize(function)(x)

    if derivative is None:
        slope = calculate_derivative_at_point(function, point)
    else:
        slope = derivative(point)

    intercept = function(point)-slope * point
    tangent_line_x = np.linspace(point-2, point+2, 10)
    tangent_line_y = slope * tangent_line_x+intercept

    plt.plot(x, y, color="blue")
    plt.plot(tangent_line_x, tangent_line_y, color="red")
    plt.xlabel("x", fontsize="x-large")
    plt.ylabel("y", fontsize="x-large")
    plt.legend(["Function", "Tangent Line"], loc="upper left")
    plt.title("Function and its Tangent Line")
    plt.grid(True)
    camera.snap()


fig = plt.figure(figsize=(5, 4), facecolor="w")
camera = Camera(fig)
for x in np.arange(-8, 10, 0.1):
    animated_plot_derivative_at_point(lambda x: x ** 2, x)
animate = camera.animate()
animate.save("derivative_1.gif")
HTML(animate.to_html5_video())
fig = plt.figure(figsize=(5, 4), facecolor="w")
camera = Camera(fig)
for x in np.arange(-8, 10, 0.1):
    animated_plot_derivative_at_point(np.sin, x)
animate = camera.animate()
animate.save("derivative_2.gif")
HTML(animate.to_html5_video())
