---
name: seam-audit
description: Use when auditing a chain of files or stages for defects and choosing the cheapest set of checks that covers every seam between them.
---

# Seam audit

## Inputs
- The wiring of the chain: which file or stage feeds which, by what kind of link.
- Fault classes per seam (statement drift, proof that does no work, wrong encoding, swallowed error, ...).
- Candidate checks (scripts, proof-assumption printers, differential runs) and, optionally, one strong model reader.

## Steps
1. Slots: one per (seam, fault class), read off the wiring by script. A seam with no wire gets no slot; if a defect was found on an unwired seam, wire it first.
2. Pieces: the checks. Each must be two-sided: green on the clean base and red on its seam's plant, in the same run. A check red on the base is unwitnessed; report that as a finding.
3. Plant one hidden fault per slot in a copy; run every check; record plant x check as caught or missed, with cost (seconds, tokens).
4. Rows:
   - A check that catches nothing unique after three tries is removed.
   - Where several checks cover a slot, pick the least-cost set that still covers every slot (a set cover; solve it by script).
   - A slot no check reaches gets the one strong reader, who must run a witness for every finding; the run decides.
5. Fix every finding and rerun until every row left is proved impossible (a slot no check can reach even after asking the owner).
6. For proofs, include a proof cell: compile, print assumptions of every root, and pin each root statement by hash.

## Done test
An audit ends zero or impossible.

## Evidence
- 11 hidden plants (9 real, 2 equivalent): checks alone caught 6 of 9 at 0 tokens; checks plus one Opus reader caught 9 of 9 at 153k tokens; Haiku, Sonnet and Opus together caught 7 of the first 8 at 372k (COUNTDOWN-SEED/METHOD3/METHOD.md).
- Sonnet and Haiku readers caught 0 of 8 at 124k and 95k tokens (COUNTDOWN-SEED/METHOD3/RESULTS.tsv).
- The proof cell caught an Admitted lemma and a weakened root statement (RESULTS.tsv H7, H8).
- The least-cost cover, solved by the project's own solver, met in 2 rounds at reader costs 70 and 400 (COUNTDOWN-SEED/METHOD3/RESEARCH-AS-SEED.md).

## Where it failed
- A renumbering-invariance check and a static duplicate pass caught nothing unique in 3 tries and were removed.
- Checks missed a checker default that accepted every end and a writer that stopped after the first name; only the reader caught those.
- The reader is not repeatable, so a check it stacks on is kept.

## Not for
- Fit of pieces to a goal formula (use mesh-ledger).
- Proving one check can fail (use two-sided-check).
- Attacking successive versions of one proof (use standing-adversary).
