# Formulario di Statistica per il Primo Parziale

Raccolta strutturata di formule e concetti: dalla statistica descrittiva alla distribuzione normale.

## Indice

1.  [Statistica Descrittiva](https://www.google.com/search?q=%231-statistica-descrittiva)
2.  [Calcolo delle Probabilità](https://www.google.com/search?q=%232-calcolo-delle-probabilit%C3%A0)
3.  [Variabili Casuali (V.C.)](https://www.google.com/search?q=%233-variabili-casuali-vc)
4.  [Distribuzioni Discrete](https://www.google.com/search?q=%234-distribuzioni-notevoli-discrete)
5.  [Distribuzioni Continue](https://www.google.com/search?q=%235-distribuzioni-notevoli-continue)
6.  [Approssimazioni e Relazioni](https://www.google.com/search?q=%236-approssimazioni-fondamentali)
7.  [Suggerimenti per l'Esame](https://www.google.com/search?q=%237-suggerimenti-per-lesame)

-----

## 1\. Statistica Descrittiva

### Misure di Posizione

  * **Media Campionaria ($\bar{y}$):** $$\bar{y} = \frac{1}{N} \sum_{i=1}^{N} y_i$$
  * **Mediana:**
      * Se $N$ è dispari: Valore in posizione $(N+1)/2$.
      * Se $N$ è pari: Media dei valori in posizione $(N/2)$ e $(N/2)+1$.
  * **Moda:** Il valore che appare con frequenza massima.
  * **Quartili ($Q_p$):**
      * **Primo Quartile ($Q_1$):** 25° percentile. Posizione: $0.25(N)$.
      * **Terzo Quartile ($Q_3$):** 75° percentile. Posizione: $0.75(N)$.

### Dati Raggruppati in Classi

  * **Media:** $\bar{x} = \frac{\sum (x_i \cdot f_i)}{\sum f_i}$ (dove $x_i$ è il valore centrale della classe).
  * **Mediana:** 1. Calcola il valore centrale $x_i = \frac{inf + sup}{2}$.
    2\. Identifica la classe mediana tramite le frequenze cumulate ($N/2$).

### Misure di Variabilità

  * **Range:** $Y_{max} - Y_{min}$.
  * **Intervallo Interquartile (IQR):** $Q_3 - Q_1$.
  * **Varianza Campionaria ($s^2$):** $s^2 = \frac{\sum (y_i - \bar{y})^2}{N-1}$.
  * **Deviazione Standard ($s$):** $s = \sqrt{s^2}$.
  * **Coefficiente di Variazione (CV):** $CV = \frac{s}{\bar{x}}$.
  * **Regola Outlier (Box-plot):** Un dato è outlier se fuori dall'intervallo $[Q_1 - 1.5 \cdot IQR, \;\; Q_3 + 1.5 \cdot IQR]$.

### Analisi Bivariata

  * **Covarianza ($s_{xy}$):** $s_{xy} = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{N-1} = \left( \frac{\sum x_i y_i}{n} \right) - \bar{x}\bar{y}$.
  * **Correlazione di Pearson ($r$):** $r = \frac{s_{xy}}{s_x s_y}$ (con $-1 \le r \le 1$).

-----

## 2\. Calcolo delle Probabilità

  * **Assiomi:** $P(A) \ge 0$, $P(\Omega) = 1$.
  * **Unione:** $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.
  * **Probabilità Condizionata:** $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$.
  * **Indipendenza:** $A, B$ indipendenti se $P(A \cap B) = P(A) \cdot P(B)$ o $P(A|B) = P(A)$.
  * **Teorema della Probabilità Totale:** $P(B) = \sum P(B \mid A_i)P(A_i)$.
  * **Teorema di Bayes:** $P(A_i \mid B) = \frac{P(B \mid A_i)P(A_i)}{\sum P(B \mid A_j)P(A_j)}$.

-----

## 3\. Variabili Casuali (V.C.)

  * **Valore Atteso (E[X]):**
      * Discreto: $\sum x_i p(x_i)$
      * Continuo: $\int x f(x) dx$
  * **Varianza (V[X]):** $V[X] = E[X^2] - (E[X])^2$.
  * **Trasformazioni Lineari:**
      * $E[aX + b] = aE[X] + b$
      * $V[aX + b] = a^2 V[X]$
  * **Somma di Variabili:**
      * $E[aX + bY] = aE[X] + bE[Y]$
      * $V[aX \pm bY] = a^2V[X] + b^2V[Y] \pm 2abCov(X, Y)$ (Se indipendenti, $Cov=0$).

-----

## 4\. Distribuzioni Notevoli (Discrete)

| Distribuzione | Formula $P(X=k)$ | $E[X]$ | $V[X]$ |
| :--- | :--- | :--- | :--- |
| **Bernoulli(p)** | $p^k (1-p)^{1-k}$ | $p$ | $p(1-p)$ |
| **Binomiale(n, p)** | $\binom{n}{k} p^k (1-p)^{n-k}$ | $np$ | $np(1-p)$ |
| **Poisson($\lambda$)** | $\frac{e^{-\lambda} \lambda^k}{k!}$ | $\lambda$ | $\lambda$ |

-----

## 5\. Distribuzioni Notevoli (Continue)

### Distribuzione Normale $N(\mu, \sigma^2)$

[Image of standard normal distribution curve]

  * **Standardizzazione:** $Z = \frac{X - \mu}{\sigma}$ dove $Z \sim N(0, 1)$.
  * **Simmetrie Tavole:**
      * $P(Z > z) = 1 - \Phi(z)$
      * $P(Z < -z) = 1 - \Phi(z)$
      * $P(-z < Z < z) = 2\Phi(z) - 1$

### Altre Distribuzioni

  * **Chi-Quadro ($\chi^2_\nu$):** Somma di $n$ variabili $Z^2$. $E[X]=\nu, V[X]=2\nu$.
  * **t di Student ($\nu$):** Simmetrica intorno a 0. Tende alla Normale per $\nu \to \infty$.
  * **Fisher-F ($\nu_1, \nu_2$):** Rapporto tra due varianze campionarie.

-----

## 6\. Approssimazioni Fondamentali

1.  **Binomiale $\to$ Poisson:** Se $n \ge 20$ e $p \le 0.05 \implies \lambda = np$.
2.  **Binomiale $\to$ Normale:** Se $np(1-p) \ge 10 \implies N(np, np(1-p))$.
3.  **Poisson $\to$ Normale:** Se $\lambda \ge 10 \implies N(\lambda, \lambda)$.

-----

## 7\. Suggerimenti per l'Esame

  * **Varianza:** Controlla sempre se dividere per $N$ o $N-1$ (campione vs popolazione).
  * **Almeno uno:** $P(X \ge 1) = 1 - P(X = 0)$.
  * **Somma di Normali:** Se indipendenti, $X+Y \sim N(\mu_X + \mu_Y, \sigma_X^2 + \sigma_Y^2)$. **Attenzione:** si sommano le varianze, non le deviazioni standard.
  * **Percentili:** Per trovare $k$ tale che $P(X \le k) = \alpha$, calcola $k = \mu + z_\alpha \cdot \sigma$.
  * **Indipendenza:** Se $X, Y$ sono indipendenti $\implies Cov(X,Y) = 0$. Il viceversa è vero solo se sono normali congiunte.
