Ecco un nuovo **Mock Test** che esplora aspetti e formule diverse rispetto al precedente, integrando concetti come il coefficiente di variazione, il Teorema di Bayes, la covarianza tra variabili aleatorie e l'approssimazione della distribuzione binomiale alla normale.

---

# Statistical Methods for Computer Science - Mock Test 3

### 1. Statistica Descrittiva: Confronto e Volatilità (5 punti)

Si hanno i tempi di risposta (in ms) di due diversi server misurati su 10 campioni:

- **Server A:** Media $\bar{x}_A = 120$, Deviazione standard $s_A = 15$.
- **Server B:** Media $\bar{x}_B = 80$, Deviazione standard $s_B = 12$.

(a) Calcolare il **Coefficiente di Variazione (CV)** per entrambi i server. (b) Sulla base del CV, determinare quale dei due server presenta una maggiore variabilità relativa (più "volatilità"). (c) Se si aggiungesse una latenza fissa di 10 ms a tutti i tempi del Server A, come cambierebbe la sua deviazione standard?.

**Risposte:** (a) $CV_A$: [ ], $CV_B$: [ ] (b) [ ] (c) [ ]

---

### 2. Probabilità e Teorema di Bayes (5 punti)

In una rete aziendale, il 2% dei pacchetti dati è considerato "malevolo" ($M$). Un sistema di rilevamento (IDS) emette un allarme ($A$) con le seguenti probabilità condizionate:

- $P(A \mid M) = 0.95$ (Probabilità di allarme se il pacchetto è malevolo).
- $P(A \mid M^c) = 0.05$ (Probabilità di falso allarme se il pacchetto è lecito).

(a) Calcolare la probabilità marginale di avere un allarme, $P(A)$. (b) Utilizzare il **Teorema di Bayes** per trovare la probabilità che un pacchetto sia effettivamente malevolo dato che il sistema ha emesso un allarme: $P(M \mid A)$.

**Risposte:** (a) [ ] (b) [ ]

---

### 3. Variabili Aleatorie e Combinazioni Lineari (5 punti)

Siano $X$ e $Y$ due variabili aleatorie discrete con la seguente distribuzione congiunta:

|$Y \setminus X$|**1**|**2**|
|:--|:-:|:-:|
|**1**|0.20|0.30|
|**2**|0.40|0.10|

(a) Calcolare la **covarianza** $Cov(X, Y)$ utilizzando la formula $E[XY] - E[X]E[Y]$. (b) Sia $W = 2X + 3Y$. Calcolare il valore atteso $E[W]$ e la varianza $V[W]$. _(Nota: $V[aX + bY] = a^2 V[X] + b^2 V[Y] + 2ab Cov(X,Y)$)_.

**Risposte:** (a) [ ] (b) $E[W]$: [ ], $V[W]$: [ ]

---

### 4. Distribuzione Normale: Approssimazione (5 punti)

Un software di test esegue 400 controlli indipendenti su un codice. Ogni controllo ha una probabilità $p = 0.10$ di trovare un errore. (a) Verificare se è possibile approssimare la distribuzione del numero totale di errori con una **Normale** (condizione $npq \ge 10$). (b) Usando l'approssimazione normale, calcolare la probabilità che il numero di errori sia **maggiore di 50**. _(Utilizzare $\mu = np$ e $\sigma^2 = npq$. Si standardizzi in $Z = \frac{X - \mu}{\sigma}$)_.

**Risposte:** (a) [ ] (b) [ ]

---

## Formulario Aggiuntivo

- **Coefficiente di Variazione (CV):** $CV = \frac{s}{\bar{x}} \times 100%$.
- **Combinazione Lineare (Media):** $E[aX + bY] = a E[X] + b E[Y]$.
- **Covarianza:** $Cov(X, Y) = \sum \sum (x_i - \mu_X)(y_j - \mu_Y) p(x_i, y_j)$.
- **Approssimazione Normale:** Se $X \sim Bi(n, p)$, allora $X \approx N(np, npq)$.

---

Ho anche creato un **nuovo report** nella scheda Studio che contiene questo test in formato Markdown, pronto per essere copiato o scaricato come desideravi.
