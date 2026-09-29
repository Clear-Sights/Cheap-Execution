---
name: blind-plant-calibration
description: Use when measuring how much a model reviewer, auditor, prover or search tool actually finds, by hiding known faults in its input without telling it.
---

# Blind plant calibration

## Inputs
- The searchers to compare (models, readers, tools), each run alone on its own copy.
- K known faults drawn from the fault families and from past real defects; a key kept away from the searchers.

## Steps
1. Plant K faults (about 5) in the audited copy. Do not tell the searchers; keep the key in a file they cannot read.
2. Run each searcher alone. Count a finding only when its own output raised it and it reproduces on the unmodified target.
3. Score per searcher: plants found of K, other real findings, tokens, wall time.
4. Drop any searcher that misses a plant another method finds, or that adds nothing unique.
5. Next round: new plants; spend on the searcher with the most confirmed findings per unit cost.
6. Stop only when every plant is found and a round by a different method adds zero confirmed findings. Do not stop on in-family estimators (Chao1, Good-Turing): they cannot see a blind spot the family shares.
7. Prefer a deterministic run over a reader wherever one can decide the plant.

## Done test
All plants found, and a different family's full round adds zero confirmed new findings.

## Evidence
- Planted 7-row target: prompt-only auditors found 3-5 of 7 over three rounds; the run-based method found 7 of 7 (LEDGER-METHOD/calib/SCORE.md).
- Sonnet and Haiku readers found 0 of 8 plants at 124k and 95k tokens; one Opus reader found 6 of 7 at 153k (COUNTDOWN-SEED/METHOD3/RESULTS.tsv).
- Six provers and harnesses (Hypothesis, Lean, Dafny, Coq, CrossHair, a control) found 0 of 5 known divergences at 144k-226k tokens each; the incumbent was kept (PRIOR-ART/math-tool/SCORE.md).
- Simulation, 400 runs: false-stop 2-54% by searcher skill under Chao1, 5% with plants plus a second family (COUNTDOWN-SEED/METHOD2/METHOD.md; a simulation, not a field measurement).

## Where it failed
- The strongest searcher false-stops most under estimators: once easy faults are found, only hard ones remain.

## Not for
- Validating a deterministic check (use two-sided-check).
- Counting a population for coverage (use census-before-coverage).
