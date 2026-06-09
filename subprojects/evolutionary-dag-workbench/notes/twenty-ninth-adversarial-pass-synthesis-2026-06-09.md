# Twenty-Ninth Adversarial Pass Synthesis

**Date:** 2026-06-09
**Trigger:** repeated partial survivals in temporal anchoring, catenative complement selection, and
agreement after the CGEL discriminator pack.

## New Cards

Added three source-backed discriminator cards:

- `perfect-already-yesterday-cgel`
- `allow-prevent-complement-selection-cgel`
- `coordination-agreement-resolution-cgel`

## Evaluation Results

`perfect-already-yesterday-cgel` partly survives `FRAME`.

The graph separates frame fit from recoverability, but the `already` plus `yesterday` case makes the
missing temporal-anchor/current-relevance construct sharper. The issue is no longer just "present
perfect plus definite past time"; it is the interaction between present perfect, experiential
framing, definite past-time anchoring, and the contribution of `already`.

`allow-prevent-complement-selection-cgel` partly survives `SEL`.

The graph correctly keeps complement selection apart from collocation and payload choice. It still
lacks catenative verb-class subtype, passive/raising/control distinctions, and the cohort channel
needed for the local `allowed doing` contrast.

`coordination-agreement-resolution-cgel` partly survives `OPG`.

The graph can route agreement into broad operator value and attribution, and it has a processing
channel. It cannot predict controller choice, licensed override, unit construal, distributive
coordination, mixed-number `or` avoidance, or correction-driven agreement.

## Mutation

Added `agreement-controller-override-candidate`.

This is a narrow mutation, not a general account. It introduces controlled constructs for:

- `agreement_controller_identification`
- `agreement_feature_alignment`
- `agreement_override_pattern`
- `notional_agreement_basis`
- `retrieval_attractor_salience`

The candidate separates three paths that previous modules blurred:

- controller/override path: controller identification and licensed override feed agreement feature
  alignment and community licensing;
- attractor path: non-controller salience perturbs processing, reported acceptability, and
  production probability without licensing the attraction error;
- ideology/task path: correction and task framing affect attribution without deciding controller
  alignment.

## Guardrail

The agreement candidate is unscored and has no `scoped_module` label. It was built from the current
agreement cards, so it has no held-out projective evidence. The next proper test is a held-out
agreement card from a distinct source or a new CGEL subsection not used in the mutation.

## Next Pressure Points

- Temporal anchoring now has three partial survivals. The next temporal move should add a
  temporal-anchor construct only after one more card distinguishes recent past, experiential
  current relevance, and continuative readings.
- Catenative complement selection now has three partial/survival cards. The next selection move
  should add a catenative-subclass construct only if a held-out catenative card breaks `SEL` in the
  same way.
- Agreement has crossed the mutation threshold. The next agreement move should be held-out testing,
  not further graph growth.
