---
name: subtract-first
description: Use when a change both adds and removes, or when additions compete for a size bound: remove first, and add only what a claim needs to become true.
---

# Subtract first

## Inputs
- A change with a stated claim it must make true.
- A size or cost bound (lines, checks, words) that must not rise without being earned.

## Steps
1. List what the change adds and what it could remove.
2. On any ordering conflict, remove before adding.
3. For each addition, name the claim it makes true. An addition with no claim is dropped.
4. Pay for each addition by a removal where one exists (a second source of the same table, a single-use helper, a defensive read the checks already cover).
5. Withdraw an addition whose check goes red rather than adding more to rescue it.
6. Raise a bound only in the commit that earns it, and say so in that commit.
7. After subtracting a rule, list what it protected; anything newly unguarded is a design question for the owner, not an automatic addition.

## Done test
Subtract first. On any ordering conflict, removal before addition. Add only what a claim needs in order to become true.

## Evidence
- Three new checks landed with a 6,422-line bound unchanged, paid by removing a second table source, a single-use helper and a defensive read (LEDGER/work/rows/th0*.tsv).
- Removing 770 owners kept with no reason: 0 left; folding a default into answers instead cost +5,902 rounds (LEDGER/work/rows/th0*.tsv).
- A skill revised with four additions ended 678 -> 677 words after cutting 8 duplicate lines (LEDGER/work/rows/th0*.tsv).

## Where it failed
- Subtracting a suffix-based freeze left 58 files unguarded and editable; flagged to the owner (LEDGER/work/rows/th0*.tsv).

## Not for
- Deciding whether a unit is removable at all (use removal-test or removal-sweep-with-cost).
