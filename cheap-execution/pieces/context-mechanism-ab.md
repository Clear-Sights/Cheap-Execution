---
name: context-mechanism-ab
description: Use before keeping any hook, plugin or setting that elides, injects or compacts what enters a model's context; it must beat off on a live A/B.
---

# Context mechanism A/B

## Inputs
- The mechanism (elision, injected context, dedupe, early compaction, tool restriction).
- A real task with a checkable answer, of the shape the mechanism is meant for (short job, long thread).
- Per-call usage records (input, cache read, cache write, output tokens).

## Steps
1. Price it first. Per call, cost = cache reads of the fixed floor + each item's write once plus a read on every later call + output. Net = tokens shrunk - text added - extra calls (each extra call re-reads the whole context). Eliding a small item loses once the chance it is fetched back is above about 0.4.
2. Find what it can reach. Hooks change only the current tool call's input or output and added context; the system prompt, tool definitions and saved history are out of reach. If most of the bill is outside its reach, stop.
3. Confirm it fired: log each replacement and check the host kept it. A trial where it did not fire is void, not a failure.
4. Offline replay on a real transcript gives an upper bound only: nothing can fetch back in replay.
5. Live A/B: same task, same model, mechanism off vs on, at least 2 runs per arm; measure the run-to-run spread of off first.
6. Keep it only if no token type rose, at least one fell beyond the spread, and every answer is equally right.
7. Test on both short and long sessions; compounding effects differ.

## Done test
Net(m) > 0 for every mechanism kept, success not lower than off.

## Evidence
- Replay: 86% fewer tool-result characters; live on the same job: 2.7x input tokens, 1.95x cost, 41-45 turns vs 12-13, same answer (TOOLS/RESULTS.tsv).
- Thread-shaped job, 2 runs per arm: every run with it cost more input than every run without, 1.25x-3.5x (TOOLS/RESULTS.tsv).
- 140-turn session: cumulative tool-output bytes -92% (226,130 -> 18,917) (TOOLS/RESULTS.tsv).
- The fixed floor (system prompt and tool definitions, 48.5k tokens) is untouched by hooks; a launch flag limiting tools cut it to 22.5k (LEDGER/work/rows/th0*.tsv).
- Output capture cannot reach 90%: tool outputs were only 23% of input cost (PLANS/TOOLS2.md).

## Where it failed
- Five delivery variants (connected-set delivery, prompt injection, re-read dedupe, capped delivery) all failed the rule; the model read files itself anyway (DETIO-CAUSALITY/from-detio-4.md, from-detio-5.md).
- A live A/B inside run noise (1.4M-2.8M off) decided nothing.

## Not for
- The agent's own dispatch and reading discipline (use cheap-execution).
