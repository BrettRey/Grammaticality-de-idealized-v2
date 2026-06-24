Your two modules already give you most of what you need for *stability* and a principled account of *exit*. The missing piece on the *arise* side is not “what kinds of innovation exist” (you already list them), but a story about how an initially rare variant crosses the coordination threshold *despite* (i) weak positive evidence, (ii) sanctions/markedness, and (iii) competition from entrenched incumbents.

A useful way to make that gap tractable is to separate *supply* from *invasion*:

1. Supply: how do tokens of a form get produced at all (innovation, contact injection, analogical extension, reanalysis, performance noise, stylistic play, repair, etc.)?

2. Invasion (threshold-crossing): when does a supply stream turn into a self-sustaining convention (i.e., C_t begins to climb endogenously)?

Your current coordination module handles what happens *after* invasion: once the form is above threshold and mutually expected, it persists. What’s missing is an explicit “crossing the basin boundary” mechanism.

Below I organise what I think are the most relevant formal and semi-formal literatures, why asymmetry is actually expected on fairly weak assumptions, and what I’d treat as the hardest conceptual objections / stress-test phenomena.

---

Arise as basin-crossing in a coordination landscape

If you model community use as a coordination game (explicitly or implicitly), then *entry* is typically hard because a rare variant is, by default, a bad best response: when almost nobody uses it, using it is costly (misunderstanding, social penalty, processing penalty), so selection drives it back toward zero. That’s the familiar “new convention can’t invade” problem in coordination games.

The standard modelling move is to add one of the following “escape hatches”:

A) Mutation / invention: a small but persistent probability that speakers produce the rare form anyway (noise, creativity, analogy, contact). In evolutionary game theory this is the *mutator* term; in learning models it’s a production channel not fully determined by current expectations. Under mutation, the system becomes a stochastic process that can (rarely) move between equilibria, and you can ask which equilibria are stochastically stable. The stochastic stability programme (Foster & Young; Young; Kandori–Mailath–Rob) is basically an equilibrium selection theory for exactly this situation. ([repository.upenn.edu][1])

B) Payoff advantages when rare: the innovation is not a pure coordination alternative, but offers some benefit that is available even when it is rare (e.g., it fills an empty niche, reduces ambiguity, reduces articulatory cost, enables a social-indexical stance, etc.). This converts “entry is impossible” into “entry requires the advantage to outweigh rarity costs”.

C) Structured diffusion / threshold adoption: adoption is not well approximated by homogeneous mixing. In network models, some traits behave as *complex contagions* (needing reinforcement from multiple sources before adoption), which changes which social structures accelerate spread. This is relevant if using a novel form carries social risk: a single exposure might not shift anyone’s production policy, but repeated exposures from multiple peers can. ([journals.uchicago.edu][2])

D) Iterated learning / acquisition bottlenecks: when learners reconstruct grammars from sparse data, small biases get amplified across generations; structure and regularities can emerge even if not “selected for” in adult interaction. Iterated learning models give you a mathematically clean way to connect acquisition dynamics to population-level trajectories. ([Cognitive Science Lab][3])

The point is that the *arise* side often needs one of A–D (usually a mixture). Your two-module theory has (a version of) B on the *exit* side via effective opportunity mass and preemption, and has the “within-equilibrium” part of coordination; the missing piece is making A/C/D explicit for how a new form (or reanalysed mapping) starts accumulating enough mutually reinforcing exposure to push C_t upward.

---

1. Innovation/entry: formalisations worth mining

I’ll group this by what they formally deliver, because that maps onto what you need.

A. Convention emergence in game-theoretic / multi-agent models

These literatures treat entry as the emergence of a shared mapping under repeated interaction, with explicit mechanisms for invention and reinforcement.

* Lewisian conventions / coordination foundations: Lewis’ analysis makes linguistic conventions a species of coordination regularity. Even if you don’t adopt his philosophical programme, it gives you a clean link between “community repertoire” and equilibrium selection in repeated coordination settings. ([eclass.upatras.gr][4])

