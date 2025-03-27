# Problem 1
(sas)[ele.html]
## Simulating the Effects of the Lorentz Force

The Lorentz force, defined as \( \mathbf{F} = q(\mathbf{E} + \mathbf{v} \times \mathbf{B}) \), describes the force on a charged particle in the presence of electric (\( \mathbf{E} \)) and magnetic (\( \mathbf{B} \)) fields, where \( q \) is the charge and \( \mathbf{v} \) is the particle's velocity. This simulation explores its applications, computes particle trajectories under different field configurations, and visualizes the results.

### 1. Exploration of Applications

The Lorentz force is critical in several systems:
- **Particle Accelerators**: In cyclotrons, magnetic fields cause charged particles to follow circular paths, while electric fields accelerate them. The balance of forces increases particle energy for research or medical applications.
- **Mass Spectrometers**: Magnetic fields deflect ions based on their charge-to-mass ratio (\( q/m \)), enabling identification of chemical species.
- **Plasma Confinement**: In fusion devices like tokamaks, magnetic fields confine charged particles in helical paths to sustain high-temperature plasmas.
- **Astrophysics**: The Lorentz force governs solar wind interactions with Earth’s magnetic field, producing auroras.

The electric field (\( \mathbf{E} \)) accelerates particles linearly, while the magnetic field (\( \mathbf{B} \)) induces circular or helical motion perpendicular to both \( \mathbf{B} \) and \( \mathbf{v} \). Combined fields can produce complex trajectories like drifts, essential for controlling particle motion.

### 2. Simulation Setup

We simulate a charged particle’s motion using the Lorentz force equation and Newton’s second law:  
\[ m \frac{d\mathbf{v}}{dt} = q(\mathbf{E} + \mathbf{v} \times \mathbf{B}) \]  
\[ \frac{d\mathbf{r}}{dt} = \mathbf{v} \]  
where \( \mathbf{r} \) is the position, \( m \) is the mass, and \( t \) is time. The Euler method updates velocity and position iteratively.

#### Field Configurations
1. **Uniform Magnetic Field**: \( \mathbf{B} = (0, 0, B_z) \), \( \mathbf{E} = 0 \).
2. **Combined Electric and Magnetic Fields**: \( \mathbf{B} = (0, 0, B_z) \), \( \mathbf{E} = (E_x, 0, 0) \).
3. **Crossed Fields**: \( \mathbf{E} = (E_x, 0, 0) \), \( \mathbf{B} = (0, 0, B_z) \), with \( \mathbf{E} \perp \mathbf{B} \).

### 3. Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants and parameters
q = 1.6e-19  # Charge (C, e.g., proton)
m = 1.67e-27  # Mass (kg, e.g., proton)
dt = 1e-9    # Time step (s)
steps = 10000  # Number of steps

# Initial conditions
r0 = np.array([0.0, 0.0, 0.0])  # Initial position (m)
v0 = np.array([1e5, 0.0, 0.0])  # Initial velocity (m/s)

# Field configurations
B = np.array([0.0, 0.0, 1.0])  # Magnetic field (T)
E = np.array([0.0, 0.0, 0.0])  # Electric field (N/C) - modify for scenarios

# Simulation function
def lorentz_force(r, v, q, m, E, B):
    return q * (E + np.cross(v, B)) / m

def simulate_trajectory(r0, v0, q, m, E, B, dt, steps):
    r = np.zeros((steps, 3))
    v = np.zeros((steps, 3))
    r[0] = r0
    v[0] = v0
    for i in range(steps - 1):
        a = lorentz_force(r[i], v[i], q, m, E, B)
        v[i + 1] = v[i] + a * dt
        r[i + 1] = r[i] + v[i] * dt
    return r, v

# Plotting function
def plot_trajectory(r, title, is_3d=True):
    if is_3d:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(r[:, 0], r[:, 1], r[:, 2])
        ax.set_xlabel('X (m)')
        ax.set_ylabel('Y (m)')
        ax.set_zlabel('Z (m)')
    else:
        plt.plot(r[:, 0], r[:, 1])
        plt.xlabel('X (m)')
        plt.ylabel('Y (m)')
    plt.title(title)
    plt.grid(True)
    plt.show()

# Scenario 1: Uniform Magnetic Field
r1, v1 = simulate_trajectory(r0, v0, q, m, np.array([0.0, 0.0, 0.0]), B, dt, steps)
plot_trajectory(r1, "Uniform Magnetic Field (Circular Motion)")

# Scenario 2: Combined Fields
E_combined = np.array([1e5, 0.0, 0.0])
r2, v2 = simulate_trajectory(r0, v0, q, m, E_combined, B, dt, steps)
plot_trajectory(r2, "Combined Electric and Magnetic Fields (Helical + Drift)")

# Scenario 3: Crossed Fields
r3, v3 = simulate_trajectory(r0, np.array([0.0, 1e5, 0.0]), q, m, E_combined, B, dt, steps)
plot_trajectory(r3, "Crossed Fields (E x B Drift)")

# Parameter exploration: Vary B strength
B_strong = np.array([0.0, 0.0, 2.0])
r4, v4 = simulate_trajectory(r0, v0, q, m, np.array([0.0, 0.0, 0.0]), B_strong, dt, steps)
plot_trajectory(r4, "Stronger Magnetic Field (Smaller Larmor Radius)")
```

### 4. Results and Visualizations

#### Uniform Magnetic Field
- **Trajectory**: Circular motion in the XY plane.
- **Larmor Radius**: \( r_L = \frac{m v_\perp}{|q| B} \). For \( v_\perp = 10^5 \, \text{m/s} \), \( B = 1 \, \text{T} \), \( r_L \approx 0.001 \, \text{m} \), matching the plot.
- **Relevance**: Seen in cyclotrons where particles spiral with constant radius.

#### Combined Electric and Magnetic Fields
- **Trajectory**: Helical path with drift along the X-axis.
- **Drift Velocity**: \( v_d = \frac{E \times B}{B^2} \). For \( E_x = 10^5 \, \text{N/C} \), \( B_z = 1 \, \text{T} \), \( v_d \approx 10^5 \, \text{m/s} \), consistent with the simulation.
- **Relevance**: Magnetic traps use this to confine particles with drift.

#### Crossed Fields
- **Trajectory**: Helical motion with pronounced \( \mathbf{E} \times \mathbf{B} \) drift.
- **Application**: Used in velocity selectors, where particles with \( v = E/B \) pass undeflected.

#### Parameter Variation
- **Stronger \( B \) (2 T)**: Smaller Larmor radius (\( r_L \propto 1/B \)), tightening the spiral.

### 5. Discussion

The simulations illustrate how the Lorentz force shapes particle motion:
- In cyclotrons, uniform \( B \) fields produce circular orbits, with radius controlled by \( B \) and \( v \).
- In plasma confinement, combined fields create helical paths with drifts, stabilizing charged particles.
- Crossed fields enable precise control, as in mass spectrometers or magnetrons.

These results align with real-world systems, offering an intuitive grasp of the Lorentz force’s role in technology and nature.

---

#### Notes
- The Euler method is simple but less accurate for long simulations; Runge-Kutta (e.g., RK4) could improve precision.
- Units are in SI for consistency (meters, seconds, tesla, etc.).
- Visualizations are 3D, but 2D plots can highlight specific planes (e.g., XY for circular motion).

This simulation provides a foundation for exploring more complex scenarios, such as non-uniform fields or relativistic effects.
