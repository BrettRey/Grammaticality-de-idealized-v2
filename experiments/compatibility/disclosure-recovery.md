# Could the disclosure study detect learning?

**Park the balanced, single-response design as a small confirmatory study.**
Even if every learner uses the key correctly and the model's probabilities
are exactly right, 256 independent truth judgments give the planned
crossover test a 12.0% chance of detecting the effect. An analysis given
the generating probabilities faces an upper bound of 25.3% at a 5%
false-positive rate. These calculations concern the fixed cabinet materials
and the original payoff. They use no participant responses.

## The recoverable effect

Each learner hears the same exchanges and then learns in which scene
six speakers passed up the marker. Each gives one truth judgment with a new
marker–adverb combination. For each test scene, take endorsement under the
reopened key minus endorsement under the still-locked key. Subtract the
reopened-scene difference from the still-locked difference, so the predicted
crossover is positive here. Full use gives $D=0.1150$ and ignoring the key
gives $D=0$. The model gives the same probabilities on all 16 list versions.
The counts below allocate independent learners equally to each version in
each of the four post-disclosure cells. The pre-disclosure control would
require additional learners. [Materials and cell probabilities](README.md#what-if-learners-discover-the-alternatives-afterward)

For the recovery calculation, a learner who ignores the key has the mean
of the two published endorsement probabilities for that scene. This is a
chosen baseline. With correct use by half the learners and the remainder
ignoring the key, $D=0.0575$. The test of ignoring the key allows any
scene-specific baseline common to both arms.

| Post-key learners, total | Chance the crossover test detects full use | Power ceiling, full use | Chance it detects half use | Power ceiling, half use |
|---:|---:|---:|---:|---:|
| 256 | 12.0% | 25.3% | 5.4% | 12.4% |
| 1,024 | 44.7% | 62.4% | 14.1% | 25.3% |
| 4,096 | 96.0% | 98.9% | 44.1% | 62.3% |

Detection means excluding the hypothesis that the key has no effect in
either scene, using a two-sided 5% test. The ceilings, rounded upward, apply
to any analysis of these four cells controlling false positives at 5% under
the chosen baseline. The script also checks the observed contrast against the
central 95% count ranges under half and full use, retaining every compatible
candidate. With 1,024 learners and full use, 53.0% of studies retain **both**
no use and full use. Even with 4,096 learners, 53.5% retain half use when
everyone used the key. Excluding zero and recovering the amount of use are
different inferential demands.

The original form-choice probe gives $P(\mathrm{choose})=0.025+0.5\,P(\mathrm{endorse})$.
One could generate that response by keeping a truth response half the time
and otherwise choosing the marker with probability .05. Under this response
law, replacing a truth probe with a single choice from an independent learner
in the same cell cannot improve the ceiling. Repeated measures would require
a model for responses from the same person.

## Why the ceiling holds

Let $L$ be the four-cell likelihood under the specified use rate divided
by the likelihood under the midpoint baseline. For any rejection rule
$0\leq T\leq1$ with $E_0[T]\leq .05$, and any $t>0$,

$$ E_1[T]=E_0[LT]\leq .05t+E_0[(L-t)_+]
  =P_1(L>t)+t\{.05-P_0(L>t)\}. $$

The script sums both tail probabilities from the four independent binomials.
A normal approximation selects a convenient threshold. The inequality
holds for every threshold, and both tails in the reported bound use the
finite-sample distributions. Enumeration of all count tables with two
learners in each cell checks the calculation against the optimal randomized
test for that small case.

For the crossover test itself, let $n$ be the learners per cell. Its signed
count is $nD$ with the cell rates replaced by their sample proportions.
Under no key effect a matched pair, one learner per key in a scene and
version, contributes $+1$ and $-1$ with equal probability $q=p(1-p)$.
Either sign has probability at most $1/4$. To see where the largest null
tails occur, write $S$ for the other pairs' sum. Adding a pair increases
$P(S\geq k)$ by $q[P(S=k-1)-P(S=k)]$ for integer $k\geq1$. The sum of
independent symmetric unimodal pair laws is symmetric and unimodal, so this
increment increases with $q$. Setting every $p=1/2$ gives the reference
law $\mathrm{Binomial}(4n,1/2)-2n$. Under each specified alternative the
script convolves the four actual cell laws. [Replay the calculation](disclosure_recovery.py)

## What infinite data would leave open

Let $c$ be the share using the key correctly and $w$ the share reversing the
two badges. If the remaining learners ignore the key and the three shares
are common to all arms and scenes, each scene's key difference is multiplied
by $c-w$. Half correct and half ignoring gives the same four probabilities
as three quarters correct and one quarter reversing under the midpoint
baseline. Even a zero effect can mean that everyone consulted the key and
half reversed it. These are exact duplicates for every sample size.

This design measures the net influence of the disclosed alternatives. A
separate observation of which badge learners associated with which scene
would address a specific uncertainty before any decision to collect more
judgments. The hard and graded accounts still agree at every use rate.
