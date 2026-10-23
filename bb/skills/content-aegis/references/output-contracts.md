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

Use a short line when possible:

`Service page → Form → Check answers → Agree and submit → Confirmation`

Use a list when the journey has branches.

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

### Formal Alpha service review deliverable

For a full Alpha service content review that includes a start page and form, produce **three parts** in this order. When creating a native Google Doc for the review, prefer three titled tabs (Review, Start page, Form) when the document tooling supports them. Otherwise use clearly labelled parts or three named files; the medium does not change the content requirements.

1. **Review**: a brief, evidence-led summary of the material findings and recommended direction; relevant expected impacts (not invented measured benefits); a concise list of outstanding MDA/service-owner questions, if any; and short content-relevant developer notes where necessary. State the baseline and material limits. Do not reproduce the full draft, narrate routine edits or fill empty sections.
2. **Start page**: complete proposed public copy, using literal Markdown headings, links/actions and only necessary, clearly distinguished internal notes. Apply the relevant page model and service-family pattern without unnecessary headings.
3. **Form**: complete proposed form content in literal Markdown, with field labels, options, hints, required/optional status, content-relevant conditions, repeatables and relevant Check your answers, declaration, submission and connected confirmation/email content when in scope and evidenced. Separate developer instructions from words the public sees.

Use only applicable parts when a service does not have both a start page and a form. A one-field GitHub request, short content-only assessment or isolated page review does **not** trigger a three-part package.

The Review is a content decision record, not a developer implementation comparison. **Do not generate an implementation log, a source-to-final change table or standalone build instructions by default.** Development compares the agreed Markdown with what was implemented and reports material departures before another Content review. See the developer implementation parity handoff below.

Keep MDA questions proportionate and prioritised. Raise only material unresolved service-owner decisions that survive the [evidence-and-escalation](evidence-and-escalation.md#sense-check-mda-and-service-owner-questions) checks. An empty MDA list is valid. Where several related information requirements genuinely need confirmation, combine them into one clear question when this does not conceal distinct decisions. Do not pass content styling, heading choices or technical implementation problems to the MDA.

For expected impact, use conditional wording such as “should improve”, “intended to reduce” or “likely to help” unless results are actually measured. A readability estimate is not proof of user comprehension, accessibility or service completion. Do not invent a reading-age value.

When the user explicitly requests a historical source-to-proposal change register for audit or migration, provide it **as an exceptional separate artefact**, not as the routine Review part. Record only observed baseline changes supported by evidence or expressly accepted decisions. Do not include `Keep`, `Retain`, `No change`, rejected wording, unsupported proposals or assistant-created draft differences. Do not confuse such a register with Development's post-handover departure list.

### Developer implementation parity handoff

The developer departure list compares *the agreed Markdown* with *what was built*. It is not the formal Content Review part, a source-to-proposal audit or a new content-design approval. Never merge these baselines or claim a developer departure was an approved content change.

For a service returned after content handover:

1. Confirm the agreed/reviewed Markdown version and the implementation environment/version being compared. If the reference is uncertain, identify and resolve that before asserting parity.
2. The implementing developer/team compares the start page, form, routes, conditional questions, errors, Check your answers, declaration, confirmation and email **where available and in scope**, against the agreed Markdown. Record not-inspected components rather than claiming parity.
3. The developer/team supplies a short list of material differences **before** requesting further content review. For each, give the exact page/field or step; agreed wording/behaviour; implemented wording/behaviour; reason; evidence or constraint where applicable; and whether it needs a decision. Screenshots or staging links may support verification but do not replace the difference description.
4. Classify each departure as a known development/technical constraint; an evidenced MDA requirement or concern; another explained proposal; or unexplained. Mark whether it is confirmed, proposed or unresolved. An MDA concern is not assumed to be an instruction from the MDA unless actually documented.
5. Aim to retain the agreed content and user-centred intent when accommodating a valid constraint. If the constraint changes the service meaning, obligations, accessibility, eligibility, required evidence, routing or user commitment, ask the appropriate decision owner and involve content design for the affected solution.
6. The content designer assesses flagged material departures and their dependent journey effects, not the complete service by default. Routine unchanged content is not re-reviewed. If there is no departure, a brief parity confirmation suffices, subject to declared test limits.
7. Where material changes lack a reason or mapping to the agreed Markdown, request the list and reconciliation first rather than automatically arranging a meeting or carrying out a fresh end-to-end editorial review. A focused meeting is useful only when concrete issues remain and its proposed topics have been provided beforehand.

Suggested developer handoff table (only material rows):

| Location | Agreed Markdown | Implemented version | Reason/evidence | Decision needed / owner |
|---|---|---|---|---|

A technical necessity is a reason for a discussion, **not** blanket approval to change settled user-facing wording. Likewise, content standards do not automatically override a confirmed legal or operational requirement: resolve the affected design using evidence and the appropriate owners. Do not invent MDA confirmation, developer constraints, or executed parity tests.

### Exceptional source-to-proposal change-register traceability

Only use this section when a source-to-proposal change register was expressly requested. The formal Alpha Review, Start page and Form deliverable does not include it. Each permitted change-register row should be auditable as:

**Observed baseline → specific problem → exact correction**

The `Existing wording / behaviour` field must describe what is actually in the active baseline. Preserve exact baseline words when quoting them; do not silently tidy a quotation.

The `Finding` or `Change needed` field must identify the concrete problem. Avoid vague reasons such as `make clearer`, `organise more logically` or `align with the pattern` unless the specific source problem is also stated.

The exact change field must contain an accepted or evidence-supported correction. Do not falsely attribute a Supported correction to operator approval. Do not put unresolved conditions such as `if required`, `if the MDA agrees` or `confirm before implementation` in the register. Keep those in unresolved questions, dependencies or review notes.

Use one coherent, independently implementable correction per row. Split changes when wording, taxonomy, validation, field order, branching, navigation behaviour or transaction-state behaviour can be implemented and tested independently.

A single screen may therefore produce several valid rows. Do not bundle them merely because they share a page.

When such a separate register is requested, cross-check the final proposed content and the source-to-proposal register:

- each included change is an accepted or evidence-supported difference from the active source baseline
- discretionary unaccepted proposals remain separately labelled and are not presented as final implementable content
- every register correction appears in the proposed content or behaviour
- no rejected, superseded or unresolved design is presented as an accepted action
- no taxonomy or structured-value change is described as a simple wording edit

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

[Sequence or branches]

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
```

Check submission status, reference number, payment, next steps and user action internally for parity.

If they are aligned, say so briefly rather than listing every unchanged item.

If they are not aligned, add a `## Parity` section containing only the material difference, risk or unresolved question.

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
