# Decisions Log

Append-only record of project decisions. Agents: add an entry whenever a non-trivial decision is made during a session (structural changes, venue choices, theoretical commitments, scope changes, reviewer feedback acted on). Keep entries short.

Format: `## YYYY-MM-DD` then bullet points with **bold topic** and brief rationale.

---

2026-04-25 — Reading note: Kuribayashi, Warstadt, Oseki & Wilcox (2026), "Dual Alignment Between Language Model Layers and Human Sentence Processing" (arXiv 2604.18563v1). They test 19 open LMs (GPT-2, OPT, Pythia) against Huang et al. (2024) syntactic ambiguity reading-time data. Every layer of every model underestimates the human reading-time slowdown at the disambiguation point of garden-path and other ambiguous constructions. Earlier layers help with naturalistic reading; later layers help (somewhat) with ambiguity processing; nothing handles both. Their interpretation: humans have a reanalysis stage that LMs lack. For "grammaticality de-idealized," this is direct evidence that the cognitive cost of structure-violating sentences resists reduction to surprisal even when surprisal comes from contextually rich layers. The idealisation that probabilistic prediction tracks grammaticality breaks down precisely at the cases the trade book wants to centre. When next touching, consider citing as a clean empirical handle on the gap between predictability and processing cost.

2026-05-31 — Root `STATUS.md` created to repair portfolio tracking coverage. This is a PM-level tracking fix only: it records the OVMG subproject map, open theoretical threads, and known dirty-state watchpoints without changing manuscript source or resolving provenance.

## 2026-06-02

- **Operator-stratum is the bridge across the grammaticality family.** Next substantive OVMG work should stop treating the operator paper as only "why morphosyntax is special." Its broader role is to define the projectible target of grammaticality judgments: operator value, a closed public-update repertoire with repair/accountability consequences.
- **The grammaticality variables should be read through operator value.** Use `map` for operator viability, `K` for operator-value coherence, and `C_t` for licensed/entrenched operator value under opportunity and preemption. This keeps the asterisk, etiology, feeling, Miller, LBC, and Varieties projects aligned.
- **Target *Functions of Language* for the operator-stratum paper.** The paper's functional, typological, prosodic, and interactional framing fits FoL better than broader or more formal venues; the submitted version should foreground public-update operators rather than the earlier "coordination account" subtitle.

## 2026-06-07

- **Create evolutionary DAG workbench as a new subproject.** Scaffolded `subprojects/evolutionary-dag-workbench/` as a non-commitment workspace for generating, mutating, attacking, scoring, and archiving rival conceptual DAGs about grammaticality.
- **Use existing grammaticality work as seeds, not conclusions.** OVMG equations, detector architecture, operator-value claims, and grammaticality-as-kind claims can seed graph families and counterexamples, but the workbench is not required to vindicate them.
- **Keep submitted and paper-shaped projects protected.** `Grammaticality_judgments_as_detectors` and `Grammaticality_as_Kind_Miller` can feed the workbench, but the workbench should not create local drift inside those projects.

## 2026-06-09

- **Re-scope categorical grammaticality to operator-functional contrasts.** Revised `main.tex` so the paper no longer promises to derive a substance-based morphosyntax privilege. The companion operator-stratum paper remains responsible for the functional boundary; this paper derives categoricality from closure, opportunity structure, and preemption dynamics.
- **Repair the formalism rather than collapse it.** Adopted null-outcome `omega_0` for `K`, hierarchical partial pooling over constructional nodes for productivity, analogically generated candidates for `rho_t^\star`, and a `\widetilde{G}_t` feedback loop into production/repair. Full unification of `map`, `K`, and `C_t` is deferred to Brett via the decision memo.
- **Normalize cross-paper terminology.** Kept "effective preemption mass" and "opportunity set" as the canonical formal terms. Logged this with `pm-update`; the companion should align to these terms, with "opportunity mass" only as informal shorthand if explicitly defined.
- **Demote the gender prediction.** Kept gender concord as a boundary case but foregrounded the stronger tests: satiation framing for stable gaps, artificial-language-learning manipulation of opportunity-set size under zero positive evidence, and L2 rejections tracking L1 preemption mass.
- **Truth-first unification recommendation after Roughdraft review.** Brett clarified that the criterion is the stronger/truer thesis, not preservation of the current architecture. Updated the memo: if near-term readiness is the criterion, keep the hybrid; if truth-first rewrite is allowed, prefer full unification as the next major version (`p=0.63` stronger after rewrite).

## 2026-06-26

- **Treat the FoL outcome as a scope/fit rejection, not a substantive review.** *Functions of Language* rejected the operator-stratum manuscript FOL-26063 as outside scope. No referee criticism was provided, so the bridge-paper argument remains the current working baseline while the project identifies a better-fit venue.
