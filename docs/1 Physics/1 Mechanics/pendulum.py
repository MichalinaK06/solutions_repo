import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parameters
g = 9.81  # gravity (m/s^2)
L = 1.0   # length (m)
gamma = 0.5  # damping (1/s)
A = 1.5      # driving amplitude (m/s^2)
omega = 2.0  # driving frequency (rad/s)
omega0 = np.sqrt(g/L)

# Differential equation
def pendulum(y, t, gamma, omega0, A, omega):
    theta, theta_dot = y
    dtheta_dt = theta_dot
    dtheta_dot_dt = -gamma * theta_dot - omega0**2 * np.sin(theta) + A * np.cos(omega * t)
    return [dtheta_dt, dtheta_dot_dt]

# Time array
t = np.linspace(0, 50, 1000)

# Initial conditions [theta, theta_dot]
y0 = [0.1, 0.0]

# Solve
sol = odeint(pendulum, y0, t, args=(gamma, omega0, A, omega))
theta, theta_dot = sol.T

# Plot time series
plt.figure(figsize=(10, 4))
plt.plot(t, theta, label=r'$\theta(t)$')
plt.xlabel('Time (s)')
plt.ylabel('Angle (rad)')
plt.title('Forced Damped Pendulum Motion')
plt.legend()
plt.show()

# Phase diagram
plt.figure(figsize=(6, 6))
plt.plot(theta, theta_dot, lw=0.5)
plt.xlabel(r'$\theta$ (rad)')
plt.ylabel(r'$\dot{\theta}$ (rad/s)')
plt.title('Phase Space')
plt.show()

# Poincaré section (sample at driving period)
T = 2 * np.pi / omega
poincare_theta = theta[::int(len(t)*T/50)]
poincare_theta_dot = theta_dot[::int(len(t)*T/50)]
plt.scatter(poincare_theta, poincare_theta_dot, s=5)
plt.xlabel(r'$\theta$ (rad)')
plt.ylabel(r'$\dot{\theta}$ (rad/s)')
plt.title('Poincaré Section')
plt.show()