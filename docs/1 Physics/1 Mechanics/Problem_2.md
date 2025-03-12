# Problem 2

### 1. Theoretical Foundation

#### Differential Equation

The motion of a forced damped pendulum is governed by a second-order nonlinear differential equation. 

For a pendulum of length $L$, mass $m$, under gravitational acceleration $g$, with damping coefficient $b$, and an external periodic force $F(t) = F_0 \cos(\omega t)$, the equation is:

$$
mL\frac{d^2\theta}{dt^2} + b\frac{d\theta}{dt} + mg\sin\theta = F_0 \cos(\omega t)
$$

Dividing through by $mL$:

$$
\frac{d^2\theta}{dt^2} + \frac{b}{m}\frac{d\theta}{dt} + \frac{g}{L}\sin\theta = \frac{F_0}{mL}\cos(\omega t)
$$

Define:

- Natural frequency: $\omega_0 = \sqrt{\frac{g}{L}}$
- Damping ratio: $\gamma = \frac{b}{m}$ (often written as $\beta = \frac{b}{2m}$ in some contexts)
- Driving amplitude: $A = \frac{F_0}{mL}$

So the equation becomes:

$$
\frac{d^2\theta}{dt^2} + \gamma\frac{d\theta}{dt} + \omega_0^2 \sin\theta = A \cos(\omega t)
$$

This is a nonlinear equation due to the $\sin\theta$ term, making it rich with complex behavior.

#### Small-Angle Approximation

For small angles ($\theta \ll 1$), $\sin\theta \approx \theta$, reducing the equation to a linear form:

$$
\frac{d^2\theta}{dt^2} + \gamma\frac{d\theta}{dt} + \omega_0^2 \theta = A \cos(\omega t)
$$

This is the equation of a damped harmonic oscillator with a periodic driving force. 

The general solution is the sum of the homogeneous solution (transient) and particular solution (steady-state):

- **Homogeneous solution**: 

  $$
  \theta_h(t) = e^{-\gamma t/2} \left( C_1 \cos(\omega_d t) + C_2 \sin(\omega_d t) \right)
  $$

  where $\omega_d = \sqrt{\omega_0^2 - (\gamma/2)^2}$ is the damped frequency (assuming underdamping, $\gamma < 2\omega_0$).

- **Particular solution**: For the driving term $A \cos(\omega t)$, assume:

  $$
  \theta_p(t) = B \cos(\omega t) + C \sin(\omega t)
  $$

  Substitute into the equation, solve for $B$ and $C$, and find the amplitude:

  $$
  B = \frac{A (\omega_0^2 - \omega^2)}{(\omega_0^2 - \omega^2)^2 + (\gamma \omega)^2}, \quad C = \frac{A \gamma \omega}{(\omega_0^2 - \omega^2)^2 + (\gamma \omega)^2}
  $$

  The steady-state amplitude is:

  $$
  D = \sqrt{B^2 + C^2} = \frac{A}{\sqrt{(\omega_0^2 - \omega^2)^2 + (\gamma \omega)^2}}
  $$

#### Resonance Conditions

Resonance occurs when the driving frequency $\omega$ approaches the natural frequency $\omega_0$. The amplitude $D$ peaks when $\omega = \omega_0$, maximizing energy transfer from the driving force to the pendulum. 

For small damping ($\gamma \ll \omega_0$), the peak amplitude scales as $D \propto \frac{A}{\gamma \omega_0}$, showing that lighter damping leads to sharper resonance. This energy amplification is critical in systems like mechanical oscillators or electrical circuits.

---

### 2. Analysis of Dynamics

#### Influence of Parameters

- **Damping Coefficient ($\gamma$)**:

  Low $\gamma$: Sustained oscillations with large amplitude near resonance.

  High $\gamma$: Overdamping suppresses oscillations, and the system settles to the driving rhythm or equilibrium.

- **Driving Amplitude ($A$)**: 

  Small $A$: Linear behavior dominates (small-angle approximation holds).

  Large $A$: Nonlinear effects (e.g., $\sin\theta$) become significant, potentially driving the pendulum over the top ( librations to rotations) or into chaos.

- **Driving Frequency ($\omega$)**: 

  $\omega \approx \omega_0$: Resonance amplifies motion.

  $\omega \ll \omega_0$: The pendulum follows the slow driving force.

  $\omega \gg \omega_0$: Small, rapid oscillations with reduced amplitude.

#### Transition to Chaos

For large driving amplitudes or specific frequency ratios, the nonlinear $\sin\theta$ term triggers complex dynamics:

- **Regular Motion**: At low $A$, the pendulum oscillates periodically, possibly synchronized with the driving force (period-1 motion).
- **Quasiperiodic Motion**: Multiple incommensurate frequencies emerge, seen in Poincaré sections as closed curves.
- **Chaotic Motion**: Sensitive dependence on initial conditions appears, with aperiodic motion and a strange attractor in phase space. This often occurs when $A$ exceeds a critical threshold, dependent on $\gamma$ and $\omega/\omega_0$.

The transition is analyzed via bifurcation diagrams, where $\theta$ or $d\theta/dt$ is plotted against $A$ or $\omega$, showing period-doubling routes to chaos.

---

### 3. Practical Applications

The forced damped pendulum model applies to:

- **Energy Harvesting**: Piezoelectric devices convert mechanical vibrations (modeled as driven oscillators) into electrical energy, optimized near resonance.
- **Suspension Bridges**: External forces (wind, traffic) can drive oscillations; Tacoma Narrows’ collapse (1940) is a dramatic example of resonance and nonlinearity.
- **Oscillating Circuits**: LC circuits with external AC sources mimic the pendulum’s dynamics, used in signal processing.

In each case, understanding resonance and chaos helps design stable or efficient systems.

---

### 4. Implementation

#### Computational Model

[Simulation model motion of pendulum](pendulum.html)

Here’s a Python snippet using the `scipy.integrate.odeint` solver to simulate the pendulum:

```python
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
```

#### Visualization
- **Time Series**: Shows $\theta(t)$ under given parameters.
- **Phase Diagram**: Plots $\theta$ vs. $\dot{\theta}$, revealing periodic orbits or chaotic attractors.
- **Poincaré Section**: Samples at intervals of the driving period, highlighting transitions (e.g., points for periodic, dense patterns for chaos).


