# Statistical Methods for Computer Science
## Exercise Battery 1 for intermediate test part 1

---

### Exercise 1: Descriptive Statistics (Grouped Data & Boxplot)
The duration $X$ (in months) for a shipment of car tyres used on a population of 900 cars is characterized by the following distribution:

| Duration (months) | $(0 - 20]$ | $(20 - 40]$ | $(40 - 60]$ | $(60 - 80]$ |
| :--- | :---: | :---: | :---: | :---: |
| **Freq.** | 200 | 250 | 350 | 100 |

Assuming equi-distribution within the classes:
**(a)** Calculate the mean duration.
**(b)** Calculate the median duration.
**(c)** Calculate the standard deviation of the duration.
**(d)** *[Enhanced]* A new batch of tyres is tested, giving a mean of 50 and a variance of 225. Calculate the coefficient of variation (CV) for both batches. Which one exhibits a higher relative variability?

**Answers:**
(a) [                   ] / 1
(b) [                   ] / 2
(c) [                   ] / 2
(d) [                   ] / 2

---

### Exercise 2: Probability and Bayes' Theorem *[Blind Spot!]*
A tech company uses three different servers to host its web service: Server A handles 40% of the traffic, Server B handles 35%, and Server C handles 25%. The probability that a request fails depending on the server is: 1% for Server A, 2% for Server B, and 4% for Server C.
**(a)** What is the overall probability that a random user request fails?
**(b)** If a request has failed, what is the probability that it was handled by Server C?

**Answers:**
(a) [                   ] / 2
(b) [                   ] / 3

---

### Exercise 3: Joint Probability & Discrete Variables
The following table displays the joint probability distribution of two discrete random variables $X$ and $Y$.

| $X \setminus Y$ | 1 | 2 | 3 |
| :---: | :---: | :---: | :---: |
| **0** | 0.1 | 0.2 | 0.1 |
| **1** | 0.2 | 0.3 | 0.1 |

**(a)** Find the expected value of $Y$, $E[Y]$.
**(b)** Find $P(X = 1 \mid Y \ge 2)$.
**(c)** *[Enhanced]* Are $X$ and $Y$ independent? Justify your answer.
**(d)** *[Enhanced]* Calculate the Covariance $Cov(X, Y)$.

**Answers:**
(a) [                   ] / 2
(b) [                   ] / 3
(c) [                   ] / 2
(d) [                   ] / 2

---

### Exercise 4: Continuous Random Variables (Normal Distribution) *[Blind Spot!]*
The time $T$ required to compile a large software module is normally distributed with a mean $\mu = 45$ seconds and a standard deviation $\sigma = 8$ seconds.
**(a)** Find the probability that a compilation takes more than 50 seconds.
**(b)** Find the 90th percentile of the compilation time (the time under which 90% of compilations finish).

*(Note: Use standard normal tables for $\Phi(z)$ values).*

**Answers:**
(a) [                   ] / 2
(b) [                   ] / 3

---

### Exercise 5: Poisson & Binomial
The number of server crashes per month in a data center is a Poisson random variable with an expected value equal to 1.5.
**(a)** Find the probability of having exactly zero crashes in a single month.
**(b)** Find the probability of having at least two crashes in a single month.
**(c)** Consider the number of crashes in different months as independent and identically distributed random variables. Find the probability that in the next 4 months, there are exactly 2 months with at least two crashes.

**Answers:**
(a) [                   ] / 1
(b) [                   ] / 2
(c) [                   ] / 3

---
## Appendix: Parametric Families

**Discrete Random Variables:**
*   $X \sim \text{Bernoulli}(p)$ $\Rightarrow E[X]=p, V[X]=p(1-p)$
*   $X \sim \text{Binomial}(n,p)$ $\Rightarrow E[X]=np, V[X]=np(1-p)$
*   $X \sim \text{Poisson}(\lambda)$ $\Rightarrow p_X(x) = \frac{e^{-\lambda}\lambda^x}{x!}, E[X]=\lambda, V[X]=\lambda$

