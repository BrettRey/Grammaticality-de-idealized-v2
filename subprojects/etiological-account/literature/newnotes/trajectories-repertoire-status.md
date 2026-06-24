### Key Points on Trajectories of Repertoire Status (C_t) in Speech Communities
- Research suggests that linguistic forms enter repertoires (C_t increase) primarily through mechanisms like grammaticalization, where lexical items evolve into grammatical markers via reanalysis, often driven by implicatures and community adoption, though formal models for this "arise" side remain less developed than for exclusion.
- Exclusion (C_t decrease) appears more readily formalized via opportunity-sensitive preemption and indirect negative evidence in Bayesian learning, where absence of expected forms in input leads to rapid downgrading, especially for low-frequency items.
- Stability (high or low C_t) is likely sustained by coordination equilibria in game-theoretic terms, where deviations are penalized socially, creating self-reinforcing norms; however, evidence leans toward asymmetry, with entry requiring innovation or contact but exclusion happening more easily through competition or lack of use.
- The framework's gap in innovation could be addressed by cultural evolution models, which emphasize iterated learning and population dynamics, but controversies exist around whether categorical constraints are emergent or innate.
- Overall, while the two-module approach aligns with empirical patterns in language change, it may undervalue sociolinguistic factors like power asymmetries or multilingualism in real-world trajectories.

#### Mechanisms for C_t Increase (Arise)
Forms typically enter through innovation processes such as grammaticalization (e.g., verbs becoming future markers like English "be going to") or analogical extension in acquisition, where overgeneralizations persist if communicatively useful. Contact linguistics highlights borrowing from other languages, formalized in some models as string mutations in ecophysics simulations. Stability requires repeated use and community coordination to establish norms.

#### Mechanisms for C_t Decrease (Exclusion)
Bayesian learners use indirect negative evidence--the absence of forms in expected contexts--to preempt possibilities, accelerated by high opportunity and consistent competitors. This leads to exclusion of structurally possible forms, with rare items more vulnerable due to low exposure.

#### Factors in Stability
Coordination equilibria from game theory explain persistence: established forms resist displacement via social penalties, while excluded ones stay out unless external forces (e.g., revival efforts) intervene. Doubly-sustained states (preemption + coordination) are more robust, but singly-sustained ones may drift.

#### Addressing the Framework's Gaps
To balance the asymmetry, incorporate evolutionary game theory for entry, where mutations introduce new forms that spread if fitness advantages emerge. Potential objections include overreliance on subjective feelings (F) without accounting for sociolinguistic variation.

---

The trajectories of a speech community's repertoire status for linguistic forms (C_t) involve complex interplay between etiological processes that drive increase, decrease, and stability. While the provided framework emphasizes opportunity-sensitive preemption for exclusion and coordination equilibria for stability, the "arise" side--how forms enter and boost C_t--remains underdeveloped, prompting exploration of literature on innovation, asymmetry, and formal models. This survey integrates insights from grammaticalization theory, game theory, cultural evolution, Bayesian learning, historical linguistics, and sociolinguistics to address the research questions, highlighting formalizations, gaps, objections, phenomena, and tools.

#### Literature on Innovation and Entry of Forms
Work on how forms enter a community's repertoire spans several subfields, with grammaticalization as a central mechanism. Grammaticalization involves the development of lexical items into grammatical markers, often through unidirectional clines (e.g., content word > function word > affix). Formal models include Lehmann's (1982/1995) parameters of weight, cohesion, and variability, where forms gain obligatoriness and scope via reanalysis. Regine Eckardt's formal semantics approach treats reanalysis as discrete semantic shifts at the syntax-semantics interface, driven by implicatures in ambiguous utterances. For instance, the English "be going to" evolves from a progressive motion verb to a future operator through reinterpretation, where old denotations are conserved, and new meanings fill compositional gaps. This process allows forms to enter repertoires by recruiting lexical material for grammatical functions, stabilized via community adoption.

