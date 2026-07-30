---
name: product-shape
description: Turn a project brief or a signed-off prototype — a GitHub issue, Claude artifact or other online page — into an MVP-first delivery document: who it's for, the problem, hypotheses, what the platform can already express versus what needs building, scope, success metric and phased features. Use it when a standalone HTML prototype has to be converted into the platform codebase. Use when the user invokes /bb:product-shape.
---

# product-shape

Turn a project brief that lives on the web into a written, MVP-first delivery document.

The document exists to **de-risk**. Its bias is toward getting something testable in front of real users
fast, not toward completeness of plan. A brief describes what someone hopes to build; your job is to find
the smallest thing that would prove them right or wrong, and to say what order the rest comes in.

The most common case is a **prototype that has to become a real service**: a standalone page of HTML, CSS
and JavaScript, built to be shown and signed off, which now has to be rebuilt inside the platform
codebase — its structure, its primitives, its dependencies, its deploy path. The demo already proves the
design. What nobody has written down is how much of it the platform can already express, what needs new
platform capability, and what that means for sequencing. That is the gap this document fills, and step 3
is where it gets filled.

The shape is **discussion first, document second** — the same rhythm as `/bb:dev-plan`. Don't draft until
you've read everything, named the gaps, and asked about the ones that change scope.

If the line below has content after the colon, treat it as the source. Otherwise ask for one.

Source: $ARGUMENTS

## 1. Read the source

- **No source given** → ask for one. Don't proceed without.
- **GitHub issue or PR** → read the body *and the comments*:

  ```bash
  gh issue view <number> --repo <owner>/<repo> --json title,body,comments,labels
  ```

  Comments are load-bearing. Reviewer sign-offs, corrections and scope changes land there, and the body
  is often stale by comparison. Read all of them, not the most recent few — a decision that reversed
  something in the body is as likely to be twenty comments back as at the end. Where a comment and the
  body conflict, the comment is usually newer; say which you followed.
- **Any other page** — a Claude artifact, a published doc — → WebFetch it.

Then follow linked material **one level deep, and only where it changes an answer**: an attached form
PDF, a parent epic. Not every cross-reference. Record what you read, and name anything you deliberately
skipped.

## 2. Evaluate the prototype

If the brief links a prototype, reading it is not optional. The prototype is the strongest available
evidence of what already works, and it will usually change the MVP more than the brief does — a brief
describes intent, a prototype describes reality.

WebFetch it. Single-page HTML prototypes hold their steps, branches and validation in client-side markup
and script, so the rendered text often shows only the first screen — fetch the raw source too and
enumerate the steps and conditional logic from it. If the flow still can't be read statically, say so and
offer to walk it in a browser. Don't guess at it.

Record, in the template's **What already exists** section:

- **What already works end to end** — the steps, and the behaviour they implement.
- **What the prototype implies but doesn't do** — a submit button that goes nowhere, a rule the brief
  describes but the page doesn't enforce, a hardcoded lookup table.
- **Where the prototype and the brief disagree.** Report the disagreement. Don't silently prefer either.
- **What is therefore genuinely left to build.** This, not the brief's ambition, is the MVP candidate.

Three things repay the effort of looking, because a prototype that demos well hides them:

- **Follow the terminal action to its end.** Find what the submit button actually does, then read the
  failure path, not the happy path. A prototype whose endpoint doesn't exist yet will often catch the
  error and fabricate success — a generated reference number, a confirmation screen — so reviewers and
  service owners come away believing a submission works that never left the browser. Say plainly when
  that's what you find.
- **Check that the payload carries what the brief promises.** Attachments are the usual casualty: files
  that appear to upload are regularly dropped or emptied on the way out.
- **Cross-check the lookup tables against each other.** Where a prototype holds two tables that have to
  agree — routing areas against office contacts, options against handlers — diff them. A key present in
  one and missing from the other is a live gap for whoever falls into it.

## 3. Assess the conversion into the platform

