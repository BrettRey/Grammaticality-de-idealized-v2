# How linguistic forms enter community repertoires: Formal models for the "arise" question

The researcher's two-module framework (opportunity-sensitive preemption for C_t decrease; coordination equilibria for stability) is well-positioned within existing literature, but **formal models for the "arise" question remain underdeveloped across all relevant fields**. The most promising formalization tools come from replicator dynamics, Bayesian learning, and iterated learning frameworks—though none fully addresses how forms initially enter repertoires. The actuation problem identified by Weinreich, Labov, and Herzog (1968) remains what Labov (2001) calls "mysterious," and strong theoretical grounds exist for expecting fundamental asymmetry between entry and exit dynamics.

---

## 1. Literature on innovation and entry mechanisms

### Grammaticalization: Descriptive richness, formal poverty

The grammaticalization literature offers detailed descriptive accounts but surprisingly few computational implementations. **Bybee (2003, 2010)** provides the most functionalist-compatible framework, proposing that frequency functions as both cause and consequence of grammaticalization. Her network model treats words as having "lexical strength" based on token frequency, with connections of varying strength between exemplars—but this remains conceptual rather than mathematically specified. The key mechanisms (semantic bleaching, generalization, decategorialization, erosion) predict directionality but not timing.

**Bentz and Buttery (2014)** offer the only fully computational grammaticalization model, using Zipf-Mandelbrot law parameters to track lexical diversity changes. Their algorithm merges high-frequency bigrams iteratively across generations, simulating how collocations fuse into grammatical morphemes. However, this model ignores part-of-speech constraints, syntactic context, and semantic factors—it addresses the "how" of fusion but not the "when" or "why."

**Traugott and Dasher (2002)** provide semi-formal directionality constraints through the Invited Inference Theory of Semantic Change, drawing on Levinson's pragmatic heuristics. Innovation arises when particularized conversational implicatures become generalized and eventually semanticized. This framework specifies pathways (propositional → textual → expressive meanings) but lacks computational implementation.

### Analogical extension: The best-formalized domain

Formal models of analogy represent the most developed area. **Skousen's Analogical Modeling (1989, 2002)** provides a fully implemented exemplar-based system: given a context, the algorithm generates all supracontexts, extracts exemplars, discards inconsistent supracontexts, and selects probabilistically with bias toward larger supracontexts. The model successfully predicts Finnish morphology, German plurals, and English past tenses—phenomena where no theoretical explanation previously existed. Available implementations exist in Perl and C.

**Albright and Hayes (2003)** developed the Minimal Generalization Learner, which inductively generates rules from paradigms and assigns confidence scores based on scope and reliability. This model predicts "islands of reliability" (phonologically similar irregular clusters), handles gradient acceptability judgments, and successfully models paradigm leveling directions in Latin and elsewhere. The MGL is fully computational and tested against experimental human data.

### Contact linguistics: No predictive formal models

**Thomason and Kaufman (1988)** explicitly reject linguistic constraints as predictive—their borrowing scale correlates contact intensity with structural borrowing depth, but they argue social/historical factors dominate over linguistic predictability. **Mufwene (2001)** uses evolutionary language extensively (feature pools, selection, ecological fit) but provides no mathematical formalization; one reviewer noted "not a single bit of actual theory is transferred from population genetics." **Matras (2007)** documents borrowability hierarchies (discourse markers most borrowable, tense/aspect least), but these remain descriptive generalizations without predictive formal implementation. This represents a significant gap for the researcher's framework.

### Acquisition and community uptake: The critical missing link

The acquisition literature focuses almost exclusively on **retreat from overgeneralization**—how children converge to adult norms—rather than the reverse process of child innovations becoming community norms. **Ambridge (2012)** reviews mechanisms preventing innovation spread (preemption, entrenchment, constraint learning), but no formal models exist for when child innovations propagate. This gap is particularly striking given historical linguistics' observation that some changes originate in acquisition (Lightfoot 1991, 2020).

---

## 2. Asymmetry between entering and exiting the repertoire

Strong theoretical and empirical grounds support **fundamental asymmetry** between entry and exit dynamics. Multiple formalisms predict this asymmetry through different mechanisms.

### Evolutionary invasion asymmetry

Evolutionary stability analysis (Maynard Smith and Price 1973) shows that **invasion requires crossing a threshold** while maintenance only requires staying above equilibrium. For a strategy S to be evolutionarily stable, a rare mutant T must either earn lower payoffs against S than S earns against itself, or if equal, S must outperform T in self-interaction. Entry conditions are thus more stringent than persistence conditions.

The **replicator-mutator equation** formalizes this in linguistic terms. Nowak, Komarova, and Niyogi (2001) derive a "coherence threshold"—minimum learning accuracy required for any grammar to persist. Novel grammars must exceed this threshold to survive, but established grammars face only stochastic extinction risk.

