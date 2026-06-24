Building Social Cognitive Models of Language Change Daniel J. Hruschka, School of Human Evolution and Social Change, Arizona State University and Santa Fe Institute Morten H. Christiansen, Department of Psychology, Cornell University and Santa Fe Institute Richard Blythe, Scottish Universities Physics Alliance and School of Physics and Astronomy, University of Edinburgh William Croft, Department of Linguistics, University of New Mexico Paul Heggarty, McDonald Institute for Archaeological Research, University of Cambridge Salikoko S. Mufwene, Department of Linguistics, University of Chicago Janet B. Pierrehumbert, Linguistics Department, Northwestern University and Northwestern Institute on Complex Systems Shana Poplack, Department of Linguistics, University of Ottawa

Corresponding author: Hruschka, Daniel J. (Daniel.Hruschka@asu.edu).

Abstract: 103 words Body (including Acknowledgments): 2212 words Boxes: 1402 words Additional Material: Glossary, Outstanding Questions, 4 boxes, 1 table, 1 figure 62 references Fonts: Arial. For phonetic representations “WP phonetic” is also used.

# Abstract

Studies of language change have begun to contribute to a number of pressing questions in the cognitive sciences—including the origins of the human language capacity, the social construction of cognition, and the mechanisms underlying culture change in general. Here, we describe recent advances within a new emerging framework for the study of language change, one which models language change as an evolutionary process among competing linguistic variants. We argue that a crucial and unifying element of this framework is the use of probabilistic, data-driven models to both infer change and to compare competing claims about social and cognitive influences on language change.

# Changes in the Study of Language Change

When Geoffrey Chaucer wrote Canterbury Tales in the 14th century, many of the linguistic devices he used to spin his Tales were very different from those that a modern English speaker might use today. Consider:

Your woful mooder wende stedfastly, That crueel houndes…Hadde eten yow.

While this sentence retains an eerie similarity to modern English, most contemporary readers have difficulty reading Chaucer’s prose. There are several reasons for this failure to communicate across the centuries. Chaucer used the currently incomprehensible past tense of wene to convey something like “believed”, and he chose houndes to mean generic canines when most modern English speakers would have used dogs. For Chaucer’s other word choices, speakers of modern English might deploy similar forms—but with very different pronunciations (i.e. mother for mooder and had for Hadde). On the other hand, some of Chaucer’s linguistic conventions match quite closely those used today. Chaucer put words together in a relatively strict order for “who-did-what-to-whom” and did not use special markings to indicate case on most nouns. These conventions were in turn dramatic shifts from the English spoken several centuries before Chaucer wrote his Tales.

Language is arguably the most complex cultural system found in humans, and understanding how this system changes—for example, from Old English through Chaucer’s time to late modern English—can shed light on a number of

important questions in the cognitive sciences (see box 1). Studies of language change have contributed to current debates about the underlying cognitive capacities for language and how they evolved in humans [1, 2]. They have also sharpened our understanding of communication as a cognitive and social process based on the repeated construction and interpretation of utterances in social interactions [3-5]. Language also provides a particularly well-documented opportunity for investigating general processes of cultural change [1, 6, 7]. In these ways, the study of language change goes beyond particular historical observations about a specific cultural system. It can also speak to more general questions about culture and cognition. Despite these potential contributions, cognitive scientists have generally neglected change, focusing on other aspects of language, such as the biological foundations of linguistic capacities, the structure of language, and processes of language acquisition.

In the past several decades, linguists in a wide range of subfieldsincluding sociolinguistics, psycholinguistics, language typology, historical linguistics, and creolistics—have proposed novel, cognitively and socially informed models of change and developed new ways of testing these models against data. These diverse approaches have begun to converge on a general framework which models language change as a dynamic population-based process whereby speakers choose variants from a pool of linguistic variation in a way governed by both social and cognitive constraints. In this article, we discuss advances within this emerging framework, highlighting some of the most commonly proposed mechanisms. More generally, we argue for the utility of

general, probabilistic models for comparing and assessing competing models developed within this framework.

# Different Approaches, Common Goals

