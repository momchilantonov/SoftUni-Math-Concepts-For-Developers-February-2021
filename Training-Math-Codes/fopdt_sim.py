import matplotlib.pyplot as plt
import numpy as np


# FOPDT model simulation
def fopdt_interactive_simulation(K_pr, tau_p, theta_p):
    time_points = 100  # time points to plot
    t = np.linspace(0, 20, 100)  # create time vector
    # create 0 -> 1 step at t=theta_p
    delay = np.empty_like(t)
    for i in range(time_points):
        if t[i] < theta_p:
            delay[i] = 0.0
        else:
            delay[i] = 1.0
    # calculate response to step input
    x = K_pr * (1.0-np.exp(-(t-theta_p) / tau_p))
    y = x * delay
    # plot response
    plt.figure(1, figsize=(15, 7))
    # plot input and step changes
    plt.subplot(1, 2, 1)
    plt.plot(t, x, c="r", ls="--", lw=2, label=r"$x(t-\theta_p)=K_{pr}(1-\exp(-(t-\theta_p)/\tau_p))$")
    plt.plot(t, delay, c="g", ls=":", lw=2, label=r"$S(t-\theta_p)$")
    plt.title("Input and step changes", fontsize="x-large")
    plt.xlabel("time(sec)", fontsize="large")
    plt.ylabel(r"$u(t)$", fontsize="large")
    plt.legend(loc="best")
    plt.ylim([-10, 10])
    plt.xlim([0, 20])
    plt.grid()
    # plot output response
    plt.subplot(1, 2, 2)
    plt.plot(t, y, c="k", ls='-', linewidth=4, label=r"$y(t)=x(t-\theta)S(t-\theta)$")
    plt.title("Output response", fontsize="x-large")
    plt.xlabel("time(sec)", fontsize="large")
    plt.ylabel(r"$y(t)$", fontsize="large")
    plt.legend(loc="best")
    plt.ylim([-10, 10])
    plt.xlim([0, 20])
    plt.grid()
    plt.show()


# K_pr_slide = wg.FloatSlider(value=3.0, min=-10.0, max=10.0, step=0.1)
# tau_p_slide = wg.FloatSlider(value=4.0, min=0.1, max=10.0, step=0.1)
# theta_p_slide = wg.FloatSlider(value=5.0, min=0.1, max=10.0, step=0.1)
# wg.interact(interactive_fopdt_simulation, K_pr=K_pr_slide, tau_p=tau_p_slide, theta_p=theta_p_slide)
print("FOPDT Simulator: Adjust K_pr, tau_p and theta_p")
fopdt_interactive_simulation(3, 4, 5)