### Frequency-based conservatism

**Bybee's token/type frequency distinction** creates systematic asymmetry. High **token frequency** generates entrenchment—forms resist analogical replacement because strong memory traces make them less susceptible to paradigm leveling. High **type frequency** generates productivity—patterns extend to new items. This creates conservatism toward established high-frequency forms and openness in productive pattern slots. Entry is favored by high type frequency of the pattern plus low token frequency of specific competitors; exit is resisted by high token frequency of the form itself.

### Hysteresis and bistability

Bistable systems exhibit **hysteresis**—the threshold for transition A→B differs from threshold for B→A. The **Baxter-Blythe-Croft-McKane utterance selection model (2006)** demonstrates this formally: in the case where linguistic forms can become extinct, the system shows "two-stage relaxation" where a common distribution "persists for a long time" because ultimate extinction requires "rare fluctuations." Entry can proceed deterministically once threshold is crossed; exit requires stochastic events.

### Extinction debt and delayed loss

Drawing from ecology (Tilman et al. 1994; Kuussaari et al. 2009), **extinction debt** predicts that forms may persist long after conditions cease to favor them. Speakers who learned forms in childhood may maintain them even after they become non-productive in the community—creating a "doomed but surviving" category. The corollary "immigration credit" predicts that new forms may take time to establish even after conditions favor them.

### Biological parallels

**Foote (2023)** demonstrates from Phanerozoic marine fossil analysis that origination rates are strongly diversity-dependent (negatively correlated with existing diversity) while extinction rates show only weak diversity dependence. This supports a model where extinction is largely driven by abiotic perturbations, with subsequent origination filling depleted niches—qualitatively different processes.

---

## 3. Adjacent fields and literature gaps

### Game theory: Convention genesis remains underspecified

