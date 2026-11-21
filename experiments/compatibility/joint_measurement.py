"""Design analysis of paired truth and production at the training payoff.

Run python3 experiments/compatibility/joint_measurement.py from the project
root. JSON on stdout contains assumptions, exact witnesses and simulation
results. NumPy, SciPy and the shared-history experiment are required.

T=1 is a recorded truth endorsement; Y=1 is recorded production of P. The
estimand D=P(T=0,Y=1) uses all paired trials. Each learner receives the same
split exposure on A, then provides ONE pair on a held-out B item, without
feedback. Between learners, cross three conditions with both task orders.
The target scene is reopened. Matched, independently established controls
make the candidate description false or true at the same production payoff.
The true control must permit the target and leave the paraphrase attractive.

For a shared gate, the entire 2x2 target table is a mixture of the two
endpoint control tables, provided their conditional response laws transport
to the target. This holds within each item family and order, even when
responses within a trial are dependent. Let x=P(T=1) and let d be D. Using
subscripts 0,t,1 for false, target and true, respectively, set
  u=(x1-x0)*(dt-d0)-(xt-x0)*(d1-d0), v=x1-x0.
The reported excess is E[u]/E[v] across balanced orders and new item families,
a control-separation-weighted excess in probability units. This uses truth
to infer the mixture weight. Applying the same contrast to P(Y=1) checks
the remaining independent coordinate of the 2x2 table. Neither fit requires
knowing the learner's g, the slip rates, the order effect or the true shares.
Giving each cell separate learners makes the sample determinant unbiased:
products using the same endpoint cancel algebraically. Interval estimation
uses independent item families, keeping the two order strata together.

For generation, integrate the learner's posterior draw g from shared_history
over a fresh learner for every pair. Direct multinomial sampling from the
integrated four-cell law is exactly equivalent to drawing these learners
separately. New test families have transfer strength g_item = transfer*g
and item-specific task slips. Each replication draws fresh items and learners.
Controls see the same family and payoff. Across-order carryover modifies
only a discordant (0,1) pair: with the specified probability the second
answer conforms to the first, giving (0,0) if truth is first or (1,1) if
production is first. Equal carryover can affect both orders undetectably
in D. All nuisance ranges and sample sizes below are design assumptions.
"""

import json
from dataclasses import asdict, dataclass

import numpy as np
from scipy.stats import t

from shared_history import B_REOPENED, HISTORIES, TRAIN_SHARE, compatibility, posterior


SEED = 20261121
REPEATS = 4000
TRANSFER_RANGE = (0.8, 1.0)
HISTORY = "P equally often after reopening"


@dataclass(frozen=True)
class Scenario:
    label: str
    # Proportion of gate sharing between tasks. 1 means the same decision
    # governs both. A graded learner can implement this with one uniform
    # threshold per person; 0 means independent decisions conditional on g.
    sharing: float
    slip_range: tuple = (0.02, 0.08)
    # Chances of alignment of the second answer in the two orders.
    carry: tuple = (0.25, 0.05)
    target_extra_production_slip: float = 0.0


def table(mu, second, truth_slip, prod_slip, share_gate, carry, truth_first):
    """Joint cell probabilities in order 00,01,10,11 (truth, production)."""
    r = TRAIN_SHARE
    dt, dy = 1 - 2 * truth_slip, 1 - 2 * prod_slip
    x = truth_slip + dt * mu
    y = prod_slip + dy * r * mu
    d_shared = ((1 - mu) * (1 - truth_slip) * prod_slip
                + mu * truth_slip * (prod_slip + dy * r))
    d = d_shared + (1 - share_gate) * r * dt * dy * (mu - second)
    if truth_first:
        y = y - carry * d
    else:
        x = x + carry * d
    d = (1 - carry) * d
    return np.stack(np.broadcast_arrays(1 - x - d, d, x - y + d, y - d), axis=-1)


def joint_contrast(cells):
    """Control-based prediction errors; arrays end in condition, joint cell."""
    x = cells[..., 2] + cells[..., 3]
    discordance = cells[..., 1]
    production = discordance + cells[..., 3]
    v = x[..., 2] - x[..., 0]
    xdiff = x[..., 1] - x[..., 0]

    def determinant(z):
        return v * (z[..., 1] - z[..., 0]) - xdiff * (z[..., 2] - z[..., 0])

    return v, determinant(discordance), determinant(production)


def summarize(u, v, reference):
    """Ratio estimate and delta-method t interval over independent families."""
    n_items = u.shape[1]
    den = v.mean(axis=1)
    if np.any(den <= 0):
        raise ArithmeticError("Controls failed to separate at the study level")
    est = u.mean(axis=1) / den
    se = (u - est[:, None] * v).std(axis=1, ddof=1) / (den * np.sqrt(n_items))
    half = t.ppf(0.975, n_items - 1) * se
    return {
        # Reference averaged over generating probabilities, not sampled replies.
        "population_reference": float(reference),
        "mean_estimate": float(est.mean()),
        "median_95ci_half_width": float(np.median(half)),
        "coverage": float(np.mean(np.abs(est - reference) <= half)),
        "positive_95ci": float(np.mean(est - half > 0)),
        "negative_95ci": float(np.mean(est + half < 0)),
    }


