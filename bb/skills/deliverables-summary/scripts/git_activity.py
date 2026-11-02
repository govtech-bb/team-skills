#!/usr/bin/env python3
"""Collect the current user's code activity for a period.

GitHub is the source of truth. Across every repo in the --org organisations,
`gh search prs` finds PRs the gh user authored (merged, or open at the end of
the period, which for a past period includes PRs merged after it ended) and PRs
they reviewed, `gh search commits` finds their commits on each repo's default
branch, and a GraphQL search finds issues assigned to them and closed as
completed. The window runs from local midnight to local midnight, because
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


def local_day(timestamp):
    """The user's local date of a GitHub timestamp, so per-day activity lines up with the calendar."""
    return datetime.fromisoformat(timestamp.replace("Z", "+00:00")).astimezone().date().isoformat()


def search_prs(orgs, *filters):
    fields = "number,title,state,url,repository,author,createdAt,closedAt"
    prs = search("prs", *filters, *owner_filters(orgs), "--json", fields)
    # closedAt is the merge time for a merged PR (search has no mergedAt field), and
    # 0001-01-01 for an open one.
    return [{"repo": p["repository"]["nameWithOwner"], "number": p["number"], "title": p["title"],
             "state": p["state"], "url": p["url"], "author": p["author"]["login"],
             "opened": local_day(p["createdAt"]),
             "closed": None if p["closedAt"].startswith("0001-") else local_day(p["closedAt"])}
            for p in prs]


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
        in_period = [t for t in submitted if start <= datetime.fromisoformat(t.replace("Z", "+00:00")) < end]
        if in_period:
            reviewed.append({**pr, "reviewed_on": sorted({local_day(t) for t in in_period})})
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
        commits.setdefault(item["sha"], {"sha": item["sha"][:9], "date": local_day(item["commit"]["committer"]["date"]),
                                         "subject": subject})
    return [{"repo": repo,
             "commits": sorted(commits.values(), key=lambda c: c["date"], reverse=True)}
            for repo, commits in sorted(repos.items())]


CLOSED_ISSUES_QUERY = """
query($q: String!, $endCursor: String) {
  search(type: ISSUE, query: $q, first: 100, after: $endCursor) {
    pageInfo { hasNextPage endCursor }
    nodes { ... on Issue { number title url closedAt repository { nameWithOwner }
      closes: timelineItems(itemTypes: [CLOSED_EVENT], last: 1) { nodes { ... on ClosedEvent {
        actor { login } closer { ... on PullRequest { url author { login } } ... on Commit { ...commit } } } } }
      refs: timelineItems(itemTypes: [CROSS_REFERENCED_EVENT, REFERENCED_EVENT], first: 100) { nodes {
        ... on CrossReferencedEvent { source { ... on PullRequest { url merged author { login } } } }
        ... on ReferencedEvent { commit { ...commit } } } } } }
  }
}
fragment commit on Commit { oid url author { user { login } } }"""


def author_login(link):
    """A PR's or commit's author login. A commit's author is a git identity, linked to a login only
    when GitHub can match it."""
    author = link.get("author") or {}
    return (author.get("user") or {}).get("login") if "oid" in link else author.get("login")


def issues_closed(orgs, me, window, prs, commits):
    """Issues assigned to the user and closed as completed, less the ones whose work is already in
    the user's own prs or commits: closed by one of them, or referenced by one ("Refs #12" closes
    nothing). GraphQL, because gh search can't return an issue's timeline. The assignee is whoever
    is assigned now, not when the issue was closed, so closed_by says who closed it: the closing
    PR's author, since whoever merges a PR is often not who did the work. earlier_work lists the
    user's own merged PRs and commits linked to a kept issue, which, being outside prs and
    commits, in practice means work from an earlier period."""
    query = " ".join(["is:issue", "reason:completed", "assignee:@me", f"closed:{window}",
                      *(f"org:{org}" for org in orgs)])
    pages = json.loads(gh("api", "graphql", "--paginate", "--slurp", "-f", f"query={CLOSED_ISSUES_QUERY}",
                          "-f", f"q={query}"))
    issues = [i for page in pages for i in page["data"]["search"]["nodes"]]
    if len(issues) >= SEARCH_LIMIT:
        sys.exit(f"the closed-issues search hit its {SEARCH_LIMIT}-result limit, so some results are missing")
    covered = {p["url"] for p in prs} | {c["sha"] for repo in commits for c in repo["commits"]}
    kept = []
    for issue in issues:
        close = next(iter(issue["closes"]["nodes"]), {})
        closer = close.get("closer") or {}
        links = [closer] + [ref.get("source") or ref.get("commit") or {} for ref in issue["refs"]["nodes"]]
        # prs are keyed by url and commits by short sha; a cross-reference from an issue is an empty link.
        if covered.intersection(link["oid"][:9] if "oid" in link else link.get("url") for link in links):
            continue
        closed_by = (closer.get("author") if "oid" not in closer else None) or close.get("actor")
        mine = {link["url"] for link in links if link.get("merged", True) and author_login(link) == me}
        kept.append({"repo": issue["repository"]["nameWithOwner"], "number": issue["number"],
                     "title": issue["title"], "url": issue["url"], "closed": local_day(issue["closedAt"]),
                     "closed_by": closed_by["login"] if closed_by else None, "earlier_work": sorted(mine)})
    return kept


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
    commits = github_commits(orgs, me, window)

    print(json.dumps({
        "window": {"since": args.since, "until_exclusive": args.until},
        "github_user": me,
        "prs_merged": authored_merged,
        "prs_open_at_period_end": open_at_end,
        "prs_reviewed_for_others": reviewed,
        "github_commits": commits,
        "issues_closed": issues_closed(orgs, me, window, authored_merged + open_at_end, commits),
    }, indent=1))


if __name__ == "__main__":
    main()
