# Notes on Skyrms (2010) - Chapter 9: Generalizing Signaling Games

### 1. BEYOND SYMMETRY
*   **The Issue:** Standard models assume equal numbers of States, Signals, and Acts. Real life is messier.
*   **Mismatches:** Too many signals (Synonyms), too few signals (Bottlenecks), or many states mapping to few acts (Categorization).

### 2. MANY STATES (CATEGORIZATION)
*   **Scenario:** 3 States, but only 2 Acts.
    *   *Case A:* Act 1 is right for State 1 *and* State 3. Act 2 is right for State 2.
    *   *Result:* The signaling system evolves to partition the world: Signal A = "State 1 or 3", Signal B = "State 2".
    *   **Implication:** Signals naturally evolve to form **categories** based on *pragmatic* needs (what acts are available/valuable).
    *   *Case B:* Act 1 is right for State 1, Act 2 for State 2, but *neither* is good for State 3 (e.g., predator eats you anyway).
    *   *Result:* No stable strategy for State 3. The system is "structurally unstable."

### 3. MANY SIGNALS (SYNONYMS)
*   **Scenario:** 2 States, 3 Signals.
*   **Result:** **Synonyms** evolve. One state might be indicated by Signal 1 *or* Signal 2 (randomly).
    *   *Dynamics:* Reinforcement learning does *not* eliminate synonyms (contrary to intuition). Synonyms persist because once established, both work equally well.
    *   *Connectivity:* The set of equilibria forms a connected component. You can drift from one synonym system to another.

### 4. FEW SIGNALS (BOTTLENECKS)
*   **Scenario:** 3 States, but only 2 Signals.
*   **Result:** Efficient and Inefficient solutions exist.
    *   *Efficient:* Pool the two states that require the most similar acts or have the lowest cost of error.
    *   *Inefficient:* Pool states that lead to high costs.
    *   *Problem:* Evolutionary dynamics can sometimes get trapped in the inefficient solution. The categorization system that evolves is not always optimal.

### 5. SYSTEMS OF CATEGORIES
*   **Hierarchical Signals:** Skyrms introduces a model where senders see "coarse" or "fine" partitions of the world (e.g., "Predator" vs. "Aerial Predator").
*   **Proto-Logic:** Signals can evolve to represent logical relationships (e.g., Signal X = "State 1 or 2", Signal Y = "State 3").
*   **Conclusion:** The logic of categories is driven by the pragmatics of action. Evolution constructs the categories we use to think.