Compared to other cultural systems, language has received unparalleled academic attention, inspiring an entire discipline—linguistics—which itself includes numerous subfields. Each subfield approaches language change with different kinds of data and at different time depths and resolutions (see table 1). Despite differences in data and focus, we see these approaches converging on a common framework for studying language change with several unifying assumptions and goals (see figure 1).

First, a language is not a static entity. Nor does it change as a monolithic whole. Rather it encompasses a population of individual speakers and listeners constructing and interpreting utterances to get things done in the world, such as drawing someone’s attention to an event or making someone think or act in desired ways. Given the demands of coordination in a speech community, utterances often share recurring commonalities, including how certain words mean specific things and how sounds and words are put together to accomplish certain goals. These conventions may give the impression of a monolithic structure, but by taking a dynamic, population perspective, it is possible to study both linguistic conventions and the many deviations from them [4, 5].

Second, people have multiple ways of constructing utterances to communicate the same meaning. This variation is generated at all levels, from

the articulation of sounds—e.g., pronouncing water as [w t r], [w D r], or

[w D ]—to the use of particular constructions—e.g., I’ll be there versus I’m going

to be there—to different ways of putting words together to clarify “who-did-whatto-whom” [2, 5, 8-10]. Such variation within speakers and between speakers in a speech community provides the raw material for change in the same way that genetic variation is a prerequisite for genetic change in a biological population [4, 5, 11].

Third, language change depends on social factors. The size of a speech community can affect the repertoire of available linguistic devices, such as the number of phonemes in a language [12]. And a community’s structure—the frequency and clustering of social interactions—as well as economic and political factors can determine the success and rate with which innovations spread through a population [4, 13-16].

A final unifying point of this framework is what researchers are trying to explain. Given the stochastic nature of language change, trying to predict individual trajectories and particular histories would be a fool’s errand. Rather, these approaches focus on a large number of cases and use probabilistic models to estimate the best fitting probability distributions of changes given a body of linguistic data [16, 17]. In this way, they aim to provide something that isolated cases cannot—a way of making general claims about language change that are not limited to a particular place, time or dataset.

The first three perspectives—dynamic population-based, variationist, and social-cognitive—fit naturally within a single cultural evolutionary framework

which aims to understand changes in the use of linguistic variants in terms of two processes: (1) the continual generation of linguistic variation and (2) the selection of variants due to cognitive biases and social influences [18]. Probabilistic models coupled with empirical data provide one powerful tool for discriminating between the many claims about linguistic variation and selection that can be made within this framework.

# Using Models to Understand Change

Linguists have proposed numerous cognitive, linguistic, and social mechanisms that can influence the generation and propagation of linguistic variants (see boxes 2 and 3). This leaves open the question of which mechanisms are sufficient to explain observed changes, which mechanisms are most important and how different mechanisms interact. For example, are simple models of copying via social networks sufficient to account for the rate at which new dialects emerge? Does the well-established effect of word frequency on rates of change apply equally at diverse time frames ranging from decades to millennia? And do commonly observed features of language, such as word order and compositionality, require language-specific cognitive biases, or can they arise from general constraints on learning and cultural transmission? Recent work has addressed such questions by specifying them within formal models which can be compared to quantitative data to assess the plausibility of different explanations and to identify what kinds of mechanisms matter most for innovation and propagation (see box 4) [19, 20].

Baxter et al [16] recently followed this strategy to test a theory for newdialect formation advanced by Trudgill [21] for New Zealand English [22]. They specified an agent-based model assuming imitation of utterances from only a small set of acquaintances (rather than from the population at large). A model based on Trudgill’s theory, which assumed copying among individuals in a social network, could easily reproduce the new dialect’s composition. However, Baxter et al. also concluded that some selection mechanisms were needed to explain the rapid pace of convergence, thereby underscoring the important role of population structure in rates of change. Thus, by building simple models in an incremental fashion, researchers have begun to understand which of the myriad potential factors are most important in certain kinds of change.

In another study, Hare and Elman proposed a simple, network learning model to account for the well-established relationship between frequency of verb use and rates of morphological change. Their model successfully captured the gradual change in verb forms from Old English to Modern English, where rarely used forms were more likely to pass to the next generation with errors and also more likely to become regular. An important finding from this research was that general properties of network learning could account for the trajectory of verb forms, relaxing the need for language-specific constraints. More recently, researchers have developed methods for estimating rates of change over longer time periods, thus providing another source of data to assess claims about cognitive and social constraints on change [7].

