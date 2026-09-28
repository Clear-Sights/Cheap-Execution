"""Each clause fires on a spelling it does not list and stays silent on the clean call."""
import json, os, subprocess, sys, unittest

HOOK = os.path.join(os.path.dirname(__file__), "..", "cheap-execution", "hooks", "cheap.py")

CASES = [  # (tool, input, expected fragment or None for silence)
    ("Agent", {"prompt": "look at x"}, "Brief:"),
    ("Bash", {"command": "tac big.log | rg ERROR"}, "Search the file directly"),
    ("Bash", {"command": "rg ERROR big.log"}, None),
    ("Bash", {"command": "until [ -f done ]; do sleep 5; done"}, "Do not poll"),
    ("Bash", {"command": "python3 -m pytest -q | tail -n 5"}, "exit code"),
    ("Bash", {"command": "python3 -m pytest -q > out.txt; echo rc=$?"}, None),
    ("Read", {"file_path": "x"}, None),
]


def run(tool, args):
    p = subprocess.run([sys.executable, HOOK], input=json.dumps({"tool_name": tool, "tool_input": args}),
                       capture_output=True, text=True, env={"PATH": os.environ.get("PATH", "")})
    assert p.returncode == 0, p.stderr
    return json.loads(p.stdout)["hookSpecificOutput"]["additionalContext"] if p.stdout.strip() else None


class Hook(unittest.TestCase):
    def test_cases(self):
        for tool, args, want in CASES:
            with self.subTest(tool=tool, args=args):
                got = run(tool, args)
                if want is None:
                    self.assertIsNone(got)
                else:
                    self.assertIn(want, got or "")
                    self.assertEqual(got.count("cheap-execution:"), 1)


if __name__ == "__main__":
    unittest.main()