**Lewis (1969)** provides the foundational analysis of conventions as coordination equilibria but offers no dynamic model of convention emergence. His treatment relies on **salience** (Schelling's focal points)—conventions initially emerge because one option "stands out" through precedent, explicit agreement, or psychological prominence. This is essentially static, defining what conventions *are* rather than how they come to be.

**Skyrms (1996, 2010, 2014)** advances beyond Lewis by applying **replicator dynamics** to signaling games, showing how initially meaningless signals can acquire informational content through evolutionary/learning dynamics. Crucially, Skyrms (2010, Chapter 10) introduces models where agents can **invent new signals**—directly addressing innovation rather than just selection among pre-existing options. Basin of attraction analysis shows which convention emerges depends on initial conditions.

**Peyton Young (1993, 1998, 2015)** pioneered **stochastic evolutionary game theory**, demonstrating that not all Nash equilibria are equally likely to emerge—risk-dominant equilibria are favored over payoff-dominant ones. His adaptive play model treats conventions as emergent from bounded rationality: agents best-respond to random samples of past plays, with occasional "mistakes" ensuring ergodicity. This predicts **stickiness and punctuated change**—norms resist small perturbations but can undergo rapid transitions once thresholds are breached.

### Cultural evolution: Conformism creates entry barriers

**Boyd and Richerson (1985, 2005)** provide the most developed models of cultural trait transmission. Three biased transmission mechanisms affect innovation adoption: **direct/content bias** (some variants fit cognitive systems better), **conformist bias** (disproportionate tendency to adopt common behaviors), and **prestige bias** (imitation of high-status individuals).

Conformist transmission creates systematic **asymmetry**: novel traits face uphill battles at low frequencies (conformist preference for majority behavior), but once established, become highly resistant to extinction. **Henrich's (2001, 2016)** work on prestige bias shows how novel variants can spread before their benefits are evident if associated with high-status individuals—potentially relevant to understanding how linguistic innovations from prestige speakers gain traction.

### Sociolinguistics: The actuation problem remains unsolved

The central puzzle is **actuation**: why does change occur when and where it does, but not in other structurally identical situations? Weinreich, Labov, and Herzog (1968) identified this as "the heart of the matter"; Labov (2001) still calls it "mysterious." The structural conditions for change are always present; actuation requires additional social factors.

**Milroy and Milroy (1985, 1987)** provide the network-based account: **weak ties** facilitate innovation diffusion across network boundaries while **strong ties** reinforce in-group markers and resist innovation through norm enforcement. **Labov (2001)** identifies leaders of linguistic change as female, upper-working-class individuals with high local network density plus wide-ranging weak ties—located centrally but not at social extremes.

**S-curve models** describe propagation patterns formally. **Kroch's (1989) Constant Rate Hypothesis** shows that when grammar competition drives change, replacement rate is identical across all affected linguistic contexts—evidence for single underlying parametric change driving multiple surface manifestations. **Kauhanen and Walkden (2018)** derive this constant rate effect from Yang's variational learner model augmented with production biases.

**Blythe and Croft (2012)** identify **four propagation mechanisms**: replicator selection (differential weighting of variants), neutral evolution/drift, neutral interactor selection (network effects), and weighted interactor selection (leader-follower dynamics). Their critical finding: "the only selection mechanism that consistently produces an S-curve trajectory is **replicator selection**."

### Language acquisition: Preemption aligns with the researcher's framework

**Yang's Tolerance Principle (2016)** states that for a rule over N items, the rule becomes productive if exceptions e ≤ N/ln N. This threshold emerges from optimization: rules "turn on" when computational cost of listing exceptions exceeds cost of computing the rule. Yang's **variational learning model (2002)** treats acquisition as competition among grammatical hypotheses, with weights shifting based on successful parsing—applicable to both acquisition and historical change.

**Statistical preemption (Goldberg and Boyd 2011; Robenalt and Goldberg 2015)** maps directly onto the researcher's "opportunity-sensitive preemption": learners block Form A when they consistently witness competing Form B in exactly the contexts where A would have been appropriate. This is competition between alternative expressions for the same function—preemption requires witnessing the specific alternative in the relevant context, distinct from general entrenchment effects.

**Iterated learning (Kirby, Griffiths, Smith 2014)** provides formal models of how individual learning biases become population-level patterns. The mathematical analysis (Griffiths and Kalish 2007) shows that with posterior sampling, iterated learning converges to the learner's prior—languages eventually reflect biases perfectly. The transmission bottleneck (learners see only partial data) creates selection pressure for learnability.

### Philosophy of science: Homeostatic property clusters

The researcher's interest in homeostatic property cluster theory (Boyd 1999) for linguistic categories aligns with viewing repertoire status as emergent from multiple interacting factors rather than single definitional features. This connects to coordination equilibria: once multiple properties cluster together, mutual reinforcement creates stability that individual properties couldn't maintain alone.

---

## 4. Potential objections and conceptual vulnerabilities

### Objection 1: Preemption and coordination may not be separable modules

**Ambridge et al. (2018)** found preemption and entrenchment effects are "rarely dissociable, due to collinearity"—they may be outcomes of single construction-competition process rather than distinct mechanisms. The researcher's two-module framework risks artificial separation of what may be a unified process operating under different conditions. Both preemption and coordination could emerge from learners tracking form-function mappings and adjusting production probabilities accordingly.

**Response needed**: The framework should specify what empirical predictions distinguish the modules versus what would collapse them into unified dynamics.

### Objection 2: Coordination equilibria alone may suffice for all C_t dynamics

Simple coordination models (e.g., naming games) produce both adoption and abandonment through the same mechanism. If the same dynamics generate entry and exit, why posit separate modules? **Kauhanen's (2020) replicator-mutator dynamics** models convergence and divergence through unified equations.

**Counter-consideration**: Coordination models typically show symmetric dynamics, but empirical data often shows asymmetric entry/exit. If the two-module framework's value lies in explaining asymmetry, this should be explicit.

### Objection 3: The framework struggles with the "first speaker" problem

For opportunity-sensitive preemption to drive C_t decrease, there must already be a competitor form—but what licensed the competitor's initial entry? The framework may be better at explaining *competition among existing forms* than *de novo entry*. How does the first instance of an innovation enter the repertoire before any preemption dynamics can operate?

### Objection 4: Network effects may be doing the explanatory work attributed to modules

What appears as separate "preemption" versus "coordination" mechanisms may reflect network position of innovators versus maintainers. Weak ties introduce variants; strong ties stabilize them (Milroy and Milroy 1985). The modules might be phenomenological descriptions of network effects rather than independent mechanisms.

### Objection 5: The framework assumes cleaner category boundaries than empirical data support

**Stable variation** (competing forms that persist indefinitely) challenges the preemption module's prediction that competition drives exclusion. **Fruehwald and Wallenberg (2013)** distinguish "language change variables" from "stable variation"—the latter may require functional or social differentiation that the framework doesn't clearly accommodate.

---

## 5. Phenomena the framework should handle but might struggle with

### Stable innovations: What protects new forms from preemption?

Once a new form enters and begins competing, what prevents opportunity-sensitive preemption from eliminating it? The framework needs a mechanism for **initial establishment** that shields innovations during their vulnerable low-frequency phase. **Prestige bias** (Henrich 2001) offers one account: association with high-status speakers creates adoption advantage that overcomes conformist resistance. **Weak tie transmission** (Granovetter 1973; Milroy 1987) offers another: innovations enter through peripheral network positions where norm enforcement is weak.

### Unstable exclusions: Why do "doomed" forms persist?

The framework should explain **extinction debt** in language: forms that "should" be excluded based on consistent competitor presence but persist for extended periods. **Bybee's token frequency entrenchment** provides one mechanism: high-frequency forms resist replacement through strong memory traces regardless of functional competition. Generational replacement may be required—forms survive in older speakers while being excluded from acquisition by younger speakers.

### Reversals: Re-entry of excluded forms or sudden decline of established forms

**Re-entry** challenges the coordination equilibrium module: if exclusion reflects stable equilibrium, what perturbations allow re-entry? Contact, prestige shifts, or register expansion might create new contexts where previously excluded forms gain foothold. **Sudden decline** requires explaining how stable equilibria destabilize—threshold/tipping point dynamics (Young 1993) predict that gradual pressure accumulates until critical threshold triggers rapid transition.

### Stable variation: Long-term coexistence without resolution

The framework's logic suggests competition should resolve: either preemption drives one form out, or coordination stabilizes one as dominant. **Stable variation** violates this prediction. Mechanisms maintaining indefinite coexistence include: **functional differentiation** (forms specialize for different contexts/meanings), **social stratification** (forms index different groups), and **exact balance** (neither form has sufficient advantage). The framework may need explicit treatment of these equilibrium conditions.

---

## 6. Formalization tools for the "arise" side

### Replicator dynamics with innovation

The **replicator-mutator equation** provides the most directly applicable formalism:

*dx_i/dt = Σ_j x_j f_j Q_ji - φx_i*

where Q_ji represents mutation/innovation probability from form j to form i. This allows modeling **de novo entry** (mutation from existing forms), **competition** (fitness f_i), and **extinction** (x_i → 0). **Kauhanen (2020)** applies this specifically to linguistic convergence/divergence.

The framework's preemption module could be formalized by making fitness f_i depend on **opportunity mass weighted by competitor presence**—forms lose fitness when competitors occupy their functional niche.

### Bayesian models of convention learning

**Griffiths and Tenenbaum's tradition** offers tools for modeling how learners infer productive patterns from limited data. The **size principle** (smaller hypotheses fitting data receive higher likelihood) could model how learners identify which forms are licensed—a form absent despite opportunity creates evidence against its licensure.

**Statistical preemption** (Goldberg) can be formalized as Bayesian inference: P(Form A licensed | B consistently observed in A-appropriate contexts) decreases with exposure. The researcher's "effective opportunity mass" could be formalized as the cumulative evidence against form licensure.

### Iterated learning for community-level emergence

**Griffiths and Kalish (2007)** prove that iterated learning dynamics converge to the learners' prior distribution over languages. This provides a formal bridge from individual learning biases to population-level patterns. If learners' opportunity-sensitive preemption creates bias against forms with strong competitors, iterated learning predicts community repertoires will reflect this bias over generations.

### Agent-based models with network structure

The **utterance selection model (Baxter et al. 2006; Blythe and Croft 2012)** provides an extensible computational framework. Key parameters include memory weight (λ), social weighting, network structure, and population size. This could be extended to incorporate:
- **Opportunity tracking**: Agents update beliefs about form licensure based on contexts encountered
- **Preemption dynamics**: Agents reduce production probability for forms when competitors observed in appropriate contexts
- **Network-mediated entry**: Innovations enter through peripheral/weak-tie positions

**Fagyal et al. (2010)** showed that networks without "loners" (peripheral nodes) converge rapidly to single variants, while networks with loners maintain variation—suggesting network structure determines whether innovations can gain foothold.

### Threshold and tipping point models

**Granovetter's (1978) threshold model** captures critical mass dynamics: each individual has a threshold (proportion of others who must adopt before they will). The distribution of thresholds determines whether innovations spread. This could formalize the entry barrier: innovations must reach critical mass to become self-sustaining.

**Hysteresis models** from physics/biology provide formal treatment of asymmetric thresholds for entry versus exit—directly relevant to the asymmetry question.

---

## Summary of key sources for further development

For the "arise" side specifically, the most promising directions combine:

- **Skyrms (2010)** Chapter 10 on inventing new signals—rare formal treatment of innovation in convention theory
- **Yang's variational learning (2002)** applied to diachrony—Wallenberg (2019) addresses the acquisition-to-community time scale gap
- **Goldberg's statistical preemption** for the proximate learning mechanism
- **Iterated learning (Griffiths and Kalish 2007)** for the individual-to-population bridge
- **Baxter-Blythe-Croft-McKane (2006)** for computational implementation with network effects
- **Young (1993)** for stochastic stability and threshold dynamics

The largest gap remains the **actuation problem**: no existing model predicts *when* innovation entry occurs. Existing models describe propagation dynamics once innovation exists but treat the initial spark as exogenous perturbation, random mutation, or unexplained salience. A complete formalization of the "arise" side would need to specify what triggers innovation in contexts where structural conditions have long been present.