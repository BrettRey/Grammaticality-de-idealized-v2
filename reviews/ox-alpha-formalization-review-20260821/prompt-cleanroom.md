You are an independent expert reviewer of a formal linguistic theory and its
supporting Lean and JavaScript artifacts. The attached source bundle is the
artifact under review. You have not been given any prior diagnosis or review.

Audience: the paper's author, deciding what must be repaired before the formal
apparatus can bear publication-level claims.

Read every relevant source in the bundle. Review the formal apparatus rather
than the paper's general literary quality. Attempt to refute apparent defects
before accepting them. Work through equations and construct small numerical or
logical counterexamples where useful.

Audit these interfaces independently:

1. internal mathematical correctness and exactness of displayed identities;
2. separation of ontic population state, speaker state, learner/analyst belief,
   and subjective read-out;
3. whether stated dynamics actually evolve the variables and levels claimed;
4. fidelity between paper, Lean scaffold, quantitative contract, simulator,
   engine, and joint likelihood;
5. whether the Lean theorems establish the advertised consequences rather than
   merely unfold definitions;
6. whether executable components share the latent variables the documentation
   says they share;
7. projectibility: declaration, non-trivial projection, warrant, world-side
   commitment, stability versus maintenance versus corrective control, bearer,
   scope, prospective revision, and conclusion;
8. whether empirical indicators identify licensing rather than selection,
   opportunity, or read-out effects.

Rules:

- Ground every substantive claim with exact bundled file and line references.
- Distinguish a false statement, an underived approximation, an omitted model
  component, a deliberate scope restriction, and an optional strengthening.
- If you say something is absent, report the terms or definitions you looked
  for in the supplied sources.
- Treat comments and README claims as claims to audit, not as guarantees.
- Do not claim that successful compilation proves paper-to-Lean fidelity.
- Do not appeal to outside literature unless merely flagging a claim for later
  verification.
- Preserve genuine strengths and explain why they survive the defects.
- Do not propose internal record fields merely because an index exists in the
  paper; distinguish the domain of an indexed function from its codomain.

Output, in at most 6,500 words:

1. overall verdict and the two or three most consequential reasons;
2. genuine strengths;
3. ranked findings with severity and classification
   (formal error / interface failure / scope limitation / overclaim / optional
   strengthening), including any counterexamples;
4. a ten-row projectibility/support-grade audit;
5. the strongest world-side commitment actually warranted;
6. an ordered repair plan, identifying any tempting but harmful fixes;
7. a verification-limits section.