def design(rng, sc, n_items, per_cell, moments):
    shape = (REPEATS, n_items)
    transfer = rng.uniform(*TRANSFER_RANGE, size=shape)
    truth_slip = rng.uniform(*sc.slip_range, size=shape)
    prod_slip = rng.uniform(*sc.slip_range, size=shape)
    # Last-but-one dimension holds false control, reopened B, true control.
    population = []
    samples = []
    for order, carry in enumerate(sc.carry):
        by_condition = []
        sampled = []
        for condition, (mu, second) in enumerate((
            (0, 0), (transfer * moments[0], transfer**2 * moments[1]), (1, 1)
        )):
            slip = prod_slip + (sc.target_extra_production_slip if condition == 1 else 0)
            p = table(mu, second, truth_slip, slip, sc.sharing, carry, order == 0)
            by_condition.append(p)
            sampled.append(rng.multinomial(per_cell, p) / per_cell)
        population.append(np.stack(by_condition, axis=-2))
        samples.append(np.stack(sampled, axis=-2))

    # Order-specific determinants precede averaging: pooling the raw cells
    # first need not preserve the mixture restriction with differing weights.
    v, ud, uy = (arr.mean(axis=0) for arr in joint_contrast(np.stack(samples)))
    vp, udp, uyp = joint_contrast(np.stack(population))
    # Compare the target's marginal reports too. Even equal suppression of
    # the discordant cell can move truth and production marginals in ways
    # randomizing task order reveals. These are descriptive pointwise CIs.
    target_change = samples[1][..., 1, :] - samples[0][..., 1, :]
    mean_change = population[1][..., 1, :] - population[0][..., 1, :]
    order_results = {}
    for name, columns in (("reject_and_produce", [1]), ("endorse", [2, 3]),
                          ("produce", [1, 3])):
        diff = target_change[..., columns].sum(axis=-1)
        ref = mean_change[..., columns].sum(axis=-1).mean()
        order_results[name] = summarize(diff, np.ones_like(v), ref)
    return {
        "families": n_items, "learners_per_condition_order_family": per_cell,
        "learners": n_items * per_cell * 6,
        "discordance_excess": summarize(ud, v, udp.mean() / vp.mean()),
        "production_excess": summarize(uy, v, uyp.mean() / vp.mean()),
        "target_order_difference_production_first_minus_truth_first": order_results,
    }


def run():
    a, b, mass, _ = posterior("hard", HISTORIES[HISTORY])
    g = compatibility(a, b, B_REOPENED)
    moments = (float(np.sum(mass * g)), float(np.sum(mass * g**2)))
    witness = {}
    for name, mu, second in (("fixed_third", 1/3, 1/9), ("split_history", *moments)):
        witness[name] = {
            model: table(mu, second, 0.05, 0.05, sharing, 0, True).tolist()
            for model, sharing in (("shared", 1.0), ("independent", 0.0))
        }
    np.testing.assert_allclose([row[1] for row in witness["fixed_third"].values()],
                               [0.04, 0.13])
    # Exact identity of a binary hard gate and a graded rule that consults
    # the same U for both tasks: P(U <= g | g) = g. Marginalize the two
    # conditional response laws. Any subsequent common order kernel preserves
    # equality, including after averaging over the learner's posterior.
    # Confirm the linear restriction survives the order manipulation.
    for truth_first in (False, True):
        test = [table(mu, mu**2, 0.07, 0.11, 1, 0.4, truth_first)
                for mu in (0, 0.36, 1)]
        np.testing.assert_allclose(test[1], 0.64 * test[0] + 0.36 * test[2])
    scenarios = [
        Scenario("shared gate or shared personal threshold", 1),
        Scenario("independent graded choices", 0),
        Scenario("half shared; noisier responses", .5, (.05, .15), (.5, .2)),
        Scenario("shared gate; target-only extra production slips", 1,
                 target_extra_production_slip=.07),
        Scenario("independent; equal carryover in both orders", 0, carry=(.4, .4)),
    ]
    results = []
    for i, sc in enumerate(scenarios):
        for n_items, per_cell in ((12, 8), (24, 12)):
            rng = np.random.default_rng([SEED, i, n_items, per_cell])
            results.append({"scenario": asdict(sc), **design(rng, sc, n_items, per_cell,
                                                              moments)})
    return {"seed": SEED, "replications": REPEATS, "payoff_share": TRAIN_SHARE,
            "transfer_range": TRANSFER_RANGE, "history": HISTORY,
            "split_history_moments": {"mean_g": moments[0], "mean_g_squared": moments[1]},
            "cell_order": ["reject_other", "reject_P", "endorse_other", "endorse_P"],
            "no_carryover_witnesses": witness, "results": results}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