It is important to note that most models emphasize only some aspects of the social-cognitive framework described above. However, they also serve as a starting point for building a complete picture of how cognition and social structure interact and shape the path of language change. We see agent-based modeling

- as one promising direction for integrating both cognition and social interaction, and thus understanding how specific assumptions about learning, social interaction, and speech production can account for common patterns of language use and change. For example, Daland et al. [23] proposed that mysteriously persistent conjugation gaps—i.e., the complete absence of the first-person present form for some Russian verbs—do not require special explanations in terms of cognitive constraints on grammar, but can rather be explained by a general model of sound-based analogical learning. The researchers specified a computational learning model in which the force of lexical analogy and the force of sound similarity could be systematically varied. They showed that under certain simple assumptions about learning, the gaps can arise and persist over time. Similar approaches have been applied to show, for example, (1) how a simple exemplar-based model of speech production and perception can account for common observations about sound change [9], (2) how compositionality in language can arise from repeated cycles in which learners acquire language from the productions of the previous generation of learners [24], and (3) how common constraints on word order follow naturally from simple models of learning and social interaction [25]. One criticism of such agent-based approaches is that they often account for qualitative observations but are not


explicitly fitted to data in a standard statistical framework. Nonetheless, they are important tools for exploring the implications of relatively complex arguments and for identifying those assumptions and details that are most crucial to reproduce observed phenomena. An important next step will be to develop models that are suitably complex to capture essential details of both cognition and social interaction, but that are simple enough to fit to quantitative data in a straightforward manner.

# Challenges and Future Directions

When studying language change, several recurring challenges arise that can benefit from interdisciplinary collaboration both within linguistics and across disciplines. As in other historical sciences, like archeology and paleontology, linguists must rely principally on artifacts—in this case, of speech—to make inferences about change. Linguists have developed a number of creative strategies to meet this challenge, but each is generally limited to a particular time scale. By comparing results from methods with resolution at different time scales—from decades, to centuries, to millennia—researchers will be in a better position to understand how the processes inferred at one time scale are consistent with those at another. Recent corroboration that frequency of word use influences rates of change across vastly different time scales is a case in point [26-29].

Another challenge is to develop models of language structure that account for variability in use and are suitably dynamic to permit learning and change over

time. This is also a central concern in more general models of categorization and perception in cognitive science. There is much to be learned about language change in particular by examining it in the light of these more general models (see box 1). For example, how can general exemplar models account for many aspects of language change that have in the past been construed as languagespecific [9]? In turn, these general models can also benefit from the richness and time depth of data available for language change in particular [26]. For example, historical data from the transition between Old and Modern English provided an important test of Hare and Elman’s model for past tense learning described above.

These and other challenges in understanding language change will best be met by linguists and cognitive scientists working together. To foster such collaboration in coming years, this paper has attempted to lay down a framework within which they might cooperate, and which integrates the dynamic, populationbased, variationist, social-cognitive, and data-driven modeling perspectives we describe (see figure 1). This work, in turn, should have implications for cognitive science more broadly. For the mechanisms that come together to influence change in language are the same cognitive, social, and cultural ones that likely play crucial roles in how language and culture are processed and acquired by the human mind [30].

Acknowledgments. We are grateful to Chris Wood, Ray Jackendoff, three anonymous reviewers, and the Editor for helpful comments on an earlier draft of this article, and to the Santa Fe Institute for funding the working group, Models of Innovation and Propagation in Language Change

# Outstanding Questions

- 1. How can language change contribute to the development of a generalized theory of selection that applies across all empirical phenomena that involve evolutionary processes? And how well does language provide a model system for cultural change in general?
- 2. Are the processes involved in language change and in the evolution of the language capacity of the same or different kinds?
- 3. How do novel languages arise from existing communicative structures, such as in emerging sign languages or creoles?
- 4. To what extent are innovation and propagation constrained by other prior structures in a language or by universal grammar-related biases?
- 5. What factors increase and decrease the speed of language change? Are these different at different levels of linguistic organization? What particular population size or community structure accelerates or decelerates it?
- 6. How much do assumptions about discreteness and continuity in change influence model predictions?
- 7. What is actually changing? Forms, functions, form-function mappings, rules, and/or exemplars?