* Signalling games with evolutionary/learning dynamics: Skyrms develops signalling games with replicator dynamics and learning, and explicitly discusses how signalling systems can grow via invention (new signals) and then stabilise. That is very close in spirit to your entry problem: how do new form–meaning pairings appear and become conventional? ([sites.socsci.uci.edu][5])

* Naming Game models (Steels and successors): the Naming Game is a canonical formal model of how populations converge on a shared lexicon via local interactions, including invention, alignment, and competition between variants. It’s lexicon-first, but the dynamics (invention → reinforcement → convergence) are exactly the shape you need for “arise”. ([martin-loetzsch.de][6])

What you can steal for C_t:

* A micro-update rule for how interaction outcomes change agents’ production probabilities.
* A principled sense in which entry is *phase-transition-like* (below some exposure density it dies out; above it, it locks in).

B. Population-level dynamics of linguistic variants: S-curves, diffusion mechanisms, and selection vs drift

This literature gives you explicit equations for trajectories like logistic/S-curves, and tools for distinguishing “neutral drift” from biased propagation.

* Blythe & Croft’s modelling of S-curves and propagation mechanisms is directly about mapping different micro-mechanisms (neutral drift, selection, social weighting, etc.) onto characteristic change trajectories. If you want C_t predictions that can be confronted with time-series data, this is highly relevant. ([semanticscholar.org][7])

* Baxter et al. style models: mathematical models tied to usage-based evolutionary framing (Croft) and applied to dialect formation (e.g., New Zealand English). This is useful because it puts “innovation in small subgroups + diffusion” into a quantitative framework. ([Research Explorer][8])

* Niyogi & Berwick (population-level acquisition/change): whatever your metatheoretical stance, the key contribution is a formal bridge between learning algorithms and population trajectories, with explicit discussion of iterated learners in a population setting. ([PNAS][9])

C. Iterated learning and cultural evolution

Iterated learning gives you an explicit account of how new regularities can emerge because learners reconstruct structure from data, and why small biases can become large-scale conventions.

* Kirby, Griffiths & Smith review the iterated learning framework and its consequences (including convergence properties under Bayesian learners). This is one of the cleanest “arise” formalisations because entry can be driven by learner biases (simplicity, compressibility, communicative efficiency) even when the innovation is not strongly selected in adult interaction. ([Cognitive Science Lab][3])

* Perfors–Tenenbaum–Wonnacott on Bayesian learning of constructions with negative evidence in play: the hierarchical Bayesian framing is useful if you want a formal “belief about licensing” layer that sits right under your F signal. ([Massachusetts Institute of Technology][10])

D. Acquisition regularisation and the creation/elimination of variability

If your C_t is repertoire status, then acquisition is an obvious driver: children can either reproduce variability or regularise it; regularisation can be a mechanism for both exclusion and (in some settings) innovation.

* Hudson Kam & Newport show that learners (especially children) regularise unpredictable variation in inconsistent input—systematically changing the distribution of forms. This is a formal/experimental foothold for an inherent asymmetry: variable systems are pulled toward more regular, more categorical distributions by learning biases. ([sites.socsci.uci.edu][11])

E. Productivity/analogy as entry into the productive repertoire

Your C_t question is not just “is a token attested?” but “is it part of the productive system?”. Quantitative morphology has tools that are basically about that transition.

* Baayen on morphological productivity: formal measures of how “open” a process is and how productivity relates to frequency distributions. If you want to operationalise C_t (or part of it) empirically, this literature gives you principled links between type frequency, token frequency, and productive availability. ([Quantling][12])

* Albright & Hayes’ probabilistic/rule induction models: even if you don’t buy their architectural conclusions, the machinery gives you a concrete way to model analogical extension as probabilistic generalisation over a lexicon. That can be repurposed as a mechanism for C_t increase: the rule becomes reliable enough that speakers extend it to new items, and learners infer it as licensed. ([Bruce Hayes][13])

F. Grammaticalisation / constructional change and contact as structured sources of “supply”

These are less often *mathematically* formalised in the classic sense, but they provide well-worked causal pathways that you can treat as generators of innovation tokens and new niches.

