#!/usr/bin/env python3
"""Validate protocol-bound evaluation JSON files."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

AXES = {
    "community",
    "norm_centre",
    "genre",
    "medium",
    "task_framing",
    "speaker_identity",
}
REQUIRED_CONTRAST_CELL_AXES = AXES
RESULTS = {
    "survives_as_module",
    "partly_survives",
    "fails",
    "fails_general_out_of_scope",
    "exploratory",
}
SCORE_DECISIONS = {
    "no-score-change",
    "score-change-proposed",
    "scope-only",
}
STATUSES = {
    "exploratory",
    "protocol-bound",
    "held-out",
    "archived",
}


def load_json(path: Path) -> dict | None:
    try:
        with path.open(encoding="utf-8") as handle:
            data = json.load(handle)
    except Exception:
        return None
    return data if isinstance(data, dict) else None


def require_string(data: dict, key: str, path: Path) -> list[str]:
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        return [f"{path}: missing non-empty string field {key!r}"]
    return []


def check_path_field(data: dict, key: str, path: Path) -> list[str]:
    errors = require_string(data, key, path)
    if errors:
        return errors
    target = ROOT / data[key]
    if not target.exists():
        return [f"{path}: {key} path does not exist: {data[key]!r}"]
    return []


def check_contrast_cell(cell: object, path: Path, card_index: int, cell_index: int) -> list[str]:
    prefix = f"{path}: card {card_index} contrast cell {cell_index}"
    if not isinstance(cell, dict):
        return [f"{prefix} must be an object"]

    errors: list[str] = []
    if not isinstance(cell.get("id"), str) or not cell["id"].strip():
        errors.append(f"{prefix}: missing non-empty string field 'id'")

    axes = cell.get("axes")
    if not isinstance(axes, dict) or not axes:
        errors.append(f"{prefix}: axes must be a non-empty object")
        return errors

    for axis, value in axes.items():
        if axis not in AXES:
            allowed = ", ".join(sorted(AXES))
            errors.append(f"{prefix}: unknown axis {axis!r}; expected one of {allowed}")
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{prefix}: axis {axis!r} must have a non-empty string value")

    missing_axes = sorted(REQUIRED_CONTRAST_CELL_AXES - set(axes))
    for axis in missing_axes:
        errors.append(f"{prefix}: missing required axis {axis!r}")

    return errors


def check_card(card: object, path: Path, index: int) -> list[str]:
    prefix = f"{path}: card {index}"
    if not isinstance(card, dict):
        return [f"{prefix} must be an object"]

    errors: list[str] = []
    errors.extend(require_string(card, "phenomenon", path))
    errors.extend(require_string(card, "expected_survival_pattern", path))

    phenomenon = card.get("phenomenon")
    if isinstance(phenomenon, str) and phenomenon.strip():
        card_path = ROOT / "phenomena" / "cards" / f"{phenomenon}.md"
        if not card_path.exists():
            errors.append(f"{prefix}: phenomenon card does not exist: {phenomenon!r}")

    result = card.get("result")
    if result not in RESULTS:
        allowed = ", ".join(sorted(RESULTS))
        errors.append(f"{prefix}: result {result!r} is not allowed; expected one of {allowed}")

    cells = card.get("contrast_cells")
    if not isinstance(cells, list) or not cells:
        errors.append(f"{prefix}: contrast_cells must be a non-empty list")
    else:
        for cell_index, cell in enumerate(cells, start=1):
            errors.extend(check_contrast_cell(cell, path, index, cell_index))

    return errors


def validate(path: Path) -> list[str]:
    data = load_json(path)
    if data is None:
        return [f"{path}: cannot load JSON object"]

    errors: list[str] = []
    for key in ("id", "target_graph", "protocol", "status", "score_decision"):
        errors.extend(require_string(data, key, path))
    errors.extend(check_path_field(data, "target_graph", path))
    errors.extend(check_path_field(data, "protocol", path))

    status = data.get("status")
    if status not in STATUSES:
        allowed = ", ".join(sorted(STATUSES))
        errors.append(f"{path}: status {status!r} is not allowed; expected one of {allowed}")

    score_decision = data.get("score_decision")
    if score_decision not in SCORE_DECISIONS:
        allowed = ", ".join(sorted(SCORE_DECISIONS))
        errors.append(
            f"{path}: score_decision {score_decision!r} is not allowed; expected one of {allowed}"
        )

    cards = data.get("cards")
    if not isinstance(cards, list) or not cards:
        errors.append(f"{path}: cards must be a non-empty list")
    else:
        for index, card in enumerate(cards, start=1):
            errors.extend(check_card(card, path, index))

    return errors


def main(argv: list[str]) -> int:
    if not argv:
        print("usage: validate_evaluation.py EVALUATION.json [EVALUATION.json ...]", file=sys.stderr)
        return 2

    all_errors: list[str] = []
    for raw_path in argv:
        path = Path(raw_path)
        errors = validate(path)
        if errors:
            all_errors.extend(errors)
        else:
            print(f"ok: {path}")

    if all_errors:
        for error in all_errors:
            print(error, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
