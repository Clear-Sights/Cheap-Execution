---
name: standing-adversary
description: Use when a proof or spec is revised repeatedly: keep one adversary attacking each new version, every round ending in a runnable witness or no counterexample.
---

# Standing adversary

## Inputs
- Each new version of the proof or spec, pinned by hash.
- The definition it claims to implement.

## Steps
1. One adversary per artifact; it writes nothing but findings and witness scripts.
2. Each round, pin the version by hash and attack every changed part against the definition, not against the author's intent.
3. For each suspected defect, write the smallest instance and a script that shows it. No script, no finding.
4. Measure each finding's reach on the real instance (how many sites are affected today); report reach 0 as real but free today.
5. For each claim that survives, write "stands" with the reason; for each fix proposed, mark it inferred until proved.
6. Distinguish a wrong answer from a lost shortcut (a fallback taken where a fast path could hold).
7. Next version: rerun every earlier witness first, then attack the new parts.

## Done test
Attack until each part demonstrably follows the definition: every round ends in a witness or "No counterexample".

## Evidence
- 11 rounds on successive proof versions found real defects review missed: a shared site counted once per term (10 real lines lose to 12), a fast route shut off after round one, and one local failure switching every part to the slow path (COUNTDOWN-SEED/DISPROVE/FINDINGS.md).

## Where it failed
- Several findings were real but reached 0 sites today (7 of 943 sites define several terms, none affected).
- Some proposed fixes stayed inferred, not proved.

## Not for
- Reproducing findings someone else made (use claim-replay).
- Covering every seam of a chain with checks (use seam-audit).
