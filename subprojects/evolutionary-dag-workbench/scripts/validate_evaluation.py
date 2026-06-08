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
SCORE_CHANGE_DECISION = "score-change-proposed"
PATH_READINGS = {
    "positive",
    "negative",
    "warranting",
    "undercutting",
    "component",
    "indeterminate",
    "non_sign_propagating",
    "unprofiled",
}
SIGN_PROFILES = {
    "positive_monotone": 1,
    "negative_monotone": -1,
    "noisy_positive_indicator": 1,
    "noisy_negative_indicator": -1,
}
INDETERMINATE_PROFILES = {
    "mixed_contextual",
    "threshold_or_nonlinear",
    "task_biased_indicator",
    "contextual_warrant",
}
WARRANT_PROFILES = {
    "evidential_warrant": "warranting",
    "evidential_undercut": "undercutting",
}
COMPONENT_PROFILES = {
    "partial_component",
    "necessary_component",
    "definitional_component",
}


def load_json(path: Path) -> dict | None:
    try:
        with path.open(encoding="utf-8") as handle:
            data = json.load(handle)
    except Exception:
        return None
    return data if isinstance(data, dict) else None


def known_card_ids() -> set[str]:
    return {path.stem for path in (ROOT / "phenomena" / "cards").glob("*.md")}


def known_evaluation_ids() -> set[str]:
    ids: set[str] = set()
    for path in (ROOT / "evaluations" / "protocol-tests").glob("*.json"):
        ids.add(path.stem)
        data = load_json(path)
        if data and isinstance(data.get("id"), str) and data["id"].strip():
            ids.add(data["id"])
    return ids


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


def check_requirement_edge(
    edge: object,
    path: Path,
    card_index: int,
    requirement_key: str,
    edge_index: int,
    graph_edges: dict[tuple[str, str, str], dict],
    *,
    should_exist: bool,
) -> list[str]:
    prefix = f"{path}: card {card_index} {requirement_key} edge {edge_index}"
    if not isinstance(edge, dict):
        return [f"{prefix} must be an object"]

    errors: list[str] = []
    values: dict[str, str] = {}
    for key in ("source", "target", "type"):
        value = edge.get(key)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{prefix}: missing non-empty string field {key!r}")
        else:
            values[key] = value
    if errors:
        return errors

    edge_key = (values["source"], values["target"], values["type"])
    exists = edge_key in graph_edges
    if should_exist and not exists:
        errors.append(
            f"{prefix}: required edge {values['source']!r} -> {values['target']!r} "
            f"of type {values['type']!r} does not exist in target_graph"
        )
    if not should_exist and exists:
        errors.append(
            f"{prefix}: forbidden edge {values['source']!r} -> {values['target']!r} "
            f"of type {values['type']!r} exists in target_graph"
        )
    return errors


def check_card_requirements(
    card: dict,
    path: Path,
    index: int,
    target_graph: dict | None,
) -> list[str]:
    requirements = card.get("requirements")
    if requirements is None:
        return []
    prefix = f"{path}: card {index} requirements"
    if not isinstance(requirements, dict) or not requirements:
        return [f"{prefix} must be a non-empty object when present"]
    if target_graph is None:
        return [f"{prefix}: cannot validate requirements without a target_graph JSON object"]

    errors: list[str] = []
    graph_nodes = set(target_graph.get("nodes", []))
    graph_edges = graph_edge_index(target_graph)

    allowed_keys = {"required_nodes", "forbidden_nodes", "required_edges", "forbidden_edges"}
    for key in requirements:
        if key not in allowed_keys:
            allowed = ", ".join(sorted(allowed_keys))
            errors.append(f"{prefix}: unknown key {key!r}; expected one of {allowed}")

    for key, should_exist in (("required_nodes", True), ("forbidden_nodes", False)):
        values = requirements.get(key, [])
        if not isinstance(values, list):
            errors.append(f"{prefix}: {key} must be a list when present")
            continue
        for node_index, node in enumerate(values, start=1):
            if not isinstance(node, str) or not node.strip():
                errors.append(f"{prefix}: {key} item {node_index} must be a non-empty string")
                continue
            exists = node in graph_nodes
            if should_exist and not exists:
                errors.append(f"{prefix}: required node {node!r} does not exist in target_graph")
            if not should_exist and exists:
                errors.append(f"{prefix}: forbidden node {node!r} exists in target_graph")

    edge_requirements = (
        ("required_edges", True),
        ("forbidden_edges", False),
    )
    for key, should_exist in edge_requirements:
        values = requirements.get(key, [])
        if not isinstance(values, list):
            errors.append(f"{prefix}: {key} must be a list when present")
            continue
        for edge_index, edge in enumerate(values, start=1):
            errors.extend(
                check_requirement_edge(
                    edge,
                    path,
                    index,
                    key,
                    edge_index,
                    graph_edges,
                    should_exist=should_exist,
                )
            )

    return errors


