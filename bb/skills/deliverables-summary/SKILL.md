---
name: deliverables-summary
description: Build a plain-language summary of everything the user delivered during one invoice period (from their invoice day in one month to the day before it in the next), drawn from git commits and PRs and the user's Google Calendar, plus what the user adds, then add it as a new tab in their running Claude Doc work log so HR or a manager can see the work behind an invoice. Use this whenever the user asks for a deliverables summary, an invoice summary, monthly work summary, timesheet narrative, "what did I do this month", a record of work for HR or payroll, or wants to update their work log, even if they don't say "invoice". Also use it to change their saved invoice day, doc or sources ("change my invoice date"). Not for daily standups (use /bb:standup) or weeknotes. Use when the user invokes /bb:deliverables-summary.
---

# Deliverables summary

The reader is HR, a manager or finance, not an engineer. They need to understand what was delivered in the period and why it mattered, so they can match it to an invoice. The user also keeps every period's summary as a permanent record. That's why output goes into **one running Claude Doc with a tab per period**: each tab can be exported on its own for an invoice, and together they form the history.

Much of the user's work never reaches a repo: workshops, stakeholder meetings, reviews, design discussions and help given to colleagues. A summary built only from git undersells the period, so this skill reads code and calendar activity and then asks the user what's still missing.

The skill does not read Slack or other chat tools, even if a connector is available. A chat connector needs wide access, and those conversations are often sensitive. Work that only shows up in chat comes from the user in step 4.

## What it needs

- **Python 3**, for the bundled scripts (standard library only), and **`gh`** signed in with access to the user's GitHub organisation.
- **The Claude Docs connector**, for the work log. If its tools aren't available, say so and offer to write the period's summary as a Markdown file instead.
- **The Google Calendar connector**, for meetings, connected through `/mcp` with calendar access granted. Without it, the skill reads a calendar export instead (see step 2).

## Configuration

Settings live in `~/.claude/deliverables-summary-config.json`, which is global and owned by the user:

```json
{
  "invoiceDay": 23,
  "docUrl": "https://claude.ai/artifact/…",
  "githubOrgs": ["govtech-bb"],
  "repoRoots": ["~/Documents/Projects"],
  "calendarEmail": "first.last@govtech.bb",
  "calendarSource": "connector",
  "name": "First Last",
  "role": "Frontend Developer, GovTech Barbados",
  "preferences": {}
}
```

- `invoiceDay` (1–31) is the day a period starts. Day 23 means 23 Sep – 22 Oct. A day that a short month doesn't have becomes that month's last day.
- `docUrl` is the running work-log doc, a Claude Doc. Leave it out until the first summary creates it.
- `githubOrgs` is where the skill looks for the user's work: every repo in these GitHub organisations, whether or not it's cloned locally. It also keeps personal and side-project repos out of an HR document. Someone who doesn't work in code (a designer, a delivery manager) can leave it empty, and the code source is skipped.
- `repoRoots` is optional. Local folders only add work that hasn't reached GitHub yet (unpushed commits).
- `calendarEmail` is the address the user's invites go to. It's how the skill finds their RSVP, so declined meetings are dropped.
- `calendarSource` is `connector` (the default: read the calendar through the Google Calendar connector). The fallbacks, for when the connector isn't available, are a folder where calendar exports land (usually `~/Downloads`) or the calendar's secret iCal URL. Treat that URL like a password: never print it or put it in the doc.
- `name` goes in each tab's heading. `role` is optional and only used if the user asks for it somewhere.
- `preferences` holds answers the user has already given, so step 4 doesn't ask the same thing every month. When the user answers one of these in step 4, offer to save it here. Until they've answered, use the cautious default in brackets:
  - `countUnansweredInvites` (ask): if true, count unanswered invites as attended instead of asking. Many people never reply to recurring team meetings.
  - `noteLeave` (false): if false, never mention leave or time off, including as the reason for a handover. Leave is personal, so it only goes in when the user says so.
  - `quietStretches` (ask): how to describe weeks with no code activity, e.g. "design work in Figma and workshops". Put it as one line under Meetings and collaboration, with the dates.
  - `nameColleagues` (false): if false, say "a teammate" or "a designer" instead of names. Other people didn't choose to appear in this person's HR record.

