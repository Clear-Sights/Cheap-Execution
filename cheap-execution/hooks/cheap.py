#!/usr/bin/env python3
"""PreToolUse hook: show the cheap-execution clause that governs this call, and only that one.

Clauses are data (clauses.tsv beside this file); this is their one evaluator. Advisory: it never
blocks. Needs only the Python standard library; it runs with or without any other plugin.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))


def clauses(path=os.path.join(HERE, "clauses.tsv")):
    with open(path, encoding="utf-8") as f:
        for line in f:
            if line.strip() and not line.startswith("#"):
                tool, field, pattern, text = line.rstrip("\n").split("\t")
                yield re.compile(tool), field, re.compile(pattern, re.I | re.S), text


def hits(event):
    name, args = event.get("tool_name", ""), event.get("tool_input") or {}
    return [text for tool, field, pat, text in clauses()
            if tool.fullmatch(name) and pat.search(str(args.get(field, "")))]


def main():
    found = hits(json.load(sys.stdin))
    if found:
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse",
                                                 "additionalContext": "cheap-execution: " + " ".join(found)}}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