- Box 1. Language Change and Cognitive Science. Work on language change is likely to contribute to key questions in cognitive science about what factors shape the acquisition and processing of language. In general terms, if some aspect of linguistic structure can emerge and change purely from constraints imposed by social interaction or from non-linguistic biases on cultural transmission, then this relaxes the need to posit specific, linguistic constraints to account for that structure. For example, computer simulations have shown how pairwise interactions within a population of agents can spur the emergence of a shared set of form-meaning mappings [31]. Other simulations have shown how non-linguistic biases on the processing of sequential information can give rise to word order regularities as consequence of cultural transmission across generations of learners [32], corroborating prior historicallinguistic analyses [29].


The framework described here also makes it possible to uncover biases in language acquisition and processing that would go unnoticed within standard cognitive science approaches to language. That is, some biases may be too weak to show up in conventional psycholinguistic experiments but can be observed when they become amplified across multiple generations of learners. Thus, whereas a recent standard psycholinguistic study found little evidence of regularization of inconsistent form-meaning mappings [33], a subsequent study employing iterated learning with human subjects showed that across generations of learners a clear pattern of regularization of ambiguous mappings emerged [34].

Related work has demonstrated that the iterated learning methodology can identify biases that go beyond language and apply to various types of learning relevant for cultural change more generally [35]. Such iterated learning experiments can be complemented by longer-term historical analyses, which may identify biases at much longer time frames [29].

Hence, observations about how languages change at a wide range of time scales have already begun to contribute to current debates about the underlying cognitive capacities for language. We also anticipate that the impact on cognitive science may be even broader as language provides a particularly welldocumented opportunity for investigating general processes of cultural change. A parallel research tradition in evolutionary anthropology deals with many of the same issues in culture change and has developed models and empirical techniques for testing competing theories about cognitive and social biases in transmission [36-40]. A rapprochement between these two traditions will likely provide new insights into the commonalities between culture change in general and language change in particular.

- Box 2. What Generates Variation? Linguistic forms and their functions can change in numerous ways. Every time we use the “same” form, there are small, but possibly consequential differences in the exact sounds we use and how people interpret them [9, 41]. Moreover, an utterance often leaves room for interpretation in how it was composed and what it means. For example, the word newt in English is derived from ewt, likely a result of people interpreting and reproducing an ewt as a newt. This is only one very simple example of formfunction re-analysis by which ambiguity leaves room for change [5, 13]. One thoroughly studied process of change in form-function mapping is grammaticalization whereby a construction can lose its concrete meaning for an abstract, grammatical function. One common example is the evolution of going somewhere to do something, originally to express a goal, to mean to intend on doing something and finally to mean the FUTURE of doing something. The form frequently used for INTENDING and the FUTURE has also phonologically eroded to gonna VERB [42]. There are many open questions about how these and other innovations emerge. How frequently do such innovations arise in everyday speech? How do cultural factors influence the tempo and nature of innovations? What specific evolutionary trajectories do they follow? And under what conditions do innovations occur gradually, by small successive extensions, or abruptly in large discrete steps? This last question is of particular importance because system dynamics may depend on the relative discreteness or continuity of changes [40]. A more fundamental question is what we mean by saying two or more forms, constructions or meanings are variants of each other. For example,


- at what point do [w t r] and [w D r] constitute different forms? And how do we decide whether I’m going to finish the project and I will finish the project have precisely the same meaning? Answers to these various questions about rate and variation will require estimates of how frequently new variants arise at the individual and population level and ways of measuring “how different” variants are from one another both in terms of the linguistic content they express, and how they are produced and perceived.


