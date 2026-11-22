# What will a learner say with a verb it has never heard?
Four verbs of one action class occur agent-first and four of another occur patient-first. When a new verb describes an action of the first kind, both a categorical learner and a graded learner favour agent-first. In a balanced reconstruction of Conwell and Snedeker’s video exposure, they give exactly the same probability, 86.6%. Both learned from the examples. Neither received a grammaticality judgment or a production rate from the participants.
## Which history goes into the calculation?
Conwell and Snedeker used 12 training verbs and six withheld verbs. In one condition an action’s meaning predicted whether its verb occurred agent-first, patient-first with _ka_, or in both orders. In the other condition the semantic and structural classes were crossed. Both orders could describe the same event. Each training video was replayed on all three training days. There were also practice tasks, refresher videos and two test days. A production late in testing can reflect earlier test encounters with the same verb. [Study, Language Structure and Procedure](https://pmc.ncbi.nlm.nih.gov/articles/PMC11588301/)

I assigned contact verbs to agent-first, posture verbs to both orders, and motion verbs to patient-first for one illustrative list. The study counterbalanced the mapping. I supplied two distinct examples per training verb, one in each order for alternating verbs. The number of examples per verb is my choice. The calculation treats the verb’s identity, action class and order as observable. It omits practice, refreshers, memory loss and errors. It predicts production conditional on using one of the two orders.

In the crossed control, each meaning has four trained verbs. One structural class contributes two verbs and the others one apiece, with the doubled class rotated across meanings. Adding two withheld verbs per meaning can then give exactly two verbs in each cell of the full three-by-three inventory. The learners see the training rows only. They receive neither the condition label nor the experimenter’s assignment for a withheld verb.
## What the learners acquire
Each learner can pool all verbs or learn a separate agent-first tendency, $\theta$, for each action class. Both possibilities start with equal prior probability and each tendency starts uniformly distributed between zero and one. Training updates those probabilities. The first production of a new verb averages over the remaining uncertainty.

| Learner | How one verb produces its observed orders |
| --- | --- |
| Categorical availability | A verb’s repertoire comes from two independent draws with agent-first probability $\theta$. Two identical draws license only that order. Different draws license both, with equal choice probabilities. This implements OVMG’s distinction between availability and choice in a finite fragment. The two-draw learning assumption is specific to this comparison. |
| Graded use | Each verb has its own continuous probability $p$ of agent-first, drawn from a beta distribution with parameters $\theta$ and $1-\theta$. Repeated encounters with a verb teach the learner about that verb as well as its action class. |
| Class and frequency | Every token contributes to the inferred order tendency at the class or pooled level. The identity of the verb carrying that token has no further effect. |

| Input and first-encounter probe | Categorical | Graded | Class and frequency |
| --- | ---: | ---: | ---: |
| Predictive meaning, new contact verb, count each distinct video once | 86.6% | 86.6% | 90.0% |
| Same videos, count each of three presentations as fresh evidence | 89.8% | 91.0% | 96.2% |
| Crossed control, new contact verb, count each distinct video once | 52.8% | 52.8% | 53.0% |

Entries give agent-first production. In this list the motion predictions are the complements and the posture predictions are 50%. Weighting the replays separately illustrates how strongly a learner might count repetition. The experimenter’s replay of a video supplies no new speaker choice. The study’s reported 57% patient-first figure pools familiar and unfamiliar verbs. A first-encounter forecast cannot be scored against it. A test of the numerical values would need the learner’s actual preceding exposures and an independently calibrated production bias. [Earlier analysis of the published summaries](./conwell-snedeker-feasibility.md)

One prediction survives variation in the number of videos per verb. Provided the restricted training verbs in one meaning all occur agent-first and those in another all occur patient-first, all three learners rank the new verbs in that direction. In the model that separates meanings, every all-agent-first history favours higher $\theta$ and every all-patient-first history favours lower $\theta$. Pooling adds the same prediction to both probes. The size of the difference depends on the token counts and on what else the learner heard.

**Why the first two predictions coincide.** For a verb’s probability of agent-first, the two models have the same conditional mean $\theta$ and second moment $(\theta+\theta^2)/2$. These determine the probabilities of hearing any one or two orders from that verb, including one of each. Whenever every training verb contributes at most two observations, the models therefore attach the same likelihood to the entire history, infer the same relevance of meaning, and predict the same first choice for an unheard verb. This holds for every such history. The parameter choices deliberately give the rival this opportunity. Three agent-first observations of a single training verb are already enough to break the identity: for a new verb of the same meaning the predictions are $13/18$ and $97/135$, a difference of just $1/270$.
## A stronger contrast once the new verbs have been introduced
Take two new verbs with the **same action class**. Demonstrate one twice agent-first and once patient-first. Give the other the reverse counts. Across the two verbs the learner hears three instances of each order. Only the assignment to the verbs varies. Exchange the verbs’ identities across lists, balance presentation order and score the first elicited production for a randomly assigned probe verb after all six demonstrations. This is a proposed transfer test. Its figures are model predictions.

| Account | Agent-first after 2 agent-first, 1 patient-first | Agent-first after 1 agent-first, 2 patient-first | Difference |
| --- | ---: | ---: | ---: |
| Categorical, equal preference when both licensed | 50.0% | 50.0% | 0 points |
| Categorical, preference learned for the action class | 57.6% | 57.6% | 0 points |
| Graded, verb-specific use | 68.2% | 43.2% | 25 points |
| Class and frequency | 74.8% | 74.8% | 0 points |
| Hard repertoire and verb-specific graded preference | 67.4% | 42.4% | 25 points |
| Simple counts for each verb, one prior count per order | 60.0% | 40.0% | 20 points |

The class-preference variant allows genuine restrictions and gives a both-licensed verb agent-first preference $(1+\theta)/3$. To make it a serious rival, its agent-only mass is $\theta(1+\theta)/[2(2-\theta)]$, its patient-only mass is the same expression evaluated at $1-\theta$, and the remaining mass licenses both. These weights match the graded learner’s first three moments at every $\theta$. It can reproduce the graded learner’s next choice after a new verb has been heard once in each order, given the two-example training list. Once both verbs are known to alternate, a preference shared across their action class predicts identical choices for the pair.

For the graded learner, the corresponding posterior means given $\theta$ are $(2+\theta)/4$ and $(1+\theta)/4$. Their difference is one quarter for **every** $\theta$, so uncertainty over the class tendency cancels. As a counterexample, give half the verbs genuine single-order repertoires, and give both-licensed verbs the same continuous distribution of individual choice preferences as the graded learner. Hearing both orders establishes that each probe verb belongs to the latter group under error-free exposure. The 25-point contrast survives intact in a grammar with categorical restrictions. The magnitude also depends on how readily a verb-specific preference updates: beta prior concentration $k$ gives a difference of $1/(3+k)$.

**Interpretation.** The first production measures generalization by action meaning. The paired production difference measures retention of relative use for particular verbs once both orders have been demonstrated, under matched exposure and response assumptions. A positive difference can coexist with categorical licensing. The next empirical comparison is the class contrast on the earliest identifiable productions of withheld verbs, conditioning on any prior test demonstrations. The role-reversal items address a separate question about interpretation. [Executable derivation and replay](./conwell_learning.py)

```sh
python3 experiments/compatibility/conwell_learning.py
```
