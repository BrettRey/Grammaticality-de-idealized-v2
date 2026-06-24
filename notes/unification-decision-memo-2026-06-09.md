# Unification Decision Memo
Date: 2026-06-09 Paper: `main.tex`, "Grammaticality de-idealized" Decision scope: do not implement without Brett's authorization.
## Question
The review proposes collapsing `map`, `K`, and `C_t` into one licensing hierarchy. On this view, structural viability and operator-value coherence would not be primitive components of grammaticality. They would be limiting regimes of conditioned licensing over constructional nodes: some nodes license analyzable substructure; some license coherent operator-value packages; some license whole utterance types in situations.

My estimate: the unified version has a 0.55 probability of becoming the stronger paper after a full rewrite. That is lower than the review's 0.70 because the move is theoretically attractive but would restructure the paper's core explanatory contract and create new burdens for the companion.
## Benefits
The main benefit is parsimony. The review is right that `map` and `K` become hard to defend as wholly independent primitives once the live `phi_j` are limited to grammaticalized operator features and once listed idioms can satisfy analyzability by being licensed units. A single hierarchy would make that dependence explicit instead of treating it as a bug.

The move would also fit the revised productivity repair. If licensing already lives over a constructional hierarchy, token viability can be derived from coverage by licensed nodes. Novel sentences are not licensed because their exact type has been observed; they inherit status from partially pooled constructional families. This would make the model cleaner.

