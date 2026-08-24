### L-triviality and Grammar

UConn Logic Group Jon Gajewski, University of Connecticut 2/27/09 Proposal There is a formally definable subset of the trivial sentences (=tautologies and contradictions) whose members are systematically unacceptable.

Such sentences are identified by their configuration of logical items at LF. Grammar has access to a representation that is underspecified with respect to the content of non-logical expressions.

At some level, all occurrences of non-logical expressions are treated as if
independent – even two occurrences of the same expression.
I’ll show that this proposal buys an explanation of three semantic restrictions on
the occurrence of quantificational determiners.1
Puzzle 1: Definiteness Effect in There Existential Sentences
There existential sentences (TESs) are compatible with only certain
quantificational there-associates.
(1)
a. There are some curious students.
b. There are no curious students.
c. *There is every curious student.
(2)
Other cases
Good: three, a, many, exactly two, at most five, few…
Bad: all, neither, both, the, most …
It has been proposed that the class of determiners that can occur in TESs is
semantically specifiable.
(3)
there-associate quantifiers are…
a. Barwise & Cooper (1981): Weak [see definition in (12) below]
b. Zucchi (1995): Non-presuppositional
c. Keenan (2003): Left conservative2
Puzzle 2: Selection Properties of Connected Exceptives

Connected Exceptive Phrases (CEPs) like English but John (not free exceptives
like except for Sue) are very picky about the quantifiers that host them.
(4)
a.
*Some student but Sue passed the exam.
b.
No student but Sue passed the exam.
c.
Every student but Sue passed the exam.
(5)
Other cases
Good: none, all
Bad: the rest
The class of acceptable hosts for CEPs seems to be semantically definable as
well; they are just the universal and negative universal quantifiers (cf. von Fintel
1993 a.o.).
(6)
Possible hosts for CEPs are (negative) universals
[The class might also be described as the left anti-additive3 determiners.
cf. van Benthem 1984]
Puzzle 3: Negative ‘Islands’ in Comparatives
Not all quantifiers can appear acceptably inside a comparative clause (CC) (in
certain positions).
(7)
a. Mary is taller than some other student is.
b. *Mary is taller than no other student is.
c. Mary is taller than every other student is.
(8)
Other cases
Good: the rest
Bad: few, fewer than 4, at most 7, not every …
Again the class of problematic quantifiers appears to be defined by a semantic
property: negativity, or more formally, downward entailingness (cf. von Stechow
1984, Rullmann 1995).
(9)
Downward entailing quantifiers are unacceptable in comparative clauses.
Summary
We have seen three semantically describable restrictions on the acceptability of
quantificational determiners.

CEPs CCs TESs Some No Every A semantic explanation of these phenomena is in order. 2. A Biased Survey of Approaches to these Puzzles In this section, we see that in each case it has been proposed that unacceptability arises from trivial truth-conditions: the bad sentences are either tautologies or contradictions. 2.1 Barwise & Cooper 1981 on Puzzle 1 Barwise & Cooper (B&C) 1981 offer an explanation of the unacceptability of certain quantifiers in TESs based on trivial truth-conditions. (10) B&C’s Proposal4

|  | CEPs |  |  | CCs |  |  | TESs |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Some |  |  |  |  |  |  |  |  |  |
| No |  |  |  |  |  |  |  |  |  |
| Every |  |  |  |  |  |  |  |  |  |

There-associates are predicates that apply to the denotation of the “expletive” there. There denotes the domain of individuals De. Logical Form (11) There are some curious students (12) a. A determiner D is strong if for every model M=<[[]],De> and every A⊆De, if

the quantifier [[D]](A) is defined, then [[D]](A)(A)=1.
b. D is weak iff D is not strong
(13) a. [[ every ]](A)(B) iff A⊆B
[STRONG]
b. [[ some ]](A)(B) iff A∩B≠∅
[WEAK]
B&C show that, given Conservativity5, all strong determiners have the following
property:
4 This analysis requires a Bare NP approach to there-associates and “codas” like that advocated by
Williams (1984, 1994, 2006). B&C actually say the construction as a whole predicates Q of De.
5 Conservativity: all natural language determiners are conservative.

