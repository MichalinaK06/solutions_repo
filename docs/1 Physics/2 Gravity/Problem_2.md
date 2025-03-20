# Problem 2

### Definitions and Physical Meaning

1. **First Cosmic Velocity (Orbital Velocity)**  
   This is the minimum speed an object must achieve to enter a stable circular orbit around a celestial body, just above its surface (ignoring atmospheric drag for simplicity). Physically, it’s the speed where the centrifugal force balances the gravitational pull, keeping the object in orbit without escaping or falling back.

2. **Second Cosmic Velocity (Escape Velocity)**  
   This is the speed required to completely escape a celestial body’s gravitational influence, starting from its surface, and travel to infinity with zero residual speed. It’s the threshold for breaking free—no orbit, just departure into space.

3. **Third Cosmic Velocity**  
   This is the speed needed to escape the gravitational pull of a star system (e.g., the Sun) from a specific point within it, such as a planet’s surface, and venture into interstellar space. It builds on the second cosmic velocity by accounting for the star’s gravity over vast distances.

### Mathematical Derivations

#### First Cosmic Velocity (v_1)

For a circular orbit, the gravitational force provides the centripetal force:

$F_g = F_c$

$$\frac{G M m}{r^2} = \frac{m v_1^2}{r}$$

Cancel $m$ (mass of the orbiting object) and simplify:

$$v_1^2 = \frac{G M}{r}$$

$$v_1 = \sqrt{\frac{G M}{r}}$$

Where:
- $G$: Gravitational constant ($6.67430 \times 10^{-11} \, \text{m}^3 \text{kg}^{-1} \text{s}^{-2}$)

- $M$: Mass of the celestial body

- $r$: Radius of the body (assuming orbit near the surface)

#### Second Cosmic Velocity (v_2)

Escape velocity comes from energy conservation. The total mechanical energy at the surface (kinetic + potential) equals zero at infinity (where potential energy is zero, and residual speed is zero):

$$\frac{1}{2} m v_2^2 - \frac{G M m}{r} = 0$$

$$\frac{1}{2} v_2^2 = \frac{G M}{r}$$

$$v_2^2 = \frac{2 G M}{r}$$

$$v_2 = \sqrt{\frac{2 G M}{r}}$$

Notice: $v_2 = v_1 \sqrt{2}$, so escape velocity is $\sqrt{2}$ times the orbital velocity.

#### Third Cosmic Velocity (v_3)

This is more complex, as it involves escaping the Sun’s gravity from a planet’s orbit. It’s the velocity needed at a planet’s surface to reach the Sun’s escape velocity at the planet’s distance ($R$) from the Sun. 

First, the escape speed from the Sun’s gravity at distance $R$:

$$v_{\text{esc,Sun}} = \sqrt{\frac{2 G M_{\text{Sun}}}{R}}$$

The planet orbits the Sun at speed:

$$v_{\text{orbit}} = \sqrt{\frac{G M_{\text{Sun}}}{R}}$$

The additional speed ($v_{\infty}$) needed to escape the Sun’s gravity, added to the orbital speed, is:

$$v_{\infty} = v_{\text{esc,Sun}} - v_{\text{orbit}} = \sqrt{\frac{2 G M_{\text{Sun}}}{R}} - \sqrt{\frac{G M_{\text{Sun}}}{R}}$$

From the planet’s surface, $v_3$ combines escaping the planet ($v_2$) and achieving $v_{\infty}$ relative to the Sun.

Approximations vary, but a simplified form (assuming a hyperbolic 
trajectory) is:

$$v_3 \approx \sqrt{v_2^2 + v_{\infty}^2}$$

### Parameters Affecting Velocities
- **Mass (M)**: Higher mass increases gravitational pull, raising all velocities.

- **Radius (r)**: Larger radius decreases velocities by increasing distance from the center of mass.

- **Distance from Star (R)**: For $v_3$, a greater orbital radius reduces the Sun’s influence, lowering the required speed.

### Calculations for Earth, Mars, and Jupiter

#### Data
- **Earth**: $M = 5.972 \times 10^{24} \, \text{kg}$, $r = 6,371 \, \text{km}$, $R = 1 \, \text{AU} = 1.496 \times 10^8 \, \text{km}$

- **Mars**: $M = 6.417 \times 10^{23} \, \text{kg}$, $r = 3,390 \, \text{km}$, $R = 1.524 \, \text{AU}$

