# Problem 1
Let’s dive into analyzing interference patterns on a water surface caused by point sources at the vertices of a regular polygon. I’ll walk through the steps systematically, keeping it engaging and clear, and I’ll choose a square as the polygon for concreteness—though the approach generalizes to any regular polygon. We’ll derive the equations, apply superposition, analyze the patterns, and discuss visualization.

### Step 1: Select a Regular Polygon
I’ll pick a square because it’s simple yet rich enough to show interesting interference. Imagine a square centered at the origin (0,0) with side length \(2d\), so the vertices (our wave sources) are at:
- \(S_1 = (d, d)\)
- \(S_2 = (d, -d)\)
- \(S_3 = (-d, -d)\)
- \(S_4 = (-d, d)\)

These points are symmetrically placed, which should lead to some neat symmetry in the patterns.

### Step 2: Position the Sources
The sources are at the four corners of the square, as listed above. Each emits a circular wave that spreads outward, and we’ll assume they’re all in sync—same amplitude \(A\), wavelength \(\lambda\), frequency \(f\), and initial phase \(\phi = 0\) for simplicity (coherent sources).

### Step 3: Wave Equations
The wave from a single source at \((x_i, y_i)\) is given by:
\[
\eta_i(x, y, t) = \frac{A}{\sqrt{r_i}} \cos(kr_i - \omega t + \phi)
\]
where:
- \(r_i = \sqrt{(x - x_i)^2 + (y - y_i)^2}\) is the distance from source \(i\) to point \((x, y)\),
- \(k = \frac{2\pi}{\lambda}\) (wave number),
- \(\omega = 2\pi f\) (angular frequency),
- \(\phi = 0\) (since sources are coherent with no phase offset),
- The \(\frac{1}{\sqrt{r_i}}\) term accounts for amplitude decreasing with distance due to energy spreading in 2D.

For our four sources:
1. \(S_1 = (d, d)\): 
   \[
   r_1 = \sqrt{(x - d)^2 + (y - d)^2}, \quad \eta_1 = \frac{A}{\sqrt{r_1}} \cos(kr_1 - \omega t)
   \]
2. \(S_2 = (d, -d)\): 
   \[
   r_2 = \sqrt{(x - d)^2 + (y + d)^2}, \quad \eta_2 = \frac{A}{\sqrt{r_2}} \cos(kr_2 - \omega t)
   \]
3. \(S_3 = (-d, -d)\): 
   \[
   r_3 = \sqrt{(x + d)^2 + (y + d)^2}, \quad \eta_3 = \frac{A}{\sqrt{r_3}} \cos(kr_3 - \omega t)
   \]
4. \(S_4 = (-d, d)\): 
   \[
   r_4 = \sqrt{(x + d)^2 + (y - d)^2}, \quad \eta_4 = \frac{A}{\sqrt{r_4}} \cos(kr_4 - \omega t)
   \]

### Step 4: Superposition of Waves
The total displacement at any point \((x, y)\) and time \(t\) is the sum of contributions from all four sources:
\[
\eta_{\text{sum}}(x, y, t) = \eta_1 + \eta_2 + \eta_3 + \eta_4
\]
\[
\eta_{\text{sum}}(x, y, t) = \sum_{i=1}^4 \frac{A}{\sqrt{r_i}} \cos(kr_i - \omega t)
\]
Since \(\omega t\) is the same for all terms (coherent sources), this oscillates in time, but the spatial pattern depends on the \(r_i\)’s, which vary with position.

### Step 5: Analyze Interference Patterns
To understand the patterns, let’s consider the spatial part at a fixed time, say \(t = 0\):
\[
\eta_{\text{sum}}(x, y, 0) = A \sum_{i=1}^4 \frac{1}{\sqrt{r_i}} \cos(kr_i)
\]
- **Constructive Interference**: Occurs when the \(\cos(kr_i)\) terms are in phase (i.e., \(kr_i\) values differ by multiples of \(2\pi\)), and the amplitudes add up. This happens when the distances \(r_i\) from multiple sources to a point are such that \(k(r_i - r_j) = 2\pi m\) (where \(m\) is an integer).
- **Destructive Interference**: Occurs when phases cancel, e.g., \(k(r_i - r_j) = (2m + 1)\pi\), making \(\cos(kr_i)\) terms oppose each other.

**Symmetry Insight**: Due to the square’s symmetry:
- At the center \((0, 0)\), \(r_1 = r_2 = r_3 = r_4 = \sqrt{2}d\). So:
  \[
  \eta_{\text{sum}}(0, 0, 0) = 4 \cdot \frac{A}{\sqrt{\sqrt{2}d}} \cos(k\sqrt{2}d)
  \]
  This is maximized when \(k\sqrt{2}d = 2\pi m\), showing strong constructive interference if the wavelength fits the geometry.
- Along the x-axis (\(y = 0\)), distances vary: \(r_1 = r_2 = \sqrt{(x - d)^2 + d^2}\), \(r_3 = r_4 = \sqrt{(x + d)^2 + d^2}\). The pattern oscillates as \(x\) changes.

The interference creates a grid-like pattern with peaks and troughs, more complex than the two-source case (which gives straight fringes).

### Step 6: Visualization
To visualize this, imagine a 2D heatmap of \(\eta_{\text{sum}}(x, y, 0)\) over a grid, say \(-3d \leq x, y \leq 3d\). The pattern would show:
- Bright spots (high amplitude) at points of constructive interference.
- Dark spots (low amplitude) where waves cancel.

Using Python with Matplotlib, you could code this:
```python
import numpy as np
import matplotlib.pyplot as plt

# Constants
A = 1.0  # amplitude
d = 1.0  # half-side length
lambda_ = 0.5  # wavelength
k = 2 * np.pi / lambda_

# Grid
x = np.linspace(-3, 3, 200)
y = np.linspace(-3, 3, 200)
X, Y = np.meshgrid(x, y)

# Distances from each source
r1 = np.sqrt((X - d)**2 + (Y - d)**2)
r2 = np.sqrt((X - d)**2 + (Y + d)**2)
r3 = np.sqrt((X + d)**2 + (Y + d)**2)
r4 = np.sqrt((X + d)**2 + (Y - d)**2)

# Wave contributions (at t=0)
eta = (A/np.sqrt(r1)) * np.cos(k * r1) + \
      (A/np.sqrt(r2)) * np.cos(k * r2) + \
      (A/np.sqrt(r3)) * np.cos(k * r3) + \
      (A/np.sqrt(r4)) * np.cos(k * r4)

# Plot
plt.imshow(eta, extent=[-3, 3, -3, 3], cmap='seismic')
plt.colorbar(label='Displacement')
plt.title('Interference Pattern from Square Sources')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
```
This would reveal a symmetrical, oscillating pattern with peaks along diagonals and axes, modulated by the \(1/\sqrt{r}\) decay.

### Final Thoughts
The square setup produces a rich, crisscrossing pattern due to four sources. Constructive peaks form where waves align, like at the center or along symmetry lines, while destructive zones appear where phases mismatch. Exploring other polygons (e.g., a triangle or pentagon) would tweak the symmetry and complexity—fewer sources simplify, more sources elaborate. It’s a fantastic way to see wave physics in action, blending math with visual intuition!

