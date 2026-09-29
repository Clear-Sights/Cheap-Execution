# Efficiency: predict, then run only the residue (2026-09-29, thread "predict failures")

## Measured
Census: 147 logged failures (`python3 build.py && python3 count.py`): memory FAILED 27, PLANS FAILED 21,
ledger void/flagged 59, a random 40 of the ledger's 595 failed rows. Two taggers, one blind (tag2.tsv):

| set | predictable before the run: yes | yes or partly | tagger |
|---|---|---|---|
| process failures (memory + plans, 48) | 81% / 65% | 98% / 96% | mine / blind |
| experiment failures (ledger, 99) | 75% / 34% | 98% / 66% | mine / blind |

Agreement 79/147. Shares by set: the script in this thread's reply, rerunnable over incidents.tsv and tag2.tsv. The split is the live DetIO A/Bs: I tagged them predictable because later tries 21, 23
and 32 were decided on paper with 0 live runs (LEDGER/OUTCOMES.tsv "PAPER GATE", "IMPOSSIBLE"); the blind
tagger, reading only the row text, called them outcomes. So: process failures are about 90% predictable
by either reading; experiment failures are predictable once a cost model exists, and not before.

Classes (mine): budget 46, claim 24, intent 19, logic 16, capability 15, reach 10, shape 6, order 6, outcome 5.

## Why we check live
Each predictor we own was built after its failure, and runs at the wrong time:
- handoff/check.py closure predicts the missing-file class, but START.md runs it in HIS launched session,
  not ours before handing off. Here it prints `CLOSURE FAIL ... missing=2` only because DetIO and Makoto
  are not cloned beside it (`python3 handoff/check.py closure`), so its verdict depends on the room it runs in.
- checks.sh, the merge gate, does not run closure (`grep -n closure checks.sh`: none).
- Makoto Pre predicted this thread's own failure at 0 tokens (event.nested_budget: timeout 300 inside a 120 s call).
- The DetIO cost formula existed before the ~20 void live A/Bs that it later decided on paper.

## The design (from COUNTDOWN-METHOD.md "spend precision at the front", cost declared before and checked
after; HIS-METHODS "the only thing tested is the change with the recorded I/O")
1. Declare: READS, NEEDS, COST, EXPECT per step, before it runs. Actual over declared is red.
2. Decide on paper at 0 tokens: reach (sealed room: zip + pinned clones only), capability (FACTS.tsv),
   budget (best case vs bar), logic (red on plant/empty, green on base, a terminating count), shape
   (hooks), order, claims. A decided step is not run.
3. Replay recorded I/O for the changed unit's blast radius before any live run.
4. Live only for the residue (effect size, model behaviour, noise), prediction written first.
5. Every surprise becomes one predictor row (FACTS.tsv or a tell in Makoto), red on the incident.

## Wipe list (proposed; nothing deleted)
| cut | what it removes | what covers it |
|---|---|---|
| cheap-execution SKILL.md, 980 words | Dispatch, Fan-out, Cache, Brief sections | new skill, 4 spending lines kept |
| lean-execution skill | a retired skill still listed (retired 05:09Z) | nothing needed |
| cheap-execution hooks/cheap.py | per-call advisory lint, 3 kinds | Makoto Pre, which blocks the same shapes (inferred: masked exit seen blocked; poll loop not checked) |
| 20 method skills in HANDOFF/skills | each restates one line of HIS-METHODS or COUNTDOWN-METHOD | those two documents, cited by step |
| launch-time closure in START.md | the missing-file check running in his session | the same check run by us in a sealed room before we say launch |

## Resume here (frozen 2026-09-29 02:42Z, "Freeze, finish one")
Gabriel SAVED the shortest-path skill 02:43Z. Still open: his word on the
wipe list above. On yes: Cheap-Execution PR replacing cheap-execution/SKILL.md with shortest-path, cheap.py
deleted only after checking Makoto blocks its three kinds; closure moved before launch (sealed room) in
Measure-Zero-Dev checks.sh. Nothing deleted yet; no branch pushed.