It would also be HPC-friendly. One maintained macro-regime, realized through multiple mechanisms, is easier to defend as a projectible kind than three partly overlapping variables. The paper could say: grammaticality is a high-licensing region in a constructional state space, with viability, coherence, and conventional status as observable faces of that regime.
## Costs
The cost is {==thesis-level revision==}{>>I'm happy to revise the thesis if the result is a stronger thesis. My goal is not to defend a particular position but rather to find the truth.<<}{id="c1" by="user" at="2026-06-09T22:23:01.178Z"}. The current paper argues for three constitutive variables and then composes them multiplicatively. A unified hierarchy would demote that architecture from thesis to diagnostic approximation. Sections 2, 3, the formalism, the factor-analysis discussion, and the comparison sections would all need re-sequencing.

The move also weakens {==the paper's immediate readability==}{>>I expect the paper could be redrafted to recover lost readability<<}{id="c2" by="user" at="2026-06-09T22:23:48.199Z"}. Reviewers can understand "map x K x C_t" quickly. A single recursive licensing hierarchy is more elegant but {==easier to perceive as an unconstrained usage-based model==}{>>This is a good point. Great care would have to be taken to avoid misconstrual.<<}{id="c3" by="user" at="2026-06-09T22:24:24.879Z"} unless the identification conditions are exceptionally tight.

The largest risk is companion compatibility. The companion needs a derivation of the operator stratum as a role-functional boundary. If this paper collapses everything into licensing, the companion must not look like it is reintroducing a stratum by assertion. {==The two papers would need coordinated language==}{>>As the Beatles sang, "we can work it out"<<}{id="c4" by="user" at="2026-06-09T22:25:11.784Z"}: the companion derives which parts of the hierarchy behave operator-like; this paper derives which licensing regimes become categorical.
## Sketch Of The Unified Formalism
Let `g` range over constructional nodes at multiple grains, from listed forms and idioms through operator exponents to schematic clause patterns. Each node has a situation-conditioned licensing posterior:

```text
C_t(g, c) ~ Beta(alpha_t(g, c), beta_t(g, c))
```

A candidate utterance `u` activates a weighted set of nodes `A(u, c)`. Its status is:

```text
L_t(u, c) = sum_{g in A(u,c)} lambda_g(u,c) C_t(g,c)
```

Structural viability is the limiting case where no licensed decomposition covers `u`, so `A(u,c)` is empty or all relevant `C_t(g,c)` are near zero. Operator-value coherence is the limiting case where a decomposition exists but the node that should bind an update-critical value is licensed against the proposed value package. Situational conventionality is the ordinary case where a coherent, analyzable candidate lacks enough positive licensing in its opportunity set.

On this view, `map(u,c)` and `K(u,c)` remain useful diagnostics, but not primitive causes. They are projections of `L_t` onto different parts of the constructional network.
## What Breaks In The Current Paper
The multiplicative definition of `G_t` would have to be replaced or explicitly downgraded. The current formalism says `map`, `K`, and `C_t` are separately estimated and then multiplied. In the unified version, multiplication risks double-counting because a low-level licensing failure already lowers the higher-level score.

The worked examples would need rewriting. `Can the have running` becomes absence of licensed decomposition, not `map=0` as a primitive. `I've finished it yesterday` becomes low licensing for the present-perfect-plus-definite-past package, perhaps with a reject outcome as a processing approximation. `I have 25 years` becomes non-licensing of an age-predication node.

The factor-analysis section would need a stronger measurement model. If all components are projections of licensing, the model must explain why ratings still separate into structural, coherence, frequency, processing, and prescriptive factors. The current objective/subjective split would not be enough.
## Companion-Stratum Mapping
Option A: keep the revised three-factor architecture.

Expression-shape stratum maps mainly to `map` and low-level constructional coverage. Operator stratum maps to the live part of `K` plus high-opportunity `C_t`. Payload stratum remains mostly outside categorical grammaticality unless a payload expression enters an operator role. This is easiest to coordinate with the companion because the companion can derive the operator stratum while this paper derives categoricality within it.

Option B: unified licensing hierarchy.

Expression-shape, operator, and payload are not separate variables. They are regions of the same constructional network with different opportunity structures and update roles. Expression-shape nodes handle signal recoverability and decomposition; operator nodes handle closed public-update contrasts; payload nodes handle open-class descriptive content. The companion would then explain why operator nodes have unusually high closure, accountability, and opportunity mass.

Option C: hybrid.

Keep `map`, `K`, and `C_t` as diagnostic projections in the main exposition, but add a limitations/future-work paragraph saying a deeper unification may derive them from licensing over a constructional hierarchy. This preserves the current paper while acknowledging the review's strongest architectural point.
## {==Recommendation==}{>>I'm genuinely unsure which is better, but I want to choose the one that is truly better and not simply strategically better.<<}{id="c5" by="user" at="2026-06-09T22:26:29.365Z"}
Implement Option C now, not Option B. Probability Option C is the best current revision path: 0.70. Probability full unification should become the next major version after Brett reviews the companion alignment: 0.55. Probability full unification breaks the current paper's submission-readiness if done now: 0.65.

The review is directionally right that `map` and `K` are partly parasitic on licensing. The present revision already admits that dependence by making `K` live only over grammaticalized operator constraints and by adding hierarchical partial pooling. But full collapse should wait for Brett because it changes the thesis from "three interacting variables de-idealize grammaticality" to "one constructional licensing quantity has three diagnostic regimes."

## Post-Review Revision

Brett's comments change the decision criterion. If the relevant question is "what is the safest revision of the current paper?", Option C remains the best near-term path. If the relevant question is "what is the stronger and more truthful thesis, assuming Brett is willing to redraft around it?", I now recommend Option B.

Revised estimate: full unification has a 0.63 probability of producing the stronger paper after a real rewrite. The review's 0.70 still feels slightly high because the unified hierarchy can easily be misconstrued as unconstrained usage-based licensing. That risk is manageable, but only if the rewrite makes the constructional hierarchy, opportunity sets, fixed conditioning state `c`, and falsification conditions more explicit than the current paper does.

The practical recommendation is therefore two-stage. Do not patch full unification into the present draft as a local edit. Instead, if Brett chooses truth over near-term continuity, rebuild the paper around the unified hierarchy: licensing over constructional nodes is primitive; `map`, `K`, and `C_t` are diagnostic projections; the companion derives why operator nodes occupy the high-closure, high-opportunity, update-critical region where categorical grammaticality clusters.

---
comments:
  c6:
    body: "Agreed. I was counting thesis-level revision as a cost under a submission-readiness criterion. Under a truth-first criterion, it is not a decisive objection."
    by: Codex
    at: "2026-06-09T22:28:18.300Z"
    re: c1
  c7:
    body: "Agreed. Readability is a tractable exposition problem, not a deep objection to unification."
    by: Codex
    at: "2026-06-09T22:28:18.300Z"
    re: c2
  c8:
    body: "This remains the main live risk. The unified version needs tight identification conditions, independently specified opportunity sets, and clear falsifiers to avoid becoming an unconstrained usage-based story."
    by: Codex
    at: "2026-06-09T22:28:18.300Z"
    re: c3
  c9:
    body: "Agreed. Companion coordination is work, not a blocker. It becomes a rewrite constraint rather than a reason to reject the move."
    by: Codex
    at: "2026-06-09T22:28:18.300Z"
    re: c4
  c10:
    body: "Revised recommendation: if the decision criterion is the stronger thesis rather than the safest current revision, choose the full unification as the next major rewrite."
    by: Codex
    at: "2026-06-09T22:28:18.300Z"
    re: c5
