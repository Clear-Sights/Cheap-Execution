---
name: two-sided-check
description: Use before trusting any test, guard, hook or gate verdict: the check must be seen red on a planted fault and green on the clean base in one run.
---

# Two-sided check

## Inputs
- The check (a command with a one-line verdict).
- The claim it is meant to falsify.
- A clean base tree.

## Steps
1. Write the claim as one row: claim, check, plant (file, old text, new text).
2. Plant: apply the smallest edit to the check's own subject that makes the claim false. The plant must be an input the spec allows; a plant on a ruled-out input is vacuous, so drop it.
3. Run the check on the clean base and on the planted copy in the same run. Record both verdicts.
4. Accept the check only if base is green and plant is red. If the base is red, the check is unwitnessed: report that itself as a finding.
5. Test what the check actually executes, not a proxy: import the module, not `command -v`; read the exit code, not a log line; read the verdict line the check prints, first line not last.
6. Run it on the installed artifact (the hook or plugin as users get it), not only on a source copy.
7. Repeat the pair on the same commit when the check has timeouts or randomness; a verdict that changes is nondeterministic and not yet a check.
8. Keep every row in one registry; the gate runs every row's check and every row's plant.

## Done test
Watch each check fail on a fault in its subject, then pass, alone: green on the clean base and red on its plant, in the same run.

## Evidence
- The rule flagged a stale input at 0 tokens where an Opus reader needed 153k tokens (COUNTDOWN-SEED/METHOD3/METHOD.md step 2).
- Target wiring: 16 of 16 fault plants red, 3 form-only changes stayed green (MESH/target/HANDOFF.md).
- A gate with 12 of 12 registry rows red under their plants passed (PLANS/FIX-MZ.md:10).
- Rule cases run on an installed hook: distance 45 -> 0, suite 1,994 tests (LEDGER/work/rows/memory.tsv).

## Where it failed
Measured failures of checks that were never seen red (LEDGER/work/rows/th0*.tsv):
- `command -v pytest` passed while `python3 -m pytest` failed.
- A ResourceWarning guard logged the leak and still returned PASS for weeks.
- A Stop hook recorded 0 verdicts across 1,765 log lines.
- A sweep read seen=1, then seen=0, on the same commit.

## Not for
- Deciding which checks to keep (use removal-test).
- Measuring recall of a model or tool searcher (use blind-plant-calibration).
