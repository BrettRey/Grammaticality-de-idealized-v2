# Notes on Skyrms (2010) - Chapter 8: Learning in Lewis Signaling Games

### 1. CAN WE LEARN TO SIGNAL?
*   **The Question:** What kind of learning allows signaling to emerge? Does it require high-level cognition?
*   **The Answer:** No. Simple reinforcement learning acts on **acts**, not strategies. Agents don't need to know they are in a "game."

### 2. ROTH-EREV LEARNING IN SIGNALING GAMES
*   **Setup:** Sender has urns for each state (balls = signals). Receiver has urns for each signal (balls = acts).
*   **Result:** They learn to signal with probability 1 in the simple (2-state/2-signal) case.
*   **Speed:** Learning is fast (80% success after 100 trials).
*   **Harder Cases:**
    *   **Unequal Probabilities:** If State 1 is 90% likely, simple reinforcement *can* get trapped in pooling (no signaling).
    *   **Crucial Parameter:** **Initial Weights**. If initial weights are low (meaning agents are easily swayed by early success), they avoid pooling and learn to signal even in the 90/10 case.

### 3. BUSH-MOSTELLER LEARNING
*   **Result:** Despite theoretical worries about being "too cold," Bush-Mosteller learners signal in >99.9% of trials in simple games.
*   **Unequal Probabilities:** Like Roth-Erev, if the learning parameter is tuned correctly, they can handle the 90/10 case.

### 4. EXPONENTIAL RESPONSE RULE
*   **Softmax:** Making choice probabilities proportional to `exp(weight)` rather than just `weight`.
*   **Result:** This helps avoid suboptimal equilibria. With low "temperature" (high randomness initially, cooling down), it always converges to signaling.

### 5. SPATIAL & NETWORK LEARNING
*   **Neural Nets (Grim et al.):** Spatially arranged agents with neural nets spontaneously evolve signaling.
*   **Imitation (Zollman):** Agents on a grid imitating successful neighbors evolve regional signaling dialects.
*   **Stag Hunt:** Pre-play signaling evolves to coordinate Stag Hunting (high payoff cooperation).
*   **Networks (Wagner):** "Small world" networks promote uniform signaling (one language) rather than dialects.

### 6. BELIEF LEARNING (REVISITED)
*   **Best Response:** In 2-state games, standard Best Response can cycle.
*   **Inertia:** Adding inertia (mostly repeat, sometimes switch) fixes the cycling.
*   **Best Response For All You Know:** In N-state games, if you fail, you don't know *which* act was right. You just know yours was wrong. Randomizing among the others (with inertia) guarantees convergence to signaling.

### 7. CONCLUSION
*   **Robustness:** Learning to signal is robust across many models (Reinforcement, Neural Nets, Imitation, Belief).
*   **Low Cognition:** None of these require "understanding" meaning or intent. Meaning emerges from the low-level dynamics.
