---
name: census-before-coverage
description: Use before claiming that every message, file, thread or item was covered: enumerate the population by script first, then join outputs against it.
---

# Census before coverage

## Inputs
- The source of the population (an API with pagination, a directory tree, a git history).
- The outputs whose coverage is to be claimed, each citing the item id it covers.

## Steps
1. Enumerate the population by script: page every listing until it reports no more; store one row per item with a unique id. Record counts per group.
2. Check the census itself: ids unique, every group paged to the end, bodies fetched in full (compare the id set of bodies to the census set; count truncated bodies).
3. Require each output row to cite item ids in its evidence. An item with no row gets exactly one drop reason (duplicate, acknowledgement, status with no measurement, ...).
4. Coverage is a script join of census ids against cited ids plus drop reasons. Never accept a worker's own count of what it read.
5. Plant: remove one covered row; the join must report that id uncovered.
6. For code, build the census from a real parser or call graph, never a name regex.

## Done test
Coverage = script join with census; done when every id is covered.

## Evidence
- A census by script: 3,822 messages in 73 threads, full bodies set-matched with 0 truncated (PLANS/LEDGER.md).
- Worker self-reported counts matched the census in 24 of 58 threads; the worst was 2 against 102 (LEDGER/work/rows/threads.tsv).
- Proved-statement inventory by layered subtraction: 14,197 raw -> 3,979 distinct (LEDGER/work/rows/threads.tsv).

## Where it failed
- A name-regex census of dead code claimed 183 dead functions (1,945 lines); the truth was 1, and removals broke the self-test.
- Three stored items were truncated in the source itself; the census can only record that.

## Not for
- Measuring a searcher's recall (use blind-plant-calibration).
- Finding duplicate code by shape (use shape-dedupe).
