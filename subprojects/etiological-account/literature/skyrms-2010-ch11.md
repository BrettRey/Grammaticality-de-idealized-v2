# Notes on Skyrms (2010) - Chapter 11: Networks I - Logic and Information Processing

### 1. LOGIC FROM SIGNALS
*   **The Goal:** Can logical inference (e.g., "P or Q", "Not P", therefore "Q") evolve from signaling?
*   **Proto-Truth Functions:** Signals that mean "Leopard OR Snake."
*   **Multiple Senders:** If one sender says "Leopard OR Snake" and another says "No Leopard," the receiver should infer "Snake."

### 2. INVENTING THE CODE (XOR PROBLEM)
*   **Scenario:** 4 States.
    *   Sender 1 sees partition {{1,2}, {3,4}} (e.g., P or Not P).
    *   Sender 2 sees partition {{1,3}, {2,4}} (e.g., Q or Not Q).
*   **The Task:** Receiver needs to do Act 1 if (P XOR Q) is true, Act 2 if false. This requires integrating partial information.
*   **Result:** Reinforcement learning solves this. Senders learn to signal their partial observation, and the Receiver learns the logical combination (Acts as an XOR gate).

### 3. INVENTING CATEGORIES
*   **Barrett's Model:** Senders see the exact state but have *too few signals* (bottleneck). They must invent categories to compress info.
*   **Result:** Senders spontaneously categorize the world in complementary ways so the Receiver can reconstruct the truth. (e.g., Sender 1 groups States 1&4, Sender 2 groups 1&3. Intersection identifies State 1).

### 4. ERROR CORRECTION (CONDORCET JURY)
*   **Scenario:** Multiple senders observe the state with error.
*   **Voting:** The Receiver evolves to take a "majority vote" of the signals.
*   **Condorcet Theorem:** With enough senders, error goes to zero. Reinforcement learning discovers this "Condorcet Signaling System."

### 5. CHRYSIPPUS' DOG
*   **The Ancient Debate:** Does a dog who sniffs two paths and runs down the third *reason* (Disjunctive Syllogism: A or B or C; Not A; Not B; therefore C)?
*   **Skyrms's Answer:** Yes, in the sense of information processing. The dog integrates signals from nose and eyes to produce the correct act. Logic *is* information processing, and it evolves.
