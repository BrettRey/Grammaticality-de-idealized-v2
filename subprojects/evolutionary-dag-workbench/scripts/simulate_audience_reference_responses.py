#!/usr/bin/env python3
"""Generate a simulation-only audience/reference response CSV."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

from build_audience_reference_pilot_packet import CHANNEL_TO_TASK, TEMPLATE_FIELDS, read_csv


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DIR = ROOT / "data" / "audience-reference-projection"
DEFAULT_STIMULI = DEFAULT_DIR / "stimulus-register.csv"
DEFAULT_CHANNELS = DEFAULT_DIR / "response-channel-schema.csv"
DEFAULT_OUTPUT = DEFAULT_DIR / "simulations" / "structured-critic-simulation-2026-06-09.csv"


REFERENCE_CONFIDENCE = {
    "aud-ref-001": 7,
    "aud-ref-002": 7,
    "aud-pol-001": 7,
    "aud-pol-002": 7,
    "aud-pol-003": 7,
    "aud-amb-001": 3,
    "aud-amb-002": 3,
    "aud-pers-001": 7,
    "aud-pers-002": 7,
    "aud-chain-001": 5,
    "aud-chain-002": 7,
}

FEATURE_FIT = {
    "aud-ref-001": 6,
    "aud-ref-002": 7,
    "aud-pol-001": 6,
    "aud-pol-002": 5,
    "aud-pol-003": 7,
    "aud-amb-001": 5,
    "aud-amb-002": 5,
    "aud-pers-001": 6,
    "aud-pers-002": 6,
    "aud-chain-001": 4,
    "aud-chain-002": 6,
}

ACCEPTABILITY = {
    "aud-ref-001": 6,
    "aud-ref-002": 7,
    "aud-pol-001": 6,
    "aud-pol-002": 4,
    "aud-pol-003": 7,
    "aud-amb-001": 4,
    "aud-amb-002": 4,
    "aud-pers-001": 6,
    "aud-pers-002": 6,
    "aud-chain-001": 4,
    "aud-chain-002": 6,
}

ATTRIBUTION = {
    "aud-ref-001": "no_problem",
    "aud-ref-002": "no_problem",
    "aud-pol-001": "no_problem",
    "aud-pol-002": "grammar_error",
    "aud-pol-003": "no_problem",
    "aud-amb-001": "reference_ambiguity",
    "aud-amb-002": "reference_ambiguity",
    "aud-pers-001": "no_problem",
    "aud-pers-002": "no_problem",
    "aud-chain-001": "reference_ambiguity",
    "aud-chain-002": "no_problem",
}

SANCTION = {
    "aud-ref-001": "leave_alone",
    "aud-ref-002": "leave_alone",
    "aud-pol-001": "leave_alone",
    "aud-pol-002": "depends",
    "aud-pol-003": "leave_alone",
    "aud-amb-001": "depends",
    "aud-amb-002": "depends",
    "aud-pers-001": "leave_alone",
    "aud-pers-002": "leave_alone",
    "aud-chain-001": "depends",
    "aud-chain-002": "leave_alone",
}

NORM_ORIENTATION = {
    "descriptive_usage": "ordinary_conversation",
    "school_standard": "school_correctness",
    "institutional_policy": "workplace_policy",
    "community_local_norm": "community_local_norm",
}


def reference_success(item: dict[str, str]) -> str:
    if item["reference_expected"] == "ambiguous":
        return "ambiguous"
    return "yes"


def simulated_response(item: dict[str, str], task: str) -> dict[str, str]:
    item_id = item["item_id"]
    response = {
        "raw_response": "",
        "reference_success": "",
        "reference_confidence": "",
        "feature_fit_score": "",
        "acceptability_score": "",
        "attribution_label": "",
        "sanction_label": "",
        "norm_orientation_label": "",
    }

    if task == "reference_resolution":
        response["raw_response"] = item["reference_expected"]
        response["reference_success"] = reference_success(item)
        response["reference_confidence"] = str(REFERENCE_CONFIDENCE[item_id])
    elif task == "feature_fit":
        response["raw_response"] = str(FEATURE_FIT[item_id])
        response["feature_fit_score"] = str(FEATURE_FIT[item_id])
    elif task == "naturalness":
        response["raw_response"] = str(ACCEPTABILITY[item_id])
        response["acceptability_score"] = str(ACCEPTABILITY[item_id])
    elif task == "grammaticality_attribution":
        response["raw_response"] = ATTRIBUTION[item_id]
        response["attribution_label"] = ATTRIBUTION[item_id]
    elif task == "respect_social_sanction":
        response["raw_response"] = SANCTION[item_id]
        response["sanction_label"] = SANCTION[item_id]
    elif task == "policy_compliance":
        response["raw_response"] = NORM_ORIENTATION[item["norm_centre"]]
        response["norm_orientation_label"] = NORM_ORIENTATION[item["norm_centre"]]
    return response


def build_rows(
    stimuli: list[dict[str, str]],
    channels: list[dict[str, str]],
    run_id: str,
    participant_id: str,
) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for item in stimuli:
        for channel in channels:
            channel_id = channel["channel_id"]
            task = CHANNEL_TO_TASK[channel_id]
            row = {
                "run_id": run_id,
                "item_id": item["item_id"],
                "participant_id": participant_id,
                "condition_id": f"{item['item_id']}::{channel_id}",
                "cell_id": item["cell_id"],
                "referent_status": item["referent_status"],
                "pro_form_pattern": item["pro_form_pattern"],
                "audience_or_evaluator": item["audience_or_evaluator"],
                "norm_centre": item["norm_centre"],
                "task_prompt": task,
                "speaker_identity": item["speaker_identity"],
                "counts_as_prediction_evidence": "no",
                "exclusion_reason": "blank",
                "notes": "simulation-only dry run; not participant, corpus, or critic evidence",
            }
            row.update(simulated_response(item, task))
            rows.append(row)
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stimuli", type=Path, default=DEFAULT_STIMULI)
    parser.add_argument("--channels", type=Path, default=DEFAULT_CHANNELS)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--run-id", default="audience-reference-structured-critic-simulation")
    parser.add_argument("--participant-id", default="simulation-001")
    args = parser.parse_args()

    rows = build_rows(
        read_csv(args.stimuli),
        read_csv(args.channels),
        args.run_id,
        args.participant_id,
    )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=TEMPLATE_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    print(f"wrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