(14) If D is strong, then for all A⊆De, then [[D]](A)(De)=1
Hence, (15)a is a tautology; while (15)b is contingent on the existence of curious
students.
(15) a. *There is every curious student.
b. There are some curious students.
The analysis is remarkably powerful and correct. Keenan (1987, 2003, a.o.) has
taken issue with B&C’s generalization.
2.2 von Fintel 1993 on Puzzle 2
Similarly, von Fintel (1993) attempts to derive the unacceptability of certain CEP
hosts from trivial truth-conditions. Gajewski (2008a) extends von Fintel’s results
to other more complex cases.
A first guess at the semantics:
Logical Form
(16)
everyD
smokesP
studentA
but MaryC
(17) [[ but ]](A)(B) = B–A
set subtraction
This is inadequate. Under this analysis, (16) does not entail that Mary does not
smoke. To add this entailment in a uniform way for positive and negative (no
student but Sue) cases is not trivial.
The solution that von Fintel arrives at is this: the complement of but is the least
that you have to take out of the restrictor to make the statement true.
(18) [[ but ]](C)(A)(D)(P) = 1 iff
D(A-C)(P) =1 and ∀S[D(A-S)(P)=1 → C⊆S]
For example, C= {Mary}, D = [[ every]], A = [[ student]], P= [[ smoke]]

A determiner D is conservative iff for all A,B: [[D]] (A)(B)=1 iff [[D]] (A)(A∩B)=1 Essentially, every and no are the only determiners that systematically allow such minimal exceptions. Nearly all other quantifiers yield contradictions or tautologies in the frame of (16). In particular, any left upward entailing quantifier (like some, many, or three) will yield a contradiction as a CEP host. (19) D is left upward entailing iff for all A,B,C s.t. [[D]](A)(C)=1 & A⊆B, [[D]](B)(C)=1. If D is upward entailing and you have removed some individuals from D’s restrictor and the statement is true, then you always could have removed fewer and had a true statement.6 2.3 Puzzle 3 Gajewski (2008b) offers an account of negative ‘islands’ in comparatives in terms of trivial truth-conditions – following an idea proposed and rejected in von Stechow (1984). (20) a. Mary is taller than every other student is. b. *Mary is taller than no other student is. Logical Form (21) Mary d3-tall -er than2 every student NOT d2-tall (22) A is P-er than Q is is True iff DegP3 ∃d[A is d-P and Q is not d-P] Alternatively: {d: A is d-P}∩{d: Q is not d-P}≠∅

(23) A gradable adjective P is monotonic iff if P(d)(x) =1 and d’<d, then

P(d’)(x)=1. (24) {d: Mary is d-tall}∩{d: every student is not d-tall}≠∅ When Q is Downward entailing, this combined with the monotonicity yields tautologies given the scheme for comparative truth-conditions in (22). (25) A quantifier Q is downward entailing (DE) iff for all A, B s.t A⊆B and

[[Q]](B)=1, [[Q]](A)=1.
(26) a. {d: Mary is d-tall}
= [0,Mary’s height]
b. {d: every student is not d-tall} =
{d: no student is d-tall}
= (the tallest student’s height,∞)
c. {d: no student is not d-tall}
=
{d: every student is d-tall} = [0,the shortest student’s height]
When Q is DE, then CC is downward closed. That is, CC denotes an initial
segment of the scale. MC is always an initial segment of the scale. Hence, they
always overlap.

Figure 1
Figure 2
3. THE GREAT CONCERN
Tautologies and contradictions aren’t unacceptable/ungrammatical!
(27) a. It is raining and it isn’t raining.
b. If Fred is wrong, then he is wrong.
c. Figure A is hexagonal or Figure A is not hexagonal.
d. Every square is a square.

Even the authors of the analyses surveyed above have their doubts: [my emphasis] While tautologies and contradictions are not ungrammatical, they are not very informative and are normally restricted to use in special situations construed as set phrases.

Barwise & Cooper 1981, p.183 The conceptual problem with this is that, in general, tautologies or contradictions are not ungrammatical. von Fintel 1993, p.133 One might object against this solution that [a sentence like (20)b] is rubbish and should not express a tautology, i.e. something very precious to the philosopher or mathematician. von Stechow 1984, p.334 Ladusaw (1986)/Kennedy (1997) explicitly deny the viability of such a program. Ladusaw (1986) cites grammatical trivial sentences like (28). (28) a. My brother is an only child. b. Either it will rain tomorrow or it won’t. I agree that sentences with trivial truth-conditions are not necessarily unacceptable. What I propose, however, is that there is a formally identifiable proper subset of the trivial sentences whose members are systematically unacceptable.7 I call these sentences L-trivial. My proposal has two parts: Part 1. Lexical Items are sorted into two classes that play significantly different roles in grammar. The classes track to some extent the logical/non-logical distinction.

Part 2. Non-logical terms are in some sense invisible to the grammar - to the extent that grammatical mechanisms do not even recognize two instances of the same non-logical expression as the same. For the time being let’s assume the sorting of lexical items has been accomplished and examine Part 2. 7 See Chierchia 1984 for another proposal of this kind.

