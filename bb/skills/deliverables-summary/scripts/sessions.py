#!/usr/bin/env python3
"""List the user's Claude Code sessions that were active in a period.

Claude Code keeps each session's transcript in ~/.claude/projects/<project>/<id>.jsonl.
A session is kept when the user typed a prompt in it inside the window (local
midnight to local midnight) while its working directory was under one of the
--folder paths. Filtering on
the folder rather than the git remote keeps working after a worktree is deleted,
and keeps personal and side-project sessions out of an HR document.

Only metadata comes out: titles, folders, branches, linked PRs, the local days the
user sent a prompt and a prompt count. A prompt copied into a resumed or forked
session is counted once, in the oldest transcript. Transcripts can hold secrets and
personal data, so no prompt or reply text is printed. Titles are generated from the
prompts, though, so they can still name people or things from the work.

Prints one JSON object. Claude Code deletes a transcript once it has had no activity
for cleanupPeriodDays (30 by default), so history_starts is the oldest surviving
transcript's last activity. A period that starts before it is only partly covered:
sessions that ended earlier were deleted, or there weren't any.

Exits with an error when there are no transcripts at all, because an empty result
would read as a period with no sessions in it.

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
    # Transcripts record the physical folder, and macOS paths are case-insensitive, so the
    # same folder turns up behind symlinks (/tmp is /private/tmp) and in both spellings.
    path = os.path.realpath(os.path.expanduser(path))
    return path.casefold() if sys.platform == "darwin" else path


def under(path, folders):
    key = path_key(path)
    return any(key == folder or key.startswith(folder + os.sep) for folder in folders)


# Transcripts from before Claude Code recorded a prompt's origin write these as ordinary
# user messages, but nobody typed them.
INJECTED = ("<task-notification", "[Request interrupted", "<local-command-stdout", "<bash-stdout")


def is_prompt(record):
    """A message the user typed, as opposed to a tool result, skill text or notification."""
    if record.get("type") != "user" or record.get("isSidechain") or record.get("isMeta") \
            or record.get("isCompactSummary"):
        return False
    if "origin" in record:
        return (record["origin"] or {}).get("kind") == "human"
    content = (record.get("message") or {}).get("content")
    if isinstance(content, list):
        parts = [part for part in content if isinstance(part, dict)]
        if any(part.get("type") == "tool_result" for part in parts):
            return False
        content = next((part.get("text", "") for part in parts if part.get("type") == "text"), "")
    return isinstance(content, str) and not content.lstrip().startswith(INJECTED)


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
    # Claude Code may delete a transcript while this runs.
    last_activity = {}
    for transcript in transcripts:
        try:
            last_activity[transcript] = os.path.getmtime(transcript)
        except OSError:
            pass
    if not last_activity:
        sys.exit(f"no Claude Code transcripts in {args.projects_dir}")
    history_starts = datetime.fromtimestamp(min(last_activity.values())).astimezone()

    sessions = {}
    seen = set()  # a resumed/forked session re-writes earlier prompts under a new sessionId
    for transcript in sorted(last_activity, key=last_activity.get):  # originals before their copies
        if last_activity[transcript] < start.timestamp():
            continue
        try:
            lines = open(transcript, errors="replace")
        except OSError:
            continue
        with lines:
            for line in lines:
                try:
                    record = json.loads(line)
                except ValueError:
                    continue
                if not isinstance(record, dict):
                    continue
                session = sessions.setdefault(record.get("sessionId") or os.path.basename(transcript)[:-len(".jsonl")], {
                    "days": set(), "folders": set(), "branches": set(), "prompts": 0,
                    "ai_title": None, "custom_title": None, "prs": {}, "continued_in": None})
                kind = record.get("type")
                if kind == "ai-title":
                    session["ai_title"] = record.get("aiTitle")
                elif kind == "custom-title":
                    session["custom_title"] = record.get("customTitle")
                elif kind == "pr-link" and record.get("prUrl"):
                    session["prs"][record["prUrl"]] = {"repo": record.get("prRepository"),
                                                       "number": record.get("prNumber"), "url": record["prUrl"]}
                elif kind == "continued-in":
                    session["continued_in"] = record.get("continuedInSessionId")

                try:
                    when = parse_time(record["timestamp"])
                except (KeyError, TypeError, ValueError):
                    continue
                cwd = record.get("cwd")
                if not (start <= when < end) or not cwd or not under(cwd, folders):
                    continue
                session["folders"].add(cwd)
                if record.get("gitBranch") and record["gitBranch"] != "HEAD":
                    session["branches"].add(record["gitBranch"])
                # Only typed prompts mark a day: a session left open keeps writing records.
                if is_prompt(record):
                    uid = record.get("uuid")
                    if uid in seen:
                        continue
                    if uid:
                        seen.add(uid)
                    session["days"].add(when.date().isoformat())
                    session["prompts"] += 1

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
        "history_starts": history_starts.date().isoformat(),
        "sessions": active,
    }, indent=1))


if __name__ == "__main__":
    main()