### First run, or "change my invoice date"

If the file is missing or has no `invoiceDay`, ask for these before doing anything else. On a "change" request, ask only for what they want to change, save it, confirm, and stop.

1. **Invoice day:** "What day of the month does your invoice period start? (e.g. 23)". Accept "the 23rd" or "23". Reject anything outside 1–31.
2. **Work-log doc:** do they already have a work-log Claude Doc (ask for the link), or should one be created on the first summary?
3. **Calendar:** their work email. If the Google Calendar connector is connected, save `connector`. If it isn't, ask whether they can connect it (`/mcp`); otherwise they can export the calendar each time (saved as `~/Downloads`) or give a secret iCal address (see "Meetings" below).
4. **GitHub organisation:** which organisation(s) their work lives in, e.g. `govtech-bb`. For anyone who writes code this is the main source, so ask for it; someone who doesn't can skip it. Optionally, the local folders that hold their clones, to catch work not yet pushed.
5. **Name** for the heading, and optionally their role. The git `user.name` and the logged-in email are reasonable defaults to offer.

Write the file with whatever tool fits, then show the user what was saved.

## Step 1: Pick the period

```bash
python3 <skill>/scripts/period.py --day <invoiceDay>
```

It prints `latest_complete`, the most recent period whose last day is today or earlier, and `current`, the period that's still open. Choose:

- By default, use `latest_complete`. People usually run this on or just after invoice day.
- If the user asks for "so far", "this month to date" or "the current period", use `current`, and mark the tab as in progress.
- For a named period ("the one ending 22 Sep", "August's invoice"), run with `--ending YYYY-MM-DD` using that period's last day.
- For several periods at once ("every month since I started"), see [Back-filling several periods](#back-filling-several-periods).

Always state the period you chose in one line before gathering ("Summarising 23 Sep – 22 Oct 2026."), so a wrong guess gets caught early.

## Step 2: Gather from every source

Run the sources in parallel where you can. If a source isn't available, carry on with the others and tell the user what's missing and how to fix it. **Never** quietly produce a summary with a hole in it, because an undercounted invoice period costs the user.

### Code: git and GitHub

Skip this when `githubOrgs` is empty.

```bash
python3 <skill>/scripts/git_activity.py --since <start_date> --until <end_exclusive_date> --org <each githubOrg> [--root <each repoRoot>]
```

GitHub is the source of truth: the script searches every repo in the organisations, not just the ones cloned on this machine, because people move between repos and delete old clones. It returns merged PRs, PRs still open, PRs the user reviewed for teammates, and the user's commits on each repo's main branch. With `--root`, it also returns `unpushed_commits`: work committed locally that GitHub doesn't have yet. Treat that as in progress. Merges and stash noise are already dropped. A commit and the PR that squash-merged it are the same piece of work, so count it once. So is the same commit appearing in a second repo: organisations often hold mirrors, forks or proof-of-concept copies of a repo (e.g. `case-management-trunk-poc`), so match on the commit subject and PR number. Reviews of teammates' work are real deliverables, so keep them.

### Meetings: Google Calendar

**Through the connector (the default).** Use the Google Calendar connector's `list_events` on the primary calendar:
- `startTime` = `<start_date>T00:00:00` and `endTime` = `<end_exclusive_date>T00:00:00`, with no offset; the server applies the user's time zone
- `orderBy` = `startTime`, `pageSize` = 250, `eventType` = `["DEFAULT", "OUT_OF_OFFICE", "FOCUS_TIME"]`
- follow `nextPageToken` until it runs out

Recurring meetings come back already expanded, one event per occurrence, with moves and skips applied. A month is about 100 events of verbose JSON, so gather it in a subagent if you can, and have it return only the summary below. That keeps the raw event list out of the main conversation.

Read each event like this:
- **The user's RSVP** is the attendee with `self: true`: `accepted`, `tentative`, `needsAction` (unanswered) or `declined`. An event with no attendees that the user organised is their own block (lunch, focus time).
- **Drop** events that are `cancelled`, events the user `declined`, and events marked free (`transparency: transparent` or `availability: AVAILABILITY_FREE`).
- **All-day events** have `start.date` instead of `start.dateTime`. Keep them apart, along with `OUT_OF_OFFICE` events, for the leave check below.
- **Recurring:** an event with `recurringEventId` is one occurrence of a series. Group occurrences by title, because Google splits a series into new ids each time it's edited.
- **Purpose** comes from the `summary`, the `description` (strip the HTML and the video-call joining text), the attendee domains and the `location`.

This gives the same summary the export script produces: meeting count and hours, recurring series with counts, one-off meetings, and all-day events.

**Read only. Never open attachments.** The connector can also create, change, delete and respond to events. This skill never does any of that. Events often carry meeting recordings and AI meeting notes as attachments. Don't open them: they hold what people said in the meeting, which is the same kind of sensitive content the user kept Slack out for. The title, description and attendee list are enough to say what a meeting was for.

**If the connector isn't available** (not connected, or an "Insufficient scope" error, which means calendar access wasn't granted when the user signed in): tell the user how to fix it ("run `/mcp`, choose claude.ai Google Calendar, reconnect, and tick the calendar permission"). Then fall back to the export below rather than leaving meetings out.

