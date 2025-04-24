# Problem 1

## **Measuring Earth's Gravitational Acceleration (g) with a Pendulum**

### **Motivation**

The acceleration due to gravity (**g**) is a fundamental physical constant that affects everything from falling objects to planetary motion. Measuring **g** accurately helps in:

- Validating physical laws (Newtonian mechanics).

- Engineering applications (structural design, vehicle dynamics).

- Geophysical surveys (measuring Earth's density variations).

A **simple pendulum** provides an accessible way to estimate **g** by relating its oscillation period (**T**) to the pendulum length (**L**).



#### **4. Calculations**

##### **a) Mean Period (T) and Uncertainty (ΔT)**

$$
\overline{T}_{10} = \text{Average of all } T_{10} \text{ measurements}
$$

$$
\sigma_T = \text{Standard deviation of } T_{10}
$$

$$
\Delta T_{10} = \frac{\sigma_T}{\sqrt{10}} \quad \text{(Uncertainty in mean)}
$$

$$
T = \frac{\overline{T}_{10}}{10}, \quad \Delta T = \frac{\Delta T_{10}}{10}
$$

##### **b) Calculating g**

$$
g = \frac{4\pi^2 L}{T^2}
$$

##### **c) Uncertainty in g (Δg)**

$$
\Delta g = g \sqrt{ \left( \frac{\Delta L}{L} \right)^2 + \left( 2 \frac{\Delta T}{T} \right)^2 }
$$

---

### **Data Table**

| Trial | Time for 10 Oscillations, T₁₀ (s) | 
|-------|----------------------------------|
| 1     | 14.12                            | 
| 2     | 14.08                            | 
| 3     | 14.11                            |
| 4     | 14.09                            | 
| 5     | 14.10                            | 
| 6     | 14.13                            | 
| 7     | 14.07                            | 
| 8     | 14.10                            | 
| 9     | 14.12                            | 
| 10    | 14.10                            |

**Calculations:** 

### **1. Pendulum Length Measurement**

- Measured length (L) = 1.000 m

- Ruler resolution = 1 mm = 0.001 m

- Uncertainty in length (ΔL) = ½ × resolution = 0.0005 m


### **2. Period Calculation**

**a) Mean time for 10 oscillations (T₁₀):**

$$
\overline{T}_{10} = \frac{\sum{T_{10}}}{n} = \frac{141.0}{10} = 14.10\,s
$$

**b) Standard deviation (σ):**

$$
\sigma = \sqrt{\frac{\sum{(T_{10} - \overline{T}_{10})^2}}{n}} = \sqrt{\frac{0.0032}{10}} = 0.05\,s
$$

**c) Uncertainty in mean time (ΔT₁₀):**

$$
\Delta T_{10} = \frac{\sigma}{\sqrt{n}} = \frac{0.05}{\sqrt{10}} = 0.016\,s
$$

**d) Single period (T) and its uncertainty (ΔT):**

$$
T = \frac{\overline{T}_{10}}{10} = 1.410\,s
$$

$$
\Delta T = \frac{\Delta T_{10}}{10} = 0.0016\,s
$$


### **3. Calculating g**

**Main equation:**

$$
g = \frac{4\pi^2 (1.000)}{(1.410)^2} = \frac{39.478}{1.988} = 9.85\,m/s^2
$$

### **4. Uncertainty in g (Δg)**

$$
\Delta g = 9.85 \sqrt{ \left( \frac{0.0005}{1.000} \right)^2 + \left( 2 \frac{0.0016}{1.410} \right)^2 }
$$

$$
\Delta g = 9.85 \sqrt{0.00000025 + 0.00000515} = 9.85 \times 0.0023 = 0.05\,m/s^2
$$



---

### **Analysis**

#### **1. Comparison with Standard Value**

- Measured: $9.85 \pm 0.05 \, \text{m/s}^2$  

- Expected: $9.81 \, \text{m/s}^2$  

- **Error:** ~0.4% (within uncertainty).

#### **2. Sources of Uncertainty**

- **Length Measurement (ΔL):** 

  - Ruler resolution limits precision.  

  - Minimized using a digital caliper.  
  
- **Timing Errors (ΔT):**  

  - Human reaction time (~0.2 s) affects short oscillations.  

  - Reduced by measuring **10 oscillations** and averaging.  

- **Air Resistance & Angle (>15°):**  

  - Introduces non-ideal simple harmonic motion.  

#### **3. Experimental Limitations**

- Assumes massless string and point-mass bob (not strictly true).

- Friction at pivot slightly dampens motion.  

---

### **Improving Accuracy**

✔ Use **longer pendulums** (reduces % error in **L**).  

✔ Measure **50 oscillations** (reduces timing errors). 
 
✔ Use a **photogate sensor** (eliminates human reaction time).  

