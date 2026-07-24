# Journey logic and mapping

Use this reference when content work involves material branching, several user routes, several actors, or a prototype whose answers change later questions, evidence, validation, outcomes or next steps.

Do not load it for a small linear task that can be understood safely from a short sequence.

## Contents

- Purpose and scope boundary
- Observed, required and proposed flows
- Logic baseline and mapping method
- Safe branching improvements
- Proportionate route coverage
- Change dependencies
- Decision-table and map outputs

## Purpose and boundary

Use content-led journey logic to make service content coherent from entry to outcome.

This reference may help:

- understand an existing flow
- identify broken, late, missing or unnecessary branches
- recommend a simpler route within confirmed service rules
- show current and proposed logic clearly
- define the routes that need testing

It does not:

- create or approve policy, eligibility, legal or operational rules
- design a full backstage service blueprint
- invent staff processes, system architecture or technical capability
- treat an existing prototype as proof that its logic is correct

Include confirmed internal handoffs only when they affect the user-facing journey. Mark anything else as unknown rather than filling the gap.

## Distinguish the flow being shown

Use these terms consistently.

Use only the flow types supported by the task and evidence. Do not manufacture a required flow when rules are unconfirmed or a proposed flow when no redesign is needed.

### Observed flow

What the supplied or directly verified page, form, prototype or live service currently does. Record hidden or unavailable behaviour as unverified.

Observed behaviour is evidence of the current state. It is not automatically the required behaviour.

### Required flow

What confirmed service rules, evidence and approved decisions require.

Do not describe a route as required when the rule behind it is assumed, disputed or missing.

### Proposed flow

A recommended improvement to the user-facing journey.

Label it as one of:

- **Recommended correction supported by evidence**
- **Illustrative proposal requiring confirmation**

Do not merge required and proposed flows into one diagram or description when their status differs.

## Establish the logic baseline

Before improving material branching, identify:

- the user task and intended outcome
- the person completing the task
- the person, organisation, event or record each question concerns
- entry points and possible exits
- each decision or condition that changes the route
- the answers that trigger each route
- questions, guidance, evidence, validation or outcomes triggered
- where routes join or end
- how users change an earlier answer or recover
- the evidence status and owner behind each material branch condition

Do not assume a branch is necessary because it exists in a form or prototype.

If a material condition is unsupported, show it as unverified and identify who must confirm it.

## Choose the smallest useful representation

Use:

- a short sequence for a linear journey
- a route list for a small number of simple branches
- a decision table when several conditions interact
- a journey logic map when routes, actors, outcomes or dependencies are hard to follow in prose
- Mermaid when branches, loops, actors or current-versus-proposed flows materially benefit from a diagram

Do not create a diagram merely to make the work look complete.

Pair every diagram with a concise written interpretation because diagrams may not render in every Claude surface.

## What a journey logic map should show

Show only what is relevant:

- entry point
- actor and data subject
- decision points and branch conditions
- destination screens or content
- evidence, validation or upload requirements
- where routes join
- outcomes, handoffs and next steps
- change-answer and recovery routes
- unresolved or unavailable routes

A journey logic map is not a full service blueprint. Do not invent backstage activity.

## Improve branching safely

Assess whether each branch:

- has a clear purpose and changes something material
- appears early enough to prevent irrelevant effort
- shows users only questions, guidance and evidence that apply
- groups related conditions together
- reuses answers instead of asking again
- preserves valid uncommon routes without complicating the main route
- leads to a valid outcome, handoff, recovery route or next step
- remains consistent when an earlier answer changes
- produces the correct check-your-answers and confirmation content

Do not assume fewer branches are always better.

A branch may be justified when it:

- prevents irrelevant questions or uploads
- reflects a genuine difference in requirements
- leads to a different outcome or next step

Consider recommending a change when:

- branching happens too late
- a question has no effect and no confirmed purpose
- users are separated even though requirements and outcomes are the same
- different requirements have been incorrectly combined
- an answer is requested more than once
- changing an earlier answer leaves contradictory dependent data
- a route is missing, unreachable, circular or ends without a clear outcome

## Recommendations the skill may make

Within confirmed rules, the skill may recommend:

- moving a route-deciding question earlier
- removing a question that has no effect and no confirmed purpose
- combining routes whose requirements and outcomes are genuinely the same
- separating routes with materially different requirements or outcomes
- reusing an earlier answer
- grouping related conditions
- clearing or rechecking dependent answers after a changed response
- changing check-your-answers or confirmation content to match the route taken

For each material recommendation, state:

1. the logic problem
2. the likely user or service effect
3. the proposed direction
4. the routes and artifacts affected
5. what must be confirmed or tested

Do not present a recommendation as an approved service rule.

## Cover and test routes proportionately

Identify every materially different route, not every theoretical combination.

When a runnable prototype or service is available, test the routes. When only static content, a specification or screenshots are available, inspect what can be verified and state which behaviour remains untested.

Include, where relevant:

- main route
- ineligible or cannot-continue route
- exception route
- representative, parent, guardian or organisation route
- missing-information route
- change-answer route
- interrupted or recovery route
- each route producing a different evidence requirement, outcome or next step

For complex logic, use a decision table to identify distinct outcomes and high-risk combinations before testing or specifying acceptance scenarios.

Give higher priority to routes involving:

- eligibility or exclusion
- payments or fees
- evidence or uploads
- legal meaning or declarations
- sensitive personal information
- rejection, referral or irreversible outcomes

## Manage dependencies after a change

A material branch change may affect:

- entry, routing, start or guidance content
- preparation and evidence requirements
- questions and conditional content
- validation and error messages
- check-your-answers
- declarations and consent
- payment
- confirmation screens and emails
- rejection, referral and recovery routes
- public and internal routing

Identify the directly affected routes and artifacts, then run the relevant journey-parity checks.

Do not restart an unrestricted review when a focused dependency check is sufficient. Widen the review only when the change alters the wider journey.

## Decision table format

Use when conditions interact:

```markdown
| Condition or question | Answer | What appears or changes | Outcome or next step | Evidence status and owner |
|---|---|---|---|---|
| [condition] | [answer] | [content, question, evidence or validation] | [outcome] | [confirmed, assumed or unclear; owner] |
```

Hide columns that add no value for a simple task.

## Map output format

Use only the applicable sections:

```markdown
## Journey logic

### Observed flow

[Sequence, route list, decision table or Mermaid]

### Required flow

[Confirmed route only]

### Proposed flow

**Status:** Recommended correction supported by evidence | Illustrative proposal requiring confirmation

[Proposed route]

### What changes and why

- [Material difference, affected users and reason]

### Confirmation and testing needed

- [Rule, owner, route or test]
```

Do not repeat the same flow in several formats unless comparison genuinely requires it.