- Box 3. What Influences Selection and Propagation? Propagation is the spread of forms or constructions within a population, when some speakers re-use what others have innovated or used before. We can observe propagation at the population level, such as one dramatic change in the recent history of English: the spread of the quotative be like (as in I’m like, “no way!’) [43]. We can also observe the effects of propagation in the utterances of an individual —as with the 50-year evolution of Queen Elizabeth's vowel production toward community-wide shifts [44, see also 45]. Many factors can plausibly influence the rate and success with which novel form-function mappings spread through populations. For example, speakers’ choices of a specific construction can depend on several cognitive factors, including learnability, ease of use, or expressivity of the construction [25]. The structure of a language itself can also bias the use of one variant over another. For example, if nouns and verbs in a specific language have different sound structures, then individuals may be more inclined to adopt a noun variant that sounds noun-typical [46]. And when there are no markings to tell “who-does-what-to-whom,” people may adopt stricter word order as another way to communicate this distinction [47]. Finally, social factors and population structure can also guide how and when people adopt specific variants. Prestige and status can affect which variants people adopt [48], and in cases of language contact, population structure can determine who copies from whom under what particular conditions [13]. Historical linguistics, meanwhile, focuses on how the splitting and merging of speech communities over time has lead to the current distribution of linguistic variants within and between languages [49]. Much recent work reverses


this cause-and-effect connection to infer past migrations and population divergence from the distribution of linguistic variants [50, 51]. It is important to note that these same cognitive and social factors may also play a role in the generation of variation and new form-function mappings, thus making it difficult to disentangle innovation from propagation and selection.

- Box 4. Testing Quantitative Models of Change. A promising trend in studies of language change is the specification and testing of quantitative models—often based on general models of cognition and social dynamics—against observational or experimental data to discriminate differing theories. A fruitful starting point for such models is the specification of a random or null model based on simple assumptions about how innovations arise and are transmitted in a population [16, 48]. An initial null model may simply involve a constant rate of innovation and random copying from other individuals in a population. It is not clear that this approach can fully explain any historical language change. Nevertheless, similar approaches applied to other complex phenomena, such as cultural change [52], ecological diversity [53], and genetics [54], have provided important insights about when selection or other mechanisms need to be invoked as explanations for change or patterns of diversity.


In many cases, relatively simple models of language learning and change can replicate observations from experiments and population-based studies. The iterated learning model [24], for instance, proposes that some language structures—for example compositionality—arise naturally as cognitive constraints favor some linguistic forms over others during cultural transmission. Recent experiments that involve chains of production and learning have verified this prediction [55]. Exemplar-based models and neural net models borrowed from cognitive science can replicate many observed facts about language learning and change, and have been tested against both experimental and observational data [9, 10, 26, 56]. And researchers have begun to test different models of

propagation based on developmental differences in learning and population structure [16, 43, 48]. By starting with simple, explicit models and applying them to rich linguistic datasets, researchers have set out to identify which assumptions are sufficient to account for patterns of diversity and change and which apparently important assumptions are not.

# Glossary

Construction. Conventionalized mappings between form and function at the word, phrase or sentence level [57]. Constructions extend the form-function relationship from morphemes (-ed meaning the past) to single words (mouse meaning a small rodent) to complex multi-word generalizations (such as ‘the Xer the Yer’ that can be instantiated, e.g., as ‘the stronger the better’).

Creole. Creoles have traditionally been defined as pidgins that acquired native speakers and expanded their functions and structures accordingly. However, current research disputes this position, citing lack of evidence to support the creolization-by-nativization claim. Instead, creoles are now defined by some experts as new varieties of European languages that emerged in the 18th and 19th centuries in plantation settlement colonies where African slave populations became the overwhelming demographic majorities [4, 13]. It is still debatable whether the term creole can be extended to varieties of non-European languages that have evolved similar structures under similar contact conditions—such as Nicaraguan Sign Language [58].

Exemplar. A specific instance of an utterance or observation that is stored in memory, and used as a benchmark for interpreting and producing utterances in the future.

Form-Function Re-analysis. Change that occurs when individuals vary in their interpretation of linguistic forms. Such re-analysis of constructions can occur at all levels of linguistic production.

Grammaticalization. The process by which a lexical item or sequence of lexical items acquires a grammatical function. The development of ‘gonna’ (signaling future time reference) out of ‘be going to’ (which originally only indicated movement in space) is an example of grammaticalization.

Historical Linguistics. The study of language(s) through time: both the general mechanisms by which language changes, and how different changes to the same original language can lead it to diverge into a family of related languages. Applied to synchronic comparative data on specific languages, such knowledge can reconstruct their common ancestral stages, classify them into families by degree of relatedness, and make inferences as to the prehistories of the populations that spoke them (ancestry, expansions, separations, relative chronologies, etc.).