def check_card(card: object, path: Path, index: int, target_graph: dict | None) -> list[str]:
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

    errors.extend(check_card_requirements(card, path, index, target_graph))

    return errors


def graph_edge_index(graph: dict) -> dict[tuple[str, str, str], dict]:
    edges: dict[tuple[str, str, str], dict] = {}
    for edge in graph.get("edges", []):
        if not isinstance(edge, dict):
            continue
        source = edge.get("source")
        target = edge.get("target")
        edge_type = edge.get("type")
        if isinstance(source, str) and isinstance(target, str) and isinstance(edge_type, str):
            edges[(source, target, edge_type)] = edge
    return edges


def contrast_cell_index(cards: object) -> dict[str, set[str]]:
    index: dict[str, set[str]] = {}
    if not isinstance(cards, list):
        return index

    for card in cards:
        if not isinstance(card, dict):
            continue
        phenomenon = card.get("phenomenon")
        if not isinstance(phenomenon, str) or not phenomenon.strip():
            continue
        cells = card.get("contrast_cells")
        if not isinstance(cells, list):
            index.setdefault(phenomenon, set())
            continue
        for cell in cells:
            if not isinstance(cell, dict):
                continue
            cell_id = cell.get("id")
            if isinstance(cell_id, str) and cell_id.strip():
                index.setdefault(phenomenon, set()).add(cell_id)
    return index


def check_activated_path_edge(
    edge: object,
    path: Path,
    path_index: int,
    edge_index: int,
    graph_edges: dict[tuple[str, str, str], dict],
    *,
    require_profile: bool,
) -> tuple[list[str], str | None, str | None, str | None]:
    prefix = f"{path}: activated path {path_index} edge {edge_index}"
    if not isinstance(edge, dict):
        return [f"{prefix} must be an object"], None, None, None

    errors: list[str] = []
    values: dict[str, str] = {}
    for key in ("source", "target", "type"):
        value = edge.get(key)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{prefix}: missing non-empty string field {key!r}")
        else:
            values[key] = value

    if errors:
        return errors, values.get("source"), values.get("target"), None

    key = (values["source"], values["target"], values["type"])
    graph_edge = graph_edges.get(key)
    relation_profile = None
    if graph_edge is None:
        errors.append(
            f"{prefix}: edge {values['source']!r} -> {values['target']!r} "
            f"of type {values['type']!r} does not exist in target_graph"
        )
    else:
        profile = graph_edge.get("relation_profile")
        if isinstance(profile, str) and profile.strip():
            relation_profile = profile
        elif require_profile:
            errors.append(
                f"{prefix}: score-change-proposed activated edges require relation_profile "
                "on the target graph edge"
            )

    return errors, values["source"], values["target"], relation_profile


def computed_path_reading(profiles: list[str | None]) -> str:
    if any(profile is None for profile in profiles):
        return "unprofiled"

    concrete_profiles = [profile for profile in profiles if profile is not None]
    if any(profile in INDETERMINATE_PROFILES for profile in concrete_profiles):
        return "indeterminate"

    if all(profile in SIGN_PROFILES for profile in concrete_profiles):
        sign = 1
        for profile in concrete_profiles:
            sign *= SIGN_PROFILES[profile]
        return "positive" if sign > 0 else "negative"

    if all(profile in WARRANT_PROFILES for profile in concrete_profiles):
        readings = {WARRANT_PROFILES[profile] for profile in concrete_profiles}
        if len(readings) == 1:
            return readings.pop()
        return "indeterminate"

    if all(profile in COMPONENT_PROFILES for profile in concrete_profiles):
        return "component"

    return "non_sign_propagating"


