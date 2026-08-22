You are the final adversarial adjudicator of two reviews of a formal linguistic
theory. The attached bundle contains the underlying paper, Lean and JavaScript
artifacts, the handoff specification, the first Claude review, and a later
Codex second opinion. Do not assume either review is right. Attempt refutation
first and recompute all important claims from the sources.

Audience: the paper's author, deciding which findings and repairs to trust.

Tasks:

1. Adjudicate the nine numbered findings in `01-claude-review.md` using exactly
   CONFIRM / REFUTE / WEAKEN / STRENGTHEN. Give a one-line basis and exact
   source lines for each, followed by prose for every refuted or reweighted
   item.
2. Independently adjudicate every major additional claim in
   `formalization-second-opinion-codex-20260821.md`, especially:
   - the outside-option normalization counterexample;
   - alleged double discounting;
   - the relation between the bounded-memory Beta filter and the cubic;
   - whether `psi_rep` can be treated as fixed;
   - whether the joint likelihood is genuinely shared-latent;
   - missing multi-node posterior dynamics;
   - the agreement-rate licensing interpretation;
   - the projectibility and maintenance/control verdict.
3. Report important defects both reviews missed.
4. Judge both recommended repair orders. Identify fixes that would erase a
   valuable distinction, introduce circularity, or solve the wrong problem.
5. State what Lean and JavaScript can and cannot verify here.

Rules:

- Ground every substantive claim with exact bundled file and line references.
- Recompute equations and give explicit counterexamples when possible.
- Distinguish falsehood, ambiguity, underived approximation, scope limitation,
  documentation overclaim, and optional strengthening.
- If an alleged defect can be repaired by a charitable reading, say exactly
  what assumptions that reading requires and whether the text states them.
- If you claim an absent transition, law, link, or definition, report the terms
  you looked for in the supplied sources.
- Do not let agreement between the two reviews count as evidence.
- Preserve strengths and disagreements; do not manufacture a consensus.
- Do not rely on outside literature or undocumented facts.

Output, in at most 6,500 words:

1. overall verdict on the two reviews;
2. the required Findings 1-9 adjudication table;
3. detailed reweighting/refutations;
4. a ranked table adjudicating the Codex review's additional findings;
5. missed findings;
6. verdict on projectibility, warrant, and world-side commitment;
7. final ordered repair plan;
8. verification limits.

