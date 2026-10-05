---
name: removal-test
description: Use when deciding whether each line, name, check or table row is needed: keep it exactly when a requirement in the requester's own words needs it, and remove it alone to see whether a check notices.
---

# Removal test

## Inputs
- The units to judge (lines, names, checks, rows, definitions), listed by script.
- A check suite and a set of plants, each already two-sided.

## Steps
1. For each unit, make a copy without it (one unit at a time).
2. Run the suite and every plant on the copy.
3. Keep the unit exactly when a requirement in the requester's own words needs it; record that requirement's source and the plant or check that names the unit.
4. A needed unit whose removal changes nothing shows a missing check: add the check, never remove the unit. A unit no requirement needs is removable. Before deleting, re-check live references to it (grep and imports); a referenced unit stays until the reference goes.
5. Moving a check elsewhere is not removing it; run the test again after any move.
6. After removals, rerun the whole suite once to confirm the set is still green together.
7. Run it as a background script; read only the summary line and the kept list.

## Done test
Every unit kept names the requirement that needs it, and every needed unit has a check that reads red without it.

## Evidence
- A checker went from 27 checks / 647 lines to 14 checks / 522 lines, each catching a fault nothing else does (LEDGER/work/rows/th0*.tsv).
- A 95-line spec went to 62 lines; all 49 names failed removal, so all are required (LEDGER/work/rows/th0*.tsv).
- 129 of 129 placement rows red on removal; 93 helper rows stayed green and were placement duplicates (MESH/HANDOFF.md).
- The reference re-check before deletion kept 1 of 19 files still cited (LEDGER/work/rows/threads.tsv).

## Where it failed
- Slow on large trees: a per-definition pass checked 277 of 477 definitions, found 0 removable, unfinished (PLANS/MAKOTO2.md).
- A plant on an input the spec rules out made a removal look needed; drop such plants (PLANS/ATTACK2.md).

## Not for
- Text spans below the unit, or choosing among removals that all keep checks green (use removal-sweep-with-cost).
- Fit to a goal formula (use mesh-ledger).
