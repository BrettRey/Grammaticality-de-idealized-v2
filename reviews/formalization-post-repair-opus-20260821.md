# Adversarial audit: main.tex + section3.tex after the formal repair

## Context

Read-only check of the current working-tree `main.tex` (2087 ll.) and `section3.tex`
(862 ll.) against the repair targets: candidate-conditional $\rho^\star$ vs full-choice
$\tilde\rho^\star$, the exact omission LLR, current-window innovations and discounting,
the speaker Beta filter / adoption–retention transition / empirical prevalence / analyst
posterior distinction, the stipulated cubic with frozen repair flow, ontic path-dependent
OBL and de-obligatorification, projectibility wording, and the agreement figure.
No edits made. Findings verified against source, not against earlier review files.

## What checks out (recomputed)

- **Omission LLR is exactly right.** With $P(y_i\mid Z_x{=}1)=e^{U(y_i)}/(D_{0,i}+e^{U(x)})$
  and $P(y_i\mid Z_x{=}0)=e^{U(y_i)}/D_{0,i}$, the ratio is $D_{0,i}/(D_{0,i}+e^{U(x)})
  = 1-\tilde\rho^\star_{i,t}$, so $\ell_i=-\log(1-\tilde\rho^\star_{i,t})\approx
  \tilde\rho^\star_{i,t}$ for small mass. main.tex:980–990 is correct as stated.
- **Discounting recurrence is self-consistent.** `main.tex:861–868`: $a^0$ undiscounted,
  $(a_t-a^0)$ discounted, innovations undiscounted. $\delta_m=1$ recovers plain conjugate
  accumulation; no-evidence limit decays to $a^0$, not Beta(0,0); steady state
  $\nu^\ast=\nu_0+\text{inflow}/(1-\delta_m)$ matches the $O(N/(1-\delta_m))$ claim at 1365.
- **Cubic fixed point is correct.** Bracket root $\theta^\ddagger=(\beta+\chi\bar\psi)/
  (\alpha+2\chi\bar\psi)$; $\theta^\ddagger\in(0,1)$ iff $\beta+\chi\bar\psi>0$ and
  $\beta<\alpha+\chi\bar\psi$, which are exactly the endpoint-attracting conditions.
- **Figure `fig:posterior-means` reproduces exactly.** Beta(1,1), mean $1/(2+mt)$:
  rare $m{=}0.01$ gives 0.4762 at $t{=}10$, 0.4000 at $t{=}50$; dense $m{=}5$ gives
  0.14286, 0.019231, 0.003968. CrIs $1-(1-p)^{1/b}$ reproduce to 4 dp.
