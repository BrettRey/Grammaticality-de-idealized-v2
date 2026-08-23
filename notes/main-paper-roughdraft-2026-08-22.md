# Grammaticality de-idealized
> Roughdraft review companion generated from `main.tex` on 2026-08-22. Comments here will be applied to the LaTeX source; this file is not the publication source.
## Abstract
Why is _I have 25 years_ easy to understand but ungrammatical in English, while _Colorless green ideas sleep furiously_ is grammatical despite its odd meaning? I argue that grammaticality research often runs together four questions. Does the language provide an analysis for the expression? Do the grammatical contributions of its parts fit together? Does it mark the contrasts required in this context? Is the construction established in this speech community and situation? Processing difficulty and implausibility are separate: they can lower acceptability without changing grammatical status. The Operator-Value Model of Grammaticality (OVMG) formalizes these distinctions and models how use, competition among alternatives, and forgetting change the constructions available to a population. It predicts that rarely encountered constructions should respond more to exposure and framing than forms consistently displaced by an established competitor; that the absence of a form is evidence of ungrammaticality only when speakers repeatedly chose an established alternative in contexts where the missing form would have been a plausible choice; and that, as a contrast becomes moribund, the evidence sustaining it should weaken before its categorical status changes. Simulations show that sharply separated population patterns can arise under specified adoption conditions, but not from Bayesian updating alone. The proposal replaces the ideal speaker's single grammaticality fact with distinct, testable claims about structure, convention, speaker experience, and change.

**Keywords:** grammaticality; projectibility; acceptability; preemption; entrenchment; conventionalization; usage-based grammar
# Introduction
Every competent speaker of English knows that *_Can the have running_ is impossible, but the source of this certainty proves remarkably elusive. What does it mean to say a sentence is ungrammatical? Consider these examples:

*_Can the have running?_ _Colorless green ideas sleep furiously._ *_I’ve finished it yesterday._ ?_I saw Joan, a friend of whose was visiting._ _The bread the baker the apprentice helped made is delicious._ **A:** _How old are you?_ **B:** *_I have 25 years._ *_Which did you buy car?_

