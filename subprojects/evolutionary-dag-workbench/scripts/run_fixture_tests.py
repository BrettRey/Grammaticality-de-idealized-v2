#!/usr/bin/env python3
"""Run positive and negative validator fixture tests."""

from __future__ import annotations

import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class FixtureTest:
    name: str
    command: list[str]
    expected_returncode: int
    expected_output: str | None = None


def rel(path: str) -> str:
    return str(Path(path))


TESTS = [
    FixtureTest(
        name="graph valid minimal context-indexed fixture",
        command=[
            "scripts/lint_graph.py",
            rel("tests/fixtures/graphs/valid/context-indexed-minimal.json"),
        ],
        expected_returncode=0,
    ),
    FixtureTest(
        name="graph valid scoped score fixture",
        command=[
            "scripts/lint_graph.py",
            rel("tests/fixtures/graphs/valid/scoped-score-valid.json"),
        ],
        expected_returncode=0,
    ),
    FixtureTest(
        name="graph valid sink outcome axis fixture",
        command=[
            "scripts/lint_graph.py",
            rel("tests/fixtures/graphs/valid/sink-outcome-axis.json"),
        ],
        expected_returncode=0,
    ),
    FixtureTest(
        name="graph rejects conditioning axis without node",
        command=[
            "scripts/lint_graph.py",
            rel("tests/fixtures/graphs/invalid/axis-without-node.json"),
        ],
        expected_returncode=1,
        expected_output="conditioning axis 'speaker_identity' has no corresponding node",
    ),
    FixtureTest(
        name="graph rejects bad score key",
        command=[
            "scripts/lint_graph.py",
            rel("tests/fixtures/graphs/invalid/bad-score-key.json"),
        ],
        expected_returncode=1,
        expected_output="scores has unknown dimension 'made_up_score'",
    ),
    FixtureTest(
        name="graph rejects context-indexed family without axes",
        command=[
            "scripts/lint_graph.py",
            rel("tests/fixtures/graphs/invalid/context-indexed-missing-axes.json"),
        ],
        expected_returncode=1,
        expected_output="context-indexed graphs must include conditioning_axes",
    ),
    FixtureTest(
        name="graph rejects unknown conditioning axis",
        command=[
            "scripts/lint_graph.py",
            rel("tests/fixtures/graphs/invalid/invalid-axis.json"),
        ],
        expected_returncode=1,
        expected_output="conditioning_axes has unknown axis 'register'",
    ),
    FixtureTest(
        name="graph rejects unknown node",
        command=[
            "scripts/lint_graph.py",
            rel("tests/fixtures/graphs/invalid/unknown-node.json"),
        ],
        expected_returncode=1,
        expected_output="id 'invented_construct' is not in ontology",
    ),
    FixtureTest(
        name="graph rejects unknown relation profile",
        command=[
            "scripts/lint_graph.py",
            rel("tests/fixtures/graphs/invalid/unknown-relation-profile.json"),
        ],
        expected_returncode=1,
        expected_output="relation_profile 'negative-ish' is not allowed",
    ),
    FixtureTest(
        name="graph rejects incompatible relation profile",
        command=[
            "scripts/lint_graph.py",
            rel("tests/fixtures/graphs/invalid/incompatible-relation-profile.json"),
        ],
        expected_returncode=1,
        expected_output="does not apply to edge type 'causal'",
    ),
    FixtureTest(
        name="graph rejects profiled graph without profiles",
        command=[
            "scripts/lint_graph.py",
            rel("tests/fixtures/graphs/invalid/profiled-without-profiles.json"),
        ],
        expected_returncode=1,
        expected_output="profiled graphs must include at least one relation_profile",
    ),
    FixtureTest(
        name="graph rejects duplicate edge",
        command=[
            "scripts/lint_graph.py",
            rel("tests/fixtures/graphs/invalid/duplicate-edge.json"),
        ],
        expected_returncode=1,
        expected_output="duplicates source/target/type",
    ),
    FixtureTest(
        name="graph rejects id filename mismatch",
        command=[
            "scripts/lint_graph.py",
            rel("tests/fixtures/graphs/invalid/id-mismatch.json"),
        ],
        expected_returncode=1,
        expected_output="must match filename stem",
    ),
    FixtureTest(
        name="graph rejects backward time-lag edge",
        command=[
            "scripts/lint_graph.py",
            rel("tests/fixtures/graphs/invalid/backward-time-lag.json"),
        ],
        expected_returncode=1,
        expected_output="time_lagged edge must point forward in time",
    ),
    FixtureTest(
        name="graph rejects backward non-lag cross-time edge",
        command=[
            "scripts/lint_graph.py",
            rel("tests/fixtures/graphs/invalid/backward-cross-time-causal.json"),
        ],
        expected_returncode=1,
        expected_output="cross-time edge must not point backward in time",
    ),
    FixtureTest(
        name="graph rejects forward non-lag cross-time edge",
        command=[
            "scripts/lint_graph.py",
            rel("tests/fixtures/graphs/invalid/forward-cross-time-causal.json"),
        ],
        expected_returncode=1,
        expected_output="cross-time forward edge must use type 'time_lagged'",
    ),
    FixtureTest(
        name="graph rejects disconnected conditioning axis",
        command=[
            "scripts/lint_graph.py",
            rel("tests/fixtures/graphs/invalid/disconnected-conditioning-axis.json"),
        ],
        expected_returncode=1,
        expected_output="has no directed path from its corresponding node to an outcome-like node",
    ),
    FixtureTest(
        name="graph rejects nonzero score without status",
        command=[
            "scripts/lint_graph.py",
            rel("tests/fixtures/graphs/invalid/nonzero-without-score-status.json"),
        ],
        expected_returncode=1,
        expected_output="non-zero scores require a score_status object",
    ),
    FixtureTest(
        name="graph rejects nonzero score without evaluation",
        command=[
            "scripts/lint_graph.py",
            rel("tests/fixtures/graphs/invalid/nonzero-missing-evaluation.json"),
        ],
        expected_returncode=1,
        expected_output="non-zero scores require score_status.evaluation",
    ),
    FixtureTest(
        name="graph rejects nonzero unprofiled score",
        command=[
            "scripts/lint_graph.py",
            rel("tests/fixtures/graphs/invalid/nonzero-unprofiled-score.json"),
        ],
        expected_returncode=1,
        expected_output="non-zero scores require edge_semantics_level 'profiled'",
    ),
    FixtureTest(
        name="graph rejects invalid score status kind",
        command=[
            "scripts/lint_graph.py",
            rel("tests/fixtures/graphs/invalid/invalid-score-kind.json"),
        ],
        expected_returncode=1,
        expected_output="score_status.kind 'winner' is not allowed",
    ),
    FixtureTest(
        name="graph rejects mismatched score evaluation",
        command=[
            "scripts/lint_graph.py",
            rel("tests/fixtures/graphs/invalid/mismatched-score-evaluation.json"),
        ],
        expected_returncode=1,
        expected_output="does not match this graph",
    ),
    FixtureTest(
        name="graph rejects held-out evaluation missing provenance",
        command=[
            "scripts/lint_graph.py",
            rel("tests/fixtures/graphs/invalid/held-out-missing-provenance-reference.json"),
        ],
        expected_returncode=1,
        expected_output="held-out score_status.evaluation requires non-empty held_out_from",
    ),
    FixtureTest(
        name="graph rejects exploratory score evaluation",
        command=[
            "scripts/lint_graph.py",
            rel("tests/fixtures/graphs/invalid/nonzero-exploratory-evaluation.json"),
        ],
        expected_returncode=1,
        expected_output="non-zero scores require evaluation.status",
    ),
    FixtureTest(
        name="graph rejects exploratory scoped label evaluation",
        command=[
            "scripts/lint_graph.py",
            rel("tests/fixtures/graphs/invalid/scoped-exploratory-evaluation.json"),
        ],
        expected_returncode=1,
        expected_output="scoped/general labels require evaluation.status",
    ),
    FixtureTest(
        name="graph rejects score out of range",
        command=[
            "scripts/lint_graph.py",
            rel("tests/fixtures/graphs/invalid/score-out-of-range.json"),
        ],
        expected_returncode=1,
        expected_output="must be between 0 and 5",
    ),
    FixtureTest(
        name="evaluation valid minimal fixture",
        command=[
            "scripts/validate_evaluation.py",
            rel("tests/fixtures/evaluations/valid/minimal-valid.json"),
        ],
        expected_returncode=0,
    ),
    FixtureTest(
        name="evaluation valid held-out fixture",
        command=[
            "scripts/validate_evaluation.py",
            rel("tests/fixtures/evaluations/valid/held-out-valid.json"),
        ],
        expected_returncode=0,
    ),
    FixtureTest(
        name="evaluation valid score-change activated path fixture",
        command=[
            "scripts/validate_evaluation.py",
            rel("tests/fixtures/evaluations/valid/scoped-score-valid-evaluation.json"),
        ],
        expected_returncode=0,
    ),
    FixtureTest(
        name="evaluation rejects empty contrast cells",
        command=[
            "scripts/validate_evaluation.py",
            rel("tests/fixtures/evaluations/invalid/empty-contrast-cells.json"),
        ],
        expected_returncode=1,
        expected_output="contrast_cells must be a non-empty list",
    ),
    FixtureTest(
        name="evaluation rejects invalid axis",
        command=[
            "scripts/validate_evaluation.py",
            rel("tests/fixtures/evaluations/invalid/invalid-axis.json"),
        ],
        expected_returncode=1,
        expected_output="unknown axis 'register'",
    ),
    FixtureTest(
        name="evaluation rejects incomplete axes",
        command=[
            "scripts/validate_evaluation.py",
            rel("tests/fixtures/evaluations/invalid/incomplete-axes.json"),
        ],
        expected_returncode=1,
        expected_output="missing required axis 'genre'",
    ),
    FixtureTest(
        name="evaluation rejects held-out missing provenance",
        command=[
            "scripts/validate_evaluation.py",
            rel("tests/fixtures/evaluations/invalid/held-out-missing-source.json"),
        ],
        expected_returncode=1,
        expected_output="held-out evaluations require non-empty list field 'held_out_from'",
    ),
    FixtureTest(
        name="evaluation rejects held-out unresolved source",
        command=[
            "scripts/validate_evaluation.py",
            rel("tests/fixtures/evaluations/invalid/held-out-unresolved-source.json"),
        ],
        expected_returncode=1,
        expected_output="does not resolve to a phenomenon card ID or evaluation ID",
    ),
    FixtureTest(
        name="evaluation rejects activated path missing edge",
        command=[
            "scripts/validate_evaluation.py",
            rel("tests/fixtures/evaluations/invalid/activated-path-missing-edge.json"),
        ],
        expected_returncode=1,
        expected_output="does not exist in target_graph",
    ),
    FixtureTest(
        name="evaluation rejects missing required node",
        command=[
            "scripts/validate_evaluation.py",
            rel("tests/fixtures/evaluations/invalid/requirements-missing-node.json"),
        ],
        expected_returncode=1,
        expected_output="required node 'operator_value' does not exist in target_graph",
    ),
    FixtureTest(
        name="evaluation rejects missing required edge",
        command=[
            "scripts/validate_evaluation.py",
            rel("tests/fixtures/evaluations/invalid/requirements-missing-edge.json"),
        ],
        expected_returncode=1,
        expected_output="required edge 'reported_acceptability' -> 'community_licensing'",
    ),
    FixtureTest(
        name="evaluation rejects present forbidden edge",
        command=[
            "scripts/validate_evaluation.py",
            rel("tests/fixtures/evaluations/invalid/requirements-forbidden-edge-present.json"),
        ],
        expected_returncode=1,
        expected_output="forbidden edge 'community_licensing' -> 'reported_acceptability'",
    ),
    FixtureTest(
        name="evaluation rejects unknown requirement key",
        command=[
            "scripts/validate_evaluation.py",
            rel("tests/fixtures/evaluations/invalid/requirements-unknown-key.json"),
        ],
        expected_returncode=1,
        expected_output="requirements: unknown key 'maybe_nodes'",
    ),
    FixtureTest(
        name="evaluation rejects activated path reading mismatch",
        command=[
            "scripts/validate_evaluation.py",
            rel("tests/fixtures/evaluations/invalid/activated-path-reading-mismatch.json"),
        ],
        expected_returncode=1,
        expected_output="does not match computed path reading",
    ),
    FixtureTest(
        name="evaluation rejects score-change without activated paths",
        command=[
            "scripts/validate_evaluation.py",
            rel("tests/fixtures/evaluations/invalid/score-change-missing-activated-paths.json"),
        ],
        expected_returncode=1,
        expected_output="score-change-proposed evaluations require activated_paths",
    ),
    FixtureTest(
        name="evaluation rejects score-change missing path reading",
        command=[
            "scripts/validate_evaluation.py",
            rel("tests/fixtures/evaluations/invalid/score-change-missing-path-reading.json"),
        ],
        expected_returncode=1,
        expected_output="score-change-proposed activated paths require expected_path_reading",
    ),
    FixtureTest(
        name="evaluation rejects score-change unprofiled activated edge",
        command=[
            "scripts/validate_evaluation.py",
            rel("tests/fixtures/evaluations/invalid/score-change-unprofiled-activated-edge.json"),
        ],
        expected_returncode=1,
        expected_output="score-change-proposed activated edges require relation_profile",
    ),
    FixtureTest(
        name="evaluation rejects invalid phenomenon",
        command=[
            "scripts/validate_evaluation.py",
            rel("tests/fixtures/evaluations/invalid/invalid-phenomenon.json"),
        ],
        expected_returncode=1,
        expected_output="phenomenon card does not exist: 'missing-card'",
    ),
    FixtureTest(
        name="evaluation rejects invalid result",
        command=[
            "scripts/validate_evaluation.py",
            rel("tests/fixtures/evaluations/invalid/invalid-result.json"),
        ],
        expected_returncode=1,
        expected_output="result 'wins' is not allowed",
    ),
    FixtureTest(
        name="evaluation rejects missing target graph path",
        command=[
            "scripts/validate_evaluation.py",
            rel("tests/fixtures/evaluations/invalid/missing-target-path.json"),
        ],
        expected_returncode=1,
        expected_output="target_graph path does not exist",
    ),
]


def run_test(test: FixtureTest) -> str | None:
    command = [sys.executable, *test.command]
    completed = subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
        timeout=10,
    )
    output = f"{completed.stdout}\n{completed.stderr}"

    if completed.returncode != test.expected_returncode:
        return (
            f"{test.name}: expected return code {test.expected_returncode}, "
            f"got {completed.returncode}\n{output}"
        )

    if test.expected_output and test.expected_output not in output:
        return f"{test.name}: expected output substring not found: {test.expected_output!r}\n{output}"

    return None


def main() -> int:
    failures = [failure for test in TESTS if (failure := run_test(test))]

    if failures:
        for failure in failures:
            print(failure, file=sys.stderr)
        return 1

    for test in TESTS:
        print(f"ok: {test.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
