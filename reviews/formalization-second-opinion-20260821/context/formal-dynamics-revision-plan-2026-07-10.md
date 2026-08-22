# Formal Dynamics Revision Plan
This review is directionally right. The state architecture should stay, but the dynamics need to be demoted or rebuilt so the paper no longer claims derivations that the current equations do not supply.
## Judgment Calls
### Keep Strong
- Assembly-based status architecture.
  
- Licensing versus selection.
  
- Opportunity-sensitive negative evidence.
  
- Decision threshold as a read-out layer.
  
### Revise Hard
- Separate ontic population state from posterior estimate.
  
- Add epistemic-versus-heterogeneity variance decomposition.
  
- Replace the pseudo-exact omission inversion with log-likelihood-ratio evidence.
  
- Correct discounted Beta updating so evidence, not the prior, is forgotten.
  
- Demote or condition the dynamics claims that are currently overstated.
  
### Do Not Try To Fully Prove Now
- Full stochastic bimodality theorem.
  
- Winnerless-cell metastability theorem.
  
- Operator/style bifurcation theorem.
  

Those can be represented as model targets or toy-regime demonstrations, not claimed as established derivations.
## Proposed Edits
### §3: State Theory
1. Rename the status objects:
  
  - `S_t(f,v,c; theta_t)` = ontic population status/prevalence: probability that a randomly sampled speaker has a complete licensed assembly.
    
  - `\hat S_t(f,v,c)` = posterior estimate of that status given evidence.
    
  - Keep `G_t` only if we explicitly define it as `\hat S_t`, but my preference is to move to `S/\hat S` for clarity.
    
2. Add the variance decomposition:
  
  - Single node:
    
    - epistemic variance: `Var(theta | D) = C(1-C)/(nu+1)`.
      
    - population heterogeneity: `E[theta(1-theta)|D] = C(1-C)nu/(nu+1)`.
      
  - Assembly level:
    
    - `U_epi = Var(S(theta)|D)`.
      
    - `U_het = E[S(theta)(1-S(theta))|D]`.
      
  - Use this to define starved, preempted, and stably heterogeneous cases.
    
3. Fix confidence:
  
  - Keep `Phi` as evidence confidence only if renamed/qualified.
    
  - Add decision confidence as `Phi_dec = max{P(S >= tau | D), P(S < tau | D)}`.
    
  - Use `Phi_dec` for judgment confidence around membership labels.
    
4. Flag dependence:
  
  - Marginal node posteriors do not determine assembly prevalence.
    
  - Product factorization requires within-speaker independence or a latent-lect model.
    
5. Compatibility algebra:
  
  - Replace “partial function to atomic values” with typed constraints and satisfiable meet.
    
  - Hard compatibility remains Boolean: `def(A)=1` iff the constraint meet is non-bottom.
    
### §4: Dynamics
1. Correct discounted update:
  
  - `a_{t+1} = a_0 + delta(a_t-a_0) + evidence^+`.
    
  - `b_{t+1} = b_0 + delta(b_t-b_0) + evidence^-`.
    
  - State fractional counts are generalized-Bayes/effective-sample-size approximations.
    
2. Normalize production:
  
  - Use gated softmax over a speaker inclusion vector.
    
  - Present `pi approx S*rho*` as an approximation under stated assumptions.
    
3. Replace omission weight:
  
  - Use log likelihood ratio: `ell_i = log P(y_i|Z_x=0) - log P(y_i|Z_x=1)`.
    
  - Add `[ell_i]_+` to negative evidence and `[-ell_i]_+` to positive evidence.
    
  - State old `rho*` result is first-order for small candidate mass.
    
4. Winnerless cells:
  
  - Stop saying low mean follows from no evidence.
    
  - Add the missing assumption: low prior for unsupported analogical candidates, weak negative evidence, or a cell-level “no established candidate” latent state.
    
  - Best near-term move: represent winnerless cells as a conjectural regime requiring a low candidate prior plus outside-option evidence starvation.
    
5. Bimodality/operator specificity:
  
  - Demote Eq. 50 if retained.
    
  - Acknowledge current cubic is not operator-specific because bistability can occur at `Delta=0`.
    
  - Either add an explicit condition that `alpha,beta` depend on `N*Delta`, or replace the claim with: “the present dynamics represent the target regime; deriving it requires the toy model below/simulation.”
    
6. Moribundity:
  
  - Revise claim: discounted evidence reduces individual effective sample size.
    
  - Rising between-speaker dispersion requires heterogeneous priors or idiosyncratic evidence histories; make it a prediction of a population model, not an immediate theorem.
    
7. Saturation:
  
  - Either define it explicitly as a derived macro or remove it from the independent constitutive conjunction.
    
  - I recommend: saturation remains a derived macro used for classification, not an independent primitive.
    
### Claims Language
Replace “derive(s)” with “represents,” “models,” “predicts under the stated dynamics,” or “conjectures” for:

- categoricality;
  
- obligatoriness;
  
- winnerless-cell phenomenology;
  
- moribundity/dispersion-leading-means.
  

Keep stronger language for:

- assembly-based state architecture;
  
- licensing-selection decomposition;
  
- opportunity-sensitive omission distinction.
  
## Implementation Order
1. Patch §3 notation and variance decomposition.
  
2. Patch §4 update, production, omissions, and claims language.
  
3. Rebuild tables/notation summary if necessary.
  
4. Recompile and grep for stale `G_t`, `derive`, `posterior existence`, `Phi` ambiguity.
  
5. Optionally update Lean scaffold after the prose stabilizes.
