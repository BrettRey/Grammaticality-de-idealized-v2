# Response Plan: Post-Review Revision

The review is right about the main pressure points. I would not try to defend the
current version as-is. The revision should make the identification discipline
symmetrical: conditioning state `c`, niche `n`, and the template/licensing boundary
all need explicit assignment rules.

## Highest-Value Edits

1. **Add a niche-identification protocol.**
   - Add it near §3.6, after the conditioning-state protocol.
   - Treat `n` the way the paper already treats `c`: preregister the communicative
     job, competitor set, outside option, and value recoverability before using
     absences as evidence.
   - Require robustness checks across at least two granularities when classifying
     a low-mean case as starved, preempted, or divided.
   - Soften `amn't`: present `pobedit'` 1sg as the clean winnerless-cell example;
     treat `amn't` as a mixed/borderline case whose classification depends on
     niche individuation and competitor treatment.

2. **Demote LBE from tested flagship to predicted/preliminary illustration.**
   - Keep the corpus result, but state that without independently normed
     `rho*_t(lbe | n,c)`, the corpus absence does not by itself identify
     high-concentration preemption.
   - Add the forced-choice norming protocol suggested in the review.
   - Rewrite the LBE/satiation language so Lu et al. is evidence about island
     satiation broadly, not direct evidence that LBE itself has been tested,
     unless the source explicitly contains LBE items.

3. **Fix the falsifier hierarchy.**
   - Demote the threshold-discontinuity design to a decision-layer test.
   - Remove conclusion language saying smoothness through `tau(c)` defeats OVMG.
   - Promote the real discriminators: Phi dissociation at matched means,
     satiation rank order, dispersion-leads-means, L2 preemption transfer,
     policing proportional to `N_t * Delta`, and the re-licensing/re-opening
     contrast.

4. **Reclassify Turkish suffix harmony.**
   - Add an assignment criterion: template failure only when violating the
     condition makes the value unrecoverable or the exponent unidentifiable;
     transparent value recovery routes to licensing or compatibility.
   - Move `kitap-ler` / `gul-du` from empty coverage to high-concentration
     non-licensing of an exponent choice in a dense operator-exponent niche.
   - Preserve the contrast with `doktor`: stem disharmony remains subjective
     phonological cost, not status failure.

5. **Correct the convergence claim.**
   - Replace the strong Pólya/convergence framing with a bounded-memory,
     constant-gain framing: stationary distribution concentrated near attractors,
     residual dispersion scaling with opportunity and memory, and escape times
     rather than almost-sure convergence.
   - Keep Argiento/Hu-Skyrms-Tarrès as decreasing-gain analogues, but stop saying
     the transfer is routine.
   - Tie this to §4.6 and §4.8: winnerless-cell metastability and actuation rarity
     become the same kind of escape-time story.

6. **Remove Phi circularity.**
   - Identify `Phi` with explicit confidence and test--retest stability.
   - Treat framing lability as a confirmatory outcome, not an identifying input.

7. **State where grammaticality stops projecting.**
   - Add a short subsection or paragraph near §3.3.2/§5: the projectible object is
     the licensing profile `(E[G_t], nu)`, with "grammatical" naming the high-mean,
     high-concentration region.
   - Say explicitly that grammaticality does not project to processing cost,
     production frequency, language-model string probability, typological
     comparanda, or conditioning states without `q_h`.

## Source-Grounding Fixes

These should be handled conservatively in the text even before full source audit:

- Change the Lu et al. claim from "LBE non-satiation is confirmed" to "LBE
  non-satiation is predicted; island non-satiation supplies the closest current
  analogue" unless the source actually includes LBE.
- Rewrite `Kawaii da` as an i-adjective/copula exponent-selection or selection
  fact, not redundant tense marking.
- Disambiguate Philip B. Corbett from Greville Corbett wherever the NYT quiz is
  cited.
- Make `big big` and embedded inversion explicitly variety-relative or replace
  them with safer examples.
- Anchor RDD methodology on an established source, with Lazzaro as a multinomial
  extension if needed.
- Add/fix venue metadata for Hu, Skyrms & Tarrès.
- Verify Grodner & Gibson figures and the Verkerk 60/191 claim before submission.

## Implementation Order

1. Make internal-theory fixes first: niche protocol, Phi identification, falsifier
   hierarchy, Turkish reclassification.
2. Then adjust the examples and source-sensitive claims.
3. Build and run the same scar scans as before.

This is enough to absorb the review without starting a new model revision. The
core architecture stays; the change is that the paper stops overclaiming exactly
where the new identification discipline has not yet been discharged.
