#!/usr/bin/env python3
"""List the user's Claude Code sessions that were active in a period.

Claude Code keeps each session's transcript in ~/.claude/projects/<project>/<id>.jsonl.
A session is kept when it has a record inside the window (local midnight to local
midnight) whose working directory is under one of the --folder paths. Filtering on
the folder rather than the git remote keeps working after a worktree is deleted,
and keeps personal and side-project sessions out of an HR document.

Only metadata comes out: titles, folders, branches, linked PRs, the local days the
session was active and a prompt count. Transcripts can hold secrets and personal data, so no prompt or reply
text is ever printed.

Prints one JSON object. history_starts is the earliest record in any transcript:
Claude Code deletes old transcripts (cleanupPeriodDays, 30 by default), so a period
that starts before it is only partly covered.

Usage: sessions.py --since 2026-09-23 --until 2026-10-23 --folder ~/Documents/Projects [--folder ...]
  --since / --until are dates; --until is exclusive.
"""
import argparse
import glob
import json
import os
import sys
from datetime import datetime


def parse_time(timestamp):
    return datetime.fromisoformat(timestamp.replace("Z", "+00:00")).astimezone()


def path_key(path):
    # macOS paths are case-insensitive, and the same folder turns up in both spellings.
    path = os.path.normpath(os.path.expanduser(path))
    return path.casefold() if sys.platform == "darwin" else path


def under(path, folders):
    key = path_key(path)
    return any(key == folder or key.startswith(folder + os.sep) for folder in folders)


def is_prompt(record):
    """A message the user typed, as opposed to a tool result sent back on their behalf."""
    if record.get("type") != "user" or record.get("isSidechain"):
        return False
    content = record.get("message", {}).get("content")
    return isinstance(content, str) or (
        isinstance(content, list) and not any(part.get("type") == "tool_result" for part in content))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--since", required=True)
    parser.add_argument("--until", required=True, help="exclusive")
    parser.add_argument("--folder", action="append", required=True, help="a folder the user does work in")
    parser.add_argument("--projects-dir", default="~/.claude/projects")
    args = parser.parse_args()

    start = datetime.fromisoformat(args.since).astimezone()
    end = datetime.fromisoformat(args.until).astimezone()
    folders = [path_key(folder) for folder in args.folder]
    # Subagent transcripts sit one level deeper and belong to their parent session.
    transcripts = glob.glob(os.path.join(os.path.expanduser(args.projects_dir), "*", "*.jsonl"))

    sessions = {}
    history_starts = None
    for transcript in transcripts:
        with open(transcript, errors="replace") as lines:
            for line in lines:
                try:
                    record = json.loads(line)
                except ValueError:
                    continue
                session = sessions.setdefault(record.get("sessionId") or os.path.basename(transcript)[:-len(".jsonl")], {
                    "days": set(), "folders": set(), "branches": set(), "prompts": 0,
                    "ai_title": None, "custom_title": None, "prs": {}, "continued_in": None})
                kind = record.get("type")
                if kind == "ai-title":
                    session["ai_title"] = record.get("aiTitle")
                elif kind == "custom-title":
                    session["custom_title"] = record.get("customTitle")
                elif kind == "pr-link":
                    session["prs"][record["prUrl"]] = {"repo": record.get("prRepository"),
                                                       "number": record.get("prNumber"), "url": record["prUrl"]}
                elif kind == "continued-in":
                    session["continued_in"] = record.get("continuedInSessionId")

                if not record.get("timestamp"):
                    continue
                when = parse_time(record["timestamp"])
                history_starts = min(history_starts or when, when)
                cwd = record.get("cwd")
                if not (start <= when < end) or not cwd or not under(cwd, folders):
                    continue
                session["days"].add(when.date().isoformat())
                session["folders"].add(cwd)
                if record.get("gitBranch") and record["gitBranch"] != "HEAD":
                    session["branches"].add(record["gitBranch"])
                session["prompts"] += is_prompt(record)

    active = [{"session_id": session_id,
               "title": s["custom_title"] or s["ai_title"],
               "days": sorted(s["days"]),
               "prompts": s["prompts"],
               "folders": sorted(s["folders"]), "branches": sorted(s["branches"]),
               "prs": list(s["prs"].values()),
               "continued_in": s["continued_in"]}
              for session_id, s in sessions.items() if s["days"]]
    active.sort(key=lambda s: s["days"])

    print(json.dumps({
        "window": {"since": args.since, "until_exclusive": args.until},
        "history_starts": history_starts.date().isoformat() if history_starts else None,
        "sessions": active,
    }, indent=1))


if __name__ == "__main__":
    main()
