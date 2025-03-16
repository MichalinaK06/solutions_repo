# Problem 1

### 1. Theoretical Foundation

Projectile motion is a classic two-dimensional problem governed by Newton’s laws. We’re dealing with an object launched with an initial velocity $v_0$ at an angle $\theta$ relative to the horizontal, under the influence of gravity $g$, and for now, we’ll assume no air resistance and a flat surface (launch height $h = 0$).

#### Deriving the Equations of Motion
The motion splits into horizontal (x) and vertical (y) components, and gravity only acts vertically. Start with the acceleration:

- Horizontal: $a_x = 0$ (no forces in x-direction).
- Vertical: $a_y = -g$ (gravity downward).

Initial conditions:

- Initial velocity in x: $v_{0x} = v_0 \cos\theta$.
- Initial velocity in y: $v_{0y} = v_0 \sin\theta$.
- Initial position: $(x_0, y_0) = (0, 0)$.

Using kinematics ($v = u + at$, $x = ut + \frac{1}{2}at^2$):

**Horizontal motion** (constant velocity):

- $v_x = v_0 \cos\theta$.
- $x(t) = (v_0 \cos\theta) t$.

**Vertical motion** (constant acceleration):

- $v_y = v_0 \sin\theta - gt$.
- $y(t) = (v_0 \sin\theta) t - \frac{1}{2} g t^2$.

This is a parametric description of a parabola. The projectile hits the ground when $y(t) = 0$. Solve for time of flight:

$$
0 = (v_0 \sin\theta) t - \frac{1}{2} g t^2
$$

Factor out $t$:
$$
t \left( v_0 \sin\theta - \frac{1}{2} g t \right) = 0
$$

- $t = 0$ (launch).

- $t = \frac{2 v_0 \sin\theta}{g}$ (landing, the time of flight $T$).

#### Family of Solutions

The parameters $v_0$, $\theta$, and $g$ define a family of trajectories. Changing $v_0$ scales the size of the parabola, $\theta$ adjusts its shape and orientation, and $g$ (e.g., Earth vs. Moon) alters the curvature. Launch height $h$ or air resistance would add complexity, but we’ll keep it simple for now.

---

### 2. Analysis of the Range

The range $R$ is the horizontal distance traveled when $y = 0$. 
Plug 

$$t = T = \frac{2 v_0 \sin\theta}{g}$$

into the x-equation:

$$
R = (v_0 \cos\theta) \cdot \frac{2 v_0 \sin\theta}{g}
$$

Use the identity $\sin 2\theta = 2 \sin\theta \cos\theta$:

$$R = \frac{v_0^2 \sin 2\theta}{g}$$

#### Dependence on Angle $\theta$
- **Maximum Range**: $R$ peaks when $\sin 2\theta = 1$, so $2\theta = 90^\circ$, or $\theta = 45^\circ$. Here, $R_{\text{max}} = \frac{v_0^2}{g}$.
- **Symmetry**: $\sin 2\theta = \sin (180^\circ - 2\theta)$, so $\theta$ and $90^\circ - \theta$ (e.g., 30° and 60°) give the same range.
- **Extremes**: At $\theta = 0^\circ$ or $90^\circ$, $\sin 2\theta = 0$, so $R = 0$.

#### Other Parameters
- **Initial Velocity $v_0$**: Range scales with $v_0^2$—double $v_0$, get four times the range.
- **Gravity $g$**: Inverse relationship—on the Moon ($g \approx 1.62 \, \text{m/s}^2$), range is much larger than on Earth ($g \approx 9.8 \, \text{m/s}^2$).

---

### 3. Practical Applications

This idealized model adapts to real-world scenarios:
- **Uneven Terrain**: If launched from height $h$, the time of flight changes. Solve $y(t) = h + (v_0 \sin\theta) t - \frac{1}{2} g t^2 = 0$ with the quadratic formula. Range still depends on $\theta$, but the optimal angle shifts (e.g., < 45° for a cliff launch).

- **Air Resistance**: Adds a drag force proportional to velocity (or $v^2$). Trajectories shorten and skew, and the optimal $\theta$ drops below 45°. Numerical methods or approximations are needed.

- **Examples**: A basketball shot (low $v_0$, air matters), artillery (high $v_0$, terrain matters), or a Mars rover landing (low $g$, thin atmosphere).

---

### 4. Implementation

[Simulation of projectile](simulation_projectile.html)

[How angle and velocity change in geogebra](https://www.geogebra.org/calculator/jubc9rkb})

[Graph of angle and velocity](prbl1.html)





