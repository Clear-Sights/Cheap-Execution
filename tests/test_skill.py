"""Every file SKILL.md or README.md names resolves inside the skill folder, so the skill reaches all it reads."""
import os, re, subprocess, sys, unittest

SKILL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "cheap-execution")
NAMED = re.compile(r"(?<![/\w.])((?:evidence|pieces)/[\w.-]+\.(?:py|tsv|md)|[A-Z]+\.(?:md|tsv))\b")


def missing(text, root=SKILL):
    return sorted({p for p in NAMED.findall(text) if not os.path.exists(os.path.join(root, p))})


class Reach(unittest.TestCase):
    def test_named_files_exist(self):
        for doc in ("SKILL.md", "README.md"):
            with open(os.path.join(SKILL, doc), encoding="utf-8") as f:
                self.assertEqual(missing(f.read()), [], doc)

    def test_plant_is_caught(self):
        self.assertEqual(missing("see GONE.tsv and evidence/gone.py"), ["GONE.tsv", "evidence/gone.py"])

    def test_evidence_command_runs(self):
        out = subprocess.run([sys.executable, os.path.join(SKILL, "evidence", "compare.py")],
                             capture_output=True, text=True, check=True).stdout
        self.assertIn("process 48 blind", out)


if __name__ == "__main__":
    unittest.main()
