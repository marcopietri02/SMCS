# Formulario Statistica

Raccolta strutturata di formule e concetti: dalla statistica descrittiva alla Linear Regression.

## Indice

### Prima Parte

1. [Statistica Descrittiva](#1-statistica-descrittiva)
2. [Calcolo delle Probabilità](#2-calcolo-delle-probabilità)
3. [Variabili Casuali (V.C.)](#3-variabili-casuali-vc)
4. [Distribuzioni Discrete](#4-distribuzioni-notevoli-discrete)
5. [Distribuzioni Continue](#5-distribuzioni-notevoli-continue)
6. [Approssimazioni e Relazioni](#6-approssimazioni-e-relazioni-fondamentali)
7. [Suggerimenti per l'Esame](#7-suggerimenti-per-lesame)


### Seconda Parte (Inferenza Statistica)

1. [Distribuzioni Continue Notevoli](#1-distribuzioni-continue-notevoli)
2. [Distribuzioni Campionarie](#2-distribuzioni-campionarie)
3. [Teoria della Stima](#3-teoria-della-stima)
4. [Intervalli di Confidenza (CI)](#4-intervalli-di-confidenza-(ci))
5. [Verifica di Ipotesi](#5-verifica-di-ipotesi)
6. [Linear Regression](#6-linear-regression)

---

# Prima Parte

## 1. Statistica Descrittiva

_Utilizzata per sintetizzare i dati di un campione._

### Misure di Posizione

- **Media Campionaria ($\bar{y}$):**
    
    $$\bar{y} = \frac{1}{N} \sum_{i=1}^{N} y_i$$
    
- **Mediana:**
    
    - Se $N$ è dispari: Valore in posizione $(N+1)/2$.
        
    - Se $N$ è pari: Media dei valori in posizione $(N/2)$ e $(N/2)+1$.
        
- **Moda:** Il valore (o i valori) che appare con frequenza massima.
    
- **Quantili e Quartili ($Q_p$):** Il valore tale che il $p\%$ delle osservazioni è $\le$ ad esso.
    
    - **Primo Quartile ($Q_1$):** 25° percentile. Posizione: $0.25(N)$.
        
    - **Terzo Quartile ($Q_3$):** 75° percentile. Posizione: $0.75(N)$.
        


![](https://encrypted-tbn3.gstatic.com/licensed-image?q=tbn:ANd9GcSj33oL0-2XXqNimeTPuHDY212Kp8kkGM2xYzOUfvF4sNVArEpbKKfb4HYJTGxquiio8jlTo670wPMIvyOO2Kj0_dsOUbWIusLj7AMkSY8Btzybaio)

### Dati Raggruppati in Classi

- **Media per dati raggruppati:**
    
    $$\bar{x} = \frac{\sum (x_i \cdot f_i)}{\sum f_i}$$
    
    (Dove $x_i$ è il valore centrale della classe e $f_i$ la frequenza).
    
- **Mediana per dati raggruppati:**
    
    1. Calcola il valore centrale di ogni classe: $x_i = \frac{inf + sup}{2}$.
        
    2. Identifica la classe mediana tramite le frequenze cumulate ($N/2$).
        
    3. Indica il valore centrale di quella classe come Mediana.
        
- **Varianza per dati raggruppati:**
    
    $$s^2 = \frac{\sum f_i (x_i - \bar{x})^2}{N} \quad \text{oppure} \quad s^2 = \left( \frac{1}{N}\sum f_i x_i^2 \right) - \bar{x}^2$$


> **Legenda:**
> 
> - $k$: numero di classi.
> 	
> - $x_i$: valore centrale della classe $i$ $\to \frac{inf + sup}{2}$.
> 	
> - $f_i$: frequenza assoluta della classe $i$.
> 	
> - $N$: totale delle osservazioni ($\sum f_i$).
> 	
> - $\bar{x}$: media dei dati raggruppati $\to \frac{\sum f_i x_i}{N}$.

### Misure di Variabilità

- **Range (Campo di Variazione):** $Y_{max} - Y_{min}$.
    
- **Intervallo Interquartile (IQR):** $Q_3 - Q_1$.
    
- **Varianza Campionaria ($s^2$):** $s^2 = \frac{\sum (y_i - \bar{y})^2}{N-1}$.
    
- **Deviazione Standard ($s$):** $s = \sqrt{s^2}$.
    
- **Coefficiente di Variazione (CV):** $CV = \frac{s}{\bar{x}}$ _(confronto tra gruppi con medie diverse)_.
    
- **Regola Outlier (Box-plot):** Un dato è outlier se fuori dall'intervallo $[Q_1 - 1.5 \cdot IQR, \;\; Q_3 + 1.5 \cdot IQR]$.
    

### Proprietà e Analisi Bivariata

- **Proprietà della Media:** $\sum_{i=1}^{n} (x_i - \bar{x}) = 0$.
    
- **Trasformazione Lineare:** Se $Y = aX + b$, allora $s_Y^2 = a^2 s_X^2$ e $s_Y = |a| s_X$.
    
- **Covarianza Campionaria ($s_{xy}$):**
    
    $$s_{xy} = \frac{\sum (y_i - \bar{y})(x_i - \bar{x})}{N-1} = \left( \frac{\sum x_i y_i}{n} \right) - \bar{x}\bar{y}$$
    
- **Correlazione di Pearson ($r$):** $r = \frac{s_{xy}}{s_x s_y}$ (con $-1 \le r \le 1$).
    
- **Asimmetria (Skewness):**
    
    - **Negativa (a sinistra):** Media < Mediana.
        
    - **Positiva (a destra):** Media > Mediana.
        

---

## 2. Calcolo delle Probabilità

- **Assiomi di Kolmogorov:** $P(A) \ge 0$, $P(\Omega) = 1$, se $A, B$ disgiunti $P(A \cup B) = P(A) + P(B)$.
    
- **Complemento:** $P(A^c) = 1 - P(A)$.
    
- **Unione (Regola Additiva):** $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.
    
    - Se mutuamente esclusivi: $P(A \cap B) = 0$.
        
- **Probabilità Condizionata:** $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$.
    
- **Indipendenza:** $A, B$ indipendenti se $P(A \cap B) = P(A)P(B)$ o $P(A|B) = P(A)$.
    
- **Teorema della Probabilità Totale:** $P(B) = \sum P(B \mid A_i)P(A_i)$ per una partizione $A_i$.
    
- **Teorema di Bayes:**
    
    $$P(A_i \mid B) = \frac{P(B \mid A_i)P(A_i)}{P(B)} = \frac{P(B \mid A_i)P(A_i)}{\sum P(B \mid A_j)P(A_j)}$$
    
- **Regola complemento per Probabilità condizionata:** $$1 = P(B \mid A) + P(B' \mid A)$$.

- **Conseguenza regola del complemento per la condizionata** $$P(B' \mid A') = 1 - P(B \mid A')$$.

- **Conseguenza dal teorema delle prob. totali** $$P(B) = P(A \cap B) + P(A' \cap B)$$ oppure
  $$P(A) = P(A \cap B) + P(A \cap B')$$
  con `A'` o `B'` negazioni di `A`e `B`.
  
  
---

## 3. Variabili Casuali (V.C.)

- **Valore Atteso (Media):**
    
    - Discreto: $E[X] = \sum x_i p(x_i)$
        
    - Continuo: $E[X] = \int x f(x) dx$
        
- **Varianza ($V[X]$):** $V[X] = E[X^2] - (E[X])^2$.
    
- **Proprietà Lineari:**
    
    - $E[aX + b] = aE[X] + b$
        
    - $V[aX + b] = a^2 V[X]$
        
    - $V[X \pm Y] = V[X] + V[Y] \pm 2Cov(X,Y)$ _(Se indipendenti, $Cov=0$)_.
        
- **Standardizzazione:** $Z = \frac{X - \mu}{\sigma}$ dove $Z \sim N(0, 1)$.
    

### Covarianza e Indipendenza (Proprietà Avanzate)

- **Relazione E[XY]-Covarianza:** $E[XY] = E[X]E[Y] + Cov(X,Y)$.
    
- **Indipendenza:** Se $X, Y$ indipendenti $\implies Cov(X,Y) = 0$ (e $r_{xy} = 0$).
    
- **Somma di RV:**
    
    - $E[aX + bY] = aE[X] + bE[Y]$.
        
    - $V[aX + bY] = a^2V[X] + b^2V[Y] + 2abCov(X, Y)$.
        

---

## 4. Distribuzioni Notevoli (Discrete)

|**Distribuzione**|**Formula P(X=k)**|**E[X]**|**V[X]**|
|---|---|---|---|
|**Bernoulli(p)**|$p^k (1-p)^{1-k}$|$p$|$p(1-p)$|
|**Binomiale(n, p)**|$\binom{n}{k} p^k (1-p)^{n-k}$|$np$|$np(1-p)$|
|**Poisson($\lambda$)**|$\frac{e^{-\lambda} \lambda^k}{k!}$|$\lambda$|$\lambda$|

---

## 5. Distribuzioni Notevoli (Continue)

### Distribuzione Normale $N(\mu, \sigma^2)$

![Gauss distribution. Standard normal distribution. Gaussian bell graph curve. Business and marketing concept. Math probability theory. Editable stroke. Vector illustration isolated on white background](https://encrypted-tbn0.gstatic.com/licensed-image?q=tbn:ANd9GcRG7XS1PzE2PqLY6azLksh0TsVK9Tt6I4nXWBxUw67IFfeKBIE0hyN1cGhuSQY7oKAvlBM_waffjDj3KgWCKDKScCdcrc3ZzJSx1YCJC4eIi3N5DrI)


- **Regola Empirica:** 68% in $\mu \pm \sigma$, 95% in $\mu \pm 2\sigma$, 99.7% in $\mu \pm 3\sigma$.
    
- **Standardizzazione:** $Z = \frac{X - \mu}{\sigma}$.
    
- **Calcolo Probabilità:**
    
    - $P(X \le k) = \Phi(z)$.
        
    - $P(a \le X \le b) = \Phi(z_b) - \Phi(z_a)$.
        
- **Simmetrie Tavole:**
    
    - $\Phi(-z) = 1 - \Phi(z)$.
        
    - $P(Z > z) = 1 - \Phi(z)$.
        
    - $P(-z < Z < z) = 2\Phi(z) - 1$.
        

### Altre Distribuzioni

- **Chi-Quadro ($\chi^2_\nu$):** $E[X] = \nu, V[X] = 2\nu$. Somma di $n$ variabili $Z^2$.
    
- **t di Student ($\nu$):** Simmetrica intorno a 0. Per $\nu \to \infty$ tende alla Normale.
    
- **Fisher-F ($\nu_1, \nu_2$):** Rapporto tra due varianze campionarie/medie di Chi-Quadro.
    

---

## 6. Approssimazioni e Relazioni Fondamentali

1. **Binomiale $\to$ Poisson:** Se $n \ge 20$ e $p \le 0.05$ (o $n \ge 100, np \le 10$) $\implies \lambda = np$.
    
2. **Binomiale $\to$ Normale:** Se $np(1-p) \ge 10 \implies N(\mu = np, \sigma^2 = np(1-p))$.
    
3. **Poisson $\to$ Normale:** Se $\lambda \ge 10 \implies N(\mu = \lambda, \sigma^2 = \lambda)$.
    
4. **Bernoulli vs Binomiale:** $Bi(1, p) = Be(p)$.
    
5. **Normale vs Chi-Quadro:** Se $Z \sim N(0, 1) \implies Z^2 \sim \chi^2(1)$.
    
6. **t di Student vs Cauchy:** Se $\nu = 1$, Student = Cauchy(0, 1).
    
7. **t di Student vs Fisher-F:** Se $X \sim T(\nu) \implies X^2 \sim F(1, \nu)$.
    
8. **Varianza Campionaria vs Chi-Quadro:** $\frac{(n-1)S^2}{\sigma^2} \sim \chi^2(n-1)$.
    

---

## 7. Suggerimenti per l'Esame

- **Varianza:** Controlla se chiede la varianza campionaria ($N-1$) o della popolazione ($N$).
    
- **Almeno uno:** $P(X \ge 1) = 1 - P(X = 0)$.
    
- **Probabilità tra due valori:** $P(a \le X \le b) = F(b) - F(a)$.
    
- **Somma di Normali:** Se indipendenti, si sommano le varianze: $\sigma_W = \sqrt{\sigma_X^2 + \sigma_Y^2}$.
    
- **Percentili:** Se $P(X \le k) = \alpha$, allora $k = \mu + z_\alpha \sigma$.
    
- **Indipendenza vs Correlazione:** Indipendenza $\implies$ $r=0$. Il viceversa vale solo per normali congiunte.

- **Regola pratica Binomiale vs Ipergeometrica:**

| **Situazione**                          | **Distribuzione corretta** |
| --------------------------------------- | -------------------------- |
| Popolazione grande / con reinserimento  | **Binomiale**              |
| Popolazione finita, senza reinserimento | **Ipergeometrica**         |

> **Nota:** La Binomiale richiede probabilità di successo costante ($p$). Senza reinserimento in popolazioni finite, $p$ cambia, richiedendo la Ipergeometrica.
> La distribuzione ipergeometrica si utilizza quando vogliamo calcolare la probabilità di ottenere un certo numero di "successi" in un campione estratto da una popolazione finita,
> senza reinserimento. A differenza della binomiale, qui le estrazioni non sono indipendenti: ogni volta che peschi un elemento, la composizione della popolazione cambia.
> $$P(X = k) = \frac{\binom{K}{k} \cdot \binom{N-K}{n-k}}{\binom{N}{n}}$$

---

# Seconda Parte

## 1. Distribuzioni Continue Notevoli

### Distribuzione Normale $N(\mu, \sigma^2)$

- **Funzione di Densità (PDF):** $f_X(x) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{1}{2}\frac{(x-\mu)^2}{\sigma^2}}$
    
- **Standardizzazione:** Se $X \sim N(\mu, \sigma^2)$, allora $Z = \frac{X - \mu}{\sigma} \sim N(0, 1)$
    
- **Proprietà Lineare:** $a + bX \sim N(a + b\mu, b^2\sigma^2)$
    
- **Regola Empirica:** $P(\mu \pm \sigma) \approx 68.27\%$, $P(\mu \pm 2\sigma) \approx 95.45\%$, $P(\mu \pm 3\sigma) \approx 99.73\%$
    

### Altre Distribuzioni Fondamentali

| **Distribuzione** | **Parametri**     | **E[X]**                | **V[X]**                          | **Note**                                    |
| ----------------- | ----------------- | ----------------------- | --------------------------------- | ------------------------------------------- |
| **Uniforme**      | $U(a, b)$         | $\frac{a+b}{2}$         | $\frac{(b-a)^2}{12}$              | Densità costante $1/(b-a)$                  |
| **Chi-Quadro**    | $\chi^2(\nu)$     | $\nu$                   | $2\nu$                            | Somma di $n$ variabili $Z^2$ indipendenti   |
| **t di Student**  | $T(\nu)$          | $0$ (per $\nu>1$)       | $\frac{\nu}{\nu-2}$ (per $\nu>2$) | $T = Z / \sqrt{W/\nu}$                      |
| **Fisher-F**      | $F(\nu_1, \nu_2)$ | $\frac{\nu_2}{\nu_2-2}$ | -                                 | Rapporto di due $\chi^2$ deviate per i d.f. |

**Relazioni Cruciali:**

- Se $Z \sim N(0,1)$, allora $Z^2 \sim \chi^2(1)$.
    
- Se $X \sim F(\nu_1, \nu_2)$, allora $1/X \sim F(\nu_2, \nu_1)$.
    

---

## 2. Distribuzioni Campionarie

- **Media Campionaria ($\bar{Y}$):** $E[\bar{Y}] = \mu$, $V[\bar{Y}] = \sigma^2/n$
    
- **Standard Error (SE):** $se(\bar{Y}) = \sigma/\sqrt{n}$. Se $\sigma$ è ignoto, si usa $s/\sqrt{n}$.
    
- **Varianza Campionaria Corretta ($S^2$):** $S^2 = \frac{\sum (Y_i - \bar{Y})^2}{n-1}$. È uno stimatore non distorto di $\sigma^2$.
    
- **Teorema del Limite Centrale (CLT):** Per $n \ge 30$, $\bar{Y}$ tende a una distribuzione Normale indipendentemente dalla distribuzione della popolazione.
    
- **Proporzione Campionaria ($\hat{p}$):** $E[\hat{p}] = p$, $V[\hat{p}] = \frac{p(1-p)}{n}$.
    

---

## 3. Teoria della Stima

### Proprietà degli Stimatori

- **Formula Bias:** $Bias(\hat{\theta}) = E[(\hat{\theta}] - \theta$

- **Non distorsione (Unbiasedness):** $E[\hat{\theta}] = \theta \implies Bias(\hat{\theta}) = 0$.
    
- **Consistenza:** $\hat{\theta} \xrightarrow{p} \theta$ al crescere di $n$.
    
- **Efficienza (MSE):** $MSE(\hat{\theta}) = E[(\hat{\theta} - \theta)^2] = V[\hat{\theta}] + [Bias(\hat{\theta})]^2$.
    

### Stima di Massima Verosimiglianza (MLE)

1. **Funzione di Verosimiglianza:** $L(\theta) = \prod_{i=1}^n f(y_i | \theta)$.
    
2. **Log-Verosimiglianza:** $l(\theta) = \ln L(\theta)$.
    
3. **Equazione di Score:** $\frac{\partial l(\theta)}{\partial \theta} = 0 \implies$ si risolve per trovare $\hat{\theta}_{MLE}$.
    

---

## 4. Intervalli di Confidenza (CI)

### Per la Media $\mu$ (Popolazione Normale)

- **$\sigma^2$ nota:** $CI = \bar{y} \pm z_{\alpha/2} \frac{\sigma}{\sqrt{n}}$
    
- **$\sigma^2$ incognita:** $CI = \bar{y} \pm t_{\alpha/2, n-1} \frac{s}{\sqrt{n}}$
    

### Per la Proporzione $p$ (Grandi Campioni)

- $CI \approx \hat{p} \pm z_{\alpha/2} \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$
    

### Per la Varianza $\sigma^2$

- $CI = \left[ \frac{(n-1)s^2}{\chi^2_{\alpha/2, n-1}}, \frac{(n-1)s^2}{\chi^2_{1-\alpha/2, n-1}} \right]$
    

---

## 5. Verifica di Ipotesi

### Struttura del Test

- **Ipotesi:** $H_0$ (nulla) vs $H_a$ (alternativa).
    
- **p-value:** Probabilità di ottenere un risultato uguale o più estremo di quello osservato, assumendo $H_0$ vera.
    
    - $p \le \alpha \implies$ Rifiuto $H_0$.
        
    - $p > \alpha \implies$ Non rifiuto $H_0$.
        

### Statistiche Test

- **Z-test (Media, $\sigma$ noto):** $z_{obs} = \frac{\bar{y} - \mu_0}{\sigma/\sqrt{n}}$
    
- **T-test (Media, $\sigma$ ignoto):** $t_{obs} = \frac{\bar{y} - \mu_0}{s/\sqrt{n}}$
    
- **Test Proporzione:** $z_{obs} = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0(1-p_0)}{n}}}$
    

### Errori e Potenza

- **Errore Tipo I ($\alpha$):** Rifiutare $H_0$ quando è vera (Significatività).
    
- **Errore Tipo II ($\beta$):** Non rifiutare $H_0$ quando è falsa.
    
- **Potenza del Test ($1-\beta$):** Capacità del test di rifiutare correttamente $H_0$ quando la verità è in $H_a$.

---

## 6. Linear Regression
    
DA FARE