**Fallback: a calendar export.** If `calendarSource` is a URL, use it directly. If it's a folder (or `connector`, in which case look in `~/Downloads`), use the newest `*.ics` or `*.ical.zip` file in it. Google names exports after the email address, e.g. `first.last@govtech.bb.ical.zip`. If there isn't one, or the newest is older than the period's last day, ask the user to export a fresh one and wait:

> In Google Calendar on the web: ⚙ Settings → **Import & export** → **Export**. It downloads a .zip to your Downloads folder. Tell me when it's there.

An export is a snapshot. Meetings added or moved after it was downloaded are missing or wrong, which is why the connector is preferred.

```bash
python3 <skill>/scripts/calendar_events.py --source <file or URL> --since <start_date> --until <end_exclusive_date> --me <calendarEmail>
```

The script expands recurring meetings, applies skipped and moved occurrences, and drops cancelled events, events the user declined and events marked free. It returns the same summary as above: meeting count and hours, recurring series with counts, one-off meetings (title, time, length, attendee domains, short description) and all-day events.

Then:

- Drop anything that isn't work, and recompute the hours without it. That means placeholder blocks the user made for themselves ("Lunch", "Focus time", "Hold", "Commute": usually no other attendees, often recurring), personal bookings (tickets, travel, weekend plans), and team socials such as a team lunch out.
- An invite the user never answered (`needsAction` / `NEEDS-ACTION`) doesn't prove they went, especially a large one-off session. Unless `preferences.countUnansweredInvites` is true, list the bigger unanswered ones in step 4 and ask which they actually attended, rather than assuming. Either way, ask what they presented or ran: the calendar can't show that.
- Check the all-day events for leave, sick days, public holidays or training days. Don't put them in the summary, but mention any that look like time off in step 4 so the user can decide whether the invoice should note them.
- Recurring series become one line each with a count ("Daily stand-ups ×21"). They show steady participation, but listing them one by one buries the meetings that matter.
- Pick out the one-off meetings that carry outcomes: workshops, user research sessions, show-and-tells, stakeholder or MDA meetings, demos, onboarding or training given, and interviews. Use the title, description and attendee domains to work out the purpose. For example, a `*.gov.bb` domain other than the user's own points to a meeting with a ministry or department.
- Keep the approximate total hours in meetings. HR often finds this useful.

