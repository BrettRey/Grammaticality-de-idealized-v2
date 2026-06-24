# Notes on Skyrms (2010) - Chapter 10: Inventing New Signals

### 1. THE ORIGIN OF NEW SIGNALS
*   **The Limitation:** Previous chapters assumed a fixed set of signals. How do new ones arise?
*   **Biological Invention:** Bacteria (*Vibrio fisheri*) modified a basic signaling molecule (AHL) for different uses (quorum sensing, virulence).
*   **Cultural Invention:** Vervet monkeys in Cameroon invented a new, quiet alarm call for "dog/hunter" to avoid being shot (unlike the loud "leopard" call).

### 2. THE CHINESE RESTAURANT PROCESS (HOPPE URN)
*   **The Metaphor:** An infinite restaurant. New guests sit at an occupied table with probability proportional to the number of people already there, or start a new table with probability proportional to a parameter (the "phantom guest").
*   **Mathematical Properties:**
    *   Generates a partition of guests into tables.
    *   "Rich get richer": Large tables (common signals) attract more guests.
    *   **Hoppe Urn:** A Polya urn (balls return with a copy) plus a "mutator" ball. If the mutator is drawn, a ball of a *new color* is added.

### 3. REINFORCEMENT WITH INVENTION
*   **The Model:** Senders can choose an existing signal or try a "new" one (invention).
    *   If the new signal succeeds, it is added to the urn (reinforced).
    *   If it fails, the system reverts.
*   **Dynamics:**
    *   **Avoiding Pooling:** In games where standard reinforcement gets trapped in "pooling" (no info), invention allows agents to break out. (e.g., the 90/10 probability case).
    *   **Synonyms:** The process naturally generates many synonyms (multiple signals for the same state).
    *   **Power Law:** A few signals do most of the work; many others are rare synonyms.

### 4. FORGETTING
*   **Noisy Forgetting:** To keep the number of signals manageable, we add "forgetting" (balls are randomly removed from urns).
*   **Result:** This prunes unused signals. The system tends to converge to the minimum number of signals needed for efficiency (eliminating excess synonyms).

### 5. CONCLUSION
*   Simple reinforcement learning, augmented with a mechanism for invention (Hoppe urn) and forgetting, explains how signaling systems can expand to meet communicative needs and avoid suboptimal traps.
