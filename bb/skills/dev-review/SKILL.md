---
name: dev-review
description: Review a GitHub pull request and post the outcome as a single review — verdict plus inline comments — after verifying every finding against the PR's head commit. Covers first reviews, re-reviews, and relaying findings from /code-review or other automated passes. Use when the user invokes /bb:dev-review.
---

# dev-review

Review for **duplication, inconsistencies, logic and structure**. Approve, or post findings as
inline comments on their lines. Every comment claims something about code at a specific commit —
verify it, yours or relayed, against that commit first.

If the line below has content after the colon, it names the PR(s) and any guidance. Otherwise ask
which PR.

PR and guidance: $ARGUMENTS

Automated passes (`/code-review`, `pr-review-toolkit:review-pr`, …) generate findings; this skill
verifies and posts them. Don't re-derive what they already produced.

## 1. Pin the ref

```bash
N=123                                   # the PR under review
T=/path/to/scratch                      # your session scratchpad, else $(mktemp -d) — write it down
R=$(gh repo view --json nameWithOwner -q .nameWithOwner)
B=$(gh pr view $N --repo $R --json baseRefName -q .baseRefName)
AUTHOR=$(gh pr view $N --repo $R --json author -q .author.login)
ME=$(gh api user -q .login)
git fetch origin "$B" "pull/$N/head"    # refresh the base too, or merge-base lies
HEAD_SHA=$(gh pr view $N --repo $R --json headRefOid -q .headRefOid)
BASE_SHA=$(git merge-base "origin/$B" "$HEAD_SHA")
printf '%s\n' "N=$N" "T=$T" "R=$R" "B=$B" "AUTHOR=$AUTHOR" "ME=$ME" \
  "HEAD_SHA=$HEAD_SHA" "BASE_SHA=$BASE_SHA" > "$T/env"
```

**Each shell call starts fresh** — the variables above are gone by the next one. Start every later
block with `. <T>/env`, writing the scratch path out literally. Without it `$HEAD_SHA` is empty: the
"head moved" guard compares against nothing and `commit_id` posts as `""`.

A stale `origin/$B` yields a base older than the true one, which inflates the diff and makes
pre-existing code read as new — the error this skill exists to prevent.

Then read what the PR claims and what it was asked to do:

```bash
gh pr view $N --repo $R --json title,body,closingIssuesReferences \
  --jq '.title, .body, (.closingIssuesReferences[].number)'
gh issue view <n> --repo $R             # each linked issue
```

The description's claims are things to verify, not facts. A linked issue's acceptance criteria
are review criteria: one the PR leaves unmet is a defect, unless the description says it is
deferred and why.

Check against the SHA, not the working tree — it may predate the base:

```bash
git grep -n "<symbol>" "$HEAD_SHA" -- src/   # right
grep -rn "<symbol>" src/                     # wrong — whatever is checked out
```

## 2. Get findings

If findings were handed to you (from `/code-review` or another pass), they are your input — go to
*Sort findings*. Otherwise, dispatch one `bb:dev-reviewer` for the PR: its tool output stays out of
your context and it returns a draft with a verification log. Reviewing the diff yourself is fine for
a small PR.

**Several PRs at once:** fetch every head in one command, then dispatch one `bb:dev-reviewer` per
PR, all in the same message. Parallel `git fetch` into one repo races on ref locks, and the agents
only read via `git show`/`git grep`, so the SHAs are all they need.

```bash
git fetch origin "$B" pull/193/head pull/382/head pull/421/head
```

Dispatch each agent with this prompt, filled in:

```markdown
Review PR #<N> in <R>. Return your draft; do not post anything.

- HEAD_SHA: <sha>
- BASE_SHA: <sha>
- Linked issues: <#n, … | none>
- Guidance from the user: <their focus, or none>
- Handed-down findings to verify: <list with path:line, or none>
- Your earlier review's open threads: <path:line — gist, or none>
```

**Check the draft before you use it.** Re-run the evidence command for every `Fabricated` and
`Pre-existing` line in the agent's verification log, and for one `Real` line. These are the verdicts
that drop or soften a finding, so a wrong one costs most. If a check disagrees, the draft is wrong:
fix it, don't post around it.

## 3. Sort findings

### Re-reviews

If you already hold a review on the PR, its threads are the first input. Per thread: does
`$HEAD_SHA` close it — resolved, still open, or filed as an issue? Don't re-raise resolved or
filed ones. The summary names which closed and the evidence (the test, the line).

