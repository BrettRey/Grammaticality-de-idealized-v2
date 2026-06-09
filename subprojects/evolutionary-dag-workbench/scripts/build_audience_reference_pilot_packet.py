#!/usr/bin/env python3
"""Build an audience/reference pilot packet and response template."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DIR = ROOT / "data" / "audience-reference-projection"
DEFAULT_STIMULI = DEFAULT_DIR / "stimulus-register.csv"
DEFAULT_CHANNELS = DEFAULT_DIR / "response-channel-schema.csv"
DEFAULT_OUTPUT = DEFAULT_DIR / "pilot-packet.md"
DEFAULT_TEMPLATE = DEFAULT_DIR / "pilot-response-template.csv"


TEMPLATE_FIELDS = [
    "run_id",
    "item_id",
    "participant_id",
    "condition_id",
    "cell_id",
    "referent_status",
    "pro_form_pattern",
    "audience_or_evaluator",
    "norm_centre",
    "task_prompt",
    "speaker_identity",
    "raw_response",
    "reference_success",
    "reference_confidence",
    "feature_fit_score",
    "acceptability_score",
    "attribution_label",
    "sanction_label",
    "norm_orientation_label",
    "counts_as_prediction_evidence",
    "exclusion_reason",
    "notes",
]


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


def write_response_template(
    path: Path,
    stimuli: list[dict[str, str]],
    channels: list[dict[str, str]],
    run_id: str,
) -> None:
    rows: list[dict[str, str]] = []
    for item in stimuli:
        for channel in channels:
            channel_id = channel["channel_id"]
            rows.append(
                {
                    "run_id": run_id,
                    "item_id": item["item_id"],
                    "participant_id": "",
                    "condition_id": f"{item['item_id']}::{channel_id}",
                    "cell_id": item["cell_id"],
                    "referent_status": item["referent_status"],
                    "pro_form_pattern": item["pro_form_pattern"],
                    "audience_or_evaluator": item["audience_or_evaluator"],
                    "norm_centre": item["norm_centre"],
                    "task_prompt": CHANNEL_TO_TASK.get(channel_id, channel_id),
                    "speaker_identity": item["speaker_identity"],
                    "raw_response": "",
                    "reference_success": "",
                    "reference_confidence": "",
                    "feature_fit_score": "",
                    "acceptability_score": "",
                    "attribution_label": "",
                    "sanction_label": "",
                    "norm_orientation_label": "",
                    "counts_as_prediction_evidence": "",
                    "exclusion_reason": "",
                    "notes": "",
                }
            )

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=TEMPLATE_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def markdown_packet(stimuli: list[dict[str, str]], channels: list[dict[str, str]]) -> str:
    lines = [
        "# Audience Reference Pilot Packet",
        "",
        "This packet is for a small pilot or structured critic run. It is not itself evidence.",
        "",
        "For each item, read the context and target sentence, then answer each response prompt",
        "separately. Do not collapse the prompts into a single acceptability judgment.",
        "",
        "Use the response template at `data/audience-reference-projection/pilot-response-template.csv`",
        "for row-level coding.",
        "",
        "## Response Channels",
        "",
    ]

    for channel in channels:
        lines.extend(
            [
                f"### {channel['channel_id']}",
                "",
                f"- Prompt: {channel['response_prompt']}",
                f"- Response type: {channel['response_type']}",
                f"- Scale or labels: {channel['scale_or_labels']}",
                "",
            ]
        )

    lines.append("## Stimuli")
    lines.append("")
    for item in stimuli:
        lines.extend(
            [
                f"### {item['item_id']}",
                "",
                f"- Cell: `{item['cell_id']}`",
                f"- Audience/evaluator: `{item['audience_or_evaluator']}`",
                f"- Norm centre: `{item['norm_centre']}`",
                f"- Speaker identity: `{item['speaker_identity']}`",
                "",
                "**Context**",
                "",
                item["context"],
                "",
                "**Target Sentence**",
                "",
                item["target_sentence"],
                "",
                "**Prompts**",
                "",
            ]
        )
        for channel in channels:
            lines.append(f"- `{channel['channel_id']}`: {channel['response_prompt']}")
        lines.append("")

    lines.extend(
        [
            "## Coding Boundary",
            "",
            "For evidence updates, code the response channels independently. A row can support the",
            "audience/reference prediction only if reference identification is recorded separately",
            "from acceptability, attribution, sanction, and norm orientation.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stimuli", type=Path, default=DEFAULT_STIMULI)
    parser.add_argument("--channels", type=Path, default=DEFAULT_CHANNELS)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--response-template", type=Path, default=DEFAULT_TEMPLATE)
    parser.add_argument("--run-id", default="audience-reference-pilot")
    args = parser.parse_args()

    stimuli = read_csv(args.stimuli)
    channels = read_csv(args.channels)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(markdown_packet(stimuli, channels), encoding="utf-8")
    write_response_template(args.response_template, stimuli, channels, args.run_id)

    print(f"wrote {args.output}")
    print(f"wrote {args.response_template}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
