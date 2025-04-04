import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set random seed for reproducibility
np.random.seed(42)

# Parameters
population_size = 10000  # Size of the population dataset
sample_sizes = [5, 10, 30, 50]  # Different sample sizes to test
num_samples = 1000  # Number of samples to draw for each size

# Generate populations
uniform_pop = np.random.uniform(0, 10, population_size)
exponential_pop = np.random.exponential(scale=1, size=population_size)
binomial_pop = np.random.binomial(n=10, p=0.5, size=population_size)

populations = {
    "Uniform": uniform_pop,
    "Exponential": exponential_pop,
    "Binomial": binomial_pop
}

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

# Calculate population variances
for dist_name, pop in populations.items():
    pop_variance = np.var(pop)
    print(f"{dist_name} Population Variance: {pop_variance:.2f}")
    for size in sample_sizes:
        theoretical_var = pop_variance / size
        sample_means = simulate_sampling(pop, [size], num_samples)
        empirical_var = np.var(sample_means[size])
        print(f"Sample Size {size}: Theoretical Var = {theoretical_var:.2f}, Empirical Var = {empirical_var:.2f}")    