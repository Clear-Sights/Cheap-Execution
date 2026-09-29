---
name: shape-dedupe
description: Use when a codebase may hold duplicated files, duplicated function bodies or unreachable code; find them by normalized shape and a real call graph, never by name.
---

# Shape dedupe

## Inputs
- The tracked tree (all repositories that share code, if several).
- A parser per language and the entry points.

## Steps
1. Files: hash every tracked file; byte-identical content at two paths is a finding.
2. Bodies: parse every function; normalize (blank constants, alpha-rename locals); group equal normalized bodies. Also group equal shapes after binding-vs-algebra normalization.
3. Reachability: build the call graph from entry points with a real parser, including attribute access, dynamic dispatch (visitors, adapters, registries) and tests. A unit no entry point reaches is a candidate, not a finding.
4. Confirm each candidate by removing it and running the suite (a two-sided check).
5. Collapse each duplicate group to one unit with an argument for what differed; generate a file that must exist in several places instead of committing copies.
6. Report counts per class and total lines; rerun until all three classes read zero.

## Done test
No file committed twice. No body written twice. No unreachable unit.

## Evidence
- 39% of 195,854 tracked lines were waste: one proof file committed three times (70,966 lines), duplicated readers (3,367), unreachable functions (LEDGER/work/rows/memory.tsv).
- Deduplicating the tripled file to one generated copy removed 70,966 lines with extraction 12 of 12 PASS (LEDGER/work/rows/memory.tsv).
- A readers dedup cut the bound 6,422 -> 6,351 and left zero on all three measures; 5 duplicate proof sets collapsed to 1; a shape check found 29 groups (LEDGER/work/rows/th0*.tsv).

## Where it failed
- A name regex over grep missed dotted access: it claimed 183 dead functions (1,945 lines), the truth was 1, and removals broke the self-test.
- 18 apparently dead functions were reached by dynamic dispatch.

## Not for
- Units that are unique but maybe unneeded (use removal-test).
- Counting a population for coverage (use census-before-coverage).
