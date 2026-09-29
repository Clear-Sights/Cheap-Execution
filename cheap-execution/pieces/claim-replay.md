---
name: claim-replay
description: Use when an outside critique, audit or review arrives: replay every claim against the current files before fixing anything.
---

# Claim replay

## Inputs
- The critique as a list of claims.
- The current files, pinned by hash.

## Steps
1. Split the critique into atomic claims; number them.
2. For each, write the command that would show it on the current files (a grep, a run, a script on a witness instance).
3. Run it. Classify: refuted (the files show otherwise), real (reproduced), or narrower (true only under a contract the files do not promise).
4. Check the critique's own inputs: a claim made against a stale copy is refuted on the current files; record the stale copy.
5. Fix only real claims, at their root; record the fix and rerun the claim's command to show it gone.
6. Keep one ledger row per claim with its class and the command that decided it.

## Done test
Every claim carries refuted, real or narrower, with the command that decided it; every real claim's command reads clean after its fix.

## Evidence
- An outside critique of 23 claims: 14 refuted, 9 real, 5 narrower (PLANS/ATTACK2.md).
- "11 of 62 roots" was refuted by grepping each root name in two versions (PLANS/ATTACK2.md).
- Replay caught that the critique's round-1 copy was stale (LEDGER/work/rows/seed.tsv).
- An earlier audit of 42 findings: 2 reproduced and open, 11 already fixed (LEDGER/work/rows/seed.tsv).

## Where it failed
- No failure measured.

## Not for
- Producing new findings (use standing-adversary or seam-audit).
