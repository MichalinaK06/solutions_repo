# Problem 1

[1.py](lol)

[lol](1.py)

Let’s dive into this exploration of the Central Limit Theorem (CLT) through simulations! I’ll provide a clear, step-by-step approach with Python code to simulate sampling distributions, visualize the results, and discuss the findings. Below is a Markdown document with embedded Python scripts that you can use or adapt as needed.

---

# Exploring the Central Limit Theorem through Simulations

The Central Limit Theorem (CLT) tells us that, under certain conditions, the distribution of sample means approximates a normal distribution as the sample size grows, regardless of the population’s original distribution. This simulation-based exploration will demonstrate this phenomenon using Python, focusing on three distinct population distributions: uniform, exponential, and binomial.

## 1. Simulating Sampling Distributions

We’ll generate large datasets for each population type and then simulate the sampling process to observe how sample means behave.

### Python Setup
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

### Population Distributions
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

## 2. Sampling and Visualization

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

### Observations
- **Uniform**: The sampling distribution starts flat but becomes bell-shaped as sample size increases.
- **Exponential**: Initially skewed, it approaches normality with larger samples.
- **Binomial**: Discrete steps smooth out into a normal curve as sample size grows.

## 3. Parameter Exploration

### Shape and Convergence
- **Uniform**: Lacks skewness, so convergence is rapid and symmetric.
- **Exponential**: High skewness delays normality, requiring larger samples (e.g., 30 or 50).
- **Binomial**: Moderate skewness; convergence depends on n and p symmetry (p = 0.5 is symmetric here).

### Variance Impact
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

## 4. Practical Applications

The CLT underpins many statistical methods:
- **Estimating Population Parameters**: Sample means estimate population means with known confidence intervals, assuming normality.
- **Quality Control**: Manufacturers use sample means to monitor product consistency, relying on CLT for small samples.
- **Financial Models**: Stock returns, often non-normal, are analyzed via sample means for predictions.

## Discussion

These simulations confirm the CLT: as sample size increases, sample mean distributions approach normality, regardless of the population’s shape. The rate of convergence varies—skewed distributions like exponential need larger samples. Variance impacts spread, aligning with the theoretical σ²/n. This hands-on approach bridges theory and practice, showing why the CLT is a statistical powerhouse.

---

### Running the Code
Copy the scripts into a Python environment with NumPy, Matplotlib, and Seaborn installed. Adjust parameters (e.g., `population_size`, `num_samples`) to explore further. The plots will visually demonstrate the CLT in action, making it a powerful learning tool!

