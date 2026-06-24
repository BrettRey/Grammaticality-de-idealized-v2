# Notes: Implications of Cohn's Multimodal Language Faculty for MVMG

**Source:** HiPhiLangSci podcast interview with Neil Cohn (2026-01-31)
**Transcript:** `/Users/brettreynolds/Documents/LLM-CLI-projects/papers/English_kinship_terms/hiphilangsci_054.txt`

---

## Summary of Cohn's Position

Neil Cohn (Tilburg) argues that humans have only three ways to express concepts: sound, bodily movement, and graphics. Given that all three come from the same brain, they should share cognitive building blocks and structural properties ("principle of equivalence").

Key claims:
1. **Modality = sensory channel + cognitive correlate** (not just a sensory system)
2. **Omnia** (full languages) have modality + grammar + compositional meaning
3. **Semia** (partial systems) have modality + meaning but no robust grammar (e.g., emoji, co-speech gesture)
4. **Conventionalization ≠ signification type** (Peircean correction to Saussure): a form can be conventionalized AND iconic/indexical/symbolic—these are orthogonal dimensions

---

## Implications for `main.tex` (MVMG Parent Paper)

### 1. Modality-Neutrality of the State Theory

The MVMG equation $\widetilde{G}_t(u,c) = \mathsf{map}(u,c) \cdot K(u,c) \cdot C_t(u,c)$ makes no reference to modality. If Cohn is right, this is a feature, not an oversight. The framework should generalize to:

- Sign languages (already well-supported)
- Visual languages (comics, diagrams, pictorial narratives)
- Gesture (though gesture is a semia, so preemption dynamics differ)

**Potential addition to §1 or §5 (Implications):** Note that MVMG is modality-neutral and cite Cohn (2024) as support for the claim that the same cognitive architecture underlies all three expressive channels.

### 2. Sharpening the Indexicality Section (§2.5)

Cohn's Peircean point clarifies the paper's treatment of socio-pragmatic indexicality:

- **Conventionalization** (whether a form is regularized) ≈ $C_t$
- **Signification type** (icon/index/symbol) ≈ part of $K$, the interpretive mapping

The paper currently treats indexicality as a dimension of value. Cohn's framework reinforces that indexical *value* is orthogonal to entrenchment: a highly entrenched form can be indexical (e.g., *vos* in Rioplatense Spanish), and a weakly entrenched form can be symbolic.

**Potential clarification:** Make explicit that indexical compatibility contributes to $K$ (the interpretation must cohere with the situation), while indexical *entrenchment* is part of $C_t$.

### 3. Visual Languages as a Testable Extension

If the MVMG framework is correct, visual languages should exhibit:

| Phenomenon | MVMG prediction |
|------------|-----------------|
| Stable gaps | Systematically avoided panel transitions (analogous to LBE) |
| Satiation effects | Marginal visual constructions improve with exposure |
| Processing costs | Complex visual layouts trigger feelings of "wrongness" |
| Preemption dynamics | Frequent visual niches accumulate strong negative evidence against non-licensed variants |

**Potential addition to §5 (Implications) or a "Future Work" section:** Flag visual languages as a domain where the framework makes testable predictions.

### 4. Omnia vs Semia: Scope Boundary

MVMG's diagnostic tree (§3, "Diagnosing (un)grammaticality at a glance") applies to *omnia*—systems with full grammatical structure. For *semia* (emoji, gesture), the stable-gap analysis doesn't apply because there's no paradigmatic closure generating high opportunity mass.

**Potential scope note:** The paper could acknowledge that the framework targets omnia; semia require a different treatment (perhaps $C_t$ dynamics without the preemption module).

---

## Subproject Notes Created

Detailed notes have been created in each subproject folder:

| Subproject | Notes file |
|------------|------------|
| `asterisk-de-idealized` | `NOTES-cohn-multimodal.md` |
| `etiological-account` | `NOTES-cohn-multimodal.md` |
| `feeling-of-ungrammaticality` | `NOTES-cohn-multimodal.md` |
| `operator-stratum` | `NOTES-cohn-multimodal.md` |

---

## Reference

Cohn, N., & Schilperkort, Y. (2024). *A Multimodal Language Faculty*. Bloomsbury Academic.

(Cohn's graphic novel version, *Speaking in Pictures: A Vision of Language*, appears February 2026.)

---

*Created 2026-01-31*
