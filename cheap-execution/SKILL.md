---
name: cheap-execution
description: Use on every task before spending tokens or running anything, reviews and audits included: walk back from the end to the few inputs that decide it, settle each where it already is, and run only what nothing settles.
---

# Cheap execution

One flow. Each step exists to make the next one unnecessary; stop at the first step that decides the end. A review or audit is the same flow with "no defect left" as its end; REVIEW.md carries its detail and evidence.

**1. Name the end.** Write the one line that will show the task is done, and what it must read. If a recorded result already carries that line for the same inputs (same hashes), the task is done: reuse it. A later review round reads only the diff since the last head it attacked (about 24,000 tokens against 231,180 for a whole-tree round).

**2. Walk back from the end.** Name only the inputs that line depends on: files at pinned hashes, facts of the room that will run it, costs, and the design's own terms. For a chain of stages these are its seams, read off the wiring by script; a stage with no wire gets no check until it is wired. That is the blast radius. Nothing outside it is read, run or checked.

**3. Settle each input where it already is.** A file either resolves in the room that will run the step, meaning a sealed copy with only the zip and the pinned clones, or it does not. A tool, variable, permission or host is either in that room's known facts (FACTS.tsv) or it is not. A cost is units times a measured unit cost. A design either contradicts its goal on paper or it does not. Every check used here is two-sided: red on its own plant and green on the base in the same run, and it tests the kind of fault, never a list of spellings. A check red on the base is the first finding. Whatever fails here is fixed now, at the input, before anything runs. Whatever cannot be settled is a hole.

**4. Ask whether the holes can change the answer.** Put the best case and the worst case of every hole through to the end line. If both give the same verdict, the end is decided on paper: record it and stop. This is where most runs disappear.

**5. Fill only the holes that matter, cheapest first.** Code before a model. Replay the recorded I/O of the changed unit before a live run. Run the smallest live case before the full one. In a review, zero-token cells (the checker, the proof cell, the differential diff) go first, and one strong reader, not the author's model, takes only the seams no cell turned red, with a witness command for every finding and a price set from its last logged run. Each fill goes back through step 4, and the flow stops the moment the end line is decided. How a model call or an agent brief spends: SPENDING.md.

**6. Run live with the prediction written down.** What is left is what only a run can show: an effect size, a model's behaviour, noise. Before it starts, write down what it should print and what it should cost; a run over twice the cheapest logged run of its kind stops and names the rise. If the result differs, name the input that would have shown it and add it where step 3 reads it (a row in FACTS.tsv, or a plant in the owner's gate), seen catching this case, so the same surprise never costs a run twice. A review ends only when every plant is red and one round of a different method adds nothing new.

## What this flow rests on

- 147 logged failures, tagged by two readers, one blind: process failures were predictable before the run in 65-81% of cases outright and 96-98% at least in part (`python3 evidence/compare.py`).
- On SEED27 the zero-token cells alone caught 8 of 8 hidden plants; on the older R1 copy cells caught 6 of 9, and one Opus reader brought it to 9 of 9 at 153k tokens, while Sonnet and Haiku readers caught 0 of 8 (REVIEW.md).
- Scour: 41 of its 47 labelled real bugs fall in classes a script generates with no model (a reading of the labels, not a run).
- A worker that only relays one script's output cost 81-98k tokens; the same script run in the background costs about none (SPENDING.md).
