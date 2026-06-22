---
name: standup
description: Produce a bulleted standup summary of the user's work since the end of the previous workday's standup, built from git history and merged PRs in the current repo. On first run it asks what time standup ends; run with "change time" to update it. Use when the user invokes /bb:standup.
---

# Standup Summary

Produce a concise, bulleted summary of what the current user completed **from
the end of the previous workday's standup up to right now**, so they can read
straight from it during standup. The summary is built from git history (and
merged PRs) in the current repository.

The "end of the previous standup" is a per-user, configurable time of day —
read on below for how it's stored and how the user sets or changes it.

## Routing — decide what to do from how you were invoked

The user's arguments are: **$ARGUMENTS**

- If the arguments mention **"change time"** (or just "change"/"set time") →
  follow [Changing the standup-end time](#changing-the-standup-end-time), then
  stop. Do **not** also produce a summary unless the user asks.
- Otherwise → follow [Produce the summary](#produce-the-summary). That flow
  handles the **first-run** case (no time configured yet) on its own.

## The standup-end time (configuration)

The time the previous standup ended is stored, per user, in a small JSON file
the skill owns:

```
~/.claude/standup-config.json
```

```json
{ "standupEndTime": "10:30" }
```

`standupEndTime` is a 24-hour `HH:MM` time of day, interpreted in **the machine's
local timezone** — i.e. the user's own time wherever they're running from. There
is no separate timezone setting: the local clock already reflects where the user
is, and the computation below reads the real local UTC offset (DST included), so
nothing is hardcoded. The skill ships read-only inside the plugin cache, so this
user-writable file is where the setting lives. It is global (not per-repo).

### Changing the standup-end time

1. Ask the user: **"What time does your standup end? (24-hour, e.g. `10:30`)"**
2. Normalize their answer to `HH:MM` (accept things like "10:30am", "10.30",
   "quarter past ten" and convert). If it isn't a sensible time of day, say so
   and ask again.
3. Write it to the config file (substitute the user's time for `10:30`):

   ```bash
   mkdir -p ~/.claude
   printf '{\n  "standupEndTime": "10:30"\n}\n' > ~/.claude/standup-config.json
   ```

   (PowerShell equivalent: `@{ standupEndTime = "10:30" } | ConvertTo-Json | Set-Content (Join-Path $HOME ".claude/standup-config.json") -Encoding utf8`.)
4. Confirm: "Standup-end time set to `HH:MM`." Then stop — only continue to a
   summary if the user explicitly asks.

## Produce the summary

### Step 0 — Ensure the standup-end time is set (first run)

Read `~/.claude/standup-config.json`.

- If the file is **missing** or has no `standupEndTime`, this is the user's
  first run: walk them through [Changing the standup-end time](#changing-the-standup-end-time)
  to capture and save it, then continue with the value you just saved.
- Otherwise, use the saved `standupEndTime` as the cutoff time of day below.

### Step 1 — Compute the window cutoff

The window starts at the configured `standupEndTime` on the **previous workday**
(Mon–Fri). "Previous workday" depends on today's weekday:

| Today      | Previous workday | Days back |
|------------|------------------|-----------|
| Monday     | Friday           | 3         |
| Tue–Fri    | yesterday        | 1         |
| Saturday   | Friday           | 1         |
| Sunday     | Friday           | 2         |

Compute the cutoff as an ISO timestamp in **local time** — no timezone override,
so both the weekday and the cutoff use the machine's own zone, and `%z` emits its
real UTC offset (DST included):

```bash
t=$(sed -n 's/.*"standupEndTime"[^"]*"\([^"]*\)".*/\1/p' ~/.claude/standup-config.json)
case $(date +%u) in 1) back=3 ;; 7) back=2 ;; 6) back=1 ;; *) back=1 ;; esac
date -d "today -${back} days ${t}" +%Y-%m-%dT%H:%M:%S%z
```

(GNU `date`; on macOS use coreutils `gdate` or adapt with `date -v`. PowerShell
equivalent: `$h,$m = (Get-Content ... | ConvertFrom-Json).standupEndTime.Split(':'); $now = Get-Date; switch ($now.DayOfWeek) { 'Monday' {$back=3} 'Sunday' {$back=2} 'Saturday' {$back=1} default {$back=1} }; $now.Date.AddDays(-$back).AddHours([int]$h).AddMinutes([int]$m).ToString("yyyy-MM-ddTHH:mm:sszzz")`.)

Use the printed value as `<cutoff>` below.

### Step 2 — Gather the raw activity

This is a team skill, so attribute work to **whoever is running it** — never a
hardcoded name. Resolve the current author from git:

```bash
me=$(git config user.name); [ -z "$me" ] && me=$(git config user.email)
```

(`git log --author` matches against the email too, so the fallback works when
`user.name` is unset.)

Commits authored by that user across all branches since the cutoff:

```bash
git log --all --author="$me" --since="<cutoff>" \
  --pretty="%h%x09%ad%x09%s" --date=format-local:"%a %H:%M"
```

Also pull PRs the user opened or merged in the window (the `gh`-authed account
is the same person):

```bash
gh pr list --author "@me" --state all --limit 100 \
  --json number,title,state,mergedAt,updatedAt,url
```

Keep only PRs whose `mergedAt`/`updatedAt` falls at or after the cutoff.

Finally, capture **what's currently in progress** — uncommitted work and the
active branch — so the summary reflects what they're working on right now, not
just what's finished:

```bash
git branch --show-current          # the branch they're actively on
git status --short                 # staged + unstaged changes in the working tree
git stash list                     # anything parked
```

If `git status --short` shows changes, summarize them by area/intent (read a
quick `git diff --stat` if the paths alone aren't telling) — these are
in-flight, not done. Ignore generated/tooling noise like
`routeTree.gen.ts`, editor dirs (`.vscode/`, `.claude/`), and `docs/plans/`.
For stashes, only mention ones that look like genuine current work — skip
`lint-staged automatic backup` entries and stale stashes tied to other
branches.

### Step 3 — Clean and group

Before writing bullets, **filter noise and dedupe**:

- **Drop** merge commits (`Merge ...`), stash artifacts (`WIP on ...`,
  `index on ...`), and pure version-bump/`Publish ...` commits unless that
  publish *is* the noteworthy deliverable.
- **Dedupe** paired commits: a feature commit on a branch and its later
  squash-merge `(#1234)` are the *same* accomplishment — report it once,
  preferring the merged/`(#PR)` version.
- **Group** related commits into one accomplishment (e.g. several
  `feat(chat): …feedback…` commits → one "feedback form" bullet). The user
  wants outcomes, not a raw commit log.

### Step 4 — Write the summary

Output GitHub-flavored markdown the user can paste/read aloud, in two sections:

**`**Done — since <Day> <HH:MM> (<YYYY-MM-DD>)**`** (header with the real cutoff —
the configured time and the previous-workday date you computed)

Under this header, **group the work into related themed sections** rather than
one flat list. Each section is a short bold title (the theme) followed by its
bullets — for example a "Feedback flow" group, a "Forms UI" group, an
"Infrastructure / API" group. Derive the groupings from the actual work in the
window; don't force a fixed set of headings.

- Order sections **most important / most active first**, and bullets within each
  section **most recent first**.
- Each bullet = one shipped outcome, written as a **terse fragment** the user can
  scan in a glance — lead with the outcome, drop filler ("Added", "Implemented a
  new", "Made it so that"), and aim for roughly one line. Not a full sentence and
  not the raw commit subject. **Do not include PR or issue numbers** (no
  `(#1182)`, no `(#1202)`) — the standup is for speaking to outcomes, not
  referencing tickets.

  Example — tighten this:
  > Added a new feedback form to the chat app that lets users rate responses and
  > leave comments, and wired it up to the backend (#1182)

  down to this:
  > Chat feedback form — ratings + comments, wired to backend

**Formatting (do not skip):**

- Every bullet **must start with a real markdown bullet marker** (`- `). Never
  emit a bullet as a bare paragraph — if it doesn't begin with `- `, it's wrong.
- Put a **blank line between each bullet** (in every section) so the list renders
  with spacing rather than as a tight block.
- Separate sections with **extra vertical space**: leave a blank line after the
  last bullet, then a `---` horizontal rule, then a blank line before the next
  section's bold title. Sections should read as clearly distinct blocks, not run
  together.

**`**Currently working on**`**
- The active branch and any uncommitted / unmerged in-flight work from Step 2,
  described by intent so they can speak to what's still open. Omit this heading
  only if there is genuinely nothing in progress (clean tree, no open branch
  work).

Keep it tight — aim for what fits on screen during a standup, not an exhaustive
changelog.

## Common mistakes

- **Listing every commit verbatim.** Standup wants accomplishments; collapse
  related commits and skip merges/WIP/publishes.
- **Writing full sentences.** Bullets are scan-fodder, not prose — lead with the
  outcome, cut filler verbs, keep each to ~one line.
- **Wrong cutoff on Monday.** Monday's previous workday is **Friday** (3 days
  back), not Sunday.
- **Counting a feature commit and its squash-merge as two items.** They're one.
- **Overriding the timezone.** Don't force `TZ=` or hardcode an offset — compute
  in local time and let `%z` report the machine's real offset, so it stays
  correct as the user travels or across DST.
- **Hardcoding the author.** Always resolve the current user via
  `git config user.name` / `@me` — this skill is shared across the team.
