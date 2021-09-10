import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math
from scipy.integrate import odeint


def sys_val(initial, t):
    omega = initial[1]
    theta = initial[0]
    omega_prime = -(g / l) * math.sin(theta)
    return omega, omega_prime


def sp(i):  # function for animation
    ax1.cla()
    ax2.cla()
    ax3.cla()
    initial = [theta_0, omega_0]  # initial_angle, initial_omega
    theta_values = odeint(sys_val, initial, t)
    x = l * np.sin(theta_values[:, 0])
    y = (-l) * np.cos(theta_values[:, 0])

    # plotting ax1
    # [pendulum animation]
    ax1.set_title("PENDULUM ANIMATION")
    ax1.plot(x[len(x) - 1], y[len(y) - 1])
    # [rod]
    ax1.plot([0, x[len(x) - 1]], [0, y[len(y) - 1]])
    # path tracer for bob
    x_path.append(x[len(x) - 1])
    y_path.append(y[len(y) - 1])
    if len(t) > 5:
        x_path.pop(0)
        y_path.pop(0)
        ax1.plot(x_path, y_path)
    # [plotting preferences]
    ax1.set_xlim(-l - (0.5 * l), l + (0.5 * l))
    ax1.set_ylim(-l - (0.5 * l), 0)

    # plotting ax2 [x vs t] & ax3 [y vs t]
    ax2.plot(t, x)
    ax3.plot(t, x)
    ax2.set_title("x v/s t")
    ax3.set_title("y v/s t")

    # append
    t.append(t[len(t) - 1] + 0.05)


x_path = []
y_path = []
t = [0.0]
g = float(input("ENTER VALUE OF ACCLN DUE TO GRAVITY IN m/s*2:\n"))
l = float(input("ENTER LENGTH OF PENDULUM IN m:\n"))
theta_0 = float(input("ENTER INITIAL ANGLE OF PENDULUM IN radians:\n"))
omega_0 = float(input("ENTER INITIAL ANGULAR VELOCITY OF PENDULUM IN radians/s:\n"))
fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1)
ani = FuncAnimation(fig, sp, interval=50)
plt.show()
plt.tight_layout()
plt.axis("equal")
