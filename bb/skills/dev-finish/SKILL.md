---
name: dev-finish
description: End a coding session cleanly. Confirm the change works, capture decisions worth recording, write a short summary, run tests, then commit. Use when the user invokes /bb:dev-finish.
---

# dev-finish

Finalize the current coding session. Run the steps in order — don't skip ahead.

If the line below has content after the colon, treat it as user guidance to bear in mind throughout. Otherwise ignore.

Bear in mind: $ARGUMENTS

## 1. Confirm the change works

If this session produced a meaningful change (a new feature, a bug fix, a refactor with risk, a dependency update):

- If you already tested it end to end this session and it worked, note that and move on.
- If not, test it now. Use the project's local dev environment — consult `CLAUDE.md` or the project's readme for how to bring it up. Run the user-visible flow that exercises the change.
- If the test reveals a problem, **stop the wrap.** Summarize what failed and hand back to the user. Don't continue to summary or commit on broken code.

For trivial work (single-line fixes, doc edits, no behaviour change), say so in one line and skip.

## 2. Review for missed work

Look over the conversation and the current diff. Check for:

- **Discussed but not done** — things you talked about doing but didn't.
- **Tests** — new behaviour without tests, or tests you said you'd write.
- **TODOs** — `TODO` / `FIXME` left in the diff that shouldn't ship.
- **Cleanup** — debug prints, commented-out code, scratch files that shouldn't be committed.

If you find anything, present a short table summarizing each finding, walk through them one at a time, wait for the user's decision on each, then implement decisions in a single pass.

If nothing's missed, say so in one line and move on.

Leverage review and explore subagents where applicable, to check over the content provided, and have them report back to you with their findings.

## 3. Capture decisions worth recording

Review the session for **architectural decisions** worth writing down — choices that establish a principle, precedent, or convention that future work on this codebase should respect.

The bar is high. A decision record is a constraint on future work, not a project diary. Write one when:

- The decision sets a principle that future implementations must respect (e.g. "all currency values use minor units", "auth tokens never persist to disk").
- It establishes a convention (vocabulary, schema, naming, policy) the codebase will lean on consistently.
- It supersedes a previous decision.

Do **not** write one for: bug fixes, performance tweaks that solve one concrete problem, things obvious from reading the code, "here's how this currently works" descriptions.

If you can't articulate which future decision the record would constrain, don't write it.

If a candidate exists:

1. Propose it to the user in this shape — wait for approval before writing:

   > **Title:** `<kebab-case title naming the principle>`
   > **Principle:** `<the rule, stated in the abstract>`
   > **Today's instance:** `<the specific decision that surfaced it>`

2. If the project has an existing decision-record location (ADR directory, design-docs folder), use it. Otherwise ask, defaulting to `docs/decisions/<NNNN>-<slug>.md` with sequential numbering — create the directory if missing.

3. Write the record. Keep it short — context, decision, consequences.

## 4. Write a session summary

Write a short narrative of the session to `docs/summaries/<YYYY-MM-DD>-<slug>.md` (use the project's convention if it has one; create the directory if missing).

The summary captures **why** the code now looks the way it does — the reasoning that doesn't survive in the diff. See [summary.md](summary.md) for the spec.

**Skip when** the session was purely mechanical — single-line fix, formatting, dependency bump with no debate, pre-decided rename. When in doubt, ask the user.

## 5. Tests and lint

Run the project's test suite and any lint or type-check it uses.

- Find the command in `CLAUDE.md` or the project's README. Don't guess. If not provided, then ask a question.
- If anything fails, **stop and discuss with the user.** Don't commit failing code. Don't bypass hooks (`--no-verify`, etc.) without the user explicitly asking for it.
- If tests already ran and passed during this session, note that and skip re-running.

## 6. Commit

- Stage files by path (`git add <path>`), not `git add -A` or `git add .` — keeps secrets and scratch files out of commits by accident.
- Group related changes into one commit per concern. Unrelated changes go in separate commits.
- Use the project's commit-message convention if it has one (consult `CLAUDE.md` or recent `git log`). If there's no convention, write clear present-tense messages.
- Decision records and other docs are typically separate commits from code.
- Don't commit files that look like secrets (`.env`, credentials, keys). Flag them instead.
- If worktrees were used, inform the user which branch the implemented feature should be merged into. If no branch currently exists that matches the work done, and the user has not provided a branch name to use, then confirm with the user what branch to "branch off of", create it, and then merge the changes into that branch.
- If a github issue was referenced, inform the user of which issue was being targeted, provide a link to it, and remove the "progressing" label from it. 

After committing, hand back to the user. Pushing is the user's call.

If the user asks you to push, and open a PR, ensure that if a GitHub issue was referenced, the GitHub issue number is a part of the PR body.

## Extra

### Cleaning up after work

When the human says **"clean up"** (or "wrap up and clean up") after work is
committed, run these steps in order:

1. **Push** the current branch to the remote.
2. **Open a PR against the default base**. If a GitHub issue was
   referenced, include its number in the PR body.
3. **Automatically remove the worktree** once the branch is pushed — no need to
   ask first.
4. **Delete the plan file** (e.g. the `docs/plans/*.md` the session worked
   from) — automatically, no need to ask. A plan exists only to drive the work
   up to the PR; once the PR is open it has served its purpose, and the
   end-of-session summary captures anything worth keeping. Plans are **not**
   version-controlled (see "Session plans live in `docs/plans/`" below), so
   there's nothing to keep around after the PR is made.
5. **Offer to watch CI yourself.** Ask the human whether you should watch the
   PR's CI. If they say yes, run `gh pr checks <n> --watch` and **block until it
   finishes** — do not hand the build back to the human to follow. Then:
   - **All checks green** → merge the PR.
   - **Any check fails** → investigate and fix the failures (push fixes to the
     same branch and re-watch), rather than just reporting them back.

### When work is finished, close the related GitHub issue

After completing a piece of work, check GitHub (`gh issue list` / `gh issue
view`) for an issue the work resolves.

- **If the issue was explicitly referenced in the plan**, no confirmation is
  needed — add a comment summarizing the resolution (link the PR/commit) and
  close it.
- **Otherwise**, confirm with the human that it's the right issue before
  closing. Watch for a plan that cites a stale or duplicate issue number — the
  live issue may differ from the one named.



## Edge cases

- **Clean tree, nothing to wrap.** Say so in one line and exit.
- **Substantive session with no commits yet** (pure investigation, prompt iteration, debugging that informed a decision): still write the summary — that reasoning is exactly what would otherwise vanish.
- **User tells you to skip a step.** Honor it, but flag the risk if relevant (e.g. skipping tests on a non-trivial change).
- **Pre-commit hook fails.** The commit didn't happen. Fix the issue and create a new commit. Don't `--amend` or `--no-verify`.
