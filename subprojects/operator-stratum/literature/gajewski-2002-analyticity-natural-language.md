## On Analyticity in Natural Language

Jon Gajewski

### 0. Introduction

In this paper, I provide preliminary evidence that there is a principle of natural language that makes crucial reference to a kind of analyticity. The traditional conception of analyticity is, perhaps, the following: a sentence S is analytic if and only if S is true in virtue of its form. For the purposes of this paper, it will be useful to count as analytic both those sentences that are true in virtue of their form and those sentences that are false in virtue of their form. I use the term ‘analytic’ in this broader sense throughout. The kind of analyticity to which I propose natural language is sensitive is what I refer to as Logical Analyticity (henceforth L-analyticity). L-analytic sentences are distinguished from analytic sentences in the broader sense by the aspects of form in virtue of which they are true (or false). More specifically, L-analytic sentence are those that are true (or false) in virtue of their logical structure. The bulk of the work to be done in this paper is to give precise content to the notion ‘logical structure.’ In so doing, I rely on the linguist’s concept of Logical Form (see, e.g., May 1985) and van Benthem’s definition of a logical constant (van Benthem 1989).

The proposed principle of natural language that makes crucial reference to L- analyticity is the following (to be revised below): (1) L-analytic sentences are ungrammatical.

Principle (1) is simply a well-formedness condition, stipulating that L-analytic sentences are ill-formed. Establishing such a principle requires investigating the intuitions of native speakers concerning the grammatical well-formedness of sentences. More controversially, it depends on the ability of native speakers to distinguish between ill- formed sentences and sentences of their language that are well-formed but semantically anomalous. Chomsky has famously argued that native speakers possess such an ability with the sentences in (2).

(2) a. Colorless green ideas sleep furiously. b. Furiously sleep ideas green colorless.

Of these sentences, Chomsky says, “Sentences [(2a)] and [(2b)] are equally non-sensical, but any speaker of English will recognize that only the former is grammatical.”1 I take the practice of generative linguistics to have borne out Chomsky’s contention about native speakers intuitions and assume the validity of such a method of investigation without further comment.

The plot of the rest of this paper is as follows. In section one, I place this paper’s empirical investigation of analyticity in the context of Quine’s skepticism about the analytic/synthetic distinction. In section two, I review two prominent analyses in the linguistics literature that make, in my view, implicit appeal to the principle in (1). In section three, I give precise formal definitions to L-analyticity and principle (1) and show how they apply to the analyses reviewed in section two.

### 1. Quine’s Doubts About Analyticity

Quine 1960 constructs a behaviorist theory of meaning for language. In so doing, Quine imagines the meaning-researcher as a field linguist approaching a hitherto undiscovered language. The only data available to this field linguist are (i) the non-verbal stimuli that he can assume to be impinging on his informant and (ii) his informant’s prompted assent or dissent to an utterance in the presence of some stimulus. According to Quine, the only reasonable notion of meaning available to a field linguist in such circumstances is that of stimulus meaning. The stimulus meaning of a sentence is the ordered pair of the stimulus conditions under which the informant assents to an assertion of the sentence and the stimulus conditions under which the informant dissents from an assertion of the sentence.

As Quine points out, the notion of stimulus meaning does not support many categories and distinctions with which we are familiar from “intuitive semantics.” For example, co-extensiveness of terms is not sufficient to secure sameness of stimulus meaning when the terms are used as observation sentences. Quine’s example: “indian nickel” and “buffalo nickel” might have the same extension while the sentences “Indian nickel” and “Buffalo nickel” differ in stimulus meaning. A novice in coins may well assent to the former when presented with the obverse side of a buffalo nickel and dissent from the latter. Neither, according to Quine, is co-extensiveness necessary for sameness of stimulus meaning. This is the famous Gavagai/Rabbit example. According to Quine, the sentences “Gavagai” and “Rabbit” might have the same stimulus meaning while the terms are not co-extensive, with “rabbit” having rabbits in its extension and “gavagai” having, perhaps, non-detached rabbit parts. Thus, synonymy of terms is not reconstructible by sameness of stimulus meaning.

