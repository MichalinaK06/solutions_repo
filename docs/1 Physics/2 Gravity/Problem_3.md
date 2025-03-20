# Problem 3

### 1. Possible Trajectories of a Payload Released Near Earth

When a payload is released from a moving rocket near Earth, its trajectory depends on its initial position (relative to Earth’s center) and velocity (magnitude and direction) at the moment of release. Earth’s gravitational field governs the motion, and the resulting path can be classified using the specific orbital energy and angular momentum. The possible trajectories are:

- **Elliptical Trajectory**:

 If the payload’s total mechanical energy (kinetic + potential) is negative, it follows a bound orbit, typically an ellipse with Earth at one focus (per Kepler’s First Law). This occurs when the release velocity is less than the local escape velocity but sufficient to maintain a closed orbit. Example: A payload released with a tangential velocity slightly below circular orbit speed.

- **Circular Trajectory**:

 A special case of an elliptical orbit where the eccentricity is zero. This requires the release velocity to exactly match the circular orbit speed, $v_c = \sqrt{\frac{GM}{r}}$, where $G$ is the gravitational constant, $M$ is Earth’s mass, and $r$ is the distance from Earth’s center.

- **Parabolic Trajectory**:

 If the total energy is exactly zero, the payload follows a parabola, escaping Earth’s gravity with the minimum energy required. This happens when the release velocity equals the escape velocity, $v_e = \sqrt{\frac{2GM}{r}}$.

- **Hyperbolic Trajectory**:

 If the total energy is positive (velocity exceeds escape velocity), the payload follows an unbound hyperbolic path, escaping Earth indefinitely. This is common in scenarios like interplanetary probes launched with excess speed.

The trajectory type hinges on the **specific energy**:


$$\epsilon = \frac{v^2}{2} - \frac{GM}{r}$$

- $\epsilon < 0$: Elliptical (bound)

- $\epsilon = 0$: Parabolic (marginally unbound)

- $\epsilon > 0$: Hyperbolic (unbound)

---

### 2. Numerical Analysis of the Payload’s Path

Let’s compute the trajectory numerically with example initial conditions. Assume the payload is released from a rocket at:

- **Altitude**: $400$ km (common for low Earth orbit, LEO)

- **Distance from Earth’s center**: $r = R_e + h = 6371 \, \text{km} + 400 \, \text{km} = 6771 \, \text{km} = 6.771 \times 10^6 \, \text{m}$

- **Initial velocity**: We’ll test three cases to explore different trajectories.

- **Earth’s parameters**: $GM = 3.986 \times 10^{14} \, \text{m}^3/\text{s}^2$, $R_e = 6.371 \times 10^6 \, \text{m}$.

#### Governing Equations

The motion is governed by Newton’s Law of Gravitation in vector form:

$$\ddot{\mathbf{r}} = -\frac{GM}{r^3} \mathbf{r}$$

where $\mathbf{r}$ is the position vector from Earth’s center, and $r = |\mathbf{r}|$. In 2D Cartesian coordinates ($x, y$), with Earth at the origin:

$$\ddot{x} = -\frac{GM}{r^3} x, \quad \ddot{y} = -\frac{GM}{r^3} y$$

where $r = \sqrt{x^2 + y^2}$.

#### Initial Conditions

- **Position**: Released at $(x_0, y_0) = (6.771 \times 10^6, 0) \, \text{m}$ (along the x-axis).

- **Velocity Cases**:

  1. **Elliptical**: $v_0 = 7.5 \, \text{km/s}$ (tangential, below circular speed).

  2. **Parabolic**: $v_0 = v_e = \sqrt{\frac{2GM}{r}} \approx 11.1 \, \text{km/s}$ (tangential).

  3. **Hyperbolic**: $v_0 = 12.0 \, \text{km/s}$ (tangential, above escape speed).

- Velocity direction: $(v_x, v_y) = (0, v_0)$ (tangential along y-axis).

#### Numerical Method

Use a simple Euler method or a more accurate Runge-Kutta (RK4) integrator to solve these second-order ODEs. For brevity, I’ll outline the Euler approach:

- Discretize time: $\Delta t = 1 \, \text{s}$.

- Update rules:

$$v_x(t + \Delta t) = v_x(t) - \frac{GM}{r^3} x(t) \Delta t$$

$$x(t + \Delta t) = x(t) + v_x(t) \Delta t$$

  (Similarly for $y$ and $v_y$).

Running this for 10,000 seconds:

- **Elliptical**: The payload orbits Earth, completing an ellipse with perigee at 400 km and apogee depending on eccentricity.

- **Parabolic**: The payload moves outward, asymptotically approaching infinite distance with zero residual speed.

- **Hyperbolic**: The payload escapes rapidly, following a sharply curved path away from Earth.

---

### 3. Relation to Orbital Insertion, Reentry, and Escape

- **Orbital Insertion**: An elliptical or circular trajectory corresponds to successful orbit. For example, releasing a satellite at $7.5$ km/s tangentially at $400$ km altitude places it in LEO, ideal for deployment.

- **Reentry**: If the initial velocity is insufficient (e.g., suborbital, $< 7.5$ km/s at $400$ km), or if directed downward, the payload intersects Earth’s atmosphere, leading to reentry. Atmospheric drag then dominates, slowing it for landing or burn-up.

- **Escape**: Parabolic or hyperbolic trajectories result in escape. A payload released at $11.1$ km/s or higher escapes Earth’s gravity, relevant for lunar missions or beyond.

---

### 4. Visualization

[Orbital Trajectories Visualization](a.html)