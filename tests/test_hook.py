"""Each kind fires on spellings it was not written from, stays silent on clean calls, shows one
clause per call, and the installed command exits 0 whatever happens."""
import json, os, subprocess, sys, tempfile, unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
HOOK = os.path.join(ROOT, "cheap-execution", "hooks", "cheap.py")
FRAGMENT = os.path.join(ROOT, "cheap-execution", "hooks", "settings.fragment.json")

EXIT, POLL, DUMP, BRIEF = "exit code is lost", "Do not poll", "Search the source directly", "Brief:"
FIRES = [
    ("Agent", "look at x", BRIEF),
    ("Bash", "python3 -m pytest -q | tail -n 5", EXIT),
    ("Bash", "pytest -q 2>&1 | tee out.txt", EXIT),
    ("Bash", "pytest -q | grep passed", EXIT),
    ("Bash", "bash checks.sh | tail -n 5", EXIT),
    ("Bash", "pytest -q; echo done", EXIT),
    ("Bash", "until [ -f done ]; do sleep 5; done", POLL),
    ("Bash", "while ! git diff --quiet; do git fetch; done", POLL),
    ("Bash", "bash -c 'until test -f done; do :; done'", POLL),
    ("Bash", "tac big.log | rg ERROR", DUMP),
    ("Bash", "sed -n p big.log | grep x", DUMP),
    ("Bash", "head -n 999999 big.log | grep x", DUMP),
    ("Bash", "python3 -c \"print(open('big.log').read())\" | grep x", DUMP),
]
SILENT = [
    ("Bash", "rg ERROR big.log"),
    ("Bash", "python3 -m pytest -q > out.txt; echo rc=$?"),
    ("Bash", "set -o pipefail; pytest -q | tail -n 5"),
    ("Bash", "grep -rn test . | head"),
    ("Bash", "echo check | head -n 1"),
    ("Bash", "git push || { sleep 2; git push; }"),
    ("Read", "x"),
]


def run(tool, text, cmd=None, env=None, raw=None):
    field = {"Bash": "command"}.get(tool, "prompt")
    data = raw if raw is not None else json.dumps({"tool_name": tool, "tool_input": {field: text}})
    p = subprocess.run(cmd or [sys.executable, HOOK], input=data, capture_output=True, text=True,
                       env=env or {"PATH": os.environ.get("PATH", "")})
    return p.returncode, (json.loads(p.stdout)["hookSpecificOutput"]["additionalContext"]
                          if p.stdout.strip() else None)


class Hook(unittest.TestCase):
    def test_fires(self):
        for tool, text, want in FIRES:
            with self.subTest(text=text):
                rc, got = run(tool, text)
                self.assertEqual(rc, 0)
                self.assertIn(want, got or "")

    def test_silent(self):
        for tool, text in SILENT:
            with self.subTest(text=text):
                self.assertEqual(run(tool, text), (0, None))

    def test_one_clause_per_call(self):
        rc, got = run("Bash", "cat f.txt | grep x; sleep 5; until [ -f d ]; do :; done")
        self.assertEqual(sum(k in (got or "") for k in (EXIT, POLL, DUMP)), 1, got)

    def test_bad_input_exits_zero(self):
        self.assertEqual(run("Bash", "", raw="{not json"), (0, None))

    def test_installed_command_never_blocks(self):
        command = json.load(open(FRAGMENT))["hooks"]["PreToolUse"][0]["hooks"][0]["command"]
        with tempfile.TemporaryDirectory() as home:
            rc, got = run("Bash", "pytest -q | tail", cmd=["sh", "-c", command],
                          env={"PATH": os.environ.get("PATH", ""), "HOME": home})
        self.assertEqual((rc, got), (0, None))


if __name__ == "__main__":
    unittest.main()
