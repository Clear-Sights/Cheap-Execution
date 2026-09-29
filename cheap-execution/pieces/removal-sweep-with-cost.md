---
name: removal-sweep-with-cost
description: Use when minimizing a spec or text word by word, and removals that keep every check green must be decided by measured whole-run cost.
---

# Removal sweep with cost

## Inputs
- The text (a spec, rule set, prompt) and the program that evaluates it.
- A two-sided check suite over an exhaustive corpus, plus a larger corpus for scale.
- A cost measure of a whole run (rounds, asks, check runs, CPU).

## Steps
1. Enumerate every word span of the text by script.
2. For each span, remove it and run the suite. Classify: red (needed), green-same-path (every output and path unchanged), or green-path-changing.
3. Apply every green-same-path removal: it is dead text.
4. For each green-path-changing removal, measure whole-run cost with and without it on both corpora. Keep whichever side costs less. Where it changes which ends are reached, count lost ends as a cost.
5. When a removal reads green but is wrong on a larger instance, shrink that instance (greedy) to a small witness and add it to the corpus, so the suite reads it red.
6. Repeat the sweep until a round finds 0 same-path removals (fixpoint).
7. Run the sweep as a background script with a per-span timeout; a timed-out span is NOT-EVALUABLE, never green.

## Done test
Where rounds, asks, work and CPU disagree, keep the side needing fewer check runs; later sweeps converge to 0 same-path removals (fixpoint).

## Evidence
- First sweep: 115 green, 38 same-path; 4 applied, spec 62 -> 60 lines, evaluation work -6% (LEDGER/work/rows/th0*.tsv).
- Round 5: 15,108 spans, 23 green, 0 same-path; the 23 are five paths, each longer on both corpora (COUNTDOWN-SEED/README.md).
- Kept words earn: one removal costs +6,434 check runs; another loses 57 met ends (LEDGER/work/rows/threads.tsv).
- Closing checker holes turned 50 of 77 path-changing removals red (LEDGER/work/rows/th0*.tsv).
- A 15,108-removal sweep ran 11 minutes as a background script at 0 model tokens.

## Where it failed
- One span timed out at 600 s CPU in four rounds and stayed NOT-EVALUABLE.
- The greedy shrink finds a local minimum only.

## Not for
- Judging whole named units against the suite (use removal-test).
