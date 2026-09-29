---
name: differential-reference
description: Use when two executables claim to implement one spec, or a spec has two readings: run both on the same exhaustive corpus and diff every output.
---

# Differential reference

## Inputs
- Two executables of one spec: a proof-extracted program vs a literal evaluator of the spec text, a program vs an independent reference, or the same evaluator under two readings of an ambiguous clause.
- A corpus: every instance up to a small size, plus known adversarial ones.

## Steps
1. Translate every corpus instance into both inputs by script; count translated and untranslatable (an untranslatable instance is itself a finding).
2. Run both on every instance; compare every observable output (final verdict, chosen values, and path length when it matters).
3. Each disagreement is a finding; store its instance as the witness.
4. Group disagreements by cause; send each group with its smallest witness to whoever owns that side.
5. Trace each group against the spec's own words; fix whichever side is wrong, including the reference.
6. Plant changes into one side (negate an output, widen a union); the diff must read DIFF.
7. Rerun after every fix until the diff reads 0.
8. Where a clause has two readings, run both; if verdicts differ on some instance, the ambiguity is live and goes to the owner.

## Done test
Every disagreement is a finding with its instance as the witness; rerun until the diff reads 0.

## Evidence
- Extracted kernel vs literal evaluator: 7,339 of 7,339 translated, 102 disagreements in 3 causes, each with a witness (PLANS/ATTACK2.md).
- Extraction vs evaluator: SAME on n=7,431 in about 20 s; planted changes read DIFF (FIXES/Measure-Zero-Dev/seed-harness/README.md).
- Two readings of one clause: met False vs met True on one adversarial instance (PLANS/NAIVE.md).
- Reading plus a same-path comparison found 5 divergences that six blind provers missed (PRIOR-ART/math-tool/SCORE.md).
- Bounded-exhaustive 7,510 instances: the checker was wrong on 100 (VERIFY/HOLDOUT.md).

## Where it failed
- A stale reference left 2,840 disagreements unadjudicated.
- A disagreement names the instance, not which side is wrong.

## Not for
- Fit of pieces to goal terms (use mesh-ledger).
- Validating one check (use two-sided-check).