* Constructionalisation / constructional change: Traugott & Trousdale provide a detailed usage-based account of how new constructions arise and stabilise (including the role of context and gradual shifts). This is directly relevant to your entry side because it gives you a rich typology of “how new form–function pairings appear”. ([Unisalento][14])

* Grammaticalisation: Hopper & Traugott is still a central synthesis of mechanisms and pathways; you can treat grammaticalisation pathways as systematic “innovation generators” that change mapping viability and niche structure over time. ([Cambridge University Press & Assessment][15])

* Contact-induced change: Heine & Kuteva and Thomason & Kaufman give frameworks for how contact injects material and structures, i.e., raises the supply rate of otherwise absent forms and provides social conditions where sanction costs differ. ([Cambridge University Press & Assessment][16])

A practical upshot: you can model these as exogenous shocks to the innovation/mutation term (A above) and/or to niche payoffs (B above), rather than trying to “formalise grammaticalisation” from scratch.

---

2. Why asymmetry between entering and exiting is actually expected

There are at least four distinct reasons to expect asymmetry, and they’re separable (so an objection to one doesn’t kill the others).

A. Evidence asymmetry: “absence as evidence” can be strong; “presence” needs supply

Your exit module already relies on indirect evidence: if an opportunity repeatedly arises and the competitor wins, learners infer the target is unlicensed. That’s a general feature of Bayesian inference with a detection model: if you expected to see X in contexts where it would fit, and you reliably don’t, the posterior can collapse quickly. Yang explicitly frames this as “negative knowledge from positive evidence” in an acquisition setting. ([sites.socsci.uci.edu][17])

On the flip side, entry requires a supply stream of tokens. Without innovation/contact/analogy generating tokens, there is nothing for Bayesian updating to work on. So “exit can be triggered by structured absence” whereas “entry cannot be triggered by structured absence alone”.

B. Coordination asymmetry: invasion barriers in coordination games

Even if a form is viable and interpretable, when it is rare it is typically not a best response in a coordination landscape. The classic equilibrium-selection results with stochastic perturbations show how conventions can persist, and how switching equilibria depends on mutation rates and risk dominance. Young (and the broader stochastic stability literature) is directly about why established conventions resist invasion. ([JSTOR][18])

So there is a structural asymmetry: once a convention is entrenched, the basin of attraction makes exit hard—but that same basin makes *entry* hard for a novel alternative.

C. Learning asymmetry: regularisation pulls distributions toward fewer variants

Hudson Kam & Newport-style results suggest a bias toward reducing unpredictable variation, which is naturally an “exit-friendly” force (pruning competitors) and not automatically an “entry-friendly” force (creating new alternations). ([sites.socsci.uci.edu][11])

This is relevant to your asymmetry question because even if “innovation happens”, learners may preferentially *collapse* variants unless the variation becomes predictable/functional/socially meaningful.

D. Social-norm asymmetry: sanctions make deviation costly, but only once a norm exists

Bicchieri’s social norms framework is useful here: norms are sustained by expectations and conditional preferences; sanctions make deviation costly, but the sanctioning logic itself depends on shared expectations. That yields a natural hysteresis: before a norm is widespread, sanctions are weak/uncertain; once widespread, sanctions become stable and deviation is punished. ([hugoribeiro.com.br][19])

Put differently: your coordination module already builds in a kind of path dependence; formal norm theory gives you a way to articulate why the penalty function changes endogenously as C_t rises.

---

3. Additional literatures and “missing” toolkits that plug directly into your questions

A. Norm establishment/extinction beyond simple coordination

* Stochastic stability / equilibrium selection: Foster & Young (1990), Young (1993), Kandori–Mailath–Rob (1993) give you ways to talk about which equilibria are selected in the long run under mutation and learning. This is exactly “why does a community settle here rather than there?”. ([repository.upenn.edu][1])

* Threshold models of collective behaviour and complex contagion: Granovetter’s threshold model gives you a clean formalism for “people adopt only after enough others adopt”; Centola & Macy show how needing multiple confirmations changes diffusion. This is a natural fit if adopting a novel form is socially risky (your “unilateral deviation is penalised” claim). ([cse.cuhk.edu.hk][20])

