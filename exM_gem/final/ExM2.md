# Statistical Methods for Computer Science
## Exercise Battery 2 for intermediate test part 1

---
*Note: Choose the correct answer for each of the following questions.*

### Section 1: Descriptive Statistics

**1. If you are interested in comparing variation in sales for small and large stores selling similar goods, which of the following is the most appropriate measure of dispersion?**
- [ ] A) The range
- [ ] B) The interquartile range
- [ ] C) The standard deviation
- [ ] D) The coefficient of variation

**2. Suppose you are told that the mean of a sample is below the median. What does this information suggest about the distribution?**
- [ ] A) The distribution is symmetric.
- [ ] B) The distribution is skewed to the right (positively skewed).
- [ ] C) The distribution is skewed to the left (negatively skewed).
- [ ] D) There is insufficient information to determine the shape.

**3. Which of the following statements is true regarding correlation and covariance?**
- [ ] A) The correlation coefficient is always greater than the covariance.
- [ ] B) The covariance is always greater than the correlation coefficient.
- [ ] C) The covariance may be equal to the correlation coefficient.
- [ ] D) Neither the covariance nor the correlation coefficient can be equal to zero.

---

### Section 2: Probability Concepts

**4. When events have no common basic outcomes (their intersection is empty), they are said to be:**
- [ ] A) mutually exclusive.
- [ ] B) mutually related.
- [ ] C) mutually apart.
- [ ] D) collectively exhaustive.

**5. If the union of several events covers the entire sample space, it is said these events are:**
- [ ] A) mutually exclusive.
- [ ] B) mutually related.
- [ ] C) mutually apart.
- [ ] D) collectively exhaustive.

**6. The proportion of times that an event will occur, assuming that all outcomes in a sample space are equally likely to occur, is called:**
- [ ] A) objective probability.
- [ ] B) classical probability.
- [ ] C) relative frequency probability.
- [ ] D) subjective probability.

---

### Section 3: Discrete Random Variables

**7. A random variable which takes on no more than a countable number of values is called a(n):**
- [ ] A) continuous random variable.
- [ ] B) outcome.
- [ ] C) statistic.
- [ ] D) discrete random variable.

**8. Which of the following is true about a probability distribution?**
- [ ] A) The sum of all possible outcomes must not equal 1.
- [ ] B) The representation must be graphed, not tabular or algebraic.
- [ ] C) The probability of each outcome must be between 0 and 1, inclusive.
- [ ] D) The outcomes do not need to be mutually exclusive.

**9. The Poisson distribution can be used to approximate the binomial probabilities when the number of trials $n$ is large and at the same time the probability $p$ is:**
- [ ] A) also large.
- [ ] B) equal to 1.
- [ ] C) small.
- [ ] D) equal to $\lambda$.

---

### Section 4: Continuous Random Variables

**10. Because the probability of any specific value is 0 for a continuous random variable, the expected values for continuous random variables are computed using:**
- [ ] A) Bayes' Theorem.
- [ ] B) an empirical formula.
- [ ] C) a Venn diagram.
- [ ] D) integral calculus.

**11. We can convert any normal distribution to a distribution with a mean 0 and a variance 1. What is this distribution called?**
- [ ] A) Poisson distribution
- [ ] B) Marginal distribution
- [ ] C) Standard normal distribution
- [ ] D) Uniform continuous distribution

**12. The shape of the normal probability density function is a symmetric bell-shaped curve centered on the:**
- [ ] A) variance.
- [ ] B) standard deviation.
- [ ] C) correlation coefficient.
- [ ] D) mean.

<div style="page-break-after: always;"></div>

---

# Solutions / Svolgimento

### Section 1
**1.** **D) The coefficient of variation.** 
*Explanation*: When comparing variability across different scales or units (small vs large stores), the coefficient of variation ($CV = \sigma/\mu$) normalizes the dispersion, making it a fair comparison.

**2.** **C) The distribution is skewed to the left (negatively skewed).** 
*Explanation*: In a left-skewed distribution, the tail is on the left side, which "pulls" the arithmetic mean down below the median.

**3.** **C) The covariance may be equal to the correlation coefficient.**
*Explanation*: If both variables have a standard deviation of 1, their covariance equals their correlation coefficient. The other statements are absolutely false.

### Section 2
**4.** **A) Mutually exclusive.**
*Explanation*: Events without common outcomes cannot happen at the same time, fulfilling the definition of mutually exclusive sets.

**5.** **D) Collectively exhaustive.**
*Explanation*: "Collectively exhaustive" means that their union accounts for every possible outcome in the sample space.

**6.** **B) Classical probability.**
*Explanation*: The approach that assumes all basic outcomes are equally likely (e.g. flipping a fair coin or rolling a die) is the classical approach to probability.

### Section 3
**7.** **D) Discrete random variable.**
*Explanation*: A random variable is discrete if it takes a finite or countably infinite number of separated values.

**8.** **C) The probability of each outcome must be between 0 and 1, inclusive.**
*Explanation*: This satisfies the fundamental axiom of Probability (Kolmogorov's axioms): $0 \le P(x_i) \le 1$.

**9.** **C) small.**
*Explanation*: The Poisson approximation to the Binomial is used for rare events, where $n \to \infty$ and $p \to 0$, such that $n \cdot p = \lambda$.

### Section 4
**10.** **D) Integral calculus.**
*Explanation*: For continuous variables, sums $\Sigma$ from the discrete case become integrals $\int_{-\infty}^{\infty} x \cdot f(x) \, dx$.

**11.** **C) Standard normal distribution.**
*Explanation*: Applying the transformation $Z = \frac{X - \mu}{\sigma}$ forces the distribution to have $\mu=0$ and $\sigma^2=1$. This is the highly utilized Standard Normal.

**12.** **D) Mean.**
*Explanation*: The normal curve is perfectly symmetric around its expected value (mean), which is also equal to its median and its mode.
