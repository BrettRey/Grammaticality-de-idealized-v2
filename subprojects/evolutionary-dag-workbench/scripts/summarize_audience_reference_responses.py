#!/usr/bin/env python3
"""Summarize validated audience/reference pilot response rows."""

from __future__ import annotations

import argparse
import sys
from collections import Counter, defaultdict
from pathlib import Path

from validate_audience_reference_responses import (
    DEFAULT_CHANNELS,
    DEFAULT_RESPONSES,
    DEFAULT_SCHEMA,
    DEFAULT_STIMULI,
    read_csv,
    validate_rows,
)


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DIR = ROOT / "data" / "audience-reference-projection"
DEFAULT_PREDICTIONS = DEFAULT_DIR / "prediction-register.csv"

NUMERIC_FIELDS = [
    "reference_confidence",
    "feature_fit_score",
    "acceptability_score",
]

LABEL_FIELDS = [
    "reference_success",
    "attribution_label",
    "sanction_label",
    "norm_orientation_label",
]

CODED_FIELDS = [
    "raw_response",
    *NUMERIC_FIELDS,
    *LABEL_FIELDS,
]


def has_response(row: dict[str, str]) -> bool:
    return any(row.get(field, "").strip() for field in CODED_FIELDS)


def is_usable(row: dict[str, str]) -> bool:
    if row.get("counts_as_prediction_evidence") == "no":
        return False
    if row.get("exclusion_reason") not in {"", "blank"}:
        return False
    return has_response(row)


def mean(values: list[int]) -> str:
    if not values:
        return "n/a"
    return f"{sum(values) / len(values):.2f}"


def summarize_rows(rows: list[dict[str, str]]) -> dict[tuple[str, str], list[dict[str, str]]]:
    grouped: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        if is_usable(row):
            grouped[(row["cell_id"], row["task_prompt"])].append(row)
    return dict(grouped)


def numeric_summary(rows: list[dict[str, str]], field: str) -> str:
    values = [int(row[field]) for row in rows if row.get(field, "").isdigit()]
    return mean(values)


def label_summary(rows: list[dict[str, str]], field: str) -> str:
    counts = Counter(row[field] for row in rows if row.get(field, ""))
    if not counts:
        return "n/a"
    return "; ".join(f"{label}={count}" for label, count in sorted(counts.items()))


def prediction_cells(predictions: list[dict[str, str]]) -> list[tuple[str, str]]:
    return [(row["prediction_id"], row["cell_id"]) for row in predictions]


def markdown_report(
    responses_path: Path,
    rows: list[dict[str, str]],
    predictions: list[dict[str, str]],
) -> str:
    usable_rows = [row for row in rows if is_usable(row)]
    grouped = summarize_rows(rows)
    lines = [
        "# Audience Reference Response Summary",
        "",
        f"**Response file:** `{responses_path}`",
        f"**Rows:** {len(rows)}",
        f"**Usable response rows:** {len(usable_rows)}",
        "",
        "This summary is descriptive only. It does not assign pass/fail outcomes or update",
        "workbench evidence labels.",
        "",
        "## Prediction Cells",
        "",
    ]

    for prediction_id, cell_id in prediction_cells(predictions):
        cell_rows = [row for row in usable_rows if row["cell_id"] == cell_id]
        lines.extend(
            [
                f"### {prediction_id}",
                "",
                f"- Cell: `{cell_id}`",
                f"- Usable rows: {len(cell_rows)}",
                "",
            ]
        )
        for task in sorted({row["task_prompt"] for row in rows if row["cell_id"] == cell_id}):
            task_rows = grouped.get((cell_id, task), [])
            lines.append(f"#### {task}")
            lines.append("")
            lines.append(f"- Usable rows: {len(task_rows)}")
            for field in NUMERIC_FIELDS:
                summary = numeric_summary(task_rows, field)
                if summary != "n/a":
                    lines.append(f"- {field} mean: {summary}")
            for field in LABEL_FIELDS:
                summary = label_summary(task_rows, field)
                if summary != "n/a":
                    lines.append(f"- {field}: {summary}")
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("responses", nargs="?", type=Path, default=DEFAULT_RESPONSES)
    parser.add_argument("--stimuli", type=Path, default=DEFAULT_STIMULI)
    parser.add_argument("--channels", type=Path, default=DEFAULT_CHANNELS)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument("--predictions", type=Path, default=DEFAULT_PREDICTIONS)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--require-responses", action="store_true")
    args = parser.parse_args()

    schema_rows = read_csv(args.schema)
    rows = read_csv(args.responses)
    stimuli = read_csv(args.stimuli)
    channels = read_csv(args.channels)
    predictions = read_csv(args.predictions)

    errors = validate_rows(rows, stimuli, channels, schema_rows, args.require_responses)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    report = markdown_report(args.responses, rows, predictions)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report, encoding="utf-8")
        print(f"wrote {args.output}")
    else:
        print(report, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