```bash
gh api --paginate repos/$R/pulls/$N/reviews --jq ".[] | select(.user.login==\"$ME\") | \"\(.id)\t\(.state)\t\(.submitted_at)\""
gh api --paginate repos/$R/pulls/$N/comments --jq '.[] | select(.pull_request_review_id==<id>) | "\(.path):\(.line)\t\(.body[0:80])"'
```

(`/reviews/<id>/comments` carries only `position`, not `line`; the PR-wide endpoint has both.)

A `CHANGES_REQUESTED` of yours blocks the merge after everyone else has approved, and only a newer
review from you lifts it — see *Changing a verdict*.

### Every finding

Findings — from an automated pass, an agent, or you — are input, not output:

| Verdict | Test | Action |
|---|---|---|
| **Real** | Symbol exists at `$HEAD_SHA`, mechanism holds | Post |
| **Fabricated** | Symbol absent at that ref | Drop; if posted, retract in-thread |
| **Overstated** | Mechanism real, "new here" framing is not | Post reframed |
| **Pre-existing** | The file already did this at base | Say so; don't bill it here |

**Before claiming the PR caused something, diff the construct.** A `+` is not proof:

```bash
git show "$BASE_SHA:$FILE" | sed -n '/^function Thing/,/^}/p'
git show "$HEAD_SHA:$FILE" | sed -n '/^function Thing/,/^}/p'
```

A defect can be real while the causation is invented — the construct may have been that way at base.
The reverse holds too: an unchanged doc, caller or test that the PR's change makes wrong is the
PR's, even though the file is byte-identical at both SHAs.
Phrase findings on untouched code as "pre-existing", never as instructions. Verify the fix you
suggest, not just the defect: a fix that is itself incomplete costs the author a second round.

### Repo checks

Read the repo's `CLAUDE.md`, contributing guide and any spec or conventions docs they point to,
and apply what they require — a spec'd behaviour owes a test, an architecture boundary must not be
crossed, a convention must be followed. Cite the doc and line in the comment.

### Keep the review in scope

Real is not the same as in scope. A finding that would materially grow the PR — a refactor it only
touches, debt it makes conspicuous, a follow-up it enables — goes in the summary body under one
**Out of scope** heading, never as its own inline change request. Inline threads are then only what
the author acts on now; one grouped comment reads as a suggestion, six inline ones read as a rework
order.

```markdown
## Out of scope — follow-ups, not blockers
- <finding> — pre-existing, touches N other call sites
- <finding> — needs a new result variant and UI handling
```

If something out of scope genuinely should block, say why it cannot wait; otherwise it is a
follow-up, and naming it as one is what keeps the PR reviewable.

## 4. Decide

**Approve only if you would merge as-is.** Split what each finding asks of the author:

- A **defect** — code or docs the review shows doing the wrong thing, or new behaviour with no
  test — blocks: `REQUEST_CHANGES`. Anything that must change before merge is a defect.
- A **decision** the author can take either way and still merge — address it or file an issue,
  handle the edge case or document it — does not. Ask it inline, say it is non-blocking, and
  approve.
- Nits you'd accept ignored don't block.

Either way the body says which findings block and which don't, so a later change of verdict is one
sentence, not a rework of the threads.

**Check CI and mergeability before approving.** "Would merge as-is" includes the checks:

```bash
gh pr checks $N --repo $R
gh pr view $N --repo $R --json mergeable,mergeStateStatus
```

`UNKNOWN` means GitHub hasn't computed it yet; query again after a few seconds.

Don't approve over failing or pending required checks: say in the body what you are waiting on. A
`CONFLICTING` PR runs little or no CI, so its green is not evidence. If the PR lists no checks at
all, its base branch has no CI. In that case build and test `$HEAD_SHA` yourself in a scratch
worktree before approving, or say plainly in the body that you didn't.

**Your own PR:** if `$AUTHOR` = `$ME`, GitHub rejects `APPROVE` and `REQUEST_CHANGES` with a 422.
Post with `"event":"COMMENT"`, and have the body say which findings would block, since a comment
carries no verdict.

Show the user the verdict, summary and comments before posting. Posting is public.

## 5. Post

**One review, carrying every comment.** Post the verdict and all inline comments in a single
`POST .../reviews` with a `comments[]` array. This is the only way new findings end up attached to
the verdict.

Write the draft to `<T>/r.json` with your file-writing tool rather than a shell heredoc, which some
harnesses refuse:

