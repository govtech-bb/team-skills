# Audit and prioritisation

Use this reference when comparing several existing service entry or start journeys, or when the user explicitly asks for a scored audit.

Do not use scoring as a substitute for evidence, user research, accessibility review or professional judgement.

## Audit unit

Audit the user journey, not an isolated screenshot.

Review the public entry or start content and, where available, the route to the transaction. Record when an unseen component prevents a reliable score.

## Scoring

Score each criterion from 0 to 3:

- 0: no material issue
- 1: minor issue
- 2: medium issue
- 3: major issue

Give one short evidence-based reason for every non-zero score.

Do not award a zero when the evidence required to judge the criterion is missing. Mark it `Not assessed` and state what is needed.

## Criteria

### C1: What the service lets users do

Can users quickly understand the purpose and expected outcome?

### C2: How the service works

Is it clear whether the route is online, in person, paper, phone, email or hybrid?

### C3: Important deadlines

Are applicable deadlines, grace periods and timing rules visible before they affect the decision to continue?

Score 0 when a reliable source confirms that no deadline applies. Use `Not assessed` when this is unknown.

### C4: Who the service is for

Can users decide whether the service applies to them without beginning the transaction?

### C5: Key information visible early

Can users find the most consequential information within the first 1 or 2 mobile screens?

Judge content order and density, not a fixed word count.

### C6: Clear next step

Is the primary action specific, visible and consistent with what happens next?

### C7: Duplicate entry step

Does the journey make users pass through 2 start-style actions before reaching the form or intended transaction?

Do not count a necessary routing decision as duplication.

## Priority bands

Add assessed scores only:

- 0 to 6: Low
- 7 to 13: Medium
- 14 to 21: High

Apply overrides:

- C6 scored 3: High candidate
- C7 scored 3: at least Medium
- C2 scored 3: at least Medium

When any criterion is `Not assessed`, label the total provisional and do not compare it directly with complete audits without showing the gap.

## Trigger rules

Raise a service for review regardless of its total when evidence shows:

- users cannot identify the service or next action
- the route sends users to the wrong place
- eligibility, fee, deadline or channel information conflicts across the journey
- the page exposes internal or personal information
- a serious accessibility barrier prevents use
- the service appears unavailable or the transaction link is broken

Describe the trigger. Do not invent a numerical penalty.

## Prioritisation

Priority reflects user and service risk, not stakeholder seniority or how easy the edit appears.

Use the scores, overrides and triggers first. Then consider:

- severity of harm or failure
- number of affected journeys or groups
- time sensitivity
- dependency on policy, MDA or technical work
- effort only when sequencing work within similar risk

Current analytics may order work within the same priority band. Do not use historical or unverified traffic figures as standards, and do not let low traffic excuse a serious failure.

## Output

For each service show:

| Field | Required content |
|---|---|
| Service | Public service name |
| Evidence reviewed | Pages or journey components actually seen |
| C1 to C7 | Score or `Not assessed`, with concise reason |
| Total | Score out of assessed maximum, marked provisional when incomplete |
| Override or trigger | Applied rule and evidence |
| Priority | Low, Medium or High |
| Recommended action | Most useful next change or investigation |
| Owner or dependency | Who must resolve it |

After the service-level results, provide:

1. recommended work order
2. reasons for that order
3. evidence gaps
4. work that can begin now

## Audit boundaries

An audit request does not automatically authorise a rewrite.

When asked only to audit:

- report findings and recommendations
- do not replace the content

When asked to audit and improve:

- audit first
- use the score to identify risks, not to dictate the page model
- then load the relevant drafting references

Do not describe a scored page as ready to publish.