def check_activated_paths(data: dict, path: Path, target_graph: dict | None) -> list[str]:
    activated_paths = data.get("activated_paths")
    requires_paths = data.get("score_decision") == SCORE_CHANGE_DECISION

    if activated_paths is None:
        if requires_paths:
            return [f"{path}: score-change-proposed evaluations require activated_paths"]
        return []

    if not isinstance(activated_paths, list) or not activated_paths:
        return [f"{path}: activated_paths must be a non-empty list when present"]

    if target_graph is None:
        return [f"{path}: cannot validate activated_paths without a target_graph JSON object"]

    errors: list[str] = []
    graph_edges = graph_edge_index(target_graph)
    cells_by_phenomenon = contrast_cell_index(data.get("cards"))

    for path_index, activated_path in enumerate(activated_paths, start=1):
        prefix = f"{path}: activated path {path_index}"
        if not isinstance(activated_path, dict):
            errors.append(f"{prefix} must be an object")
            continue

        for key in ("id", "phenomenon", "contrast_cell", "prediction"):
            value = activated_path.get(key)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{prefix}: missing non-empty string field {key!r}")

        expected_reading = activated_path.get("expected_path_reading")
        if expected_reading is None:
            if requires_paths:
                errors.append(
                    f"{prefix}: score-change-proposed activated paths require "
                    "expected_path_reading"
                )
        elif not isinstance(expected_reading, str) or not expected_reading.strip():
            errors.append(f"{prefix}: expected_path_reading must be a non-empty string")
        elif expected_reading not in PATH_READINGS:
            allowed = ", ".join(sorted(PATH_READINGS))
            errors.append(
                f"{prefix}: expected_path_reading {expected_reading!r} is not allowed; "
                f"expected one of {allowed}"
            )

        phenomenon = activated_path.get("phenomenon")
        if isinstance(phenomenon, str) and phenomenon.strip():
            if phenomenon not in cells_by_phenomenon:
                errors.append(
                    f"{prefix}: phenomenon {phenomenon!r} is not present in evaluation cards"
                )
            else:
                contrast_cell = activated_path.get("contrast_cell")
                if isinstance(contrast_cell, str) and contrast_cell.strip():
                    if contrast_cell not in cells_by_phenomenon[phenomenon]:
                        errors.append(
                            f"{prefix}: contrast_cell {contrast_cell!r} is not present "
                            f"for phenomenon {phenomenon!r}"
                        )

        edges = activated_path.get("edges")
        if not isinstance(edges, list) or not edges:
            errors.append(f"{prefix}: edges must be a non-empty list")
            continue

        previous_target: str | None = None
        relation_profiles: list[str | None] = []
        for edge_index, edge in enumerate(edges, start=1):
            edge_errors, source, target, relation_profile = check_activated_path_edge(
                edge,
                path,
                path_index,
                edge_index,
                graph_edges,
                require_profile=requires_paths,
            )
            errors.extend(edge_errors)
            relation_profiles.append(relation_profile)
            if previous_target is not None and source is not None and source != previous_target:
                errors.append(
                    f"{prefix}: edge {edge_index} source {source!r} does not continue "
                    f"from previous target {previous_target!r}"
                )
            previous_target = target

        if isinstance(expected_reading, str) and expected_reading in PATH_READINGS:
            actual_reading = computed_path_reading(relation_profiles)
            if expected_reading != actual_reading:
                errors.append(
                    f"{prefix}: expected_path_reading {expected_reading!r} does not match "
                    f"computed path reading {actual_reading!r}"
                )

    return errors


def check_held_out_from(data: dict, path: Path) -> list[str]:
    status = data.get("status")
    if status != "held-out":
        return []

    held_out_from = data.get("held_out_from")
    if not isinstance(held_out_from, list) or not held_out_from:
        return [f"{path}: held-out evaluations require non-empty list field 'held_out_from'"]

    errors: list[str] = []
    allowed_sources = known_card_ids() | known_evaluation_ids()
    for index, item in enumerate(held_out_from, start=1):
        if not isinstance(item, str) or not item.strip():
            errors.append(f"{path}: held_out_from item {index} must be a non-empty string")
        elif item not in allowed_sources:
            errors.append(
                f"{path}: held_out_from item {index} {item!r} does not resolve to a "
                "phenomenon card ID or evaluation ID"
            )
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

    target_graph = None
    target_graph_value = data.get("target_graph")
    if isinstance(target_graph_value, str) and target_graph_value.strip():
        target_graph = load_json(ROOT / target_graph_value)

    status = data.get("status")
    if status not in STATUSES:
        allowed = ", ".join(sorted(STATUSES))
        errors.append(f"{path}: status {status!r} is not allowed; expected one of {allowed}")
    errors.extend(check_held_out_from(data, path))

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
            errors.extend(check_card(card, path, index, target_graph))

    errors.extend(check_activated_paths(data, path, target_graph))

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
