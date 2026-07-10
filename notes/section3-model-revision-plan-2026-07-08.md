# Section 3 Model Revision Plan
## Scope
Implement the supplied revision as a model swap in `main.tex`, not as a light copy edit. The current paper source is single-file; there is no `section3-revised.tex` to splice.
## Load-Bearing Assumptions
1. Section 3 is the formal core beginning at `\section{A formal core: grammaticality as conditioned stability}`.
  
  - Tested: `main.tex` contains §3 at line 691.
    
  - Consequence: edits should replace contiguous subsections in `main.tex`.
    
2. The request preserves three parts of current §3.
  
  - Preserve `Conditioning structure` (`sec:conditioning`).
    
  - Preserve `Interlocutor misalignment about conditioning` (`sec:misalignment-conditioning`).
    
  - Preserve `Identifying the conditioning state before prediction` (`sec:identification-c`), except for the one confidence-readout sentence.
    
3. The old scalar product model must stop doing constitutive work.
  
  - Retire the null-outcome energy model for `K`.
    
  - Replace `\widetilde{G}_t = \mathsf{map}\cdot K\cdot C_t` with posterior existence over assemblies.
    
  - Keep the old product only as a limiting/special-case explanation.
    
4. The downstream paper still contains many references to `map`, `K`, `C_t`, `\widetilde{G}_t`, and thresholded `G_t`.
  
  - Falsification condition: if those references remain as active claims after §3, the revision will compile but be conceptually inconsistent.
    
  - Plan response: patch the most load-bearing downstream passages now: §4 dynamics notation, §5 predictions, conclusion, and Appendix A.
    
## Edit Plan
1. Replace the notation summary table and the current `Objects` subsection with the supplied construction/assembly objects.
  
  - Insert the notation bridge after the preserved `Conditioning structure`.
    
  - Define constructions, operator assignments, assemblies, `def`, `sat`, and latent licensing `L_t(A,c)`.
    
  - Keep partial pooling, rewritten over construction nodes.
    
2. Replace `Grammatical status as a conditioned state property` through `What map does and doesn't do`.
  
  - Use posterior existence `G_t(f,v,c)`.
    
  - Preserve projectibility, categorical talk, and decision-theoretic read-out in the revised terms.
    
  - Replace the old three-way failure assignment with the four-step procedure: structural, compatibility, saturation, licensing.
    
3. Preserve §3.5 and §3.6 with minimal surgery.
  
  - Update misalignment from `\widetilde{G}^{(h)}_t` to the hearer expected posterior-status notation.
    
  - Add the requested confidence-readout identification sentence after the `F` evidence stream sentence.
    
  - Avoid broader rewrites unless needed to prevent stale terminology.
    
4. Replace the current feeling and measurement subsections.
  
  - Implement `(F,\Phi)`.
    
  - Add plausibility to `R_i`.
    
  - Replace the measurement model with four observation channels.
    
  - Remove the old two-layer figure if it no longer matches the text.
    
5. Replace worked examples.
  
  - Use the supplied eight examples.
    
  - Add the winnerless-cell case for `amn't` and `pobedit'` 1sg.
    
  - Remove or update the current posterior-means figure if its caption assumes the old scalar score.
    
6. Patch §4 dynamics for the forward obligations.
  
  - Add omission weighting with recoverability `r_i` and rejection-ascription `q_i`.
    
  - Add repair stream/controller language with `\phi_{\mathrm{rep}}(n)`.
    
  - Add a new subsection on winnerless cells as metastable avoidance attractors.
    
  - Add a new subsection on derived obligatoriness.
    
  - Calibrate emergent bimodality language and cite the convergence sources already present or add local bib keys if missing.
    
7. Patch §5.2 predictions.
  
  - Add dispersion as leading indicator.
    
  - Add policing intensity proportional to `\lambda\Delta`.
    
  - Add re-licensing prediction for perfect-plus-past-adverb varieties.
    
  - Sharpen the satiation/framing rank order by `1/\nu`.
    
8. Patch abstract, §2, conclusion, and Appendix A lightly.
  
  - Abstract: add two sentences on posterior existence and mean/concentration.
    
  - §2: add forward pointers for derived obligatoriness where progressive/evidentiality are discussed.
    
  - Conclusion: remove stale `map/K/C_t` scalar framing and flip the memory-burden paragraph to treat the inventory as the model's data structure.
    
  - Appendix A: recast `kitap-ler` as failure of exponent-selection/no well-typed covering assembly, while `doktor` remains in the feeling channel.
    
## Checks
1. Run targeted searches for retired concepts:
  
  - `null outcome`, `energy`, `\widetilde{G}`, `\mathsf{map}`, active `K(u,c)` definitions.
    
2. Run `latexmk main.tex`.
  
3. Run the house-style audit on edited LaTeX per the repo skill.
  
## Open Judgment Calls
1. I will not attempt a complete rewrite of all §1--§2 narrative scaffolding in this pass; the supplied text explicitly says the prose architecture survives.
  
2. I will keep existing empirical figures unless their captions directly contradict the new core. The posterior-means figure may remain useful in §4 as a visualization of mean/concentration dynamics, but not as evidence for `\widetilde{G}_t`.
  
3. I will prefer existing bibliography keys over adding new entries. If the convergence sources named in the forward obligations are absent, I will add placeholders only if enough metadata is already present locally.
