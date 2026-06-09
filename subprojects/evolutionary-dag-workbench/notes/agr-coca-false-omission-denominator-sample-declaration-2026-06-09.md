# AGR COCA False-Omission Denominator Sample Declaration

**Date:** 2026-06-09
**Target graph:** `graphs/archive/agreement-controller-override-candidate.json`
**Audit lane:** `false-omission-audit`
**Query:** `the majority of people`

## Decision

Use a bounded denominator KWIC sample for `the majority of people` to check whether the present-tense
direct agreement strings miss enough agreement-bearing opportunities to change the direction of the
`majority` discriminator.

The bounded check is:

- the first/default KWIC page exposed by the normal list-result-click route;
- acceptable if it contains at least 90 rows;
- coded separately from direct agreement rows;
- interpreted as an omission audit, not a replacement filtered count.

## Interpretation Rule

The omission audit supports the existing `majority` discriminator if:

- the sample contains agreement-bearing opportunities not captured by `are/is`; and
- those omitted agreement-bearing opportunities do not reverse the plural-dominant direction.

The audit weakens the discriminator if omitted singular-agreement opportunities are common enough to
make the direct present-tense result misleading.

No numeric score movement follows from this audit.
