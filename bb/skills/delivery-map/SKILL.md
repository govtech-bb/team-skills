---
name: delivery-map
description: Build a "Super Delivery Manager" page for one service — a shareable artifact that shows where a GitHub-tracked service sits in the delivery pipeline (the form intake process), read from its GitHub issue and Slack. It derives each step's status, dates, time-in-stage against an SLA, blockers, owners and evidence links, and gives a copy-ready status update. Use when the user gives an issue number or link and wants to see or share where a service is on its way to going live. Use when the user invokes /bb:delivery-map.
---

# Super Delivery Manager (delivery-map)

Build a **Super Delivery Manager** page for one service: a self-contained, shareable
artifact that shows where that service sits in the delivery pipeline, read from its
GitHub issue (and Slack, where the user has it). It is styled to match
**alpha.gov.bb** and written in plain English so anyone can pick it up and read it.

You are the delivery manager's tool here. Do the pulling, mapping and building for
them. Do not ask them to gather data you can gather yourself.

## What it produces

A single HTML artifact for **one service** with:

- a **console** — the issue reference, service title, target, a progress meter, and a
  derived **Now / Waiting on / Next**;
- **time on GitHub** and **active work** durations;
- a **"Blocking go-live"** band listing what the service is waiting on, with "since"
  dates and links;
- the full **pipeline** as a timeline: each step shows status (done / in progress /
  to do), date, owner, an **evidence link** to the comment or sub-issue that proves
  it, and — for active and blocked steps — **time-in-stage against an SLA** and a
  **"Next move"** (whose court the ball is in);
- a **"Last synced"** stamp and a **"Copy update"** button that emits a plain-text
  Now / Waiting on / Next for a weeknote or Slack post.

It is a **synced snapshot, not a live page.** Published artifacts have no network
capability and cannot call the GitHub API, and delivery repos are usually private, so
the page cannot fetch itself. You pull the data, stamp when you pulled it, and
re-syncing means running this skill again.

## Routing

The user's arguments are: **$ARGUMENTS**

- Resolve the **service** from the arguments: accept a bare issue number (`249`), a
  `#249`, or a full issue URL. If several are given, the first is the service; treat
  any others as candidate dependencies (see Step 3).
- Resolve the **repo**: from a full URL if given, else the current repo
  (`gh repo view --json nameWithOwner -q .nameWithOwner`). If neither resolves, ask
  which repo.
- If no issue is given at all, ask for the issue number or link, then stop.

## Step 1 — Pull the service data from GitHub

Use the `gh` account that can read the issue's repo. If a `gh` call returns `404`,
the account lacks access — tell the user which account is active
(`gh api user -q .login`) and ask them to switch, rather than guessing.

```bash
REPO="<owner/repo>"; N="<issue number>"
# issue meta + every comment (author, timestamp, body, permalink)
gh issue view "$N" --repo "$REPO" \
  --json number,title,createdAt,updatedAt,state,url,labels,comments
# sub-issues (state + dates are strong step signals)
gh api graphql -H "GraphQL-Features: sub_issues" -f query='
  query($owner:String!,$repo:String!,$n:Int!){
    repository(owner:$owner,name:$repo){ issue(number:$n){
      subIssues(first:100){ totalCount nodes{ number title state url createdAt closedAt } } } } }' \
  -F owner="${REPO%/*}" -F repo="${REPO#*/}" -F n="$N"
```

Read the comment bodies. They are the real record of what happened — prototype
links, review docs, meeting notes, MDA/department decisions, sprint plans. Keep each
comment's **permalink** (the `url` field) — it becomes a step's evidence link.

## Step 2 — Pull Slack signals (optional)

If the user points at Slack (a channel, a thread, or "check Slack"), read it for
updates that have not reached GitHub — a sign-off given verbally, a blocker, a date.
Fold those into the mapping in Step 3. If the user does not mention Slack, skip it;
do not block on it.

## Step 3 — Map the data onto the pipeline

Read [references/pipeline.md](references/pipeline.md). It defines the canonical
steps (phases, names, the "why", typical owner and a suggested SLA) and how to read
GitHub/Slack signals into each step's **status, date, evidence, owner, blocker and
aging**. Work through it and produce, for this service:

- each step's **status** (`done` / `current` / `pending`), **date**, **owner**, and an
  **evidence** `{label, url}` where a real comment or sub-issue proves it;
- the **dependencies** blocking go-live (open gate sub-issues, a paired form, a named
  approver), each with a `since` date and a link;
- **SYNCED_AT** = today's date.

Keep the pipeline steps and phases from `pipeline.md` unless the service genuinely
differs; the value is a consistent shape across services.

## Step 4 — Fill the template

Copy [assets/template.html](assets/template.html) to a working file. Replace **only
the DATA block** at the top of its `<script>` — `SYNCED_AT`, `SERVICE`,
`DEPENDENCIES` and `STAGES` — with the values from Step 3. Do not touch the render
engine or the styles below the DATA block; everything (meter, aging, blockers,
console, copy button) computes from the data.

The template ships with a fully worked example (issue #249) so you can see the exact
shape each object takes. Match that shape.

## Step 5 — Publish

Verify it renders in light and dark, then publish it with the **Artifact** tool.
Give a new service its own artifact; when **re-syncing** a service you built before,
republish to the **same** artifact (pass its URL) so the link is stable. Favicon: 🛰️.

Do **not** declare any `capabilities` — the page must stay freely shareable, and
declaring `mcp` would block sharing.

## Writing style

Write every user-facing string in **GDS content-design plain English**: short
sentences, active voice, lead with the key fact, address the reader as "you" where it
fits. **No em dashes** — use full stops, commas or colons. Spell acronyms out on
first use: *case management system* (not CaMS), *Permanent Secretary* (not PS), *end
to end* (not E2E), and name the department rather than "MDA" where you can.

## Re-syncing

To refresh a service, run this skill again for the same issue: re-pull (Step 1),
re-map (Step 3), update the DATA block and `SYNCED_AT`, and republish to the same
artifact URL. The aging, blockers and status recompute from the new data.

## Common mistakes

- **Editing the markup instead of the data.** All 24 steps render from the `STAGES`
  array. Change the data, never the `<li>` generation.
- **Asserting a step is done with no proof.** A `done` step should carry an evidence
  link to the comment or sub-issue that shows it. If there is no evidence, say so in
  the gist rather than inventing a date.
- **Promising a live page.** It is a synced snapshot. Stamp `SYNCED_AT` honestly and
  tell the user re-syncing means re-running the skill.
- **Em dashes and jargon.** Plain English, acronyms spelled out, no `—`.
- **Declaring `mcp` or other capabilities.** Keep the page shareable; declare nothing.
- **Guessing repo access.** If `gh` returns 404, surface the active account and ask
  the user to switch — do not fabricate data.