- **LBE rule-of-three:** $3/1228=0.244\%$, matches the stated 0.24% upper bound.
- **Wilson intervals** for the 105, 142 and 14 cells reproduce exactly.
- **Ontic/epistemic discipline is applied correctly** in §4.9 (`main.tex:1391`: "motion in
  its mean is not itself actuation") and in `eq:phi-dec`, `sec:measurement-C`, and the
  $\theta$-not-posterior-mean note at 1168.

## BLOCKER

**B1. Derived obligatoriness is not niche-indexed, so the flagship worked case fails
its own definition.** `main.tex:1250,1261–1266`; `section3.tex:113–120`.

$\mathrm{OBL}_t(c,\phi)$ is indexed only by conditioning state and frame type. But
$R_s^0(A,c)=P_j(L_s(A,c)=1\mid\boldsymbol\theta_s,c)$ and $L_t(A,c)=\bigwedge_\kappa
Z_t(\kappa,c)$ are node-wise and value-blind, and $c$ is explicitly *not* the niche
($n$ is introduced separately at `main.tex:759` as the communicative job, and disciplined
separately at `section3.tex:568–575`).

For English progressive: the simple-present assembly is a member of $\mathcal A_0(d,\phi,c)$,
and its nodes are licensed at $\approx 1$ in any ordinary $c$ (speakers say *she studies*).
So $\sup_{s\in W_t}R^0_s(A,c)\approx 1 \gg \epsilon_0$, the first clause fails, and $d\notin
\mathrm{OBL}_t$. The definition therefore does not derive the case it is introduced to
derive (`main.tex:1302–1305`).

The escape makes it worse. If instead $R^0$ is read as availability of the *form–value*
route (zero-marking paired with the ongoing-at-issue value), then $R^0\!\approx\!0$ just
*is* the pivotal node being licensed to zero — and saturation collapses into licensing,
contradicting Table `tab:vars`, the four-condition architecture, and the ordered
diagnostic at `section3.tex:487–493`.

Internal confirmation: `main.tex:1318–1319` predicts a contrast "obligatory in some frame
types **and niches**, optional in others" — a proposition the object $\mathrm{OBL}_t(c,\phi)$
cannot express. `main.tex:1302` likewise reasons over "a $d$-at-issue niche" while the
definition has no $n$.

Fix is local: index $\mathrm{OBL}$ and $R^0$ by $n$ (or state that $c$ absorbs the at-issue
job and reconcile with §4.1/§3.7), and say explicitly what distinguishes near-zero
$R^0_n$ from a licensing failure.

## MAJOR

**M1. The membership definition and the de-obligatorification rule contradict each other
in the dead band.** `main.tex:1261–1266` vs `1286–1291`.
Membership is defined as holding *when* $\sup R^0<\epsilon_0$ and $\Pi\ge\pi_0$. Lapse is
defined as requiring $R^0$ above $\epsilon_1>\epsilon_0$. For $R^0\in[\epsilon_0,\epsilon_1)$
the definition says "not obligatory" and the hysteresis rule says "still obligatory."
$\mathrm{OBL}_t$, hence $\operatorname{sat}_t$, hence $S_t^\theta$, is undefined for any
contrast in that band. Also asymmetric: $\Pi$ gets no band, so a $\Pi$ fluctuating around
$\pi_0$ flips saturation window to window — the exact behaviour the hysteresis was added
to prevent.

**M2. The temporal recursion is not well founded.** `main.tex:1256–1258, 1284–1286`.
$\Pi_{W_t}$ is weighted by the "full **gated** counterfactual share," and the gate
$z_i(x,c)$ (`main.tex:817–822`) contains $\operatorname{sat}_t$. So $\mathrm{OBL}_t$ depends
on $\operatorname{sat}_s$ for $s\in W_t$, hence on $\mathrm{OBL}_s$, hence on $W_s$, with no
base case. The claim at 1284–1286 establishes only the *within-slice* ordering
($R^0\to\mathrm{OBL}\to\operatorname{sat}\to S^\theta$), not the temporal descent. Either
state an initialization at some $t_0$, or make $\Pi$ ungated (pure $\tilde\rho^\star$),
which would remove the dependence.

**M3. Ontic/epistemic leak at the licensing×choice factorization.**
`main.tex:830–832`, repeated `1786–1787`.
$\pi_t(x\mid n,c)=E_i[\cdot]$ is defined at `main.tex:806–822` as a $\theta$-conditional
expectation over speakers' inclusion states — an ontic population quantity. It is then set
$\approx G_t(x,c)\,\tilde\rho^\star$, where $G_t$ is by definition the *analyst's*
$\widehat S^{(a)}_t$ (`section3.tex:219–221`). Same at 832 with $C_t$, a filter posterior
mean. Should be $S_t^\theta$ / $\theta_t(\kappa_x,c)$, with the analyst version stated as a
separate estimation step. This is the single site where the repair's central distinction is
still collapsed.

**M4. The decision rule feeds the judge the analyst's posterior.** `section3.tex:420–427`.
"A judge in $c$ chooses ... accepts iff $G_t(u,c)\ge\tau(c)$." The judge's input must be
$\hat G^{(h)}_{i,t}$ or $g_{i,t}$. Two sites in the same file get it right —
`eq:phi-dec` (651–655) conditions on $\mathcal D_{i,t}$, and the judgment channel (705)
takes $\hat G^{(h)}$ — so this is an internal inconsistency, not a convention. It
propagates to `fig:rd-test` (`main.tex:1946,1956,1965`), where "community treatment"
is plotted against the analyst's $G_t$.

**M5. Bearer index systematically dropped in §3.2.2, where the projections depend on it.**
`section3.tex:302–304, 316, 321–335, 340–353`. The repair introduced
$\mathcal D_{r,t}$ with $r\in\{i,a\}$ (211–221), then §3.2.2 writes bare
$\operatorname{Var}(S_t^\theta\mid\mathcal D_t)$ and $\theta\mid\mathcal D_t\sim
\mathrm{Beta}(a,b)$ throughout. Satiation and framing lability are *speaker*-level
phenomena driven by $\nu_i$; as written, "satiation and framing rank order turn on $1/\nu$"
(316) and the four status regions (340–353) are stated over an analyst's posterior. An
analyst with abundant data would then predict no satiation for a form speakers are
uncertain about — the wrong direction.

**M6. $\theta_t$ carries two incompatible definitions.**
`section3.tex:128` defines $\theta_t(\kappa,c)=P_j(z_{j,t}(\kappa,c)=1)$, a sampling
proportion over speakers — which for a finite community *is* the empirical prevalence.
`main.tex:899–905` then distinguishes the empirical prevalence $\theta^{(M)}_{t+1}=
M^{-1}\sum_i z_{i,t+1}$ from "the exchangeable rate $\theta_{t+1}$." The finite-population
repair (the $O_p(M^{-1/2})$ fluctuation, the closure-approximation caveat) needs the
latent-rate reading; §3 licenses the sampling-proportion reading. Fix §3's definition to
the de Finetti mixing parameter.

**M7. The positive omission channel $p_t^+$ is identically zero, and mis-weighted.**
`main.tex:854–867, 959–1007`.
Under the stated normalized softmax, adding $x$ to the choice set can only lower a
competitor's probability, so $\ell_i(x)=-\log(1-\tilde\rho^\star_{i,t})\ge 0$ on every
competitor occasion; on outside-option occasions the paper's own result is $\ell_i\approx0$.
Hence $[-\ell_i]_+=0$ throughout and $p_t^+\equiv 0$: a dead term in the $a$-recurrence.
Separately, the $a$-update weights $p_t^+$ by $\lambda^+_\kappa=P(\kappa\in A^\ast\mid
x,c,\mathcal D_t)$ — a parsing posterior over a token of $x$ that, on an omission occasion,
was not produced — while the prose at 919–929 assigns *all* omission evidence to
$\lambda^-$. Either drop $p_t^+$, or name the model feature (utility coupling, gate
correlation) that can make $\ell_i<0$, and re-type its weight.

## MINOR

- **m1.** `main.tex:991–997` and `1789–1792` list the conditions for reducing $p_t^-$ to
  $N_t\rho^\star$ / $N_t\tilde\rho^\star$ but omit two: $r_i\approx1$ (certain niche
  identification) and $|\mathcal I_t^{\text{om}}|\approx N_t$ (the target essentially never
  produced). The second is benign for gaps and false for the general case as stated.
- **m2.** Frozen-flow (`main.tex:1169–1175`) holds $P(\text{mis-set})$ fixed, but that term
  is generically a function of $\theta$ — it is the same majority dependence the
  $(2\theta-1)$ factor encodes. The conditional escape clause is present and honest, but
  the caveat reads as an edge case when it is the generic one.
- **m3.** "Policing intensity should scale with ... $N_t\cdot\Delta$" (`main.tex:1058,
  1607–1608`) doesn't follow from $\psi_{\mathrm{rep}}=N_t\cdot P(\text{mis-set})\cdot
  r(\Delta,\iota)$ unless $r$ is linear in $\Delta$ and $P(\text{mis-set})$ is constant
  across contrasts. The model says only that $r$ is *increasing* in $\Delta$.
- **m4.** Residual $\rho^\star$ where the factorization requires $\tilde\rho^\star$:
  `main.tex:1587` ("variation carried entirely by selection $\rho^\star$"), `1814`, `1824`.
  Defensible if the dative is treated candidate-conditionally, but the paper's own rule
  (800–804) is that the two coincide only when the outside option is negligible, and that
  condition is never stated for the dative.
- **m5.** "$\operatorname{sat}_t$ is a path-dependent **ontic** macro" (`section3.tex:117`)
  sits awkwardly with "$W$ and tolerances $\epsilon_0,\pi_0$ are conventional parameters to
  be fixed **before classifying a contrast**" (`main.tex:1274–1275`). Analyst-fixed
  tolerances make $\mathrm{OBL}_t$ analyst-parameterized, hence $S_t^\theta$ too. If the
  thresholds are meant to be community conventions rather than analyst stipulations, say so.
- **m6.** $C_t$ (a posterior mean) used for population facts: `main.tex:1504` ("push the
  induced licensing posterior $C_t(\kappa,c)$ toward fixation"), `2036–2037` ("licensed at
  the population level, $C_t(\kappa,c)\approx1$"). Same leak as M3, lower stakes.
- **m7.** `section3.tex:779`: Wilson 95% upper for 71/72 is **0.997**, not 0.998
  (centre 0.96144, half-width 0.03605). The 105/142/14 rows are exact. The error is
  inherited verbatim from
  `subprojects/evolutionary-dag-workbench/notes/agr-coca-vertical-slice-report-2026-06-09.md:96`,
  so the probe should be corrected, not just the table.
- **m8.** `tab:agr-cells`: rows 2 and 3 ("exact" and "audited" *the majority* + set) are two
  codings of one cell. "Notional plural dominates in every cell" (caption, and
  `section3.tex:746`) therefore rests on three independent cells, not four.
- **m9.** The construction inventory is untensed ($\mathcal A(f,v)$ at `section3.tex:190`,
  $\mathcal H$ at 537, `main.tex:769`) while $\mathcal V^\star_{n,t}$, $\theta_t$, $z_{i,t}$
  and $\mathrm{OBL}_t$ all carry $t$. Coverage is then diachronically frozen, which sits
  badly with stored wholes entering and leaving the repertoire (468).
- **m10.** `main.tex:1665–1667` describes LBE as "extracting determiner-adjective sequences"
  and uses *Which do you prefer car?*, where every other site uses the determiner–head
  discontinuity and *Which did you buy car?*. Also, on CGEL terms *which* here is a
  determinative in determiner function, not a "determiner-adjective sequence."

## Verdict

**Materially coherent, with one blocking defect at a repaired site.**

The repair did the hard part correctly: the LLR derivation is exact, the discounting
recurrence is self-consistent at both limits, the cubic's fixed point and stability
conditions are right, the figure reproduces to 4 dp, and the ontic/epistemic separation
holds where it matters most (actuation, the transition kernel, the proof-obligation
language). The abstract does not overclaim relative to the body.

What does not hold is §4.6. Derived obligatoriness is the newest and most load-carrying
piece of the repair, and as written it cannot classify its own worked case (B1), is
ill-defined in the hysteresis band (M1), and grounds out in an unfounded temporal
recursion (M2). Alongside that, the bearer index is dropped or wrong at four sites
(M3–M6) — all local, all fixable in a sentence each, but M3 and M4 sit exactly on the
distinction the revision was for.

Recommended order: B1, then M1–M2 (same subsection), then M3–M6 as a single bearer-index
sweep, then M7. None of this requires restructuring; the architecture survives.
