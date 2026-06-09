#!/usr/bin/env python3
"""Build a compact critic-verdict variance packet for one evaluation."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


DEFAULT_EXTRA_FILES = {
    "agreement-controller-override-coca-projection-2026-06-09": [
        "notes/agr-coca-vertical-slice-report-2026-06-09.md",
        "notes/agr-coca-ablation-test-2026-06-09.md",
        "data/agr-coca-projection/summary.csv",
        "data/agr-coca-projection/baseline-discriminator.csv",
        "data/agr-coca-projection/uncertainty-summary.csv",
    ]
}


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"{path} did not contain a JSON object")
    return data


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def fence(label: str, body: str, language: str = "") -> str:
    return f"\n## {label}\n\n```{language}\n{body.rstrip()}\n```\n"


def compact_json(data: dict) -> str:
    return json.dumps(data, indent=2, ensure_ascii=False)


def packet(evaluation_path: Path, extra_files: list[str]) -> str:
    evaluation = load_json(evaluation_path)
    graph_path = ROOT / evaluation["target_graph"]
    graph = load_json(graph_path)

    lines = [
        "# Critic Verdict Variance Packet",
        "",
        "You are one independent critic pass for the evolutionary DAG workbench.",
        "",
        "Your job is not to improve the graph first. Your job is to decide whether the",
        "existing evaluation verdicts are stable under adversarial reading.",
        "",
        "Use only the packet contents. Do not assume outside facts.",
        "",
        "Return JSON only, matching this shape:",
        "",
        "```json",
        "{",
        '  "critic_id": "short identifier you choose",',
        '  "target_evaluation": "evaluation id",',
        '  "overall_score_decision": "no-score-change | scope-only | score-change-proposed",',
        '  "overall_stability": "stable | unstable | underdetermined",',
        '  "prediction_test_verdicts": [',
        "    {",
        '      "id": "prediction test id",',
        '      "evidence_status": "passed | failed | mixed | inconclusive | not-run",',
        '      "confidence": 0.0,',
        '      "reason": "one sentence"',
        "    }",
        "  ],",
        '  "card_result_verdicts": [',
        "    {",
        '      "phenomenon": "card id",',
        '      "result": "survives_as_module | partly_survives | fails | fails_general_out_of_scope | exploratory",',
        '      "confidence": 0.0,',
        '      "reason": "one sentence"',
        "    }",
        "  ],",
        '  "strongest_instability": "one sentence",',
        '  "score_movement_allowed": false,',
        '  "minimal_change": "one sentence"',
        "}",
        "```",
        "",
        "Important: do not award numeric score movement unless the packet itself contains",
        "enough evidence to justify it under the workbench scoring policy.",
    ]

    lines.append(fence("Target Evaluation JSON", compact_json(evaluation), "json"))
    lines.append(fence("Target Graph JSON", compact_json(graph), "json"))

    for card in evaluation.get("cards", []):
        if not isinstance(card, dict):
            continue
        phenomenon = card.get("phenomenon")
        if not isinstance(phenomenon, str) or not phenomenon.strip():
            continue
        card_path = ROOT / "phenomena" / "cards" / f"{phenomenon}.md"
        if card_path.exists():
            lines.append(fence(f"Phenomenon Card: {phenomenon}", read_text(card_path), "markdown"))

    for extra in extra_files:
        path = ROOT / extra
        if path.exists():
            suffix = path.suffix.removeprefix(".")
            lines.append(fence(f"Extra File: {extra}", read_text(path), suffix))

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("evaluation", type=Path)
    parser.add_argument("--extra", action="append", default=[], help="Extra file to include.")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    evaluation_path = args.evaluation
    if not evaluation_path.is_absolute():
        evaluation_path = ROOT / evaluation_path
    evaluation = load_json(evaluation_path)
    evaluation_id = evaluation.get("id", "")
    default_extras = DEFAULT_EXTRA_FILES.get(evaluation_id, [])
    body = packet(evaluation_path, [*default_extras, *args.extra])
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(body, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
