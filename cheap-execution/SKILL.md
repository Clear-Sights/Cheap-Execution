---
name: "cheap-execution"
description: "Use on every task that spends tokens or runs tools: before dispatching agents, big reads, repeated steps, reviews, handoffs, or compactions."
---

# Cheap Execution

## Terms

- Plant: break an input on purpose; the checks it names, and only those, must fail. A plant that fails nothing is a gap, not a pass.
- Default: every uncited number below is untested; replace it with a measured one.

## Rungs: take the first that applies

0. Result changes no next act → skip it. A check's result always gates done, so never skip a check.
1. Search existing sources first; found → read or call it, never copy or recompute.
2. Same input always gives same answer → compute with code.
3. Pruning code costs less than model reading all → prune.
4. Smaller than its own brief → do it here.
5. Has ACCEPTANCE, reversible, internal → cheaper executor; else here.

## Every step

- Anything processing items reports in, out, and dropped counts.
- Every number or fact for a reader is copied from a run's output with its command, or marked `believed`.
- Repeated review → read only the diff since the last reviewed commit; each finding becomes a plant in the gate, so old escapes are rechecked by script.
- Gated, irreversible or unknown work → first mock its wiring from existing pieces at 0 model calls, smallest case first; each void becomes a row, filled in order under a numeric cost cap, ending met or measured-not-met.
- Model calls: batch items per call and pass low effort explicitly; each call pays fixed overhead (Claude ~1.2k, Codex ~10k tokens) and ~1k thinking even when off. Measured: 44.8k → 16.6k.

## Done twice by hand, or shared across items → make it run unasked

- Do it once in code, store the result for all, inside the act's one entry point.
- Assert the expected count before acting.

## Dispatch

- One agent gets at most 3 tasks, sized to fit one context window (GSD REQ-PLAN-02).
- Parallel agents share no writable state; sessions talk through a file, one writer each, since a message between sessions may never arrive.
- Grant each agent only the tools its task needs.
- Verification: checks first (0 tokens); only what they leave goes to one reader, the strongest model, never several cheaper ones.
- Inputs that may change mid-run, other repos included → pin by content hash or commit, never a live branch.

## Fan-out

- Width starts at min(4, independent items).
- Rate-limit or usage-limit error → halve width.

## Cache

- Keep every repeated prefix byte-identical: only append to the context, and keep the tool set fixed (restrict a tool by rule, never by removing its definition).
- Text loaded on every turn (skill descriptions, CLAUDE.md, MCP tools, hook output) → cap its length with a lint set before the session; the rest lives in files read on demand (claude-token-optimizer: 11,000 → 1,300 start tokens).
- A cached prefix under the model's minimum (512 to 2,048 tokens, prompt caching doc) never caches; check it clears.
- Model jobs that can wait → Batch API, 50% off, stacks with caching (batch processing doc).

## Brief: inputs

- Whole brief at most 2,000 characters.
- READ: exactly what to open, with line spans.
- "Open only READ; need more → return `NEED: <path> <why>`."
- GROUND TRUTH: facts the task needs, each with confirming command.
- Embed a random token in context files; missing from the return → that file was not read.

## Brief: outputs

- WRITE: the exact files it may change.
- ACCEPTANCE: one argv command that tests the kind, never a list of spellings; seen failing on a plant spelled unlike anything it lists.
- EXPECTED: the exact line ACCEPTANCE prints on PASS.
- RETURN ≤15 lines: `DONE <file> <counts>` or `BLOCKED <question> <options>`.

## Returns

- Accept only on your own run of ACCEPTANCE.
- Claim fails its check → keep its coordinates; re-derive there.
- Verdicts disputed or ≥90% identical → settle by planting.

## On failure

- Resume or retry once, with a changed brief and the change recorded; then one rung up.
- Permission refused → ask the owner once for the exact action; never retry it or route around it.
- After a fix: rerun its check, then the regression suite.

## Handoff, task boundary, or compaction: write a plan file

- Sections, in this order: BLOCKING, DONE, NOW, DECIDED, FAILED, NEXT.
- State, as values not locations, every fact NEXT's first three steps need.
- Quote verbatim the user's instructions still in force.
- Omit transcripts, listings, narration and history; history lives in a separate file, read by path only when a step names it.
- The next job starts in a fresh session from the plan file: a long thread re-read about 325,000 tokens on every call.

## Main window

- Emit only what changed: bounded edits, diffs, new facts.
- Plan file written → tell the user `/clear` is safe.
- Output over about 8,000 tokens → write it to a file; read back first 5, FAIL/ERROR lines, last 5, count. Smaller output stays: a hidden output was asked back 85% of the time.
- Derive what files settle; ask the rest in one message.

## Savings

- Claim a saving only from the same task measured before and after, same conditions: no token type rose, one fell, done-check passes.
- Count tokens per type from `~/.claude/projects/*/*.jsonl` usage fields; size a prompt before sending with the free count_tokens endpoint, never bytes/4.
- Timing checks compare a ratio or interleaved runs, never one mean against a fixed bar.
- Each round ends with one cut applied, its before, after and command appended to Cheap-Execution LESSONS.tsv. Cost over 2× the cheapest logged way → stop, name the rise.
- Later rounds fold general rows in by measured saving per word; each replaces a weaker line, so it never grows.