## Step 3: Turn activity into deliverables

The raw material is commits, events and messages. The output is **deliverables**: things that now exist or happened because of the user's work. Group everything into a small number of workstreams (usually 3–6), named by product or programme rather than repo name. Use "Case management system", not `case-management`.

For each deliverable, write one plain sentence about what changed for users, the team or the organisation. Leave out implementation detail, ticket numbers and jargon. Spell out acronyms once.

> Commit trail: `fix(a11y): sortable header aria-sort`, `test: e2e sort`, `docs: sortable header`
> Deliverable: Made the case list's sortable columns work properly with screen readers, so staff using assistive technology can sort cases. ([#299](https://github.com/govtech-bb/case-management/pull/299))

**Link each bullet to the pull requests behind it.** End the sentence with the PR numbers as links in brackets: `([#299](url))`, or `([#16](url), [#24](url))` when several PRs make one deliverable. The reader then gets the claim and its proof in one place, and a bare number stays out of the way of the sentence. Do the same for reviews (the teammate's PR) and for in-progress work with an open PR. A deliverable from a meeting or from what the user told you has no link, and needs none.

Work committed straight to the main branch has no pull request to link. When most of a workstream is like that, put one plain line under its heading saying so, with the dates ("Most of this work went straight to the main branch between 28 May and 9 Jun, so only some bullets link to a pull request."), so the missing links don't read as missing proof.

**Account for every merged PR.** Each one backs a bullet, or is deliberately left out. Small fixes can share a bullet with related work, but a PR that matches no bullet is a gap in the summary or a sign it isn't worth listing, and only the user knows which. Collect these orphans for step 4 rather than dropping them silently.

Fold meetings into the workstream they belong to. A workshop about the case system goes under the case system, not in a separate meetings pile. Only meetings that serve no single workstream go in the collaboration section.

## Step 4: Ask what's missing

Show the user a short draft in the terminal: the workstreams and their deliverable bullets, plus the meeting highlights. Then ask:

"Is anything missing? Things that often aren't in code or the calendar:
- help or answers you gave teammates or other departments
- decisions you drove or unblocked in discussions
- coordination with partners or MDAs
- research, planning, training given, or work in other tools (design work in Figma, workshops, documents)
Is anything here that shouldn't be shared with HR?"

If any merged PRs back no bullet, list them by plain-language title with their links, and ask for each: add it as a bullet (or fold it into an existing one), or leave it out.

Add what they mention, remove what they flag, and only then write to the doc. This step exists because the sources can't see everything, and the user is the only one who can fill the gaps.

## Step 5: Write the tab

The work log is a **Claude Doc**: one running doc with a tab per period, and each tab exports on its own to PDF or Word.

**Load the `docs` skill before your first docs call, then follow what the docs connector says to read.** At minimum that's its index topic, plus the tabs topic, because this step adds and orders tabs. The connector owns the exact call shapes, so take them from there, not from memory.

**The doc's shape:**

| Tab | Order key | Holds |
|---|---|---|
| Overview | `a0` | One line on what the log is, then a table with one row per period, newest first: period (a link chip to its tab), main focus in one line, and meeting hours. |
| One per period, e.g. `23 Sep – 22 Oct 2026` | `b` + (99999999 − the start date as YYYYMMDD), e.g. `b79739076` for 2026-09-23 | That period's summary, laid out as below. |

The order key sorts newer periods first without renumbering older tabs. Every tab needs an explicit order, because unordered tabs land in no useful position.

**Cases:**
- **No `docUrl` yet:** create the doc titled "<name> - Deliverables Summary" (its Overview tab's heading too) with the Overview tab and this period's tab at birth. Open it for the user, then save its link to the config file.
- **`docUrl` exists:** read the doc's tab list. Add the period's tab with its order key, and add a row to the Overview table.
- **The period already has a tab** (a re-run): ask whether to replace its contents. If yes, replace the contents of that same tab and update its Overview row. Never add a second tab for a period, and never delete and recreate one.
- Add "(in progress)" to the tab name when it's the current period. Rename the tab when the period is summarised again after it closes.

Fill the period tab one section at a time with pending blocks, as the docs connector describes. The user is usually watching it fill.

### Period tab layout

Use this layout every time, so tabs are consistent across months and HR knows where to look:

```
# <name> - Deliverables Summary - <period label>
<as-of date chip> · <the user, as a mention chip>

<Lead: 2–3 sentences on the period's main focus and its most significant outcomes. Don't open with the person's name or role: the heading already names them.>

## Deliverables
### <Workstream name>
- Deliverable, in one plain sentence. ([#123](PR url), [#124](PR url))
### <Next workstream>
- …

## Meetings and collaboration
- Key meetings, workshops and sessions run or contributed to, and what came of them.
- Recurring commitments, collapsed (e.g. "Daily stand-ups ×21, fortnightly sprint planning ×2").
- About <N> hours in meetings across the period.

## Support and reviews
- Reviews of teammates' work (linked to the PR reviewed), help given across teams, and onboarding or knowledge-sharing.

## In progress at period end
- Work started but not finished, so the next period's summary picks it up. Link the open PR where there is one.
```

Leave out any section with nothing in it, except Deliverables. There is no separate list of links at the end: each link sits on the bullet it backs, so a links-only section would only repeat the deliverables.

### Exporting for an invoice

When the user asks to export a period, use the docs connector's export on **that period's tab only**, as PDF or Word (docx), whichever they say. Save the file where they ask, defaulting to `~/Downloads/<name> - Deliverables Summary - <period label>.<ext>`. The PR links stay in the export, because they're the evidence behind each claim.

## Back-filling several periods

When the user wants a run of past periods, such as every month since they started:

1. **Find where the history starts.** Look for the earliest work in each source: the earliest PR in `githubOrgs`, the earliest commit, and the earliest event in the calendar export. Ask the user for their start date if the first period would only be partly covered. Tell them which months have no calendar data, because the export may not reach back that far.
2. **Gather and draft each period separately**, in parallel. Use one subagent per period if you can. Each one runs both scripts for its window, follows steps 2 and 3, and returns a draft in the period tab layout, plus its own questions: large unanswered invites, possible leave, and gaps such as weeks with no activity. Drafting period by period keeps work from one month leaking into another.
3. **Run step 4 once for the whole run**, not once per period. Show a short outline of every period (main focus plus 3–5 headline deliverables), then the questions grouped by period. Asking seven separate times wears the user out.
4. **Write one tab per period** with its own order key, plus one Overview row each. Thinly covered months still get a tab. Say what's thin in the lead ("Calendar records start in April, so meetings for this period aren't listed"), rather than padding.

## Step 6: Finish

Read the tab back and check that it matches what you meant to write. Then reply with one line: the doc as a link, the tab's name, and the sources used.

**Always end with the doc's link** (`docUrl`, written out in full), on every run, not only when a tab is written. That includes runs that only edit tabs, stop to ask a question, change settings, or end early because a source isn't available. The user goes straight from the reply to the doc, so a reply without the link sends them looking for it. Offer the PDF or Word export. Name any source that was unavailable, so the user knows the summary may be incomplete there.

## Common mistakes

- **Writing for engineers.** "Refactored the CSV parser" means nothing to HR. "Fixed a bug that stopped some applications uploading" does.
- **Counting the same work twice:** a feature commit and its squash-merge, or a meeting and the deliverable it produced.
- **A bullet without its proof, or a PR without a bullet.** Every code deliverable carries its PR links, and every merged PR is either behind a bullet or left out because the user said so.
- **Listing every meeting.** Collapse recurring ones, and only call out meetings that had an outcome.
- **Dropping reviews and support work.** For senior people, these are often a large share of the month.
- **Editing the wrong period.** Always state the period first, and replace a period's existing tab rather than adding a second one.