B. Learning-theoretic work on indirect evidence / absence

* Yang (2015) is directly about how learners infer ungrammaticality from distributional patterns. ([sites.socsci.uci.edu][17])
* Perfors et al. provide a hierarchical Bayesian treatment where variability and (indirect) negative evidence matter for learning argument structure constructions. ([Massachusetts Institute of Technology][10])
* If you want a clean general Bayesian statement of when “absence is evidence”, Stephens gives a discussion in explicitly Bayesian terms (not linguistics-specific, but it’s conceptually clarifying for how your “effective opportunity mass” licenses strong inference from non-occurrence). ([informallogic.ca][21])

C. Sociolinguistics of innovation spread via social meaning

Your coordination module treats sanctions as primarily about conventionality/grammaticality. But innovations often spread because they *mean* something socially; in that case “deviation” is not merely tolerated but strategically valuable.

* Eckert’s work on variation as a system of social meaning is a direct route to modelling payoffs that are not purely communicative efficiency. In your terms, this is a route by which a form can have a payoff advantage even when rare (because it indexes stance/identity). ([justinecassell.com][22])

D. Formal historical change trajectories

If you want to tie C_t to empirical trajectories (corpus-based), the S-curve literature and mechanisms-of-propagation work is relevant.

* Blythe & Croft on what micro-mechanisms are needed to get S-curves. ([semanticscholar.org][7])
* Ghanbarnejad et al. on extracting endogenous/exogenous contributions from S-curves (bridges to complex-systems modelling). ([PMC][23])
* Baxter et al. on lifespan/community change modelling, including age-graded flexibility parameters (useful if your C_t is partly an intergenerational learning outcome). ([Cambridge University Press & Assessment][24])

E. Extinction / loss models you can cannibalise

Even though Abrams & Strogatz model language competition (not intra-language forms), it’s a clean example of how prestige/utility parameters can drive extinction trajectories. The formal move—frequency-dependent switching under social status—ports to within-language variants. ([Nature][25])

---

4. Strong objections and conceptual vulnerabilities

Here are the objections I’d expect to be hardest to parry cleanly unless you bake accommodations into the theory.

A. Scalar C_t vs heterogeneity (register, subgroup, style, stance)

If C_t is a single community scalar, you risk collapsing stable structured heterogeneity into “instability”. Many “low C_t” forms are stable within registers or communities-of-practice, and many “high C_t” forms are only high in a standard register. Eckert-style enregisterment/indexicality is an existence proof that variant stability can be driven by social meaning rather than mere coordination on a single norm. ([Stanford University][26])

What this forces: C_t probably has to be conditionalised—at least C_t(form | register, group, activity type)—or else you need an explicit mixture model (a community is a weighted set of partially overlapping equilibria).

B. The role of F: is the “feeling of ungrammaticality” the right proximate signal?

Two related risks:

* People often produce forms they report as “bad” under reflection, especially under style-shifting, quotation, jocular registers, or strategic identity work. If F is treated as the sole driver, you may mispredict persistence of stigmatised but socially functional variants.

* Judgement *instability* can be driven by processing/surprisal effects rather than repertoire status. If a form is rare, it’s surprising; surprise can feel like ungrammaticality even when the grammar licenses it. That makes F partly an epistemic signal about expectation rather than a direct signal of grammatical constraint.

Your framework can survive this, but only if F is explicitly decomposed (e.g., into expectation/surprisal, social evaluation, and mapping-viability components), or if you treat F as a composite utility signal rather than a dedicated grammaticality detector.

C. “Competitor consistently wins” is not always the right picture of exit

A lot of loss is *niche loss* rather than competitive exclusion: the relevant communicative situations stop arising (semantic/pragmatic change, cultural change, technological change), so opportunities vanish and the form drifts down without being preempted by an explicit competitor. Your “effective opportunity mass” can handle this if it allows the mass to go to ~0 (no opportunities), but then the mechanism is not “preemption”; it’s “no reinforcement + drift + acquisition bottleneck”.

D. Institutional and metalinguistic forces can reverse dynamics