```json
{"event":"REQUEST_CHANGES","body":"<summary>","comments":[
  {"path":"<path>","line":<n>,"side":"RIGHT","body":"..."},
  {"path":"<path>","line":<n>,"side":"RIGHT","body":"..."}]}
```

**Check every anchor before posting.** One `line` outside the diff and GitHub rejects the whole
review ("Line could not be resolved"). Only lines inside a hunk of the merge-base diff, changed or
context, can be anchored:

```bash
. <T>/env
jq -r '.comments[] | "\(.path) \(.line)"' $T/r.json | while read -r p l; do
  git diff "$BASE_SHA" "$HEAD_SHA" -- "$p" | awk -v l="$l" -v p="$p" '
    /^@@/ { split($3, a, /[+,]/); s = a[2]; n = (a[3] == "" ? 1 : a[3]); if (l >= s && l < s + n) ok = 1 }
    END   { if (!ok) print "not in diff: " p ":" l }'
done                                    # want no output
```

Move any line it prints into the summary as `file:line`. Then post:

```bash
. <T>/env
[ -n "$HEAD_SHA" ] && [ "$(gh pr view $N --repo $R --json headRefOid -q .headRefOid)" = "$HEAD_SHA" ] || { echo "head moved (or env not loaded) — re-verify first"; exit 1; }
jq --arg c "$HEAD_SHA" '. + {commit_id: $c}' $T/r.json > $T/post.json
RID=$(gh api repos/$R/pulls/$N/reviews --input $T/post.json --jq .id); echo "RID=$RID" >> $T/env
```

`commit_id` pins every anchor to the commit you verified against. Without it GitHub anchors to the
head at post time, which may not be the one you read.

If the post fails with "can only have one pending review", an earlier attempt left an unsubmitted
draft of yours. Find it, check it holds nothing you need, delete it, and post again:

```bash
gh api --paginate repos/$R/pulls/$N/reviews --jq ".[] | select(.user.login==\"$ME\" and .state==\"PENDING\") | .id"
gh api -X DELETE repos/$R/pulls/$N/reviews/<id>
```

**Never `POST .../comments` to raise a new finding.** That endpoint wraps each comment in its own
implicit `COMMENTED` review, so the comments detach from your verdict and the PR fills with
single-comment reviews. `gh pr review --request-changes` fails the same way from the other side —
it takes a body but cannot anchor comments.

Those endpoints are for reading and for threads that already exist:

```bash
gh api repos/$R/pulls/$N/comments --jq '.[] | "\(.id)\t\(.path):\(.line)"'   # list
gh api repos/$R/pulls/$N/comments/<id>/replies -f body='...'      # reply/retract in-thread
gh api -X PUT repos/$R/pulls/$N/reviews/<id> -F body=@$T/summary.md   # PUT, not PATCH
```

Editing one sentence of a body: `jq`'s `sub()` is a regex, so `**bold**` in the old text fails to
match and the `PUT` re-sends the unchanged body while reporting success. Replace literally and check
the response, not your file:

```bash
jq --arg o "$OLD" --arg n "$NEW" '{body: (.body | split($o) | join($n))}' $T/post.json > $T/put.json
gh api -X PUT repos/$R/pulls/$N/reviews/$RID --input $T/put.json --jq .body | grep -c "$NEW"   # want 1
```

Check it landed as one review, not N. `--paginate` or the check lies: the endpoint pages at 30,
and on a long-lived PR the review you just posted is on page 2.

```bash
gh api --paginate repos/$R/pulls/$N/reviews --jq ".[] | select(.user.login==\"$ME\") | .state" | sort | uniq -c
gh api --paginate repos/$R/pulls/$N/comments --jq "[.[] | select(.pull_request_review_id==$RID)] | length"  # = your comments[]
gh pr view $N --repo $R --json reviewDecision,mergeStateStatus
```

Only diff lines can be anchored; otherwise name `file:line` in the summary. Retract in the original
thread, and `PUT` the summary if it repeats the claim.

### Changing a verdict

To go from `REQUEST_CHANGES` to `APPROVE` after posting, don't dismiss and don't re-post the
comments. `PUT` the original body so it stops calling its findings blocking, then `POST` a new
`APPROVE` pinned to the same `commit_id` with a one-line body pointing at the threads above. GitHub
counts each reviewer's latest review, so the old one stops blocking and its threads stay put. The
same two calls clear a `CHANGES_REQUESTED` of yours that has outlived its fixes on a re-review.

Worked examples of each rule failing in practice, with the commands that would have caught it:
[`references/worked-examples.md`](references/worked-examples.md).
