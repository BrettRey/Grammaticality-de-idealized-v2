#!/usr/bin/env python3
"""Score a graph that contains rubric dimensions in a JSON scores block."""

from __future__ import annotations

import json
import sys
from pathlib import Path


POSITIVE = [
    "empirical_coverage",
    "counterexample_resilience",
    "measurement_clarity",
    "explanatory_payoff",
    "cross_domain_stability",
]

PENALTIES = [
    "complexity_penalty",
    "circularity_penalty",
    "construct_confusion_penalty",
]


def numeric(scores: dict, key: str) -> float:
    value = scores.get(key, 0)
    if isinstance(value, bool):
        raise ValueError(f"score {key!r} must be numeric, got {value!r}")
    if isinstance(value, (int, float)):
        return float(value)
    raise ValueError(f"score {key!r} must be numeric, got {value!r}")


def score(path: Path) -> tuple[float, dict[str, float], dict]:
    with path.open(encoding="utf-8") as handle:
        graph = json.load(handle)

    scores = graph.get("scores")
    if not isinstance(scores, dict):
        raise ValueError(f"{path}: graph has no scores object")

    values = {key: numeric(scores, key) for key in POSITIVE + PENALTIES}
    total = sum(values[key] for key in POSITIVE) - sum(values[key] for key in PENALTIES)
    score_status = graph.get("score_status")
    if not isinstance(score_status, dict):
        score_status = {"kind": "unscored"}
    return total, values, score_status


def main(argv: list[str]) -> int:
    if not argv:
        print("usage: score_graph.py GRAPH.json [GRAPH.json ...]", file=sys.stderr)
        return 2

    errors: list[str] = []
    for raw_path in argv:
        path = Path(raw_path)
        try:
            total, values, score_status = score(path)
        except Exception as exc:  # noqa: BLE001 - CLI should report all scoring issues.
            errors.append(f"{path}: {exc}")
            continue

        print(f"{path}: total={total:g}")
        print(f"  score_status.kind: {score_status.get('kind', 'unscored')}")
        if score_status.get("evaluation"):
            print(f"  score_status.evaluation: {score_status['evaluation']}")
        if score_status.get("scope"):
            print(f"  score_status.scope: {score_status['scope']}")
        for key in POSITIVE + PENALTIES:
            print(f"  {key}: {values[key]:g}")

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
