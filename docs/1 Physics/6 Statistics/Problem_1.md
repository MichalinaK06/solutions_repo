# Problem 1

## Exploring the Central Limit Theorem (CLT) through Simulations

The **Central Limit Theorem (CLT)** is a foundational concept in statistics. It states that the sampling distribution of the sample mean will approximate a **normal distribution** as the sample size increases, regardless of the shape of the original population distribution. This principle is crucial to many statistical methods such as hypothesis testing, confidence intervals, and regression analysis.

In this exercise, we'll explore the CLT through Python simulations using three different population distributions:

[Simulation Link](e.html)

### Population Distributions

- **Uniform Distribution**: Evenly spread values between 0 and 10.

- **Exponential Distribution**: Positively skewed with a rate parameter λ = 1.

- **Binomial Distribution**: Discrete values from 10 trials with a success probability p = 0.5.

---

## 3. Parameter Exploration

### Shape and Convergence

- **Uniform Distribution**: Since it’s symmetric and unskewed, it converges quickly to a normal distribution.

- **Exponential Distribution**: Its skewed nature causes slower convergence. A larger sample size (e.g., n = 30 or 50) is needed to approximate normality.

- **Binomial Distribution**: The shape depends on p. With p = 0.5, it’s symmetric and converges reasonably fast; with more extreme p values, convergence slows.

---

## 4. Key Observations

- **Sample Size Matters**:

  - Small samples (e.g., n = 5) may not exhibit normality, especially for skewed distributions.

  - As sample size increases (n ≥ 30), the sampling distribution begins to resemble a normal distribution.
  
- **Population Variance Effects**:

  - Greater variance in the population leads to wider sampling distributions.

  - The **standard error (SE)** decreases with larger sample sizes, as SE = σ / √n.

---

## Practical Applications of CLT

The Central Limit Theorem enables various real-world applications:

- **Estimating Population Parameters**: Sample means can estimate population means with calculable confidence intervals.

- **Hypothesis Testing**: Allows use of z-tests and t-tests, even when the original population distribution isn’t normal.

- **Quality Control**: Used in manufacturing to assess product consistency using small samples.

- **Financial Modeling**: Supports analysis of stock returns and other financial data, even when they aren't normally distributed.

