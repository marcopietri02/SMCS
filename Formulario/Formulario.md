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
4. [Intervalli di Confidenza (CI)](#4-intervalli-di-confidenza-ci)
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

- Punti di Flesso della Normale: Si trovano in $\mu - \sigma$ e $\mu + \sigma$.

- Relazione $t$ e $F$: Se $X \sim T(\nu)$, allora $X^2 \sim F(1, \nu)$.
    

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

- **Formula Bias:** $Bias(\hat{\theta}) = E[\hat{\theta}] - \theta$

- **Non distorsione (Unbiasedness):** $E[\hat{\theta}] = \theta \implies Bias(\hat{\theta}) = 0$.
    
- **Consistenza:** $\hat{\theta} \xrightarrow{p} \theta$ al crescere di $n$.
    
- **Efficienza (MSE):** $MSE(\hat{\theta}) = E[(\hat{\theta} - \theta)^2] = V[\hat{\theta}] + [Bias(\hat{\theta})]^2$.

- **Efficienza Relativa:** Rapporto tra le varianze di due stimatori non distorti: $Eff(\hat{\theta}_1, \hat{\theta}_2) = MSE[\hat{\theta}_2] / MSE[\hat{\theta}_1]$.
    

### Stima di Massima Verosimiglianza (MLE)

1. **Funzione di Verosimiglianza:** $L(\theta) = \prod_{i=1}^n f(y_i | \theta)$.
    
2. **Log-Verosimiglianza:** $l(\theta) = \ln L(\theta)$.
    
3. **Equazione di Score:** $\frac{\partial l(\theta)}{\partial \theta} = 0 \implies$ si risolve per trovare $\hat{\theta}_{MLE}$.
    

---

## 4. Intervalli di Confidenza (CI)

### Metodo del Pivot
Procedura in tre passi: 
1) Trovare una quantità pivotale $Q(\theta, Y)$ la cui distribuzione sia nota e indipendente da $\theta$;
2) Trovare l'intervallo più corto per il pivot;
3) Invertire l'intervallo rispetto a $\theta$.

### Per la Media $\mu$ (Popolazione Normale)

- **$\sigma^2$ nota:** $CI = \bar{y} \pm z_{\alpha/2} \frac{\sigma}{\sqrt{n}}$
    
- **$\sigma^2$ incognita:** $CI = \bar{y} \pm t_{\alpha/2, n-1} \frac{s}{\sqrt{n}}$

Per usare la distribuzione T-Student, deve essere specificato che i dati provengano da una distribuzione Normale.
(Se non è specificato si può aggiungere un commento nel compito, in cui questo assunzione viene fatta).
Quindi:
- campione molto grande -> si usa la distribuzione Normale
- campione piccolo -> se i dati provengono da una distribuzione Normale, allora si può usare la distribuzione T-Student
    

### Per la Proporzione $p$ (Grandi Campioni)

- $CI \approx \hat{p} \pm z_{\alpha/2} \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$
    

### Per la Varianza $\sigma^2$

- $CI = \left[ \frac{(n-1)s^2}{\chi^2_{\alpha/2, n-1}}, \frac{(n-1)s^2}{\chi^2_{1-\alpha/2, n-1}} \right]$
    

---

## 5. Verifica di Ipotesi

### Struttura del Test

- **Ipotesi:** $H_0$ (nulla) vs $H_a$ (alternativa).
    
- **p-value:** Probabilità di ottenere un risultato uguale o più estremo di quello osservato, assumendo $H_0$ vera.
    
    - $p \lt \alpha \implies$ Rifiuto $H_0$.
        
    - $p \ge \alpha \implies$ Non rifiuto $H_0$.

### Calcolo p-value in base alla Direzione del Test

La formula esatta del p-value cambia radicalmente a seconda di come hai impostato l'ipotesi alternativa ($H_1$).

#### Test Monodirezionale Destro ($H_1: \mu > \mu_0$)

Vuoi vedere se il tuo risultato è significativamente *maggiore* della media. Il p-value è l'area a **destra** della tua statistica test.

