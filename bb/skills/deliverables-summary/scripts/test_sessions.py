"""Tests for sessions.py. Standard library only.

Run from the repo root:
  python3 -m unittest discover -s bb/skills/deliverables-summary/scripts
"""
import json
import os
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from sessions import is_prompt, path_key, under  # noqa: E402

SCRIPT = os.path.join(HERE, "sessions.py")


def prompt(session_id, uid, cwd, text="hi"):
    return {"type": "user", "sessionId": session_id, "uuid": uid, "timestamp": "2026-10-01T12:00:00Z",
            "cwd": cwd, "origin": {"kind": "human"}, "message": {"role": "user", "content": text}}


def title(session_id, text):
    return {"type": "ai-title", "sessionId": session_id, "aiTitle": text}


class MainTest(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.projects = os.path.join(tmp.name, "projects")
        self.work = os.path.realpath(tmp.name)
        os.makedirs(os.path.join(self.projects, "p"))

    def transcript(self, name, records, mtime):
        path = os.path.join(self.projects, "p", name + ".jsonl")
        with open(path, "w") as f:
            f.writelines(json.dumps(r) + "\n" for r in records)
        os.utime(path, (mtime, mtime))

    def run_script(self, *extra):
        # Wide window, so converting the timestamp to local time can't push it out.
        out = subprocess.run([sys.executable, SCRIPT, "--since", "2026-09-01", "--until", "2026-11-01",
                              "--folder", self.work, "--projects-dir", self.projects, *extra],
                             capture_output=True, text=True, check=True).stdout
        return json.loads(out)

    def test_copied_prompt_counts_once_in_oldest_transcript(self):
        # Early October, inside the window; the original is older.
        old, new = 1791000000, 1791090000
        self.transcript("original", [title("original", "Original"), prompt("original", "u1", self.work)], old)
        self.transcript("resumed", [title("resumed", "Resumed"), prompt("resumed", "u1", self.work),
                                    prompt("resumed", "u2", self.work)], new)
        self.transcript("forked", [title("forked", "Forked"), prompt("forked", "u1", self.work)], new + 10)
        sessions = {s["session_id"]: s for s in self.run_script()["sessions"]}
        self.assertEqual(sessions["original"]["prompts"], 1)
        self.assertEqual(sessions["resumed"]["prompts"], 1)
        self.assertNotIn("forked", sessions)  # its only prompt is a copy

    def test_folders_only_prints_no_titles(self):
        self.transcript("s", [title("s", "Secret title"), prompt("s", "u1", self.work)], 1791000000)
        result = self.run_script("--folders-only")
        self.assertEqual(result["folders"], [self.work])
        self.assertNotIn("sessions", result)
        self.assertNotIn("Secret title", json.dumps(result))


class IsPromptTest(unittest.TestCase):
    def user(self, content="hi", **fields):
        return {"type": "user", "message": {"role": "user", "content": content}, **fields}

    def test_origin_decides(self):
        self.assertTrue(is_prompt(self.user(origin={"kind": "human"})))
        self.assertFalse(is_prompt(self.user(origin={"kind": "task-notification"})))
        self.assertFalse(is_prompt(self.user(origin={"kind": "peer"})))

    def test_without_origin_falls_back_to_text(self):
        self.assertTrue(is_prompt(self.user("fix the bug")))
        self.assertFalse(is_prompt(self.user("<task-notification>done</task-notification>")))

    def test_tool_result_is_not_a_prompt(self):
        self.assertFalse(is_prompt(self.user([{"type": "tool_result", "content": "ok"}])))

    def test_flagged_records_are_not_prompts(self):
        for flag in ("isMeta", "isSidechain", "isCompactSummary"):
            self.assertFalse(is_prompt(self.user(origin={"kind": "human"}, **{flag: True})), flag)

    def test_other_types_are_not_prompts(self):
        self.assertFalse(is_prompt({"type": "assistant", "message": {"content": "hi"}}))


class UnderTest(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = os.path.realpath(tmp.name)
        self.folder = os.path.join(self.root, "b")
        os.makedirs(os.path.join(self.folder, "sub"))
        os.makedirs(os.path.join(self.root, "bc"))
        self.folders = [path_key(self.folder)]

    def test_exact_and_subfolder(self):
        self.assertTrue(under(self.folder, self.folders))
        self.assertTrue(under(os.path.join(self.folder, "sub"), self.folders))

    def test_sibling_with_shared_prefix(self):
        self.assertFalse(under(os.path.join(self.root, "bc"), self.folders))

    def test_symlink_resolved(self):
        link = os.path.join(self.root, "link")
        os.symlink(self.folder, link)
        self.assertTrue(under(os.path.join(link, "sub"), self.folders))

    @unittest.skipUnless(sys.platform == "darwin", "macOS paths are case-insensitive")
    def test_casing_ignored_on_macos(self):
        self.assertTrue(under(self.folder.upper(), self.folders))


if __name__ == "__main__":
    unittest.main()