Iterated learning. A kind of cultural transmission whereby specific patterns of behavior emerge through repeated cycles of production, observation and learning across generations of learners. Linguistic transmission is one example of iterated learning.

Language Change. The manner in which the phonetic, morphological, semantic, syntactic, and other features of a language arise, vary and fall out of use over time.

Language Evolution. (1) The emergence of language in the human lineage by way of biological and/or cultural evolution, (2) A view of processes of change and divergence of language lineages based on parallels with speciation and/or population histories. The second approach has applied evolutionary models from the biological sciences to comparative-historical language data to compute likely trees of descent and to draw inferences about the histories of speech communities.

Lexical Replacement. The shift in the probability of one form being used for a function in favor of another form, such that the dominance of the two forms is switched.

Model selection. The task of deciding which of a set of competing models best fits the available data. Quantitative methods include fitting measurable quantities to mathematical predictions by adjusting parameters, or choosing the model that generates the observed data with the maximum likelihood. One may also employ other criteria, such as parsimony (i.e., out of two equally successful models, choosing that with the fewer assumptions). Information criteria, such as Akaike

Information Criteria or Bayesian Information Criteria, are often used in biology and ecology to compare competing models [59].

Morphosyntax. Loosely, the overlap between morphology and syntax, i.e. respectively: how minimal units of meaning (morphemes) are structured within a word; and how word units are meaningfully structured in a sentence. Morphosyntax covers the same grammatical functions performed in some types of language by morphology, in others by syntax: e.g. the subject/object distinction shown by either case affixes (inflectional morphology) or relative word order (syntax).

Neutral Evolution. Change in the system that is the result of random fluctuation of frequencies of variants, in the absence of selection. If a variant fluctuates to zero, it has become extinct and the system has changed. If a variant fluctuates to invade an entire population, it has spread to fixation.

Null model. In this context, a model with a restricted set of mechanisms. Incompatibility of observed data with the null model may provide evidence for additional mechanisms playing a role in generating the data.

Phonological Erosion. Change to the phonological structure of a word, which involves for example, the simplification of diphthongs or indeed the complete loss of particular sounds.

Population Structure. Patterns in the frequency and nature of interactions between members of a population, for example, an increased tendency for one pair of speakers to interact compared to another pair of speakers. Typically represented graphically as a network indicating those individuals that are most likely to interact.

Replicator. A particular linguistic structure in a language that can be propagated in a population or go extinct. Called 'lingueme' in Ref. [5].

Selection. In evolutionary dynamics, the set of processes and mechanisms that combine so that some replicators produce more copies of themselves on average than others, whether or not these offspring are identical or altered copies of their parents.

Sociolinguistics (variationist). The study of linguistic variability inherent in speech and its quantitative correlates with elements of the linguistic and social structure as well as with language change.

Table 1. Linguistic Subfields and Related Methods of Studying Change Subfield Example of Method Psycholinguistics Study variation in how people speak and hear linguistic forms in

tightly controlled laboratory settings [9].

Sociolinguistics Study speech of living populations, detecting potential changes in form and meaning from generational differences in the use of sounds, words, and grammatical structures [60]. They may test these inferences with longitudinal data, sometimes spanning several centuries [61].

Creolistics Study how competition among inputs from both colonizing and substrate languages leads to the emergence of novel language varieties in colonial contexts [4, 13].

Historical Linguistics

Linguistic Typology

Study change over much longer time depths. By making controlled comparisons between languages whose speech communities have descended from a common ancestor, they can infer which changes have most likely led to the observed diversity in forms [50].

Study correlations between different kinds of grammatical structures in a wide range of languages, to understand how one kind of structure can influence another [62].

Figure 1. Perspectives that contribute to an understanding of language change. Although partial insights can be gained individually from each of these perspectives, complete understanding of the processes involved in language

## change will require integrating explanations across them.

Variationist

Populationbased

Understanding Language Change

Cognitive

Data-based Modeling

Social

# References

