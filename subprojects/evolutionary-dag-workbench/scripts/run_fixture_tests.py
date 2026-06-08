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
        name="graph rejects invalid score status kind",
        command=[
            "scripts/lint_graph.py",
            rel("tests/fixtures/graphs/invalid/invalid-score-kind.json"),
        ],
        expected_returncode=1,
        expected_output="score_status.kind 'winner' is not allowed",
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
