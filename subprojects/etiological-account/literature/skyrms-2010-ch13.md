# Notes on Skyrms (2010) - Chapter 13: Networks II - Teamwork

### 1. COOPERATIVE HUNTING (TEAMWORK)
*   **Examples:** Grouper and Moray Eel (Grouper signals Eel to enter crevice); Lions (Wings and Centers); Bacterial swarming.
*   **Requirement:** Teamwork requires coordination, often achieved by signaling.

### 2. QUORUM SENSING (POSITIVE FEEDBACK)
*   **The Problem:** Bacteria need to switch a gene ON if enough friends are present, OFF otherwise. But the signal (chemical concentration) is continuous and noisy.
*   **Solution:** **Positive Feedback**. The signal is an "autoinducer"—receiving it makes you produce more. This creates a robust bi-stable switch (snap ON, snap OFF) rather than a useless flicker.

### 3. HOMEOSTASIS
*   **Scenario:** State is Too Hot, Too Cold, or Just Right.
*   **Dynamics:** Reinforcement learning easily evolves a homeostatic signaling system (Sender says "Hot" -> Receiver turns heat down).

### 4. DIALOGUE (TWO-WAY SIGNALING)
*   **Scenario:** Receiver has different decision problems (needs to know different things).
*   **Dialogue:**
    1.  Receiver signals *which problem* it is (e.g., "I need to know color").
    2.  Sender observes the relevant partition (looks at color).
    3.  Sender signals the state ("Red").
    4.  Receiver acts.
*   **Result:** Reinforcement learning solves this, though it is slow. It's faster if the sender already has "names" for the attributes.

### 5. TEAM LEADER (CORRELATED EQUILIBRIUM)
*   **Coordination Problems (e.g., Hawk-Dove):** Two players want to avoid fighting (Hawk-Hawk) but prefer different equilibria (I play Hawk, you play Dove).
*   **Signal as Choreographer:** A Sender observes a random event (coin flip) and tells Player 1 "Play Hawk" and Player 2 "Play Dove."
*   **Correlated Equilibrium:** Both players obey because if they know the other is obeying, it is their best response.
*   **Result:** A "Team Leader" (sender) can evolve to coordinate the group, resolving conflicts and improving efficiency.