Similarly, Quine argues that the analytic/synthetic distinction dissolves once we take this behaviorist approach meaning. Quine’s understanding of philosophical tradition is that an analytic sentence is “true purely by meaning and independent of collateral information.” According to Quine typical examples of analytic sentences are “Bachelors are unmarried”, “Pigs are pigs”, and “2 + 2 = 4”. The nearest reconstruction of analyticity that is available to the field linguist is socialized stimulus analyticity. A sentence is socialized stimulus analytic if and only if every member of the speech community under consideration assents to the presentation of the sentence under every stimulus condition. This clearly does not capture the original intuitive content of analyticity, since, as Quine points out, the sentence “There have been black dogs” may well turn out to be socialized stimulus analytic.

For Quine, the unrecoverability of the traditional notion of analyticity within his behaviorist theory of meaning is no great loss. While Quine is sympathetic to intuitions of analyticity, he states, “The intuitions are blameless in their way, but it would be a mistake to look to them for a sweeping epistemological dichotomy between analytic truths as by-products of language and synthetic truths as reports of the world.”2 Quine’s position on the analytic/synthetic distinction has been most notably supported in the work 2 Word & Object p.67 [italics are mine] of Donald Davidson, who goes so far as to suggest that Quine’s “erasing the line between the analytic and the synthetic saved philosophy of language as a serious subject by showing how it can be pursued without what there cannot be: determintate meanings.”3 To Quine and his followers then there are no determinate meanings directly associated with language; rather all meaning must be understood in terms of a speaker’s general systems of belief.4 In the remainder of this paper, I will assume a rather different approach to natural language meaning. I assume a model-theoretic interpretation of language along the lines of Montague 1974 and its later developments within linguistic theory, as in Dowty, Peters & Wall 1981 and Heim & Kratzer 1998, for example. I use this method of semantic investigation to argue for the empirical usefulness of the concept of analyticity. This may seem somewhat circular, since adopting this approach to meaning is in some sense already committing to a notion of analyticity.5 My goal, however, is to use this framework to uncover a variety of analyticity (L-analyticity) whose existence can be argued for on the firmer basis of grammaticality judgments.

### 2. Analyticity and Explanation in Linguistics

In attempting to explain the ill-formedness of certain natural language constructions, many semanticists have made appeal to the notion of trivial truthconditions. That is, they suggest that native speakers reject a construction as ungrammatical or ill-formed because they know either that it is always true or always false. Such a principle, however, is always invoked with trepidation. After all, it is not at all clear that a tautology or a contradiction is always ill-formed in natural language. In fact, it is not clear that tautologies and contradictions cannot be used in the course of meaningful communication. The latter point has been made most forcefully, and familiarly, by Grice 1957. Grice specifies a set of maxims on the basis of which hearers read more into what a speaker utters than what he actually says. According to Grice, the flouting of these 3 “Coherence Theory of Truth and Knowledge” in Lepore 1986, p. 313 4 See Chomsky 2000 for a critique of this position. 5 See Quine’s 1960 (p.67) comments on Carnap’s Meaning and Necessity. maxims by the speaker can also lead the hearer to draw conclusions about a speakers intentions. A blatant violation of Grice’s Maxim of Quantity is to utter an uninformative sentence, such as a tautology. Grice gives (3) as examples of sentences that can be used to flout the Maxim of Quantity in a meaningful way: (3) a. Women are women. b. War is war.

The possibility of flouting the Maxim of Quantity in this way justifies the trepidation of linguists who propose to derive ungrammaticality from trivial truthconditions.

In the next two subsections, I present two representative analyses of this kind from the linguistics the literature. In both instances, we will see that more underlies the intuition behind these analyses than just the contention that tautologies and contradictions are ungrammatical. The first analysis, the most famous of this kind, is Barwise & Cooper’s 1981 explanation of the so-called Definiteness Restriction in there-existential sentences. The second is von Fintel’s 1993 explanation of co-occurrence restrictions on exceptive phrases. In section three, I show how these analyses can best be understood in terms of L-analyticity.

