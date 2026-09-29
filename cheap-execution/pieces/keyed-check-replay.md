---
name: keyed-check-replay
description: Use when a deterministic check suite or build is rerun often: key each unit by a hash of its inputs and replay recorded results when the key is unchanged.
---

# Keyed check replay

## Inputs
- A suite of deterministic check units (tests, proof files, audits) and what each reads.

## Steps
1. For each unit, record the files it reads (trace the reads, or declare them) and compute a key: a length-prefixed digest of those inputs plus the command.
2. Run cold once; store per key: exit code, verdict line, output digest.
3. On rerun, replay the stored result for every unchanged key; run only units whose key moved.
4. For proofs, split statements from proof bodies: check statements first (fast), proofs in parallel per unit; a unit whose interface file is byte-identical does not move later keys (early cutoff).
5. Plant: neuter the key comparison in a copy; the suite must read red, proving the skip is not silently passing.
6. Log wall time per pass; report cold, warm and one-change times.

## Done test
Only the change is tested against the recorded I/O; the plant that neuters the key comparison reads red.

## Evidence
- A gate went from 769 s to 4 s warm; recording costs 372 s once (LEDGER/work/rows/th0*.tsv).
- Proof compile: 174.9 s serial -> 73.8 s cold, 8.7 s warm, 2.7 s for one touched unit of 54 (FULL-READ-2026-09-23.md:286).
- A keyed read ledger: 271 -> 95 file opens, 14.4 MiB -> 3.91 MiB, verdict lines byte-identical (LEDGER/work/rows/th0*.tsv).
- A length-prefixed digest fixed a boundary collision where 25,694 of 29,791 triples shared a key (PRIOR-ART/ALTERNATIVES.tsv:54).

## Where it failed
- File-level keys fan out: one changed file cost 1,196 s; function-level keys need a reach trace.

## Not for
- Agent token cost (use cheap-execution).
- Deciding which checks should exist (use removal-test).
