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


def is_evidence_usable(row: dict[str, str]) -> bool:
    if row.get("counts_as_prediction_evidence") == "no":
        return False
    if row.get("exclusion_reason") not in {"", "blank"}:
        return False
    return has_response(row)


def is_summarized(row: dict[str, str], include_non_evidence: bool) -> bool:
    if row.get("exclusion_reason") not in {"", "blank"}:
        return False
    if row.get("counts_as_prediction_evidence") == "no" and not include_non_evidence:
        return False
    return has_response(row)


def mean(values: list[int]) -> str:
    if not values:
        return "n/a"
    return f"{sum(values) / len(values):.2f}"


def summarize_rows(
    rows: list[dict[str, str]],
    include_non_evidence: bool,
) -> dict[tuple[str, str], list[dict[str, str]]]:
    grouped: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        if is_summarized(row, include_non_evidence):
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


def prediction_items(prediction: dict[str, str]) -> set[str]:
    item_ids = prediction.get("item_ids", "")
    if not item_ids:
        return set()
    return {item_id for item_id in item_ids.split("|") if item_id}


def validate_predictions(
    predictions: list[dict[str, str]],
    stimuli: list[dict[str, str]],
) -> list[str]:
    errors: list[str] = []
    stimulus_by_id = {row["item_id"]: row for row in stimuli}
    for prediction in predictions:
        prediction_id = prediction.get("prediction_id", "<missing prediction_id>")
        item_ids = prediction_items(prediction)
        if not item_ids:
            errors.append(f"prediction {prediction_id!r} must declare non-empty item_ids")
            continue
        for item_id in sorted(item_ids):
            stimulus = stimulus_by_id.get(item_id)
            if stimulus is None:
                errors.append(
                    f"prediction {prediction_id!r} item_id {item_id!r} is not in stimulus register"
                )
            elif stimulus["cell_id"] != prediction.get("cell_id", ""):
                errors.append(
                    f"prediction {prediction_id!r} item_id {item_id!r} has cell_id "
                    f"{stimulus['cell_id']!r}, not prediction cell {prediction.get('cell_id', '')!r}"
                )
    return errors


def markdown_report(
    responses_path: Path,
    rows: list[dict[str, str]],
    predictions: list[dict[str, str]],
    include_non_evidence: bool,
) -> str:
    evidence_usable_rows = [row for row in rows if is_evidence_usable(row)]
    summarized_rows = [row for row in rows if is_summarized(row, include_non_evidence)]
    grouped = summarize_rows(rows, include_non_evidence)
    lines = [
        "# Audience Reference Response Summary",
        "",
        f"**Response file:** `{responses_path}`",
        f"**Rows:** {len(rows)}",
        f"**Usable response rows:** {len(evidence_usable_rows)}",
        f"**Summarized response rows:** {len(summarized_rows)}",
        f"**Includes non-evidence rows:** {'yes' if include_non_evidence else 'no'}",
        "",
        "This summary is descriptive only. It does not assign pass/fail outcomes or update",
        "workbench evidence labels.",
        "",
        "## Prediction Cells",
        "",
    ]

    for prediction in predictions:
        prediction_id = prediction["prediction_id"]
        cell_id = prediction["cell_id"]
        item_ids = prediction_items(prediction)
        prediction_rows = [
            row
            for row in summarized_rows
            if row["cell_id"] == cell_id and (not item_ids or row["item_id"] in item_ids)
        ]
        prediction_all_rows = [
            row
            for row in rows
            if row["cell_id"] == cell_id and (not item_ids or row["item_id"] in item_ids)
        ]
        lines.extend(
            [
                f"### {prediction_id}",
                "",
                f"- Cell: `{cell_id}`",
                f"- Items: {', '.join(sorted(item_ids)) if item_ids else 'all cell items'}",
                f"- Summarized rows: {len(prediction_rows)}",
                "",
            ]
        )
        for task in sorted({row["task_prompt"] for row in prediction_all_rows}):
            task_rows = grouped.get((cell_id, task), [])
            if item_ids:
                task_rows = [row for row in task_rows if row["item_id"] in item_ids]
            lines.append(f"#### {task}")
            lines.append("")
            lines.append(f"- Summarized rows: {len(task_rows)}")
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
    parser.add_argument(
        "--include-non-evidence",
        action="store_true",
        help="include validated rows marked counts_as_prediction_evidence=no in the summary",
    )
    parser.add_argument("--require-responses", action="store_true")
    args = parser.parse_args()

    schema_rows = read_csv(args.schema)
    rows = read_csv(args.responses)
    stimuli = read_csv(args.stimuli)
    channels = read_csv(args.channels)
    predictions = read_csv(args.predictions)

    errors = validate_rows(rows, stimuli, channels, schema_rows, args.require_responses)
    errors.extend(validate_predictions(predictions, stimuli))
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    report = markdown_report(args.responses, rows, predictions, args.include_non_evidence)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report, encoding="utf-8")
        print(f"wrote {args.output}")
    else:
        print(report, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