2.1. Barwise and Cooper 1981 The seminal paper of Barwise & Cooper 1981 (henceforth B&C) gives strong support to the hypothesis that noun phrases in natural language denote Generalized Quantifiers6 (henceforth GQs) and investigates the formal properties of GQs in some detail. One of their most important and influential contributions was their explanation of the Definiteness Restriction in there-existentials. The facts to be explained, first precisely stated in Milsark 1977, are the following: (4) “Strong” quantifiers ungrammatical in there sentences: a. *There is the wolf at the door 6 See Mostowski 1957 b. *There were John and Mary cycling along the creek c. *There was everyone in the room (5) “Weak” quantifiers grammatical in there sentences: a. There is a wolf at the door b. There were two people cycling along the creek c. There was someone in the room “Strong” and “weak” are simply labels that Milsark assigned to the classes of quantifiers that are ungrammatical and grammatical in there sentences, respectively. B&C provided a precise formal characterization of “strong” in terms of GQ-theory: (6) DEFINITION. A determiner D is strong if for every model M = <E, || ||> and every A Õ E, if the quantifier ||D||(A) is defined then AŒ||D||(A).

D is weak if it is not strong.

A determiner meaning, such as ||D|| is a function from sets to GQs (which are sets of sets). Some examples of determiner meanings: (7) a. ||some|| = lA.{XÕE | A«X≠∅} b. ||every|| = lA.{XÕE | AÕX} c. ||no|| = lA.{XÕE | A«X=∅} Of these determiners, only every (7b) is strong; a set is always a subset of itself no matter the model. Some is not strong because when its restrictor A is the emptyset, then A œ ||some||(A), since in that case A«A=∅. For the vast majority of cases, the definition (6) divides quantifiers into the appropriate class with respect to their acceptability in there sentences. This is, in and of itself, an achievement. B&C go on to suggest, however, that the fact that all the quantifiers that are excluded from there sentences are strong provides an explanation for the phenomenon.

To see how the explanation works, consider the following consequence of a quantifier’s being strong: (8) If a determiner D is strong, the for every model M = <E, || ||> and every AÕE, E Œ ||D||(A) That is, the domain of the model is always a member of a strong quantifier. For B&C, this property is responsible for the fact that strong quantifiers are ungrammatical in there sentences. Here’s why: B&C make the following claim about the interpretation of there- sentences: (9) A sentence of the form there is/are NP can be interpreted as meaning that the set of individuals in the model (E) is a member of the GQ denoted by the NP.

For example, (10) there are some new students is True iff E Œ ||some||(||new-students||) In the case of (10), these truthconditions will be met just in case there are some new students in the domain of individuals. Now consider what happens when the NP in a there sentence is a strong quantifier. B&C state, “for any strong determiner the result will be a tautology, since to say that E is in the quantifier is the same as to say that A is in the quantifier [see (8)].” They then go on to note that tautologies are not generally ungrammatical though they are uninformative. As we’ve learned from Grice’s examples, however, this truthconditional uninformativity cannot be the explanation for the judgments of ungrammaticality reported in (6).

2.2. Von Fintel 1993 Von Fintel 1993 gives an explanation of the distribution of exceptive phrases that is in the same spirit as B&C 1981. Von Fintel focuses on the distribution of but-exceptives.

