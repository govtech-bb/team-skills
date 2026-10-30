#!/usr/bin/env python3
"""Collect the current user's code activity for a period.

GitHub is the source of truth. Across every repo in the --org organisations,
`gh search prs` finds PRs the gh user authored (merged, or open at the end of
the period, which for a past period includes PRs merged after it ended) and PRs
they reviewed, and `gh search commits` finds their commits on each repo's
default branch. The window runs from local midnight to local midnight, because
GitHub's plain dates are UTC days and would move evening work into the next
period. A review counts in the period it was submitted in, not when its PR
last changed. Limiting to the work organisations keeps personal and
side-project repos out of an HR document.

Prints one JSON object. Merge commits and stash artifacts are dropped here;
grouping and wording are left to the caller.

Usage: git_activity.py --since 2026-09-23 --until 2026-10-23 --org govtech-bb [--org ...]
  --since / --until are dates; --until is exclusive.
"""
import argparse
import json
import re
import subprocess
import sys
from datetime import datetime


def gh(*args):
    """Run a gh command. A failure (rate limit, expired auth, network) must stop the script:
    an empty result would read as a period with no work in it."""
    result = subprocess.run(["gh", *args], capture_output=True, text=True)
    if result.returncode != 0:
        sys.exit(f"gh {args[0]} {args[1]} failed: {result.stderr.strip()}")
    return result.stdout.strip()


SEARCH_LIMIT = 1000  # the most GitHub search returns


def search(kind, *args):
    """Run a gh search. Hitting the limit must stop the script too: the results past it are
    dropped without a word, and they can be work inside the period."""
    out = gh("search", kind, *args, "--limit", str(SEARCH_LIMIT))
    results = json.loads(out) if out else []
    if len(results) >= SEARCH_LIMIT:
        sys.exit(f"gh search {kind} hit its {SEARCH_LIMIT}-result limit, so some results are missing")
    return results


NOISE = re.compile(r"^(Merge (pull request|branch|remote-tracking|main|.+ into )|WIP on |index on |On \S+: )")


def owner_filters(orgs):
    return [flag for org in orgs for flag in ("--owner", org)]


def search_prs(orgs, *filters):
    fields = "number,title,state,url,repository,author"
    prs = search("prs", *filters, *owner_filters(orgs), "--json", fields)
    return [{"repo": p["repository"]["nameWithOwner"], "number": p["number"], "title": p["title"],
             "state": p["state"], "url": p["url"], "author": p["author"]["login"]} for p in prs]


def local_midnight(day):
    return datetime.fromisoformat(day).astimezone()


def reviewed_prs(orgs, me, start, end):
    """Other people's PRs the user reviewed between start and end. Search can only filter on a
    PR's last update, so take every PR reviewed and touched since start, then check when each
    of the user's reviews was actually submitted."""
    candidates = [p for p in search_prs(orgs, "--reviewed-by", "@me", "--updated", f">={start.isoformat()}")
                  if p["author"] != me]  # gh search ignores a negated author qualifier
    reviewed = []
    for pr in candidates:
        # A pending review has no submitted_at yet.
        submitted = gh("api", "--paginate", f"repos/{pr['repo']}/pulls/{pr['number']}/reviews",
                       "--jq", f'.[] | select(.user.login == "{me}" and .submitted_at) | .submitted_at').split()
        if any(start <= datetime.fromisoformat(t.replace("Z", "+00:00")) < end for t in submitted):
            reviewed.append(pr)
    return reviewed


def github_commits(orgs, me, window):
    """The user's commits on the organisations' default branches, grouped by repo."""
    commits_found = search("commits", "--author", me, "--committer-date", window, *owner_filters(orgs),
                           "--json", "sha,commit,repository")
    repos = {}
    for item in commits_found:
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
    args = parser.parse_args()

    start, end = local_midnight(args.since), local_midnight(args.until)
    window = f"{start.isoformat()}..{end.isoformat()}"
    orgs = args.org
    authored_merged = search_prs(orgs, "--author", "@me", "--merged-at", window)
    created_before_end = f"<{end.isoformat()}"
    # A PR left open for months with no activity is paused or abandoned, not in progress.
    still_open = search_prs(orgs, "--author", "@me", "--created", created_before_end, "--state", "open",
                            "--updated", f">={start.isoformat()}")
    merged_later = search_prs(orgs, "--author", "@me", "--created", created_before_end, "--merged-at", f">={end.isoformat()}")
    open_at_end = list({p["url"]: p for p in still_open + merged_later}.values())
    me = gh("api", "user", "--jq", ".login")
    reviewed = reviewed_prs(orgs, me, start, end)

    print(json.dumps({
        "window": {"since": args.since, "until_exclusive": args.until},
        "github_user": me,
        "prs_merged": authored_merged,
        "prs_open_at_period_end": open_at_end,
        "prs_reviewed_for_others": reviewed,
        "github_commits": github_commits(orgs, me, window),
    }, indent=1))


if __name__ == "__main__":
    main()
