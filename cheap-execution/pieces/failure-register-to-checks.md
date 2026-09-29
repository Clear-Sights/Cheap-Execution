---
name: failure-register-to-checks
description: Use when a list of known failure kinds must become checks: merge kinds that need the same evidence, and write each check as a short exact tell.
---

# Failure register to checks

## Inputs
- A register of known failure kinds (one entry per kind, with an example).
- The current checks and constructions.

## Steps
1. For each entry, name what a checker must have in hand to catch it (a fresh clone, a commit, a run's exit code).
2. Two entries needing the same thing are one family; give the family one check.
3. For each family, first ask whether a construction already prevents it (the input shape makes it impossible); mark those prevented, citing the construction.
4. Write each remaining check as a tell of at most ten words that is exactly true when the fault is present.
5. Mark entries no check can decide (for example, minimality of a program) as undecidable, not open.
6. Make each check two-sided before it counts.

## Done test
A family is what a checker must have in hand to catch its entries; two families needing the same thing are one. Every entry is prevented, checked by a tell of at most ten words, or marked undecidable.

## Evidence
- A 74-entry register: 69 prevented by construction, 5 need their own row; of those, 4 replaceable and 1 undecidable (LEDGER/work/rows/th0*.tsv).
- 11 entries fell to one shared check: a fresh-clone read that names its commit (LEDGER/work/rows/th0*.tsv).
- Checks over ten words: 18 -> 0 (LEDGER/work/rows/th0*.tsv).

## Where it failed
- No failure measured.

## Not for
- Checks for a goal's terms (use mesh-ledger).
- Validating each resulting check (use two-sided-check).
