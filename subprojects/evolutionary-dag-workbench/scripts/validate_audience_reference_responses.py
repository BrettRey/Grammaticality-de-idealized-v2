#!/usr/bin/env python3
"""Validate audience/reference pilot response rows."""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DIR = ROOT / "data" / "audience-reference-projection"
DEFAULT_RESPONSES = DEFAULT_DIR / "pilot-response-template.csv"
DEFAULT_STIMULI = DEFAULT_DIR / "stimulus-register.csv"
DEFAULT_CHANNELS = DEFAULT_DIR / "response-channel-schema.csv"
DEFAULT_SCHEMA = DEFAULT_DIR / "coding-schema.csv"

CHANNEL_TO_TASK = {
    "reference_identification": "reference_resolution",
    "feature_personhood_fit": "feature_fit",
    "reported_acceptability": "naturalness",
    "grammaticality_attribution": "grammaticality_attribution",
    "social_sanction": "respect_social_sanction",
    "norm_orientation": "policy_compliance",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def enum_values(spec: str) -> set[str] | None:
    if not spec or spec in {"string", "string_or_blank", "1-7_or_blank"}:
        return None
    if "|" not in spec:
        return None
    return set(spec.split("|"))


def is_int_1_to_7(value: str) -> bool:
    try:
        parsed = int(value)
    except ValueError:
        return False
    return 1 <= parsed <= 7


def task_map(channels: list[dict[str, str]]) -> dict[str, str]:
    return {
        channel["channel_id"]: CHANNEL_TO_TASK[channel["channel_id"]]
        for channel in channels
        if channel["channel_id"] in CHANNEL_TO_TASK
    }


def expected_rows(
    stimuli: list[dict[str, str]],
    channels: list[dict[str, str]],
) -> set[tuple[str, str]]:
    mapping = task_map(channels)
    return {
        (stimulus["item_id"], mapping[channel["channel_id"]])
        for stimulus in stimuli
        for channel in channels
    }


def validate_rows(
    rows: list[dict[str, str]],
    stimuli: list[dict[str, str]],
    channels: list[dict[str, str]],
    schema_rows: list[dict[str, str]],
    require_responses: bool,
) -> list[str]:
    errors: list[str] = []
    stimulus_by_id = {row["item_id"]: row for row in stimuli}
    unknown_channels = [
        channel["channel_id"]
        for channel in channels
        if channel["channel_id"] not in CHANNEL_TO_TASK
    ]
    for channel_id in unknown_channels:
        errors.append(f"response-channel schema has no task mapping for {channel_id!r}")

    channel_tasks = set(task_map(channels).values())
    fields = [row["field"] for row in schema_rows]
    schema_by_field = {row["field"]: row for row in schema_rows}

    for index, row in enumerate(rows, start=2):
        missing = [field for field in fields if field not in row]
        if missing:
            errors.append(f"row {index}: missing fields: {', '.join(missing)}")
            continue

        item_id = row["item_id"]
        stimulus = stimulus_by_id.get(item_id)
        if stimulus is None:
            errors.append(f"row {index}: unknown item_id {item_id!r}")
            continue

        for field in [
            "cell_id",
            "referent_status",
            "pro_form_pattern",
            "audience_or_evaluator",
            "norm_centre",
            "speaker_identity",
        ]:
            if row[field] != stimulus[field]:
                errors.append(
                    f"row {index}: {field}={row[field]!r} does not match stimulus "
                    f"{item_id} value {stimulus[field]!r}"
                )

        if row["task_prompt"] not in channel_tasks:
            errors.append(f"row {index}: unknown task_prompt {row['task_prompt']!r}")

        for field, schema_row in schema_by_field.items():
            value = row.get(field, "")
            if value == "":
                continue
            values = enum_values(schema_row["allowed_values"])
            if values is not None and value not in values:
                errors.append(f"row {index}: {field}={value!r} is not one of {sorted(values)}")

        for field in ["reference_confidence", "feature_fit_score", "acceptability_score"]:
            value = row.get(field, "")
            if value and not is_int_1_to_7(value):
                errors.append(f"row {index}: {field}={value!r} is not an integer from 1 to 7")

        if require_responses and not row.get("raw_response", "").strip():
            errors.append(f"row {index}: raw_response is required")

    observed = {(row.get("item_id", ""), row.get("task_prompt", "")) for row in rows}
    expected = expected_rows(stimuli, channels)
    missing_expected = sorted(expected - observed)
    counts: dict[tuple[str, str], int] = {}
    for row in rows:
        key = (row.get("item_id", ""), row.get("task_prompt", ""))
        counts[key] = counts.get(key, 0) + 1
    duplicate_keys = sorted(key for key, count in counts.items() if count > 1)
    for item_id, task in missing_expected:
        errors.append(f"missing expected row for item_id={item_id!r}, task_prompt={task!r}")
    for item_id, task in duplicate_keys:
        errors.append(f"duplicate row for item_id={item_id!r}, task_prompt={task!r}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("responses", nargs="?", type=Path, default=DEFAULT_RESPONSES)
    parser.add_argument("--stimuli", type=Path, default=DEFAULT_STIMULI)
    parser.add_argument("--channels", type=Path, default=DEFAULT_CHANNELS)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument("--require-responses", action="store_true")
    args = parser.parse_args()

    schema_rows = read_csv(args.schema)
    rows = read_csv(args.responses)
    stimuli = read_csv(args.stimuli)
    channels = read_csv(args.channels)

    errors = validate_rows(rows, stimuli, channels, schema_rows, args.require_responses)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print(f"ok: {args.responses} ({len(rows)} rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
