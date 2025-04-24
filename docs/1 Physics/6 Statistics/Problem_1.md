# Problem 1


## Exploring the Central Limit Theorem through Simulations

The Central Limit Theorem (CLT) tells us that, under certain conditions, the distribution of sample means approximates a normal distribution as the sample size grows, regardless of the population’s original distribution. This simulation-based exploration will demonstrate this phenomenon using Python, focusing on three distinct population distributions: uniform, exponential, and binomial.

### 1. Simulating Sampling Distributions

We’ll generate large datasets for each population type and then simulate the sampling process to observe how sample means behave.

#### Python Setup
```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set random seed for reproducibility
np.random.seed(42)

# Parameters
population_size = 10000  # Size of the population dataset
sample_sizes = [5, 10, 30, 50]  # Different sample sizes to test
num_samples = 1000  # Number of samples to draw for each size
```

#### Population Distributions
- **Uniform Distribution**: Values evenly spread between 0 and 10.
- **Exponential Distribution**: Skewed with a rate parameter (λ = 1).
- **Binomial Distribution**: Discrete, with n = 10 trials and p = 0.5 success probability.

```python
# Generate populations
uniform_pop = np.random.uniform(0, 10, population_size)
exponential_pop = np.random.exponential(scale=1, size=population_size)
binomial_pop = np.random.binomial(n=10, p=0.5, size=population_size)

populations = {
    "Uniform": uniform_pop,
    "Exponential": exponential_pop,
    "Binomial": binomial_pop
}
```

### 2. Sampling and Visualization

For each population, we’ll draw random samples of varying sizes, compute the sample means, and plot their distributions.

```python
# Function to simulate sampling and return means
def simulate_sampling(population, sample_sizes, num_samples):
    sample_means = {size: [] for size in sample_sizes}
    for size in sample_sizes:
        for _ in range(num_samples):
            sample = np.random.choice(population, size=size, replace=True)
            sample_means[size].append(np.mean(sample))
    return sample_means

# Plotting function
def plot_sampling_distributions(sample_means, dist_name):
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes = axes.flatten()
    for i, size in enumerate(sample_sizes):
        sns.histplot(sample_means[size], bins=30, kde=True, ax=axes[i], color='skyblue')
        axes[i].set_title(f"Sample Size = {size}")
        axes[i].set_xlabel("Sample Mean")
        axes[i].set_ylabel("Frequency")
    plt.suptitle(f"Sampling Distribution of Means ({dist_name})", y=1.02)
    plt.tight_layout()
    plt.show()

# Run simulations and plot for each distribution
for dist_name, population in populations.items():
    sample_means = simulate_sampling(population, sample_sizes, num_samples)
    plot_sampling_distributions(sample_means, dist_name)
```

#### Observations
- **Uniform**: The sampling distribution starts flat but becomes bell-shaped as sample size increases.
- **Exponential**: Initially skewed, it approaches normality with larger samples.
- **Binomial**: Discrete steps smooth out into a normal curve as sample size grows.

### 3. Parameter Exploration

#### Shape and Convergence
- **Uniform**: Lacks skewness, so convergence is rapid and symmetric.
- **Exponential**: High skewness delays normality, requiring larger samples (e.g., 30 or 50).
- **Binomial**: Moderate skewness; convergence depends on n and p symmetry (p = 0.5 is symmetric here).

#### Variance Impact
The spread of the sampling distribution is tied to the population variance divided by the sample size (σ²/n). Let’s compute and compare:

```python
# Calculate population variances
for dist_name, pop in populations.items():
    pop_variance = np.var(pop)
    print(f"{dist_name} Population Variance: {pop_variance:.2f}")
    for size in sample_sizes:
        theoretical_var = pop_variance / size
        sample_means = simulate_sampling(pop, [size], num_samples)
        empirical_var = np.var(sample_means[size])
        print(f"Sample Size {size}: Theoretical Var = {theoretical_var:.2f}, Empirical Var = {empirical_var:.2f}")
```

- **Uniform**: High variance (≈ 8.33) leads to wider distributions at small sizes.
- **Exponential**: Variance = 1, so spread decreases predictably with n.
- **Binomial**: Variance (≈ 2.5) reflects binomial properties, narrowing with larger n.

### 4. Practical Applications

