#!/usr/bin/env python3
"""Collect the current user's code activity for a period.

GitHub is the source of truth. Across every repo in the --org organisations,
`gh search prs` finds PRs the gh user authored (merged, or still open) and PRs
they reviewed, and `gh search commits` finds their commits on each repo's
default branch. Limiting to the work organisations keeps personal and
side-project repos out of an HR document.

--root is optional. When given, it scans the git repos (and worktrees) up to
two levels under each folder and adds only commits that were never pushed.
Pushed branch work already shows up as PRs, and squash-merged branch commits
would only repeat their PR. Worktrees of one repo are grouped by their origin
URL, so shared history is read once.

Prints one JSON object. Merge commits and stash artifacts are dropped here;
grouping and wording are left to the caller.

Usage: git_activity.py --since 2026-09-23 --until 2026-10-23 --org govtech-bb [--org ...] [--root ~/Documents/Projects ...]
  --since / --until are dates; --until is exclusive.
"""
import argparse
import json
import os
import re
import subprocess
from datetime import date, timedelta


def run(cmd, cwd=None):
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    return result.stdout.strip() if result.returncode == 0 else ""


def find_repos(root):
    root = os.path.expanduser(root)
    candidates = [root]
    for entry in sorted(os.listdir(root)):
        path = os.path.join(root, entry)
        if os.path.isdir(path) and not entry.startswith("."):
            candidates.append(path)
            try:
                candidates += [os.path.join(path, sub) for sub in sorted(os.listdir(path))
                               if os.path.isdir(os.path.join(path, sub)) and not sub.startswith(".")]
            except PermissionError:
                pass
    return [p for p in candidates if os.path.exists(os.path.join(p, ".git"))]


def repo_key(path):
    url = run(["git", "config", "--get", "remote.origin.url"], cwd=path)
    match = re.search(r"[:/]([^/:]+/[^/]+?)(?:\.git)?$", url)
    return match.group(1) if match else os.path.realpath(path)


NOISE = re.compile(r"^(Merge (pull request|branch|remote-tracking|main|.+ into )|WIP on |index on |On \S+: )")


def unpushed_commits(roots, since, until):
    groups = {}
    for root in roots:
        for path in find_repos(root):
            groups.setdefault(repo_key(path), []).append(path)

    repos = []
    for key, paths in sorted(groups.items()):
        path = paths[0]
        authors = {run(["git", "config", "user.email"], cwd=path), run(["git", "config", "user.name"], cwd=path)}
        # A branch whose upstream is gone was pushed, merged and deleted: its work is
        # already on GitHub. Only commits ahead of a live upstream, or on a branch that
        # was never pushed, are missing from GitHub.
        ranges = []
        refs = run(["git", "for-each-ref", "--format=%(refname:short)\t%(upstream:short)\t%(upstream:track)",
                    "refs/heads"], cwd=path)
        for line in refs.splitlines():
            branch, upstream, track = (line.split("\t") + ["", ""])[:3]
            if "gone" in track:
                continue
            ranges.append([f"{upstream}..{branch}"] if upstream else [branch, "--not", "--remotes"])
        seen = {}
        for rng in ranges:
            args = ["git", "log", *rng, "--no-merges", f"--since={since}", f"--until={until}",
                    "--pretty=%H%x09%ad%x09%s", "--date=format-local:%Y-%m-%d"]
            args += [f"--author={a}" for a in authors if a]
            for line in run(args, cwd=path).splitlines():
                sha, day, subject = line.split("\t", 2)
                if not NOISE.match(subject):
                    seen.setdefault(sha, {"sha": sha[:9], "date": day, "subject": subject})
        if seen:
            branches = sorted({run(["git", "branch", "--show-current"], cwd=p) for p in paths} - {""})
            repos.append({"repo": key, "branches": branches,
                          "commits": sorted(seen.values(), key=lambda c: c["date"], reverse=True)})
    return repos


def owner_filters(orgs):
    return [flag for org in orgs for flag in ("--owner", org)]


def search_prs(orgs, *filters):
    fields = "number,title,state,url,repository,author"
    out = run(["gh", "search", "prs", *filters, *owner_filters(orgs), "--limit", "200", "--json", fields])
    prs = json.loads(out) if out else []
    return [{"repo": p["repository"]["nameWithOwner"], "number": p["number"], "title": p["title"],
             "state": p["state"], "url": p["url"], "author": p["author"]["login"]} for p in prs]


def github_commits(orgs, me, window):
    """The user's commits on the organisations' default branches, grouped by repo."""
    out = run(["gh", "search", "commits", "--author", me, "--committer-date", window, *owner_filters(orgs),
               "--limit", "1000", "--json", "sha,commit,repository"])
    repos = {}
    for item in json.loads(out) if out else []:
        repo = item["repository"]["fullName"]
        subject = item["commit"]["message"].split("\n")[0]
        if NOISE.match(subject):
            continue
        commits = repos.setdefault(repo, {})
        commits.setdefault(item["sha"], {"sha": item["sha"][:9], "date": item["commit"]["committer"]["date"][:10],
                                         "subject": subject})
    return [{"repo": repo,
             "commits": sorted(commits.values(), key=lambda c: c["date"], reverse=True)}
            for repo, commits in sorted(repos.items())]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--since", required=True)
    parser.add_argument("--until", required=True, help="exclusive")
    parser.add_argument("--org", action="append", required=True, help="the user's work organisations on GitHub")
    parser.add_argument("--root", action="append", default=[], help="optional local folders, for work not on GitHub yet")
    args = parser.parse_args()

    last = (date.fromisoformat(args.until) - timedelta(days=1)).isoformat()
    window = f"{args.since}..{last}"
    orgs = args.org
    authored_merged = search_prs(orgs, "--author", "@me", "--merged-at", window)
    authored_open = search_prs(orgs, "--author", "@me", "--created", window, "--state", "open")
    me = run(["gh", "api", "user", "--jq", ".login"])
    # gh search ignores a negated author qualifier, so drop the user's own PRs here.
    reviewed = [p for p in search_prs(orgs, "--reviewed-by", "@me", "--updated", window) if p["author"] != me]
    unpushed = [repo for repo in unpushed_commits(args.root, args.since, args.until)
                if repo["repo"].split("/")[0] in orgs]

    print(json.dumps({
        "window": {"since": args.since, "until_exclusive": args.until},
        "github_user": me,
        "prs_merged": authored_merged,
        "prs_open": authored_open,
        "prs_reviewed_for_others": reviewed,
        "github_commits": github_commits(orgs, me, window),
        "unpushed_commits": unpushed,
    }, indent=1))


if __name__ == "__main__":
    main()