Do this whenever a prototype has to be rebuilt inside a codebase. It is usually the single most useful
part of the document, and the part nobody has written down.

**Fix a baseline first.** Name the target repository and the commit or date you are assessing against, and
put it in the document. Platform capability moves weekly: a primitive that exists today did not exist a
fortnight ago, and an assessment with no baseline is unreadable a month later. If the user names a date,
use that commit — `git log --until=<date>` — not the current tip, and don't let today's code tell you
something was available then.

**Then learn the platform's vocabulary before you judge the prototype.** Read the target's own building
blocks — its field and component registry, its validation and condition vocabulary, its shared packages,
the modules that handle submission, files, email and notification — and read two or three existing
examples of the thing you're converting. Follow the target's contributing guide and conventions docs. You
are looking for what the platform can already say, in its own terms.

Then sort every behaviour in the prototype into one of four buckets:

- **Already supported** — it maps onto an existing primitive, so it's recipe or configuration work. Name
  the actual primitive, not a category. "Conditional requirement" is not an answer; the name of the
  validation that does it is.
- **Not supported yet** — it needs new platform capability. Say what has to be built and which package or
  app it lands in. **Then give every one of these an MVP fallback**: the degraded version expressible with
  primitives that exist today. A map picker falls back to a parish dropdown; a collapsible grouped selector
  falls back to plain checkbox groups; a dependent dropdown falls back to free text; a rule the validation
  DSL can't express falls back to being enforced operationally. This is the most valuable column in the
  document — it is what lets the first phase ship the *whole* journey on fallbacks and be tested end to end,
  instead of stalling until the custom work lands. If a behaviour genuinely has no fallback, say so; that is
  a real finding and it changes the sequencing.
- **Data and assets to move** — anything embedded in the prototype that has to live somewhere else.
  Prototypes routinely inline datasets that belong on the server; say where each one goes.
- **Dropped in translation** — what the platform version deliberately won't do, and why. Silence here
  reads as an oversight later.

Two failure modes to avoid:

- **Don't report prototype defects that the platform makes irrelevant.** A stub endpoint, a fabricated
  reference number, a file that never uploads — if the platform supplies submission, references and
  uploads, these are artefacts of the prototype being a prototype, not work. Say so once and move on;
  listing them as defects sends the team hunting bugs that cannot survive the port.
- **Don't assume a primitive exists because it obviously should.** Check. The gap between "the platform
  surely handles dates" and the specific validation that enforces a statutory notice period is where
  estimates go wrong.
- **A helper in a package is not a capability.** Finding a date function in a shared library says nothing
  about whether the form's own configuration language can reach it. Confirm the primitive is expressible in
  the artefact you will actually be writing — the recipe, the schema, the config — by finding it in use in
  an existing example. If it appears nowhere, treat it as new capability however tantalisingly close the
  building blocks look. This is the single easiest way to under-estimate a port.
- **Enumerate the input types the prototype uses against the ones the platform declares.** Times of day,
  durations, currency, coordinates and dependent dropdowns are the usual absentees, and each one is quiet
  until someone tries to build the field.

## 4. Separate what you know from what you don't

Before asking anything, say out loud what the source already answers and what it doesn't. Briefs are
routinely strong on scope and silent on customers, hypotheses and metrics.

Never ask the user for something the source already says.

## 5. Discuss

One or two questions per turn, on the gaps only. Prioritise the gaps that would change the MVP — an
unnamed success metric changes it, a missing contact address doesn't.

Then state explicitly that you could now write something useful, and **ask before drafting.**

If the user says "just write it", write it, and put every unresolved item in Assumptions.

## 6. Draft

Fill [assets/product-shape-template.md](assets/product-shape-template.md), including **The brief** at
the top — three lines on who it's for, the problem, and how it tries to solve it. Anyone opening the
document should know what the project is before reading anything else. These rules are not
negotiable — they're the reason the skill exists:

- **Every hypothesis carries a falsifying test.** "Users want this" is not a hypothesis. Write what
  result would make the team abandon it.
