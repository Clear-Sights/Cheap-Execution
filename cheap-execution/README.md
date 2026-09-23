# cheap-execution

A Claude Code skill that cuts token spend without cutting verification.

## Why

Measured on 68 real Claude Code sessions (64,667 model calls):

- Cache reads were 98.6% of all tokens; output was 0.2%.
- A block that entered the conversation stayed there for about 480 model calls on average.

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

## How it was tested

Every line was checked on Claude Opus against a behaviour probe written for that line, first as
direct questions and then inside a realistic mid-task session, each with and without the skill.

- 23 lines change behaviour: the model gets them wrong without the skill and right with it.
- The rest are behaviours the model already shows, but removing them as a group made other lines
  fail, so they stay.
- Lines that changed nothing even with the skill loaded were removed.
- One line was misread (the model put the NEXT section first instead of writing it first); it was
  reworded and the misreading stopped.
