# Project Notes

---

## ⚠️ PRIORITY: Rachell Powell Connection ⚠️

**Status:** NOT STARTED (Jan 26, 2026)

Rachell Powell (BU Philosophy) - *Contingency and Convergence* (MIT Press 2020)

**Why this matters:**
- Powell's contingency/convergence framework maps onto the OVMG project
- Operators as *convergent* solutions to coordination problems (like eyes, wings)
- Morphosyntactic realization as *contingent* (language-specific implementation)
- Her "deep vs shallow replay" distinction: grammatical categories contingent at origin but convergent given cognitive/social constraints

**Questions Powell would ask:**
1. What *mechanism* drives convergence toward closed-paradigm operators?
2. Does OVMG tell us about evolution of linguistic cognition, not just structure?

**Sub-project connections:** Grammar_and_emergence, Labels_to_Stabilisers, TFRs

**Profile:** https://www.bu.edu/philo/profile/rachell-powell/

**Delete this section once explored.**

---

## Bottom-Up Norm Enforcement (Corrected Attribution)

**Added:** 2026-01-27
**Corrected:** 2026-01-28
**Actual source:** Richerson & Boyd (2005) *Not by Genes Alone*, ch. 6; O'Connor (2019) *Origins of Unfairness*, ch. 4

~~Powell observes that social insects enforce norms bottom-up~~ **Correction:** Powell's *Contingency and Convergence* does not discuss social insects or norm enforcement. The book is about biological evolution (eyes, brains, body plans).

**What the sources actually say:**
- **Richerson & Boyd (2005):** Human cooperation in large groups is maintained by *moralistic punishment* -- "If everyone punishes deviants, *any* norm can become stable." This is distributed, not top-down. Ants/bees are mentioned as a CONTRAST: they cooperate via kin selection (siblings), not cultural norms.
- **O'Connor (2019):** Deviation from conventions is penalized via "gossip, ostracism, open criticism, and sometimes more serious forms of punishment" (p. 67).

**The valid connection to OVMG:** C_t (community licensing) emerges from distributed speaker interactions, not central decree. Every local reaction to usage aggregates into community-level norms. This parallels Richerson & Boyd's moralistic punishment mechanism. The insect comparison would be an *analogy* one could draw (emergent colony-level behavior from local interactions), not a direct claim from the sources.

**Implications (still valid):**
1. C_t isn't a sociological add-on -- bottom-up norm enforcement is the mechanism
2. Counters the "grammar police" caricature: enforcement is distributed, not top-down
3. Supported by cultural evolution literature (Boyd & Richerson, O'Connor)

**Where it belongs:**
- **Etiological account paper** (Module 2): Coordination equilibria sustained by distributed moralistic punishment
- **HPC book**: HPC kinds maintained by distributed mechanisms
- **Grammar_and_emergence** (Nefdt): Bottom-up emergence. (But NO LLMs on that project.)

---

## ⚠️ PRIORITY: Integrate Operator Stratum Paper ⚠️

**Status:** NOT STARTED (Jan 25, 2026)
**Source:** `subprojects/operator-stratum/Reynolds_Operator_Stratum.pdf` (uploaded to lingbuzz)

The CxG section (~line 1144 in main.tex) claims morphosyntax is "uniquely privileged" but doesn't explain WHY. The operator stratum paper provides the answer.

### What to add:

1. **refs.bib**: Add Reynolds 2026 citation for operator stratum paper

2. **main.tex CxG section**: Explain WHY morphosyntax is special:
   - Morphosyntactic form-value relations serve as **operators**
   - Operators = closed-paradigm contrasts that configure public update, allocate participant roles, constrain uptake
   - Information-theoretic: operators are header-like (few bits, large downstream entropy reduction)

3. **Consider adding** the three-stratum distinction:
   - Expression-shape ("not a word")
   - Operator ("can't say that")
   - Payload (negotiation)

### Key quote from stratum paper:
> Operators configure how utterances update shared commitments, allocate participant roles, and constrain uptake.

**Delete this section once integration is complete.**

---

## External Feedback

### Jong-Bok Kim (Dec 2025) - On licensing vs gradience

Kim (SBCG/HPSG theorist, Kyung Hee University) responded to questions about formal grammar and grammaticality:

> "The licensing-based theory, to my knowledge, has no clear distinction between well-formed ones and those with ? or ??, thus not clear about gradience. The grammar would accept all such, while not licensing * sentences. As for the grammaticalization, this would then imply that the grammar would license all the diachronic developments."

**Relevance to MVMG:** This is exactly the gap your model addresses:
- Discrete licensing captures * vs. not-*, but nothing in between
- The MVMG's F(u) function models gradient acceptability
- Kim's admission from within the formal tradition supports the claim that formal grammars need something like MVMG to capture judgment patterns

**Full correspondence:** See `HPC book/correspondence/kim-jongbok-2025-12.md`

### Related: Transparent Free Relatives (`Transparent_free_relatives/`)

Kim proposed collaboration on TFRs (Dec 27). TFRs may show **gradient acceptability** based on internal/external feature match:
- Perfect match → fully acceptable
- Partial match → marginal
- Mismatch → degraded

This could be empirical evidence for the MVMG-style gradient grammaticality model -- TFRs as a test case for F(u) predictions.

---

*Notes file created Dec 27, 2025*
