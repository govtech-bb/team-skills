# Worked examples

Each rule in `SKILL.md` exists because it failed in practice on a real team PR. These are the cases,
kept out of the skill so the rules stay readable.

## Pin the ref — a valid finding retracted as "hallucinated"

An automated pass reported that `personName` in `listCaseTimeline.ts` duplicates `userLabel` from
`src/core/userSummary.ts`. The reviewer ran:

```bash
grep -rn userLabel src/          # no output
```

…concluded the symbol did not exist, and publicly retracted the finding as fabricated.

`userLabel` did exist, added a few commits earlier. The working tree was checked out at an older
`main` that predated it. The finding was correct, and the retraction then had to be retracted.

```bash
git grep -n userLabel "$HEAD_SHA" -- src/    # would have found it
```

The same failure has a second form: a stale `origin/main` makes `git merge-base` return a base older
than the true one, so unchanged code appears in the diff and reads as new. Hence the fetch of the
base branch before computing `$BASE_SHA`.

## Diff the construct — invented causation

A `DispatchBlock` component was flagged: its wrapper kept `flex flex-col gap-xs` after an
`EntryHeader` extraction "left it a single child". The classes were indeed inert. But at base:

```tsx
<div className="… flex flex-col gap-xs">
  <div className="flex items-baseline justify-between gap-s">   {/* the only child */}
    <span>Sent</span>
    <time …/>
  </div>
</div>
```

The wrapper already had exactly one child. The extraction swapped one child for another and changed
nothing. The defect was real; the causation was invented, and the comment told the author to fix
something that was not theirs.

The line also carried no `+` — it was context in a changed hunk, which is not the same as changed.

## Keep the review in scope — six correct findings, two worth posting

A pass returned six findings, all technically correct. Only two were both in scope and caused by
the PR:

| # | Finding | Verdict |
|---|---|---|
| 1 | `beforeEach` clears a table then refills it via the new trigger | In scope — introduced here |
| 2 | New spec clause has no test | In scope — introduced here |
| 3 | `personName` duplicates `userLabel` | Pre-existing; 3 other call sites |
| 4 | Missing write-conflict → `conflict` mapping | Pre-existing; needs a new result variant + UI |
| 5 | Print route pays for queries it discards | Untouched file; fix splits a shared query |
| 6 | Five duplicate `textOf` test helpers | Already flagged as a follow-up in the code |

Posting all six inline would have read as a rework order on a PR whose real defects were a one-line
move and one missing test. 3–6 belong in one grouped section.

## A fix that was itself incomplete

The `beforeEach` finding above was posted with the fix "move `auditEvent.deleteMany()` below
`case.deleteMany()`". That is not enough: a `deleteMany()` two lines further down fires another
pre-existing trigger with no cascade guard. The correct fix was to move the line **last**.

Verify the fix you suggest, not just the defect you found.

## Post as one review — 28 reviews instead of one

The inline comments were raised with `POST /pulls/{n}/comments`, one call per finding. That endpoint
wraps each comment in its own implicit `COMMENTED` review, so the PR ended up with:

```
28 reviews, each holding exactly 1 comment, all COMMENTED
 1 review,  holding 0 comments,             CHANGES_REQUESTED
```

The verdict carried no comments and the comments carried no verdict. A reader opening the PR sees 29
reviews and has to work out which one is the decision.

The fix is to send the verdict and every comment in a single `POST /pulls/{n}/reviews` with a
`comments[]` array, and then check:

```bash
gh api --paginate repos/$R/pulls/$N/comments --jq '[.[] | .pull_request_review_id] | unique | length'   # want 1
```

## Paginate — an approval the check said was not there

A PR had more than thirty reviews. An `APPROVE` was posted and the check ran a second later:

```bash
gh api repos/$R/pulls/$N/reviews --jq ".[] | select(.user.login==\"$ME\") | .state" | sort | uniq -c
#   1 CHANGES_REQUESTED
#   7 COMMENTED
```

No `APPROVED` — yet `gh pr view` said `reviewDecision=APPROVED`. The endpoint pages at 30 and the
new review was on page 2. `--paginate` shows it. Any check that counts reviews or comments on a PR
with history needs it, or a correct post reads as a failed one.

## Replace literally — a `PUT` that changed nothing

To downgrade a verdict, the summary sentence "**REQUEST_CHANGES** only because two of them need a
decision" was to be rewritten before posting the approval:

```bash
jq --arg o "$OLD" --arg n "$NEW" '{body: (.body | sub($o; $n))}' review.json > put.json
gh api -X PUT repos/$R/pulls/$N/reviews/$RID --input put.json    # 200 OK
```

The `PUT` succeeded and the body was unchanged. `sub()` takes a regex; the `**` in the old text is
not a literal there, so nothing matched and the unchanged body was sent back. `split($o) | join($n)`
is literal, and the check belongs on the response — `--jq .body | grep -c "$NEW"` — not on the file
you built.
