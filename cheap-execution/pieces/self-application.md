---
name: self-application
description: Use to test whether a method or tool is universal by running it on its own text or on a decision about itself, treating every stuck point as a defect.
---

# Self-application

## Inputs
- A method or tool that claims to apply to any instance of some kind.
- An instance built from the method itself: its own text as target, or a choice it must make about itself (which checks to run, which research to use).

## Steps
1. State the claim of universality in one sentence.
2. Encode the self-instance in the tool's own input format, without changing the tool. If it cannot be encoded, that is the first finding.
3. Run it. Record every step where it cannot say what to do next (a branch stop) and every step it takes.
4. Each branch stop is a defect in the method: name the missing rule; do not patch the run by hand.
5. Each change the run earns (a removal, a reordering) is applied only if the method's own checks still pass.
6. For self-audits, make sure the harness runs every step of the method; a row caused by a harness that skips steps is an artifact, not a finding.
7. Attack the result, then repeat until a run makes no change and stops nowhere.

## Done test
Dogfood it and make the new steps, then attack, repeat until bulletproof: a run with no branch stop and no earned change.

## Evidence
- Choosing audit checks, encoded as an instance of the project's own solver, met in 2 rounds at two reader costs with no change to the solver (COUNTDOWN-SEED/METHOD3/RESEARCH-AS-SEED.md).
- A 17-line spec run on itself earned 1 removal (17 -> 16) and exposed 3 branch stops where it did not say what to do next (DOGFOOD-seed-2026-09-23.md).
- The ledger method run on itself proposed 4 rows; 1 was accepted and changed the method (build the matrix as a run), 3 were artifacts (LEDGER-METHOD/self/PROPOSED-METHOD-rows.tsv).

## Where it failed
- Two self-audit rows came from a harness that ran only steps 1-4 of the method.
- The spec dogfood stopped at 21 of 22 with three stops unresolved.

## Not for
- Applying a method to an outside target (use the method's own skill).
