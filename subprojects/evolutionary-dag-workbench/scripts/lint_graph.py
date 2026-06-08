#!/usr/bin/env python3
"""Lint graph JSON files against the local ontology and scoring conventions."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import validate_graph


ROOT = Path(__file__).resolve().parents[1]
NODES_PATH = ROOT / "ontology" / "nodes.yaml"

STATUSES = {"seed", "candidate", "archived", "rejected", "superseded"}
SCORE_STATUS_KINDS = {"unscored", "scoped_module", "general_account"}
SCORABLE_STATUS_KINDS = {"scoped_module", "general_account"}
SCORING_EVALUATION_STATUSES = {"protocol-bound", "held-out"}
SCORING_EVALUATION_DECISION = "score-change-proposed"
SCORE_MIN = 0
SCORE_MAX = 5
SCORE_KEYS = [
    "empirical_coverage",
    "counterexample_resilience",
    "measurement_clarity",
    "explanatory_payoff",
    "cross_domain_stability",
    "complexity_penalty",
    "circularity_penalty",
    "construct_confusion_penalty",
]
CONDITIONING_AXIS_KEYS = {
    "community",
    "norm_centre",
    "genre",
    "medium",
    "task_framing",
    "speaker_identity",
}
CONDITIONING_AXIS_NODE_REQUIREMENTS = {
    "community": {"community_licensing"},
    "norm_centre": {
        "standard_language_ideology",
        "metalinguistic_condemnation",
        "editorial_correction_probability",
    },
    "genre": {"genre", "register_genre_appropriateness"},
    "medium": {"medium"},
    "task_framing": {"task_framing"},
    "speaker_identity": {"speaker_identity", "social_indexical_value"},
}
OUTCOME_NODE_BASES = {
    "reported_acceptability",
    "grammaticality_attribution",
    "production_probability",
    "editorial_correction_probability",
    "felt_naturalness_context",
    "community_licensing",
    "register_genre_appropriateness",
    "repair_reformulation_pressure",
    "metalinguistic_condemnation",
}
CONTEXT_INDEXED_REQUIRED_AXES = {
    "community",
    "norm_centre",
    "genre",
    "medium",
    "task_framing",
    "speaker_identity",
}

FAMILY_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
NODE_ID_PATTERN = re.compile(r"^\s*-\s+id:\s+([A-Za-z][A-Za-z0-9_]*)\s*$")
TIME_SLICE_PATTERN = re.compile(r"^(?P<base>.+)_t(?P<index>[0-9]*)$")


def load_controlled_nodes(path: Path = NODES_PATH) -> set[str]:
    node_ids: set[str] = set()
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            match = NODE_ID_PATTERN.match(line)
            if match:
                node_ids.add(match.group(1))
    if not node_ids:
        raise ValueError(f"{path}: no controlled node ids found")
    return node_ids


def load_json(path: Path) -> dict | None:
    try:
        with path.open(encoding="utf-8") as handle:
            data = json.load(handle)
    except Exception:
        return None
    return data if isinstance(data, dict) else None


def known_node(node: str, controlled_nodes: set[str]) -> bool:
    base = base_node_id(node)
    if base in controlled_nodes:
        return True
    return False


def base_node_id(node: str) -> str:
    match = TIME_SLICE_PATTERN.match(node)
    if not match:
        return node
    return match.group("base")


def score_value(scores: dict, key: str) -> float | None:
    value = scores.get(key)
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    return float(value)


def lint_family_and_status(graph: dict, path: Path) -> list[str]:
    errors: list[str] = []

    graph_id = graph.get("id")
    if not isinstance(graph_id, str) or not graph_id:
        errors.append(f"{path}: missing non-empty string field 'id'")
    elif graph_id != path.stem:
        errors.append(f"{path}: id {graph_id!r} must match filename stem {path.stem!r}")

    family = graph.get("family")
    if not isinstance(family, str) or not family:
        errors.append(f"{path}: missing non-empty string field 'family'")
    elif not FAMILY_PATTERN.fullmatch(family):
        errors.append(f"{path}: family {family!r} must be a lowercase hyphenated slug")

    status = graph.get("status")
    if not isinstance(status, str) or not status:
        errors.append(f"{path}: missing non-empty string field 'status'")
    elif status not in STATUSES:
        allowed = ", ".join(sorted(STATUSES))
        errors.append(f"{path}: status {status!r} is not allowed; expected one of {allowed}")

    return errors


def lint_nodes(graph: dict, path: Path, controlled_nodes: set[str]) -> list[str]:
    errors: list[str] = []
    seen: set[str] = set()

    for index, node in enumerate(graph.get("nodes", []), start=1):
        try:
            node = validate_graph.node_id(node)
        except ValueError as exc:
            errors.append(f"{path}: {exc}")
            continue

        if node in seen:
            errors.append(f"{path}: duplicate node id {node!r}")
        seen.add(node)

        if not known_node(node, controlled_nodes):
            errors.append(
                f"{path}: node {index} id {node!r} is not in ontology/nodes.yaml "
                "or a time-sliced extension of a controlled node"
            )

    return errors


def lint_scores(graph: dict, path: Path) -> list[str]:
    errors: list[str] = []
    scores = graph.get("scores")
    status = graph.get("status")

    if scores is None:
        if status == "seed":
            errors.append(f"{path}: seed graphs must include an all-zero scores block")
        return errors

    if not isinstance(scores, dict):
        return [f"{path}: scores must be an object"]

    missing = [key for key in SCORE_KEYS if key not in scores]
    extra = [key for key in scores if key not in SCORE_KEYS]
    for key in missing:
        errors.append(f"{path}: scores missing dimension {key!r}")
    for key in extra:
        errors.append(f"{path}: scores has unknown dimension {key!r}")

    values: dict[str, float] = {}
    for key in SCORE_KEYS:
        value = score_value(scores, key)
        if value is None:
            errors.append(f"{path}: score {key!r} must be numeric and not boolean")
        else:
            if value < SCORE_MIN or value > SCORE_MAX:
                errors.append(f"{path}: score {key!r} must be between {SCORE_MIN} and {SCORE_MAX}")
            values[key] = value

    if status == "seed":
        nonzero = [key for key, value in values.items() if value != 0]
        for key in nonzero:
            errors.append(f"{path}: seed score {key!r} must remain zero pending critique")

    return errors


def nonzero_scores(graph: dict) -> bool:
    scores = graph.get("scores")
    if not isinstance(scores, dict):
        return False

    for key in SCORE_KEYS:
        value = score_value(scores, key)
        if value is not None and value != 0:
            return True
    return False


def lint_score_status(graph: dict, path: Path) -> list[str]:
    errors: list[str] = []
    score_status = graph.get("score_status")
    has_nonzero_scores = nonzero_scores(graph)

    if score_status is None:
        if has_nonzero_scores:
            errors.append(f"{path}: non-zero scores require a score_status object")
        return errors

    if not isinstance(score_status, dict):
        return [f"{path}: score_status must be an object"]

    kind = score_status.get("kind")
    if kind not in SCORE_STATUS_KINDS:
        allowed = ", ".join(sorted(SCORE_STATUS_KINDS))
        errors.append(f"{path}: score_status.kind {kind!r} is not allowed; expected one of {allowed}")

    evaluation = score_status.get("evaluation")
    if evaluation is not None:
        if not isinstance(evaluation, str) or not evaluation.strip():
            errors.append(f"{path}: score_status.evaluation must be a non-empty string")
        elif not (ROOT / evaluation).exists():
            errors.append(f"{path}: score_status.evaluation path does not exist: {evaluation!r}")
        else:
            errors.extend(lint_score_evaluation_target(path, evaluation, require_score_authorized=has_nonzero_scores))

    if has_nonzero_scores:
        if kind not in SCORABLE_STATUS_KINDS:
            allowed = ", ".join(sorted(SCORABLE_STATUS_KINDS))
            errors.append(
                f"{path}: non-zero scores require score_status.kind to be one of {allowed}"
            )
        if evaluation is None:
            errors.append(f"{path}: non-zero scores require score_status.evaluation")

    return errors


def lint_score_evaluation_target(
    graph_path: Path,
    evaluation: str,
    *,
    require_score_authorized: bool,
) -> list[str]:
    evaluation_path = ROOT / evaluation
    evaluation_data = load_json(evaluation_path)
    if evaluation_data is None:
        return [f"{graph_path}: score_status.evaluation must point to a JSON evaluation file"]

    target_graph = evaluation_data.get("target_graph")
    if not isinstance(target_graph, str) or not target_graph.strip():
        return [f"{graph_path}: score_status.evaluation file lacks target_graph"]

    expected = graph_path.resolve()
    actual = (ROOT / target_graph).resolve()
    if actual != expected:
        return [
            f"{graph_path}: score_status.evaluation target_graph {target_graph!r} "
            "does not match this graph"
        ]

    errors: list[str] = []
    if require_score_authorized:
        status = evaluation_data.get("status")
        if status not in SCORING_EVALUATION_STATUSES:
            allowed = ", ".join(sorted(SCORING_EVALUATION_STATUSES))
            errors.append(
                f"{graph_path}: non-zero scores require evaluation.status to be one of {allowed}"
            )

        score_decision = evaluation_data.get("score_decision")
        if score_decision != SCORING_EVALUATION_DECISION:
            errors.append(
                f"{graph_path}: non-zero scores require evaluation.score_decision "
                f"{SCORING_EVALUATION_DECISION!r}"
            )
    return errors


def lint_conditioning_axes(graph: dict, path: Path) -> list[str]:
    errors: list[str] = []
    family = graph.get("family")
    axes = graph.get("conditioning_axes")
    is_context_indexed = isinstance(family, str) and "context-indexed" in family

    if axes is None:
        if is_context_indexed:
            errors.append(f"{path}: context-indexed graphs must include conditioning_axes")
        return errors

    if not isinstance(axes, dict) or not axes:
        return [f"{path}: conditioning_axes must be a non-empty object"]

    unknown = [key for key in axes if key not in CONDITIONING_AXIS_KEYS]
    for key in unknown:
        allowed = ", ".join(sorted(CONDITIONING_AXIS_KEYS))
        errors.append(f"{path}: conditioning_axes has unknown axis {key!r}; expected one of {allowed}")

    for key, value in axes.items():
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{path}: conditioning_axes[{key!r}] must be a non-empty string")

    node_bases: set[str] = set()
    for node in graph.get("nodes", []):
        try:
            node_bases.add(base_node_id(validate_graph.node_id(node)))
        except ValueError:
            continue

    outgoing: dict[str, list[str]] = {}
    for edge in graph.get("edges", []):
        if not isinstance(edge, dict):
            continue
        source = edge.get("source")
        target = edge.get("target")
        if isinstance(source, str) and isinstance(target, str):
            outgoing.setdefault(source, []).append(target)

    for key in axes:
        expected_nodes = CONDITIONING_AXIS_NODE_REQUIREMENTS.get(key)
        if not expected_nodes:
            continue
        expected = ", ".join(sorted(expected_nodes))
        matching_nodes: list[str] = []
        for node in graph.get("nodes", []):
            try:
                node_id = validate_graph.node_id(node)
            except ValueError:
                continue
            if base_node_id(node_id) in expected_nodes:
                matching_nodes.append(node_id)
        if not matching_nodes:
            errors.append(
                f"{path}: conditioning axis {key!r} has no corresponding node; "
                f"expected at least one of {expected}"
            )
        elif not any(has_directed_path_to_outcome(node, outgoing) for node in matching_nodes):
            errors.append(
                f"{path}: conditioning axis {key!r} has no directed path from "
                f"its corresponding node to an outcome-like node"
            )

    if is_context_indexed:
        missing = sorted(CONTEXT_INDEXED_REQUIRED_AXES - set(axes))
        for key in missing:
            errors.append(f"{path}: context-indexed graph missing conditioning axis {key!r}")

    return errors


def has_directed_path_to_outcome(start: str, outgoing: dict[str, list[str]]) -> bool:
    queue = list(outgoing.get(start, []))
    seen: set[str] = set()

    while queue:
        node = queue.pop(0)
        if node in seen:
            continue
        seen.add(node)
        if base_node_id(node) in OUTCOME_NODE_BASES:
            return True
        queue.extend(outgoing.get(node, []))

    return False


def lint(path: Path, controlled_nodes: set[str]) -> list[str]:
    errors = validate_graph.validate(path)
    graph = load_json(path)
    if graph is None:
        return errors

    errors.extend(lint_family_and_status(graph, path))
    errors.extend(lint_nodes(graph, path, controlled_nodes))
    errors.extend(lint_scores(graph, path))
    errors.extend(lint_score_status(graph, path))
    errors.extend(lint_conditioning_axes(graph, path))
    return errors


def main(argv: list[str]) -> int:
    if not argv:
        print("usage: lint_graph.py GRAPH.json [GRAPH.json ...]", file=sys.stderr)
        return 2

    try:
        controlled_nodes = load_controlled_nodes()
    except Exception as exc:  # noqa: BLE001 - CLI should report any ontology load error.
        print(exc, file=sys.stderr)
        return 1

    all_errors: list[str] = []
    for raw_path in argv:
        path = Path(raw_path)
        errors = lint(path, controlled_nodes)
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
