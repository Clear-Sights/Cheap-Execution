---
name: computed-verdict-ledger
description: Use when recording outcomes of experiments or trials, so each verdict is computed from typed fields and conflicting verdicts are found by script.
---

# Computed verdict ledger

## Inputs
- Measurements, each of one thing under one condition.

## Steps
1. One row per measurement, tab-separated, typed columns: check (command reproducing it), claim, thing (same string for the same thing everywhere), condition, metric (with unit), better (higher, lower, pass), baseline, value, noise (measured spread), done_test (pass, fail, none), correctness vs baseline (same, better, worse, unknown), fired (did the mechanism actually execute: yes, no, unknown), basis (measured, inferred), evidence (path or id).
2. Never type a verdict. Compute it:
   - fired=no -> void
   - basis=inferred or no value -> untested
   - done_test=fail -> didnt-work
   - numeric baseline and noise: d = signed difference; d > noise and correctness same or better -> helped; d < -noise or correctness worse -> hurt; else no-effect
   - numeric baseline, no noise -> unresolved-noise
   - no baseline, done_test=pass -> worked
3. Conflict check: rows with equal (thing, condition, metric) whose verdicts fall in different classes ({helped, worked}, {hurt, didnt-work}, {no-effect}); exit 1 if any.
4. Keep a plant file with a known conflict and a fired=no row; the script must report the conflict and compute void.
5. Resolve each conflict by a new measurement under a narrower condition, not by editing a verdict.

## Done test
Verdict is computed, never typed; the conflict check exits 0 on the ledger and exits 1 on its plant.

## Evidence
- Plant run: "CONFLICT A | c | m: line 2 helped vs line 3 hurt", conflicts 1, exit 1; the fired=no row computed void (LEDGER/work/verdict.py on LEDGER/work/plant.tsv, run 2026-09-24).
- Live trials of a context mechanism, first recorded as didnt-work, became void once fired=no was recorded: the host had discarded 35 of 35 and 32 of 32 replacements (PLANS/LEDGER.md).

## Where it failed
- Older 8-column rows with a typed verdict cannot be run through it without retyping.
- Most rows lack a measured noise, so they compute unresolved-noise.

## Not for
- Deciding what to measure.
- Validating a check or registering product claims (use two-sided-check).