The CLT underpins many statistical methods:
- **Estimating Population Parameters**: Sample means estimate population means with known confidence intervals, assuming normality.
- **Quality Control**: Manufacturers use sample means to monitor product consistency, relying on CLT for small samples.
- **Financial Models**: Stock returns, often non-normal, are analyzed via sample means for predictions.

### Discussion

These simulations confirm the CLT: as sample size increases, sample mean distributions approach normality, regardless of the population’s shape. The rate of convergence varies—skewed distributions like exponential need larger samples. Variance impacts spread, aligning with the theoretical σ²/n. This hands-on approach bridges theory and practice, showing why the CLT is a statistical powerhouse.

---

#### Running the Code
Copy the scripts into a Python environment with NumPy, Matplotlib, and Seaborn installed. Adjust parameters (e.g., `population_size`, `num_samples`) to explore further. The plots will visually demonstrate the CLT in action, making it a powerful learning tool!




## **Exploring the Central Limit Theorem through Simulations**

### **Motivation**
The **Central Limit Theorem (CLT)** is one of the most fundamental concepts in statistics. It states that, regardless of the underlying population distribution, the **sampling distribution of the sample mean** will approximate a **normal distribution** as the sample size increases. This theorem underpins many statistical methods, including hypothesis testing, confidence intervals, and regression analysis.

#### **Why Simulate the CLT?**
- **Intuitive Understanding**: Visualizing how sample means converge to normality helps solidify theoretical knowledge.
- **Hands-on Learning**: Simulations allow experimentation with different distributions and sample sizes.
- **Real-World Applications**: The CLT is crucial in fields like **finance, quality control, and data science**, where we often rely on sample means to make inferences about populations.

---

### **Task: Simulating the CLT**

#### **1. Simulating Sampling Distributions**
We will examine three different population distributions:
1. **Uniform Distribution** (e.g., numbers between 0 and 1)
2. **Exponential Distribution** (e.g., λ = 1, highly skewed)
3. **Binomial Distribution** (e.g., n=10, p=0.5, discrete)

For each distribution:
- Generate a large population (e.g., 100,000 data points).
- Take **random samples** of different sizes (e.g., n = 5, 10, 30, 50).
- Compute the **sample mean** for each sample.
- Repeat this process many times (e.g., 10,000 iterations) to build the **sampling distribution of the mean**.

#### **2. Visualization**
For each distribution and sample size:
- Plot a **histogram** of the sample means.
- Overlay a **normal distribution curve** with the same mean and standard deviation.
- Observe how the sampling distribution becomes more **bell-shaped** as the sample size increases.

#### **3. Key Observations**
- **Effect of Sample Size**:  
  - Small samples (n=5) may not look normal, especially for skewed distributions.  
  - Larger samples (n=30+) tend to approximate normality, regardless of the original distribution.  
- **Effect of Population Variance**:  
  - Higher variance in the population leads to a wider sampling distribution.  
  - The **standard error** (SE = σ/√n) decreases as sample size increases.  

#### **4. Practical Applications**
The CLT enables:
- **Confidence Intervals**: Estimating population means from sample data.
- **Hypothesis Testing**: Using z-tests and t-tests even if the original data isn’t normal.
- **Quality Control**: Monitoring manufacturing processes using sample averages.
- **Financial Modeling**: Predicting stock returns based on historical averages.

---

### **Deliverables**
1. **Markdown Report** (like this one) explaining the CLT and simulation results.
2. **Interactive Python/JavaScript Simulation** (code provided below).
3. **Plots** showing:
   - Original population distributions.
   - Sampling distributions for different sample sizes.
   - Convergence to normality as sample size increases.

---





### **Key Findings**
1. **Uniform Distribution** → Sampling distribution becomes normal quickly (even at n=5).
2. **Exponential Distribution** → Needs larger n (≥30) to approximate normality due to skewness.
3. **Binomial Distribution** → Discrete nature is smoothed out as n increases.

### **Conclusion**
This simulation demonstrates the **power of the CLT**—even with non-normal data, the sample mean's distribution converges to normality. This justifies many statistical techniques used in real-world data analysis.  

**Try experimenting with:**
- Different sample sizes (n=5 vs. n=50).
- Other distributions (e.g., Poisson, Pareto).
- The impact of population skewness on convergence rate.  

Would you like any modifications or additional features? 🚀
