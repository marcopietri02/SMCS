# Statistical Methods for Computer Science
## Exercise Battery 3 for intermediate test part 1

---

### Exercise 1: Descriptive Statistics & Outlier Detection
A small software startup measured the server response times (in milliseconds) for 10 API requests, producing the following sorted dataset:
**12, 14, 15, 16, 18, 19, 21, 23, 24, 42**

**(a)** Calculate the First Quartile ($Q_1$), the Median ($Q_2$), and the Third Quartile ($Q_3$).
**(b)** Calculate the Interquartile Range ($IQR$).
**(c)** Using the standard $1.5 \times IQR$ rule, determine mathematically if there are any outliers in the dataset.

**Answers:**
(a) $Q_1$: [       ], Median: [       ], $Q_3$: [       ] / 3
(b) $IQR$: [                   ] / 1
(c) Outliers?: [                   ] / 2

---

### Exercise 2: Combinatorics & Classical Probability
An IT department is auditing a cluster of 15 database nodes. Without the department knowing, exactly 4 of these nodes are infected with a hidden malware. A technician randomly selects exactly 5 nodes to inspect.
**(a)** What is the probability that exactly 2 of the inspected nodes are infected?
**(b)** What is the probability that NONE of the inspected nodes are infected?

**Answers:**
(a) [                   ] / 3
(b) [                   ] / 3

---

### Exercise 3: Linear Transformations & Chebyshev's Inequality
A security firm tracks the number of brute-force attacks $X$ on a network per day. It is known that the expected value is $E[X] = 50$ and the variance is $V[X] = 16$. The system DOES NOT follow a Normal distribution (the shape is unknown).
A new tracking metric $Y$ assigns a "severity score" defined by the linear transformation $Y = 3X - 10$.
**(a)** Find the Expected Value $E[Y]$ and the Variance $V[Y]$.
**(b)** Using Chebyshev's Inequality, find the *minimum* probability that the metric $Y$ falls inside the interval $[104, 176]$.

**Answers:**
(a) $E[Y]$: [       ], $V[Y]$: [       ] / 2
(b) [                   ] / 4

---

### Exercise 4: Continuous Distributions (The Exponential)
The lifespan $T$ (in years) of a specific solid-state drive (SSD) follows an Exponential distribution, with an average lifespan of 4 years.
**(a)** What is the rate parameter $\lambda$ of the distribution?
**(b)** Find the probability that an SSD will last longer than 6 years.
**(c)** *[Memoryless Property]* An SSD has already been functioning perfectly for 3 years. What is the probability that it will survive for *an additional* 6 years?

**Answers:**
(a) [                   ] / 1
(b) [                   ] / 2
(c) [                   ] / 2

<div style="page-break-after: always;"></div>

---

# Solutions / Svolgimento

### Exercise 1
**Premise:** Dataset $N=10$, already sorted: $\{12, 14, 15, 16, 18, 19, 21, 23, 24, 42\}$.
**(a) Quartiles:**
- **Median ($Q_2$):** The average of the 5th and 6th values: $(18 + 19) / 2 = 18.5$.
- **$Q_1$:** The median of the lower half of the data $\{12, 14, 15, 16, 18\}$. The middle value is **15**.
- **$Q_3$:** The median of the upper half of the data $\{19, 21, 23, 24, 42\}$. The middle value is **23**.
**(b) IQR:** 
$IQR = Q_3 - Q_1 = 23 - 15 = 8$.
**(c) Outlier Detection:**
An observation is considered an outlier if it falls below the Lower Bound or above the Upper Bound.
- **Lower Bound** = $Q_1 - 1.5 \times IQR = 15 - 1.5(8) = 15 - 12 = 3$.
- **Upper Bound** = $Q_3 + 1.5 \times IQR = 23 + 1.5(8) = 23 + 12 = 35$.
Looking at the dataset, the value **42** is greater than 35. Therefore, **42 is an outlier**.

---

### Exercise 2
This is a hypergeometric probability problem (sampling without replacement).
Total items $N = 15$. Successes in population $K = 4$ (infected). Sample size $n = 5$.
We use combinations: $\binom{n}{k} = \frac{n!}{k!(n - k)!}$
**(a) Exactly 2 are infected:**
We need to choose 2 from the 4 infected, and 3 from the 11 non-infected.
$P(X = 2) = \frac{\binom{4}{2} \cdot \binom{11}{3}}{\binom{15}{5}} = \frac{6 \cdot 165}{3003} = \frac{990}{3003} \approx 0.329$ (32.9\%).
**(b) None are infected:**
We need to choose 0 from the 4 infected, and all 5 from the 11 non-infected.
$P(X = 0) = \frac{\binom{4}{0} \cdot \binom{11}{5}}{\binom{15}{5}} = \frac{1 \cdot 462}{3003} \approx 0.154$ (15.4\%).

---

### Exercise 3
**(a) Linear Transformations:**
$E[X] = 50$, $V[X] = 16$.
$E[Y] = E[3X - 10] = 3E[X] - 10 = 3(50) - 10 = 150 - 10 = 140$.
$V[Y] = V[3X - 10] = 3^2 V[X] = 9(16) = 144$. (Note: additive constants vanish for variance).
**(b) Chebyshev's Inequality:**
Since $V[Y] = 144$, the standard deviation is $\sigma_Y = \sqrt{144} = 12$.
The interval is $[104, 176]$, which represents $140 \pm 36$.
We need to find $k$, the number of standard deviations from the mean: $k = \frac{36}{12} = 3$.
Chebyshev's inequality states: $P(|Y - \mu| < k\sigma) \ge 1 - \frac{1}{k^2}$.
$P(104 \le Y \le 176) \ge 1 - \frac{1}{3^2} = 1 - \frac{1}{9} = \frac{8}{9} \approx 0.8889$ (88.89\%).

---

### Exercise 4
**(a) Rate Parameter:**
The expected value of an Exponential distribution is $E[T] = \frac{1}{\lambda}$.
Since $E[T] = 4$, then $\lambda = \frac{1}{4} = 0.25$ $\text{years}^{-1}$.
**(b) Prob. longer than 6 years:**
The cumulative distribution function is $F(t) = 1 - e^{-\lambda t}$. The survival function is $P(T > t) = e^{-\lambda t}$.
$P(T > 6) = e^{-0.25 \cdot 6} = e^{-1.5} \approx 0.2231$ (22.3\%).
**(c) Memoryless Property:**
The exponential distribution has mathematically "no memory": $P(T > t + s \mid T > s) = P(T > t)$.
The fact that it already survived 3 years does not affect the probability of surviving the *next* 6 years.
$P(T > 3 + 6 \mid T > 3) = P(T > 6) = e^{-1.5} \approx 0.2231$ (22.3\%).
