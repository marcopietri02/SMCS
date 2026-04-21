Certamente! Per questo secondo **Mock Test**, ho inserito argomenti e formule che non erano stati approfonditi nel primo, come il **Teorema di Bayes**, la **Correlazione**, le **proprietà del Valore Atteso e della Varianza** (trasformazioni lineari) e il calcolo dei **percentili** della distribuzione Normale.

---

### **Statistical Methods for Computer Science**

#### **Mock Intermediate Test 2 (Versione Avanzata)**

**Nome e Cognome:** _______________________________________

**Numero di Matricola:** ____________________________________

---

**1. Statistica Descrittiva e Correlazione**

Si considerino i dati relativi a due variabili $X$ (ore di studio) e $Y$ (punteggio esame) misurate su un gruppo di studenti. Sono noti i seguenti indici sintetici:

- Varianza di $X$: $s_X^2 = 16$
    
- Varianza di $Y$: $s_Y^2 = 100$
    
- Covarianza tra $X$ e $Y$: $s_{XY} = 30$
    
- Quartili di $Y$: $Q_1 = 18$, $Q_3 = 27$
    

(a) Calcolare il coefficiente di correlazione lineare $r_{xy}$.

(b) Calcolare il Range Interquartile (IQR) per la variabile $Y$.

(c) Calcolare il Coefficiente di Variazione ($CV$) per la variabile $X$, sapendo che la media $\bar{x} = 10$.

**Risposte:**

(a) [ ____________________________ ]

(b) [ ____________________________ ]

(c) [ ____________________________ ]

---

**2. Probabilità e Teorema di Bayes**

Un sistema di rilevamento intrusioni (IDS) analizza il traffico di rete. Si sa che:

- Il $5\%$ del traffico totale è costituito da attacchi informatici ($A$).
    
- Se il traffico è un attacco, l'IDS genera un allarme ($S$) con probabilità $P(S|A) = 0.98$.
    
- Se il traffico è lecito ($\bar{A}$), l'IDS genera un falso allarme con probabilità $P(S|\bar{A}) = 0.04$.
    

(a) Calcolare la probabilità totale che l'IDS generi un allarme $P(S)$.

(b) Se l'IDS ha generato un allarme, qual è la probabilità che si tratti effettivamente di un attacco?

**Risposte:**

(a) [ ____________________________ ]

(b) [ ____________________________ ]

---

**3. Variabili Casuali e Proprietà Lineari**

Sia $X$ una variabile casuale discreta con la seguente distribuzione di probabilità:

$P(X=0) = 0.4$, $P(X=1) = 0.4$, $P(X=2) = 0.2$.

(a) Calcolare il valore atteso $E[X]$ e la varianza $V[X]$.

(b) Sia $Z = 5X - 2$ una trasformazione lineare di $X$. Calcolare $E[Z]$ e $V[Z]$ utilizzando le proprietà di linearità.

**Risposte:**

(a) $E[X] =$ [______] , $V[X] =$ [______]

(b) $E[Z] =$ [______] , $V[Z] =$ [______]

---

**4. Distribuzione Normale (Problema Inverso)**

Il tempo di risposta di un server segue una distribuzione Normale con media $\mu = 200$ ms e deviazione standard $\sigma = 40$ ms.

(a) Trovare il tempo di risposta $k$ tale che solo il $10\%$ delle richieste sia più lento di $k$ (ovvero il 90-esimo percentile).

(b) Qual è la probabilità che il tempo di risposta sia esattamente uguale a $200$ ms?

**Risposte:**

(a) [ ____________________________ ]

(b) [ ____________________________ ]

---

### **Soluzioni Sintetiche per l'Esercitazione**

1. **Statistica Descrittiva:**
    
    - (a) $r_{xy} = \frac{30}{\sqrt{16} \cdot \sqrt{100}} = \frac{30}{4 \cdot 10} = 0.75$
        
    - (b) $IQR = Q_3 - Q_1 = 27 - 18 = 9$
        
    - (c) $CV = \frac{s_X}{\bar{x}} = \frac{4}{10} = 0.4$ (o 40%)
        
2. **Bayes:**
    
    - (a) $P(S) = (0.98 \cdot 0.05) + (0.04 \cdot 0.95) = 0.049 + 0.038 = 0.087$
        
    - (b) $P(A|S) = \frac{0.049}{0.087} \approx 0.5632$
        
3. **V.C. Discrete:**
    
    - (a) $E[X] = 0.8$; $E[X^2] = 1.2 \implies V[X] = 1.2 - (0.8)^2 = 0.56$
        
    - (b) $E[5X-2] = 5(0.8) - 2 = 2$; $V[5X-2] = 5^2 \cdot V[X] = 25 \cdot 0.56 = 14$
        
4. **Normale:**
    
    - (a) Cerco $z$ tale che $\Phi(z) = 0.90 \implies z \approx 1.28$. Quindi $k = 200 + (1.28 \cdot 40) = 251.2$ ms
        
    - (b) $P(X = 200) = 0$ (per ogni v.c. continua, la probabilità in un punto è nulla)
        

---

### **Formule Aggiuntive per questo Test**

- **Correlazione:** $r_{xy} = \frac{s_{xy}}{s_x s_y}$
    
- **Linearità Valore Atteso:** $E[aX + b] = aE[X] + b$
    
- **Proprietà Varianza:** $V[aX + b] = a^2 V[X]$
    
- **Percentile Normale:** $x_p = \mu + z_p \cdot \sigma$
    
- **Bayes:** $P(A|B) = \frac{P(B|A)P(A)}{P(B)}$