- **Jupiter**: $M = 1.899 \times 10^{27} \, \text{kg}$, $r = 69,911 \, \text{km}$, $R = 5.203 \, \text{AU}$

- **Sun**: $M_{\text{Sun}} = 1.989 \times 10^{30} \, \text{kg}$

#### Earth

- $$v_1 = \sqrt{\frac{6.67430 \times 10^{-11} \cdot 5.972 \times 10^{24}}{6.371 \times 10^6}} = 7.91 \, \text{km/s}$$
- $$v_2 = \sqrt{2} \cdot 7.91 = 11.19 \, \text{km/s}$$
- $$v_{\text{esc,Sun}} = \sqrt{\frac{2 \cdot 6.67430 \times 10^{-11} \cdot 1.989 \times 10^{30}}{1.496 \times 10^{11}}} = 42.1 \, \text{km/s}$$
- $v_{\text{orbit}} = 29.8 \, \text{km/s}$
- $v_{\infty} = 42.1 - 29.8 = 12.3 \, \text{km/s}$
- $v_3 \approx \sqrt{11.19^2 + 12.3^2} = 16.7 \, \text{km/s}$

#### Mars
- $v_1 = \sqrt{\frac{6.67430 \times 10^{-11} \cdot 6.417 \times 10^{23}}{3.39 \times 10^6}} = 3.55 \, \text{km/s}$
- $v_2 = \sqrt{2} \cdot 3.55 = 5.02 \, \text{km/s}$
- $v_{\text{esc,Sun}} = \sqrt{\frac{2 \cdot 6.67430 \times 10^{-11} \cdot 1.989 \times 10^{30}}{1.524 \cdot 1.496 \times 10^{11}}} = 34.1 \, \text{km/s}$
- $v_{\text{orbit}} = 24.1 \, \text{km/s}$
- $v_{\infty} = 34.1 - 24.1 = 10.0 \, \text{km/s}$
- $v_3 \approx \sqrt{5.02^2 + 10.0^2} = 11.2 \, \text{km/s}$

#### Jupiter
- $v_1 = \sqrt{\frac{6.67430 \times 10^{-11} \cdot 1.899 \times 10^{27}}{6.9911 \times 10^7}} = 42.6 \, \text{km/s}$
- $v_2 = \sqrt{2} \cdot 42.6 = 60.2 \, \text{km/s}$
- $v_{\text{esc,Sun}} = \sqrt{\frac{2 \cdot 6.67430 \times 10^{-11} \cdot 1.989 \times 10^{30}}{5.203 \cdot 1.496 \times 10^{11}}} = 18.5 \, \text{km/s}$
- $v_{\text{orbit}} = 13.1 \, \text{km/s}$
- $v_{\infty} = 18.5 - 13.1 = 5.4 \, \text{km/s}$
- $v_3 \approx \sqrt{60.2^2 + 5.4^2} = 60.4 \, \text{km/s}$

### Visualization
[Escape and Cosmic Velocities](velocity.html)

### Importance in Space Exploration

1. **First Cosmic Velocity (Orbiting)**  
   - **Satellites**: Rockets must reach $v_1$ (plus extra to counter drag) to place satellites in orbit. For Earth, $7.91$ km/s is the baseline—real launches hit $~9$ km/s due to atmosphere.  
   - **Mars**: Lower $v_1$ ($3.55$ km/s) makes orbiting easier, aiding missions like Mars Reconnaissance Orbiter.

2. **Second Cosmic Velocity (Escaping)**  
   - **Planetary Missions**: To send probes to Mars or beyond, we exceed Earth’s $v_2$ ($11.19$ km/s). Apollo missions used this to reach the Moon (not escaping Earth fully, but leveraging orbits).  
   - **Jupiter**: Its high $v_2$ ($60.2$ km/s) makes escaping its gravity a monumental challenge—hence why probes like Juno orbit rather than land and depart.

3. **Third Cosmic Velocity (Interstellar)**  
   - **Voyager Probes**: Launched from Earth, they used gravitational assists to approach $v_3$, escaping the Sun’s grasp (effective speed $~17$ km/s relative to the Sun).  
   - **Future Travel**: Interstellar missions need $v_3$ or beyond, likely requiring advanced propulsion (e.g., nuclear or solar sails).

These velocities shape mission design—rockets must pack enough energy (via chemical or future propulsion) to hit these thresholds, often using gravity assists to bridge gaps. For interstellar dreams, $v_3$ is just the start; relativistic speeds await beyond.





---

