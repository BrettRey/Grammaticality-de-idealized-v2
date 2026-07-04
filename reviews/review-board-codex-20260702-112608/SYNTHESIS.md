# Codex review board — synthesis — 2026-07-02

Five Codex reviewers (codex-cli 0.142.4), one process per persona, read-only, on the current `main.tex` (1770 lines, post section-by-section revision). Verbatim reviews in `codex-*.md`.

**Verdicts: 4 Revise & Resubmit, 1 Accept.** The Accept is the Projectibility reviewer, on the specific ground that projectibility is now load-bearing. The four R&Rs all target the formal *identification* machinery, not the framing.

This is a redundant board to the earlier Fable/Opus board (`review-board-2026-07-01.md`). The cross-model comparison is the most useful output: what both boards flag independently is very likely real.

## Consensus strengths (Codex)

1. **Projectibility-first spine is genuinely load-bearing** (all five; Projectibility reviewer's audit is all-GREEN, Philosopher's HPC check confirms "structurally real, not decorative"). The fix landed.
2. **Mean-vs-concentration distinction** (`whose` vs LBE: same low mean, different posterior concentration → different satiation/framing predictions) is named the best technical move by four reviewers. This is exactly the posterior-state fix from the last round; the earlier board asked for it, this board praises it.
3. **Status/feeling two-layer split** (conventional `C_t`/`G_t` vs subjective `F`, ratings as evidence not definition) — Generative, UBA, Philosopher.
4. **`p_t = N_t·ρ*` opportunity/preemption formalization** — Methodologist, Philosopher, UBA.
5. **The UBA credit paragraph is candid and fair** (UBA reviewer specifically praises the crediting of Schmid/Croft/Stefanowitsch/Goldberg/Ambridge). Validates last round's recalibration.

## Consensus weaknesses, ranked

1. **Identifiability: `C_t` vs `ρ*` (the product problem).** Corpus-rate-per-opportunity ≈ `C_t·ρ*`; `ρ*` must be independently normed *before* touching licensing evidence or the product is underidentified. Pre-registration "helps but is not yet a statistical identification strategy." Raised by Methodologist, Generative, Projectibility, Philosopher — three of their Q&A questions are this. **Also the #1 finding of the earlier board. Confirmed across two model families.**
2. **LBE / partial-pooling.** The convex sum `C_t(u,c)=Σλ_g C_t(g,c)` should let LBE inherit licensing from wh-fronting, question-formation, modifier–noun packaging. The credit-assignment asymmetry added last round (negative evidence concentrates on the most-specific node) "helps, but only if the LBE-specific node is independently required and given near-gating weight." Generative (sharp), Projectibility, Philosopher. **Also raised by the earlier board; the fix is acknowledged but judged not yet independently motivated.**
3. **`K`/`C_t` boundary not a clean decomposition.** Since the paper concedes `K` is partly derivative of licensing facts, `map·K·C_t` needs a dependency graph / temporal anchoring (operator inventory first, licensing second) and pre-judgment criteria for assigning a failure to `map`, `K`, or `C_t` (*I've finished it yesterday* = K vs *I have 25 years* = C_t needs principled diagnostics). Generative, Philosopher. **Also raised by the earlier board.**
4. **`τ(c)` ontology.** What fixes `τ(c)` independently of the community responses it predicts? If nothing does, "objective conventional status" deflates to a decision rule on a response-dependent state. The threshold-reality (RD) test helps but the recipe for estimating `τ(c)` independently needs sharpening. Philosopher, Projectibility.
5. **Operator not self-contained.** "operator" fixes the scope of `K`, the categoricality prediction, and the Turkish appendix, yet is deferred to the companion paper. Needs an in-text operator / non-operator / borderline diagnostic table with predictions that differ from "closed-class," "grammaticalized," "high-frequency." UBA (sharp): "What empirical result would force you to abandon the operator stratum rather than reclassify after the fact?"
6. **`whose`/COCA and AGR evidence under-reported.** (a) Internal tension: "uncertainty not rejection" (tiny opportunity set) vs "dramatically rarer than expected given components" (which reads as significant absence/preemption) — the two framings of `whose` pull opposite ways and must be reconciled with one shared denominator (query strings, opportunity definition, expected-rate model, upper bound, counted-opportunity examples). (b) The AGR figure needs an auditable in-text table (exact cells, counts, filtering exclusions, corpus version/date, the rival baseline beaten). UBA.

## Smaller / newer items

- **Grodner & Gibson "59–73%" — web-verified by the Methodologist reviewer.** 59% is Exp 1; 72.9% is Exp 2 *regional means*; much lower with item-specific variance. Defensible only if restricted to collapsed region-level analyses. The text currently says "59–73% of variance in reading times" without that caveat. (This matches the parent agent's own PDF check last round.) **Actionable now.**
- **`logit(C_t)` at boundaries.** Fine under finite Beta updating (never literal 0/1), but the prose/table assert boundary values; say explicitly "near-boundary, not literal." Methodologist. (F ∈ (−1,0] now judged mathematically fine; logistic-vs-hyperbolic mostly handled by the mean-field note.)
- **§2.16 Mechanisms of change reverts to a catalogue** (semantic/social/structural/iconic) without saying what each predicts about repair/transmission/actuation. Projectibility reviewer wants it tied to projection. (Parent kept this as narrative last round; this is a projectibility-consistency nudge.)
- **Relationship subsections compare coverage more than distinctive predictions** in places. Philosopher (YELLOW), echoing the earlier board.

## Contradiction worth preserving

The verdict split is informative, not noise: **the reframing is judged done (Accept on projectibility grounds), while the formal identification is judged not done (four R&Rs on `ρ*`/`τ(c)`/pooling/`K`-`C_t`).** Don't smooth this into a single "R&R" — it says precisely which half of the paper is finished.

## Review-board self-check

Convergence on identifiability is partly prompt-induced (the Methodologist was seeded with that probe), but the Generative and Projectibility reviewers reached the `ρ*`/`τ(c)`-independence problem from un-seeded angles (LBE niche definition, threshold estimation). More importantly, it matches the earlier independent Fable/Opus board — cross-model agreement across two model families is the strongest signal on the board. The Projectibility Accept is real dissent and should not be averaged away.

## What both boards agree the paper still needs (highest confidence)

1. An independent estimation procedure for `ρ*` (and `τ(c)`), pre-committed, so projective successes aren't retro-fitted.
2. Independent motivation for why preemption mass concentrates on an LBE-specific node rather than the convex sum licensing LBE through its parents.
3. Pre-judgment diagnostics for `map` vs `K` vs `C_t` assignment (and a dependency ordering, since `K` leans on licensing).