* **Formula:** $\text{p-value} = P(Z > Z_{calc})$

#### Test Monodirezionale Sinistro ($H_1: \mu < \mu_0$)

Vuoi vedere se il tuo risultato è significativamente *minore*. Il p-value è l'area a **sinistra** della tua statistica test.

* **Formula:** $\text{p-value} = P(Z < Z_{calc})$

#### Test Bidirezionale ($H_1: \mu \neq \mu_0$)

Vuoi vedere se c'è una differenza, non importa in quale direzione. Visto che la differenza può essere sia positiva che negativa, devi calcolare l'area della coda e **moltiplicarla per 2**.

* **Formula:** $\text{p-value} = 2 \times P(Z > |Z_{calc}|)$
        

### Statistiche Test

- **Z-test (Media, $\sigma$ noto):** $z_{obs} = \frac{\bar{y} - \mu_0}{\sigma/\sqrt{n}}$
    
- **T-test (Media, $\sigma$ ignoto):** $t_{obs} = \frac{\bar{y} - \mu_0}{s/\sqrt{n}}$
    
- **Test Proporzione:** $z_{obs} = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0(1-p_0)}{n}}}$


### Valore Critico nella Verifica d'Ipotesi

#### Definizioni Fondamentali

* **$\alpha$ (Livello di significatività):** Probabilità di errore di I tipo (rifiutare $H_0$ quando è vera).
* **Valore Critico ($z_c, t_c, \chi^2_c$):** Il punto di soglia che delimita la regione di rifiuto.
* **Statistica Test ($Z_{calc}, T_{calc}$):** Il valore calcolato dai dati del campione.

#### Regola di Decisione (Standard)

Si confronta la statistica calcolata ($Test_{calc}$) con il valore critico ($Soglia_c$):

* **Test Bidirezionale:** Rifiuto $H_0$ se $|Test_{calc}| > |Soglia_c|$
* **Test Monodirezionale Destro:** Rifiuto $H_0$ se $Test_{calc} > Soglia_c$
* **Test Monodirezionale Sinistro:** Rifiuto $H_0$ se $Test_{calc} < -Soglia_c$

#### Formule delle Statistiche Test Principali

A. Test Z (Popolazione con varianza $\sigma^2$ nota, o grandi campioni $n > 30$)

$$Z_{calc} = \frac{\bar{X} - \mu_0}{\frac{\sigma}{\sqrt{n}}}$$


Dove $\bar{X}$ è la media campionaria, $\mu_0$ la media sotto $H_0$, $\sigma$ la deviazione standard della popolazione, $n$ l'ampiezza del campione.

B. Test t di Student (Varianza $\sigma^2$ ignota e piccoli campioni $n < 30$)

$$T_{calc} = \frac{\bar{X} - \mu_0}{\frac{s}{\sqrt{n}}}$$

Dove $s$ è la deviazione standard campionaria. Gradi di libertà: $df = n - 1$.


#### Calcolo soglia critica con le Tavole Statistiche

Per trovare la soglia ti servono tre dati di partenza:

1. **Il tipo di distribuzione** ($Z$, $t$ di Student, $\chi^2$, $F$).
2. **Il livello di significatività $\alpha$** (es. $0.05$ o $0.01$).
3. **Il tipo di test** (Monodirezionale o Bidirezionale).

**Passo A: Determina l'area della coda ($p$)**

Prima di aprire la tavola, devi capire che valore cercare in base al test:

* **Test Monodirezionale (una coda):** Cerchi direttamente l'area $p = \alpha$.
* **Test Bidirezionale (due code):** Devi dividere l'alfa a metà, quindi cerchi l'area $p = \frac{\alpha}{2}$.

**Passo B: Trova il valore sulla tavola**

**Caso 1: Distribuzione Z (Normale Standardizzata)**

Le tavole $Z$ mostrano l'area *a sinistra* del punto o l'area *tra 0 e il punto*.

