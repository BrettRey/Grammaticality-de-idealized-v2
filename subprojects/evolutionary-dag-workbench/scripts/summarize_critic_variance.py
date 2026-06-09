#!/usr/bin/env python3
"""Summarize critic-verdict variance for one evaluation."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"{path} did not contain a JSON object")
    return data


def expected_prediction_statuses(evaluation: dict) -> dict[str, str]:
    statuses: dict[str, str] = {}
    for test in evaluation.get("prediction_tests", []):
        if not isinstance(test, dict):
            continue
        test_id = test.get("id")
        status = test.get("evidence_status")
        if isinstance(test_id, str) and isinstance(status, str):
            statuses[test_id] = status
    return statuses


def expected_card_results(evaluation: dict) -> dict[str, str]:
    results: dict[str, str] = {}
    for card in evaluation.get("cards", []):
        if not isinstance(card, dict):
            continue
        phenomenon = card.get("phenomenon")
        result = card.get("result")
        if isinstance(phenomenon, str) and isinstance(result, str):
            results[phenomenon] = result
    return results


def summarize_prediction_tests(evaluation: dict, runs: list[dict]) -> list[dict[str, str | int]]:
    expected = expected_prediction_statuses(evaluation)
    labels: dict[str, list[str]] = defaultdict(list)
    for run in runs:
        for verdict in run.get("prediction_test_verdicts", []):
            if not isinstance(verdict, dict):
                continue
            test_id = verdict.get("id")
            status = verdict.get("evidence_status")
            if isinstance(test_id, str) and isinstance(status, str):
                labels[test_id].append(status)

    rows: list[dict[str, str | int]] = []
    for test_id in sorted(expected):
        observed = labels.get(test_id, [])
        counts = Counter(observed)
        majority = counts.most_common(1)[0][0] if counts else ""
        rows.append(
            {
                "item_type": "prediction_test",
                "id": test_id,
                "expected": expected[test_id],
                "runs": len(observed),
                "unique_labels": len(counts),
                "majority_label": majority,
                "majority_count": counts.get(majority, 0) if majority else 0,
                "matches_expected": counts.get(expected[test_id], 0),
                "label_counts": ";".join(f"{label}:{count}" for label, count in sorted(counts.items())),
            }
        )
    return rows


def summarize_cards(evaluation: dict, runs: list[dict]) -> list[dict[str, str | int]]:
    expected = expected_card_results(evaluation)
    labels: dict[str, list[str]] = defaultdict(list)
    for run in runs:
        for verdict in run.get("card_result_verdicts", []):
            if not isinstance(verdict, dict):
                continue
            phenomenon = verdict.get("phenomenon")
            result = verdict.get("result")
            if isinstance(phenomenon, str) and isinstance(result, str):
                labels[phenomenon].append(result)

    rows: list[dict[str, str | int]] = []
    for phenomenon in sorted(expected):
        observed = labels.get(phenomenon, [])
        counts = Counter(observed)
        majority = counts.most_common(1)[0][0] if counts else ""
        rows.append(
            {
                "item_type": "card_result",
                "id": phenomenon,
                "expected": expected[phenomenon],
                "runs": len(observed),
                "unique_labels": len(counts),
                "majority_label": majority,
                "majority_count": counts.get(majority, 0) if majority else 0,
                "matches_expected": counts.get(expected[phenomenon], 0),
                "label_counts": ";".join(f"{label}:{count}" for label, count in sorted(counts.items())),
            }
        )
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("evaluation", type=Path)
    parser.add_argument("runs", nargs="+", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    evaluation_path = args.evaluation
    if not evaluation_path.is_absolute():
        evaluation_path = ROOT / evaluation_path
    evaluation = load_json(evaluation_path)
    runs = [load_json(path if path.is_absolute() else ROOT / path) for path in args.runs]

    rows = [
        *summarize_prediction_tests(evaluation, runs),
        *summarize_cards(evaluation, runs),
    ]

    fieldnames = [
        "item_type",
        "id",
        "expected",
        "runs",
        "unique_labels",
        "majority_label",
        "majority_count",
        "matches_expected",
        "label_counts",
    ]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