This distribution is illustrated below: (11) a. Every/no student but Bill passed the exam. b. *Some/*three/*many students but Bill passed the exam. c. *Most/*exactly two/*fewer than three students but Bill passed the exam.

The traditional generalization about the distribution of exceptives, which these data reflect, is that they are only compatible with universal quantifiers, either positive (every) or negative (no). Von Fintel argues that this distribution follows from the semantics of the construction. The semantic facts to be explained are the entailments in (12).

(12) a. Every student but Bill passed the exam.

(i) fi Bill is a student (ii) fi Bill did not pass the exam (iii) fi Every other student passed the exam b. No student but Bill passed the exam.

(i) fi Bill is a student (ii) fi Bill passed the exam (iii) fi No student that is not Bill passed The challenge here is to find a unified semantics for but-exceptive constructions that yields this pattern of inference; i.e., that gives us that Bill passed when but Bill modifies the negative universal and that he did not when but Bill modifies the positive universal.

Von Fintel meets this challenge by giving the following meaning schema for the construction: (13) D A || but || C P is True iff PŒD(A\C) & "S[PŒD(A\S) Æ CÕS] Where A, C, P are sets and D is a determiner meaning as above. For example, for (12a): D = ||every||, A=||student||, C = {||Bill||} and P = ||passed the exam||. These truthconditions say that C is the least (i.e., unique minimal) set whose subtraction from the restrictor of the quantifier (i.e., A) makes the quantification true. It is very nearly true that only universal quantifiers guarantee such least exceptions.7 Most other quantifiers, though not all, not only do not guarantee but actually cannot have least exceptions.

Whenever such a determiner is substituted in the schema (13), the result is a contradiction.

Take as an example the class of determiners that B&C refer to as left upward monotone (↑mon): (14) DEFINITION. A determiner is left upward monotone if for all models M = <E, || ||>, and all AÕBÕE, if X Œ ||D||(A) implies X Œ ||D||(B).

Examples of ↑mon determiners are some/a, (at least) one, two, etc. Whenever a ↑mon determiner is substituted into (13), the result is a contradiction. Here’s the reason: if XÕY, then Z\Y Õ Z\X. The first conjunct of (13) says that P Œ D(A\C), so if there exists a set S that is a proper subset of C, then the second conjunct is false because P Œ ||D||(A\S) (since ||D|| is ↑mon) but C is not a subset of S8.

Von Fintel, thus, appeals to the fact that a sentence is a contradiction to explain is its ungrammaticality. This is dubious for the reasons cited above. Von Fintel himself notes that, “the conceptual problem with this is that, in general, tautologies or contradictions are not ungrammatical.” He then suggests that the cause of the ungrammaticality is “grammaticization” of the fact that the quantifiers do not guarantee least exceptions. An appeal to a vague process of grammaticization takes away from the force of his explanation. The concept of L-analyticity developed in the next section will enable us to keep the simpler, more forceful explanation.

2.3. Summary

7 Von Fintel 1993 himself points out most as a problem. See Moltmann 1995 and Lappin 1996 for further problems. 8 Of course, if there are no proper subsets, there is no problem. This is the case where C = ∅. This problem was not noted in von Fintel 1993; it is not hard to fix, however: just add a clause to (13) stating that C must not be empty.

The two analyses reviewed above show that it is often useful to explain the ungrammaticality of a sentence by showing that it has trivial truthconditions (is analytic).

It is well known, however, that there can be no general principle stipulating that all tautologies and contradictions are ungrammatical. This casts doubt on the viability of such analyses. In the next section, I propose a principle that puts these analyses on more solid ground.

### 3. L-analyticity

In his paper “ Truth and Meaning”, Donald Davidson sketches a spare, extensional theory of meaning. He notes that within this theory, “ analyticity goes untreated…Even such sentences as ‘A vixen is a female fox’ bear no special tag unless it is our pleasure to provide one.” He goes on to point out that there is another slightly different kind of analyticity that does fall out of his theory: A truth definition does not distinguish between analytic sentences and others, except for sentences that owe their truth to the presence alone of the constants that give the theory its grip on structure: the theory entails not only that these sentences are true but that they remain true under all significant rewritings of their non-logical parts.9 This is, in essence, the kind of analyticity that I propose induces ungrammaticality in natural language. Call it L(ogical)-analyticity. We should not speak, however, as if this is a clear concept. A good deal of explication is required. The two most important points that require clarification are (i) the definition of ‘logical constant’ (ii) what counts as a ‘significant rewriting’ of the non-logical parts of a sentence. These points are the topics of the next two sections, respectively.

3.1. Van Benthem 1989 on Logical Constants 9 “Truth and Meaning” in Ludlow 1997 p.103 [italics are mine].

Van Benthem 1989 gives a definition for logical constants across types that I will adopt.

Though logicality may be more standardly defined in syntactic terms, in terms of a constant’s role in inference, van Benthem’s definition is semantic. Since van Benthem’s theory is stated in terms of type logic, let’s be clear about the domain of semantic entities he assumes. For van Benthem the domain of semantic values is sorted into a type hierarchy. There are two basic domains, those of individuals and truthvalues; and the rest are defined by induction: (15) De is the base set of individual entities Dt is the set of truthvalues {0,1} D<a,b> is the set of all functions with domain Da and range Db Given this hierarchy, van Benthem asks whether there is a criterion by which we can identify the logical elements in each type. Generalizing from uncontroversially logical elements such as the first-order quantifiers and truth functional connectives, he proposes that logical items can be identified by the property of individual neutrality. That is, the logical items are those that are insensitive to which individuals are in the base domain De.

Van Benthem makes individual neutrality precise by defining it in terms of permutations on De. Since permutations “shuffle” individuals around, the logical constants will be those items that are preserved under all permutations of the domain.

(16) A permutation p on Deis a bijective mapping from De to De (17) Lift a permutation p on De to a family of permutations defined on all types, thus: a. pe = p b. pt = the identity map c. p<a,b>(f) = {<pa(x), pb(y)> | <x,y> Œ f } for f Œ D<a,b> (18) DEFINITION. An item f Œ Da is permutation invariant if pa(f) = f for all permutations p of De.

Now we have at our disposal an analysis of logicality in terms of permutation invariance.

As a definition of logicality, permutation invariance casts a broad net. This, as we shall see, is exactly what we want.

Before moving on, however, let’s consider a trivial application of this definition.

Take truth-functional conjunction, with the following standard denotation: (19) a. ||and|| = luŒDt.lvŒDt.u = v = 1 b. ||and|| Œ D<t,<t,t>> Given our inductive definition of permutations, this function is clearly preserved under every permutation of the base domain, that is: (20) p<t,<t,t>>(||and||) = ||and||, for every permutation p of De.

By contrast, a predicate of type <e,t> such as women will not be preserved under all permutations of the domain since some of the permutations will map women onto non- women.

3.2. Significant Rewritings In this section, I give a formal analysis of Davidson’s phrase “significant rewriting of non-logical parts.” The basic idea is that to evaluate L-analyticity one must look at the logical skeleton of a sentence. The logical skeleton is derived from the logical form of a sentence by replacing each non-logical expression with a distinct variable of the appropriate type. A sentence is L-analytic if it is true (or false) under all assignments of values to variables. This is the technical notion that stands in for Davidson’s “significant rewritings of non-logical parts.” 3.2.1. Logical Form The notion of logical form that I assume is taken from linguistics. At Logical Form (LF) a sentence is structured into binary constituents. These constituents are assigned denotations recursively: (i) lexical items receive their denotations by stipulation in the lexicon (ii) complex constituents receive their denotations by means of (21) (21) Functional Application If a is a constituent that immediately dominates b and g and ||g|| is in the domain of ||b||, then ||a|| = ||b||(||g||) An example, (22) Logical Form of There are some new students: There are some new-students (23) a. ||some|| = lf<e,t>.lg<e,t>. there is an x such that f(x)=1 and g(x)=110 b. ||new-students|| = lx. x is a new student c. ||there|| = lx.x Œ De I am assuming that the copula is vacuous. I assign there the denotation in (23c) as a way of implementing B&C’s (9). Using the basic denotations in (23) and the composition principle in (21) we see that ||(22)|| = 1 iff there are new students in De.

3.2.2. Logical Skeleton The logical skeleton of a sentence, which will be used in evaluating L-analyticity, is obtained from its logical form by means of the following (semi-formal) algorithm: (24) a. Identify the maximal constituents containing no logical items b. Replace each such constituent with a distinct variable of the same type 10 This denotation differs from that in (7) only in that now, instead of sets, I amusing their characteristic functions.

So, for example the logical skeleton obtained from (22) is (25). [From now on I indicate constituent structure with brackets.]

(25) Logical Skeleton of (22)

[there [are [some u1,<e,t>]]] The item there is not replaced by a variable as it denotes De, which is one of the two elements of D<e,t> that is preserved under permutations of De. The other permutation invariant element of D<e,t> is the empty set. Neither is the existential determiner some replaced, as it denotes a permutation invariant element of D<<e,t><<e,t>,t>>. New-student, on the other hand, is not a permutation invariant element of D<e,t>. It is therefore replaced by a variable of the same type, i.e., a variable of type <e,t>.

Since logical skeletons contain free variables, they only receive semantic values relative to a variable assignment. As we are assuming type-sorted variables, a variable assignment is a function from ordered pairs of a natural number and a type to elements of that type. That is, a variable assignment g is constrained in the following way: (26) For every natural number i and type s, g(<i,s>) Œ Ds.

The following rule gives the interpretation of variables in our system: (27) Variable Rule If a is a variable with index <i,s>, then ||a||g = g(<i,s>) 3.3. L-analyticity implies Ungrammaticality Now we are in a position to state the principle that will explain the facts presented in section 2. First, a formal definition of L-analyticity: (28) DEFINITION. An LF constituent a of type t is L-analytic iff a’s logical skeleton receives the denotation 1 (or 0) under every variable assignment.

Now, the principle linking analyticity and ungrammaticality: (29) A sentence is ungrammatical if its Logical Form contains a L-analytic constituent.

Let’s apply these new definitions and principles to the Definiteness Restriction and the distribution of exceptives.

3.3.1. The Definiteness Restriction We have already given the logical skeleton for a there sentence in (25), repeated below.

(25) Logical Skeleton of (22) [there [are [some n1,<e,t>]]] This logical skeleton is of type t, but it is not L-analytic. The reason is that when the variable assignment maps n1,<e,t> to the emptyset, the logical skeleton (25) receives the value 0. When the variable assignment maps n1,<e,t> to any other set (25) receives the value 1. Consider, however, what happens when some is replaced by a strong determiner such as every. Then the logical skeleton is (30b).

(30) a. *There is every new student. b. Logical skeleton of (30a) [there [are [every n1,<e,t>]]] This logical skeleton (30b) does receive the value 1 under every variable assignment.

The reason is that every variable assignment is constrained by (26) to map n1,<e,t> to an element of D<e,t>. Every element of D<e,t> is a subset of De. Thus, (30b) is L-analytic and

(30a) is ungrammatical. The Definiteness Restriction can, thus, be explained in terms of

principle (29).

3.3.2. The distribution of but-exceptives To implement his theory compositionally in terms of LFs, von Fintel 1993 assigns but the following denotation, factored out of the meaning schema in (13): (31) ||but|| = lf<e,t>.lg<e,t>.lD<et,<et,t>>.lh<e,t>.D(g\f)(h)=1 & "j<e,t>[D(g\j)(h)=1 Æ gÕj]11 This is a permutation invariant element in D<et<et<<et,ett><et,t>>>>, i.e., a logical constant. Thus, it is not replaced by a variable in the formation of logical skeletons. So (32a) and (33a) receive the logical skeletons (32b) and (33b), respectively.

(32) a. Every student but Bill complained b. [[every [n1,<e,t> [but n2,<e,t>]]] n3,<e,t>] (33) a. Some student but Bill complained b. [[some [n1,<e,t> [but n2,<e,t>]]] n3,<e,t>] Given our discussion of ↑mon determiners in section 2.2, we know that the logical skeleton in (33b) will receive the value 0 under every variable assignment. Its falsity is independent of the sets denoted by its non-logical parts. (32b), on the other hand, will receive either the value 1 or 0 depending on the facts of the matter. Thus, principle (29) can be invoked to explain the distribution of but-exceptives, as well.

3.3.3. Tautologies and contradictions more generally Our notion of L-analyticity and the principle (29) have captured the spirit, and maintained the predictions, of B&C’s and von Fintel’s analyses. Recall, however, that both of these analyses already made correct predictions for the phenomena they were intended to cover. The problem for B&C and von Fintel was that the broad notion of analyticity they invoked included all tautologies and contradictions. That is, they predicted tautologies and contradictions such as (34) to be ungrammatical; contrary to fact.

11 (i) f\g is the function that maps x to 1 iff f(x)=1 and g(x)=0 (ii) fÕg iff "x[f(x)=1 Æ g(x)=1] (34) a. Every woman is a woman b. John is smoking and John is not smoking The point in defining L-analyticity was to find a more restrictive notion of analyticity that did not include sentences such as (34a) and (34b). Let us now check that we have succeeded in this endeavor. Since every is permutation invariant but woman is not, (35) is the logical skeleton of (34a).

(35) Logical skeleton of (34a) [[every n1,<e,t>] n2,<e,t>] Notice that the two instances of woman were crucially replaced with distinct variables.

This is in accordance with (24b), which encodes our notion of “significant rewriting of non-logical parts.” So one part of significant rewriting is obliterating co-variation among non-logical arguments. Clearly, then (35) does not receive the value 1 or 0 under every variable assignment. Some variable assignments will map n1,<e,t> and n2,<e,t> to sets that are in a subset relation and some will not.

Similarly consider the logical skeleton of (34b): (36) Logical skeleton of (34b) [n1,t [and [not n2,t]]] Once again the algorithm for forming logical skeletons obliterates the co-variation of non-logical elements, in this case assigning distinct variables to the two occurrences of John smokes. And again, clearly the result is a logical skeleton that is not L-analytic.

Under a variable assignment that maps the variables to 1 and 0, (36) receives the value 1; under a variable assignment that maps them both to 1, (36) receives the value 0.

In sum, L-analyticity correctly explains the contrasts noted in B&C 1981 and von Fintel 1993, while improving on these theories by failing to predict that garden-variety analytic sentences such as (34a) and (34b) are ungrammatical.

### Conclusion

In this paper, I have argued for recognizing a category of analyticity on the basis of its usefulness in providing an explanation for a puzzling class of facts about native speakers’ intuitions of ungrammaticality.

### References

Barwise, J. and R. Cooper 1981. “Generalized Quantifiers and Natural Language” Linguistics and Philosophy 4:2, 159-220.

Van Benthem, J.F.A.K. 1989. “Logical Constants Across Types” Notre Dame Journal of Formal Logic 3.

Chomsky, N. 1957. Syntactic Structures Chomsky, N. 2000. New Horizons in the Study of Language Davidson, D. 1967[1997] “Truth and Meaning” in Ludlow 1997 Davidson, D. 1986. “Coherence Theory of Truth and Knowledge” in Lepore 1986 Dowty, D., S. Peters, and R. Wall. 1981. Introduction to Montague Semantics. Kluwer.

Von Fintel, K. 1993. “Exceptive Constructions” Natural Language Semantics 1:2 Grice, H. P. 1975. “Logic and Conversation” in Grice 1994 Heim, I. and A. Kratzer. 1998. Semantics in Generative Grammar. Blackwell.

Lepore, E. 1986. Truth and Interpretation.

Ludlow, P. 1997. Readings in the Philosophy of Language. MIT Press.

Milsark, G. 1977. “Toward an Explanation of Certain Peculiarities of the Existential Construction in English” Linguistic Analysis 3:1-30.

Montague, R. 1974. Formal Philosophy: Selected Papers of Richard Montague, edited by R. Thomason, Yale University Press.

Quine, W.V.O. 1960 Word and Object.

## Footnotes
1. [p2:1] Chomsky 1957 p.15
