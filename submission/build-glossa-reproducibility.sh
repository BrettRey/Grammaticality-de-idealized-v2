#!/bin/sh
set -eu

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
project_dir=$(dirname "$script_dir")
tools_dir="$project_dir/../../../tools/ovmg-tools"
archive_path="$script_dir/glossa-supplement-3-anonymous.zip"
staging_dir=$(mktemp -d)
package_dir="$staging_dir/glossa-supplement-3"

cleanup() {
  rm -rf "$staging_dir"
}
trap cleanup EXIT HUP INT TERM

mkdir -p "$package_dir/model/js"
mkdir -p "$package_dir/model/tests/fixtures"
mkdir -p "$package_dir/model/experiments"
mkdir -p "$package_dir/model/results"
mkdir -p "$package_dir/figure"
mkdir -p "$package_dir/formalization/OVMG"
mkdir -p "$package_dir/corpus"

cp "$script_dir/glossa-reproducibility/README.md" "$package_dir/README.md"
cp "$script_dir/glossa-reproducibility/corpus/README.md" "$package_dir/corpus/README.md"

cp "$tools_dir/Makefile" "$package_dir/model/Makefile"
cp "$tools_dir/js/engine.js" "$package_dir/model/js/engine.js"
cp "$tools_dir/js/sim.js" "$package_dir/model/js/sim.js"
cp "$tools_dir/js/revised-engine.mjs" "$package_dir/model/js/revised-engine.mjs"
cp "$tools_dir/js/revised-sim.mjs" "$package_dir/model/js/revised-sim.mjs"
cp "$tools_dir/js/joint-likelihood.mjs" "$package_dir/model/js/joint-likelihood.mjs"
cp "$tools_dir/js/closed-loop-sim.mjs" "$package_dir/model/js/closed-loop-sim.mjs"
cp "$tools_dir/tests/run-fixtures.mjs" "$package_dir/model/tests/run-fixtures.mjs"
cp "$tools_dir/tests/run-sim-smoke.mjs" "$package_dir/model/tests/run-sim-smoke.mjs"
cp "$tools_dir/tests/run-revised-model.mjs" "$package_dir/model/tests/run-revised-model.mjs"
cp "$tools_dir/tests/run-joint-likelihood.mjs" "$package_dir/model/tests/run-joint-likelihood.mjs"
cp "$tools_dir/tests/run-closed-loop.mjs" "$package_dir/model/tests/run-closed-loop.mjs"
cp "$tools_dir/tests/fixtures/fig4-preemption.json" "$package_dir/model/tests/fixtures/fig4-preemption.json"
cp "$tools_dir/experiments/run-closed-loop-sweep.mjs" "$package_dir/model/experiments/run-closed-loop-sweep.mjs"
cp "$tools_dir/experiments/run-bifurcation-diagnostics.mjs" "$package_dir/model/experiments/run-bifurcation-diagnostics.mjs"
cp "$tools_dir/results/closed-loop-sweep.json" "$package_dir/model/results/closed-loop-sweep.json"
cp "$tools_dir/results/bifurcation-diagnostics.json" "$package_dir/model/results/bifurcation-diagnostics.json"

cp "$project_dir/simulate_dynamics.py" "$package_dir/figure/simulate_dynamics.py"
cp "$project_dir/simulation_data.dat" "$package_dir/figure/simulation_data.dat"

cp "$project_dir/formalization/AxiomAudit.lean" "$package_dir/formalization/AxiomAudit.lean"
cp "$project_dir/formalization/OVMG.lean" "$package_dir/formalization/OVMG.lean"
cp "$project_dir/formalization/lake-manifest.json" "$package_dir/formalization/lake-manifest.json"
cp "$project_dir/formalization/lakefile.toml" "$package_dir/formalization/lakefile.toml"
cp "$project_dir/formalization/lean-toolchain" "$package_dir/formalization/lean-toolchain"
cp "$project_dir/formalization/OVMG/Core.lean" "$package_dir/formalization/OVMG/Core.lean"
cp "$project_dir/formalization/OVMG/OperatorBridge.lean" "$package_dir/formalization/OVMG/OperatorBridge.lean"
cp "$project_dir/formalization/OVMG/OperatorStratum.lean" "$package_dir/formalization/OVMG/OperatorStratum.lean"

corpus_dir="$project_dir/subprojects/evolutionary-dag-workbench/data/agr-coca-projection"
cp "$corpus_dir/query-plan.csv" "$package_dir/corpus/query-plan.csv"
cp "$corpus_dir/query-manifest-bunch-animate-list.csv" "$package_dir/corpus/query-manifest-bunch-animate-list.csv"
cp "$corpus_dir/query-manifest-bunch-inanimate-list.csv" "$package_dir/corpus/query-manifest-bunch-inanimate-list.csv"
cp "$corpus_dir/query-manifest-known-qn-list.csv" "$package_dir/corpus/query-manifest-known-qn-list.csv"
cp "$corpus_dir/query-manifest-majority-minority-list.csv" "$package_dir/corpus/query-manifest-majority-minority-list.csv"
cp "$corpus_dir/query-manifest-partitive-agreement-list.csv" "$package_dir/corpus/query-manifest-partitive-agreement-list.csv"
cp "$corpus_dir/query-manifest-partitive-list.csv" "$package_dir/corpus/query-manifest-partitive-list.csv"
cp "$corpus_dir/kwic-coding-schema.csv" "$package_dir/corpus/kwic-coding-schema.csv"
cp "$corpus_dir/summary.csv" "$package_dir/corpus/summary.csv"
cp "$corpus_dir/uncertainty-summary.csv" "$package_dir/corpus/uncertainty-summary.csv"
cp "$corpus_dir/baseline-discriminator.csv" "$package_dir/corpus/baseline-discriminator.csv"
cp "$corpus_dir/false-positive-audit.csv" "$package_dir/corpus/false-positive-audit.csv"

for manifest in "$package_dir"/corpus/query-manifest-*.csv; do
  cut -d, -f1-6 "$manifest" > "$manifest.tmp"
  mv "$manifest.tmp" "$manifest"
done

perl -pi -e 's/of Reynolds, /of the author, /g' "$package_dir/model/js/engine.js"
perl -pi -e "s/in Reynolds, 'Grammaticality de-idealized'/in the paper/g" \
  "$package_dir/model/tests/fixtures/fig4-preemption.json"

(
  cd "$package_dir"
  find . -type f ! -name SHA256SUMS.txt -print0 \
    | LC_ALL=C sort -z \
    | xargs -0 shasum -a 256 > SHA256SUMS.txt
)

find "$package_dir" -exec touch -t 202608230000 {} +
rm -f "$archive_path"
(
  cd "$staging_dir"
  find glossa-supplement-3 -type f | LC_ALL=C sort \
    | zip -X -q "$archive_path" -@
)

shasum -a 256 "$archive_path"
