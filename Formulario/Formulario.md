Ecco un formulario completo e strutturato, basato sulle tue fonti (slide ed esercizi), organizzato per i macro-argomenti del tuo primo parziale: dalla statistica descrittiva alla distribuzione normale.

---

# **1. Statistica Descrittiva

_Utilizzata per sintetizzare i dati di un campione._
### Misure di Posizione

- **Media Campionaria ($\bar{y}$):** $\bar{y} = \frac{1}{N} \sum_{i=1}^{N} y_i$.

- **Mediana:**
    - Se $N$ è dispari: Valore in posizione $(N+1)/2$.
    - Se $N$ è pari: Media dei valori in posizione $(N/2)$ e $(N/2)+1$.
    
- **Moda:** Il valore (o i valori) che appare più frequentemente.

- **Quantili e Quartili ($Q_p$):** Il valore tale che il $p\%$ delle osservazioni è $\le$ ad esso.
    - **Primo Quartile ($Q_1$):** 25° percentile. Posizione: $0.25(N)$.
    - **Terzo Quartile ($Q_3$):** 75° percentile. Posizione: $0.75(N)$.
    
- **Media per dati raggruppati in classi**
	Per i dati raggruppati, la media aritmetica $\bar{x}$ si calcola utilizzando i valori centrali delle classi pesati per le loro frequenze:

$$\bar{x} = \frac{\sum (x_i \cdot f_i)}{\sum f_i}$$
	Dove:
	- **$x_i$**: è il valore centrale della classe.
	- **$f_i$**: è la frequenza della classe (quante unità appartengono a quell'intervallo).
	- **$\sum f_i$**: è il numero totale di osservazioni ($N$).
    
- **Mediana per dati raggruppati in classi:** Se devi trovare la mediana in una tabella con classi $(L_i, L_{i+1}]$, usa la formula:
    $$Me \approx L + \left( \frac{\frac{n}{2} - F_{prev}}{f_{me}} \right) \cdot \Delta$$
    _Dove:_ $L$ è il limite inferiore della classe mediana, $F_{prev}$ è la frequenza cumulata della classe precedente, $f_{me}$ è la frequenza della classe mediana e $\Delta$ è l'ampiezza della classe.
    
- **Proprietà della Media:**
    $$\sum_{i=1}^{n} (x_i - \bar{x}) = 0$$
    (La somma degli scarti dalla media è sempre nulla).
    
- **Varianza di una trasformazione lineare:**
    
	Se $Y = aX + b$, allora $s_Y^2 = a^2 s_X^2$ e $s_Y = |a| s_X$.

### Misure di Variabilità

- **Range (Campo di Variazione):** $Y_{max} - Y_{min}$.

- **Intervallo Interquartile (IQR):** $Q_3 - Q_1$.

- **Varianza Campionaria ($s^2$):** $s^2 = \frac{\sum (y_i - \bar{y})^2}{N-1}$.

- **Deviazione Standard ($s$):** $s = \sqrt{s^2}$.

- **Coefficiente di Variazione (CV):** $$CV = \frac{s}{\bar{x}} $$ (utilizzato per confrontare la variabilità tra gruppi con medie diverse).

**Regola Outlier (Box-plot):** Un dato è outlier se fuori dall'intervallo $[Q_1 - 1.5 \cdot IQR, \;\; Q_3 + 1.5 \cdot IQR]$.

![](https://encrypted-tbn3.gstatic.com/licensed-image?q=tbn:ANd9GcSj33oL0-2XXqNimeTPuHDY212Kp8kkGM2xYzOUfvF4sNVArEpbKKfb4HYJTGxquiio8jlTo670wPMIvyOO2Kj0_dsOUbWIusLj7AMkSY8Btzybaio)
### Analisi Bivariata e Forma

- **Covarianza Campionaria ($s_{xy}$):** $s_{xy} = \frac{\sum (y_i - \bar{y})(x_i - \bar{x})}{N-1}=\left( \frac{\sum x_i y_i}{n} \right) - \bar{x}\bar{y}$.

- **Coefficiente di Correlazione di Pearson ($r$):** $r = \frac{s_{xy}}{s_x s_y}$ ($\text{con } -1 \le r_{xy} \le 1$).

- **Dati in Classi (Grouped Data):**
    - Media stimata: $\bar{x} \approx \frac{\sum f_i m_i}{n}$, dove $f_i-$ è la frequenza e $m_i$ il valore centrale della classe.
    
- **Asimmetria (Skewness):**
    - **Negativa (a sinistra):** Media < Mediana.
    - **Positiva (a destra):** Media > Mediana.

---

# **2. Calcolo delle Probabilità**

- **Assiomi di Kolmogorov:** $P(A) \ge 0$, $P(\Omega) = 1$, se $A, B$ disgiunti $P(A \cup B) = P(A) + P(B)$.

- **Complemento:** $P(A^c) = 1 - P(A)$.

- **Unione (Regola Additiva):** $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.
	- Se $A, B$ sono _mutuamente esclusivi_: $P(A \cap B) = 0$.
	
- **Probabilità Condizionata:** $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$.

- **Indipendenza:** $A$ e $B$ sono indipendenti se $P(A \cap B) = P(A) \cdot P(B) \quad \text{oppure} \quad P(A|B) = P(A)$

- **Teorema della Probabilità Totale:** $P(B) = \sum P(B \mid A_i)P(A_i)$ per una partizione $A_i$.

- **Teorema di Bayes:** $P(A \mid B) = \frac{P(B \mid A)P(A)}{P(B)}$ , generalizzata: $P(A_i|B) = \frac{P(B|A_i)P(A_i)}{P(B)}$.

---

# **3. Variabili Casuali (V.C.)**

- **Valore Atteso (Media):**
    
    - _Discreto:_ $E[X] = \sum x_i p(x_i)$
        
    - _Continuo:_ $E[X] = \int x f(x) dx$
        
- **Varianza** ($V[X]$ o $\sigma^2$): $V[X] = E[X^2] - (E[X])^2$
    
- **Proprietà Lineari:**
    
    - $E[aX + b] = aE[X] + b$
        
    - $V[aX + b] = a^2 V[X]$
        
    - $V[X \pm Y] = V[X] + V[Y] \pm 2Cov(X,Y)$ (Se indipendenti, $Cov=0$).
    
- **Standardizzazione:** $Z = \frac{X - \mu}{\sigma}$, dove $Z \sim N(0, 1)$.
### **Covarianza e Indipendenza (Proprietà Avanzate)**

- **Relazione Valore Atteso-Covarianza:**
    $$E[XY] = E[X]E[Y] + Cov(X,Y) $$ $$ -> Cov(X,Y) = E[XY] - E[X]E[Y] $$
- **Indipendenza:** Se $X$ e $Y$ sono indipendenti $\implies Cov(X,Y) = 0$ (quindi $r_{xy} = 0$).
    
	_Attenzione:_ Il viceversa non è sempre vero (correlazione nulla non implica sempre indipendenza, a meno che le variabili non siano normali congiunte).
	
- **Somma di RV:**
    - $E[aX + bY] = aE[X] + bE[Y]$.

    - **Varianza della somma:** $V[aX + bY] = a^2V[X] + b^2V[Y] + 2abCov(X, Y)$.
    
    - Se $X, Y$ indipendenti: $V[X+Y] = V[X] + V[Y]$ (perché $Cov(X,Y)=0$).
---

# **4. Distribuzioni Notevoli (Discrete)**

- **Bernoulli ($p$):** $X \in \{0, 1\}$
    
    - $E[X] = p$, $V[X] = p(1-p)$
        
- **Binomiale ($n, p$):** Successi in $n$ prove indipendenti.
    
    - $P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$
        
    - $E[X] = np$, $V[X] = np(1-p)$
        
- **Poisson ($\lambda$):** Eventi in un intervallo continuo (tempo/spazio).
    
    - $P(X=k) = \frac{e^{-\lambda} \lambda^k}{k!}$
        
    - $E[X] = \lambda$, $V[X] = \lambda$

### Approssimazione della Binomiale alla Poisson

_Spesso richiesta quando $n$ è molto grande e $p$ è molto piccolo:_

- **Condizione:** Di solito se $n \ge 20$ e $p \le 0.05$ (o $n \ge 100$ e $np \le 10$).
    
- **Formula:** $X \sim Bin(n, p) \implies X \approx Poisson(\lambda = n \cdot p)$.

---

# **5. Distribuzione Notevoli Continue**

- **Normale($\mu, \sigma^2$):** Simmetrica rispetto a $\mu$.
    - **Regola Empirica:** 68% in $\mu \pm \sigma$, 95% in $\mu \pm 2\sigma$, 99.7% in $\mu \pm 3\sigma$.
    
- **Chi-Quadro ($\chi^2_\nu$):** $E[X] = \nu$, $V[X] = 2\nu$.

- **Student's $t$ ($\nu$):** Simmetrica intorno a 0; per $\nu \to \infty$ tende alla Normale Standard.

_X segue una distribuzione a campana $N(\mu, \sigma^2)$._

- **Standardizzazione:** Per usare le tavole, trasforma $X$ in $Z \sim N(0, 1)$:
    $$Z = \frac{X - \mu}{\sigma}$$
- **Calcolo Probabilità:**
    
    - $P(X \le k) = P(Z \le \frac{k-\mu}{\sigma}) = \Phi(z)$
        
    - $P(a \le X \le b) = \Phi(z_b) - \Phi(z_a)$
        
- **Proprietà Simmetria:**
    
    - $\Phi(-z) = 1 - \Phi(z)$
        
    - $P(Z > z) = 1 - \Phi(z)$
        

![Gauss distribution. Standard normal distribution. Gaussian bell graph curve. Business and marketing concept. Math probability theory. Editable stroke. Vector illustration isolated on white background](https://encrypted-tbn0.gstatic.com/licensed-image?q=tbn:ANd9GcRG7XS1PzE2PqLY6azLksh0TsVK9Tt6I4nXWBxUw67IFfeKBIE0hyN1cGhuSQY7oKAvlBM_waffjDj3KgWCKDKScCdcrc3ZzJSx1YCJC4eIi3N5DrI)

_Gauss distribution. Standard normal distribution. Gaussian bell graph curve. Business and marketing concept. Math probability theory. Editable stroke. Vector illustration isolated on white background_

### **Uso delle Tavole della Normale (Simmetrie)**

- $P(Z > z) = 1 - \Phi(z)$
    
- $P(Z < -z) = 1 - \Phi(z)$
    
- $P(-z < Z < z) = 2\Phi(z) - 1$
    
- **Per trovare i percentili ($z$ dato $p$):** Se cerchi $z$ per cui $P(Z \le z) = 0.95$, cerchi il valore più vicino a $0.95$ dentro la tabella e leggi il valore di $z$ corrispondente ($1.645$).

### Approssimazioni Fondamentali

- **Binomiale $\to$ Poisson:** Se $n \ge 20$ e $p \le 0.05$ (o $n \ge 100, p \le 0.1$), allora $Bi(n, p) \approx Po(\lambda = np)$.

- **Binomiale $\to$ Normale:** Se $npq \ge 10$, allora $Bi(n, p) \approx N(\mu = np, \sigma^2 = npq)$.

- **Poisson $\to$ Normale:** Se $\lambda \ge 10$, allora $Po(\lambda) \approx N(\mu = \lambda, \sigma^2 = \lambda)$.

- **Binomiale vs Bernoulli:** Una distribuzione Binomiale con un solo tentativo ($n=1$) coincide con una Bernoulli: **$Bi(1, p) = Be(p)$**.

- **Normale vs Chi-Quadro:** Se $Z \sim N(0, 1)$, allora il suo quadrato segue una Chi-Quadro con 1 grado di libertà: **$Z^2 \sim \chi^2(1)$**. La somma di $n$ quadrati di variabili $N(0, 1)$ indipendenti segue una **$\chi^2(n)$**.

- **t di Student vs Cauchy:** Quando $\nu = 1$, la distribuzione $t$ di Student è equivalente alla distribuzione di **Cauchy(0, 1)**, dove media e varianza non esistono a causa delle code estremamente pesanti.

- **t di Student vs Fisher-F:** Se $X \sim T(\nu)$, allora il suo quadrato segue una distribuzione di Fisher: **$X^2 \sim F(1, \nu)$**.

- **Composizione della Fisher-F:** Dati $X_1 \sim \chi^2(\nu_1)$ e $X_2 \sim \chi^2(\nu_2)$ indipendenti, il rapporto delle loro medie segue una Fisher: **$\frac{X_1/\nu_1}{X_2/\nu_2} \sim F(\nu_1, \nu_2)$**.

- **Composizione della t di Student:** Se $Z \sim N(0, 1)$ e $W \sim \chi^2(\nu)$ sono indipendenti, allora **$\frac{Z}{\sqrt{W/\nu}} \sim T(\nu)$**.

- **Relazione tra Varianza Campionaria e Chi-Quadro:** Se un campione $X_1$​,…,$X_n$​ proviene da una popolazione Normale N(μ,$σ^2$), allora la statistica che coinvolge la varianza campionaria $S^2$ segue una distribuzione Chi-Quadro: σ2(n−1)S2​∼χ2(n−1)

---

# **Suggerimenti per l'Esame (Tratti dai Mock Test):**

- **Attenzione alla varianza:** Negli esercizi di statistica descrittiva, controlla se viene chiesta la varianza campionaria ($n-1$) o della popolazione ($n$). Nelle slide di Cardinali si usa spesso $n$ per la descrizione.
    
-  **Passaggio Binomiale $\to$ Poisson:** Se $n$ è grande e $p$ è piccolo, puoi approssimare con $\lambda = n \cdot p$.
    
-  **Somma di Normali:** Se $X$ e $Y$ sono normali e indipendenti, la loro somma $W = X+Y$ è ancora normale con:
    
    - $\mu_W = \mu_X + \mu_Y$
        
    - $\sigma_W = \sqrt{\sigma_X^2 + \sigma_Y^2}$ (attenzione: somma le varianze, non le deviazioni standard!).
    
- **Almeno uno:** $P(X \ge 1) = 1 - P(X = 0)$.

- **Probabilità tra due valori:** $P(a \le X \le b) = F(b) - F(a)$.

- **Trovare il Percentile ($k$):** In una Normale, se $P(X \le k) = \alpha$, usa le tavole per trovare $z_\alpha$ e poi $k = \mu + z_\alpha \cdot \sigma$.

- **Indipendenza vs Correlazione:** Se $X, Y$ indipendenti $\implies$ incorrelati ($r=0$). Il viceversa non è sempre vero (tranne per RV congiuntamente normali).