- 1. Christiansen, M.H., and Chater, N. (2008) Language as shaped by the brain. Behavioral and Brain Sciences 31, 489-509
- 2. Tomasello, M. (2008) The Origins of Human Communication. The MIT Press
- 3. Keller, R. (1994) On Language Change: the Invisible Hand of Change. Routledge
- 4. Mufwene, S.S. (2001) The Ecology of Language Evolution. Cambridge University Press
- 5. Croft, W. (2000) Explaining Language Change: An Evolutionary Approach. Pearson Education Limited
- 6. Griffiths, T.L., et al. (2008) Theoretical and empirical evidence for the impact of inductive biases in cultural evolution. Philosophical Transactions of the Royal Society (B) 363, 3503-3514
- 7. Pagel, M. (2009) Human language as a culturally transmitted replicator. Nature Reviews: Genetics 10, 405-415
- 8. Poplack, S., and Tagliamonte, S. (1999) The grammaticization of going to in (African American) English. Language Variation and Change 11, 315-342
- 9. Pierrehumbert, J. (2001) Exemplar dynamics: word frequency, lenition and contrast. In Frequency and the Emergence of Linguistic Structure, 137-158, John Benjamins


- 10. Bybee, J. (2006) From usage to grammar: the mind's response to repetition. Language 82, 711-733
- 11. Weinreich, U., et al. (1968) Empirical Foundations for a Theory of Language Change. In Directions for Historical Linguistics (Lehmann, W.P., and Malkiel, Y., eds), 95-195, University of Texas Press
- 12. Hay, J., and Bauer, L. (2007) Phoneme inventory size and population size. Language 83, 388-400
- 13. Mufwene, S.S. (2008) Language Evolution: Contact, Competition, and Change. Continuum Press
- 14. Goldstone, R.L., and Janssen, M. (in press) Computational models of collective behavior. Trends in Cognitive Sciences
- 15. Labov, W. (1972) Sociolinguistic patterns. University of Pennsylvania Press
- 16. Baxter, G.J., et al. (2009) Modeling language change: an evaluation of Trudgill's theory of the emergence of New Zealand English. Language Variation and Change 21, 257-296
- 17. McMahon, A., et al. (2007) The sound patterns of Englishes: representing phonetic similarity. English Language and Linguistics 11, 113-142
- 18. Croft, W. (2008) Evolutionary linguistics. Annual Review of Anthropology 37, 219-234
- 19. Pierrehumbert, J. (2006) The next toolkit. Journal of Phonetics 34, 516530


- 20. Niyogi, P. (2006) The Computational Nature of Language Learning and Evolution. MIT Press
- 21. Trudgill, P. (2004) New-dialect Formation: The Inevitability of Colonial Englishes. Edinburgh University Press
- 22. Gordon, E., et al. (2004) New Zealand English: Its Origins and Evolution. Cambridge University Press
- 23. Daland, R., et al. (2007) Much ado about nothing: a social network model of Russian paradigmatic gaps. Proceedings of the 45th Annual Meeting of the Association for Computational Linguistics, 936-943
- 24. Smith, K., et al. (2003) Iterated learning: a framework for the emergence of language. Artificial Life 9, 371-386
- 25. Clark, B., et al. (2008) Language change as a source of word order generalizations. In Variation, Selection, Development: Probing the Evolutionary Model of Language Change (Eckardt, R., et al., eds), 75-102, Mouton de Gruyter
- 26. Hare, M., and Elman, J.L. (1995) Learning and morphological change. Cognition 56, 61-98
- 27. Poplack, S., and Malvar, E. (2007) Elucidating the transition period in linguistic change. Probus 19, 121-169
- 28. Pagel, M., et al. (2007) Frequency of word-use predicts rates of lexical evolution throughout Indo-European history. Nature 449, 717-721
- 29. Bybee, J.L. (2007) Frequency of Use and the Organization of Language. Oxford University Press