### 3.1 Logical Skeleton

The idea is this. Take a typical example of a tautology like (27)a. The distinction among lexical items will put lexical content predicates like rain on the nonlogical side. I propose the grammar pays little attention to these. As far as the grammar is concerned, the structure of (27)a might as well be (29) and it it is is P -ing not Q -ing The sentence (27)a shares this skeleton with other perfectly contingent statements, e.g., It is raining and it isn’t snowing. Thus, (27)a is acceptable. Call the structure of a sentence scrubbed of information on identity of nonlogical elements its Logical Skeleton: (30) Logical Skeleton

To obtain the Logical Skeleton (LS) of an LF α
a. Identify the maximal constituents of α containing no logical items
b. Replace each such constituent with a fresh constant of the same type
(31) a. LS of (27)b: [if a is P, then b is Q]
b. LS of (27)c: [a is P or b is not Q]
c. LS of (27)d: [every P is a Q]
The intuition behind the Logical Skeleton is that the grammar treats all
occurrences non-logical constants as independent.

Historical Note This idea has a precursor in Körner’s (1955, 1960) logic of inexact concepts. Körner’s two-tiered, three-valued logic effectively made all instances of propositional variables independent. As Williamson (1994, p.108 ff.) notes such a propositional logic has no tautologies or contradictions, and hence supports no theory of inference.

### 3.2 (Non-)Logical Expressions

I propose that the key elements of the Logical Skeleton are logical expressions, i.e., expressions whose denotations meet certain invariance conditions. Much of the discussion in the philosophical literature on the identification of logical constants centers around invariance conditions. (Tarski 1966/1986, Mautner 1946, Mostowski 1957… and many more.) An element of a denotation domain is invariant if it remains the same under certain dramatic changes to the domain. The most commonly used change is permutation of the domain of individuals De. The central intuition here is that invariant elements are topic-neutral; they are insensitive to the identity of particular individuals. (32) A permutation π of De is a one-to-one mapping from De to De. Permutations of De can be extended to permutations of all types (cf. van Benthem 1989). (33) De is the domain of individuals Dt = {0,1} D<a,b>= the set of functions from Da to Db (34) Given a permutation π of De: πe = π πt(x) = x, for all x in Dt π<a,b>(f) = πb  f  πa -1, for all f in D<a,b> (35) An item f ∈ Da is permutation invariant if πa(f) = f, for all permutations πa on Da. (36) A sample of Invariant items

a. De: none
b. Dt: 0, 1
c. D<e,t>: ∅, De
[properly, their characteristic functions]
(37) A lexical item c of type σ is logical iff c denotes a permutation invariant

element of Dσ in all models.8

### 3.3 Application to Puzzles 1-3

3.3.1 There Existential Sentences The denotation of there is an invariant element of D<e,t>. (38) [[there]] = De The denotations of determiners some and every are invariant in D<et<et,t>>, see e.g. van Benthem 1989. (39) There are some curious students. Logical skeleton: [there [are [some P1,<e,t>]]] Interpretation: [[some]](I(P1))(De) (40) *There is every curious student. Logical skeleton: [there [is [every P1,<e,t>]]] Interpretation: [[every]](I(P1))(De) Now we want to use the LS of (40) to explain its unacceptability. The idea is that even once we’ve scrubbed out the identity of the non-logical expressions, we can still deduce the triviality of (40). (41) A sentence S is L-trivial iff S’s logical skeleton receives the truth-value 1 (or 0) in all interpretations. No matter what denotation an interpretation assigns to P1 in the LS of (40), we know the sentence is true. This follows directly from the fact that every is strong, cf.(14). Similarly because some is weak, we know (39) is not L-trivial. (42) A sentence is ungrammatical if its Logical Form contains a L-trivial constituent sentence. 3.3.2 Exceptives (43) [[but]] is invariant in D<et,<et,<<et,<et,t>>,<et,t>>> See Peters & Westerståhl (2006) for proof that exceptive operators are invariant. (44) Every student but Mary smokes Logical skeleton: [every [P1 but P2] P3] Interpretation: [[every]](I(P1)-I(P2))(I(P3)) =1 and ∀S[[[every]](I(P1)-S)(I(P3))=1 → I(P2)⊆S] (45) *Some student but Mary smokes Logical skeleton: [some [P1 but P2] P3] Some interpretations of the predicate constants P1, P2 and P3 will map (44) to true; and some to false. As we saw above, all interpretation of these constants will map (45) to false. Hence (45) is L-trivial and ungrammatical. 3.3.3 Comparatives (46) Mary is taller than every student is tall Logical skeleton: [A is P1-er [than [every P2] is P3]] (47) *Mary is taller than no student is tall

