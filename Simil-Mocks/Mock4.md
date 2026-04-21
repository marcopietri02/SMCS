Ecco un quarto **Mock Test** che riprende e adatta esercizi specifici tratti direttamente dalle tue fonti (fogli di esercizi e slide), focalizzandosi su punti che spesso compaiono nei parziali ma che richiedono un ragionamento più approfondito.

---

### **Statistical Methods for Computer Science**

#### **Mock Intermediate Test 3 (Basato sulle fonti del corso)**

**Nome e Cognome:** _______________________________________

**Numero di Matricola:** ____________________________________

---

**1. Analisi della Distribuzione e Outliers**

Un ricercatore ha analizzato le spese mensili di un campione di 25 studenti per l'acquisto di libri. La spesa media risulta essere di $24.40$, mentre la mediana è di $21.76$. La deviazione standard è di $4.42$.

(a) Determina la forma della distribuzione (simmetrica, obliqua a destra o obliqua a sinistra) spiegandone il motivo in base ai parametri forniti.

(b) Calcola il **Coefficiente di Variazione (CV)**.

(c) Se il terzo quartile ($Q_3$) è $15.9$ e il primo quartile ($Q_1$) è $8.1$, una spesa di $30$ sarebbe considerata un outlier secondo la regola del box-plot ($1.5 \times IQR$)?

**Risposte:**

(a) [ ____________________________ ]

(b) [ ____________________________ ]

(c) [ ____________________________ ]

---

**2. Probabilità e Indipendenza di Eventi**

Un'impresa edile ha presentato due offerte per due progetti indipendenti, A e B. La probabilità di ottenere il progetto A è $0.60$. La probabilità di ottenere il progetto B è $0.75$. La probabilità di ottenere almeno uno dei due progetti è $0.85$.

(a) Calcola la probabilità che l'impresa ottenga entrambi i progetti ($P(A \cap B)$).

(b) Gli eventi "ottenere il progetto A" e "ottenere il progetto B" sono mutuamente esclusivi? Spiega perché.

(c) Dimostra, tramite calcolo, se i due eventi sono statisticamente indipendenti.

**Risposte:**

(a) [ ____________________________ ]

(b) [ ____________________________ ]

(c) [ ____________________________ ]

---

**3. Distribuzioni Discrete (Poisson)**

Una piattaforma di e-commerce riceve richieste di assistenza a un tasso medio di $1$ ogni $2$ minuti ($\lambda = 0.5$ richieste/min).

(a) Calcola la probabilità di non ricevere alcuna richiesta in un intervallo di $10$ minuti.

(b) Se il tasso di richieste raddoppia improvvisamente ($\lambda = 1$), qual è la probabilità di ricevere esattamente $2$ richieste in un minuto?

**Risposte:**

(a) [ ____________________________ ]

(b) [ ____________________________ ]

---

**4. Variabili Casuali Continue e Somma di Normali**

Un'azienda ha due canali di vendita indipendenti. Le vendite mensili del canale $X$ (fisico) sono normali con $\mu_X = 100,000$ e $\sigma_X = 12,000$. Le vendite del canale $Y$ (online) sono normali con $\mu_Y = 240,000$ e $\sigma_Y = 25,000$. Sia $W = X + Y$ la vendita totale mensile.

(a) Calcola il valore atteso $E[W]$ e la deviazione standard $\sigma_W$ delle vendite totali.

(b) Qual è la probabilità che le vendite totali $W$ superino quota $350,000$?

**Risposte:**

(a) $E[W] =$ [______] , $\sigma_W =$ [______]

(b) [ ____________________________ ]

---

### **Soluzioni Commentate**

1. **Analisi Dati:**
    
    - (a) **Obliqua a destra (skewed to the right)** perché la Media ($24.40$) > Mediana ($21.76$).
        
    - (b) $CV = (\sigma / \bar{x}) \times 100 = (4.42 / 24.40) \times 100 \approx 18.11\%$.
        
    - (c) $IQR = 15.9 - 8.1 = 7.8$. Limite superiore $= Q_3 + 1.5(IQR) = 15.9 + 11.7 = 27.6$. Sì, $30$ è un **outlier** perché $30 > 27.6$.
        
2. **Probabilità:**
    
    - (a) $P(A \cap B) = P(A) + P(B) - P(A \cup B) = 0.60 + 0.75 - 0.85 = 0.50$.
        
    - (b) **No**, perché $P(A \cap B) = 0.50 \neq 0$.
        
    - (c) **No**, non sono indipendenti perché $P(A) \cdot P(B) = 0.60 \cdot 0.75 = 0.45$, che è diverso da $P(A \cap B) = 0.50$.
        
3. **Poisson:**
    
    - (a) In $10$ min, il nuovo $\lambda_{10} = 0.5 \cdot 10 = 5$. $P(X=0) = \frac{e^{-5} \cdot 5^0}{0!} = e^{-5} \approx 0.0067$ ($0.67\%$).
        
    - (b) Con $\lambda=1$, $P(X=2) = \frac{e^{-1} \cdot 1^2}{2!} = \frac{0.3678}{2} \approx 0.1839$.
        
4. **Normali:**
    
    - (a) $E[W] = 100,000 + 240,000 = 340,000$. Siccome sono indipendenti, $V[W] = \sigma_X^2 + \sigma_Y^2 = 12,000^2 + 25,000^2 = 769,000,000$. Quindi $\sigma_W = \sqrt{769,000,000} \approx 27,730.85$.
        
    - (b) Standardizzazione: $Z = \frac{350,000 - 340,000}{27,730.85} \approx 0.36$. $P(W > 350,000) = P(Z > 0.36) = 1 - \Phi(0.36) \approx 1 - 0.6406 = 0.3594$.