Standardisation, schooling, prescriptivism, and orthography can impose penalties or subsidies that do not arise endogenously from local interaction alone. If your causal story is purely decentralised interaction, you’ll need a way to represent “centralised payoff shocks” (which can drive reversals and stable high-C_t maintenance of low-frequency forms).

E. Contact as non-Bayesian evidence injection

Contact can flood the input with a form without it being locally optimal, and can shift sanction structures. Treating everything as endogenous Bayesian updating from local opportunities can miss this “supply shock + prestige” pathway unless you explicitly include exogenous token influx and social weighting (which Blythe & Croft treat as distinct propagation mechanisms). ([semanticscholar.org][7])

---

5. Stress-test phenomena: what your framework should cover but may struggle with

A. Stable low-frequency innovations

Examples include discourse markers, stance markers, and socially-indexed alternants that remain minority variants but persist for decades. These look like *polymorphic equilibria* (stable variation) rather than a single equilibrium with noise. Blythe & Croft explicitly distinguish stable variation vs change and tie it to social weighting. ([semanticscholar.org][7])

B. Unstable exclusions (forms that “should” stay out but keep reappearing)

Some excluded forms recur because the innovation supply is high (analogy keeps generating them) or because they have a processing/expressive advantage that keeps pushing them back in. In your terms: high mutation pressure can prevent C_t from reaching zero even under preemption.

C. Reversals / “resurrections”

Forms can re-enter the repertoire via:

* contact injection (supply shock),
* prestige reversal (payoff reversal),
* institutional enforcement,
* niche creation (new meaning niche appears).

The formal challenge is that these are exogenous parameter shifts in your dynamics; you need the theory to predict *which* parameters matter and how big a shift is needed to cross back over the basin boundary.

D. Multiple competitors and near-synonymy

Preemption is cleanest with a single strong competitor. In practice, niches can be filled by a set of partial competitors. This can make exclusion slower, more gradient, and more context-sensitive—potentially producing “pockets” of C_t stability even when aggregate C_t is falling.

E. Innovation without obvious communicative advantage

A lot of change is not obviously “better” functionally. Neutral drift models (Baxter/Blythe/Croft/McKane traditions) give you a way to explain this, but then your “arise” module must allow drift-driven invasion under stochasticity, not only selection-driven invasion. ([Research Explorer][8])

---

6. Concrete formalisation moves that sharpen “arise” predictions

Here are three modelling patterns that connect tightly to your existing machinery, with minimal new ontology.

A. Replicator–mutator coordination model for C_t

Let x_t be the community usage probability of the innovative form (as a proxy for C_t), with two forces:

* Selection/coordination: payoffs depend on matching community expectations (your stability module).
* Mutation/innovation: speakers sometimes produce the innovative form even when it’s not currently expected (your missing supply channel).

In evolutionary game terms, this is a replicator–mutator dynamic; you can use stochastic stability to predict which equilibrium is selected under low mutation. This directly gives you:

* invasion thresholds,
* hysteresis (entry harder than exit),
* conditions for persistent low-frequency variants (when mutation pressure balances selection against rarity). ([personal.math.ubc.ca][27])

B. Threshold/complex-contagion diffusion layered on your sanction idea

If adopting/using a new form is socially risky, then model adoption as requiring k exposures (or k distinct sources) before an individual updates their production policy. That is exactly the Granovetter/complex-contagion formalism, and it yields sharp predictions about:

* why some innovations spread only in clustered networks,
* why “weak ties” sometimes accelerate and sometimes inhibit change,
* why innovations can remain locally stable without global takeover. ([cse.cuhk.edu.hk][20])

This is, in effect, a formal version of “coordination penalty blocks unilateral deviation” with an explicit adoption rule.

C. Bayesian iterated learning with an explicit innovation channel

You already have Bayesian updating for *exit*. For *entry*, add a generative model in which:

* speakers sometimes produce an innovative form with probability μ(context), where μ is higher in “niche pressure” contexts (repair, ambiguity, expressive needs, contact contexts, etc.);
* learners update a hypothesis about licensing/viability given sparse data.