* Se vuoi un test **bidirezionale con $\alpha = 0.05$**, l'area nella coda di destra deve essere $0.025$. L'area a sinistra di quel punto sarà $1 - 0.025 = 0.975$.
* Cerchi il valore $0.975$ *all'interno* della tavola $Z$. Troverai che corrisponde all'incrocio tra la riga `1.9` e la colonna `0.06`.
* **Soglia critica $z_c = \pm 1.96$**.

**Caso 2: Distribuzione $t$ di Student (o $\chi^2$)**

Queste tabelle sono più semplici perché hanno già i livelli di significatività nelle colonne. Ti servono però i **Gradi di Libertà ($df$)**, che per un test a un campione sono $df = n - 1$ (dove $n$ è il numero di osservazioni).

* *Esempio:* Test $t$ bidirezionale, $\alpha = 0.05$, ampiezza campione $n = 11$ ($\implies df = 10$).
* Prendi la tavola della $t$ di Student.
* Incrocia la colonna dei test bidirezionali a $0.05$ (oppure una coda a $0.025$) con la riga $df = 10$.
* **Soglia critica $t_c = \pm 2.228$**.

> **Riassunto operativo per il tuo formulario:**
> Per calcolare la soglia critica devi isolare geometricamente l'area $\alpha$ (o $\alpha/2$) all'estremo della curva. Per farlo usi la funzione inversa della tua distribuzione, inserendo come input i gradi di libertà (se richiesti) e l'area della coda desiderata.
    

### Errori e Potenza

- **Errore Tipo I ($\alpha$):** Rifiutare $H_0$ quando è vera (Significatività).
    
- **Errore Tipo II ($\beta$):** Non rifiutare $H_0$ quando è falsa.
    
- **Potenza del Test ($1-\beta$):** Capacità del test di rifiutare correttamente $H_0$ quando la verità è in $H_a$.

- **Relazione tra $\alpha$ e $\beta$:** Sono inversamente proporzionali; non è possibile minimizzarli entrambi simultaneamente.

---

## 6. Linear Regression

### Definizione del Modello

Il modello di regressione lineare esprime la variabile risposta $Y$ come somma di una componente sistematica (predittore lineare) e una componente d'errore casuale $\epsilon$.

*   **Modello Teorico (Unità $i$):** $Y_i = \beta_0 + \beta_1 x_{i1} + \dots + \beta_p x_{ip} + \epsilon_i$.
*   **Formulazione Matriciale:** $\mathbf{Y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\epsilon}$.
    *   $\mathbf{Y}$: Vettore delle risposte ($n \times 1$).
    *   $\mathbf{X}$: Matrice del disegno ($n \times (p+1)$), con la prima colonna di 1 per l'intercetta.
    *   $\boldsymbol{\beta}$: Vettore dei parametri ($ (p+1) \times 1$).
    *   $\boldsymbol{\epsilon}$: Vettore degli errori casuali.

