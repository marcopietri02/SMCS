# Statistical Methods for Computer Science
## Exercise Battery 4 for intermediate test part 1

---

### Section 1: Probability Basics & Random Experiments

**1. Which of the following is NOT an example of a random experiment?**
- [ ] A) The daily change of a stock market index price.
- [ ] B) A customer inspecting a delivery and finding an error.
- [ ] C) An executive board budgeting a fixed 10% increase in marketing.
- [ ] D) Tossing a coin to determine heads or tails.

**2. A subset of outcomes from a random experiment is formally defined as a(n):**
- [ ] A) Sample space.
- [ ] B) Event.
- [ ] C) Basic group.
- [ ] D) Probability frequency.

---

### Section 2: Exact Set Operations (Sample Space)
*Assume you roll a pair of standard 6-sided dice and consider the SUM of the dice as your outcome. Let $S = \{2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12\}$ be your sample space.*  
*Let **Event A** be the event that you observe an EVEN sum.*  
*Let **Event B** be the event that you observe a sum STRICTLY GREATER than 7.*

**3. What is the intersection set exactly, $A \cap B$?**
- [ ] A) $\{8, 10, 12\}$
- [ ] B) $\{7, 8, 9, 10, 11, 12\}$
- [ ] C) $\{2, 4, 6, 8, 10, 12\}$
- [ ] D) $\{8, 9, 10, 11, 12\}$

**4. What is the union set exactly, $A \cup B$?**
- [ ] A) $\{8, 10, 12\}$
- [ ] B) $\{2, 4, 6, 8, 9, 10, 11, 12\}$
- [ ] C) $\{2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12\}$
- [ ] D) $\{4, 5, 7, 8, 11, 12\}$

**5. What is the exact set for $A^C \cap B$ (the intersection of the complement of A and B)?**
- [ ] A) $\{9, 11\}$
- [ ] B) $\{3, 5, 7\}$
- [ ] C) $\{2, 3, 4, 6\}$
- [ ] D) $\{7, 9, 11\}$

---

### Section 3: Descriptive Statistics Contextual & Visual

**6. Which measures of central location are NOT heavily affected by extremely small or extremely large data values (outliers)?**
- [ ] A) Arithmetic mean and median
- [ ] B) Median and mode
- [ ] C) Mode and arithmetic mean
- [ ] D) None, they are all affected.

**7. *Visual Test:* Imagine a scatter plot where the points are moderately spread out but clearly form a downward sloping band from the top-left to the bottom-right. What would be your best visual estimate of the correlation coefficient, $r$?**
- [ ] A) $1.0$
- [ ] B) $-1.0$
- [ ] C) $0.0$
- [ ] D) $-0.8$

**8. Given a set of exactly $N = 25$ observations, for what value of the linear correlation coefficient $r$ would we be statistically confident to say there is solid evidence of a relationship?** *(Hint: standard rule-of-thumb threshold)*
- [ ] A) $|r| \ge 0.40$
- [ ] B) $|r| \ge 0.35$
- [ ] C) $|r| \ge 0.30$
- [ ] D) $|r| \ge 0.25$

<div style="page-break-after: always;"></div>

---

# Solutions / Svolgimento

### Section 1
**1. C) An executive board budgeting a fixed 10% increase in marketing.**
*Explanation:* A random experiment (or trial) must contain uncertainty about its outcome until it is performed. A management decision to budget a fixed amount is deterministic and predetermined, not a random trial.

**2. B) Event.**
*Explanation:* In statistical terminology, while the "Sample space" represents ALL possible outcomes, any specific subset of those combinations is called an "Event".

---

### Section 2
*Premise breakdown:* Let's write out the sets clearly.
$S = \{2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12\}$
$A$ (Even) $= \{2, 4, 6, 8, 10, 12\}$
$B$ (Greater than 7) $= \{8, 9, 10, 11, 12\}$

**3. A) $\{8, 10, 12\}$.**
*Explanation:* The intersection $A \cap B$ asks for values that are BOTH Even AND Greater than 7. Looking at the two sets, the common numbers are 8, 10, and 12.

**4. B) $\{2, 4, 6, 8, 9, 10, 11, 12\}$.**
*Explanation:* The union $A \cup B$ groups all elements from $A$ and all elements from $B$ without repeating them. You take all the even numbers, plus the odd numbers greater than 7 (which are 9 and 11).

**5. A) $\{9, 11\}$.**
*Explanation:* 
First find $A^C$ (Complement of A, i.e., "Not Even" means "Odd"):
$A^C = \{3, 5, 7, 9, 11\}$.
Now intersect $A^C \cap B$ (Odd AND Greater than 7). The common values between $\{3, 5, 7, 9, 11\}$ and $\{8, 9, 10, 11, 12\}$ are exactly 9 and 11.

---

### Section 3
**6. B) Median and mode.**
*Explanation:* The arithmetic mean includes all values in its sum, meaning one giant outlier drastically changes the average. The median relies only on physical *position*. The mode relies only on *frequency*. Thus, neither median nor mode fly wildly off the handle with extreme outliers.

**7. D) $-0.8$.**
*Explanation:* A downward slope implies a **negative** relationship ($r < 0$). However, since the points are "moderately spread out" instead of perfectly forming a thin single line, the correlation cannot be a perfect $-1.0$. Therefore, $-0.8$ is the only reasonable estimate.

**8. A) $|r| \ge 0.40$.**
*Explanation:* A very well known statistical approximation (often taught in intro SMCS courses to determine the evidence threshold for Pearson's $r$) is $2 / \sqrt{N}$. Here $N = 25$, so $2 / \sqrt{25} = 2/5 = 0.40$. Without reaching this threshold, the linear relationship might just be noise.
