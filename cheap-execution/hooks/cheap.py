#!/usr/bin/env python3
"""PreToolUse hook: show the one cheap-execution clause that governs this call.

Clauses are data (clauses.tsv beside this file); each names a KIND, and the kinds below are the one
evaluator. Kinds read the shape of the command, never a list of spellings. Advisory: it exits 0
whatever happens (missing file, bad input, malformed row), so it can never block a call. Standard
library only; it runs with or without any other plugin.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SEP = re.compile(r"\|\||&&|;|\||\n")
RUNNER = re.compile(r"^\s*(\w+=\S*\s+)*(python3?\s+-m\s+(pytest|unittest)\b|pytest\b|make\s+(test|check)\b"
                    r"|npm\s+(run\s+)?test\b|cargo\s+test\b|go\s+test\b"
                    r"|(ba|z)?sh\s+\S*(test|check|gate|verify)\S*\.sh\b|python3?\s+\S*(test|check|gate|mutate)\S*\.py\b)")
SEARCH = re.compile(r"^\s*(grep|rg|ag|find|git\s+grep|ls|fd|echo|printf)\b")
FILTER = re.compile(r"^\s*(grep|rg|awk|sed|head|tail)\b")


def parts(cmd):
    """Top-level segments with the operator that follows each (None at the end)."""
    out, pos = [], 0
    for m in SEP.finditer(cmd):
        out.append((cmd[pos:m.start()], m.group()))
        pos = m.end()
    out.append((cmd[pos:], None))
    return out


def verifier_exit_lost(cmd):
    if "pipefail" in cmd:
        return False
    segs = parts(cmd)
    for i, (seg, op) in enumerate(segs):
        if RUNNER.search(seg) and op in ("|", ";", "||", "\n"):
            rest = "".join(s + (o or "") for s, o in segs[i + 1:])
            if op == "|" or "$?" not in rest:
                return True
    return False


def poll_loop(cmd):
    return bool(re.search(r"\b(while|until)\b[\s\S]*?\bdo\b", cmd) or re.search(r"\bwatch\s", cmd))


def filter_after_dump(cmd):
    for chain in re.split(r"\|\||&&|;|\n", cmd):
        stages = chain.split("|")
        if len(stages) > 1 and FILTER.match(stages[-1]) and not SEARCH.match(stages[0]) \
                and not RUNNER.search(stages[0]):
            return True
    return False


KINDS = {"any": lambda s: True, "verifier_exit_lost": verifier_exit_lost,
         "poll_loop": poll_loop, "filter_after_dump": filter_after_dump}
FIELD = {"Bash": "command", "Agent": "prompt", "Task": "prompt"}


def clauses(path=os.path.join(HERE, "clauses.tsv")):
    with open(path, encoding="utf-8") as f:
        for line in f:
            cells = line.rstrip("\n").split("\t")
            if len(cells) == 3 and not line.startswith("#") and cells[1] in KINDS:
                yield re.compile(cells[0]), KINDS[cells[1]], cells[2]


def first_hit(event):
    name, args = event.get("tool_name", ""), event.get("tool_input") or {}
    text = str(args.get(FIELD.get(name, ""), ""))
    for tool, kind, clause in clauses():
        if tool.fullmatch(name) and kind(text):
            return clause
    return None


def main():
    try:
        clause = first_hit(json.load(sys.stdin))
        if clause:
            print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse",
                                                     "additionalContext": "cheap-execution: " + clause}}))
    except Exception:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
