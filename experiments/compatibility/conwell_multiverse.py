"""Enumerate fake response tables for two word-order experiments.

Run with 'production' or 'comprehension' to print all branches as CSV.
All sample sizes are totals. A participant contributes exactly one response.
"""
import argparse
import csv
import sys
from fractions import Fraction
from itertools import product

import numpy as np
from scipy.stats import binom

from conwell_learning import TrainingVerb, forecast, paired_predictions, training_history
from conwell_recovery import fisher_rejections, response_tables


GRADED, HARD = "graded", "gate+lexical"
CONCENTRATIONS = (Fraction(1, 2), 1, 3)
SIZES = (24, 96, 192)
REPLAYS = (1, 3)


def choose_graded(tables):
    """Equal prior odds. Randomize when the likelihoods coincide."""
    left, right = tables[GRADED], tables[HARD]
    ties = np.isclose(left, right, rtol=1e-12, atol=0)
    return np.where(ties, 0.5, left > right)


def production():
    """Compare ideal, fixed-reference and freely fitted response midpoints."""
    nominal = paired_predictions()
    fixed_rule, detect = {}, {}
    for total in SIZES:
        n = total // 2
        tables, _ = response_tables(n, {m: nominal[m] for m in (GRADED, HARD)})
        fixed_rule[n] = choose_graded(tables)
        detect[n] = fisher_rejections(n)
    for replays, k in product(REPLAYS, CONCENTRATIONS):
        raw = paired_predictions(replays, k)
        for lapse, total in product((Fraction(0), Fraction(1, 5)), SIZES):
            n = total // 2
            rates = {m: tuple((1 - lapse) * p + lapse / 2 for p in raw[m])
                     for m in (GRADED, HARD)}
            gap = (1 - lapse) / (3 + k)
            for first, second in rates.values():
                assert first - second == gap
            tables, _ = response_tables(n, rates)
            ideal = np.maximum(tables[GRADED], tables[HARD]).sum() / 2
            graded_correct = (tables[GRADED] * fixed_rule[n]).sum()
            hard_correct = (tables[HARD] * (1 - fixed_rule[n])).sum()
            assert (graded_correct + hard_correct) / 2 <= ideal + 1e-12
            yield dict(replays=replays, concentration=float(k), guess=float(lapse), N=total,
                       contrast=float(gap), graded_power=tables[GRADED][detect[n]].sum(),
                       hard_power=tables[HARD][detect[n]].sum(), calibrated_accuracy=ideal,
                       reference_correct_graded=graded_correct, reference_correct_hard=hard_correct,
                       # Equal gaps imply identical binomial families once the
                       # midpoint is estimated over [gap/2, 1-gap/2] in each.
                       free_midpoint_likelihood_ratio=1)


def comprehension():
    """Isolate what the extra comprehension observation can identify.

    Four independent groups, restricted/alternating by production/comprehension.
    Match the rivals on fresh-verb production and alternating comprehension.
    The matched cells cancel from their likelihood ratio. The remaining cell
    is the fresh restricted verb heard in the patient-first order.
    """
    for replays, k in product(REPLAYS, CONCENTRATIONS):
        history = training_history(True, replays)
        # For a fresh verb both the singleton and both-order components have
        # mean agent-first use theta. Thus production averages to E(theta).
        prod_restricted, prod_control = (
            forecast(HARD, history, TrainingVerb(meaning, 0, 0), k)[0]
            for meaning in ("contact", "posture"))
        assert prod_restricted > prod_control == Fraction(1, 2)
        for c, repair, timing, total in product((Fraction(4, 5), Fraction(19, 20)),
                                                (0, Fraction(1, 2), 1),
                                                ("prior", "update-on-hearing"), SIZES):
            n = total // 4
            # Half of verbs have singleton repertoires. A fraction theta of
            # those license only agent-first; on the rest the rare order is accessible.
            def gate_accuracy(agent_first):
                # An error-free tutor's use excludes an agent-only repertoire
                # if the listener updates on the form before choosing the video.
                unavailable = agent_first / 2 if timing == "prior" else 0
                return c - (c - Fraction(1, 2)) * (1 - repair) * unavailable

            target = gate_accuracy(prod_restricted)
            control = gate_accuracy(prod_control)
            # A smooth listener weights the role cue by experience with
            # patient-first. Fit its intercept to the same control; a fixed
            # slope from the generative branch then matches the held-out cell.
            slope = (c - Fraction(1, 2)) * (1 - repair) / 2 if timing == "prior" else 0
            smooth_target = control + slope * (prod_control - prod_restricted)
            assert smooth_target == target
            counts = np.arange(n + 1)
            access = binom.pmf(counts, n, float(target))
            cue_only = binom.pmf(counts, n, float(control))
            ideal = np.maximum(access, cue_only).sum() / 2
            yield dict(replays=replays, concentration=float(k), accessible_accuracy=float(c),
                       recovery=float(repair), timing=timing, N=total, target_cell_n=n,
                       production_agent_restricted=float(prod_restricted),
                       production_agent_control=float(prod_control), correct_control=float(control),
                       correct_restricted=float(target), deficit=float(control-target),
                       calibrated_access_vs_cue_accuracy=ideal,
                       matched_access_vs_smooth_accuracy=0.5)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("experiment", choices=("production", "comprehension"))
    args = parser.parse_args()
    rows = list(production() if args.experiment == "production" else comprehension())
    writer = csv.DictWriter(sys.stdout, fieldnames=rows[0], lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
