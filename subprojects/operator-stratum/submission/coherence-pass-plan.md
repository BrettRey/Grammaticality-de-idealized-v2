# Coherence, Cohesion, and Redundancy Pass
Date: 2026-06-02

Scope: targeted prose surgery on `main.tex`. No blind-version changes, no reference changes, no theoretical rebuild.
## Aim
Make the paper read as one argument rather than a sequence of repaired objections. The current draft is much stronger than the January version, but revision history has left repeated guardrails around the same distinctions:

- operator membership vs. automatic ungrammaticality;

- public consequence vs. public-update instruction;

- operator stratum vs. expression-shape/payload;

- categoricality as a predicted profile rather than a definition.


Those distinctions are right. The pass should make them do work once, then let later sections rely on them.
## Proposed Edits
1. Tighten the opening-to-definition path.

  - Keep the puzzle and public accountability setup.

  - Remove or compress repeated claims that “some aspects are public and others are not” once the operator definition is introduced.

  - Make the transition into Section 3 more direct.

2. Reduce repetition in the operator-stratum definition.

  - Keep the two conditions.

  - Compress the “header-like / three strata” paragraph so it does not restate the table at full length.

  - Keep the table, but make surrounding prose lighter.

3. Tighten boundary cases.

  - Preserve slurs, interjections, and `le hiver`.

  - Cut repeated “this does not imply all X belongs to the operator stratum” language where the table and definition already establish that.

  - Keep the `le hiver` asterisk call.

4. Improve Section 4 cohesion.

  - Reduce repeated “clausal architecture packages operator contrasts” sentences.

  - Keep Amele as the hard operator-mismatch case.

  - Keep Japanese `ka` as the membership-not-asterisk case.

  - Make the bridge from examples to complement/modifier cleaner.

5. Reduce overlap between tense/number and typological consequences.

  - Keep tense/number as a short universality guardrail.

  - Avoid restating the full cross-linguistic thesis twice.

6. Tighten the “phonology and lexicon” section.

  - Keep the cross-substance payoff.

  - Reduce repeated “boundary is not substance-based” formulations.

  - Keep phonotactics as the three-way contrast case.

7. Social-technology section.

  - Keep S/A/I conditioning and detector/output distinction.

  - Reduce overlap between the earlier slur boundary case and the later slur/social-policing paragraph.

  - Keep the ideological-policing distinction, but make it less aphoristic if the prose is carrying the point already.

8. Predictions and conclusion.

  - Leave predictions mostly intact unless a sentence repeats earlier diagnostics verbatim.

  - Trim the conclusion so it synthesizes rather than re-listing every section.

## Non-Goals
- No new examples.

- No new citations.

- No blind-review preparation.

- No title/abstract rewrite for FoL yet.

- No aggressive section reordering unless a local cut clearly requires it.

## Verification
After edits:

1. Run `../../../../.house-style/check-style.py main.tex`.

2. Run `latexmk -xelatex -interaction=nonstopmode main.tex`.

3. Report any remaining layout warnings separately from prose issues.