Logical skeleton: [A is P1-er [than [no P2] is P3] ]
Note that by the algorithm (30) the two occurrences of degree predicates –
which are not logical – in a comparative construction must be treated
independently.
I propose that, despite this, L-triviality still holds. This follows if we place
restrictions on the domain D<d,<e,t>>.
(48) Constraints on the class of gradable predicates
a. All gradable adjectives are monotonic.
b. The domains of gradable adjectives are restricted to scales.
(49) a. [[ tall ]] = λd: d∈Sheight.λx:∃d∈ Sheight[HEIGHT(x)=d].d < HEIGHT(x)

b. [[old]] = λd: d∈Sage.λx:∃d∈ Sage[AGE(x)=d].d < AGE(x) If the scales of P1and P3 do not match, as in (49)a&b, then (47) is undefined. If they share a scale, then since both are monotonic the result is a tautology. This means that we must adjust the definition of L-triviality. (50) A sentence S is L-trivial iff S’s logical skeleton receives the truth value 1 (or 0) in all interpretations in which it is defined.

4. Problems for L-triviality.
4.1 Domain-denoting expressions
As mentioned above, the characteristic function of De is an invariant element in
D<e,t>. B&C hypothesize that there denotes De. It is natural to ask whether any
other expressions denote De.
Some natural candidates: exist, self-identical
(51) a. Bill exists.
b. Sue is self-identical.
First, does exist mean the same thing as being in the domain? Are TESs
equivalent to corresponding exist sentences? The answer to the second
question is clearly no.
Second, what do we make of technical vocabulary like self-identical?
Suppose that we decide that [[ exist ]] = [[ self-identical ]] = De. We may still
preserve our account. Exist and self-identical differ from the previous items
we examined in being open-class. We might then limit the terminals of Logical
skeletons to closed-class logical constants.
4.2 Reflexives and variable binding
The copula and reflexives ought to be treated as belonging to a closed class.
Under certain semantic analyses, they are both logical. This presents a problem
to the L-triviality account:
(52) Bill is himself.
(53) a. [[ be ]] = λx.λy.x=y
[cf. Sharvit 2003]
b. [[ himself ]] = λf.λx.f(x)(x)
[cf. Keenan 2006]
c. [[ be himself ]] = λx.x=x = De
How could we handle such cases? The main point of stress here seems to be
the reflexive. If reflexives are not reflexivizing operations but bound variables,
we can connect this problem to another.
(54) Bound variable analysis: Bill 1[ t1 is himself1 ]

We can take any trivial sentence, co-bind its arguments and obtain an – ostensibly – L-trivial sentence.9 (55) Tall is what Bill is and isn’t Tall is [what2 Bill is t2,<e,t> and is not t2,<e,t>] Co-bound variables present a problem for the current formulation of the L-trivial principle. This suggest to me that the next step in this investigation is to determine the role of indices and variable binding in the Logical Skeleton. I leave this for future research. [Van Benthem 1989 calls variable binding a transcendental operation and raises the issue of its logicality – without resolution.] 5. Discussion: Functional Categories Could the distinction that we are after here just be the familiar functional/lexical distinction? Abney (1987) on properties of functional items: 1. Closed-class 2. Phono/morphologically dependent 3. Unique complement 4. Inseparable from complement 5. Lack descriptive content: semantic contribution is second order. Von Fintel (1995) on functional items: 1. Permutation invariant. 2. High type. 3. Subject to universal constraints. A controversial case is prepositions. This is crucial for the exceptive marker but. They are typically taken to be a lexical class (see, e.g., Jackendoff 1977) but are closed class. See Baker (2003) for a recent argument that adpositions are functional. How would a sui generis item like expletive there fit into the functional/lexical split? Is this a pro-PP? An analogy with the f-node/l-node distinction in Distributed Morphology is particularly intriguing.10 While f-nodes are fully specified with (semantic) features, l-nodes are marked with minimal grammatical information. For example, the difference between cat and dog is not represented grammatically until the lateinsertion of Vocabulary items (cf. Marantz 1997, Harley and Noyer 1998).

If this model is correct, we could dispense with the algorithm constructing the Logical Skeleton. The Logical Skeleton would simply be the syntactic structure before Vocabulary Item insertion. 6. Conclusion There is a subset of trivial sentences defined by L-triviality that are systematically unacceptable. There are two steps to identifying an L-trivial sentence.

