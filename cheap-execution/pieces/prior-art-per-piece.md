---
name: prior-art-per-piece
description: Use when checking whether each distinct mechanism in a system has a known better replacement, with every citation opened and every claim measured.
---

# Prior art per piece

## Inputs
- The pieces: one per distinct mechanism, not per unit (copies count once), listed by script.
- Real inputs each piece runs on.

## Steps
1. Build the piece list by script; one file per piece brief, holding all a searcher is given.
2. A cheap model searches for leads only: candidate names, papers, libraries.
3. A stronger model opens every cited source with a plain fetch (curl) and quotes it; an unopened citation is dropped. Cheap-model quotes are never kept unread.
4. For each surviving candidate, write a measurement script: same inputs, same outputs, time or operation count, on the real usage pattern (how many queries per build, real sizes).
5. Verdict per piece: replace, add, or none, with the measured numbers. An override of a verdict carries its reason.
6. Compile one result table (one row per piece) from the verified files by script. Keep a dispatched list; a dispatched id without its result file is unfinished.
7. Pieces with nothing to measure against stay open, not none.

## Done test
One row per piece in the result table; a missing result file for a dispatched id is unfinished.

## Evidence
- 89 pieces: 30 with a measured superior alternative; 17 replace, 8 add, 63 none (memory prior-art-per-piece-2026-09-23.md).
- Union-find over all-pairs: 289.5x faster at n=500, identical partitions; `inspect.Signature.bind` agreed 1152/1152 vs a hand check 776/1152; temp file + `os.replace` torn 0 of 12 interrupts vs 12 of 12 (PRIOR-ART/ALTERNATIVES.tsv).
- SCC condensation: 1.463 s -> 0.0055 s, same output on 1,052,740 cases (PRIOR-ART/OVERRIDES.tsv).

## Where it failed
- Cheap-model citations and quotes were often invented or spliced.
- Textbook wins lost on the real usage pattern: radix sort on vocabulary-bounded keys, indexes for single queries (3.7x-17x slower).
- 5 pieces stayed open with no realizer to measure.

## Not for
- Choosing a whole tool or method family (use blind-plant-calibration).
- Verifying the piece's own correctness (use two-sided-check).