- 30. Chater, N., and Christiansen, M.H. (in press) Language acquisition meets language evolution. Cognitive Science DOI: 111/j.1551-6709.2009.01049.x
- 31. Puglisi, A., et al. (2008) Cultural route to the emergence of linguistic categories. Proceedings of the National Academy of Sciences 105, 7936-7940
- 32. Reali, F., and Christiansen, M.H. (2009) Sequential learning and the interaction between biological and linguistic adaptation in language evolution. Interaction Studies 10, 5-30
- 33. Vouloumanos, A. (2008) Fine-grained sensitivity to statistical information in adult word learning. Cognition 107, 729-742
- 34. Reali, F., and Griffiths, T.L. (2009) The evolution of linguistic frequency distribution: relating regularization to inductive biases through iterated learning. Cognition 111, 317-328
- 35. Kalish, M.L., et al. (2007) Iterated learning: Intergenerational knowledge transmission reveals inductive biases. Psychonomic Bulletin and Review 14, 288-294
- 36. Henrich, J., and McElreath, R. (2003) The evolution of cultural evolution. Evolutionary Anthropology 12, 123-135
- 37. McElreath, R., et al. (2008) Beyond existence and aiming outside the laboratory: estimating frequency-dependent and payoff-biased social learning strategies. Philosophical Transactions of the Royal Society (B) 363, 3515-3528
- 38. Boyd, R., and Richerson, P.J. (2005) The Origin and Evolution of Cultures. Oxford University


- 39. Mesoudi, A., and Whiten, A. (2008) The multiple roles of cultural transmission experiments in understanding human cultural evolution. Philosophical Transactions of the Royal Society (B) 363, 3489-3501
- 40. Goldstone, R.L., and Janssen, M. (2005) Computational models of collective behavior. Trends in Cognitive Sciences 9, 424-430
- 41. Ohala, J.J. (1981) The listener as a source of sound change. In Papers from the Parasession on Language and Behavior (Masek, C.S., et al., eds), 178203, Chicago Linguistics Society
- 42. Hopper, P.J., and Traugott, E.C. (2003) Grammaticalization. Cambridge University Press
- 43. Tagliamonte, S.A., and D'Arcy, A. (2009) Peaks beyond phonology: adolescence, incrementation, and language change. Language 85, 48-108
- 44. Harrington, J. (2006) An acoustic analysis of 'happy-tensing' in the Queen's Christmas broadcasts. Journal of Phonetics 34, 439-457
- 45. Sankoff, G., and Blondeau (2008) Language change across the lifespan: /r/ in Montreal French. Language 83, 560-588
- 46. Farmer, T.A., et al. (2006) Phonological typicality influences on-line sentence comprehension. Proceedings of the National Academy of Sciences 103, 12203-12208
- 47. Mondloch, J. (1978) Disambiguating subjects and objects in Quiché. Journal of Mayan Linguistics 1, 3-19
- 48. Labov, W. (2001) Principles of Linguistic Change. Volume II: Social Factors. Blackwell


- 49. Heggarty, P., et al. (in press) Splits or waves? Trees or webs? How divergence measures and network analysis can unravel language histories. Philosophical Transactions of the Royal Society (B)
- 50. Heggarty, P. (2007) Linguistics for archaeologists: principles, methods and the case of the Incas. Cambridge Archaeological Journal 17, 311-340
- 51. Gray, R.D., et al. (2009) Language phylogenies reveal expansion pulses and pauses in Pacific settlement. Science 323, 479-483
- 52. Bentley, R.A., et al. (2004) Random drift and culture change. Proceedings of the Royal Society B: Biological Sciences 271, 1443-1450
- 53. Hubbell, S.P. (2001) The unified neutral theory of biodiversity and biogeography. Princeton University Press
- 54. Kimura, M. (1983) The neutral theory of molecular evolution. Cambridge University Press
- 55. Kirby, S., et al. (2008) Cumulative cultural evolution in the laboratory: an experimental approach to the origins of structure in human language. Proceedings of the National Academy of Sciences 105, 10681-10686
- 56. Bybee, J. (2001) Phonology and Language Use. Cambridge University Press
- 57. Goldberg, A.E. (2003) Constructions: a new theoretical approach to language change. Trends in Cognitive Sciences 7, 219-224
- 58. Siegel, J. (2008) The Emergence of Pidgin and Creole Languages. Oxfrod University Press


- 59. Burnham, K.P., and Anderson, D.R. (2002) Model Selection and and Multimodel Inference: a Practical Information-Theoretic Approach. SpringerVerlag
- 60. Labov, W. (1963) The social motivation of a sound change. Word 19, 273309
- 61. Poplack, S., and Dion, N. (in press) Prescription vs. praxis: the evolution of future temporal reference in French. Language
- 62. Croft, W. (2003) Typology and Universals. Cambridge


