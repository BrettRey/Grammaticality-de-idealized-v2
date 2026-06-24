# Notes on Peyton Young (1993) - The Evolution of Conventions

### 1. DEFINITION OF CONVENTION
*   **Young's Definition:** A convention is a pattern of behavior that is customary, expected, and self-enforcing.
*   **Game Theory Link:** A convention is a **Nash Equilibrium** that everyone expects.
*   **The Problem:** In games with multiple equilibria (like Coordination Games), how does one become established?

### 2. ADAPTIVE PLAY (THE MODEL)
*   **Setup:** An $n$-person game played repeatedly by different agents drawn from a large population.
*   **Information (Sampling):** Each player does not know the entire history. They take a **random sample** of size $k$ from the last $m$ plays.
*   **Behavior:** Players choose a **best reply** to the frequency distribution of strategies in their sample.
*   **No Mistakes:** If players always optimize perfectly, the process eventually converges to a pure strategy Nash equilibrium (a convention) in "weakly acyclic" games.
    *   *Weakly Acyclic Games:* From any starting point, there is a sequence of best replies leading to a strict Nash equilibrium. This includes coordination and common interest games.

### 3. ADAPTIVE PLAY WITH MISTAKES (STOCHASTIC STABILITY)
*   **The Perturbation:** Assume players occasionally "experiment" or make mistakes with a small probability $\epsilon$.
*   **Stationary Distribution:** With mistakes, the process is a perturbed Markov chain. It no longer has absorbing states but has a unique long-run stationary distribution.
*   **Stochastic Stability:** As the mistake probability $\epsilon \to 0$, the stationary distribution concentrates on a specific subset of equilibria. These are **stochastically stable**.
*   **Significance:** Even if many equilibria are Nash, only the stochastically stable ones will be seen most of the time in the long run.

### 4. EQUILIBRIUM SELECTION
*   **Risk Dominance:** In $2 \times 2$ coordination games, the stochastically stable equilibrium is the **Risk Dominant** one (the one that is "safer" to play if you are uncertain about the other's move).
*   **General Games:** In larger games ($3 \times 3$ and up), stochastic stability may select an equilibrium that is neither Risk Dominant nor Pareto Optimal.
*   **Computation (The Algorithm):
    1.  Identify all strict Nash equilibria.
    2.  Calculate the "Resistance" (minimum number of mistakes) needed to move from the basin of attraction of one equilibrium to another.
    3.  Construct a graph where nodes are equilibria and edges are resistances.
    4.  Find the **minimum resistance spanning tree** (Arborescence). The equilibrium at the root of the easiest tree is the stochastically stable one.

### 5. CONCLUSION
*   Conventions emerge through a process of **positive feedback** from precedent.
*   Small, random fluctuations (mistakes) eventually drive the population out of "weak" conventions and into the most "robust" ones.
*   Society can "learn" even if individual members are naive or short-lived.