**Continuous Random Variables:**
*   $X \sim \text{Normal}(\mu, \sigma^2)$ $\Rightarrow f_X(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left\{-\frac{1}{2\sigma^2}(x-\mu)^2\right\}$

<div style="page-break-after: always;"></div>

---

# Solutions / Svolgimento

### Exercise 1
**Premise**: Let $x_i$ be the class midpoints: 10, 30, 50, 70. Total count $N = 900$.
**(a) Mean**: 
$\mu \approx \frac{\sum x_i \cdot f_i}{N} = \frac{10(200) + 30(250) + 50(350) + 70(100)}{900} = \frac{34000}{900} = 37.78$ months.
**(b) Median**: 
The total frequency is 900, the median position is $450$. Cumulative frequencies are: 200, 450, 800, 900.
Since $N/2 = 450$ exactly falls at the upper boundary of the second class $(20-40]$, the median is exactly **40**. 
**(c) Standard Deviation**: 
$\text{Var}(X) \approx \frac{\sum x_i^2 \cdot f_i}{N} - \mu^2 = \frac{10^2(200) + 30^2(250) + 50^2(350) + 70^2(100)}{900} - 37.78^2$
$\text{Var}(X) = \frac{1610000}{900} - 1427.33 = 1788.89 - 1427.33 = 361.56$.
$\sigma = \sqrt{361.56} \approx 19.01$ months.
**(d) Coefficient of Variation**:
Original Batch: $CV_1 = \frac{\sigma}{\mu} = \frac{19.01}{37.78} \approx 0.503 \text{ (50.3\%)}$.
New Batch: $CV_2 = \frac{\sqrt{225}}{50} = \frac{15}{50} = 0.300 \text{ (30.0\%)}$.
The original batch exhibits a higher relative variability.

### Exercise 2
**(a) Total Probability**:
$P(\text{Fail}) = P(\text{Fail} \mid A)P(A) + P(\text{Fail} \mid B)P(B) + P(\text{Fail} \mid C)P(C)$
$P(\text{Fail}) = (0.01)(0.40) + (0.02)(0.35) + (0.04)(0.25) = 0.004 + 0.007 + 0.010 = 0.021 \text{ (2.1\%)}$.
**(b) Bayes' Theorem**:
$P(C \mid \text{Fail}) = \frac{P(\text{Fail} \mid C)P(C)}{P(\text{Fail})} = \frac{0.010}{0.021} = \frac{10}{21} \approx 0.476 \text{ (47.6\%)}$.

### Exercise 3
Marginal distributions: $P(X=0)=0.4$, $P(X=1)=0.6$. $P(Y=1)=0.3$, $P(Y=2)=0.5$, $P(Y=3)=0.2$.
**(a) Expected value of Y**: 
$E[Y] = 1(0.3) + 2(0.5) + 3(0.2) = 0.3 + 1.0 + 0.6 = 1.9$.
**(b) Conditional probability**:
$P(Y \ge 2) = 0.5 + 0.2 = 0.7$.
$P(X=1 \cap Y \ge 2) = P(X=1, Y=2) + P(X=1, Y=3) = 0.3 + 0.1 = 0.4$.
$P(X=1 \mid Y \ge 2) = \frac{0.4}{0.7} = \frac{4}{7} \approx 0.571$.
**(c) Independence**: 
Requires $P(X=x, Y=y) = P(X=x)P(Y=y)$ for all combinations.
Let's check $X=0, Y=1$: $P(X=0)P(Y=1) = (0.4)(0.3) = 0.12$. 
But from the table $P(X=0, Y=1) = 0.1$. Since $0.1 \neq 0.12$, they are **Not Independent**.
**(d) Covariance**: $Cov(X,Y) = E[XY] - E[X]E[Y]$.
$E[X] = 0(0.4) + 1(0.6) = 0.6$.
$E[XY] = \sum x \cdot y \cdot P(X=x, Y=y) = (1)(1)(0.2) + (1)(2)(0.3) + (1)(3)(0.1) = 0.2 + 0.6 + 0.3 = 1.1$.
$Cov(X,Y) = 1.1 - (0.6)(1.9) = 1.1 - 1.14 = -0.04$.

### Exercise 4
$T \sim N(\mu=45, \sigma^2=8^2)$. Standardizing: $Z = \frac{T - \mu}{\sigma}$.
**(a)** $P(T > 50) = P\left(Z > \frac{50 - 45}{8}\right) = P(Z > 0.625)$.
Using symmetric properties and normal tables: $1 - \Phi(0.625) \approx 1 - 0.7340 = 0.266$.
**(b) 90th percentile**: Find $t_{90}$ such that $P(T < t_{90}) = 0.90$.
From the inverse standard normal table, $\Phi(z) = 0.90 \implies z \approx 1.28$.
$t_{90} = \mu + z \cdot \sigma = 45 + 1.28(8) = 45 + 10.24 = 55.24$ seconds.

### Exercise 5
**(a)** Poisson with $\lambda = 1.5$.
$P(X = 0) = \frac{e^{-1.5} \cdot 1.5^0}{0!} = e^{-1.5} \approx 0.223$.
**(b)** $P(X \ge 2) = 1 - P(X \le 1) = 1 - [P(X=0) + P(X=1)] = 1 - [e^{-1.5} + 1.5e^{-1.5}] = 1 - 2.5(e^{-1.5}) \approx 1 - 0.558 = 0.442$.
**(c)** This is a Binomial distribution! Let $W$ be the number of months with at least 2 crashes: $W \sim Bin(n=4, p=0.442)$.
We need $P(W = 2) = \binom{4}{2} (0.442)^2 (1 - 0.442)^2 = 6 \cdot (0.1954) \cdot (0.3114) \approx 0.365$.
