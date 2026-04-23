# Mock Test 1: Statistica Descrittiva e Probabilità

Il presente documento costituisce una guida di esercitazione per i temi di Statistica Descrittiva e Calcolo delle Probabilità. Il test è strutturato per simulare la complessità e il rigore richiesti negli esami universitari per le Scienze Informatiche, integrando scenari applicativi con dati derivati dalle fonti di riferimento.

---

### 1. Sezione I: Statistica Descrittiva (Dati Raggruppati in Classi)

Un team di ingegneri del software ha analizzato i tempi di esecuzione di una query (in millisecondi) su un campione di 10 istanze. I dati grezzi, derivati dal dataset "Income" scalato per il contesto informatico, sono i seguenti: 16, 18, 26, 16, 34, 22, 42, 42, 16, 20.

I dati sono stati raggruppati nella seguente tabella di frequenza:

| Tempo di esecuzione (Y) in ms | Frequenza Assoluta ($f_i$) | Valore Centrale ($y_i$) |
|---|---|---|
| $[10, 20)$ | 4 | 15 |
| $[20, 30)$ | 3 | 25 |
| $[30, 40)$ | 1 | 35 |
| $[40, 50]$ | 2 | 45 |
| **Totale** | **10** | |

**Richieste:**

1. Calcolare la **media campionaria** ($\bar{Y}$) utilizzando i valori centrali di ciascuna classe.
2. Determinare la **mediana** approssimata per dati raggruppati.
3. Calcolare la **deviazione standard campionaria** ($s$).

---

### 2. Sezione II: Calcolo delle Probabilità e Indipendenza

In un'infrastruttura cloud, vengono effettuati test di disponibilità su 3 server. Lo spazio campionario $\Omega$ è definito dalle terne di esiti (S = Successo/Attivo, F = Fallimento/Inattivo). Si assuma che ogni esito elementare sia equiprobabile.

Si definiscano i seguenti eventi:

- $A$: "Il primo server testato fallisce".
- $B$: "Almeno due server su tre sono attivi (Successo)".

**Richieste:**

1. Elencare gli elementi degli eventi $A$ e $B$ all'interno dello spazio campionario $\Omega$.
2. Calcolare $P(A \cap B)$ e $P(A \cup B)$ utilizzando la definizione classica di probabilità.
3. Dimostrare, tramite il calcolo delle probabilità, se gli eventi $A$ e $B$ siano **indipendenti** e se siano **mutuamente esclusivi**, esplicitando la differenza teorica tra i due concetti.

---

### 3. Sezione III: Variabili Aleatorie Bivariate

Un'analisi sulla qualità del codice correla il linguaggio di programmazione utilizzato con la rilevazione di bug critici. La seguente tabella riporta le probabilità congiunte:

| Presenza di Bug / Linguaggio | Java ($L_1$) | Python ($L_2$) | C++ ($L_3$) |
|---|---|---|---|
| **Sì ($B$)** | 0.08 | 0.05 | 0.07 |
| **No ($\bar{B}$)** | 0.32 | 0.35 | 0.13 |

**Richieste:**

1. Calcolare le **probabilità marginali** per i tre linguaggi ($P(L_1)$, $P(L_2)$, $P(L_3)$) e per la presenza di bug ($P(B)$, $P(\bar{B})$).
2. Calcolare la probabilità condizionata che un modulo contenga un bug dato che è scritto in Python ($P(B \mid L_2)$).
3. Utilizzando la **Formula di Bayes**, calcolare la probabilità che un modulo sia scritto in Java, sapendo che è stato rilevato un bug ($P(L_1 \mid B)$).

---

### 4. Sezione IV: Distribuzioni Discrete (Binomiale e Poisson)

**Esercizio A (Distribuzione Binomiale):** Un sistema di rilevamento intrusioni (IDS) ha una probabilità $p = 0.15$ di generare un falso positivo per ogni pacchetto analizzato. Se il sistema riceve un blocco di $n = 8$ pacchetti indipendenti, calcolare la probabilità che si verifichino **esattamente 2** falsi positivi.