Contact linguistics addresses entry via borrowing and code-switching, where forms from one language integrate into another's repertoire. Thomason and Kaufman's (1988) model formalizes this as intensity-based scales, from casual loans to structural shifts in intense contact scenarios. Analogical extension, common in morphology, enables entry through pattern generalization; Bybee's (2009) work links this to usage-based theory, where high-frequency exemplars drive analogies, informing a dynamic view of language where grammaticization suggests token repetition leads to entrenchment. In L1 acquisition, overgeneralizations (e.g., "goed" for "went") can be retained if they fill niches, as modeled in Yang's (2017) variational learning, where tolerance parameters allow innovations to spread if not preempted.

Formalizations exist but are patchy: Eckardt uses lambda calculus for semantic compositions (e.g., λPλx[IMMINENT(R,^P(x))] for futures), emphasizing unidirectionality without reversals. In cultural evolution, iterated learning models (e.g., Kirby et al., 2014) simulate entry via transmission chains, where biases like compressibility introduce systematicity.

#### Asymmetry Between Entering and Exiting the Repertoire
Theoretical reasons for asymmetry abound, with exclusion often easier than entry. Frequency effects play a key role: rare forms are vulnerable to preemption due to low exposure, while common ones are protected by entrenchment and coordination. In grammaticalization, unidirectionality enforces asymmetry--forms grammaticalize but rarely degrammaticalize, as reanalysis increases scope and bondedness without easy reversal. Bayesian learning amplifies this: indirect negative evidence efficiently excludes forms via absence in input, but entry requires positive evidence or innovation, which is rarer. Game-theoretic models suggest entry needs "invasions" (new strategies with fitness edges), while exclusion follows from stable equilibria where deviations fail. Historical linguistics notes innovations spread via waves or gravity (population-driven), but extinctions accelerate in competition, as in minority language decline. Beyond coordination, social status and bilingualism buffer common forms, per Abrams-Strogatz models.

#### Literature Gaps and Relevant Work
From game theory, Lewis signaling games model norm emergence as coordination on efficient signals, extended in evolutionary game theory (EGT) to population dynamics where strategies replicate based on payoffs. Bicchieri's (2005) social norm models apply to establishment/extinction, with thresholds for tipping points. Cultural evolution fills gaps via agent-based simulations: Steels (2011) models self-organization in language games, where innovations emerge from interactions and stabilize through alignment. Iterated learning (Kirby, 2001) shows how biases lead to composable structures, explaining norm establishment without innate primitives.

Sociolinguistics offers Haugen's (1950) standardization model: selection, codification, implementation, elaboration for norm establishment; extinction ties to prestige loss. Labov's quantitative paradigm tracks variation, but formal models are rare--e.g., degree-biased voter models with innovation for spread/extinction. Acquisition literature emphasizes indirect evidence: Pearl and Goldwater (2011) use Bayesian inference to incorporate subset principles, constraining overgeneralization. Rohde and Plaut (1999) show connectionist networks learn without explicit negatives.

Historical linguistics contrasts spread (wave/gravity models) with extinction (competition fronts): Burridge (2018) unifies them via surface tension dynamics, predicting radiation or gravity-based shifts. Patriarca et al. (2010) use ecophysics for diversity/competition, with Lotka-Volterra equations for exclusion.

| Model Type | Key Work/Example | Application to Arise | Application to Exclude | Application to Stability |
|------------|------------------|----------------------|-------------------------|--------------------------|
| Game Theory | Lewis Signaling Games | Mutations introduce new signals | Inefficient strategies die out | Equilibria sustain norms |
| Bayesian Learning | Pearl & Goldwater (2011) | Overgeneralizations as entry points | Indirect evidence preempts | Entrenchment via priors |
| Cultural Evolution | Kirby et al. (2014) | Iterated biases create forms | Competition filters unfit | Population structure preserves |
| Ecophysics | Patriarca et al. (2010) | String mutations originate | Thresholds drive extinction | Spatial segregation coexists |
| Historical | Burridge (2018) | Wave radiation spreads | Gravity excludes minorities | Fronts maintain boundaries |

