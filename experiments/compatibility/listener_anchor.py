"""Exact population checks for the changed-rule listener design. No human data."""

from fractions import Fraction as F

from scipy.stats import beta


def probabilities(*counts):
    assert all(n >= 0 for n in counts)
    return tuple(F(n, sum(counts)) for n in counts)


def mixture(past, present, share):
    assert len(past) == len(present) and 0 <= share <= 1
    return tuple((1 - share) * a + share * b for a, b in zip(past, present))


def distance(first, second):
    """Total variation between response distributions."""
    assert len(first) == len(second)
    return sum(abs(x - y) for x, y in zip(first, second)) / 2


def reading_share(past, present, target):
    """Identify the share from today's response and check every other category."""
    if present[1] == past[1]:
        raise ValueError("The controls do not separate on the designated today response.")
    share = (target[1] - past[1]) / (present[1] - past[1])
    if not 0 <= share <= 1 or mixture(past, present, share) != target:
        raise ValueError("The complete target distribution is outside the control segment.")
    return share


def share_bounds(count_tables, alpha=0.05):
    """Conservative simultaneous confidence set for a common two-anchor share.

    Each cue has three rows of counts (past control, present control, target).
    Each row contains one multinomial response per independently sampled listener.
    An empty intersection rejects the mixture. Coordinate-wise overlap alone
    does not prove that the joint model fits.
    """
    coordinates = sum(len(row) for table in count_tables for row in table)
    tail = alpha / (2 * coordinates)
    low, high = 0., 1.
    for table in count_tables:
        bounds = []
        for row in table:
            n = sum(row)
            if n <= 0 or any(k < 0 for k in row):
                raise ValueError("Each row needs observations and nonnegative counts.")
            bounds.append([(0. if k == 0 else beta.ppf(tail, k, n - k + 1),
                            1. if k == n else beta.isf(tail, k + 1, n - k))
                           for k in row])
        for (al, au), (bl, bu), (yl, yu) in zip(*bounds, strict=True):
            # Weighted lower controls <= target upper; target lower <= weighted upper controls.
            for intercept, slope in ((yu - al, al - bl), (au - yl, bu - au)):
                if slope > 0:
                    low = max(low, -intercept / slope)
                elif slope < 0:
                    high = min(high, -intercept / slope)
                elif intercept < 0:
                    return None
    return (low, high) if low <= high else None


def run():
    # Outcomes in order: posting-day rule, today's rule, either, cannot interpret.
    # Each pair (past control, present control) has the same ambiguous question.
    earlier_cue = (probabilities(75, 10, 10, 5), probabilities(15, 65, 15, 5))
    later_cue = (probabilities(45, 30, 20, 5), probabilities(5, 80, 10, 5))

    # Constructed target probabilities, specified separately from the readout.
    first = probabilities(240, 95, 45, 20)
    second = probabilities(140, 170, 70, 20)
    alternative = probabilities(60, 270, 50, 20)
    share = reading_share(*earlier_cue, first)
    forecast = mixture(*later_cue, share)
    assert share == F(1, 4) and forecast == second
    raw_change = second[1] - first[1]
    assert raw_change == F(3, 16)
    print(f"First-cue share = {share}. Second-cue forecast =", *map(str, forecast))
    print(f"Rise in today's responses with fixed share: {100 * float(raw_change):.2f} points.")

    # An account that starts in the past on every trial and retrieves today's
    # frame with probability share induces exactly the same kernels in both arms.
    for controls, target in ((earlier_cue, first), (later_cue, second)):
        past, present = controls
        report = tuple(a + share * (b - a) for a, b in zip(past, present))
        assert report == target

    other_share = reading_share(*later_cue, alternative)
    miss = distance(forecast, alternative)
    assert other_share == F(3, 4) and miss == F(1, 4)

    # When each cue fits separately, the error at any proposed common share x
    # is distance(past, present) * abs(x - the cue-specific fitted share).
    # The minimax choice balances the two errors between the two fitted shares.
    d1, d2 = distance(*earlier_cue), distance(*later_cue)
    best = (d1 * share + d2 * other_share) / (d1 + d2)
    error = distance(mixture(*earlier_cue, best), first)
    assert error == distance(mixture(*later_cue, best), alternative) == F(3, 22)
    print(f"Alternative second-cue share = {other_share}. Held-out discrepancy = {miss}.")
    print(f"Best common share = {best}. Minimum worst-cue discrepancy = {error} "
          f"({100 * float(error):.2f} points of probability mass).")

    # Same today's rate as the forecast, but twice as many unusable exchanges.
    excess_failures = probabilities(120, 170, 70, 40)
    assert excess_failures[1] == forecast[1]
    try:
        reading_share(*later_cue, excess_failures)
    except ValueError as exc:
        print("Extra interpretation failures:", exc)
    else:
        raise AssertionError("A fit to today's answers hid a failure on the other responses.")

    # Fixed example count tables at the displayed proportions, not random samples.
    for n in (80, 400):
        for label, later_target in (("stable", second), ("alternative", alternative)):
            tables = ((*earlier_cue, first), (*later_cue, later_target))
            assert all((n * p).denominator == 1 for table in tables for row in table for p in row)
            counts = [[[int(n * p) for p in row] for row in table] for table in tables]
            bounds = share_bounds(counts)
            assert bounds is not None
            low, high = bounds
            if label == "stable":
                assert low <= share <= high
            print(f"{n} observations per row, {label} table: common shares "
                  f"retained by the 95% simultaneous screen [{low:.3f}, {high:.3f}].")


if __name__ == "__main__":
    run()