**Esercizio B (Distribuzione di Poisson):** In una rete ad alta velocità, il tasso medio di pacchetti persi è $\lambda = 3$ pacchetti al secondo. Calcolare la probabilità che, in un intervallo di un secondo, vengano persi **esattamente 4** pacchetti.

---

### 5. Sezione V: Distribuzione Normale e Standardizzazione

Il tempo di risposta di un server per una richiesta API segue una distribuzione normale con media $\mu = 50$ ms e deviazione standard $\sigma = 10$ ms. Si indichi la variabile come $X \sim N(50,\, 10^2)$.

**Richieste:**

1. Calcolare la probabilità che una richiesta richieda più di 65 ms, mostrando il processo di **standardizzazione** verso la variabile $Z$.
2. Trovare il valore $k$ (90° percentile) tale che la probabilità di un tempo di risposta inferiore a $k$ sia pari a 0.90 ($P(X < k) = 0.90$).
3. **Quesito teorico:** Perché è utile trasformare una distribuzione normale generica in una normale standard $Z \sim N(0, 1)$? (Riferimento: Quesito 12 delle fonti).

---

### 6. Appendice: Soluzioni Sintetiche

- **Sezione I:**
  - **Media campionaria:** $\bar{Y} = 26.0000$ ms. Calcolo:

$$\bar{Y} = \frac{(15 \cdot 4) + (25 \cdot 3) + (35 \cdot 1) + (45 \cdot 2)}{10} = \frac{260}{10} = 26$$

  - **Mediana:** $\approx 23.3333$ ms. (Classe mediana $[20, 30)$).
  - **Deviazione standard:**

$$s \approx 11.9722 \text{ ms}, \quad s = \sqrt{\frac{\sum f_i(y_i - \bar{Y})^2}{N-1}} > \sqrt{\frac{1290}{9}}$$

- **Sezione II:**
  - $A = \{FSS,\, FSF,\, FFS,\, FFF\}$; $B = \{SSS,\, SSF,\, SFS,\, FSS\}$.
  - $P(A \cap B) = 0.1250$ (Solo l'esito $\{FSS\}$ soddisfa entrambi).
  - $P(A \cup B) = 0.8750$.
  - **Indipendenza:** $A$ e $B$ **non sono indipendenti** poiché $P(A \cap B) = 0.1250 \neq P(A) \cdot P(B) = 0.2500$.
  - **Mutua Esclusività:** Gli eventi **non sono mutuamente esclusivi** perché $A \cap B \neq \emptyset$. La mutua esclusività implica che il verificarsi di un evento impedisca l'altro; l'indipendenza riguarda invece l'assenza di influenza informativa sulla probabilità.

- **Sezione III:**
  - **Marginali:** $P(L_1)=0.4000$, $P(L_2)=0.4000$, $P(L_3)=0.2000$; $P(B)=0.2000$, $P(\bar{B})=0.8000$.

$$P(B \mid L_2) = \frac{0.05}{0.40} = 0.1250$$

  - **Bayes:**

$$P(L_1 \mid B) = \frac{P(B \mid L_1) \cdot P(L_1)}{P(B)} = \frac{0.08}{0.20} = 0.4000$$

- **Sezione IV:**
  - **Binomiale:**

$$P(X=2) = \binom{8}{2}(0.15)^2(0.85)a6 \approx 0.2376$$

  - **Poisson:**

$$P(X=4) = \frac{e^{-3} \cdot 3^4}{4!} \approx 0.1680$$

- **Sezione V:**
  - $P(X > 65) = P\!\left(Z > \frac{65-50}{10}\right) = P(Z > 1.5) \approx 0.0668$.
  - **90° Percentile:** $k \approx 62.8200$ ms, utilizzando $z_{0.90} \approx 1.282$:

$$k = \mu + z_{0.90} \cdot \sigma = 50 + 1.282 \cdot 10 = 62.82 \text{ ms}$$

  - **Nota teorica:** La standardizzazione permette di confrontare diverse distribuzioni normali e utilizzare tavole statistiche universali poiché ogni $X \sim N(\mu, \sigma^2)$ può essere mappata su $Z \sim N(0, 1)$ tramite:

$$Z = \frac{X - \mu}{\sigma}$$
