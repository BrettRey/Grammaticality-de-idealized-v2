# Notes on Skyrms (2010) - Chapter 3: Information

### 1. EPISTEMOLOGY AS INFORMATION FLOW
*   **Dretske's View:** Epistemology should study the flow of information, not just justify beliefs against skepticism. Skyrms agrees but rejects Dretske's move to "propositional" content.

### 2. QUANTITY VS. CONTENT
*   **Quantity:** How *much* does a signal move probabilities? (Measured in bits, Kullback-Leibler distance).
*   **Content:** In *which direction* does a signal move probabilities? (A vector).
    *   *Example:* Signal A moves probability of State 1 from 0.5 to 0.9. Signal B moves it from 0.5 to 0.1. They have the same *quantity* of information but different *content*.

### 3. TWO KINDS OF INFORMATION
In a signaling game, a signal carries two types of information simultaneously:
1.  **Information about the State:** (From Sender to Receiver). How much the signal changes the probability of the State.
2.  **Information about the Act:** (From Receiver to Sender). How much the signal changes the probability of the Receiver's Action.
    *   These need not be identical (e.g., if the receiver ignores the signal, there is info about state but none about act).

### 4. CREATION OF INFORMATION
*   **Ex Nihilo:** Evolution/learning can create information where none existed. In the beginning of a simulation, signals are random (zero information). As the system converges to a signaling equilibrium, information "appears" because the correlation between signal and state/act is established.

### 5. INFORMATIONAL CONTENT AS A VECTOR
*   Skyrms defines informational content as a **vector** of log-odds ratios for each possible state.
*   **Propositional Content:** This is a special case. A proposition like "The state is {1, 2}" corresponds to a vector where the components for states 3 and 4 are negative infinity (impossible).
*   **Richness:** The vector account is richer; it captures probabilistic information ("State 1 is likely") that standard propositional logic misses.

### 6. INTENTIONALITY
*   **Not Required:** Skyrms argues we don't need "intentionality" (mental directedness) to define information. Information is objective correlation.
*   **Subjective Information:** If agents *do* have mental states (subjective probabilities), we can model that as "subjective information," but it's an add-on, not the foundation.

### 7. INFORMATION FLOW IN NETWORKS
*   **Chains (Sender -> Intermediary -> Receiver):** Reinforcement learning can establish signaling chains.
*   **Translation:** If Sender and Receiver speak different "languages" (different signal-state mappings), an Intermediary can learn to act as a Translator, preserving the flow of information.
*   **Conclusion:** Signaling networks process and transmit information. Logic and inference are just special cases of this information flow.
