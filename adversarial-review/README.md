# adversarial-review

A Claude Code skill for auditing a chain of stages: sealed plants, run-only checks at every seam, one
witness-giving reader, and a stop rule. It sits beside cheap-execution because it is the cheap way to
attack: checks that spend no model tokens run first, later rounds read only the diff since the last
head attacked, and every finding becomes a plant the target's own gate rechecks for free.

## Install

```sh
cp -r adversarial-review ~/.claude/skills/
```

## Measured

- Cells alone caught 8 of 8 hidden plants at 0 model tokens on SEED27 (Evidence in SKILL.md).
- A whole-tree round cost 231,180 tokens; the diff-only round after it, over four repos, about 24,000.
  Different targets, so this is not a same-task comparison.
