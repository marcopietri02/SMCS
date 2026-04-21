Certamente! Ecco un nuovo **Mock Test** per il primo parziale di statistica, strutturato seguendo fedelmente il formato e la difficoltà del documento fornito. Gli esercizi coprono gli argomenti che vanno dalla statistica descrittiva alla distribuzione normale.

---

### **Statistical Methods for Computer Science**

#### **Mock Intermediate Test 1 (Versione di Esercitazione)**

**Nome e Cognome:** _______________________________________

**Numero di Matricola:** ____________________________________

---

**1. La durata $X$ (in giorni) di un componente elettronico su una popolazione di 500 unità è caratterizzata dalla seguente distribuzione di frequenza:**

|**Durata**|**(0−10]**|**(10−20]**|**(20−30]**|**(30−40]**|
|---|---|---|---|---|
|**Freq.**|80|120|200|100|

**Assumendo l'equidistribuzione all'interno delle classi:**

(a) Calcolare la durata media.

(b) Calcolare la durata mediana.

(c) Calcolare la deviazione standard della durata.

**Risposte:**

(a) [ ____________________________ ]

(b) [ ____________________________ ]

(c) [ ____________________________ ]

---

**2. La seguente tabella mostra la distribuzione di probabilità congiunta di due variabili casuali discrete $X$ e $Y$:**

|**Y∖X**|**1**|**2**|
|---|---|---|
|**0**|$0.05$|$0.20$|
|**1**|$0.15$|$0.30$|
|**2**|$0.10$|$0.20$|

(a) Trovare il valore atteso di $X$.

(b) Calcolare la probabilità condizionata $P[Y=1 \mid X=1]$.

**Risposte:**

(a) [ ____________________________ ]

(b) [ ____________________________ ]

---

**3. Il numero di chiamate che arrivano a un help desk in un'ora segue una distribuzione di Poisson con un valore atteso $\lambda = 1.2$:**

(a) Calcolare la probabilità di ricevere almeno due chiamate in un'ora.

(b) Considerando 4 ore indipendenti tra loro, calcolare la probabilità che in esattamente 2 di queste ore si ricevano almeno due chiamate.

**Risposte:**

(a) [ ____________________________ ]

(b) [ ____________________________ ]

---

**4. Il peso di una confezione di cereali segue una distribuzione Normale con media $\mu = 500$ grammi e deviazione standard $\sigma = 10$ grammi:**

(a) Calcolare la probabilità che una confezione pesi più di $515$ grammi.

(b) Calcolare la probabilità che una confezione pesi tra $490$ e $510$ grammi.

**Risposte:**

(a) [ ____________________________ ]

(b) [ ____________________________ ]

---

### **Soluzioni sintetiche**

1. **Statistica Descrittiva:**
    
    - (a) **Media**: $\bar{x} = 21.4$
        
    - (b) **Mediana**: $Me = 22.5$
        
    - (c) **Deviazione Standard**: $\sigma \approx 9.749$
        
2. **Variabili Casuali Bivariate:**
    
    - (a) $E[X] = 1(0.30) + 2(0.70) = 1.70$
        
    - (b) $P[Y=1 \mid X=1] = 0.15 / 0.30 = 0.5$
        
3. **Distribuzioni Discrete:**
    
    - (a) $P(X \ge 2) = 1 - P(X=0) - P(X=1) \approx 0.3374$
        
    - (b) Distribuzione Binomiale con $n=4, p=0.3374 \implies P(K=2) \approx 0.2997$
        
4. **Distribuzione Normale:**
    
    - (a) $P(Z > 1.5) = 1 - \Phi(1.5) \approx 0.0668$
        
    - (b) $P(-1 < Z < 1) = \Phi(1) - \Phi(-1) \approx 0.6826$
        

---

### **Formulario (Famiglie Parametriche)**

| **Distribuzione** | **Supporto**    | **pX​(x) o fX​(x)**                                                   | **E[X]**    | **V[X]**         |
| ----------------- | --------------- | --------------------------------------------------------------------- | ----------- | ---------------- |
| **Binomiale**     | $\{0,1,...,n\}$ | $\binom{n}{x}p^x(1-p)^{n-x}$                                          | $n \cdot p$ | $n \cdot p(1-p)$ |
| **Poisson**       | $\{0,1,...\}$   | $e^{-\lambda} \frac{\lambda^x}{x!}$                                   | $\lambda$   | $\lambda$        |
| **Normale**       | $\mathbb{R}$    | $\frac{1}{\sqrt{2\pi\sigma^2}} \exp\{-\frac{1}{2\sigma^2}(x-\mu)^2\}$ | $\mu$       | $\sigma^2$       |