### Assunzioni del Modello (Gauss-Markov)
Perché il modello sia valido, si assumono le seguenti proprietà per gli errori $\epsilon_i$:
1.  **Media nulla:** $E[\epsilon_i] = 0$ per ogni $i$.
2.  **Omoschedasticità:** $Var(\epsilon_i) = \sigma^2$ (varianza costante per tutte le unità).
3.  **Assenza di correlazione:** $Cov(\epsilon_i, \epsilon_j) = 0$ per $i \neq j$.
4.  **Normalità (per l'inferenza):** $\epsilon \sim N(\mathbf{0}, \sigma^2\mathbf{I})$.

**Conseguenze sulla risposta $Y_i$:** $E[Y_i] = \mathbf{x}'_i\boldsymbol{\beta}$ e $Var(Y_i) = \sigma^2$.

### Interpretazione dei Parametri
*   **Intercetta ($\beta_0$):** Valore atteso di $Y$ quando tutti i predittori $x_k$ sono uguali a zero (interpretazione pratica solo se lo zero ha senso nel contesto).
*   **Coefficiente parziale ($\beta_k$):** Variazione attesa nel valore medio di $Y$ per un aumento unitario di $x_k$, mantenendo costanti tutti gli altri predittori.

### Variabili Categoriche e Dummy
Se un predittore è qualitativo con $k$ categorie, si utilizzano **$k-1$ variabili dummy** (valori 0 o 1).
*   Una categoria viene scelta come **riferimento** (tutte le dummy a 0).
*   Il coefficiente della dummy rappresenta la differenza nella risposta media rispetto alla categoria di riferimento.

### Stima dei Parametri ($\hat{\beta}$)
I parametri vengono stimati con il metodo dei **Minimi Quadrati Ordinari (OLS)** o di **Massima Verosimiglianza (MLE)**, che portano allo stesso risultato sotto l'assunzione di normalità.

*   **Equazioni Normali:** $(\mathbf{X}'\mathbf{X})\hat{\boldsymbol{\beta}} = \mathbf{X}'\mathbf{Y}$.
*   **Stimatore OLS:** $\hat{\boldsymbol{\beta}} = (\mathbf{X}'\mathbf{X})^{-1}\mathbf{X}'\mathbf{Y}$.
*   **Valori Adattati (Fitted):** $\hat{\mathbf{y}} = \mathbf{X}\hat{\boldsymbol{\beta}}$.
*   **Residui:** $u_i = y_i - \hat{y}_i$.

### Proprietà degli Stimatori
*   **Non distorsione:** $E[\hat{\boldsymbol{\beta}}] = \boldsymbol{\beta}$.
*   **Matrice di Covarianza:** $Cov(\hat{\boldsymbol{\beta}}) = \sigma^2(\mathbf{X}'\mathbf{X})^{-1}$.
    *   La varianza del singolo coefficiente $\hat{\beta}_k$ è $\sigma^2 h_{kk}$, dove $h_{kk}$ è l'elemento diagonale della matrice $(\mathbf{X}'\mathbf{X})^{-1}$.

### Analisi della Varianza e Bontà di Adattamento
La variabilità totale di $Y$ ($SST$) viene scomposta in quota spiegata dal modello ($SSR$) e quota residua ($SSres$):
*   $SST = \sum (y_i - \bar{y})^2$
*   $SSR = \sum (\hat{y}_i - \bar{y})^2$
*   $SSres = \sum (y_i - \hat{y}_i)^2 = \mathbf{u}'\mathbf{u}$

**Indici di bontà:**
*   **Coefficiente di determinazione ($R^2$):** $R^2 = \frac{SSR}{SST} = 1 - \frac{SSres}{SST}$. Rappresenta la proporzione di variabilità di $Y$ spiegata dal modello.
*   **Stima della varianza dell'errore ($\hat{\sigma}^2$):** $\hat{\sigma}^2 = \frac{SSres}{n - p - 1}$.
*   **$R^2$ corretto (Adjusted $R^2$):** $\bar{R}^2 = 1 - \left( \frac{n-1}{n-p-1} \right)(1 - R^2)$. Penalizza l'aggiunta di predittori non necessari.

### Inferenza sui Parametri
#### Test t individuale (Significatività del singolo coefficiente)
**Ipotesi:**
$H_0: \beta_k = 0$ rispetto a $H_1: \beta_k \neq 0$

**Statistica Test:**
$$
T = \frac{\hat{\beta}_k}{\text{se}(\hat{\beta}_k)} \sim t_{n-p-1}
$$

dove l'errore standard è calcolato come:
$$
\text{se}(\hat{\beta}_k) = \sqrt{\hat{\sigma}^2 h_{kk}}
$$

**Decisione:**
Rifiuto $H_0$ se $|T| > t_{\alpha/2, n-p-1}$ oppure se il p-value $< \alpha$.

#### Test F globale (Validità del modello)
*   **Ipotesi:** $H_0: \beta_1 = \beta_2 = \dots = \beta_p = 0$ vs $H_1$: almeno un $\beta_k \neq 0$.
*   **Statistica Test:** $F = \frac{SSR / p}{SSres / (n - p - 1)} \sim F_{p, n-p-1}$.
*   **Significato:** Un valore di $F$ elevato indica che il modello ha un potere esplicativo significativo.
