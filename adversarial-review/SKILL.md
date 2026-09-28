---
name: "adversarial-review"
description: "Use to adversarially verify a chain of stages (spec, proof, extracted code, checker, tree write): sealed plants, run-only checks at every seam, one witness-giving reader, and a stop rule."
---

# Adversarial review

One audit of a whole chain. The wiring says where to look. Runs decide. A reader covers only what no run reaches. The audit ends zero or impossible.

## Terms
- Seam: a link where one stage feeds another (spec to proof, proof to extracted code, checker to spec, code to tree).
- Slot: one (seam, fault class) pair.
- Plant: one fault put in a copy on purpose. Sealed means neither the reader nor whoever builds the checks ever sees it or its key.
- Cell: a check that only runs (script, compiler, differential diff) and spends no model tokens.
- Two-sided: in the same run, green on the clean base and red on its own plant.
- Witness: a command the finder ran whose output shows the defect on the unmodified target.
- Head: the commit sha a round attacked. Every round pins one.

## Steps
0. Scope. The first round reads the whole target. Every later round reads only the diff since the last head attacked; old findings are rechecked by their plants in step 6, at 0 tokens. No diff, no round. Measured: a diff-only round over four repos cost about 24,000 tokens against 231,180 for one whole-tree round.
1. Slots. Read the seams off the wiring by script, one slot per (seam, fault class). Fault classes come from the target's own register families when it has one (Scour: zero/resources/REGISTER.md A-H), never from invention. A stage with no wire gets no slot. If a defect ever turned up on an unwired stage, wire it first: that gap is a finding.
2. Plants, sealed. For each slot, make at least one plant by script (one fault per copy) and keep the key where the reader cannot read it. Include the classes that are easy to miss:
   - checker internals: a default that accepts every end, or a writer that stops early;
   - a proof that does no work: Admitted, or an axiom;
   - a statement weakened with its proof redone;
   - an order or tie-break swapped;
   - an error swallowed.
   Mechanical mutants count as plants (AST operators on code: comparison swap, and/or swap, dropped not, int+1; mCoq-style edits on proof definitions). A plant that changes no run is equivalent: show that and exclude it. Each plant declares the checks it must redden; reddening any other is a finding too.
3. Cells, zero tokens first. Every cell must be two-sided. A cell red on the base is unwitnessed, and that is itself the first finding. Run each cell under two PYTHONHASHSEED values (or the language's equivalent). If the two runs differ, the cell depends on set order, and that is a cell defect, not a finding. Read a plant against the base's whole normalized output, not just the pass/fail verdict: a checker plant can leave every verdict unchanged and move only a witness line. A cell tests the kind of fault, never a list of spellings: plant one spelling the cell does not list (a spelling table let 6 fresh spellings through). Timing cells compare a ratio or interleaved runs, never one mean against a bar under load.
   - The checker on the spec and its own plant list.
   - Proof cell: compile, Print Assumptions on every root, and hash every root statement. A changed hash is red.
   - Differential: the extracted kernel against the reference evaluator on the whole corpus, every round's values and every end diffed, with both sides ended by the same rule (Countdown: ATTACK2/kdiff3/run2.sh, not kdiff2, whose old end rule gave false disagreements).
   - Certificate checks: each must be red on a corrupted certificate.
4. Reader: one, only for the slots no cell turned red. Use a strong model different from the one that wrote the target. Give it the requirements, the files, and the list of uncovered seams, and require a witness command per finding. The run decides; the reader's prose never does. It must also prove it read: each finding quotes one exact line from the second half of the file it cites, and a script rejects any finding whose line is not in that file. A reader that used far fewer tokens than its input size did not read, and its round counts as failed. Price it before running: tokens from the last logged reader run on this chain.
5. Matrix. Record plant x piece (each cell and the reader) as caught or missed, with seconds and tokens, plus predicted vs actual per piece. A piece whose actual differs from its prediction is a bug in the piece or in the prediction; trace it.
   - A piece that catches nothing unique after three tries is removed.
   - Where pieces stack on a slot, keep the least-cost set that still covers every slot (a set cover, solved by script). Keep a cell the reader stacks on anyway, because the reader is not repeatable.
   - A slot no piece turns red is a Needed row. Add a cell for it, or wire the seam.
6. Fix and rerun. Every finding names the plant that proves it; the owner lands that plant in the target's own gate, so the next round rechecks it by script. Fix every real finding at its root and rerun the cells, then every plant.
7. Record the round: head, tokens, tool calls, seconds, findings by severity. A round costing over 2x the cheapest logged round of its kind stops and names the rise.
8. Stop only when every plant is red AND one round of a different method adds nothing new (for example, mechanical mutants after hand plants, or cells after the reader). Do not stop on duplicate rates, Chao1, Good-Turing, tiers or a judge model: a blind spot the whole family shares stays invisible to them.

## Done test
The 8 hidden plants of COUNTDOWN-SEED/METHOD3/RESULTS.tsv (H1-H8), ported to the current pins by `python3 METHOD3/s27/mkplants27.py BASE`. Pass means every plant is red under some piece, or is shown to be equivalent. Record the cell-only score and, if the cells miss any, the reader's price.
Result on SEED27 82d0cccc805a + Seed.v 266783613363 (METHOD3/s27/RESULTS27.tsv): the cells alone caught 8 of 8 at 0 model tokens, so the reader was not needed.
- The checker caught H1, H2, H4 and H6. H2, equivalent on the older copy, is real now: plant E01 turns green.
- The kernel diff caught H1, H3 and H4, and was the only piece to catch H3.
- The proof cell caught H7 and H8.
- H5 was caught only weakly: the verdicts stayed the same and 2 witness lines moved.
The base was green in every cell, and the kernel diff read identically under two hash seeds.

## Evidence
- SEED27: 8 of 8 by the cells at 0 tokens (above).
- 2026-09-28: whole-tree round on Scour #27 at 1416f15, 231,180 worker tokens, 19 tool calls, 377 s; the diff-only round after it, four repos, about 24,000 tokens (HANDOFF/sections/attack.md).
- R1 copy, 11 plants (9 real, 2 equivalent): cells alone caught 6 of 9 at 0 tokens; cells plus one Opus reader caught 9 of 9 at 153k tokens. The cells missed H5 (the checker default) and H6 (the write model), both checker internals on unwired seams (METHOD3/RESULTS.tsv).
- Sonnet readers caught 0 of 8 at 124k tokens and Haiku 0 of 8 at 95k. Opus missed H8, the weakened statement, which the proof cell's hash caught.
- Mechanical mutants: Seed.v, 12 of 12 killed (11 by coqc, 1 by the statement hash). check.py, 8 of 12 killed; the 4 survivors cost 8 min each (PLANS/METHOD.md).
- A renumbering-invariance cell and a static duplicate pass caught nothing unique in 3 tries and were removed.

## Where it failed
- Checker internals are the weak seam: on the older copy the cells missed H5 and H6. On SEED27, H5 still shows only as a moved witness line. Wire the checker's own seams.
- A reader without a witness rule reports prose that no run confirms.
- A surviving mutant costs a full run, so order the oracle so most mutants die on its first line.
- Re-reading the whole tree every round cost 231,180 tokens for findings the plants would have rechecked for free.
- A check written as a list of spellings passed 6 fresh spellings; the kind, not the wording, is the check.

## Supersedes
seam-audit, and the stop rule of blind-plant-calibration, for chain audits. Use two-sided-check alone to prove that one check can fail. Use standing-adversary to attack successive versions of one proof.