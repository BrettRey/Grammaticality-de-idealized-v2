# Notes on Skyrms (2010) - Chapter 7: Learning

### 1. THE LAW OF EFFECT
*   **Thorndike's Law:** Responses accompanied by satisfaction are more likely to recur.
*   **The Approach:** Skyrms views reinforcement learning as a complement to belief learning, not an antagonist. He starts with simple reinforcement to see how far it gets us.

### 2. ROTH-EREV REINFORCEMENT
*   **The Model:**
    *   Agents have "urns" with balls representing actions.
    *   Probability of an act is proportional to the number of balls (accumulated rewards).
    *   **Law of Practice:** As rewards accumulate, the relative effect of each new reward diminishes. Learning slows down.
*   **Result:** In simple signaling games, Roth-Erev learners converge to a signaling system with probability 1 (proven by Beggs, 2005).

### 3. BUSH-MOSTELLER REINFORCEMENT
*   **The Model:** Probabilities are updated directly based on the current reward and a learning rate parameter. It does *not* slow down (no Law of Practice).
*   **Comparison:**
    *   **Too Cold:** Because it learns fast and doesn't slow down, Bush-Mosteller can freeze into suboptimal habits (like playing the wrong slot machine).
    *   **Too Hot:** Some models explore forever and never settle.
    *   **Goldilocks:** Roth-Erev is "just right" (explores enough, then settles).
*   **Surprise:** Despite theoretical flaws ("too cold"), simulations show Bush-Mosteller learners *do* learn to signal with very high probability (>99%) in standard games.

### 4. REINFORCEMENT AND EVOLUTION
*   **Mean-Field Dynamics:** The expected motion of a reinforcement learner often approximates the Replicator Dynamics (evolution).
*   **Conclusion:** Learning and Evolution are mathematically deeply intertwined. A single model often explains both.

### 5. BELIEF LEARNING
*   **Best Response:** Agents know the game structure and play the best response to the other's last move.
    *   *Problem:* Can get trapped in cycles (like "I think you'll go Left, so I go Right," "I think you'll go Right, so I go Left").
*   **Best Response with Inertia:** Agents usually repeat their last move, but occasionally best-respond.
    *   *Result:* This breaks the cycles and converges to signaling with probability 1.
*   **Simplicity:** "Best Response for all you know with inertia" requires minimal cognitive load (just remember what you did last time and occasionally try something else if it failed).

### 6. CONCLUSION
*   **It is Easy to Learn to Signal:** Whether using simple reinforcement (Roth-Erev, Bush-Mosteller) or simple belief learning (Best Response with Inertia), agents spontaneously learn to signal. High-level rationality is not required.