First divide the terminal elements of LF into logical/functional and nonlogical/lexical expressions. Mark all non-logical lexical expressions as distinct from each other. A sentence whose truth-value depends in no way on the interpretation of nonlogical expressions is L-trivial. L-triviality results in unacceptability. APPENDIX As it stands it is too easy to circumvent the conditions that I have placed on the constructions above. Conjoining a problematic quantifier with an unproblematic one, for example, should improve certain sentences, but does not. For example, neither (56)a nor (56)b contains an L-trivial constituent as defined above. Both are still bad. (56) a. *There is [every curious student and no boring professor]. b. *Fred is taller than [no student and every professor] is. This suggests to me that we need a stronger ban. Currently, we say that a sentence is ungrammatical if its Logical Skeleton contains a constituent c of type t all of whose non-logical parts are irrelevant to determining the value of c. A natural strengthening of the principle that covers the data in (56) would be: (57) A sentence S is ungrammatical if its Logical Skeleton contains a non- logical terminal element that is irrelevant to determining the semantic value of S. (58) a. LS of (56)a: [there [is [every P and no Q]] b. LS of (56)b: [a is P-er than [no P and every Q] is] It is easy to see, for example, that P in (58)a never plays any role in determining the truth-value of (58) as a whole. Selected References Baker, Mark. 2003. Lexical Categories: Verbs, Nouns and Adjectives.

Cambridge. Barwise, Jon & Robin Cooper. 1981. Generalized quantifiers and natural language. Linguistics and Philosophy 4: 159-219. van Benthem, Johan. 1984. Questions about quantifiers. Journal of Symbolic Logic 49:443-466. van Benthem, Johan. 1989. Logical constants across varying types. Notre Dame Journal of Formal Logic 30: 315-342. von Fintel, Kai. 1993. Exceptive constructions. Natural Language Semantics. 1: 123-148. von Fintel, Kai. 1995. The formal semantics of grammaticalization. Proceedings of NELS 25, pp. 175-189. Gajewski, Jon. 2002. L-analyticity and natural language. Ms. MIT. Gajewski, Jon. 2008a. Connected exceptives and NPI any. Natural Language Semantics. Gajewski, Jon. 2008b. More on quantifiers in comparative clauses. Proceedings of SALT 18. Keenan, Edward. 2003. The definiteness effect: semantics or pragmatics?

Natural Language Semantics 11:187-216. Keenan, Edward. 2007. On the denotation of anaphors. Research on Language and Computation 5: 5-17. Körner, Stephan. 1955. Conceptual thinking. Cambridge. Ladusaw, William. 1986. Principles of semantic filtering. In M. Dalrymple et al.

(eds.) Proceedings of WCCFL 5, pp. 129-141. Peters, Stanley & Dag Westerståhl. 2006. Quantifiers in Language and Logic.

Oxford. Rullmann, Hotze. 1995. Maximality in the Semantics of Wh-constructions. PhD Thesis. UMass Amherst. Sharvit, Yael. 2003. Tense and identity in copular constructions. Natural Language Semantics 11: 363-393. von Stechow, Arnim. 1984. Comparing semantic theories of comparison.

Journal of Semantics 3:1-77. Tarski, Alfred. 1966/1986. What are logical notions? History and Philosophy of Logic. Williams, Edwin. 1984. There-insertion. Linguistic Inquiry 15: 131-153. Williamson, Timothy. 1994. Vagueness. Routledge. Zucchi, Alessandro. 1995. The ingredients of definiteness and the definiteness effect. Natural Language Semantics 3: 33-78.

## Footnotes
1. [p1:1] These ideas were first sketched in Gajewski (2002). For additional applications of those ideas see Fox & Hackl (2006), Menéndez-Benito (2006), Abrusan (2007). 2 A determiner D is left conservative iff for all A,B: [[D]] (A)(B)=1 iff [[D]] (A∩B)(B)=1
2. [p2:3] A determiner D is left anti-additive iff for all A,B,C: [[D]](A∪B)(C)=1 iff [[D]](A)(C)=1 ∧ [[D]](B)(C)=1
3. [p5:6] In other words the least you have to remove is nothing (i.e., C = the empty set). Von Fintel (1993) assumes there is a presupposition that C is not empty. We could also just add this to the truthconditions: (i) [[but]] (C)(A)(D)(P) = 1 iff C≠∅ and D(A-C)(P) =1 and ∀S[D(A-S)(P)=1 → C⊆S]
4. [p9:8] This is an oversimplification, see McGee (1996), MacFarlane (2000), and Peters & Westerstahl (2006) for more sophisticated definitions.
5. [p13:9] Thanks to Danny Fox for bringing this kind of example to my attention. 10 Thanks to Danny Fox for this suggestion.
