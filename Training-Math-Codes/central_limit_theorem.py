import numpy as np
import matplotlib.pyplot as plt


# Create plot function just to see how the original functions looks
def plot_function(function, x_values, title):
    x = np.linspace(0, 1, x_values)
    y = np.vectorize(function)(x)
    plt.plot(x, y)
    plt.xlabel("x", fontsize="x-large")
    plt.ylabel("y", fontsize="x-large")
    plt.title(title, fontsize="x-large")
    plt.grid()
    plt.show()


# Plot all functions
plot_function(lambda x: 1, 2000, "$f(x)=1$")
plot_function(lambda x: 2 * x, 2000, "$f(x)=2x$")
plot_function(lambda x: 3 * x ** 2, 2000, "$f(x)=3x^2$")
plot_function(lambda x: 4 * np.abs(x-0.5), 2000, "$f(x)=4|x-0.5|$")
plot_function(lambda x: 2 - 4 * np.abs(x-0.5), 2000, "$f(x)=2-4|x-0.5|$")


def plot_clt_histogram(function, quantity_trails, quantity_random_numbers, data_ranges, title):
    sums = []
    for _ in range(quantity_trails):
        random_x = np.random.rand(quantity_random_numbers)
        y = np.vectorize(function)(random_x)
        y_sum = np.sum(y)
        sums.append(y_sum)
    plt.hist(sums, bins=data_ranges)
    plt.xlabel("Data Ranges (Bins)", fontsize="x-large")
    plt.ylabel("Observed Frequency", fontsize="x-large")
    plt.title(title, fontsize="x-large")
    plt.grid()
    plt.show()


# Plot the histograms with the basic "settings"
plot_clt_histogram(lambda x: 1, 1000, 25, 20, "$f(x)=1$")
plot_clt_histogram(lambda x: 2 * x, 1000, 25, 20, "$f(x)=2x$")
plot_clt_histogram(lambda x: 3 * x ** 2, 1000, 25, 20, "$f(x)=3x^2$")
plot_clt_histogram(lambda x: 4 * np.abs(x-0.5), 1000, 25, 20, "$f(x)=4|x-0.5|$")
plot_clt_histogram(lambda x: 2 - 4 * np.abs(x-0.5), 1000, 25, 20, "$f(x)=2-4|x-0.5|$")

# Plot the histograms with different "settings"
plot_clt_histogram(lambda x: 1, 5000, 50, 100, "$f(x)=1$")
plot_clt_histogram(lambda x: 2 * x, 5000, 50, 100, "$f(x)=2x$")
plot_clt_histogram(lambda x: 3 * x ** 2, 5000, 50, 100, "$f(x)=3x^2$")
plot_clt_histogram(lambda x: 4 * np.abs(x-0.5), 5000, 50, 100, "$f(x)=4|x-0.5|$")
plot_clt_histogram(lambda x: 2 - 4 * np.abs(x-0.5), 5000, 50, 100, "$f(x)=2-4|x-0.5|$")