Iterated learning results tell you what happens under repeated transmission: languages converge toward learners’ priors/biases in the absence of strong functional selection, and toward a balance of priors and communicative pressures when communication is included. This gives you a principled route to “stable innovations” that are learnability-favoured even if not initially frequent. ([Cognitive Science Lab][3])

D. A symmetry-breaking bridge to your effective opportunity mass

Your exit variable is “effective opportunity mass” for contexts where the form would have been suitable but a competitor wins.

For arise, the natural dual is something like:

* effective niche gap mass: contexts where existing repertoire options are counterfactually *less* suitable (ambiguity, cost, expressive mismatch), weighted by the magnitude of mismatch.

Then predict:

* innovation supply rate rises with niche gap mass,
* invasion probability rises when niche gap mass is high *and* coordination penalties are locally weakened (e.g., within a subgroup, a register, or a contact setting),
* once x_t clears a threshold, your existing coordination mechanism locks it in.

This gives you a formal pathway from “communicative pressure + local social ecology” to C_t increases without pretending entry is simply the reverse of preemption.

---

A compact “reading map” aligned to your six questions

If you want a short list that covers most of the formal space quickly:

* Statistical preemption / learning what not to say: Goldberg on corpus evidence for statistical preemption; and Yang on negative knowledge from positive evidence. ([Lang Osaka University][28])
* Norm emergence and equilibrium selection: Lewis (convention), Young (stochastic stability), Kandori–Mailath–Rob (learning/mutation long-run equilibria), Bicchieri (norm dynamics). ([eclass.upatras.gr][4])
* Entry via invention + interaction: Steels / Naming Game; Skyrms signalling games with invention. ([martin-loetzsch.de][6])
* Cultural evolution / iterated learning: Kirby–Griffiths–Smith. ([Cognitive Science Lab][3])
* Diffusion trajectories and mechanisms: Blythe & Croft; Ghanbarnejad et al. on S-curves. ([semanticscholar.org][7])
* Learner-driven distributional reshaping (asymmetry lever): Hudson Kam & Newport regularisation. ([sites.socsci.uci.edu][11])
* Social meaning as payoff structure (why rare innovations can be advantageous): Eckert. ([justinecassell.com][22])

---

If you want one concrete next step that would immediately sharpen the “arise” side without ballooning the framework: import a threshold/complex-contagion adoption rule into your coordination module, and add a minimal innovation/mutation channel whose rate is proportional to an “effective niche gap mass”. That gives you a mathematically explicit basin-crossing story, explains asymmetry non-hand-wavingly (hysteresis + evidence asymmetry), and makes room for social-meaning payoffs as a way for innovations to be beneficial even when rare.