- **The MVP is the smallest thing that tests the riskiest assumption.** Name the riskiest assumption
  first, then cut to it. Score risk by what it would cost to be wrong, not by how hard it is to build.
- **Deferral is the default.** Anything not serving that test goes to a later phase. Deferring is not a
  demotion, and you don't need permission for it.
- **Every phase states what it proves and what would make us stop.** A phase with no stop condition is a
  wish list.
- **Every phase carries a horizon: `Now (this week)`, `Next week`, or `Later`.** Exactly one phase may be
  `Now (this week)`, and it has to be genuinely completable this week by the team that exists — measured
  against what the prototype already does, not against a clean slate. If nothing fits in a week, the MVP
  is drawn too wide. Say so and redraw it.
- **Work blocked on an external input can't be `Now`**, however small it is — a monitored inbox address,
  a data-handling sign-off, a confirmed contact list. Name the blocker and the horizon it unblocks.
- **When the obvious first phase is blocked, look for the version of it that isn't.** Usually the build
  is unblocked and only the destination is gated: the same work delivering to a test inbox, a dummy
  account or a dry run proves the mechanism this week, and flipping the destination becomes next week's
  phase once the approval lands. Never route real personal data anywhere a sign-off hasn't cleared, and
  never let that rule turn a shippable week into an idle one.
- Prefer a metric that already exists or is cheap to instrument over the theoretically ideal one.
- Distinguish the citizen from the MDA staff who process the work. They are different customers with
  different problems, and a solution for one is regularly a burden for the other.

### The logic flow diagram

One `flowchart TD` covering what will be built, with MVP paths solid and deferred branches dashed and
labelled with their phase, so the reader sees the MVP and its seams in one picture.

- Conditional branches are `{diamond}` decision nodes with labelled edges.
- Dependencies are edges. External systems — an MDA inbox, a workbook, a payment provider — are their own
  nodes.
- Deferred work uses `-.->` and a dashed `classDef`, labelled with its phase.
- One screen. If it doesn't fit on one, the MVP is too big — say that instead of shrinking the diagram.
- Don't invent branches the source doesn't support. An unknown is either a node labelled as unknown or a
  row in Assumptions.
- Keep node labels free of `(`, `)`, `{`, `}`, `"` and `#` — they break mermaid parsing. The diagram has
  to render both in the file and in a GitHub comment.

## 7. Write it out

Ask where the document should live. Default to `docs/product-shape/<issue-number>-<slug>.md`, or
`<slug>.md` when there's no issue number. Create the directory if needed.

## 8. Offer to publish

Offer — never assume — to post the document as a comment on the source issue, so the shaping lives with
the brief where the team and the service owner will find it. Only on an explicit yes:

```bash
gh issue comment <number> --repo <owner>/<repo> --body-file <path>
```

This writes to a shared, externally visible thread. If the user doesn't clearly say yes, don't post.

## 9. Hand off

End by naming the next step, once:

- Categorised as a content change or a new form → `/bb:govtech-service-content` to write the content.
- Phase 1 ready to build → `/bb:dev-plan`.

Then stop. Don't start planning the implementation in this session.

## Edge cases

- **Source is behind auth and can't be fetched.** Say so and ask the user to paste the content. Don't
  shape a brief you haven't read.
- **The brief is already an MVP plan.** Say so plainly, then stress-test it: is the riskiest assumption
  actually being tested first, and is the `Now` phase really a week's work? Shape it rather than
  rubber-stamp it.
- **One customer only.** Fine. Don't invent a second to fill the table.
- **The prototype is more complete than the brief admits.** Common, and the most valuable thing you can
  report. Say what's already done and shrink the MVP to match.
- **Everything is blocked on external inputs.** Then the `Now` phase is chasing those inputs. Say that,
  and name who is chasing what.
- **The user wants phases they can't staff.** Name the mismatch. Don't quietly stretch a horizon to make
  a plan look achievable.
