---
name: cheap-execution
description: Use before dispatching agents, big reads, repeated steps, handoffs, or compactions.
---

# Cheap Execution

## Terms

- Plant: break an input on purpose; the check must fail.

## Rungs: take the first that applies

1. Search existing sources first; found → read, not recompute.
2. Same input always gives same answer → compute with code.
3. Pruning code costs less than model reading all → prune.
4. Smaller than its own brief → do it here.
5. Has ACCEPTANCE, reversible, internal → cheaper executor; else here.

## Every step

- Anything processing items reports in, out, and dropped counts.
- Check every reported number against its source's own figure.
- Work shared across items → do once, store for all.
- Facts for a next reader: state values, not locations.

## Dispatch

- Give each agent everything its answer depends on.
- Parallel agents share no writable state.
- Grant each agent only the tools its task needs.
- At most 2 verification agents per gate.
- Inputs that may change mid-run → pin by content hash.

## Fan-out

- Width starts at min(4, independent items).
- Next round: +1 if all unique and passing, else −1.
- Rate-limit or usage-limit error → halve width.
- Keep every repeated prompt's prefix byte-identical.
- Returns over 30 lines → one agent condenses to 30.

## Brief: inputs

- Whole brief at most 2,000 characters.
- READ: exactly what to open, with line spans.
- "Open only READ; need more → return `NEED: <path> <why>`."
- GROUND TRUTH: facts the task needs, each with confirming command.
- Embed a random token in context files; require it returned.

## Brief: outputs

- WRITE: the exact files it may change.
- ACCEPTANCE: one argv command, seen failing on a plant.
- EXPECTED: the exact line ACCEPTANCE prints on PASS.
- RETURN ≤15 lines: `DONE <file> <counts>` or `BLOCKED <question> <options>`.

## Returns

- Accept only on your own run of ACCEPTANCE.
- Resume any agent at most once.
- Token missing → treat the context file as unread.
- Claim fails its check → keep its coordinates; re-derive there.
- Verdicts disputed or ≥90% identical → settle by planting.

## Done twice by hand → make it run unasked

- Its output becomes the next act's input.
- Move it inside the act's one entry point.
- Assert the expected count before acting.

## On failure

- Each retry changes the brief; record what changed.
- Retry once with a fresh agent, then one rung up.
- After a fix: rerun its check, then the regression suite.

## Handoff, task boundary, or compaction: write a plan file

- Sections, in this order: BLOCKING, DONE, NOW, DECIDED, FAILED, NEXT.
- State every fact NEXT's first three steps need.
- Each fact carries its producing command, or `believed`.
- Quote verbatim the user's instructions still in force.
- Omit transcripts, listings, and narration.

## Main window

- Emit only what changed: bounded edits, diffs, new facts.
- Plan file written → tell the user `/clear` is safe.
- Output over 50 lines → write it to a file.
- Read back first 5, FAIL/ERROR lines, last 5, count.
- Derive what files settle; ask the rest in one message.

## Savings

- Measure the same task before and after, same conditions.
- Count tokens per type from `~/.claude/projects/*/*.jsonl` usage fields.
- Saving: no token type rose, one fell, done-check passes.
- Log each recurring job's token cost in a file.
- Cost over 2× lowest log → stop, name the rise.