[1]: https://repository.upenn.edu/bitstreams/cfcfcbfc-775a-4b32-989d-59bd85a085ec/download?utm_source=chatgpt.com "Stochastic Evolutionary Game Dynamics"
[2]: https://www.journals.uchicago.edu/doi/abs/10.1086/521848?utm_source=chatgpt.com "Complex Contagions and the Weakness of Long Ties1"
[3]: https://cocosci.princeton.edu/tom/papers/IteratedLearningEvolutionLanguage.pdf?utm_source=chatgpt.com "Iterated learning and the evolution of language"
[4]: https://eclass.upatras.gr/modules/document/file.php/CEID1184/0%20%CE%93%CE%B5%CE%BD%CE%B9%CE%BA%CE%AC/David%20Lewis%20-%20Convention_%20A%20Philosophical%20Study%20%282002%2C%20Wiley-Blackwell%29.pdf?utm_source=chatgpt.com "Convention | A Philosophical Study - David Lewis"
[5]: https://sites.socsci.uci.edu/~bskyrms/bio/books/signals.pdf?utm_source=chatgpt.com "SIGNALS"
[6]: https://martin-loetzsch.de/publications/steels12grounded.pdf?utm_source=chatgpt.com "The Grounded Naming Game"
[7]: https://www.semanticscholar.org/paper/S-curves-and-the-mechanisms-of-propagation-in-Blythe-Croft/798b82e08c71f71e1946e3ad936b2c7423127018?utm_source=chatgpt.com "S-curves and the mechanisms of propagation in language ..."
[8]: https://research.manchester.ac.uk/en/publications/modeling-language-change-an-evaluation-of-trudgills-theory-of-the?utm_source=chatgpt.com "Modeling language change: An evaluation of Trudgill's theory ..."
[9]: https://www.pnas.org/doi/abs/10.1073/pnas.0903993106?utm_source=chatgpt.com "The proper treatment of language acquisition and change ..."
[10]: https://web.mit.edu/cocosci/archive/Papers/vcpaper-forweb-finaldec09.pdf?utm_source=chatgpt.com "Variability, negative evidence, and the acquisition of verb ..."
[11]: https://sites.socsci.uci.edu/~lpearl/courses/readings/HudsonKamNewport2005_RegularizingUnpredictableVariation.pdf?utm_source=chatgpt.com "Hudson Kam Newport"
[12]: https://quantling.org/~hbaayen/publications/BaayenHSK2009.pdf?utm_source=chatgpt.com "morphological productivity R. Harald Baayen (Baayen, 43) 1"
[13]: https://brucehayes.org/papers/AlbrightHayes2003RulesVsAnalogy.pdf?utm_source=chatgpt.com "Rules vs. analogy in English past tenses"
[14]: https://www.unisalento.it/documents/20152/4991507/Traugott%2Be%2Btrousdale%2BRefencia%2Bbasica.pdf/86cf671e-a26c-396f-6635-804ba71f3fe8?download=true&version=1.0&utm_source=chatgpt.com "Constructionalization and Constructional Changes"
[15]: https://www.cambridge.org/core/books/grammaticalization/420C6D59856F8020065C275312FE2E1B?utm_source=chatgpt.com "Grammaticalization"
[16]: https://www.cambridge.org/core/books/language-contact-and-grammatical-change/167D47802E87FAF5871D94AE065CB277?utm_source=chatgpt.com "Language Contact and Grammatical Change"
[17]: https://sites.socsci.uci.edu/~lpearl/courses/readings/Yang2015_NegFromPosEvidence_AAdjectives.pdf?utm_source=chatgpt.com "Negative Knowledge from Positive Evidence"
[18]: https://www.jstor.org/stable/2951778?utm_source=chatgpt.com "The Evolution of Conventions"
[19]: https://hugoribeiro.com.br/area-restrita/Bicchieri-The_grammar_of_society-nature_and_dynamics_social_norms.pdf?utm_source=chatgpt.com "Bicchieri-The_grammar_of_society- ..."
[20]: https://www.cse.cuhk.edu.hk/~cslui/CMSC5734/Granovetter-threshold_models.pdf?utm_source=chatgpt.com "Threshold Models of Collective Behavior Mark Granovetter ..."
[21]: https://informallogic.ca/index.php/informal_logic/article/view/2967/2516?utm_source=chatgpt.com "A Bayesian Approach to Absent Evidence Reasoning"
[22]: https://www.justinecassell.com/discourse09/readings/EckertLSA2005.pdf?utm_source=chatgpt.com "Variation, convention, and social meaning 1. Introduction"
[23]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4223929/?utm_source=chatgpt.com "Extracting information from S-curves of language change - PMC"
[24]: https://www.cambridge.org/core/journals/language-variation-and-change/article/modeling-language-change-across-the-lifespan-individual-trajectories-in-community-change/41CB5D788EAE99FD1831D44848DE77D9?utm_source=chatgpt.com "Modeling language change across the lifespan: Individual ..."
[25]: https://www.nature.com/articles/424900a?utm_source=chatgpt.com "Modelling the dynamics of language death"
[26]: https://web.stanford.edu/~eckert/PDF/ThreeWaves.pdf?utm_source=chatgpt.com "Three Waves of Variation Study"
[27]: https://personal.math.ubc.ca/~hauert/publications/preprints/traulsen_09.pdf?utm_source=chatgpt.com "Stochastic evolutionary game dynamics"
[28]: https://www.lang.osaka-u.ac.jp/~sugimoto/M%26D2011/CoglVol22/COGL.2011.006.Goldberg.pdf?utm_source=chatgpt.com "Corpus evidence of the viability of statistical preemption"