#### Potential Objections and Conceptual Vulnerabilities
Strongest objections include determinism: the framework treats outcomes as stable equilibria, but real change is probabilistic, influenced by individual agency or external shocks (e.g., migration). Conceptual vulnerability lies in the "feeling" (F) as mediator--critics argue it's epiphenomenal, not causal, per Chomskyan innatism vs. emergentism debate. Overemphasis on preemption ignores positive reinforcement in entry; asymmetry may be overstated if revivals (e.g., Hebrew) show exclusions aren't irreversible. Measuring C_t empirically is vague--how to quantify "repertoire status" beyond corpus frequency? Game-theoretic assumptions of rationality may not hold in cultural contexts.

#### Phenomena the Framework Should Handle but Might Struggle With
Stable innovations: Neologisms like "selfie" spread rapidly via media, but the framework lacks social network models for viral entry. Unstable exclusions: Forms like archaic pronouns revive in niches (e.g., "thou" in dialects), challenging preemption's finality. Reversals: Language shifts reverse under policy (e.g., Catalan revival), requiring integration of power dynamics. Multilingual repertoires complicate C_t, as code-switching sustains "excluded" forms. The model might struggle with creolization, where new systems arise from contact without clear preemption.

#### Formalization Tools to Sharpen Predictions
Evolutionary game theory (EGT) offers replicator dynamics for the "arise" side: mutations introduce variants, spreading if payoff > average (e.g., Maynard Smith, 1982). Cultural evolution modeling uses agent-based simulations (e.g., naming games) to predict entry via alignment thresholds. Bayesian learning refines preemption: priors on sampling assumptions (size vs. strong) affect evidence use, enabling probabilistic C_t trajectories. Ecophysics tools like Lotka-Volterra equations model competition: dx/dt = x(1-x) - sxy, predicting stability thresholds. For integration, hybrid models (e.g., EGT + Bayesian) could simulate doubly/singly-sustained states, sharpening predictions on drift.

**Key Citations:**
- [Grammaticalization | Oxford Research Encyclopedia of Linguistics](https://oxfordre.com/linguistics/display/10.1093/acrefore/9780199384655.001.0001/acrefore-9780199384655-e-103)
- [Grammaticalization and models of language - John Benjamins](https://www.jbe-platform.com/content/books/9789027288448-tsl.90.14vin)
- [Grammaticization: implications for a theory of language](https://www.unm.edu/~jbybee/downloads/Bybee2009Gramtion.pdf)
- [Grammaticalization and Semantic Reanalysis Regine Eckardt](https://semanticsarchive.net/Archive/GRmOWZmN/SemanticReanalysis.pdf)
- [Applications of Game Theory in Linguistics](https://profgerhard.de/sfs/publications/compass.pdf)
- [Negative evidence in language acquisition - Wikipedia](https://en.wikipedia.org/wiki/Negative_evidence_in_language_acquisition)
- [Statistical Learning, Inductive Bias, and Bayesian Inference...](https://sites.socsci.uci.edu/~lpearl/papers/PearlGoldwater2011Manu_InferenceDevLing.pdf)
- [Indirect negative evidence - Faculty of Language](http://facultyoflanguage.blogspot.com/2016/04/indirect-negative-evidence.html)
- [Unifying models of dialect spread and extinction using surface tension dynamics](https://royalsocietypublishing.org/rsos/article/5/1/171446/93561/Unifying-models-of-dialect-spread-and-extinction)
- [Evolutionary Game Theory for linguists. A primer](https://profgerhard.de/sfs/publications/egtPrimer.pdf)
- [Cultural evolutionary modeling of patterns in language change](https://www.lotpublications.nl/Documents/223_fulltext.pdf)
- [Diversity, competition, extinction: the ecophysics of language change - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC2988263/)
- [Language standardization in sociolinguistics and international business](https://vbn.aau.dk/ws/files/288222813/Linn_Sanden_Piekkari_Language_standardization_in_sociolinguistics_and_international_business.pdf)
- [Clarifying the logical problem of language acquisition - Steven Pinker](https://stevenpinker.com/files/pinker/files/jcl_macwhinney_commentary.pdf)
- [A model of norm emergence and innovation in language change](https://dl.acm.org/doi/10.5555/2031678.2031716)
