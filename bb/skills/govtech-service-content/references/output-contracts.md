# Output contracts

Use this reference to choose the smallest clear response format for the task.

Do not show every section for every request.

Do not make a user read process notes before reaching the answer they requested.

## Contents

- General output and sizing
- Decisions, journeys and copy-ready content
- Notes and MDA questions
- Reviews and QA
- Developer handover and form specifications
- MDA, confirmation and audit outputs
- Status and next action

## General output rules

Lead with the outcome or recommendation.

Use plain language.

Keep public copy separate from:

- risks
- MDA questions
- design notes
- developer notes
- QA findings

Use visible Markdown headings in copy-ready specifications when required.

Do not convert Markdown headings into commentary about the heading level.

Hide empty sections.

End substantial work with:

- one status
- unresolved points
- named owner type
- one useful next action

## Choose the output size

### Small task

Use for:

- one wording correction
- one heading
- one hint
- one short email or confirmation change
- one clear QA question

Return:

1. answer or recommendation
2. copy-ready wording
3. confirmation needed, if any

Add a status only if the task affects a wider service decision.

### Medium task

Use for:

- one page
- one form section
- a short review
- a set of MDA questions

Return only the relevant parts of:

1. recommendation
2. risks or missing facts
3. draft or corrections
4. next action
5. status

### Full task

Use for:

- several pages
- a complete form
- an end-to-end journey
- developer handover
- a complex MDA content set

Return:

1. content decision
2. recommended journey
3. missing or conflicting information
4. copy-ready content
5. behaviour and developer notes
6. QA result
7. status and next action

## Content decision format

Use:

```markdown
## Content decision

Recommended approach: [plain-language recommendation]

Why:
- [short reason]
- [short reason]
```

Use 1 to 3 reasons.

Do not provide several equal alternatives when one can be recommended.

For a simple task, use one sentence instead of the full block.

## Journey format

Use the smallest representation that makes the route clear.

For a simple sequence:

`Service page → Form → Check answers → Agree and submit → Confirmation`

Use a route list for a few simple branches and a decision table when conditions interact.

When status matters, label the flow as:

- Observed flow
- Required flow
- Proposed flow

A proposed flow must say whether it is a recommended correction supported by evidence or an illustrative proposal requiring confirmation.

Use Mermaid only when branches, loops, actors or existing-versus-proposed logic are materially easier to understand visually. Pair it with a written interpretation.

Do not add a diagram for a simple sequence.

## Copy-ready content

Introduce with:

`## Draft content`

Then provide the content without interleaving explanatory commentary.

Use literal Markdown headings when the user needs content for Word, a prototype, CMS or developer handover.

Example:

```markdown
# Apply for [service]

Use this service to [task].

## Before you start

[Content]
```

Do not place the full draft inside quotation marks.

## Internal-note placement

For 1 to 3 notes, place each note immediately after the affected content.

For many notes:

1. provide a readable clean draft
2. provide a separate `## Issues to confirm` section
3. reference the affected heading or question

Use:

- `[MDA note: Confirm...]`
- `[Content risk: ...]`
- `[Design note: ...]`
- `[Dev note: ...]`

Do not create new note prefixes without need.

## Questions format

Ask no more than 3 questions at one time in conversation.

For a document containing all outstanding questions, group them:

```markdown
## Needed before drafting

1. [Question]
   Why this matters: [short reason]

## Needed before factual approval

1. [Question]

## Useful but not blocking

1. [Question]
```

Hide empty groups.

Use terms from the source.

Do not ask an MDA to decide:

- content style
- page patterns
- heading structure
- accessibility standards
- GovTech terminology preferences

Ask the MDA to confirm facts and operation.

## Review output

### Red flags

Use for issues affecting:

- accuracy
- eligibility
- legal or policy meaning
- route or task completion
- data collection
- accessibility
- privacy or security
- serious implementation behaviour

### Yellow flags

Use for issues affecting:

- clarity
- consistency
- avoidable effort
- mobile scanning
- minor journey friction

### Recommended action

Give one prioritised next action.

Do not:

- list harmless preferences
- inflate issue severity
- repeat the same problem under several headings
- rewrite everything when the user asked only for an assessment

### Review-only format

```markdown
## Red flags

- [Issue, impact and required fix]

## Yellow flags

- [Issue and recommended improvement]

## Recommended action

[One prioritised action]

Status: [status]
```

Hide a flag section when there are no issues in that category.

## Page or form QA format

For concise QA:

```markdown
## What works

- [Only material strengths]

## Issues

### Red
- [Issue]

### Yellow
- [Issue]

## Recommended changes

1. [Highest priority]
2. [Next priority]
```

Do not praise routine compliance at length.

When the user asks for one issue at a time, provide only the highest-priority unresolved issue.

## Developer handover

Use for content sufficiently resolved for implementation.

```markdown
# [Service or content title]

## Content decision

[Recommended model and short reason]

## Journey

[Observed, required or proposed sequence, route list, decision table or map as needed]

## Journey logic

- [Material condition, trigger, route and outcome]
- [Change-answer or recovery behaviour]
- [Evidence status or owner where unresolved]

## Copy

[Copy-ready content with literal Markdown headings]

## Behaviour

- [Conditional display]
- [Required or optional behaviour]
- [Repeatable behaviour]
- [Validation that affects content]
- [Routing]

## Developer notes

- [Only notes developers need to implement the intended experience]

## Outstanding confirmations

- [Fact, owner and affected content]

## Known platform constraints

- Intended experience: [rule]
- Current limitation: [limitation]
- Safest implementation: [recommendation]
- Remaining gap: [risk]

Status: Ready for developer handover
```

Hide sections that genuinely do not apply, except:

- copy
- outstanding confirmations when any remain
- status

Do not hide an implementation gap to make the handover appear complete.

## Form specification field format

When the form module requires it:

```markdown
Question or field label (field type)

Hint text, if needed.

(If condition, display:)
```

Do not add technical detail to every field.

Place shared behaviour once at the relevant section level.

## Public and internal MDA outputs

When both are required, separate them with:

```markdown
[USER-FACING PAGE]

[Public copy]

[MDA-FACING PAGE]

[Internal copy]
```

These labels are review markers, not public content.

Do not create both pages automatically.

If a role-holder page is justified, use:

`[ROLE-HOLDER PAGE (USER-FACING)]`

## Confirmation screen and email output

When both are requested:

```markdown
## Confirmation screen

[Copy]

## Confirmation email

Subject: [subject]

[Copy]

## Parity check

- Submission status: aligned
- Reference number: aligned or not used
- Payment: aligned or not applicable
- Next steps: aligned
- User action: aligned
```

Do not expose sensitive form answers in the email merely to demonstrate parity.

## Audit output

For one service:

```markdown
## Audit result

Score: [0 to 21]
Priority: [Low, Medium or High]
Trigger: [trigger or None]

## Main issues

1. [Issue]

## Recommended improvement order

1. [Action]
```

For several services, use a table with:

- service
- score
- trigger
- priority
- main issue

Do not include traffic unless current traffic data is supplied and needed as a tie-breaker.

## Status presentation

Use:

`Status: [one approved status]`

When the label may be unfamiliar, add one short explanation.

Do not stack several statuses.

Choose the status that represents the immediate next stage.

Approved statuses:

- Not ready to draft
- Structure only
- Draft with confirmation notes
- Ready for content review
- Ready for factual confirmation
- Ready for developer handover

Never use:

- Ready to publish
- Approved
- MDA approved
- Legally compliant
- Accessibility compliant

unless the user supplies explicit evidence of that external decision. Even then, distinguish the evidence from the skill’s own assessment.

## Final next-action format

Use:

```markdown
## Next action

[Person or owner type] should [specific action] because [short reason].
```

Skip the heading for a small task.

Do not give several equally weighted next actions.

## Final output check

Before returning:

- the answer requested appears before process detail
- the output size matches the task
- public copy can be copied without internal commentary
- internal notes are distinct
- questions are prioritised
- developer notes are implementable
- the status matches the evidence
- the next owner and action are clear
- no empty headings remain
