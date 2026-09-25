# cheap-execution

A Claude Code skill of rules meant to cut token spend without cutting verification. Its saving is
not yet measured; see "Not yet tested".

## Why

Measured on one Claude Code session (45 model calls when read) by
`python3 token_share.py '~/.claude/projects/*/*.jsonl'`:

- Cache reads were about 96% of all tokens; output was 0.3%.

So what matters is how long bytes stay in context, not how many get written. Every rule that keeps
bytes out of context, or clears them sooner, pays back on every later call.

## Install

```sh
cp -r cheap-execution ~/.claude/skills/
```

It loads on its own when its description matches the work, or on demand with `/cheap-execution`.

## What it covers

- which executor does each step, cheapest first (a script, you, or a cheaper model);
- how to dispatch agents: one per independent item, one for a whole-set answer, how wide to go;
- what an agent brief contains and what it returns, so the result can be checked without trust;
- what to do when a step fails or an agent's claim does not hold;
- how to hand off or compact so the next reader rereads nothing;
- how to prove a saving before claiming one.

## Not yet tested

No before-and-after token count exists for this skill. Every number in SKILL.md is a default until
one does; SKILL.md's Savings section says how to take it.
