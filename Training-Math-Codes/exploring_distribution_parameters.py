import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import scipy.io.wavfile
from scipy.fftpack import fft, fftfreq


def plot_binomial_distribution(x, n, p):
    binomial = scipy.stats.binom.pmf(x, n, p)
    plt.scatter(x, binomial, color="blue")
    plt.vlines(x, 0, binomial, color="blue", linewidth=5, alpha=0.5)
    plt.xlabel("Number of successes")
    plt.ylabel("Probability")
    plt.title("Binomial Distribution")
    plt.grid()
    plt.show()


def plot_gaussian_distribution(x, mu, sigma):
    gaussian = scipy.stats.norm.pdf(x, loc=mu, scale=sigma)
    plt.plot(x, gaussian, color="blue")
    plt.xlabel("Number of successes")
    plt.ylabel("Probability")
    plt.title("Gaussian Distribution")
    plt.grid()
    plt.show()


# Example
x_binomial = np.arange(1, 10)
plot_binomial_distribution(x_binomial, 10, 0.5)
x_gaussian = np.linspace(-3, 3, 1000)
plot_gaussian_distribution(x_gaussian, 0, 1)

# Test Binomial Distribution by changing "n" the number of trials and keep "p" probability 0.5
x_binomial = np.arange(1, 50)
plot_binomial_distribution(x_binomial, 0, 0.5)
plot_binomial_distribution(x_binomial, 10, 0.5)
plot_binomial_distribution(x_binomial, 30, 0.5)
plot_binomial_distribution(x_binomial, 50, 0.5)
plot_binomial_distribution(x_binomial, 70, 0.5)

# Test Binomial Distribution by changing "p" probability (0-1) and keep "n" the number of trials 20
x_binomial = np.arange(1, 25)
plot_binomial_distribution(x_binomial, 20, 0)
plot_binomial_distribution(x_binomial, 20, 0.3)
plot_binomial_distribution(x_binomial, 20, 0.5)
plot_binomial_distribution(x_binomial, 20, 0.7)
plot_binomial_distribution(x_binomial, 20, 1)

# Test Gaussian Distribution by changing "mu" and keep "sigma"
x_gaussian = np.linspace(-10, 10, 1000)
plot_gaussian_distribution(x_gaussian, -5, 1)
plot_gaussian_distribution(x_gaussian, -3, 1)
plot_gaussian_distribution(x_gaussian, 0, 1)
plot_gaussian_distribution(x_gaussian, 3, 1)
plot_gaussian_distribution(x_gaussian, 5, 1)

# Test Gaussian Distribution by changing "sigma" and keep "mu"
x_gaussian = np.linspace(-10, 10, 1000)
plot_gaussian_distribution(x_gaussian, 0, 0.1)
plot_gaussian_distribution(x_gaussian, 0, 1.1)
plot_gaussian_distribution(x_gaussian, 0, 2.1)
plot_gaussian_distribution(x_gaussian, 0, 3.1)
plot_gaussian_distribution(x_gaussian, 0, 4.1)