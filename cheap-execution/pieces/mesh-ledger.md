---
name: mesh-ledger
description: Use when checking whether an existing program, config or document does exactly what its stated goal requires, no more and no less.
---

# Mesh ledger

## Inputs
- TARGET: the artifact (code, config, text) and a way to run it, if it runs.
- GOAL: the goal's own words, plus every doc statement about what it produces.
- A corpus of inputs: exhaustive or near-exhaustive where one exists, plus known adversarial cases (a tie, a self-use, a shared owner).
- A trusted reference, if one exists (an accepted fix, a proven kernel).

## Steps
0. If GOAL serves a further purpose, run these steps with GOAL as target and that purpose as goal first; drop from GOAL whatever that run voids.
1. Write GOAL as a formula of named terms. Every term must be required: removing it breaks GOAL. Each term is one slot. Where the wording admits two readings, keep both formulas.
2. Split TARGET into atomic pieces at every top-level separator the goal could drop on its own (clause, conjunct, tuple component), by script where possible.
3. Build a matrix: one row per piece, one column per slot. A cell is yes when a traced run shows an observable depends on the piece (for text: the piece states a requirement nothing else states). Give each cell a one-line reason.
   - Where TARGET runs, build the matrix by runs, not by reading: remove each piece, rerun on the corpus, compare to the exact terms.
   - Vary every input the formula leaves free; a piece whose output moves under a free input over-defines.
   - Where a reference exists, run both on the same corpus; trace each disagreement and fix whichever side is wrong against GOAL's words.
   - For joint effects no single removal explains, use a one-at-a-time group test (n+1 runs), not pairwise search.
4. Read rows off the matrix:
   - Stack: a slot with two or more yes cells, or a piece with two or more. If removing one leaves the term unchanged, remove it; otherwise split what they share.
   - Misfit: a piece with no yes cell. If removing it breaks GOAL, add the missing slot; otherwise remove the piece.
   - Needed: a slot with no yes cell.
   - Overdefinition: a piece pins what the formula leaves free (an order, a precision, a check). Prove by swapping in the coarsest substitute and rerunning every consumer.
   - Underdefinition: the formula pins something no piece pins, or a piece leaves it to an unnamed input (an env var, a default).
5. Fix every row and rerun until every row left is proved impossible.

## Done test
Fix every row and rerun until every row left is proved impossible.

## Evidence
- Calibration on a planted target with 7 known rows: prompt-only auditors (two models, three rounds) found 3 to 5 of 7, and prompt changes did not converge (LEDGER-METHOD/calib/SCORE.md).
- The run-based ledger (mesh.py) found 7 of 7 with a hand reference and with references written blind by Haiku (~$0.07/run) and Sonnet (~$0.4/run); a clean tree exits 0 with no false rows (TOOLS/ledger-run/SCORE.md).
- Joint search: one-at-a-time group test, worst case 125 -> 25 runs; dupe search 288 pairwise runs -> 0-1 confirming runs (TOOLS/ledger-run/SCORE.md).
- Self-calibration: 6 of 6 planted faults caught (LEDGER/work/rows/th0*.tsv).

## Where it failed
- A "disagree" row says a term is missing or wrong, not which one.
- Mapping thousands of code units by reading (not running) to 17 goal lines: 71% fit, and two terms had no realizer at all; judgment was the weak point (LEDGER-countdown-2026-09-23.md).
- Fit of prose and config pieces stays a judgment.

## Not for
- Hunting defects at seams between several artifacts (use seam-audit).
- Deciding whether each unit is needed by an existing check suite (use removal-test).
- Declaring slots before any piece exists (use typed-holes).
