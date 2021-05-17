import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

# Simulation time
time_points = 601  # time points to plot
time_final = 600.0  # final time

# FOPDT parameters
Kp = 1
tau_p = 120.0
theta_p = 15.0

# Temperatures and times for simulation
temp_init = 20.0
desired_temp_1 = 60.0
desired_temp_2 = 40.0
desired_time_1 = 10
desired_time_2 = 300


# Process simulation
def process_simulation(y, t, u):
    dydt = (-(y-temp_init)+Kp * u) / tau_p
    return dydt


# PI control
def pi_control_interactive_simulation(Kc, tau_I):
    t = np.linspace(0, time_final, time_points)  # create time vector
    P = np.zeros(time_points)  # initialize proportional term
    I = np.zeros(time_points)  # initialize integral term
    e = np.zeros(time_points)  # initialize error
    OP = np.zeros(time_points)  # initialize controller output
    PV = np.ones(time_points) * temp_init  # initialize process variable
    SP = np.ones(time_points) * temp_init  # initialize setpoint
    SP[desired_time_1:] = desired_temp_1  # step up
    y0 = temp_init  # initial condition
    iae = 0.0  # initialize integral abs error
    # loop through all time steps
    for i in range(1, time_points):
        # simulate process for one time step
        ts = [t[i-1], t[i]]  # time interval
        y = odeint(process_simulation, y0, ts, args=(OP[max(0, i-int(theta_p))],))  # compute next step
        y0 = y[1]  # record new initial condition
        iae += np.abs(SP[i]-y0[0])  # calculate integral abs error
        # calculate new OP with PID
        PV[i] = y[1]  # record PV
        e[i] = SP[i]-PV[i]  # calculate error = SP - PV
        dt = t[i]-t[i-1]  # calculate time step
        P[i] = Kc * e[i]  # calculate proportional term
        I[i] = I[i-1]+(Kc / tau_I) * e[i] * dt  # calculate integral term
        OP[i] = P[i]+I[i]  # calculate new controller output
        # controller output limitation
        if OP[i] >= 100:
            OP[i] = 100.0
            I[i] = I[i-1]  # reset integral
        if OP[i] <= 0:
            OP[i] = 0.0
            I[i] = I[i-1]  # reset integral
    # plot PID response
    plt.figure(1, figsize=(15, 7))
    # plot setpoint and measured temperature
    plt.subplot(2, 2, 1)
    plt.plot(t, SP, c="k", ls="-", lw=2, label="Setpoint (SP)")
    plt.plot(t, PV, c="r", ls=":", lw=2, label="Temperature (PV)")
    plt.xlabel("time (sec)")
    plt.ylabel(r"T $(^oC)$")
    plt.text(200, 40, f"Integral Abs Error: {np.round(iae, 2)}")
    plt.text(200, 35, f"$K_c$: {np.round(Kc, 0)}")
    plt.text(200, 30, f"$\\tau_I$: {np.round(tau_I, 0)} sec")
    plt.legend(loc="best")
    # plot terms
    plt.subplot(2, 2, 2)
    plt.plot(t, P, 'g.-', linewidth=2, label=r"Proportional = $K_c e(t)$")
    plt.plot(t, I, 'b-', linewidth=2, label=r"Integral = $\frac{K_c}{\tau_I} \int_{i=0}^{n_t} e(t)dt$")
    plt.xlabel("time (sec)")
    plt.ylabel("Terms")
    plt.legend(loc="best")
    # plot error
    plt.subplot(2, 2, 3)
    plt.plot(t, e, c="m", ls="--", lw=2, label="Error (e=SP-PV)")
    plt.xlabel('time (sec)')
    plt.ylabel(r"$\Delta T$ $(^oC)$")
    plt.legend(loc="best")
    # plot output
    plt.subplot(2, 2, 4)
    plt.plot(t, OP, c="b", ls="--", lw=2, label="Heater (OP)")
    plt.xlabel("time (sec)")
    plt.ylabel("Output (%)")
    plt.legend(loc="best")
    plt.show()


# Kc_slide = wg.FloatSlider(value=5.0, min=0.0, max=20.0, step=1.0)
# tau_I_slide = wg.FloatSlider(value=50.0, min=1.0, max=180.0, step=1.0)
# wg.interact(pi_control_interactive_simulation, Kc=Kc_slide, tau_I=tau_I_slide)
print('PI Simulator: Adjust Kc and tau_I for lowest Integral Abs Error')
pi_control_interactive_simulation(5, 50)