While all might receive asterisks in many analyses, they represent fundamentally different types of unacceptability. Some constructions, like ([[ex:nonsense]](#ex:nonsense)), fail to establish any form–value relationship in English. Others, like ([[ex:tense]](#ex:tense)), involve incompatible operator contributions: the present perfect’s reference-interval contribution doesn’t unify with _yesterday_’s deictic anchoring. Still others, such as ([[ex:whose]](#ex:whose)), show gradient or indeterminate status. ([[ex:center]](#ex:center)) illustrates what might be called predicted grammatical but reliably rejected: constructions that linguistic theory predicts should be grammatical but that are consistently rejected by native speakers in ordinary judgment tasks. Still others, like ([[ex:age]](#ex:age)), are readily interpretable and grammatical in related languages but lack licensing in English age predication. And a few, like the left-branch extraction of ([[ex:lbe]](#ex:lbe)), seem to be ruled out entirely, despite being apparently short and interpretable.

Different traditions emphasize different pieces: formal approaches focus on abstract principles, usage-based theories on frequency and entrenchment, processing accounts on cognitive constraints. Each captures part of the picture, but none unifies categorical constraints, gradient acceptability, cross-linguistic variation, and change over time. I’ll argue that the obstacle is a shared idealization, and that removing it reorders the questions.

The de-idealization in the title is specific. Early generative grammar idealized grammaticality to the knowledge of an ideal speaker–listener in a completely homogeneous speech community , treating variation, uncertainty, and change as noise around a categorical competence fact. That idealization bought tractability, but it priced out the phenomena in ([[ex:starting-stars]](#ex:starting-stars)). Following , removing it reorders the questions: ask first what the category grammatical lets us predict (its {==projectibility==}{>>consider adding a Goodman citation or a footnote with such citation. No need to limit it to Goodman if citing others makes sense.<<}{id="c1" by="user" at="2026-08-23T00:23:04.967Z"}, what observing some features licenses us to expect about others), and only then what worldly profile supports those predictions and what stabilizes it . Mechanisms matter because they explain why the projection holds, not because naming them settles the kind.

This paper develops that answer as the **Operator-Value Model of Grammaticality** (OVMG). Some grammatical contrasts tell interlocutors how to treat an utterance: as a question rather than an assertion, as committing one participant rather than another, or as linking one referent to another across clauses. I call these contrasts operator values and their contribution a public-update role. They form closed paradigms of instructions rather than a class defined by expressive substance, so tone, particles, word order, and inflection all count when they realize such a contrast . The framework rests on three premises, which track the order just named: profile, projection, and support.

1. **Profile.** A grammaticality claim is shorthand for a profile: a bundle of answers to several separable questions about a candidate in a situation. Is there any available analysis for it? Do its grammatically encoded contrasts agree with one another? Are the contrasts required in that situation supplied? Is the pattern a conventional resource for the relevant community, dialect, or register? And, separately, does it merely feel bad because it’s implausible or hard to process? Section [3](#sec:formalism) gives these questions their formal labels: coverage, compatibility, saturation, licensing, and subjective read-out. The examples in ([[ex:starting-stars]](#ex:starting-stars)) don’t instantiate one kind of “ungrammaticality”; they occupy different profiles.

2. **Projection.** The profile earns its standing by what it lets us predict, not by the mechanisms that hold it together: which rejections should soften under repeated exposure and which resist ([[ex:whose]](#ex:whose)) vs. ([[ex:lbe]](#ex:lbe)), how faithfully forms transmit, and how they change over time.

3. **Support, tested separately.** The dynamics module specifies candidate sufficient conditions under which usage could stabilize a population licensing state; conversational repair is a candidate _controller_, testable by its intervention signature (§[[sec:repair-controller]](#sec:repair-controller)); and the subjective read-out of ungrammaticality is separate from grammatical status: it comprises gradient anomaly and confidence signals.


Together, the premises explain why the traditions have talked past one another. The profile premise preserves the formal insight that constraints can be systematic while letting categorical and gradient cases share one architecture, in line with ’s () case for building gradience into core grammatical theory. The projection premise keeps the account testable: low-evidence constructions should respond to exposure and framing differently from high-opportunity preempted forms. The support premise explains why formal licensing, processing cost, and subjective read-out can move together without being the same thing.

{==Section [1](#sec:previous) traces the impasse in grammaticality theory to the attempt to treat it as one phenomenon. Section [2](#sec:framework) presents OVMG, defining the constitutive conditions and the recurrent instability modes that route a form to one diagnostic category or another. Section [3](#sec:formalism) gives the state theory: grammatical status is a population licensed-assembly state estimated through a posterior that retains concentration for projection. Section [4](#sec:dynamics) gives the dynamics module, specifying candidate routes by which such states could arise and stabilize. The module identifies conditional sufficient regimes rather than deriving categoricality from updating alone. Section [5](#sec:implications) situates the account against generative grammar, Construction Grammar, usage-based, logicality, and relevance-theoretic approaches, and states the predictions. The paper closes with limitations and a research program spanning corpus, experimental, and cross-linguistic methods.==}{>>rewrite to be clearer and more useful, less of a list that people will gloss over<<}{id="c2" by="user" at="2026-08-23T00:26:06.132Z"}
# The impasse in grammaticality theory
The concept of grammaticality remains elusive despite its centrality to linguistic theory. After decades of research, the field still lacks a unified account of what makes an utterance grammatical or ungrammatical. The impasse persists because grammaticality is often treated as a single phenomenon, when judgments actually reflect several questions at once: whether a covering assembly exists, whether its operator contributions are compatible, whether the situation’s obligatory dimensions are saturated, whether the relevant constructions are licensed, and how the resulting token feels to a speaker.
## The problem of structural viability
The first challenge in defining grammaticality is distinguishing structures that admit no viable analysis from those that fail for other reasons. , building on formal production systems developed by , treated grammaticality as a categorical property defined by membership in a set of well-formed strings. That categorical view captures the intuition that some strings, like ([[ex:nonsense]](#ex:nonsense)), resist structural analysis entirely:

*_Can the have running?_

Here, the input crashes the structural analysis independent of meaning. The “categorical” view correctly identifies that a viable structural analysis is necessary for grammaticality. But raising this single condition to the _definition_ of grammaticality leaves formal approaches struggling with evidence that speakers consistently provide gradient judgments for structures that are clearly analyzable but degraded. The competence-performance distinction attempted to preserve categorical grammar by attributing gradience to processing limitations. But as notes, this often leads to circularity, where problematic results are dismissed as performance artifacts. The OVMG framework resolves this by recognizing that while structural coverage–the existence of some assembly covering the relevant form–value pair–is a necessary, categorical prerequisite, it isn’t the sole determinant of grammaticality.
## The problem of operator compatibility
The second tension arises from the interaction of form and value. Chomsky’s famous example ([[ex:colorless-grammatica]](#ex:colorless-grammatica)) shows that operator-valued form–value relations can be intact even when lexical plausibility fails: the sentence is structurally a declarative, the subject is correctly identified both positionally and through agreement, and the tense suggests a general claim. What breaks is the plausibility of the construal, not grammatical status. Conversely, ([[ex:tense]](#ex:tense)) *_I’ve finished it yesterday_ shows that an intended meaning can be readily recovered even when an operator-valued form–value relation fails. Here, the clash is between the present perfect’s temporal contribution and the deictic anchoring contributed by _yesterday_.

Generative semanticists like and demonstrated early on that many constraints have semantic motivations. Construction Grammar has further shown how constructions carry meanings that interact with lexical semantics. Novel uses that align with established constructional meanings (like _She texted him the address_) are accepted, while those that clash with a construction’s licensed value (like *_She disappeared him the evidence_) are rejected. A complete theory needs a hard compatibility condition for conflicts among grammatically encoded operator contributions, while keeping lexical implausibility and processing cost in the subjective cost vector rather than turning every odd construal into a status failure.
## The problem of situational licensing
Finally, even structurally viable forms with readily recoverable interpretations may be ungrammatical if they violate community conventions. Sociolinguistic research demonstrates that grammaticality references community norms. Cross-linguistic variation shows that each language community conventionalizes particular form–value mappings through historical processes. These conventions become entrenched through statistical preemption : speakers learn that certain forms are ungrammatical precisely because they encounter alternative expressions in contexts where the ungrammatical form would otherwise be expected.

Consider ([[ex:age]](#ex:age)), repeated here:

**A:** _How old are you?_ **B:** *_I have 25 years._

This utterance is structurally viable and easy to interpret, but it’s categorically rejected in English. The same form is grammatical in French (_J’ai 25 ans_) and Spanish (_Tengo 25 años_); the constraint is community-specific. Usage-based approaches emphasize that such rejection arises from the absence of **situational licensing**. The English-speaking community has conventionalized a different way to express age, so the _have_+age frame is preempted by the be-frame in a dense niche rather than merely being unattested.

These problems don’t reduce to one scale. Structural coverage, operator compatibility, saturation, licensing, and subjective read-out have different diagnostics and different evidence streams. Acknowledging them as distinct but interacting routes makes it possible to move beyond the impasse of trying to force all grammaticality judgments into a single “competence” definition or a purely probabilistic usage model.
# The Operator-Value Model of Grammaticality
The term value is used here in the Saussurean sense of _valeur_ : the identity of a linguistic unit is constituted not by intrinsic properties but by its position in a system of contrasts, what it patterns with, what it opposes, and what interpretations it makes available. This isn’t feature-value assignment or decision-theoretic value. Throughout, I treat grammatical knowledge as a conditioned **form–value relation**; when this relation is sufficiently stable in a communicative situation, with a dominant value reliably recoverable and socially licensed, I refer to it informally as an established **form–value relationship**.

The model’s name marks its unit: operator values (closed-paradigm, update-configuring contrasts). A companion operator-stratum paper develops this boundary in full and argues that it follows public-update role rather than expressive substance: tone, particles, word order, inflection, and suprasegmental material all fall within its scope when they realize an operator contrast .

Here a self-contained working test suffices, because the concept has to stand on its own inside this paper: it fixes the scope of hard compatibility, the categoricality prediction, and the appendix on Turkish suffix harmony (§[8](#app:turkish-harmony)).

A contrast is an operator contrast when it meets three conditions jointly: drawn from a _closed_ paradigm, _high-opportunity_ (the communicative job recurs constantly), and _configured to the public update_ (clause type, polarity, tense and aspect anchoring, agreement and role allocation, scope, or reference tracking). Mis-setting such a contrast changes the update instruction even when the intended message is recoverable. {==The three conditions have formal counterparts in §§[3](#sec:formalism)–[4](#sec:dynamics): closure is finiteness of the dimension’s value set, opportunity is the niche count $`N_t(n,c)`$, and update-configuration is a positive expected common-ground divergence $`\Delta(d)>0`$ from mis-setting the contrast . $`\Delta(d)`$ needn’t be identified from repair itself: comprehension probes can ask whether mis-setting $`d`$ changes hearers’ answers about who did what to whom, when, with what force, or under which evidential commitment.==}{>>Do we need this? It seems overwhelming and impenetrable at this point in the paper at least? if we can't cut the whole thing, can we cut some of it and/or reduce some/all of it to a footnote?<<}{id="c3" by="user" at="2026-08-23T00:30:55.237Z"}

These conditions exclude cases that “closed-class”, “grammaticalized”, or “high-frequency” alone would admit. A closed-class item that doesn’t configure the update, such as a purely stance-marking discourse particle, fails the third condition and is predicted _not_ to attract categorical policing; a high-frequency open-class collocation fails the first; and a genuinely update-configuring contrast that’s gone low-opportunity, such as a moribund case distinction, fails the second and is predicted to destabilize. {==The prediction is falsifiable in the direction that matters: a closed, high-opportunity contrast that isn’t update-configuring should be policed like style, not like grammar.==}{>>I would replace it with something like:

  > These conditions define the operator stratum, not grammaticality as a whole. A closed, high-opportunity contrast that does not configure public update is not thereby an operator contrast, but it may still be categorically licensed or excluded as a
  > community-specific construction. The narrower prediction is that, once closure, opportunity, and competitor strength are matched, only update-configuring contrasts should produce the operator-specific comprehension and repair profile.

  That preserves a genuine falsifier without predicting that every non-operator must behave like style. It is exactly the kind of category error you suspected: operator membership was being mistaken for grammatical status.<<}{id="c4" by="user" at="2026-08-23T00:44:34.407Z"}

The formal architecture rests on four constitutive conditions: structural viability, operator-value compatibility, saturation of obligatory dimensions, and situational licensing. Together they specify a profile in the projectibility-first sense: a pattern whose partial observation licenses further expectations . Their interaction determines grammaticality (§[3](#sec:formalism)); what the profile projects, and what supports those projections, is the business of §[3](#sec:formalism) and §[4](#sec:dynamics). Figure [1](#fig:profile-spine) lays out this order of explanation, which the rest of the paper fills in. Table [1](#tab:vars) summarizes these conditions; the formal definitions appear in §[3](#sec:formalism).

The projectibility-first order of explanation. The constitutive conditions specify a licensed-assembly population profile whose posterior estimate, concentration, and heterogeneity license the projections on the right. Stabilization, maintenance, and control are separate world-side hypotheses (below), each requiring its own evidence.

| Condition | Component |
|:---|:---|
| $`\mathcal{A}(f,v)\neq\emptyset`$ | Structural coverage: some value-matched assembly exists |
| $`\operatorname{def}(A)`$ | Operator-value compatibility (unification) |
| $`\operatorname{sat}_t(A,c)`$ | Saturation of obligatory dimensions (derived, §<a href="#sec:derived-obligatoriness" data-reference-type="ref" data-reference="sec:derived-obligatoriness">4.5</a>) |
| $`L_t(A,c)`$ | Predictive assembly licensing from node-level $`\theta_t`$ |

The conditions used by the OVMG framework. Saturation is a path-dependent macro derived from preceding zero-marking rates and preemption pressure. Their conjunction, existentially quantified over covering assemblies and read through the learner’s posterior, gives grammatical status (§[3.3.1](#sec:posterior-existence)). {#tab:vars}

The formal core needs names for recurrent instability modes: ways of defeating coverage, unification, saturation, or licensing, with processing and prescriptive factors modulating how grammatical something _feels_ without directly fixing grammatical status.
## Diagnostic categories
The categories below are labels for common routes to ungrammaticality, not primitives of the model. Each traces to one or more constitutive conditions, as the formal core in §[3](#sec:formalism) makes explicit.

Form–value relations. Grammaticality depends on stable links between forms and the operator values they realize within communicative situations. T{++he idea t++}{id="s1" by="user" at="2026-08-23T00:46:29.524Z"}hat form–value relations exist at every level of grammatical organization, including morphemes and abstract syntactic patterns, is a core insight of Construction Grammar . OVMG narrows the target of {==categorical==}{>>is this word right/needed?<<}{id="c5" by="user" at="2026-08-23T00:46:52.788Z"} grammaticality to closed-paradigm, high-opportunity, update-critical contrasts: resources that configure how an utterance enters public coordination.

Operator exponents, like words, are typically polysemous: a single form participates in multiple form–value relationships, usually with one dominant value . The English past tense, for instance, usually denotes past time, but it can also mark social distance (_Could you help me?_) or low likelihood (_If I went tomorrow…_). What matters for grammaticality is whether a stable relationship exists within the relevant communicative situation, not whether the form has a single fixed meaning.

Neuroimaging work provides converging evidence that form and meaning aren’t processed by wholly sealed modules. Fedorenko and colleagues distinguish language-selective regions from neighbouring domain-general systems while showing that syntactic and semantic manipulations both recruit the language-processing architecture . The processing claim here is modest: the subjective read-out can reflect interacting processing demands even when grammatical status remains intact.

Following , grammaticality is conditioned by regularities within a “communicative situation”. The emergence claim defended below is narrower: categoricality arises through the licensing dynamics in §[4.4](#sec:emergent-categoricality), not through an unanalyzed appeal to usage.

Communicative situations aren’t static or mutually exclusive. A speaker orients to overlapping contexts that shift on multiple dimensions: the immediate situation (formal meeting vs. casual chat), durable social positions (regional, generational), and the norms they’re orienting to (which can shift with audience). This fluidity explains style-shifting, dialect formation, and the gradual acceptance of initially marginal constructions.

Early child language shows this. Toddlers produce utterances that deviate from adult norms but remain internally consistent within the child’s developing system. A toddler in a monolingual English household might say:

_Ava cookie._ (intended as ‘Ava = I want a cookie’) Although this differs from adult English norms, it may not be perceived as ungrammatical by the child’s regular caregivers. Used with the same pragmasemantic force among anglophone adults, the construction would be judged ungrammatical.

Multiple modal constructions provide another clear example of variety-relative grammaticality:

_I might could help you with that._ This combination of modal auxiliaries is systematically possible for some American English speakers, who can productively generate similar constructions . Speakers from communities where only single modals are grammatical, though, typically reject such combinations as ungrammatical.

A similar pattern appears in code-mixing among bilingual speakers, where combinations of forms from different languages can be grammatical within that bilingual community’s norms but not without. Consider a Spanish-English bilingual speaker who uses a Spanish progressive auxiliary with an English lexical verb:

Within the right communicative situation, this utterance is grammatical. The Spanish auxiliary _estábamos_ combines with an English participial form _lifting_ to form the progressive aspect. This cross-linguistic combination of morphology and a lexical verb is consistent with local norms, where code-mixed utterances are common and meaningful. In contrast, in a standard monolingual Spanish setting, where fully Spanish progressive structures are licensed (_estábamos levantando pesas_), speakers may judge the example in ([[ex:estábamos-lifting]](#ex:estábamos-lifting)) as ungrammatical. The use of intransitive _lifting_, specific to the gym community, further illustrates just how localized grammaticality judgments can be.

This doesn’t mean bilingual communities simply accept any combination of languages. As reports, Spanish–English bilingual speakers judge examples like ([[ex:enanitos-failed]](#ex:enanitos-failed)) as unacceptable, showing that even in bilingual communities, there are systematic constraints on which language combinations are permitted.

In a slightly different case, as a second-language speaker of Japanese, I used to say Conventionally, though, plain _i_-adjective predicates in Japanese don’t take the plain copula _da_ in this frame. The issue is exponent selection: the predicate’s value is recoverable, but the community doesn’t license that copular exponent there. The example shows why acquisition history matters: shared routines stabilize form–value relations for a community, while individual trajectories can still pull judgments away from that norm.

The specific linguistic context can matter too:

> To take an obvious case which Jerry Morgan [()] discussed recently, certain combinations of words are extremely strange if presented in isolation but are perfectly normal as answers to certain questions. _Spiro conjectures Ex-Lax_ would generally be felt to be unintelligible if presented out of context but is a perfectly normal answer to the question _Does anyone know what Mrs. Nixon frosts her cakes with?_ [^1]

These examples show why grammaticality has to be indexed to communicative situation. Conversants who differ in immediate situation, social position, or the norms they orient to may disagree on whether a form is grammatical, and both may be right within their respective contexts. The linguist’s task is to determine whether a form is grammatical from some position in that space, or systematically excluded from all of it.

The stability of form–value relations within speech communities can be empirically modeled, as demonstrated by . Their utterance selection model treats speech communities as networks where speakers track and reproduce linguistic variants based on their interactions. When applied to dialect formation, these models show how competing linguistic variants spread and eventually stabilize, with initial variant frequency strongly predicting which form will prevail.

In different languages, different distinctions become conventionalized as grammatically obligatory. These obligatory contrasts reflect historically stabilized patterns in which meaning distinctions are systematically marked. Over time, usage establishes grammatical constructions that reliably signal these distinctions. As a result, what counts as a grammatical necessity in one language may be optional or absent in another.

The progressive aspect provides a useful example. In Standard English, it isn’t optional but an obligatory grammatical marker for ongoing, incomplete actions: _She is studying right now._ Here, the progressive form _is studying_ isn’t just a stylistic choice. It’s the recognized, grammatical way to convey the appropriate aspectual meaning in this frame.

In French, by contrast, the progressive aspect isn’t a grammatically mandatory distinction. Speakers can signal ongoing activity through adverbs or periphrastic constructions, but standard French doesn’t have a dedicated progressive form. The sentence: _Elle étudie maintenant._
‘she studies/is studying now’ can comfortably describe a currently ongoing action without any need for special morphology. In Standard French, this aspectual distinction isn’t conventionalized as an obligatory operator contrast. English grammar treats the contrast as obligatory; French doesn’t. On this account that difference isn’t a primitive of either grammar: §[4.5](#sec:derived-obligatoriness) models obligatoriness as the limit of preemption applied to zero-marking, so the English–French contrast is a prediction of the dynamics, not a stipulation they inherit.

The same holds for evidentiality, the grammatical marking of information sources. In Turkish, evidentiality is systematically realized through verb forms and particles that distinguish between directly witnessed events and those inferred or reported: _Gelmiş_
‘He/she came (apparently)’
(i.e.  the speaker wasn’t a witness but inferred or heard about it.) In Turkish, evidential distinctions are conventionalized as obligatory operator contrasts. A speaker can’t simply omit evidential marking without sounding ungrammatical.

English speakers can say _I heard that he arrived_ or _He must have arrived_, but these are optional lexical or modal resources rather than required elements of the grammar. In English, evidential distinctions aren’t conventionalized as obligatory operator contrasts. The same mechanism covers the Turkish case on a different dimension (§[4.5](#sec:derived-obligatoriness)).

demonstrate this principle systematically in their analysis of verbal morphology across French and other Romance languages. They show how apparently similar verbal systems can grammaticalize quite different semantic distinctions as obligatory. The contrast reflects different conventions about which meaning distinctions are systematically marked. For instance, while both French and Italian mark aspect morphologically, they differ in which aspectual distinctions are grammaticalized versus left to optional lexical expression.

Establishing a form–value mapping is necessary for grammaticality, but it isn’t sufficient. Speakers routinely interpret strings that still count as ill-formed in the relevant communicative situation. That flexibility makes licensing, not interpretability in principle, the central question.

The conditions do different work. Coverage asks whether any assembly can be built; compatibility asks whether its operator contributions unify; saturation asks whether the obligatory dimensions for the situation are set; licensing asks whether the population treats the relevant constructions as repertoire. Processing costs, recovery costs, and lexical implausibility can still make a licensed assembly feel bad, but they enter selection and the subjective cost vector rather than replacing status. The interaction predicts why *_Furiously sleep ideas green colorless_ elicits universal rejection while ([[ex:center]](#ex:center)) feels bad in everyday quotation but is accepted as “grammatical but hard to process” once speakers are walked through the intended structure.

Nor does convergent usage by itself settle the matter. Defining grammaticality as “whatever speakers accept” would be circular: it couldn’t flag contested innovations, explain stable dialectal differences despite mutual intelligibility, or distinguish licensed forms from performance errors that pass unnoticed. Separating coverage, compatibility, saturation, licensing, and subjective read-out avoids trivializing grammaticality while still treating durable population-level licensing as decisive for which relationships endure.

Operator-value compatibility. Beyond the existence of form–value relations, grammaticality requires compatibility among the operator values those relations realize. This condition captures cases where individual elements are well formed but their combination creates conflicts among grammaticalized contrasts activated in the communicative situation.

Consider the temporal incompatibility in: Here, the present perfect construction contributes a reference interval anchored to present relevance, while _yesterday_ contributes a deictically past interval. Unlike lexically incongruous combinations like _colorless green ideas_, which remain grammatical because the clash doesn’t mis-set an operator value, this example shows failed unification between grammatically encoded temporal contributions.

The age example belongs elsewhere: In English, _have_+_years_ is a licensed frame for duration, remaining time, or experience, but ordinary age predication is licensed through a different frame. The intended value is readily recoverable, so the failure isn’t an operator-compatibility failure. It’s a licensing failure for an age-predication construction in English, even though cognate-looking frames are licensed in French and Spanish.

Sometimes compatibility failures involve conflicting information-packaging requirements: The clash is in grammatically encoded information packaging: the same participant is simultaneously focused through fronting _who_ while being backgrounded by the relative clause construction .

These examples also delimit compatibility. The formal core treats operator-value conflict as failed unification among partial operator assignments: tense–aspect anchoring where tense–aspect is obligatory, argument-linking requirements where a construction licenses roles, information-packaging instructions where a construction grammatically encodes focus or backgrounding, and indexical contrasts only when they’ve entered a closed accountable repertoire. This makes compatibility partly derivative of licensing facts at the feature level, keeping arbitrary lexical implausibility out of grammatical incompatibility.

Processing constraints. Language processing engages both dedicated language networks and domain-general cognitive systems . When constructions overload these systems, particularly through multiple long-distance dependencies or heavy embedding, they may trigger feelings of ungrammaticality despite being structurally well-formed.

_The bread the baker the apprentice helped made is delicious._

Evidence for these constraints comes from multiple sources. Studies of sentence processing show that dependencies spanning multiple intervening elements increase processing difficulty, with new referents between dependent elements compounding memory load . In ([[ex:center-process]](#ex:center-process)), while each individual relation (like _the apprentice helped_ and _the baker made_) is interpretable in isolation, their nested combination overwhelms incremental processing. The construction is grammatical, but excessive bridging costs from its nested structure trigger feelings of ungrammaticality.

Rather than reflecting simple memory limitations, processing constraints emerge from the interaction between specialized language networks and other cognitive systems . On this processing-level interpretation, what speakers experience as difficulty may reflect demands distributed across specialized brain systems rather than a single cognitive bottleneck.

Dependency locality is the best-documented such cost. Integration difficulty rises with dependency length and peaks at loci of long-distance integration, with locality accounting for substantial region-level variance in reading times in . Because the effect is robust across processing work, the formal treatment in §[3](#sec:formalism) gives dependency locality a dedicated component rather than hiding it inside a residual term. High-locality constructions feel worse even when structurally well-formed, and because they’re harder to produce and parse, speakers tend to avoid them.

That avoidance is a pathway from processing to change, developed formally in §[2.5](#sec:change-mechanisms) and §[4](#sec:dynamics): lower-processing forms are easier to store and reuse, so simpler patterns can spread and conventionalize. The processing evidence supports this as a plausibility claim about one route into stability, not a direct neural explanation of grammatical change.

Processing constraints also interact with the licensing state without becoming part of status. A construction that is marginal because its licensing posterior is diffuse may be judged more harshly when it is also hard to process. Conversely, a highly licensed construction can remain grammatical despite considerable processing demands, even while those demands keep its anomaly signal high.

Socio-pragmatic indexicality. The value of a construction extends beyond semantic content to include socio-pragmatic dimensions: how linguistic forms index aspects of social context, speaker identity, group membership, stance, or interpersonal relationships .

In many varieties of Latin American Spanish, for example (e.g.  the Río de la Plata region), speakers use _vos_ and its associated verb forms instead of the _tú_ forms used elsewhere in the Spanish-speaking world :

Here, the use of _vos_ rather than _tú_ denotes the second-person singular hearer (the person being offered a coffee) and indexes the speaker’s regional identity and familiarity with the local dialect. This indexical value may convey closeness, solidarity, or membership in a particular geographic and social community.

This situational view of grammaticality can manifest asymmetrically. Speakers from the Río de la Plata region may view a conversational situation as accommodating both their own norms and those of _tú_-using interlocutors; the situation itself can encompass both _vos_ and _tú_ as grammatical options. But speakers from _tú_-only regions might conceptualize the same situation more restrictively, defining it in a way that categorically excludes _vos_ as a grammatical possibility. This asymmetry doesn’t depend on different understandings of the forms themselves, but can arise from different ways of defining what the communicative situation allows, influenced by the indexical values attached to _vos_ versus _tú_ in their respective communities.

Phonology can carry constructional indexical value, but it bears on grammaticality only when it realizes an operator contrast or enters an operator-exponent licensing condition. provides an example. In a study conducted in Bolivia, participants were presented with audio stimuli where only the vowels were manipulated to reflect either a highland or lowland accent. This presented participants with incongruent identity cues (e.g.  vowels from one accent along with consonants from the other). But this didn’t trigger feelings of ungrammaticality. Instead, vowel contrasts activated expectations about consonant features and discourse markers, and some participants “hallucinated” identity-linked features that weren’t present in the signal.

So a construction’s value reaches beyond semantic features to socio-pragmatic aspects that shape how speakers and hearers negotiate authority, identity, solidarity, and other interpersonal relations. Recognizing these indexical dimensions helps explain why certain forms feel natural and grammatical to some speakers and out of place or even ungrammatical to others.

Situational licensing. Even well-formed constructions with clear meanings may be judged ungrammatical if they lack conventionalized licensing. This condition concerns whether a form–value relation is licensed within the relevant communicative situations.

The regular plural marking has a compositionally recoverable meaning and is structurally parallel to other English plurals, but the irregular form _sheep_ is entrenched across English-speaking communicative situations, making the regularized version unacceptable. Without a metaphorical or playful justification (as in _the black sheeps of the family_, where the irregular plural might signal a figurative usage), the utterance is ungrammatical.

Situational licensing operates independently from the other conditions. A construction may have complete operator compatibility and minimal processing demands but still be excluded because a different form has been conventionalized for that meaning. Extreme rarity makes the distinction clear. Some constructions are so infrequent that speakers lack a shared consensus about their status.

The independent relative genitive pronoun _whose_ provides an example, being so unusual that deem it non-existent. The contexts that license this construction require the simultaneous convergence of distinct pragmatic and syntactic conditions (sufficient accessibility of both possessor and possessum, the appropriate information structure, and an environment allowing ellipsis), which are seldom met all at once :

In the COCA check reported here, no token of the construction appears . That absence supplies little negative evidence, because the opportunity set is tiny: contexts requiring an independent relative genitive are vanishingly rare. Speakers have little evidence either way: neither positive tokens nor the systematic absence that would accumulate if the construction were regularly passed over. The evidence supports high _uncertainty_ rather than confident rejection. Some speakers can draw an analogy with similar constructions and accept examples like ([[ex:whose-entrench]](#ex:whose-entrench)); others remain unsure; still others, lacking sufficient exposure, can’t construct a stable form–value relation at all. Even among those who grasp the construction analytically, ’s account predicts that its unexpectedness would trigger high surprisal, compounding the uncertainty with processing difficulty.

This contrasts with putative preempted cases like left-branch extraction, discussed next, where the opportunity set appears large and the construction is systematically untaken. The classification depends on a further quantity, though: how often speakers would choose the discontinuous form if it were stipulated to be licensed.

Apparent categorical exclusions. Some constructions face rejection so persistent that it _appears_ categorical. Left-branch extraction is the textbook case:

The intended meaning is easily grasped; nothing in the semantics or pragmatics prevents understanding the speaker’s intent. Nor does the construction seem excessively complex to process. Yet English speakers categorically reject it, and treats this kind of pattern as a core case of “ungrammaticality”.

Under OVMG, such patterns are candidate **preempted gaps**: situational licensing is driven toward zero by persistent preemption when the communicative job is common, an established competitor wins, and the counterfactual choice probability of the missing form is high. For English left-branch extraction, the natural competitor is _Which car did you buy?_. The corpus absence is suggestive but not decisive; the missing ingredient is independent norming of $`\widetilde{\rho}_t^\star(\textsc{lbe}\mid n,c)`$ under permissive framing. Additional processing penalties, such as systematic garden-path reanalysis when the bare interrogative phrase is encountered, can strengthen the subjective categoricality without any independent structural constraint. The formal dynamics appear in §[4](#sec:dynamics).

Cross-linguistic comparison doesn’t threaten this analysis, because the dynamics are defined over a language’s own niches. Left branch is a descriptive class tied to a particular phrase-structure analysis, not a comparative concept ; whether discontinuous nominals in case-rich, article-less languages instantiate the same configuration as the English case is far from clear, and the companion corpus study deliberately brackets the comparison . The model instead predicts which opportunity structures should support similar patterns. Discontinuous nominal orders should be learnable where inflectional marking makes the dependency recoverable, a productive discontinuous-order pattern supplies scaffolding, and a discourse niche makes the separated element useful. English meets none of the three, so the candidate has no scaffolding of its own and the contiguity-preserving competitors win every opportunity.

Several diagnostic criteria help identify these preempted-gap constructions:

1. **Persistent non-licensing:** The construction doesn’t improve under ordinary exposure or framing while the high-concentration non-licensing state remains in place.

2. **Categorical rejection:** Speakers find the constructions simply impossible, with high confidence rather than mere uncertainty.

3. **Resistance to satiation:** Unlike processing-heavy cases, repeated exposure doesn’t improve acceptability.


**Prediction:** If lbe is really a high-concentration preempted gap, framing tokens as intentional dialectal or ingroup resources should do little to move judgments; the same manipulation should matter more for low-concentration cases such as independent relative _whose_ or defective cells. A robust framing effect for lbe, or a low independently normed $`\widetilde{\rho}_t^\star`$, would count against the preempted-gap diagnosis.

If no covering assembly is available at all, the diagnosis isn’t a further residual constraint but structural coverage failure: the existential over assemblies is empty. Treating classic cases like lbe as driven to zero under preemption keeps the constitutive core minimal and pushes the explanatory work into the dynamics of situational licensing, while reserving true coverage failure for cases with no well-typed route through the constructional inventory.

Winnerless cells: paradigm defectiveness. Preempted gaps have a winning competitor. Defective paradigm cells don’t. They leave a high-opportunity cell empty without any single form winning it. A clearer case is the Russian first-person singular non-past of _pobedit’_ ‘win’: speakers avoid the expected cell and resort to periphrasis instead. The English _amn’t_ gap is diagnostically useful but less clear, because broader niches include _I’m not_ as a competitor, while narrower contracted-negator niches make the cell look winnerless .

In the Russian case, the niche is common and candidate forms are readily identifiable, but no candidate accumulates enough positive evidence to settle as the form. The source can be structural uncertainty, lexical restriction, learning dynamics, or avoidance, with the mixture varying across cases . In this account, defectiveness is a third licensing profile: high opportunity with evidence divided among candidate forms, leaving each candidate’s posterior low in mean but unstable, rather than concentrated near zero.

The phenomenology matches: speakers report not knowing how to say it (ineffability), not the confident “that’s wrong” of a preempted gap. §[4.6](#sec:winnerless-cells) represents this profile with an avoidance attractor plus low candidate support: avoidance absorbs the cell’s opportunities, and because avoidance is nearly uninformative about any particular candidate, no candidate accumulates confident negative evidence either. The satiation-framing prediction follows: defective cells should behave like low-evidence forms, movable under framing, not like preempted gaps.
## Diagnosing (un)grammaticality at a glance
For exposition the recurrent instability modes can be read as a short decision tree (the formal definitions appear in §[3](#sec:formalism)):

| Condition | Canonical outcome |
| :--- | :--- |
| no covering assembly | nonsense (*_Can the have running_) |
| operator-value clash (unification failure) | compatibility failure (*_I’ve finished it yesterday_) |
| obligatory dimension unset | saturation failure (unmarked progressive in English) |
| rarely encountered, low certainty | community-novel (_friend of whose_) |
| systematically preempted, high confidence | preempted gap (left-branch extraction if normed) |
| high opportunity, candidates split | defective cell (_pobedit’_ 1sg) |
| high processing cost, structure recoverable | transiently ill-felt (centre embedding) |
| otherwise | grammatical |

Lexical-semantic oddity without an operator clash (_colorless green ideas_) routes to “grammatical”; its strangeness is a construal-plausibility cost in the subjective read-out (§[3.7](#sec:feeling-new)), not a status fact.
## Patterns of (un)grammaticality
These categories aren’t points on one severity scale. They name different routes through the same architecture. A token can fail because no assembly covers it, because its operator contributions don’t unify, because an obligatory dimension is unsaturated, or because the pivotal construction isn’t licensed in the population. Separately, a licensed token can feel bad because processing, plausibility, or prescriptive dissonance pushes the anomaly channel away from zero; confidence tracks how settled the relevant status condition is.

This matters for apparent gradience. Intermediate acceptability ratings can come from a diffuse licensing posterior, from a strong anomaly signal attached to an otherwise licensed form, or from disagreement about the conditioning state. They aren’t automatically evidence for soft compatibility. Recoverability of the intended interpretation can affect attribution or repair, but it can’t make an operator clash grammatical. Conversely, high processing cost can make a licensed construction feel bad without lowering its licensing posterior. The formal core in §[3](#sec:formalism) separates these routes; the worked examples in §[3.9](#sec:worked-examples) show how they project differently.
## The subjective experience of grammaticality
The constitutive conditions determine conventional grammatical status (§[3.3](#sec:objective-G)); speakers register putative violations through read-outs and judgments that can diverge from it.[^2]

The subjective read-out. The familiar “feeling of ungrammaticality” is the anomaly side of a broader metacognitive read-out. It parallels other well-studied metacognitive feelings like the feeling of knowing , which arises when one feels certain of knowing something but can’t retrieve it.

There isn’t a positive feeling of grammaticality, just as there isn’t a feeling of having enough oxygen, only the negative feeling registered in its absence. The anomaly channel, then, is the negative response triggered when an utterance violates expected form–value patterns. The confidence channel tracks how settled the speaker takes the relevant status condition to be.

This notion echoes Edward Sapir’s “form-feeling”, an often unconscious grasp of language patterns . Evidence from aphasia supports the same separation. Patients with Broca’s aphasia, who produce agrammatic speech, often exhibit self-monitoring behavior, attempting self-correction and expressing frustration with their grammatical errors .

Unstable or missing form–value relations, detected during processing, can trigger this response. The response is a speaker-level heuristic for detection, not the definition of grammaticality. That separation explains why marginal constructions elicit gradient certainty, why repeated exposure can attenuate negative responses without necessarily changing status, and why conventionally licensed constructions can still feel wrong under processing pressure. In that sense, (un)grammaticality can be illusory .

Distinguishing grammatical status from subjective ratings. Grammaticality research has to distinguish grammatical status, the conventional, population-level property made precise in §[3.3](#sec:objective-G), from the subjective read-outs that speakers provide. Those read-outs have two channels in the formal model: anomaly and confidence. (I use “objective” below only in that sense, population-level and convention-constituted, not judge-independent.)

Table [2](#tab:two-levels) summarizes the two levels of analysis.

| Level | Nature | Observable through |
| :--- | :--- | :--- |
| Grammatical status | Population licensed-assembly | Converging evidence: |
|     | state, posterior-estimated in $`c`$ | corpora, production, |
|     |     | repair behaviour |
| Subjective read-out | Anomaly signal $`F`$ and | Ratings, online measures, |
|     | confidence $`\Phi`$ | self-reports, test–retest, |
|     |     | explicit confidence |

Grammatical status versus subjective read-out {#tab:two-levels}

The measurement problem is familiar from other sciences: temperature can’t be directly observed but has to be inferred through the behaviour of thermometers. Grammaticality likewise has to be inferred from several measures, with acceptability ratings as one imperfect window. The same caution applies to language-model probabilities: raw string probability by itself doesn’t separate grammatical from ungrammatical strings, and minimal-pair probability contrasts are informative only when the intended message is controlled .[^3]

The formal counterpart of this status/read-out picture, including what it implies for interpreting the factor analyses that are common in experimental syntax, appears in the formal core (§[3.7](#sec:feeling-new), §[3.8](#sec:measurement-C)): because such analyses target the structure of the subjective read-out, not grammatical status directly, a factor counts as evidence about the grammar only when it also shows up in the independent indicators for licensing, compatibility, and confidence.

This also explains why satiation and gradient judgments don’t automatically threaten categorical status. A construction can remain unlicensed in the community’s system while triggering progressively weaker negative responses through familiarization. Conversely, subjective response can remain continuous even when the population licensing state is effectively categorical (§[4.4](#sec:emergent-categoricality)). Treating ratings as evidence rather than definition keeps grammatical hypotheses empirically vulnerable without collapsing the linguistic system of a communicative situation into individual responses to it.

Misattribution effects. Sometimes the subjective read-out of ungrammaticality doesn’t accurately reflect conventional grammatical status. Both false positives (grammatical constructions feeling ungrammatical) and false negatives (ungrammatical constructions escaping detection) occur systematically.

When grammatical constructions feel ungrammatical. Listeners and readers can misanalyze utterances, triggering feelings of ungrammaticality even though the construction conforms to standard patterns: _The old man the boats._ On first reading, one might treat _old man_ as a noun phrase and arrive at nonsense. But the sentence actually has _the old_ as the subject (meaning ‘the elderly’), and _man_ as a verb. Interpreted correctly, the sentence means ‘The elderly operate the boats’, and is fully grammatical.

Processing overload provides another source of misattribution. Heavily nested structures like ([[ex:center-process]](#ex:center-process)) are grammatically well-formed but trigger negative responses due to cognitive limitations rather than grammatical violations.

When ungrammatical constructions escape detection. Conversely, conventionally ungrammatical utterances may fail to trigger negative responses when the intended meaning is strong:

The intended interpretation is clear, and hearers readily infer the meaningful comparison. Under the relevant syntactic analysis, the comparison composes differently. The first clause suggests comparing numbers of people, but the second clause has _they_ (‘more people’), making the meaning ‘more people did x than more people did y’, which is nonsensical. But this violation often escapes detection.

Agreement errors can similarly hide within complex noun phrases: The singular subject _patchwork_ clashes with plural _help_, but the intervening plural nouns mask this violation. Cognitive resources devoted to processing complexity can prevent speakers from registering the agreement error.
## Mechanisms of grammatical change
The stability of form–value relations isn’t static. Various motivations alter the choice likelihood or the adoption transition for new and established forms, explaining how grammatical systems evolve over time. These aren’t a loose catalogue of causes: each names a route by which the update or transition in §[4.3](#sec:update) can change, so each predicts a direction of change (which forms should gain licensing and which should lose it) and feeds the actuation dynamics of §[4.8](#sec:actuation).

Semantic motivations for reanalysis. Speakers regularly deploy metaphors, analogies, and context-induced reinterpretations that stretch or shift the meaning of existing forms. Over time, such re-analyses can yield new grammatical constructions that weren’t previously part of the language’s repertoire.

A well-documented example is the development of the _going to_ futurate construction. Historically, _going to_ described physical motion toward a place:

_I am going to London._

Frequent usage in contexts where motion implied subsequent action (e.g.  _I am going to fetch some firewood_) led to semantic shift. The directional component was reinterpreted as marking future intention rather than spatial goals:

_It’s going to rain._

What once expressed physical trajectory now serves as a predictive futurate marker. The form–value relation changed through semantic reanalysis, driven by communicative utility.

Social motivations for licensing and excluding forms. Linguistic variants often serve as markers of regional background, class, ethnic identity, or age group. These social cues motivate speakers to favor some forms over others; over time, those preferences shift what counts as grammatical.

The decline of the simple past (_le passé simple_) in modern spoken French illustrates social motivation. Forms like _il alla_ (‘he went’) became associated with formal, literary, or provincial speech. To avoid signaling undesirable social affiliations, speakers gravitated toward compound forms like _il est allé_, which lacked these status-laden connotations.

Situational licensing tracks changing social dynamics: forms that were once fully grammatical can become socially marked and gradually excluded from normative grammar.

Structural motivations. Structural considerations arise from cognitive and communicative demands, including processing limitations, the need for clarity, and the influence of analogy.

Processing constraints and memorability. Transmission tends to favor patterns that minimize processing demands. Forms requiring multiple long-distance dependencies or heavy embedding are less likely to achieve stable transmission across generations. This pressure toward processability shapes grammatical evolution, with simpler patterns spreading through communities.

Analogical extension. When speakers encounter new communicative challenges, they often extend known patterns to new contexts: Such forms are licensed in some English varieties and marginal or rejected in others. Where they spread, the analogical source is readily identifiable: main-clause interrogatives such as _What did she do?_. If licensed in a new community, this analogical extension would represent structural motivation reshaping the grammar.

Iconic motivations. Forms are sometimes licensed precisely because their structure reflects their meaning. Reduplication for intensity provides a simple example:

The formal repetition iconically mirrors the magnitude being expressed. Such patterns are readily interpretable and likely to spread because the form–value link is immediately apparent.

Iconicity remains syntactically and variety constrained, though. In the target standard-English frame here, adjectival reduplication is natural in pre-head modifiers but rejected as a predicative complement:

These motivations (semantic, social, structural, and iconic) can interact and sometimes conflict. While Optimality Theory has productively modeled such competing pressures through ranked constraints , OVMG views their resolution as arising from usage within communicative situations rather than solely from fixed rankings. The specific weighting of motivations reflects historically established patterns and communicative needs.
# A formal core: grammaticality as conditioned stability
The framework separates two explanatory targets. A state theory specifies the conditions under which a form–value pair is grammatical _for a population in a communicative situation_ at time $`t`$; a dynamics module specifies candidate routes by which such states arise, persist, and change.

{==In projectibility terms==}{>>we haven't really set out what such terms might be.<<}{id="c6" by="user" at="2026-08-23T00:56:07.129Z"}, the state theory specifies the profile, while the dynamics module states candidate support hypotheses: what could stabilize the profile and, where the evidence warrants, maintain it. Support claims come in grades. Stabilization, maintenance by a production–repair loop, and control by a deviation-detecting process are distinct claims, each requiring independent evidence . In Woodward’s interventionist terms, a stabilizer earns that status when an intervention on it changes the profile in an invariant, predictable way .
## Conditioning structure
Let $`c\in\mathcal{C}`$ be a conditioning state, a construed communicative situation in ’s () sense, together with whatever norm-centre is treated as relevant. Nothing here requires $`c`$ to be externally given; interlocutors can misalign about $`c`$, and $`c`$ can be learned, split, and renegotiated over time.

For many purposes it helps to think of $`c`$ as a bundle that may include situational features (activity type, medium, footing), stable baselines tied to speaker ascription, and norm-orientation (discourse-community identification), but the formalism treats $`c`$ abstractly as the conditioning variable that selects the relevant distribution of form–value relations.
## Objects
Before introducing the notation, here is the ordinary-language picture. An assembly is a candidate way of building a form–value pair out of learned patterns. The model asks four questions about it: is there a way to build it at all? Do the grammatical instructions contributed by its parts fit together? Are the instructions that this situation requires actually supplied? And does the relevant community treat the patterns involved as available resources? A negative answer can arise at any of these points. Difficulty of processing, implausibility of the construal, and prescriptive dissonance are different: they can make an otherwise licensed assembly feel bad without changing its status.

The table maps that sequence onto the formal core. The prose that follows first describes constructions and assemblies, then distinguishes the community state from the evidence-based estimate of it. Readers need not retain the symbols on first pass: grammatical status tracks whether a population has an assembly that passes all four questions in a situation, while the evidence also records how settled that estimate is.

| Expository role | Formal object (§3) | Work in the formal core |
| :--- | :--- | :--- |
| coverage / structural viability | $`\mathbf{1}\bigl[\mathcal{A}(f,v)\neq\emptyset\bigr]`$ | structural viability: some covering assembly exists |
| operator compatibility | $`\operatorname{def}(A)`$: unification | hard operator-value compatibility |
| saturation | $`\operatorname{sat}_t(A,c)`$ | derived saturation of obligatory dimensions |
| content oddness | plausibility term in $`R_i`$ (§[3.7](#sec:feeling-new)) | content-oddness as a subjective cost |
| situational licensing | population rate $`\theta_t`$; Beta posterior; $`L_t(A,c)`$ | population licensing and its evidence state |
| status profile | $`S_t^{\theta}`$ population state; $`\widehat{S}^{(r)}_t=\mathbb{E}_r[S_t^{\theta}]`$ | status and its epistemic estimate; simple products are limiting cases (§[3.3.1](#sec:posterior-existence)) |
| decision threshold | $`\tau(c)`$, §[3.3.4](#sec:decision-readout) | decision-theoretic read-out only |

Where the expository roles from the opening sections live in the formal core. The formal implementation uses assemblies, unification, licensing posteriors, and decision read-outs. {#tab:notation-bridge}

{==Notation==}{>>throughout the section, many variable (and constants?) are introduced without being defined, or at least, I couldn't follow<<}{id="c9" by="user" at="2026-08-23T01:08:43.386Z"} is typed as follows. In §3, $`f`$ is a form, $`v`$ is a value, and $`u`$ is used only when the value is recoverable from context. In §4, a niche candidate is written $`x\in\mathcal{V}_{n,t}^{\star}`$ and abbreviates a candidate form–value realization. Constructional nodes are $`\kappa`$, assemblies are $`A`$, speaker-level inclusion states are $`z_{j,t}`$, and population licensing rates are $`\theta_t`$.

The core’s unit is the construction, in the CxG sense of a learned form–value pairing at any grain . Formally, {==a construction $`\kappa`$ is a pair $==}{>>should we stick with this or adopt the richer SBCG perspective?<<}{id="c7" by="user" at="2026-08-23T01:02:06.442Z"}`(T_\kappa, \mu_\kappa)`$: a form template with typed slots, and a value contribution mapping slot fillers to content together with a partial operator assignment $`\omega_\kappa`$. Nothing here is level-specific: a construction can be the plural cell of a lexeme, a clause pattern, an intonational contour, or a code-mixed frame.

Operator contributions live in a typed constraint space $`\Omega`$ over a dimension set $`O(c)`$. The dimensions {==include==}{>>we should be clear about whether this is supposed to be exhaustive or not<<}{id="c8" by="user" at="2026-08-23T01:03:14.315Z"} clause type, polarity, tense–aspect anchoring, role allocation, scope, reference tracking, and information-packaging instructions. Which dimensions belong to $`O(c)`$ is itself conventional: a contrast enters only when the community has conventionalized it as an operator contrast in the sense of §[[sec:operator-values]](#sec:operator-values), so the inventory is community-indexed. Atomic feature–value assignments are a useful special case, but the general object is a constraint structure: tense intervals, scope relations, anaphoric dependencies, and information-packaging requirements can refine one another without being identical atomic values. Two contributions unify, written $`\omega \sqcup \omega'`$, iff their conjunction is satisfiable in the typed constraint system; otherwise the join is undefined ($`\bot`$). Compatibility remains Boolean, but equality of atomic values isn’t the only way to satisfy it.

An assembly $`A`$ is a finite tree of constructions with all slots filled. Its yield is $`\mathrm{form}(A)`$; its operator assignment is $`\omega(A)=\bigsqcup_{\kappa\in A}\omega_\kappa`$, defined iff all contributions unify; its value is $`\mathrm{val}(A)`$. Three predicates over assemblies do the core work:

```math
\begin{align}
\operatorname{def}(A) &= \mathbf{1}\bigl[\omega(A)\ \text{is defined}\bigr]
  && \text{(compatibility)} \\
\operatorname{sat}_t(A,c) &= \mathbf{1}\bigl[\omega(A)\ \text{is total on}\
  \mathrm{OBL}_t(n(A,c),c,A)\bigr]
  && \text{(saturation)} \\
L_t(A,c) &= \textstyle\bigwedge_{\kappa\in A} Z_t(\kappa,c)
  && \text{(licensing)}
\end{align}
```

Compatibility is hard: there’s no weighting an operator clash away. Saturation refers to the obligatory dimensions $`\mathrm{OBL}_t(n(A,c),c,A)`$, which aren’t stipulated per language. Section [4.5](#sec:derived-obligatoriness) derives them from a preceding window of population-level, niche-specific zero-marking rates and ungated preemption pressure, without using the analyst’s posterior or saturation itself. On this definition, $`\operatorname{sat}_t`$ is a path-dependent ontic macro rather than an independent primitive or an epistemic estimate. For an assembly $`A`$ of frame type $`\varphi(A)`$ and registered at-issue niche $`n(A,c)`$, $`\mathrm{OBL}_t(n(A,c),c,A)`$ abbreviates $`\mathrm{OBL}_t(n(A,c),c,\varphi(A))`$. English progressive marking and Turkish evidential marking are the worked cases there.

Licensing is latent, and the Beta is typed over a rate rather than a fixed binary fact. Let $`z_{j,t}(\kappa,c)\in\{0,1\}`$ be speaker $`j`$’s local inclusion state for construction $`\kappa`$ in $`c`$. The population state $`\theta_t(\kappa,c)\in[0,1]`$ is the latent exchangeable licensing-rate parameter. For a randomly sampled exchangeable speaker, $`Z_t(\kappa,c)\mid\theta_t(\kappa,c)\sim \mathrm{Bernoulli}(\theta_t(\kappa,c))`$ is the predictive inclusion state for that speaker, and $`L_t(A,c)`$ is the event that the sampled speaker licenses all nodes in $`A`$. The definition needs a joint predictive distribution over the vector $`\{Z_t(\kappa,c):\kappa\in A\}`$. Posterior dependence among node rates represents epistemic co-uncertainty; it doesn’t by itself generate co-licensing within a speaker. A tractable joint model introduces a latent lect $`\ell_i\in\{1,\ldots,H\}`$ for speaker $`i`$:

```math
\ell_i\sim\mathrm{Categorical}(\boldsymbol{\pi}),\qquad
z_{i,t}(\kappa,c)\mid\ell_i=\ell\sim
\mathrm{Bernoulli}\!\left(\theta_{\ell,t}(\kappa,c)\right).
```

Conditional independence across nodes within a lect is still an approximation; an explicit within-lect joint can replace it where constructional kin cluster more tightly. Under this tractable version,

```math
P\!\left(L_t(A,c)=1\mid\boldsymbol{\pi},\boldsymbol{\theta}_t\right)=
\sum_{\ell=1}^{H}\pi_\ell\prod_{\kappa\in A}
\theta_{\ell,t}(\kappa,c),
```

and the marginal rate used elsewhere is $`\theta_t(\kappa,c)=\sum_\ell\pi_\ell\theta_{\ell,t}(\kappa,c)`$. The independent product of marginal node rates is a single-lect limiting case, not a general account of assembly prevalence.

No speaker or analyst observes $`\theta`$ directly. Under exchangeability, de Finetti’s representation theorem supplies a mixing measure over $`\theta`$ . The Beta family is the conjugate specialization that adds linear predictive updating: in the Bernoulli case, linearity of the posterior expectation of success in the counts is the binary analogue of Johnson’s sufficientness postulate in Zabell’s generalization . Direct inclusion observations would preserve that conjugacy. The choice observations used here don’t: a non-target choice has an affine likelihood in $`\theta`$, so its exact finite-window posterior is a Beta mixture. Section [4.3](#sec:update) uses the Beta family as an assumed-density approximation, matching the exact mixture’s mean and variance after each window. A speaker’s filter has mean $`C^{(i)}_t(\kappa,c)`$ and concentration $`\nu^{(i)}_t(\kappa,c)`$; an analyst can use the same family with a different evidence set, producing $`\widehat C_t`$ and $`\widehat\nu_t`$. The choice likelihood, memory discount, and moment projection are distinct modelling commitments. The population transition in [[eq:inclusion-transition]](#eq:inclusion-transition) states how speakers’ filters can alter later inclusion; updating an analyst posterior doesn’t alter the population. The vector $`\Lambda_{i,t}`$ collects speaker $`i`$’s inclusion states $`z_{i,t}(\kappa,c)`$, and the population distribution over those vectors supplies the population-level status state.

Compositional inheritance matters here. A novel token such as _She texted him the address_ needn’t have been encountered: the assemblies covering it are built from nodes–ditransitive transfer, pronominal object order, the relevant lexical-category relations–each with its own posterior, and the token inherits its status through them. What the learner updates is constructional regions, not memorized sentence types, so first-heard sentences aren’t predicted to have zero licensing. Actual statistical pooling would require hierarchical hyperpriors over construction families, lexemes, and situations; this core needs only the compositional inheritance just described.
## Grammatical status as a conditioned state property
### Status and its posterior estimate
For a form $`f`$, value $`v`$, and conditioning state $`c`$, let $`\mathcal{A}(f,v)`$ be the set of assemblies with yield $`f`$ and value $`v`$, and let $`\mathcal Y_{W_t}`$ collect the preceding window’s population realization rates, ungated pressure statistics, and prior obligatoriness state. The population state is

```math
\begin{equation}
S_t^{\theta}(f,v,c)=
P\Bigl(\,\exists A\in\mathcal{A}(f,v):\;
\operatorname{def}(A)\wedge\operatorname{sat}_t(A,c)\wedge L_t(A,c)
\,\Bigm|\,\boldsymbol{\theta}_t,\mathcal Y_{W_t},c\Bigr),
\label{eq:Gtheta}
\end{equation}
```

the prevalence, among exchangeable speakers in $`c`$, of at least one defined, saturated, licensed route to the form–value pair. The history argument is needed because $`\operatorname{sat}_t`$ inherits its path dependence from $`\mathrm{OBL}_t`$, which is determined by the preceding population window and prior convention state rather than by an instantaneous estimate. Neither a learner nor an analyst observes this population state directly. For an epistemic bearer $`r`$ (a speaker $`i`$ or an analyst $`a`$), the estimate is

```math
\begin{equation}
\widehat{S}^{(r)}_t(f,v,c)=
\mathbb{E}_{p_r(\boldsymbol{\theta}_t,\mathcal Y_{W_t}\mid\mathcal{D}_{r,t})}
\!\left[S_t^{\theta}(f,v,c)\right],
\label{eq:Gt}
\end{equation}
```

where $`\mathcal{D}_{r,t}`$ is that bearer’s evidence to date: tokens, structured omissions, repairs, avoidance, and situation cues. Status is the population property $`S_t^{\theta}`$; $`\widehat{S}^{(r)}_t`$ is a particular bearer’s estimate of it. For compactness, later predictive equations write $`G_t`$ for the analyst’s $`\widehat{S}^{(a)}_t`$ and $`g_{i,t}`$ for speaker $`i`$’s $`\widehat{S}^{(i)}_t`$. Where value is recoverable from context, I write $`G_t(u,c)`$ and $`S_t^{\theta}(u,c)`$ for readability. For a single pivotal node, $`S_t^{\theta}=\theta_t(\kappa,c)`$ when compatibility and saturation are fixed at one, so the estimate’s mean and concentration are literally the corresponding Beta posterior’s mean and concentration.

Two scope conditions matter. First, for a finite yield and a finite, non-empty-recursive construction inventory (no cycles of null-yield expansions–the standard offline-parsability condition), $`\mathcal{A}(f,v)`$ is finite, so the existential is a finite disjunction. No additional tractability stipulation is needed.

Second, the relation to simpler heuristics. In the high-precision limit, where every node posterior has concentrated, the pair [[eq:Gtheta]](#eq:Gtheta)–[[eq:Gt]](#eq:Gt) has the same limiting classification as a weakest-link rule over the best assembly: a licensed, defined, saturated assembly exists or it doesn’t. And under a single-lect, within-speaker node-independence approximation, posterior independence across nodes, and a single dominant assembly $`A^{\ast}`$, the mean factorizes,

```math
\begin{equation}
\widehat{S}^{(r)}_t(f,v,c)\approx \mathbf{1}\bigl[\operatorname{def}(A^{\ast})\bigr]
\cdot \mathbf{1}\bigl[\operatorname{sat}_t(A^{\ast},c)\bigr]
\cdot \prod_{\kappa\in A^{\ast}} C_t(\kappa,c).
\end{equation}
```

A three-factor product heuristic can work in easy cases as the single-assembly, independent, high-precision special case of [[eq:Gtheta]](#eq:Gtheta)–[[eq:Gt]](#eq:Gt), with structural viability as non-emptiness and hard compatibility folded into $`\operatorname{def}`$. Away from that limit, [[eq:Gtheta]](#eq:Gtheta) supplies the population state and [[eq:Gt]](#eq:Gt) its posterior mean, so uncertainty remains part of the status profile rather than being folded into the mean.

A three-factor heuristic can also hide content-oddness inside compatibility–the concentration of construal for cases like _colorless green ideas_. That work lives instead in the subjective read-out’s cost vector (§[3.7](#sec:feeling-new)). A lexically bizarre but operator-compatible construal doesn’t lower $`S_t^{\theta}`$ or its estimate and shows up as a plausibility cost in $`R_i`$: the sentence is grammatical and odd, matching the target contrast.
### Projectible use of the posterior state
Grammaticality projects over this posterior state. $`G_t`$ is compact notation for the analyst’s estimate $`\widehat{S}^{(a)}_t`$, the mean of a posterior random variable whose dispersion remains available for projection. Figure [2](#fig:state-space) depicts both the estimate and its dispersion.

The causal bearers remain speakers and their inclusion or evidence states. A speaker’s candidate availability gates production, while a hearer’s own estimate $`g_{i,t}`$ can enter repair:

```math
\begin{align}
\Pr_i(\text{produce }u\mid n,c,t) &\propto
  z_i(u,c)e^{U_{i,t}(u;n,c)}, \\
\Pr_i(\text{repair }u\mid c,t) &=
  \sigma\!\left(\eta_0+\eta_1
  \bigl(1-g_{i,t}(u,c)\bigr)\,r(\Delta,\iota)\right), \qquad \eta_1>0,
\end{align}
```

where $`z_i(u,c)`$ abbreviates availability of a complete route for speaker $`i`$ (expanded in §[4.2](#sec:usage)) and $`\sigma`$ is the logistic link.

The repair expression is the $`\Delta`$-sensitive form used in §[[sec:repair-controller]](#sec:repair-controller); if $`\Delta`$ and footing are marginalized out, it reduces to a monotone reduced form in $`1-g_{i,t}`$. Aggregate production and repair are obtained by integrating over speakers; $`G_t`$ predicts those rates but doesn’t cause them. This scopes the controller claim: licensing failures with readily recoverable intended updates but low update divergence should attract only baseline understanding-repair and, if stable, be supported mainly by preemption, while operator mis-settings draw the $`\Delta`$-scaled repair flow; correction rates should instead track ascription and prescriptive dissonance.

Other generalizations run over epistemic concentration, and they’re the diagnostic ones. Two form–value pairs can share a low mean while differing in how much evidence backs it, and the update dynamics make them behave differently under new exposure: a diffuse posterior moves with framing and familiarization; a concentrated one doesn’t. This epistemic dispersion is $`\operatorname{Var}(S_t^{\theta}\mid\mathcal{D}_{r,t})`$ for epistemic bearer $`r`$. Behavioral predictions use a speaker’s $`r=i`$ posterior; analyst-facing estimates use $`r=a`$. In single-node cases the corresponding concentration is the pivotal node’s $`\nu^{(r)}`$.

Population heterogeneity is different. A community can have a sharply estimated interior $`\theta`$ because speakers are genuinely split, as with _might could_ in a mixed community. That state has low epistemic variance but high between-speaker disagreement. The interior estimate counts as genuine heterogeneity only when no independently specifiable refinement of $`c`$ (§[3.6](#sec:identification-c)) splits the population toward the attractors; if such a partition exists, the apparent heterogeneity was a mis-specified conditioning state. Within-speaker test–retest instability and framing lability identify epistemic uncertainty; between-speaker disagreement with within-speaker stability identifies heterogeneity. Satiation and framing rank order turn on $`1/\nu`$. For a moribund contrast, falling concentration is the direct filter prediction; between-speaker dispersion is a separate, conditional outcome whose ordering depends on how histories, priors, networks, and cohorts diverge.

For a single node and epistemic bearer $`r`$, with $`\theta\mid\mathcal{D}_{r,t}\sim\mathrm{Beta}(a^{(r)},b^{(r)})`$, let $`C^{(r)}=E[\theta\mid\mathcal{D}_{r,t}]`$ and $`\nu^{(r)}=a^{(r)}+b^{(r)}`$. The two dispersions decompose as

```math
\begin{align}
U^{(r)}_{\mathrm{epi}} &= \operatorname{Var}(\theta\mid\mathcal{D}_{r,t})
  =\frac{C^{(r)}(1-C^{(r)})}{\nu^{(r)}+1},\\
U^{(r)}_{\mathrm{het}} &= E[\theta(1-\theta)\mid\mathcal{D}_{r,t}]
  =\frac{C^{(r)}(1-C^{(r)})\nu^{(r)}}{\nu^{(r)}+1}.
\end{align}
```

Their sum is the predictive variance of a newly sampled speaker’s inclusion state, $`C^{(r)}(1-C^{(r)})`$. For assemblies the corresponding quantities are $`U^{(r)}_{\mathrm{epi}}=\operatorname{Var}(S_t^{\theta}\mid\mathcal{D}_{r,t})`$ and $`U^{(r)}_{\mathrm{het}}=E[S_t^{\theta}(1-S_t^{\theta})\mid\mathcal{D}_{r,t}]`$. A preempted gap has low mean, low epistemic uncertainty, and low heterogeneity; a sparse form has appreciable epistemic uncertainty; a stably divided community has low epistemic uncertainty but high heterogeneity.

The status regions are:

- **licensed**: $`\widehat S^{(r)}_t\approx1`$, $`\operatorname{Var}(S_t^{\theta}\mid\mathcal{D}_{r,t})\approx0`$;

- **excluded**: $`\widehat S^{(r)}_t\approx0`$, $`\operatorname{Var}(S_t^{\theta}\mid\mathcal{D}_{r,t})\approx0`$–confident rejection, whether by structural failure or by concentrated non-licensing;

- **unsettled**: $`\operatorname{Var}(S_t^{\theta}\mid\mathcal{D}_{r,t})`$ high, in two subtypes–_starved_ (low concentration from a sparse opportunity set, as with independent relative _whose_) and _avoidance-divided_ (low concentration despite dense opportunities, from conflicting or absorbed evidence flows, as with defective cells, §[4.6](#sec:winnerless-cells));

- **heterogeneous**: posterior concentration high but the estimated population rate is interior–stable within speakers, divided across speakers.


The projectible generalizations–satiation profiles, framing sensitivity, transmission fidelity, repair rates, actuation–run over a state that carries the dimension they turn on. Left-branch extraction and _whose_ approach similar means and part on concentration; clean defective cells such as _pobedit’_ 1sg part from preempted gaps the same way. The dynamics module closes the temporal loop explicitly: production and repair generate later speaker evidence, speakers’ filters enter the adoption–retention kernel in [[eq:inclusion-transition]](#eq:inclusion-transition), and the resulting inclusion states determine the next population rate. The analyst posterior only tracks that loop.

Strictly, the object doing the projecting is the licensing profile $`(G_t,\nu)`$ plus independently estimated population heterogeneity, not the bare predicate grammatical. The classical predicate names the high-mean, high-concentration region of that profile. It projects only those expectations that don’t turn on concentration or heterogeneity; it doesn’t by itself predict processing cost, production frequency, language-model string probability, typological comparanda, or transfer across conditioning states without the situation posterior $`q_h(c\mid e)`$.

The epistemic status state has two dimensions. Preempted gaps (dense preemption, posterior concentrated near zero) and winnerless cells (readily identifiable candidates with weak support, low mean but diffuse evidence) share a low mean and part on concentration, the axis that predicts satiation, framing sensitivity, and actuation. Stable between-speaker heterogeneity is a separate dimension, not shown.
### Categorical talk as posterior concentration
Communities often treat grammaticality as a membership fact: a relationship counts as an available resource in $`c`$ or it doesn’t. On this account, a speaker’s categorical talk is expected where that speaker’s posterior has concentrated–where the estimated licensing state sits near an attractor and $`\operatorname{Var}(S_t^{\theta}\mid\mathcal{D}_{i,t})\approx0`$. Categoricality is a property of the population profile, not a threshold imposed by the analyst. Section [4.4](#sec:emergent-categoricality) gives conditional dynamics under which an independently fixed adoption criterion can yield separated attracting regions. In the contested middle, categorical talk is predicted to be unstable and stakes-sensitive.
### A decision-theoretic read-out
The response threshold $`\tau(c)`$ belongs in the read-out. A judge in $`c`$ chooses between in-repertoire and not-in-repertoire under asymmetric losses $`L_{\mathrm{fa}}(c)`$ and $`L_{\mathrm{fr}}(c)`$. The optimal rule accepts iff

```math
\begin{equation}
g_{i,t}(u,c)\geq \tau(c)
=\frac{L_{\mathrm{fa}}(c)}{L_{\mathrm{fa}}(c)+L_{\mathrm{fr}}(c)}.
\end{equation}
```

$`\tau(c)`$ does no constitutive work: it’s a decision criterion induced by payoff structure, strict in high-stakes institutional contexts, permissive in in-group ones. Where population licensing states are well separated, the read-out is insensitive to the exact value of $`\tau(c)`$; in the middle, judgments should be unstable and stakes-sensitive. A decision-layer discontinuity test can probe this read-out, but smoothness through $`\tau(c)`$ wouldn’t by itself refute the licensing-state theory.

Here “objective” means population-level and convention-constituted. The status stands apart from any individual’s response the way facts about word meaning or currency do: given the community’s practices, the projected relations aren’t made available by the analyst’s decision to group cases together . Conventional status would be an equally accurate name.

$`\tau(c)`$ and the adoption criterion $`q_\kappa`$ in [[eq:posterior-threshold-adoption]](#eq:posterior-threshold-adoption) have different roles. The former governs a judge’s response under independently measured stakes; the latter is a causal assumption about learning or coordination costs. Where licensing states are well separated, the read-out is insensitive to the exact value of $`\tau(c)`$; in the contested middle, $`\tau(c)`$ is set by independent stakes cues.
## The scope of the existential
Structural coverage is the non-emptiness of $`\mathcal{A}(f,v)`$: genuine analyzability failure is the case where no assembly covers the string at all. Conditional on a fixed inventory, $`S_t^{\theta}=G_t=0`$ from an existential over the empty set. With inventory uncertainty, the value is zero up to whatever posterior mass remains on an unobserved stored construction. Empty coverage is the categorical failure mode generated by structural failure alone.

A condition belongs in a form template only when violating it makes the intended value unrecoverable or the exponent unidentifiable as an instance of the construction. If the intended value is recoverable and the exponent is identifiable, the issue is licensing or compatibility, not coverage. This keeps template typing from becoming a way to relabel any concentrated licensing failure as structural failure.

Analyzability is relative to the constructional inventory, stored wholes included, not to productive composition alone. Syntactically anomalous idioms make the difference visible: _by and large_, _far be it from me_, and _come Monday_ have no analysis by the productive syntax of English, but they’re fully conventional . They’re covered by their own stored constructions–coverage by some node, productive or memorized, is what analyzability means here. The cost is explicit: non-emptiness isn’t pre-conventional. What it contributes is a different kind of failure (no covering assembly at all), not a convention-free one.

A string with no covering assembly gets $`G_t=0`$ conditional on the inventory; a preempted gap gets $`G_t\approx0`$ from a covering assembly licensed to zero. Both are excluded, and they differ in _why_–no assembly versus licensed-to-zero assembly–a difference with an empirical signature: the first fails under every construal and resists all framing once the relevant inventory is fixed; the second has a readily recoverable construal, resists framing by concentration (§[3.3.2](#sec:projectible-use)), and is predicted to be re-openable only by the actuation route of §[4.8](#sec:actuation). The constitutive core stays minimal without losing the distinction.

Because the existential is over value-matched assemblies, homophonous strings can split by construal. A form with one clashing parse and one compatible parse is grammatical on the compatible value and excluded on the clashing value; ambiguity doesn’t let a failed assembly contaminate a successful one.
### Assigning a failure
The result is a four-step diagnostic procedure, applied before consulting acceptability data and checkable against the independent indicators of §[3.6](#sec:identification-c) at each step.

Ask first whether any assembly covers $`u`$: if none does, the failure is structural (*_Can the have running_). If a covering assembly exists, ask whether its operator contributions unify: if every covering assembly sets some dimension twice incompatibly, the failure is compatibility (*_I’ve finished it yesterday_–two values on the reference-interval dimension; and the information-packaging clash in Cuneo and Goldberg’s island example is the same formal object on a different dimension ).

If the contributions unify, ask whether the obligatory dimensions are saturated: if not, the failure is saturation (unmarked progressive in an ongoing-at-issue English niche). Only then does licensing arbitrate: a defined, saturated assembly whose pivotal node the population withholds is a licensing failure (*_I have 25 years_ for age–the assembly is compatible, the intended value is recoverable, and the age-predication node sits at $`C_t\approx0`$ under preemption by the be-frame).

Because the dimension inventory $`O(c)`$ is itself conventionalized, what counts as a compatibility failure in $`c`$ depends on which contrasts the community has conventionalized. The steps are ordered, not independent–and each step’s verdict is checkable against evidence other than the judgment it explains, which is what keeps the procedure from reproducing the circularity of a pure community-verdict account.
## Interlocutor misalignment about conditioning
Because $`c`$ is construed, interlocutors can disagree about which conditioning state is in force. Let a hearer $`h`$ maintain a posterior $`q_h(c\mid e)`$ over conditioning states given cues $`e`$ (situational cues, ascription cues, stance cues, etc.). Then the hearer’s expected status is

```math
\begin{equation*}
\hat{G}^{(h)}_{t}(u\mid e)=\sum_{c\in\mathcal{C}} G_t(u,c)\,q_h(c\mid e).
\end{equation*}
```
## Identifying the conditioning state before prediction
The conditioning state $`c`$ isn’t a free parameter to be selected after a judgment is observed. For empirical work, $`c`$ has to be fixed before predicting ratings or repair behaviour. The posterior $`q_h(c\mid e)`$ is the identification device, estimated from non-judgment cues such as activity type, medium, participant roles, speaker ascription, register cues, and overt norm orientation. A form like _might could_ isn’t rescued by choosing a sympathetic norm-centre after the fact; the model predicts different judgments only when the independent cues make that norm-centre probable.

Separate evidence streams identify the licensing and performance layers. $`C_t`$, the posterior mean of the population licensing rate, is identified by corpus-rate-per-opportunity, elicited production, and repair behaviour, not by acceptability ratings alone. $`F`$, the anomaly signal, is identified by ratings, online measures, and self-reports. The confidence read-out $`\Phi`$ (§[3.7](#sec:feeling-new)) is identified by test–retest stability and explicit confidence ratings, neither of which enters the estimation of the licensing posterior itself. Framing lability is a confirmatory outcome, not an identifying input. The model is falsified where these dissociate in the wrong direction: if satiation changes later corpus rates for a purportedly preempted gap, if repair behaviour tracks prescriptive dissonance rather than licensing, or if high-opportunity preempted forms behave like low-evidence uncertainties, the state assignment is wrong.

Reassignment is constrained. Localizing a failed prediction to a narrower conditioning state is warranted only when that state is specifiable independently of the surviving cases, by activity type, medium, participant roles, or norm-orientation fixed before the failures were seen . A partition of $`\mathcal{C}`$ redrawn around exactly the successes redescribes failure as success; it doesn’t rescue the model.

Confirmatory studies should register the conditioning partition and the protocol for estimating $`\rho_t^\star`$ and $`\widetilde{\rho}_t^\star`$ (e.g.  forced-choice norming over the competitor set, with the outside option retained for the latter, before the licensing data is touched). The corpus checks in this paper are illustrative probes, not registered tests. Under that discipline, repeated post-hoc reassignment across future studies counts against the framework itself, not just against particular state assignments.

The same discipline applies to the construction inventory $`\mathcal H`$, its template-to-frame typing, and the mapping from candidate realizations to assemblies and pivotal nodes. These choices must be fixed before the target judgments or corpus absences are inspected, alongside $`c`$, $`n`$, $`\widetilde{\rho}_t^\star`$, and $`\tau(c)`$. A later inventory change may be a legitimate reanalysis, but it must be reported as such rather than treated as if the original prediction had survived. The untensed $`\mathcal H`$ is the registered representational inventory for a study, not the set of currently licensed constructions: diachronic entry and exit occur through $`z_{i,t}`$ and $`\theta_t`$. Expanding $`\mathcal H`$ is a separately reported model revision.

Two identification points follow from the fact that a corpus rate conflates availability and counterfactual choice (§[4.2](#sec:usage)), not licensing alone. First, the relevant counterfactual choice term has to be estimated from evidence that doesn’t include the licensing data it later interprets. A forced-choice norming task supplies it: present the niche $`n`$ and the competitor set $`\mathcal{V}_{n,t}^{\star}`$ to a separate sample and record how often each candidate is chosen when stipulated to be available. Candidate-only choice yields $`\rho_t^\star`$; retaining avoidance, periphrasis, and repair-in-progress yields the full-choice $`\widetilde{\rho}_t^\star`$ required by the production and omission models. Both are fixed before any corpus rate for $`u`$ is consulted, so a low rate can be diagnosed as non-licensing ($`C_t\!\approx\!0`$, $`\widetilde{\rho}_t^\star`$ high) rather than licensed-but-dispreferred selection ($`C_t`$ high, $`\widetilde{\rho}_t^\star\!\approx\!0`$).

Second, $`\tau(c)`$ isn’t fit to the judgments it predicts. Where population licensing states are well separated (§[4.4](#sec:emergent-categoricality)), $`G_t`$ is insensitive to the exact threshold, so no point estimate of $`\tau(c)`$ is needed; in the contested middle, $`\tau(c)`$ is set by independent stakes cues (institutional versus in-group footing), and the movable-cutoff prediction of §[3.3.4](#sec:decision-readout) tests the decision layer directly: manipulate the stakes and the location of any response-type switch should move, which can’t happen if $`\tau(c)`$ were merely a curve fitted to the responses.

The niche $`n`$ is disciplined in the same way as $`c`$. Before an absence is counted as preemption, the analyst has to specify the communicative job, the recoverable intended value, the competitor set, and the outside option without using the target’s acceptability as the criterion. The counterfactual choice terms $`\rho_t^\star(u\mid n,c)`$ and $`\widetilde{\rho}_t^\star(u\mid n,c)`$ are then normed independently, for example by forced choice under a stipulation that all candidates in the set are available, once without and once with the outside response.

A low-rate candidate counts as preempted only when $`N_t(n,c)`$ is large, $`\widetilde{\rho}_t^\star`$ is non-negligible, and omissions are attributable to competitor choice rather than avoidance; otherwise the same absence is starved or divided. Classifications of low-mean cases should be reported with robustness checks across at least two plausible niche granularities.
## The feeling of (un)grammaticality
Speakers register putative violations through a metacognitive signal that can diverge from status; the two are identified by different evidence streams (§[3.6](#sec:identification-c)). The observable phenomenology is modeled as a pair: a signed anomaly signal and a confidence read-out. The pair is what lets the model distinguish confident rejection from ineffability.

Let $`\hat{G}^{(h)}_{i,t}(u\mid e)`$ be hearer $`i`$’s expected status under situation uncertainty (§[3.5](#sec:misalignment-conditioning)). Write $`R_i(u,e)`$ and $`I_i(u,e)`$ for implementation costs and prescriptive dissonance after cue-based situation uncertainty has been integrated. The anomaly drive accumulates low expected status, implementation costs, and ideological overlays:

```math
\begin{align}
M_{i,t}(u,e) &= \alpha_G\bigl(1-\hat{G}^{(h)}_{i,t}(u\mid e)\bigr)
  +\gamma^{\top} R_i(u,e)+\delta_I\,I_i(u,e)+\varepsilon_i, \\
F_{i,t}(u,e) &= -\frac{\max\{M_{i,t},0\}}{1+\max\{M_{i,t},0\}}
  \in (-1,0].
\end{align}
```

The bounded link and the floor at zero encode the asymmetry of the signal: there’s no positive feeling of grammaticality, only the negative signal registered on deviation. $`I_i`$ is prescriptive dissonance. The cost vector $`R_i`$ includes the processing components–the locality term $`\mathcal{L}_{\mathrm{loc}}(u)`$ with its saturating form, interference, garden-path reanalysis, surprisal–and a plausibility component: the implausibility of the best construal given world knowledge and lexical expectations. That component handles content oddness without making it a status fact. _Colorless green ideas sleep furiously_ is defined, saturated, and licensed node by node, so $`G_t\approx1`$; its strangeness enters here, as a construal-plausibility cost, and the sentence comes out grammatical and odd, with no extra primitive.

The locality component can still be written explicitly:

```math
\begin{equation*}
\mathcal{L}_{\mathrm{loc}}(u)=
\sum_{d\in\mathcal{D}_{\mathrm{dep}}(u)}\ell\!\bigl(|d|\bigr),\qquad
\ell(k)=
  \begin{cases}
    k, & k\le K_{\text{sat}},\\[4pt]
    K_{\text{sat}}+\beta_L\,(k-K_{\text{sat}})^{\eta_L}, & k>K_{\text{sat}}.
  \end{cases}
\end{equation*}
```

Here $`|d|`$ is the length of dependency $`d`$ (in intervening discourse referents or words), $`K_{\text{sat}}`$ is a saturation threshold beyond which additional distance contributes sublinearly, and $`\beta_L,\eta_L`$ (with $`0<\eta_L<1`$) control the rate of that sublinear growth.

The second read-out is confidence. Two quantities matter. Let $`\nu_i(u,e)`$ be the concentration of $`i`$’s posterior over the _pivotal condition_–the conjunct in [[eq:Gtheta]](#eq:Gtheta) on which the token’s status turns–after cue-based situation uncertainty has been integrated. Conditional on an independently fixed $`c`$, write $`\nu_i(u,c)`$; if the pivotal condition differs across high-probability conditioning states, the observable confidence read-out follows the modal condition and treats the remaining mixture as lower confidence. For structural and compatibility failures the pivotal condition is a fact about the assembly set, so once the relevant inventory is fixed that posterior is treated as effectively degenerate: confidence is high by modelling convention, not by a separate learning theorem. For licensing-pivotal tokens, $`\nu_i`$ is the Beta concentration of the pivotal node’s posterior (§[4.3](#sec:update)).

Evidence confidence, the quantity that predicts framing lability, is

```math
\begin{equation}
\Phi^{\mathrm{ev}}_{i,t}(u,e)=\frac{\nu_i(u,e)}{\nu_i(u,e)+\nu_0}
\in [0,1),
\end{equation}
```

with $`\nu_0`$ a scaling constant. Confidence in a binary in-repertoire/not-in-repertoire verdict also depends on where the posterior mass lies relative to the decision threshold:

```math
\begin{equation}
\Phi^{\mathrm{dec}}_{i,t}(u,e)=
\max\!\left\{
P\!\left(S_t^{\theta}(u,c^\ast)\ge\tau(c^\ast)\mid\mathcal{D}_{i,t},e\right),
P\!\left(S_t^{\theta}(u,c^\ast)<\tau(c^\ast)\mid\mathcal{D}_{i,t},e\right)
\right\}.
\label{eq:phi-dec}
\end{equation}
```

A sharply estimated interior population split has high $`\Phi^{\mathrm{ev}}`$ but low decision confidence if its mass lies near $`\tau(c)`$. Here $`c^\ast`$ is the modal conditioning state under $`q_h(c\mid e)`$; residual situation uncertainty lowers the effective confidence as described above. In the prose below, $`\Phi`$ names the relevant observed confidence read-out: decision confidence for explicit verdicts, evidence confidence for framing and familiarization predictions. The pair $`(F,\Phi)`$ is the observable phenomenology, and the predictions separate:

- _No assembly_ (*_Can the have running_): $`F`$ strongly negative, $`\Phi\approx1`$, under every construal.

- _Compatibility failure_ (*_I’ve finished it yesterday_): $`F`$ strongly negative, $`\Phi\approx1`$; entrenchment of the parts can’t repair it, because unification is hard.

- _Preempted gap_ (left-branch extraction if $`\widetilde{\rho}_t^\star`$ norms high): $`F`$ strongly negative, $`\Phi`$ high–“that’s impossible”; framing-resistant.

- _Defective cell_ (_pobedit’_ 1sg; *_amn’t_ as a borderline case): $`F`$ negative, $`\Phi`$ low–“I don’t know how to say it”; framing-movable when the outside option, rather than a winner, absorbs production.

- _Community-novel_ (independent relative _whose_): $`F`$ weakly negative, $`\Phi`$ low; framing-movable, with surprisal adding $`R`$-channel noise.

- _Processing overload_ (centre embedding): $`F`$ negative via $`R_i`$, $`\Phi`$ moderate; satiation lowers the $`R`$ contribution, moving $`F`$ toward zero without touching the licensing posterior.


Optionally, the model can carry an attribution variable: on anomaly detection the hearer infers a source $`\zeta\in\{\textsc{unlicensed},\textsc{other-community},\textsc{speaker error}, \textsc{noise},\textsc{own overload}\}`$, with the posterior over $`\zeta`$ shaped by $`\Phi`$ and by the same ascription machinery as $`q_h(c\mid e)`$. That gives a measurement route for why learner errors and cross-dialect tokens fail to trigger the same anomaly signal–they’re attributed to other-community or error–and it gives the misattribution effects of §[2.4](#sec:subjective) a formal home. The attribution layer is a measurement refinement, not part of status.

A direct falsifier follows: if measured confidence fails to dissociate preempted gaps from clean winnerless cells such as _pobedit’_ 1sg at matched mean ratings, posterior concentration has no independent empirical role in the model.
## Measurement: four observation channels
Status is latent; it’s estimated from converging observation channels, none of which defines it. The observation model has four channels:

```math
\begin{align}
&P(\text{production}_i\mid\Lambda_{i,t},n,c)
  && \text{choice among assemblies in a niche (\S\ref{sec:usage})} \\
&P(\text{repair}_i\mid\Lambda_{i,t},\Delta,I,c)
  && \text{sensitive to operator mis-setting (\S\ref{sec:repair-controller})} \\
&P(\text{judgment}_i\mid \hat{G}^{(h)},R_i,I_i,\nu_i,\tau)
  && \text{the }(F,\Phi)\text{ read-out of \S\ref{sec:feeling-new}} \\
&P(e\mid c),\ P(c)
  && \text{cue generation and situation prior; }q_h(c\mid e)\text{ follows by Bayes}
\end{align}
```

Production is choice among assemblies, not a direct read of licensing: a corpus rate reflects both availability and counterfactual choice, approximated by their product in the single-pivotal-node regime described in §[4.2](#sec:usage), and the identification discipline of §[3.6](#sec:identification-c) (norming $`\widetilde{\rho}_t^\star`$ on independent data before the licensing data is touched) applies here. Repair enters with the sign predicted in §[3.3.2](#sec:projectible-use) and with the $`\Delta`$-sensitivity of the repair stream (§[[sec:repair-controller]](#sec:repair-controller)). Judgment is a metacognitive read-out, not status; the confidence channel $`\Phi`$ is identified by test–retest stability and explicit confidence ratings, with framing lability reserved for confirmation. Situation is inferred from cues, not stipulated after the fact. A fit-ready version would have to compose the channels as a joint likelihood over production, repair, judgment, confidence, and situation cues with shared latent $`\ell_i`$, $`\Lambda_{i,t}`$, $`\boldsymbol{\theta}_t`$, and $`c`$, together with $`n`$ where it isn’t fixed by an independent coding protocol. The situation posterior $`q_h(c\mid e)`$ is derived from $`P(c)P(e\mid c)`$ rather than treated as a generative observation channel. Identifiability requires at least one non-judgment channel for $`\boldsymbol{\theta}`$, one non-repair estimate of $`\Delta`$, and independently specified niches, candidate sets, and assembly availability.

Factor analyses of acceptability ratings target the structure of the judgment channel; a factor counts as evidence about the grammar only when it also shows up in the independent indicators for licensing and compatibility. Judgment studies should report dispersion and test–retest structure alongside means, because the model’s sharpest projections–satiation rank order, framing lability, the gap/cell contrast–run over the concentration that means discard.

The corpus-rate-per-opportunity indicator is concrete. Figure [3](#fig:agr-projection) shows one worked case: agreement on collective-partitive subjects (_a bunch of people_, _the majority_), where surface-head number (singular) and notional number (plural) diverge. The usage pattern is overwhelmingly one-sided, which makes the case useful as an audit trail. Counting only subject-position tokens after KWIC filtering (so non-subject false positives are removed) gives a plural-agreement share with a Wilson interval for each cell. The shares sit far above parity in all four tabulations, which cover three constructional cells because the exact and audit-augmented majority rows are nested views of one cell. Interval width tracks token count rather than direction. The example supplies production-choice evidence per opportunity rather than a licensing estimate by itself. It bears on licensing only if independent norming shows that the singular candidate and the outside option would otherwise have non-negligible choice mass; the Wilson intervals quantify sampling uncertainty in the production share, not uncertainty about licensing.

Production-choice evidence for a prescriptively salient agreement contrast. Plural-agreement share (dot) with Wilson 95% interval (bar) for collective-partitive subjects in coca, after kwic filtering to subject-position tokens; the dashed line marks parity (no directional preference). The share is a licensing indicator only conditional on independent norming of candidate and outside-option choice. Data: `agr-coca-projection` probe (_bunch_, _majority_/_minority_, and partitive cells). Notional plural dominates in each of the three constructional cells, and the interval widens with the smaller denominators rather than drifting toward parity.

Table [4](#tab:agr-cells) makes the figure auditable: exact filtered cell counts, so the estimate can be checked rather than taken on trust.

| Cell | pl. | sg. | $`N`$ | Plural share (Wilson 95%) |
| :--- | ---: | ---: | ---: | :--- |
| _a bunch of_ + animate pl. | 71  | 1   | 72  | 0.986 (0.925–0.998) |
| _the majority_ + set (exact) | 105 | 0   | 105 | 1.000 (0.965–1.000) |
| _the majority_ + set (audited) | 142 | 0   | 142 | 1.000 (0.974–1.000) |
| _the rest of the people_ | 14  | 0   | 14  | 1.000 (0.785–1.000) |

Filtered agreement cells behind Figure [3](#fig:agr-projection). Counts are kwic-filtered subject-position tokens in coca; “pl.” and “sg.” are plural- and singular-agreement targets. The surface-head baseline predicts singular; the observed share is plural. {#tab:agr-cells}
## Worked examples: deriving status from the posterior
The examples from §[2.2](#sec:diag-tree) show how population status and its posterior estimate are related. The winnerless cell adds the case where concentration carries the phenomenology rather than merely labelling it.

1. *_Can the have running_ (nonsense). $`\mathcal{A}(f,v)=\emptyset`$: no covering assembly in the fixed inventory. $`S_t^{\theta}=G_t=0`$ up to inventory uncertainty; $`\Phi\approx1`$ under every construal. Status: ungrammatical, structurally.

2. _Colorless green ideas sleep furiously_. A covering assembly is defined, saturated, and licensed node by node: $`S_t^\theta\approx1`$, with $`G_t`$ and a typical $`g_{i,t}`$ tracking it. The strangeness is a construal-plausibility cost in $`R_i`$: $`F`$ negative, status grammatical. Content-odd, not ill-formed.

3. *_I’ve finished it yesterday_ (compatibility failure). Covering assemblies exist, but every one sets the reference-interval dimension twice incompatibly–the perfect’s contribution and the deictic adverb’s don’t unify–so $`\operatorname{def}(A)=0`$ throughout. $`S_t^{\theta}=G_t=0`$; $`\Phi\approx1`$. Entrenchment of the component constructions can’t repair it: the clash is outside the licensing terms altogether.

4. *_I have 25 years_ (licensing failure). Defined and saturated; the intended value is recoverable. The pivotal age-predication node has $`\theta_t\approx0`$, tracked by a typical speaker at $`C^{(i)}_t\approx0`$ with high $`\nu^{(i)}`$, after preemption by the be-frame in a dense niche. $`g_{i,t}\approx0`$ and $`\Phi`$ is high. Status: ungrammatical, by concentrated non-licensing.

5. ?_friend of whose_ (community-novel). Defined and saturated; the niche is vanishingly sparse, so a typical speaker’s pivotal-node posterior sits near its prior with low $`\nu^{(i)}`$. The speaker’s $`g_{i,t}`$ is intermediate, $`\operatorname{Var}(S_t^{\theta}\mid\mathcal{D}_{i,t})`$ is high, and $`\Phi`$ is low. Status: unsettled (starved); framing-movable, with surprisal adding $`R`$-channel noise.

6. *_Which did you buy car?_ (putative preempted gap). Defined and saturated; the dedicated discontinuity node–the only activated node covering the determiner–head discontinuity–receives negative evidence from fronting opportunities only in proportion to independently normed $`\widetilde{\rho}_t^\star`$. If that full-choice term is high, its posterior is driven to zero and concentrates there (§[4.3](#sec:update)); if it’s low, the case belongs closer to starvation. Status assignment requires the niche-norming protocol of §[3.6](#sec:identification-c).

7. _pobedit’_ 1sg (winnerless cell; *_amn’t_ as a mixed case). The niche is dense and candidate assemblies have readily recoverable values, but candidate support is weak and no candidate accumulates positive evidence–the outside option absorbs production, and because avoidance has low attributability, candidates accumulate little confident negative evidence either (§[4.6](#sec:winnerless-cells)). Given that low support, every candidate’s pivotal node has a low speaker-level mean and low $`\nu^{(i)}`$. The typical $`g_{i,t}`$ is low, $`\operatorname{Var}(S_t^{\theta}\mid\mathcal{D}_{i,t})`$ is high, and $`\Phi`$ is low. Status: unsettled (avoidance-divided); phenomenology ineffability, not rejection–same mean as a preempted gap, different concentration, different feeling.

8. _The bread the baker the apprentice helped made is delicious_ (processing overload). A typical $`g_{i,t}`$ is high; the locality term in $`R_i`$ is large. $`F`$ is negative and $`\Phi`$ moderate; satiation and instruction move the $`R`$ contribution, not the licensing posterior. Status: grammatical, transiently ill-felt.


Figure [4](#fig:posterior-means) shows the low-opportunity versus dense-preemption contrast that underwrites several of these classifications.

Licensing posteriors under the affine omission likelihood, from a Beta(1, 1) prior. The sparse arm receives one attributable omission every ten steps (five total); the dense arm receives five per step (250 total). Each omission has _d_ = .495, derived from equal-utility candidates and outside utility −4. Lines are moment-matched posterior means; shading gives 95% Beta intervals. Sparse evidence leaves a broad posterior even as its mean moves, while dense preemption lowers the mean and raises concentration. Population actuation also requires the transition in [[eq:inclusion-transition]](#eq:inclusion-transition).
# Dynamics: candidate routes to stabilization
The dynamics module explains trajectories of construction-level licensing posteriors, and in principle refinements of the conditioning partition itself. It doesn’t define grammaticality.
## Niches, competitors, and opportunity sets
Let $`n`$ index a constructional niche (a communicative job), and let $`\mathcal{V}_{n,t}^{\star}`$ be the opportunity set: the observed, licensed, and analogically generated candidate realizations that could plausibly do that job in some conditioning states. Let $`N_t(n,c)`$ be the number of opportunities for niche $`n`$ in conditioning state $`c`$ over some time window, and $`k_t(x,n,c)`$ the observed count of candidate realization $`x\in\mathcal{V}_{n,t}^{\star}`$.

The star matters. Preempted gaps and innovations often involve candidates with no positive tokens. Their counterfactual utilities are still defined because the hierarchy $`\mathcal{H}`$ generates analogical candidates. English learners can represent a left-branch extraction candidate by combining interrogative fronting, modifier–noun packaging, and question formation, even if no one licenses that candidate as an English resource. The same machinery lets a novel but ordinary sentence inherit coverage from licensed higher-grain constructions rather than being preempted merely because that exact sentence type is new.
## Usage as licensing $`\times`$ choice among candidates
Separate licensing from selection. A candidate can be licensed but rarely chosen.

Let $`\rho_t^\star(x\mid n,c)\in[0,1]`$ be the candidate-conditional counterfactual probability of choosing $`x`$ if every registered candidate were available in niche $`n`$ under $`c`$. A flexible choice model is a softmax over utilities:

```math
\rho_t^\star(x\mid n,c)=
\frac{e^{U_t(x;n,c)}}{\sum_{x'\in\mathcal{V}_{n,t}^{\star}}e^{U_t(x';n,c)}},
\qquad
U_t(x;n,c)=\mathbf{w}^{\top}\mathbf{f}(x;n,c).
```

Because the production model also contains an outside option, the quantity that enters a licensing–usage factorization is instead the full-choice share

```math
\widetilde{\rho}_t^\star(x\mid n,c)=
\frac{e^{U_t(x;n,c)}}
{e^{U_t(\bot;n,c)}+
 \sum_{x'\in\mathcal{V}_{n,t}^{\star}}e^{U_t(x';n,c)}}.
```

The two coincide only when the outside option has negligible mass. Empirical norming has to offer the relevant avoidance, periphrasis, or repair-in-progress response as well as the candidate realizations; a candidate-only forced choice estimates $`\rho_t^\star`$, not $`\widetilde{\rho}_t^\star`$.

At the population level, the expected usage rate is

```math
\pi_t(x\mid n,c)=
E_i\!\left[
\frac{z_i(x,c)e^{U_t(x;n,c)}}
{e^{U_t(\bot;n,c)}+
\sum_{x'\in\mathcal{V}_{n,t}^{\star}}z_i(x',c)e^{U_t(x';n,c)}}
\right],
```

where, for a candidate $`x`$ with form–value pair $`(f_x,v_x)`$,

```math
z_i(x,c)=\mathbf{1}\!\left[
\exists A\in\mathcal{A}(f_x,v_x):
\operatorname{def}(A)\wedge\operatorname{sat}_t(A,c)\wedge
\bigwedge_{\kappa\in A}z_{i,t}(\kappa,c)
\right]
```

abbreviates speaker $`i`$’s availability of a complete licensed route for $`x`$ (with the time index suppressed on the left), and $`\bot`$ is the outside option (avoidance, periphrasis, or repair-in-progress). A candidate realization appears once in the softmax: if several assemblies license the same realization, the existential above aggregates them into the single gate $`z_i(x,c)`$ rather than adding separate choice masses. With several required nodes, the expectation is evaluated over the joint inclusion model rather than inferred from marginal node means alone. When one pivotal availability gate dominates and the other gates and full-set choice weights have been normed independently, the predictive product $`\pi_t(x\mid n,c)\approx S_t^\theta(x,c) \widetilde{\rho}_t^\star(x\mid n,c)`$ is a useful population-level approximation. In single-pivotal-node cases this reduces to $`\theta_t(\kappa_x,c)\widetilde{\rho}_t^\star(x\mid n,c)`$, where $`\kappa_x`$ is the node that would realize $`x`$ in $`c`$. The corresponding analyst prediction replaces $`S_t^\theta`$ with $`G_t`$, or $`\theta_t`$ with $`\widehat C_t`$, as an estimation step; it doesn’t identify the ontic usage rate with the estimate. The full-choice term can be high even when the population availability is near zero, so absence becomes informative under that condition.
## Dynamics: evidence streams, weighted omissions, and repair
Speaker $`i`$ represents each construction–situation pair $`(\kappa,c)`$ with a Beta filter over the population licensing rate $`\theta_t(\kappa,c)`$ (§[3.2](#sec:objects)); the analyst may use the same family on a different data stream. The Beta is exact after direct Bernoulli inclusion observations, but the observable data here are gated choices. A target choice supplies a factor proportional to $`\theta`$; a non-target choice supplies an affine factor in $`\theta`$. The resulting finite-window posterior is generally a Beta mixture. The bounded filter below projects that exact mixture back to Beta by matching its first two moments.

Discount accumulated evidence before applying the new window. For baseline prior $`\mathrm{Beta}(a^0,b^0)`$ and memory $`\delta_m\in(0,1]`$, put

```math
\begin{equation}
\widetilde a_t=a^0+\delta_m(a_t-a^0),\qquad
\widetilde b_t=b^0+\delta_m(b_t-b^0).
\label{eq:baseline-discount}
\end{equation}
```

A quiet filter returns to its stated prior. The recurrence discounts the accumulated state, and the current window enters once. Setting $`\delta_m=1`$ gives a fixed-parameter filter, while $`\delta_m<1`$ is an assumed-density dynamic filter for a drifting convention .

Consider a non-target outcome $`y_j\ne x`$. Let

```math
\begin{equation}
\ell_j(x)=\log P(y_j\mid Z_x=0,n,c)-
\log P(y_j\mid Z_x=1,n,c)
\label{eq:attributability}
\end{equation}
```

be its omission log likelihood ratio, used here as an information diagnostic. The update itself uses the probability-space contrast below. With $`r_j\in[0,1]`$ the independently coded probability that the occasion is attributable to the target niche, define

```math
\begin{equation}
d_j=r_j\left(1-
\frac{P(y_j\mid Z_x=1,n,c)}{P(y_j\mid Z_x=0,n,c)}\right)\in[0,1].
\label{eq:preemption-mass}
\end{equation}
```

Marginalizing the latent availability state $`Z_x\sim\mathrm{Bernoulli}(\theta)`$ gives, up to a constant independent of $`\theta`$,

```math
P(y_j\mid\theta,n,c)\ \propto\ 1-d_j\theta.
```

Attribution scales $`d_j`$ in probability space: with probability $`1-r_j`$ the event is uninformative, and with probability $`r_j`$ it carries the full counterfactual contrast.

If the window contains $`s_t`$ target choices and $`m_t`$ non-target choices, its exact posterior kernel after [[eq:baseline-discount]](#eq:baseline-discount) is

```math
\begin{equation}
p_{t+1}(\theta)\ \propto\
\theta^{\widetilde a_t-1+s_t}(1-\theta)^{\widetilde b_t-1}
\prod_{j=1}^{m_t}(1-d_j\theta).
\label{eq:affine-window-posterior}
\end{equation}
```

The affine product has the Bernstein expansion

```math
\prod_{j=1}^{m_t}(1-d_j\theta)=
\sum_{k=0}^{m_t}c_k\theta^k(1-\theta)^{m_t-k},
```

where $`c^{(0)}_0=1`$ and $`c^{(j+1)}_k=c^{(j)}_k+(1-d_{j+1})c^{(j)}_{k-1}`$, with out-of-range coefficients zero. Hence [[eq:affine-window-posterior]](#eq:affine-window-posterior) is exactly a mixture of at most $`m_t+1`$ Betas,

```math
\mathrm{Beta}(\widetilde a_t+s_t+k,
              \widetilde b_t+m_t-k),
```

with normalized weights proportional to the corresponding $`c_k`$ times the Beta normalizer. Let $`\mu_{t+1}`$ and $`v_{t+1}`$ be that mixture’s exact mean and variance. The bounded assumed-density step is

```math
\begin{align}
\nu_{t+1}&=\frac{\mu_{t+1}(1-\mu_{t+1})}{v_{t+1}}-1, &
a_{t+1}&=\mu_{t+1}\nu_{t+1}, &
b_{t+1}&=(1-\mu_{t+1})\nu_{t+1},\\
C_{t+1}&=\frac{a_{t+1}}{a_{t+1}+b_{t+1}}, &
\nu_{t+1}&=a_{t+1}+b_{t+1}.
\label{eq:beta-update}
\end{align}
```

This projection preserves the exact first two posterior moments but not, in general, higher moments. Its approximation error is part of the model audit. Direct target observations, $`d_j=0`$, and $`d_j=1`$ recover the relevant conjugate limits.

The equations describe one pivotal availability gate. If a token’s parse or niche attribution is uncertain, that uncertainty is marginalized in its likelihood before $`d_j`$ is calculated. A genuinely multi-node target requires the joint inclusion model from §[3.2](#sec:objects); one omission LLR can’t be split into independent node failure counts.

Population change enters through an explicit learner-to-population transition kernel. Let $`C^{(i)}_{\kappa,c,t}`$ and $`\nu^{(i)}_{\kappa,c,t}`$ be speaker $`i`$’s filter summaries, let $`\xi_{i,t}`$ collect lect, network, and other independently specified adoption covariates, and let $`\lambda_{i,\kappa}\in[0,1]`$ govern persistence. Then

```math
\begin{equation}
z_{i,t+1}(\kappa,c)\sim\operatorname{Bernoulli}\!\left(
  (1-\lambda_{i,\kappa})z_{i,t}(\kappa,c)+
  \lambda_{i,\kappa}h_\kappa(C^{(i)}_{\kappa,c,t},
    \nu^{(i)}_{\kappa,c,t},\xi_{i,t},c)\right),
\label{eq:inclusion-transition}
\end{equation}
```

where $`h_\kappa\in[0,1]`$ is an adoption–retention response fixed independently of the outcome being predicted. The numerical analysis below uses

```math
\begin{equation}
h_\kappa(C,\nu;q_\kappa)=
P(\theta\geq q_\kappa\mid C,\nu),
\label{eq:posterior-threshold-adoption}
\end{equation}
```

which can be read as posterior sampling against an adoption criterion. $`q_\kappa`$ has to be fixed from independently measured switching or coordination costs, while concentration supplies the response’s curvature. This causal transition parameter is distinct from the judge’s non-constitutive read-out threshold $`\tau(c)`$ in §[3.3.4](#sec:decision-readout). A logistic response to $`C-q_\kappa`$ remains a reduced-form sensitivity analysis only when its slope is independently estimated. The persistence term allows stable individual lects even when the population is divided. For a finite population of $`M`$ speakers, distinguish the empirical prevalence

```math
\theta^{(M)}_{t+1}(\kappa,c)=\frac{1}{M}\sum_{i=1}^{M}
z_{i,t+1}(\kappa,c)
```

from the exchangeable rate $`\theta_{t+1}`$. Conditional on the current population state, the expected empirical prevalence is the average of the transition probabilities in [[eq:inclusion-transition]](#eq:inclusion-transition); in a homogeneous mean-field case the realized prevalence fluctuates around that common probability at $`O_p(M^{-1/2})`$. Replacing the average of a nonlinear $`h_\kappa`$ by its value at average covariates is a separate closure approximation whose error depends on population heterogeneity, not on the opportunity count $`N_t`$. Speakers’ evidence states can mediate population change, while an analyst’s posterior remains only a measurement of that change. Counterfactual informativeness. When $`y_i`$ is an in-repertoire competitor, let

```math
D_{0,i}=e^{U_t(\bot;n,c)}+
  \sum_{x'\ne x}z_i(x',c)e^{U_t(x';n,c)}
```

be the gated normalizer when $`x`$ is unavailable, and define the occasion-level full-choice share

```math
\widetilde{\rho}_{i,t}^\star(x\mid n,c)=
  \frac{e^{U_t(x;n,c)}}{D_{0,i}+e^{U_t(x;n,c)}}.
```

Holding the other gates fixed, normalized softmax choice then gives the exact identity

```math
\frac{P(y_i\mid Z_x=1,n,c)}{P(y_i\mid Z_x=0,n,c)}
  =1-\widetilde{\rho}_{i,t}^\star(x\mid n,c),
```

and hence

```math
\ell_i(x)=-\log\!\bigl(1-\widetilde{\rho}_{i,t}^\star(x\mid n,c)\bigr)
  \approx \widetilde{\rho}_{i,t}^\star(x\mid n,c)
```

only when the target’s full gated mass is small. The common $`N_t\cdot\rho_t^\star`$ score is recovered as a small-mass information approximation in a near-complete gap and under four further conditions: nearly every opportunity is an attributable omission ($`r_i\approx1`$), the outside option has negligible mass, the other candidate gates match the norming task, and the target mass is small enough for the log expansion. Continued attributable competitor choices can keep supplying evidence against a concentrated gap; reopening it requires an actuation route that changes utilities, gates, or the observed likelihood.

When $`y_i`$ is the outside option–periphrasis or avoidance, available at fixed utility under both hypotheses–the same denominator identity applies. Its choice is nearly uninformative only when the target’s full counterfactual mass $`\widetilde{\rho}_{i,t}^\star`$ is small, which requires $`x`$’s utility to be low relative to the candidate set and the outside option. That condition is independently estimable from the same norming task. Then $`\ell_i(x)\approx0`$.

When candidate support is weak, the affine contrast lets periphrasis remain weak evidence against any one candidate. This separates the defective cell’s low-concentration state from the preempted gap’s high-concentration state (§[4.6](#sec:winnerless-cells), §[3.9](#sec:worked-examples)).

The repair stream: a candidate controller. The paper’s support claims come in grades: stabilization, maintenance, control (§[5](#sec:implications)). The transition and full map below specify candidate conditions for stabilization; showing that it or the proposed loop supports an actual linguistic profile requires longitudinal or intervention evidence. Control needs the stronger result that a process registers departures from the licensed profile and pushes the population back. Conversational repair is the candidate considered here.

Let $`\Delta(d)`$ be the expected common-ground divergence from mis-setting operator dimension $`d`$: the quantitative face of “update-configuring” in the working test of §[[sec:operator-values]](#sec:operator-values). Formally, $`\Delta(d)`$ is an expected KL divergence between the common-ground posterior induced by the intended value and the posterior induced by the mis-set value, in the same spirit as RSA-style update models . When a token mis-sets $`d`$, other-initiated repair occurs with probability $`r(\Delta,\iota)`$, increasing in $`\Delta`$ and modulated by footing $`\iota`$. A fit-ready model derives repair and production from the same latent inclusion state. Over a window with $`N_t(n,c)`$ opportunities, the repair-generated flow against a deviant convention in niche $`n`$ is

```math
\begin{equation}
\psi_{\mathrm{rep}}(n)=N_t(n,c)\cdot
P(\text{mis-set})\cdot r(\Delta,\iota),
\label{eq:repair-flow}
\end{equation}
```

whose magnitude is linear in opportunity and increases with divergence through $`r`$; it needn’t be linear in $`\Delta`$. This scalar is a candidate repair exposure, not yet a derived term in the likelihood-consistent filter.

The numerical results in §[4.4](#sec:emergent-categoricality) supply no evidence for the repair hypothesis; the companion software’s programmed repair comparison is only a diagnostic. Repair earns controller status under Woodward’s interventionist criterion if an intervention on it changes the profile’s return-to-attractor behaviour in an invariant, predictable way . Until then, repair remains a testable candidate controller.

Two commitments come with the term. First, the operator/style boundary becomes a parameter statement: policing intensity is predicted to follow $`N_t\,P(\text{mis-set})\,r(\Delta,\iota)`$, with opportunity estimable from opportunity-annotated corpora and $`\Delta`$ from comprehension probes or annotated update-divergence tasks that ask what common-ground change the mis-set value would induce. The §[[sec:operator-values]](#sec:operator-values) falsifier–a closed, high-opportunity, non-configuring contrast policed like grammar–has a quantitative form: such a contrast has $`\Delta\approx0`$, so its corrective flow collapses to a social-sanction baseline and its licensing distribution should stay gradient, policed like style. Second, if repair rates track social indexing rather than $`\Delta`$, the corrective term collapses into sociolinguistic policing and the controller claim fails cleanly. Blythe and Croft’s utterance-selection dynamics remain the $`r\equiv0`$ special case, so the import is conservative .

Grain asymmetry and compositional inheritance. The two kinds of evidence attach at different grains. Positive evidence distributes over activated nodes by the coverage weights: a heard token confirms every construction that covers it. Error and preemption mass instead concentrate on the most specific node that individuates the candidate within its niche, because that node is what distinctively predicts the missing tokens. In Bayesian terms, the likelihood penalty for structured non-occurrence falls on the hypothesis that wastes probability mass on sentence types never observed; likelihood is a quantitative measure of the weight of implicit negative evidence .

Compositional inheritance raises an objection. Token-level licensing is assembled from constructional nodes, so left-branch extraction activates the well-licensed nodes for interrogative fronting, question formation, and modifier–noun packaging. The sum can look as though it should hand the candidate substantial licensing.

The coverage weights block that result. A node contributes to a token’s pooled licensing only for the properties it actually sanctions, and those parent nodes sanction only _contiguous_ realizations. None of them covers the determiner–head discontinuity that defines *_Which did you buy car?_; producing that token requires a node that licenses a determiner–head arc crossing the verb, and no contiguity-preserving node in $`\mathcal{H}`$ generates one .

The parents keep their high licensing, each confirmed by its own abundant contiguous tokens, and contribute none of it to the discontinuous token through the pooling sum. The dedicated left-branch-extraction node, the only activated node that covers the discontinuity, carries near-gating weight for it. It absorbs preemption mass only to the extent that the missed opportunities are attributable to competitor choice, which is why the independent $`\widetilde{\rho}_t^\star`$ norming required in §[3.6](#sec:identification-c) is necessary for the assignment. This asymmetry also answers an acquisition worry. If token-level licensing were just pooled parent licensing, learners should pass through a stage of treating left-branch extraction as live. They don’t need to: the candidate is generated by analogy, so it’s on the table with non-zero prior support, but its dedicated node has no scaffolding of its own, fronting opportunities are dense in the input, and each one adds preemption mass.

A companion corpus study quantifies one side of the evidential situation: across 1,228 fronting opportunities in a sixteen-corpus Universal Dependencies sample, zero genuine determiner–head discontinuities occur (95% upper bound 0.24%), while contiguity-preserving alternatives (pied-piping, fused-head construals, and the _big mess_ family) occur at measurable rates . Comprehension pushes the same way: a fronted _whose_ or _which_ defaults to a fused-head parse, so the discontinuous analysis also loses the parsing race . What remains to be normed is $`\widetilde{\rho}_t^\star`$: if speakers would rarely choose the discontinuous form even under a permissive stipulation that English allowed it, the absence would support starvation rather than preemption. The predicted non-satiation of left-branch extraction remains a test; ’s () meta-analysis of satiation in extraction from islands supplies the closest current analogue, not a direct measurement of lbe itself.

Open-loop learning and closed-loop dynamics. The discrete update [[eq:beta-update]](#eq:beta-update) changes an evidence state in a fixed exogenous environment. Figure [4](#fig:posterior-means) shows the resulting evidential difference between sparse and dense attributable omissions. Population bifurcation requires the transition in [[eq:inclusion-transition]](#eq:inclusion-transition): inclusion gates production, production supplies later choice evidence, and speaker filters affect later adoption and retention.
## Conditional emergence of separated regimes
The sense of emergence used here is weak and mechanistic: population-level categoricality is a possible outcome of learner updating, adoption, and selection. This differs from Hopper’s “emergent grammar”, where grammar is perpetually provisional .

For a homogeneous focal candidate, let $`X_t=(\theta_t,a_t,b_t)`$ and let $`\mathcal M_{\theta_t}(a_t,b_t)=(a'_t,b'_t)`$ be the deterministic expected-window version of the discounted likelihood update in [[eq:affine-window-posterior]](#eq:affine-window-posterior). It uses the expected target and non-target counts implied by the gated-choice model and moment-matches the resulting power-likelihood posterior. The composed mean-field map is

```math
\begin{equation}
F(X_t)=\left(
(1-\lambda)\theta_t+\lambda h_\kappa(a'_t,b'_t),
a'_t,b'_t\right).
\label{eq:full-mean-field-map}
\end{equation}
```

This expected-window closure is a deterministic diagnostic of the finite-population stochastic process, whose transition kernel remains [[eq:inclusion-transition]](#eq:inclusion-transition). Fixed points satisfy $`F(X^\ast)=X^\ast`$; their local stability is governed by the full Jacobian,

```math
\begin{equation}
\rho\!\left(J_F(X^\ast)\right)<1,
\label{eq:full-map-stability}
\end{equation}
```

where $`\rho`$ is spectral radius. This criterion retains the slow evidence directions that a scalar population equation discards.

A reduced crossing plot remains useful for location. Holding $`\theta`$ fixed, let $`(a^\ast(\theta),b^\ast(\theta))`$ be the stationary evidence state and put

```math
H(\theta)=h_\kappa(a^\ast(\theta),b^\ast(\theta)).
```

Crossings of $`H(\theta)`$ and the diagonal locate candidate equilibria. They do not supply return times: the scalar derivative can differ sharply from the dominant eigenvalue of [[eq:full-map-stability]](#eq:full-map-stability) when evidence is slow. The unstable interior crossing is denoted $`\theta^\ddagger`$ below.

The numerical analysis uses a specified two-candidate cell: equal candidate utilities, outside utility $`-4`$, twelve opportunities per step, observation probability $`.6`$, memory $`.96`$, inclusion-update rate $`.08`$, a uniform Beta baseline, and $`q_\kappa=.5`$. Under the posterior-threshold response in [[eq:posterior-threshold-adoption]](#eq:posterior-threshold-adoption), the deterministic closure has stable fixed points effectively at $`0`$ and $`1`$ and an unstable crossing at $`\theta^\ddagger\approx .493`$. The corresponding spectral radii are $`.961`$, $`1.087`$, and $`.971`$. A logistic reduced form with slope $`8`$ has stable fixed points near $`.024`$ and $`.968`$ around an unstable crossing near $`.489`$; slope $`4`$ has only one stable interior fixed point. A proportional response likewise has one interior fixed point. Thus the independently specified adoption response supplies the nonlinearity.

Finite-population runs preserve that scope result. Across 36 seeded runs of 320 steps initialized at $`.1`$, $`.5`$, and $`.9`$, the posterior-threshold and slope-$`8`$ responses both passed the declared basin-separation and endpoint criteria; the proportional response didn’t. A dominant outside option ($`U(\bot)=5`$) produced weak evidence and no endpoint concentration. Moderate inclusion-only and evidence-state perturbations returned to both attracting regions. These runs establish existence and scope for the declared process. They provide neither an empirical fit nor a stationary-distribution result. The exact grid, seeds, approximation diagnostics, and artifact hash are archived with the companion software.

A cubic normal form,

```math
\begin{equation}
\dot{\theta}=\theta(1-\theta)(\alpha\theta-\beta)
\label{eq:cubic-normal-form}
\end{equation}
```

summarizes an endpoint-absorbing, large-concentration limit. Finite-concentration responses generally put their attracting points inside the unit interval, and the cubic omits the evidence-state eigenmodes; the full map carries the explanatory claim.

The convergence claim has to match both levels of the model. With perfect retention ($`\delta_m=1`$), an individual evidence filter is close to reinforcement processes of Pólya type, where stochastic approximation supplies relevant techniques . The signaling-game case, structurally the closest analogue, is treated directly by Argiento, Pemantle, Skyrms, and Volkov , with an extension by Hu, Skyrms, and Tarrès . Those results don’t establish convergence of the composed population transition in [[eq:inclusion-transition]](#eq:inclusion-transition); that requires a specified $`h_\kappa`$.

With bounded memory ($`\delta_m<1`$), the learner filters have constant gain, so the decreasing-gain analogues no longer prove almost-sure convergence even at that level. The population-level formal target is a stationary distribution for the composed transition concentrated near the full map’s attracting regions, with escape times and residual dispersion set by opportunity, persistence, and memory: high-$`N`$ contrasts should sit tightly near the extremes, while low-$`N`$ or outside-option-dominated contrasts remain diffuse. That claim is a proof obligation rather than a theorem here.

The operator-specific prediction also needs its scope stated. Neither the full map nor its cubic limit derives the operator/style boundary. The OVMG claim is conditional: adoption criteria and selection intensity have to vary with independently estimated switching or coordination costs, opportunity, and update divergence. Under that condition, dense, update-configuring contrasts should concentrate fastest, while low-$`\Delta`$ contrasts remain more gradient and are policed like style. If a closed, dense, non-configuring contrast shows the same licensing and repair profile, the operator-specific part of the account fails.

Bounded memory adds a quantitative residual: even near an attractor, dispersion should scale with opportunity and forgetting, roughly with the effective concentration supplied by the discounted evidence filter.

Sampling drift near the extremes makes the boundaries sticky in finite populations, while middle states stay vulnerable to renewed evidence. The same escape-time logic connects winnerless-cell metastability (§[4.6](#sec:winnerless-cells)) and actuation (§[4.8](#sec:actuation)): a state can persist for long periods and then move quickly once the observation likelihood or outside-option utility changes. This connects the dynamics to complex-adaptive and cultural-evolutionary accounts of language change , and to invisible-hand explanations, where macro-level order emerges as the unintended consequence of micro-level choices .
## Derived obligatoriness
The state theory defines saturation relative to the obligatory dimensions $`\mathrm{OBL}_t(n,c,A)`$ (§[3.2](#sec:objects)), where $`n=n(A,c)`$ is the registered at-issue niche. Those dimensions are path-dependent population properties, estimated separately by an analyst. Let $`\mathcal{A}_0(d,n,\phi,c)`$ be the finite, independently fixed class of defined assemblies of frame type $`\phi`$ that realize niche $`n`$ while leaving $`d`$ unset. For $`A`$ in that class, define the population’s raw zero-marking rate

```math
R_s^0(A,n,c)=P_j\!\left(\text{speaker $j$ realizes a $d$-at-issue opportunity
in $(n,c)$ with $A$ at $s$}\right).
```

This realized population statistic is distinct from the licensing predicate $`L_s`$ and from a status estimate. The same simple-present nodes can have high licensing in a habitual niche while their zero-marked realization rate is near zero in an ongoing-at-issue niche. General node availability, niche-specific zero marking, and saturation remain separate quantities.

Let $`W_t=[t-W,t)`$ be a preceding convention-individuating window, and let $`\Pi_{W_t}(A,d,n,c)`$ be the realized pressure against $`A`$ there: $`d`$-at-issue opportunities in which a marked competitor wins, weighted by the independently normed full-choice share $`\widetilde\rho^\star`$. This weight is ungated; it doesn’t use $`\operatorname{sat}_s`$ or $`\mathrm{OBL}_s`$. Outside-option choices don’t contribute. Write $`E_t(d,n,\phi,c)`$ for the entry condition that, for every $`A\in\mathcal A_0(d,n,\phi,c)`$,

```math
\sup_{s\in W_t}R_s^0(A,n,c)<\epsilon_0
\qquad\text{and}\qquad
\Pi_{W_t}(A,d,n,c)\geq\pi_0.
```

Write $`X_t(d,n,\phi,c)`$ for the release condition that, for some such $`A`$,

```math
\inf_{s\in W_t}R_s^0(A,n,c)>\epsilon_1
\qquad\text{or}\qquad
\Pi_{W_t}(A,d,n,c)\leq\pi_1,
```

where $`\epsilon_1>\epsilon_0`$ and $`\pi_1<\pi_0`$. Given an initial convention state $`\mathrm{OBL}_{t_0}`$ fixed independently of the target interval, the path-dependent macro is

```math
d\in\mathrm{OBL}_t(n,c,\phi)
\quad\Longleftrightarrow\quad
E_t(d,n,\phi,c)\ \lor\
\bigl[d\in\mathrm{OBL}_{t-1}(n,c,\phi)\land
\neg X_t(d,n,\phi,c)\bigr].
```

The entry clauses say that every zero-marking realization has persistently disappeared under dense, attributable competition rather than because the niche was starved or an outside option absorbed a winnerless cell. The release clauses require sustained recovery or a clear pressure lapse. The two pairs of thresholds leave a hysteresis band in which the preceding state persists. The timescale and thresholds are community-indexed model parameters fixed independently of the contrast being classified. The initial condition and strict temporal descent make the recursion well founded: realized outputs and ungated pressure in $`W_t`$, together with $`\mathrm{OBL}_{t-1}`$, determine $`\mathrm{OBL}_t`$; $`\mathrm{OBL}_t`$ determines $`\operatorname{sat}_t`$; and saturation then enters $`S_t^\theta`$. This makes status a functional of the recent population history, not just of instantaneous $`\boldsymbol{\theta}_t`$.

An analyst identifies $`d`$ as obligatory when the posterior upper bound for every relevant $`R_s^0(A,n,c)`$ lies below $`\epsilon_0`$, the estimated pressure clears $`\pi_0`$, and the effective evidence meets a preregistered $`\nu_{\min}`$. Those conditions warrant an inference about the population property $`\mathrm{OBL}_t`$. Identification of release analogously requires posterior evidence for $`X_t`$ across the registered window.

The proposed mechanism is the population transition plus preemption applied to zero-marking. In a $`d`$-at-issue niche, marked and unmarked assemblies compete; where the marked assembly repeatedly wins, speakers’ filters and later inclusion states can drive the raw zero-marking rate down. The full map shows one possible phase portrait for that process, while the stationary-distribution claim remains a proof obligation rather than part of the definition of obligatoriness.

The typological payoff is that §[[sec:community-values]](#sec:community-values)’s descriptions convert to predictions. On the proposed diagnosis, English progressive marking is obligatory because simple-present assemblies in ongoing-at-issue niches have persistently low raw zero-marking rates under a winning marked competitor; French zero-marking there hasn’t, so the dimension stays optional, and _Elle étudie maintenant_ is fine. Turkish evidential marking is the same kind of hypothesis on a different dimension. Grammaticalization’s obligatorification receives a candidate mechanism: a contrast on its way to obligatory status is one whose zero-marking competitor is losing dense niches one at a time, which predicts an intermediate stage–obligatory in some frame types and niches, optional in others–that grammaticalization corpora are positioned to test.
## Winnerless cells
Preempted gaps have a winning competitor. Defective paradigm cells don’t, and the dynamics explain how the difference can be stable rather than transitional.

Suppose candidates $`f_1,\dots,f_m`$ for a dense cell have weak analogical support, the outside option (periphrasis, avoidance) has moderate fixed utility, and producing a weakly licensed form carries a face cost. Then the production rule routes the cell’s opportunities to the outside option: no candidate accumulates positive evidence. The omission likelihood matters here: outside-option choices have $`\ell_i(x)\approx0`$, so no candidate accumulates much negative evidence either. Evidence starvation alone preserves the prior. The low-mean/low-concentration profile requires an additional independently motivated ingredient–low priors for unsupported analogical candidates, weak diffuse negative evidence, a hierarchical prior over defective cells, or a latent cell-level state such as “no candidate is established”. Given such an ingredient, avoidance keeps every candidate at low mean and low concentration, because escaping the state requires some candidate to accumulate positive evidence that the outside option keeps starving it of.

The claim has two strengths. The winnerless-cell example in §[3.9](#sec:worked-examples) relies on the qualitative mechanism: an avoidance attractor plus evidence starvation, with low prior support or weak diffuse negative evidence supplying the low mean. The stronger metastability claim, persistence for times exponential in population size, remains a conjecture with analogues in evolutionary dynamics. ’s () point that the maintenance mixture varies across cases–structural uncertainty, lexical restriction, learning dynamics, avoidance–is compatible with this narrower claim: the model supplies the avoidance-and-starvation component and is agnostic about the rest of the mixture.

The phenomenological contrast is represented by the resulting evidence profile. Clean defective cells (_pobedit’_ 1sg, with *_amn’t_ depending on niche granularity) show low mean with low concentration–“I don’t know how to say it”–where preempted gaps show low mean with high concentration–“that’s impossible”. Same mean, different concentration, different feeling, read out by $`\Phi`$ (§[3.7](#sec:feeling-new)). The satiation-framing prediction follows: defective cells should behave like low-evidence forms, movable under framing; preempted gaps shouldn’t .
## Destabilization of moribund contrasts
Bounded memory yields one more result. With discount $`\delta_m<1`$, the equilibrium concentration of a node’s posterior is set by the balance of evidence inflow against forgetting: $`\nu^{\ast}\approx\nu_0+O\bigl(N/(1-\delta_m)\bigr)`$, with $`N`$ the per-window opportunity count for the node’s niches and $`\nu_0=a^0+b^0`$ the baseline concentration. If opportunity falls–a case distinction going moribund, a niche drying up–equilibrium concentration falls toward the baseline. With no further evidence, means drift toward the baseline prior under [[eq:beta-update]](#eq:beta-update); with sparse, idiosyncratic evidence, individual histories can diverge. Falling excess concentration is the direct consequence and the primary preregistrable precursor; increasing test–retest instability is a behavioral proxy only if it is independently validated against concentration.

Prior heterogeneity alone doesn’t make dispersion lead the mean. If, after a shared evidence stream disappears,

```math
C_{i,t}=w_t m_i+(1-w_t)C_E,
```

where $`m_i`$ is speaker $`i`$’s baseline-prior mean, $`C_E`$ is the former common evidence mean, and $`w_t`$ rises toward one, movement of the population mean is linear in $`w_t`$ while between-speaker variance is $`w_t^2\operatorname{Var}(m_i)`$. On a common fraction-of-eventual-change scale, dispersion lags. The companion simulation reproduces this ordering at both 25% and 50% progress. Dispersion-leading decline remains a conditional hypothesis requiring a faster heterogeneity source, such as cohort replacement, unequal network opportunity loss, heterogeneous retention, or a specified judgment mapping.
## Actuation
In a bistable cell of the full map, actuation is movement of the coupled population-and-evidence state across the basin boundary whose population coordinate is $`\theta^\ddagger`$. A utility change, new target evidence, altered outside-option mass, or a social change in $`q_\kappa`$ can move the state across that boundary. Speakers’ filters then alter adoption and retention through [[eq:inclusion-transition]](#eq:inclusion-transition). An analyst posterior should track the population movement with a lag; motion in its mean isn’t itself actuation. No S-shaped time course follows without specifying the full perturbation and the slow evidence state.

The factors that drive such bifurcations align with the motivations discussed in §[[sec:motivations]](#sec:motivations). Semantic reanalysis may increase utility (and thus $`\widetilde{\rho}_t^\star`$) by making a form–value relation easier to interpret or more useful. Social pressures may shift utilities (prestige effects) or alter the relevant community standard. Structural motivations such as analogical extension can systematically raise licensing probability by borrowing strength from frequent neighbors. Processing innovations may reduce error rates ($`e_t`$) or locality costs, changing either the observation likelihood or later adoption.

Individual innovation is insufficient. A few speakers adopting a marginal construction don’t guarantee its success; the likelihood and transition have to shift so that inclusion is systematically favoured across the relevant community. Many sensible innovations fail because they appear before those community conditions are in place.

Near the separatrix, small perturbations in community attitudes can trigger rapid shifts between exclusion and licensing. As the state moves further past $`\theta^\ddagger`$, reversal becomes increasingly unlikely. The full map can represent the S-curves documented in some language changes . For constructions in the marginal zone, with the population state near $`\theta^\ddagger`$, the model predicts heightened sensitivity to external factors and greater cross-community variation. Small or peripheral communities may show volatile behaviour near bifurcation points before a change spreads to larger population centres.

The destabilization result sharpens the actuation picture at the other end of a form’s life. Actuation is crossing a separatrix; destabilization is a collapse in concentration. A contrast can lose its grip when evidence of any kind stops arriving, without accumulating negative evidence; the model predicts the two routes are empirically distinguishable: actuation crosses a basin boundary in the coupled state; moribundity first removes evidence confidence and need not cross that boundary until later population turnover. Judgment dispersion may lead only under the additional heterogeneity mechanisms named above.
## Apparent exclusions from concentrated non-licensing
When a defined, saturated assembly exists but its pivotal node’s licensing posterior is driven toward zero and concentrates there under persistent preemption in a dense opportunity set, speakers converge on a sharp, non-satiating rejection profile. Additional processing penalties in $`R_i(u,c)`$ (e.g.  systematic garden-path repair due to an entrenched fused-head construal) can strengthen the subjective categoricality without any independent structural constraint being posited.
# Theoretical implications
OVMG’s decomposition of grammaticality determines what the category should let us expect. If a form–value relation is grammatical in a communicative situation, it should pattern with other licensed resources in repair behaviour, transmission, satiation under exposure, and trajectories of change. If it’s unlicensed, weakly licensed, or backed by little evidence, those expectations should fail in different, diagnostic ways (§[[sec:projectible-G]](#sec:projectible-G)).

In this sense, the account is projectibility-first: grammaticality earns theoretical standing by the inferences it supports, not by the mere fact that a mechanism can be named for it . The profile proposed to support those inferences is conditioned form–value stability. The state architecture yields projective tests and distinguishes three world-side support hypotheses. The full map represents conditional sufficient conditions for stabilization. The production–repair loop is a candidate maintainer whose removal effect needs longitudinal or intervention evidence. Repair is also a candidate controller only if it registers departures from the licensed profile and pushes the community back toward it. That stronger claim depends on the intervention signature in §[[sec:repair-controller]](#sec:repair-controller) .

This recasts the competence–performance relation. Licensing and feeling are coupled layers, not a competence core plus performance noise: processing and other performance factors help shape which form–value relations stabilize, and those stable relations in turn constrain performance. Their evidence streams remain separate. The identification strategy in §[3.6](#sec:identification-c) keeps this from becoming a catch-all, since licensing, anomaly, and confidence are measured by different evidence streams and can falsify each other. The rest of this section develops the consequences: the account’s reading of macro-typological universals, its distinctive predictions, and its relation to neighbouring frameworks.
## Macro-typological constraints on grammatical design
Recent macro-typological work sharpens the question of how strongly grammar is constrained across languages. test 191 implicational universals from the Universals Archive against Grambank’s 2,430-language morphosyntactic sample, using Bayesian models that control explicitly for genealogical and areal non-independence and then follow up with spatiophylogenetic analyses of evolutionary rates.

A naïve analysis that ignores relatedness appears to support the vast majority of proposed universals, but once phylogeny and geography are accounted for, only about a third (60 of 191) remain statistically supported. Support is concentrated in relatively narrow domains: most hierarchical universals and a substantial minority of “narrow” word-order universals survive, whereas “broad” word-order universals and miscellaneous others fare poorly. Diachronically, supported universals typically correspond to “harmonic” combinations of features (for instance, consistent head–dependent orders) that languages are more likely to evolve into than out of, with these preferred configurations recurring independently across lineages.

From an OVMG perspective, these findings identify candidate attractors in the design space of operator-valued form–value relations rather than exceptionless grammatical laws. They don’t by themselves show that a macro-typological feature is a language-internal grammatical object. The typological claim has to pass through a comparandum-to-realization mapping, which requires specifying the comparative feature is being tracked, how each language realizes the relevant operator value or form–value relation, and whether the resulting profile predicts held-out languages or diachronic trajectories .

Under that discipline, supported patterns correspond to configurations for which the choice likelihood and independently specified adoption response in §[4.3](#sec:update) favour inclusion across a wide range of communities. They’re cognitively and communicatively favourable enough that repeated episodes of change tend to push the population licensing rate $`\theta_t(\kappa,c)`$ toward an attracting region in lineage after lineage.

The fact that roughly two-thirds of the tested universals fail once autocorrelation is controlled for also fits a de-idealized view of grammaticality. Community-specific conventions still have considerable freedom in how they realize operator values, with only some regions of the space strongly preferred. Large-scale comparative work of this kind complements OVMG by locating candidate stable regions; OVMG explains how local community dynamics and operator compatibility can make those regions reachable and persistent.
## Predictions
The model’s distinctive predictions come from separating positive evidence, opportunity structure, counterfactual choice probability, posterior concentration, and repair flow. Cross-linguistic gender remains a useful boundary case, but it isn’t the strongest test. Any framework that treats grammaticalized concord as obligatory predicts stronger judgments where concord is more tightly grammaticalized. The companion operator-stratum account also complicates the simple gender story: gender concord can be policed through paradigm inertia even when its public-update value is attenuated . The sharper predictions concern concentration contrasts, zero-evidence learning, L2 transfer, moribundity, repair policing, and change by re-licensing.

Satiation framing, as a rank order. Framing manipulations are prior shifts, and a prior shift moves a posterior in proportion to $`1/\nu`$–the inverse of its concentration. The prediction is ordinal across construction types, once $`\widetilde{\rho}_t^\star`$ has identified the relevant niche: confirmed preempted gaps $`\approx`$ *_sheeps_ (nil) $`<`$ entrenched-but-uncommon constructions $`<`$ independent relative _whose_ $`\approx`$ clean winnerless cells such as _pobedit’_ 1sg (largest). Participants told that tokens of a low-concentration form come from an intentional dialectal, literary, or ingroup resource should show more improvement than participants told the same tokens are errors; the same manipulation should leave a confirmed preempted gap unmoved. ’s () meta-analysis of syntactic satiation in extraction from islands supplies a nearby benchmark for extraction phenomena, not a direct measurement of left-branch extraction. The dependent variables are rating change, evidence-confidence change ($`\Phi^{\mathrm{ev}}`$), decision-confidence change ($`\Phi^{\mathrm{dec}}`$), later repair behaviour, and elicited production.

Artificial-language learning. An artificial-language-learning experiment can hold positive evidence constant at zero while manipulating opportunity-set size. Learners could see a system in which a target candidate is never produced. In the high-opportunity condition, competitor candidates repeatedly occupy the relevant niche and the target has high $`\widetilde{\rho}_t^\star`$; in the low-opportunity condition, the niche rarely arises or the target would have low counterfactual utility. OVMG predicts categorical rejection in the first condition and uncertainty in the second, even though both conditions contain identical zero positive evidence. The design operationalizes the Figure [4](#fig:posterior-means) contrast and is compatible with artificial-language learning paradigms that manipulate simplicity and communicative structure .

L2 preemption transfer. Early L2 rejections should track L1 preemption mass, not just L2 frequency. A learner whose L1 strongly preempts a candidate in a high-opportunity niche should reject the L2 analogue early, even if the L2 input frequency is low enough to leave native speakers uncertain. Conversely, low L1 preemption should make learners more willing to treat rare L2 patterns as unresolved rather than impossible. As learners join the L2 speech community, $`q_h(c\mid e)`$ and the constructional hierarchy should shift toward the target norm-centre. This view aligns with ’s () concept of interlanguage, but gives a more specific prediction: transfer is strongest where the L1 has accumulated many attributable, counterfactually informative omissions.

Concentration loss before categorical decline. For a contrast going moribund, the direct destabilization result (§[4.7](#sec:destabilization)) is loss of excess evidence concentration as opportunities thin. Longitudinal designs should measure confidence, test–retest stability, and sensitivity to controlled exposure alongside means and production. A reliable drop in those concentration-sensitive measures while the population rate remains approximately stable would support the proposed precursor. Inter-speaker judgment dispersion is a separate, conditional target: prior heterogeneity by itself makes normalized dispersion lag the mean, so a dispersion-leading result should be predicted only when cohort replacement, unequal network opportunity loss, heterogeneous retention, or a specified judgment mapping supplies faster divergence.

Soft alternations as a non-bimodal control. The conditional dynamics (§[4.4](#sec:emergent-categoricality)) predict separated licensing only where the observation process and independently motivated adoption costs support it; a both-licensed alternation should stay unimodal, its variation carried entirely by selection $`\rho_t^\star`$ when the outside option is negligible (and by $`\widetilde\rho_t^\star`$ otherwise). The dative is the worked case (§[5.5](#sec:usage-based)): a corpus production model is well calibrated on the recipient choice within its high-frequency core, the graded, single-peaked signature OVMG predicts when $`S_t^\theta\approx1`$ for both variants. The alternation is non-categorical through optionality, not the uncertainty of a winnerless cell (§[4.6](#sec:winnerless-cells)): the niche is common and both variants are licensed, so judgments should be confident and gradient rather than ineffable. An account that reads categoricality off structural membership predicts the opposite.

Policing intensity as a parameter. The repair stream (§[[sec:repair-controller]](#sec:repair-controller)) converts the operator/style boundary from a classification into a regression: policing intensity should follow $`N_t\,P(\text{mis-set})\,r(\Delta,\iota)`$, increasing with niche opportunity and update divergence conditional on the other factors. Opportunity and divergence are independently estimable–the first from opportunity-annotated corpora, divergence from comprehension probes or annotated update-divergence tasks fixed before the repair data is inspected. The §[[sec:operator-values]](#sec:operator-values) falsifier becomes quantitative: a closed, dense, non-configuring contrast has $`\Delta\approx0`$ and should show style-like policing–a social-sanction baseline with gradient, unimodal licensing regardless of frequency. If repair rates track social indexing rather than $`\Delta`$, the corrective term collapses into sociolinguistic policing and the controller claim fails.

Change by re-licensing. Hard unification makes a commitment that a weighted-penalty model doesn’t: no amount of entrenchment can make the same clashing operator assignment grammatical. Apparent change in cases like *_I’ve finished it yesterday_ should come either from read-out effects or from re-licensing. Where present-perfect combinations with definite past-time adverbials are attested in a community , change has to proceed by _re-licensing_: a perfect construction with a different operator contribution enters the repertoire, potentially producing judgment distributions that are bimodal across communities and categorical within speakers, not gradual within-speaker reduction in the status cost of the original clash. A soft-constraint model predicts the opposite signature. Judgment-distribution data from the relevant contact varieties decides it.

This contrasts with preempted gaps. A preempted gap can re-open when changed utilities, opportunities, or target evidence move the coupled state across its basin boundary: the pivotal node’s mean then rises through the middle, producing within-speaker gradience during the transition and potentially a community S-curve. Compatibility failures can’t re-open that way; they require a distinct construction with a different $`\omega`$. The identification discipline is the same as elsewhere: the re-licensed construction has to be diagnosed before the judgment data is used, for example by showing that it supports other definite past-time adverbials, scope interactions, or ellipsis patterns predicted by the new operator contribution.

Intonational operators. Nothing in the model privileges segmental material, so intonational patterns are predicted to count as operator exponents wherever they form closed, high-opportunity, update-critical repertoires: the English polar-question rise and nuclear-accent placement configure what an utterance does to the common ground much as tense and agreement do . The Turkish suffix-harmony analysis in Appendix [8](#app:turkish-harmony) gives the parallel case for segmental exponent choice: phonological material matters for grammaticality when it realizes an operator exponent. The corresponding intonational test is whether mismatches between intonation and text (e.g.  nuclear accent on a closed-class word under broad focus) are policed like grammar, with categorical rejection, repair, and resistance to framing, or like style.
## Relationship to generative grammar
Generative work made a central contribution by showing that grammaticality can’t be reduced to semantic plausibility, processing ease, or frequency of attestation. Chomsky’s _Colorless green ideas sleep furiously_ made the contrast visible: speakers can recognize syntactically well-formed sentences even when they’re semantically bizarre. Generative analyses explain apparent categorical exclusions like the determiner–head discontinuity in English left-branch extraction (*_Which did you buy car?_), and they capture the fact that such sequences remain unacceptable even when their intended meaning is clear and processing demands are low.

OVMG retains the lesson. Judgments reflect systematic patterns ; those patterns can’t be reduced to meaning or processing alone; and certain syntactic configurations appear to be excluded regardless of context. The earlier diagnostics for center embeddings and preempted gaps build on ideas about recursive structure and acknowledge the generative discovery that some exclusions are systematic. They relocate the explanation in coverage, hard compatibility, saturation, and concentrated exclusion.

The same point governs the account’s use of formal evidence. A generative analysis can supply a real warrant when it specifies the target, diagnostics, evidence, and failure conditions for a grammatical contrast. OVMG isn’t an attempt to replace every I-language analysis; it rejects only the stronger claim that categorical grammaticality must be explained by an autonomous syntactic component or a UG-backed inventory of primitives. Its target is the community-level licensing profile that makes some form–value relations categorically policed.

One well-known case is independent relative _whose_ ([[ex:whose]](#ex:whose)). As observe, the construction appears to violate no syntactic principles: independent genitives are possible (_Mine was visiting_), independent interrogative _whose_ is grammatical (_Whose was open?_), and _whose_ can be used as a dependent relative pronoun (_the student whose friend was visiting_). The generative tradition’s careful documentation of such cases, where seemingly parallel constructions show puzzlingly different grammatical status, has driven theoretical development.

OVMG explains the contrast differently. Rather than positing an autonomous syntactic component, it treats grammatical constraints as products of form–value relations within specific communicative situations. For independent relative _whose_ to be felicitous, multiple conditions have to converge: the possessor has to be sufficiently accessible in the discourse while the possessum is predictable enough to license ellipsis, but the possessive relationship needs to be semantically significant enough to warrant explicit marking, and this configuration has to occur in a context where a relative clause is the natural way to package this information.

The relevant niche is tiny. Speakers encounter the construction so rarely, despite perfectly common components, that the licensing posterior remains diffuse; even when all conditions align, the construction feels alien because the evidence is thin, not because the community has accumulated confident negative evidence against it.

The difference is evidential rather than merely terminological. A generative theory has to explain why a syntactically possible and pragmatically useful construction remains marginal. OVMG predicts the profile of that marginality: low concentration, framing sensitivity, and weak confidence, not the non-satiating rejection profile of a preempted gap. The result preserves the generative recognition of systematic constraints while embedding it in a theory of how form–value relations become established and maintained in language communities.

Other cases that generative grammar struggles to explain are grammatical with one meaning but ungrammatical with another, such as _have_+numeral years. While syntactically identical to grammatical expressions like _I have 25 dollars_, this construction becomes ungrammatical specifically when used to express age. A purely syntactic account would have to explain why the same structure is well-formed in one case but ill-formed in another, despite no apparent syntactic differences.

OVMG, in contrast, locates the source of ungrammaticality in the community’s form–value conventions: _have_+numeral years is licensed for duration or future time (_I have 16 years until retirement_), but the age-predication use is driven toward zero in English by dense competition with the _be_+age frame (_I am 16 years old_). Similar cases arise with plural forms that are grammatical with some meanings but not others (e.g.  _peoples_ for ethnic groups but not multiple individuals) and with verbs that resist certain arguments despite no obvious syntactic prohibition (e.g.  _discuss about_). These meaning-dependent grammaticality patterns suggest that licensing is keyed to specific form–value associations rather than purely structural templates.
## Relationship to Construction Grammar
Construction Grammar (CxG) made a central contribution by treating learned form–meaning pairings as grammatical objects. At its core, CxG argues that language consists of learned relationships between form and meaning at multiple levels of complexity. These form–value relations, or constructions, include both individual morphemes and abstract syntactic patterns. This perspective helps explain phenomena that proved challenging for earlier approaches, including idiomatic and partially schematic expressions that don’t fit a clean core/periphery split.

CxG shows that meaning suffuses all levels of grammatical organization. Rather than treating syntax as an autonomous formal system that interfaces with semantics only at designated points, CxG reveals how meaning and form are inseparable aspects of linguistic knowledge. For instance, the _What’s X doing Y?_ construction carries an implication of incongruity that can’t be derived from its component parts . Recent work connects this framework to model-internal analysis: use construction grammar to probe how neural language models handle different levels of linguistic abstraction.

OVMG shares these CxG commitments about form–value relations and constructional abstraction. It doesn’t privilege one expressive substance over another. The companion operator-stratum paper explicitly denies a substance-based boundary: phonological, gestural, lexical, morphological, and syntactic material can all realize operator contrasts when they enter a closed, accountable public-update repertoire . The OVMG claim is narrower. Categorical grammaticality clusters around form–value relations with a particular role: high-opportunity, closed-paradigm contrasts that configure update, role allocation, scope, reference, or repair.

The contrast becomes clear when speakers judge violations. Register, politeness, genre, and many lexical choices can be stable and socially important without blocking the public update itself. A wrong tense, agreement value, or clause-linking marker can mis-set the update instruction; a wrong obligatory allomorph can instead fail as an unlicensed exponent choice for a closed operator. The age-predication example (_I have 25 years_) has a readily recoverable intended meaning but not licensed for that English frame; its rejection comes from non-licensing in a high-opportunity constructional niche, not from the substance of syntax or morphology as such.

OVMG preserves CxG’s systematic treatment of constructions while adding a prediction about which constructional contrasts attract categorical policing. The relevant contrasts are those whose closure, opportunity structure, and independently motivated adoption costs place the licensing state in a separated regime of §[4.4](#sec:emergent-categoricality). That lets CxG’s continuum of constructions coexist with a non-arbitrary explanation of why some violations are heard as grammar and others as style, stance, or appropriateness.
## Relationship to usage-based approaches
OVMG shares with usage-based approaches (UBA) the idea that linguistic knowledge develops from patterns of actual language use rather than from an autonomous formal system. Both perspectives reject the notion that grammaticality can be reduced to abstract rules operating independently of meaning and context.

Several pieces of the formal core come directly from this tradition. The speaker/population split restates ’s () separation of entrenchment, the cognitive reorganization of a speaker’s knowledge, from conventionalization, the social establishment of a community’s regularities. Here $`z_{j,t}(\kappa,c)`$ gives speaker-level inclusion states, and $`\theta_t(\kappa,c)`$ gives the population licensing rate; a speaker or analyst tracks it with a distinct posterior mean. The proposed population transition is motivated by ’s () utterance-selection theory, in which variants are replicated and selected within a community; S-curve patterns of change are already worked out in that lineage .

Frequency per opportunity is likewise not new: it’s the core of ’s () case that corpora contain negative evidence, where a form counts as “significantly absent” rather than “accidentally absent” only once its observed frequency is weighed against the frequency expected given its opportunities. Variationist sociolinguistics has normalized by opportunity since Labov’s principle of accountability .

OVMG adds their joint formalization and a prediction. The licensing-versus-selection factorization $`\pi_t\approx S_t^\theta\cdot\widetilde{\rho}_t^\star`$–or $`\theta_t(\kappa,c)\cdot\widetilde{\rho}_t^\star`$ in single-pivotal-node cases–turns Croft’s replication-versus-selection into an estimable product. For an attributable omission, the affine contrast $`d_i=r_i(1-e^{-\ell_i})`$ is approximately $`r_i\widetilde{\rho}_t^\star`$ when the target is nearly always omitted, niche identification is nearly certain, the outside option is negligible, the other gates are stable, and the target’s full choice mass is small in the competitor regime, putting a quantity on the absence that left open, since he showed how to establish that a form is significantly absent but stressed that significant absence “does not, in itself, provide any clues as to why”. Licensing-versus-selection is exactly that missing clue: a significantly absent form may be unlicensed ($`S_t^\theta\approx0`$, or pivotal $`\theta_t\approx0`$) or licensed but dispreferred ($`\widetilde{\rho}_t^\star\approx0`$), and the two project differently.

The speaker-level Beta approximations feed the adoption–retention transition, whose population drift the full mean-field map represents (§[4.4](#sec:emergent-categoricality)). The relation to ’s () coverage and statistical preemption is one of formalization in the same spirit: her “explain me this” puzzle (a high-coverage double-object frame preempted by the prepositional dative) is a preemption-mass story in which the competitor wins a high-opportunity niche.

The dative alternation gives the licensing-versus-selection factorization its cleanest empirical case, because both variants are licensed and the whole contrast lives in selection. model the choice between _give Kim the book_ and _give the book to Kim_; a frozen version of such a model can be rescored on later British conversation in the Spoken BNC2014 to estimate $`\rho_t^\star`$ directly. Because both realizations are grammatical ($`G_t\approx1`$ for each), nothing in the corpus probability bears on $`G_t`$: it estimates the probability of an NP recipient conditional on a token that has already entered the annotated alternation sample, a conditional production probability rather than a probability of grammaticality. The released rows fix realization inside that annotated frame, the innermost of a set of nested opportunity sets; the broader licensing set is a different denominator, and reaching it is a step to a new target rather than a larger sample of the same one.

The conditioning that transports is projectible in Goodman’s sense : length, animacy, definiteness, and pronominality carry across varieties, while verb base rates travel worse, and even the transportable relations run overconfident out of domain (a recalibration slope near $`0.73`$). A relation can be projectible and still project poorly under a population shift, which is just $`\rho_t^\star`$ being variety-relative.

The both-licensed case complements the preempted double-object gap above: on the same construction, the factorization separates a cell where an entrenched competitor wins a large opportunity set ($`G_t\approx0`$) from a fully optional contrast where selection is the whole story, and a corpus production model measures the second without licensing a reading of the first. What a production model can’t do is diagnose such a cell on its own: from inside the annotated frame, an unlicensed gap and a merely dispreferred one look alike, and telling them apart needs evidence of another kind, not more tokens of the same sampling design.

One caution follows from , who find that overall form frequency (entrenchment) predicts the retreat from overgeneralization more robustly than competitor frequency (preemption), and who propose collapsing the two into a single competition process. OVMG keeps them analytically separate as direct error observations and counterfactual choice observations. They have to enter a shared likelihood rather than being added as interchangeable Beta failure counts (§[4.3](#sec:update)). Whether one latent competition process accounts for both remains an empirical question rather than a stipulation.

The analysis of independent relative _whose_, as in ?_I saw Joan, a friend of whose was visiting_, is a case in point. A simple UBA account might predict that this construction’s marginality stems from its low frequency. But this explanation proves insufficient: the construction is rare, and it’s dramatically rarer than one would expect given the frequency of its component parts. Independent _whose_ appears in interrogatives (_Whose is that?_), and the relative _whose_ is common in dependent contexts (_the student whose paper was late_). Given these frequencies, analogical extension should make the independent relative more common than observed.

Raw component frequency is the wrong predictor; _whose_ isn’t a preempted gap. The frequency of independent and relative _whose_ taken separately doesn’t create opportunities for the niche that requires both at once, together with an accessible possessor, a predictable possessum, and a licensing ellipsis site; that convergence is vanishingly rare. This isn’t the significant absence of a preempted form, which needs a large opportunity set and a competitor that keeps winning; it’s the low-opportunity uncertainty described in the diagnostic categories above. The tension between “rarer than expected” and “uncertain rather than rejected” dissolves once licensing is separated from selection: _whose_ is under-_observed_ because its niche rarely arises, not preempted because a rival repeatedly beats it.

OVMG doesn’t exempt the operator stratum from usage dynamics; it makes those dynamics more specific. A rare form can remain grammatical when the opportunity set is tiny or when higher-grain constructions license the token by compositional inheritance. A readily interpretable candidate can become categorically rejected when the opportunity set is large, the analogical candidate would have had high $`\widetilde{\rho}_t^\star`$, and an entrenched competitor wins every time. The result preserves usage-based findings about frequency and entrenchment while predicting when frequency becomes preemption.
## Relationship to logicality of language accounts
An alternative perspective, prominent in recent formal semantics, suggests certain types of unacceptability stem from the language faculty itself possessing a deductive system that identifies and filters sentences with logically trivial meanings (tautologies or contradictions) . This “logicality of language” hypothesis attempts to explain, for example, systematic restrictions on quantifiers by arguing the unacceptable cases are “L-trivial”, meaning their triviality arises solely from the meaning and configuration of logical or closed-class terms (like _every_, _some_, _not_), irrespective of the open-class words (like _student_, _run_) .

A key challenge is explaining why simple tautologies or contradictions (e.g.  _It’s raining and it isn’t raining_) are often acceptable. argues against “Logical Skeletons” (which assume the system ignores open-class word identity) in favour of “LF+RESCALE”, a view where the system sees standard logical forms but allows optional, context-dependent modulation of open-class terms (e.g.  interpreting the second “raining” as “raining hard”) to yield non-trivial meanings.

OVMG offers a broader account of ungrammaticality. “Logicality” approaches explain restrictions tied to logical and closed-class vocabulary through L-triviality. OVMG also covers cases less easily reducible to logical contradiction, such as absent form–value relations ([[ex:nonsense]](#ex:nonsense)), strong deviations from conventional community forms ([[ex:sheeps-entrench]](#ex:sheeps-entrench)), and extreme, unexpected rarity ([[ex:whose]](#ex:whose)). By grounding grammaticality in community-specific conventions while separating hard compatibility from posterior licensing, OVMG accommodates cross-linguistic variation and rating gradience, which are less central to the L-triviality filter.

LF+RESCALE provides a specific mechanism for acceptable “trivialities”. OVMG treats those cases as possible products of more general interpretive principles within community norms, without positing a dedicated deductive module or specific operators like RESCALE. It also keeps conventional grammatical status separate from subjective processing effects or “feelings” (§[3.7](#sec:feeling-new)). OVMG frames grammaticality as an emergent consequence of communicative practice in the formal sense of §[4.4](#sec:emergent-categoricality), rather than a direct output of logical computation within syntax.
## Relationship to relevance-theoretic accounts
Recent work by makes a useful observation: linguistic intuitions about acceptability arise as byproduct effects of cognitive systems for interpreting communicative acts. Just as people immediately sense when a visual stimulus violates core assumptions about physical objects (as with impossible objects), they detect when utterances violate basic presumptions about communicative efficiency. Scott-Phillips argues that unacceptability occurs not from mere inefficiency, but from an inherent impossibility of interpreting an utterance consistently with these presumptions, much as an impossible trident (Figure [5](#fig:impossible trident)) can’t be interpreted as physically cohesive in any context.

![](./trident.jpg)

Impossible trident

OVMG shares several premises with this account. Both reject the need for an innate grammar faculty, locating linguistic intuitions instead within general cognitive systems, and both treat language as developing from communicative needs rather than autonomous syntactic principles. OVMG’s emphasis on situation-specific form–value relations builds directly on Scott-Phillips’s arguments about how communicative pressures shape linguistic conventions.

The frameworks differ primarily in their explanatory mechanisms. Where Scott-Phillips argues that grammaticality judgments reduce to impossibilities of efficient interpretation, OVMG suggests that while communicative pressures shape which form–value relations become conventionalized, these relationships then create systematic constraints that can’t be reduced to efficiency alone. For Scott-Phillips, one would have to demonstrate that ([[ex:tense]](#ex:tense)) contains inherent contradictions making efficient interpretation impossible. OVMG instead analyzes how _yesterday_’s deictic temporal anchoring fails to unify with the present perfect’s reference-interval contribution. While these analyses might ultimately converge, it remains unclear why the criterion of inherent impossibility of interpretation should apply specifically to operator-value violations rather than to lexical-lexical conflicts or certain phonological patterns. The scope of what constitutes an interpretive impossibility requires further theoretical development.

Empirically, OVMG requires tests of whether specific form–value relations are stable within a communicative situation and where operator-value conflicts arise. The challenge for relevance-theoretic accounts, as Scott-Phillips (personal communication, Dec. 16, 2024) acknowledges, lies in establishing independent, empirically vulnerable claims about what makes efficient interpretation inherently impossible rather than merely difficult. The clearest comparison would test the two accounts on novel constructions as they become acceptable or unacceptable.
# Limitations and future directions
The account has real limits, and each points to work it invites rather than forecloses. One is its reliance on the concept of “communicative situation”. Speakers move among overlapping contexts that shift with the immediate setting, durable social positions, and the norms they orient to. The account builds in this fluidity, but operationalizing these dimensions, and measuring their influence on grammatical stability, will take more precise methods. A further limit is mathematical candour: the Beta filter is a moment-matched approximation to a choice-likelihood mixture; the adoption criterion $`q_\kappa`$ is declared rather than estimated; the deterministic expected-window map is a closure approximation; and the bounded-memory stationary distribution and escape times remain unproved (§[4.4](#sec:emergent-categoricality)). Networked exposure, cohort replacement, and a genuinely shared-latent likelihood for production, repair, ratings, and confidence remain future work. The emergence claim is conditional on those interfaces rather than a generic consequence of filtering.

A second boundary concerns stylistic variation and individual preference. Most choices that fall within grammatical acceptability aren’t cases of (un)grammaticality at all. They matter for this account only when they become tied to communicative situations strongly enough to affect licensing, repair, or categorical rejection. The account still has to explain how stylistic preferences become grammatical licensing facts.

A third concerns the boundary of constructional coverage. The paper argues that many apparently arbitrary restrictions are either compatibility failures, saturation failures, or concentrated non-licensing under historical preemption. Cases that resist those treatments should be analyzed as failures to build a well-typed covering assembly, or else as evidence that the constructional inventory has been specified too narrowly.
## Methodological considerations
The development of experimental syntax since the 2000s has transformed how gradient acceptability is measured, letting researchers quantify subtle differences in judgments and track how they change with exposure. The framework’s predictions invite corpus-based, experimental, and cross-linguistic investigation. Several avenues stand out:

1. _Corpus analysis:_ Large, balanced corpora allow researchers to track frequency patterns and stability over time. Investigating rare or marginal forms (e.g. the independent relative _whose_) in corpora can reveal whether low frequency corresponds to genuinely unstable operator-value patterns or merely a sampling artifact. Comparative corpus research in multiple languages can test predictions about how community values influence grammatical distinctions.

2. _Judgments:_ Controlled psycholinguistic tasks, including magnitude estimation or forced-choice paradigms, can assess rating gradience, confidence, and test–retest stability. Exposure and familiarity manipulations measure satiation effects and distinguish entrenched constraints from constructions that become more acceptable through repeated exposure. Exposure effects should be interpreted through the two-channel read-out: rating improvement without corresponding change in confidence, production, or repair behaviour is evidence for movement in the anomaly channel rather than for a change in licensing status.

3. _Processing measures:_ Eye-tracking, self-paced reading, and EEG studies can identify whether some judgments arise from processing overload rather than durable grammatical constraints. If a form becomes easier to parse with practice while production and repair indicators remain stable, the effect belongs to the implementation-cost channel rather than to the licensing posterior.

4. _Sociolinguistic fieldwork:_ Investigations in communities with distinct dialects or multilingual practices can clarify how social and pragmatic motivations shape grammatical stability. Elicitation tasks and careful comparisons across speech communities can confirm that what counts as grammatical depends on local norms rather than universal principles.

5. _Longitudinal and historical studies:_ Diachronic corpora and historical grammars can trace how marginal constructions evolve, testing predictions about which factors lead certain patterns to stabilize, which fade, and which undergo reanalysis. Tracking a community’s licensing of previously dubious constructions over time provides direct evidence for the gradual dynamics posited by the framework.

6. _A decision-layer discontinuity check:_ The threshold $`\tau(c)`$ is a read-out parameter, not a constitutive boundary. A discontinuity in response type near $`\tau(c)`$ would test the decision layer: whether asymmetric losses shift hearers from acceptance to repair, request for clarification, or sanction, over and above the smooth effect of their own $`g_{i,t}`$. The general design is a regression-discontinuity problem ; multinomial and covariate-adjusted versions are the needed extension . In a confirmatory test, $`\tau(c)`$ has to be estimated and registered before the outcome data is touched. In a contrast independently shown to occupy a separated regime, the dynamics in §[4.4](#sec:emergent-categoricality) predict thin support near the threshold. Smoothness through $`\tau(c)`$ would weaken the proposed decision-layer switch, not the licensing-state theory itself.


Figure [6](#fig:rd-test) states the decision-layer check in one picture: a discontinuity is evidence for a response switch at $`\tau(c)`$, while a smooth curve is evidence that the read-out tracks the posterior mean continuously.

The decision-layer discontinuity check. If asymmetric losses induce a response switch, judge _i_’s treatment of a form should change discontinuously as the judge’s _gi_, _t_ crosses the situational threshold _τ_(_c_) (left); if the read-out tracks that posterior mean continuously, treatment should vary smoothly through it (right). A regression-discontinuity design on multinomial hearer responses targets this decision layer, not the constitutive status state itself.
# Conclusion
Grammaticality, de-idealized, isn’t a categorical fact about an ideal speaker in a homogeneous community but a conditioned form–value relation. Its profile–whether some assembly covers the form, whether the assembly’s operator contributions unify, whether its obligatory dimensions are saturated, and whether the population licenses its constructions–is specified relative to a communicative situation and read through a posterior that carries concentration as well as mean.

The competence–performance split becomes two layers with separate evidence streams, a conventional, population-level status and a two-channel subjective read-out–anomaly and confidence–identified by different measures so that they can falsify each other (§[3.6](#sec:identification-c)). Where licensing is at issue, categoricality is modeled conditionally: an explicit adoption–retention transition connects moment-matched speaker filters to population rates, and the full mean-field map identifies parameter regimes with separated attracting regions. Beta filtering alone doesn’t generate them, and the bounded-memory stationary-distribution result remains open (§[4.4](#sec:emergent-categoricality)). Coverage failure and hard compatibility remain distinct routes rather than default explanations for every sharp rejection.

What the profile is for is projection. A category earns its standing by supporting expectations licensed by partial observation, not by the mere presence of mechanisms: repair, transmission fidelity, satiation, and trajectories of change, over the licensing state as such, its concentration as well as its mean (§[3.3.2](#sec:projectible-use)).

The supporting claims are tested separately. The full population map supplies conditional sufficient conditions for stabilization; longitudinal evidence is needed to attribute an observed profile to those dynamics. The production–repair loop is a candidate maintainer, and intervention evidence would establish whether repair registers operator mis-settings and restores the licensing profile. Section [[sec:repair-controller]](#sec:repair-controller) states the relevant signatures. On this account, grammaticality matters because it predicts which forms will be repaired, transmitted, softened by exposure, or resistant to change.

These commitments expose the framework to failure. The sharp tests aren’t exhausted by the decision-threshold design but form a family of profile-sensitive contrasts: confidence should dissociate preempted gaps from clean winnerless cells at matched mean ratings; framing effects should follow the inverse-concentration rank order; artificial-language learners should distinguish zero evidence from strong preemption; early second-language rejections should track first-language omission informativeness rather than second-language frequency alone; moribund contrasts should lose concentration before categorical decline, while dispersion-leading change requires a named heterogeneity mechanism; policing intensity should follow $`N_t\,P(\text{mis-set})\,r(\Delta,\iota)`$; and compatibility failures should change by re-licensing, not by gradual within-speaker cost reduction.

The account doesn’t have the simplicity of a one-variable theory. It doesn’t reduce grammaticality to a single scalar, a competence–performance split, or a social-pragmatic explanation. Its economy is architectural: the same recurring distinctions (coverage, compatibility, saturation, licensing, subjective read-out, opportunity structure, and diachronic support) handle cases that otherwise invite separate stories. That economy has to be earned empirically. The conditions need independent indicators, and the projections need to fail when those indicators are wrong.

It also carries a significant memory burden. Speakers need not store every utterance as a separate item, but the account asks them to retain many situation-indexed pairings among forms, operator values, constructional neighbours, opportunity estimates, competitors, and repair histories.

That inventory is large, but the framework makes it the model’s data structure: the situation-indexed pairings among forms, values, neighbours, opportunity estimates, competitors, and repair histories are exactly the sufficient statistics the licensing posterior runs on (§§[3](#sec:formalism)–[4](#sec:dynamics)). Compositional inheritance across assemblies keeps first-heard tokens from starting at zero, and future hierarchical pooling across construction families, lexemes, and situations would make the burden still more estimable. If linguistic memory is presumed small in advance, stored generalizations get forced into a rule-plus-exception format, and conditioned licensing is misdescribed as residue.

The program these predictions define is measurement-first. Estimate licensing from converging non-rating indicators (corpus rate per opportunity, elicited production, repair), fix the conditioning state before predicting rather than after, and prioritize cross-linguistic contrasts whose operator status differs, since that’s where the account predicts categoricality should form or dissolve. De-idealizing grammaticality trades a tractable idealization for a profile that answers to evidence. It yields a category that predicts which rejections soften, which forms transmit, and which absences hold.
# Turkish vowel harmony and operator-exponent realization
Turkish illustrates a sharp distinction between lexical disharmony inside stems and allomorphic harmony on inflectional suffixes. [^4] Only suffixal harmony matters for OVMG, and even there the role is indirect. Vowel backness isn’t a public-update value; plural and past are. In Turkish, the exponents of those operators have to satisfy suffixal harmony.

Stem-internal vowels: disharmony tolerated. Loanwords such as _doktor_ ‘doctor’ violate backness harmony, but are fully acceptable; speakers store the form, and the community-level licensing state remains near 1.

doktor
doctor
‘doctor’ (disharmonic stem, grammatical) Because the word contains no malformed operator exponent, a stored construction covers it, the relevant operators unify, and $`G_t\approx1`$.

Suffixal harmony: operator-exponent licensing. Inflectional morphemes are lexicalized with an underspecified vowel; the licensed allomorph copies stem backness and, for some suffixes, rounding. Using the “wrong” vowel doesn’t make the intended value unrecoverable: speakers can identify _-ler_ as a plural exponent and _-du_ as a past exponent. What fails is licensing of that exponent choice in a dense operator-exponent niche.

OVMG account. For the ill-formed *_kitap-ler_ and *_gül-du_:

- The plural and past constructional nodes are licensed at the population level, $`\theta_t(\kappa,c)\approx1`$, with speaker-level inclusion states correspondingly concentrated near inclusion. The mismatched exponent-choice node is unlicensed.

- The mismatched allomorph is still identifiable as an intended exponent, so the token is covered by a candidate operator-exponent assembly. But its pivotal exponent-choice node is licensed to near zero by overwhelming preemption from harmonic suffix choices across the dense plural and past opportunity set. Thus $`G_t\approx0`$ with very high $`\nu`$: a licensing failure with high $`\Phi`$, not empty coverage.


So speakers judge the word categorically wrong, not just odd-sounding, and the confidence is evidential rather than structural: the posterior has concentrated because every relevant suffix opportunity teaches the same allomorphic choice. This keeps suffix-harmony errors apart from word salad. *_Can the have running_ lacks a covering assembly; *_kitap-ler_ has a recoverable intended value and an identifiable exponent, but the exponent-choice node is licensed to zero. By contrast, _doktor_ in ([[ex:doktor]](#ex:doktor)) is covered by its own stored node: stem disharmony violates no operator-exponent licensing condition, so $`G_t\approx1`$ and the disharmony registers only as a phonological cost in $`R_i`$ (§[3.7](#sec:feeling-new)).

Localized exceptions. Some derivational suffixes (e.g. _-imsi_ ‘-ish’) are lexically marked “disharmonic”. Speakers store them, and community-level licensing remains near 1: no exponent condition is violated, so $`G_t\approx1`$ despite vowel mismatch. Clitic boundaries that start a fresh harmony cycle are handled the same way: they satisfy the operator-exponent requirement and leave harmony to phonology alone.

Turkish suffix-harmony errors are grammaticality failures in a precise sense: they don’t mis-set a public-update contrast themselves, but they choose an unlicensed exponent for a closed inflectional operator in a dense niche. Stem disharmony lowers phonological well-formedness and affects only the subjective cost vector. A counterexample would be a case where phonology alone produced categorical, framing-resistant rejection without any operator-exponent licensing requirement in play.
# Acknowledgements
Thanks to Peter Evans, Geoff Pullum, Muhammad Ali Khalidi, Ryan Nefdt, Irene Kosmas, and Mostafa Hasrati for comments and suggestions. I’d like to thank Jamie Ramsden for bringing up the cases of _a orange_ and _le hiver_, and Henri Kauhanen for reviewing the formalization.

Large language models and AI-assisted formalization services – including Claude, ChatGPT/Codex, Gemini, DeepSeek, Ox Alpha, and Aristotle – were used for drafting, editing, adversarial review, and formalization assistance. Substantive outputs were checked against the manuscript and, where applicable, by independent recomputation, local proof replay, or executable tests. I remain responsible for all theoretical claims, arguments, errors, and interpretive choices.

[^1]: The humour derives from political tensions of the Watergate era, when both Vice-President Spiro Agnew and President Nixon would ultimately resign from office.

[^2]: The distinction between grammatical status and the subjective read-out has a philosophical analogue in ’s () distinction between knowledge and acknowledgment. For Cavell, acknowledgment isn’t a separate capacity from knowing but an inflection of it, bearing knowledge toward the situation that produced it. Speakers don’t merely _know_ that a string is ungrammatical; they _register_ it as a violation, with metacognitive consequences. For LLM-based grammaticality research, the distinction blocks an easy inference: LLMs can produce judgments that correlate with human ones, but whether they acknowledge the norms they’re applying or merely process patterns that correlate with those norms remains an open question .

[^3]: Recent real-patterns work on language models raises the broader question of where linguistic patterns reside–in outputs, cognition, model-internal compression, or a plurality of models . OVMG doesn’t settle that question for language as a whole. Its narrower claim is that grammaticality, for the purposes tracked here, is a projectible pattern in situation-indexed licensing profiles.

[^4]: See for discussion of the phonology and for experimental evidence on native judgments.
