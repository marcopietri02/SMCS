# Statistical Methods for Computer Science
## Exercise Battery 5 for intermediate test part 1

---

### Exercise 1: The "Reverse" Normal Distribution (System of Equations)
The number of viewers ordering a particular pay-per-view program is normally distributed. You are given the following historical data:
- **20%** of the time, fewer than 20,000 people order the program.
- **10%** of the time, more than 28,000 people order the program.

**(a)** Using the Standard Normal probability tables, find the two $Z$-scores corresponding to these given critical percentiles.
**(b)** Construct a system of linear equations to solve for the completely unknown mean ($\mu$) and standard deviation ($\sigma$) of the distribution.

**Answers:**
(a) $Z_1$ (lower tail): [       ], $Z_2$ (upper tail): [       ] / 2
(b) Mean $\mu$: [                   ], StdDev $\sigma$: [                   ] / 4

---

### Exercise 2: Summing Independent Normal Variables (Aggregate Variation)
Sales at a local plumbing wholesaler consist of both over-the-counter sales ($X$) as well as deliveries ($Y$). During the course of a month:
- Over-the-counter sales have an expected value of $\mu_X = \$102,000$ with a standard deviation of $\sigma_X = \$13,500$.
- Deliveries average $\mu_Y = \$242,000$ with a standard deviation of $\sigma_Y = \$25,000$.

Assuming that the over-the-counter sales are strictly statistically independent of deliveries, define the Total Aggregate Sales as $W = X + Y$.

**(a)** Calculate the expected value (mean) $E[W]$ and the exact variance $V[W]$ of the Total Aggregate Sales.
**(b)** What is the standard deviation $\sigma_W$ of the Total Aggregate Sales? *(Hint: Be very careful about what you are allowed to add together).*

**Answers:**
(a) $E[W]$: [                   ], $V[W]$: [                   ] / 3
(b) $\sigma_W$: [                   ] / 2

<div style="page-break-after: always;"></div>

---

# Solutions / Svolgimento

### Exercise 1
**Premise:** Let $X \sim N(\mu, \sigma^2)$ be the number of viewers. We know:
1) $P(X < 20,000) = 0.20$
2) $P(X > 28,000) = 0.10$  *(which implies $P(X < 28,000) = 0.90$)*

**(a) Finding Z-scores:**
From a standard normal table ($\Phi(z)$):
- The $Z$-score that leaves $20\%$ ($0.20$) area to the left is approximately **$Z_1 = -0.84$**.
- The $Z$-score that leaves $90\%$ ($0.90$) area to the left is approximately **$Z_2 = 1.28$**.

**(b) Solving the System:**
We use the standardization formula $X = \mu + Z\sigma$.
1) $20000 = \mu - 0.84\sigma$
2) $28000 = \mu + 1.28\sigma$

Let's subtract equation (1) from equation (2) to eliminate $\mu$:
$28000 - 20000 = (\mu - \mu) + (1.28\sigma - (-0.84\sigma))$
$8000 = 2.12\sigma$
$\sigma = \frac{8000}{2.12} \approx \textbf{3773.58}$.

Now, substitute $\sigma$ back into equation (1):
$\mu = 20000 + 0.84(3773.58)$
$\mu = 20000 + 3169.81 = \textbf{23169.81}$.

*Conclusion:* The mean viewership is $\approx 23,170$ with a standard deviation of $\approx 3,774$.

---

### Exercise 2
**Premise:** $X$ and $Y$ are independent random variables.
$\mu_X = 102000$, $\sigma_X = 13500$.
$\mu_Y = 242000$, $\sigma_Y = 25000$.
$W = X + Y$.

**(a) Expected Value and Variance:**
By the linearity of expectation:
$E[W] = E[X] + E[Y] = 102000 + 242000 = \textbf{344,000}$.

For variance, since the variables are *independent*, their covariance is zero. Thus, the variance of the sum is exactly the sum of the variances: $V[W] = V[X] + V[Y]$.
*Warning: We must first square the standard deviations!*
$V[X] = (13500)^2 = 182,250,000$
$V[Y] = (25000)^2 = 625,000,000$
$V[W] = 182,250,000 + 625,000,000 = \textbf{807,250,000}$.

**(b) Aggregate Standard Deviation:**
To find the combined standard deviation, we take the square root of the combined variance:
$\sigma_W = \sqrt{V[W]} = \sqrt{807,250,000} \approx \textbf{28,412.15}$.

*(Note: Notice how taking the square root of the sum of squares is VERY different from just summing the standard deviations. $13500 + 25000 = 38500$. If you answered $38,500$, you committed one of the most classic errors in statistics!)*
