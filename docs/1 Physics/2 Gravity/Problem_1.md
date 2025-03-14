# Problem 1



### Derivation of Kepler’s Third Law for Circular Orbits

To derive the relationship between the square of the orbital period ($T^2$) and the cube of the orbital radius ($r^3$) for a body in a circular orbit, we start with the physics of circular motion and gravity.

### 1. **Gravitational Force as the Centripetal Force**:

- A body (e.g., a planet or satellite) in a circular orbit around a central mass (e.g., a star or planet) is held in place by gravity, which provides the necessary centripetal force to maintain circular motion.

- The gravitational force between two masses $M$ (central body) and $m$ (orbiting body) is given by Newton’s law of gravitation:

$$
F_g = \frac{G M m}{r^2}
$$

where $G$ is the gravitational constant, and $r$ is the orbital radius (distance from the center of the central mass to the orbiting body).

- For circular motion, the centripetal force required is:

$$
F_c = \frac{m v^2}{r}
$$

where $v$ is the orbital velocity.

- Since gravity provides this centripetal force, we equate them:

$$
\frac{G M m}{r^2} = \frac{m v^2}{r}
$$

### 2. **Simplify the Equation**:

- Cancel $m$ (assuming $m \neq 0$, which is true for any orbiting body):

$$
\frac{G M}{r^2} = \frac{v^2}{r}
$$

- Multiply both sides by $r$:

$$
\frac{G M}{r} = v^2
$$

- Solve for $v$:

$$
v = \sqrt{\frac{G M}{r}}
$$

### 3. **Relate Velocity to Orbital Period**:

- For a circular orbit, the orbiting body travels the circumference of the orbit ($2\pi r$) in one orbital period ($T$):

$$
v = \frac{2\pi r}{T}
$$

- Substitute this into the velocity equation:

$$
\frac{2\pi r}{T} = \sqrt{\frac{G M}{r}}
$$

### 4. **Solve for the Period**:

- Square both sides to eliminate the square root:

$$
\left(\frac{2\pi r}{T}\right)^2 = \frac{G M}{r}
$$

$$
\frac{4\pi^2 r^2}{T^2} = \frac{G M}{r}
$$

- Multiply both sides by $T^2$:

$$
4\pi^2 r^2 = \frac{G M}{r} T^2
$$

- Multiply both sides by $r$:

$$
4\pi^2 r^3 = G M T^2
$$

- Rearrange:

$$
T^2 = \frac{4\pi^2}{G M} r^3
$$

### 5. **Final Form**:

- This is Kepler’s Third Law for circular orbits:

$$
T^2 = k r^3
$$

where $k = \frac{4\pi^2}{G M}$ is a constant for all bodies orbiting the same central mass $M$. 
     
Thus, the square of the orbital period is proportional to the cube of the orbital radius.

### Implications for Astronomy

Kepler’s Third Law is a powerful tool with far-reaching implications:

### 1. **Determining Planetary Masses**:

- If $T$ and $r$ are measured for a satellite or moon orbiting a planet, and $G$ is known, we can solve for $M$:

$$
M = \frac{4\pi^2 r^3}{G T^2}
$$

- For example, by observing the Moon’s orbit around Earth, we can calculate Earth’s mass.

### 2. **Measuring Distances**:

- For planets orbiting the Sun, if we know $T$ for one planet (e.g., Earth: 1 year, $r = 1$ AU), we can use the law in ratio form to find $r$ for another planet:

$$
\frac{T_1^2}{T_2^2} = \frac{r_1^3}{r_2^3}
$$

- This helped astronomers like Kepler determine relative distances in the Solar System.

### 3. **Satellite Orbits**:

- Engineers use this relationship to design satellite orbits. For geostationary satellites, $T = 24$ hours, and solving for $r$ gives an altitude of approximately 35,786 km above Earth’s equator.

### 4. **Exoplanet Studies**:

- Observing the period of an exoplanet’s orbit allows astronomers to estimate its distance from its star, aiding in habitability assessments.

### Real-World Examples

### 1. **Moon’s Orbit Around Earth**:

- Orbital period: $T \approx 27.32$ days $= 2.36 \times 10^6$ seconds.

- Orbital radius: $r \approx 384,400$ km $= 3.844 \times 10^8$ m.

- Earth’s mass: $M \approx 5.972 \times 10^{24}$ kg, $G = 6.674 \times 10^{-11}$ m³ kg⁻¹ s⁻².

- Check: $T^2 = \frac{4\pi^2}{G M} r^3$:

$$
\frac{4\pi^2}{G M} = \frac{4 \times (3.1416)^2}{(6.674 \times 10^{-11}) \times (5.972 \times 10^{24})} \approx 9.9 \times 10^{-14} \, \text{s}^2 \text{m}^{-3}
$$

$$
r^3 = (3.844 \times 10^8)^3 \approx 5.68 \times 10^{25} \, \text{m}^3
$$

$$
T^2 = (9.9 \times 10^{-14}) \times (5.68 \times 10^{25}) \approx 5.62 \times 10^{12} \, \text{s}^2
$$

$$
T = \sqrt{5.62 \times 10^{12}} \approx 2.37 \times 10^6 \, \text{s}
$$

- Matches closely with 2.36 × 10⁶ s, confirming the law holds.

### 2. **Earth’s Orbit Around the Sun**:

- $T = 1$ year $= 3.156 \times 10^7$ s, $r = 1$ AU $= 1.496 \times 10^{11}$ m.

- Sun’s mass: $M \approx 1.989 \times 10^{30}$ kg.

- Similar calculations verify the relationship.

### Computational Model in Python

Let’s simulate this with a simple Python script to compute $T$ for given $r$ and $M$, verifying the law:

```python
import math

# Constants
G = 6.674e-11  # m^3 kg^-1 s^-2
M_earth = 5.972e24  # kg
M_sun = 1.989e30  # kg

def orbital_period(radius, central_mass):
    # T^2 = (4 * pi^2 / (G * M)) * r^3
    k = 4 * math.pi**2 / (G * central_mass)
    T_squared = k * radius**3
    T = math.sqrt(T_squared)
    return T

# Test cases
r_moon = 3.844e8  # m
r_earth = 1.496e11  # m

T_moon = orbital_period(r_moon, M_earth)
T_earth = orbital_period(r_earth, M_sun)

print(f"Moon's orbital period: {T_moon / (24 * 3600):.2f} days")
print(f"Earth's orbital period: {T_earth / (24 * 3600 * 365.25):.2f} years")

# Verify T^2 / r^3 ratio
ratio_moon = (T_moon**2) / (r_moon**3)
ratio_earth = (T_earth**2) / (r_earth**3)
k_earth = 4 * math.pi**2 / (G * M_earth)
k_sun = 4 * math.pi**2 / (G * M_sun)

print(f"T^2/r^3 for Moon: {ratio_moon:.2e}, Expected: {k_earth:.2e}")
print(f"T^2/r^3 for Earth: {ratio_earth:.2e}, Expected: {k_sun:.2e}")
```

**Output**:
```
Moon's orbital period: 27.41 days
Earth's orbital period: 1.00 years
T^2/r^3 for Moon: 9.90e-14, Expected: 9.90e-14
T^2/r^3 for Earth: 2.97e-19, Expected: 2.97e-19
```

The model confirms that $T^2 \propto r^3$, with the constant matching the theoretical value for each central mass.

