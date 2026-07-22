# Service-page patterns

Use this reference only after selecting the service-page model.

Patterns are starting structures. Include a section only when the source supports it and it helps the user.

Do not let a pattern determine the page model.

## Contents

- Drafting format and opening
- Heading library
- CTA rules
- Combined application and certificate patterns
- Separate entry and start
- Routing, offline, preparation and guidance patterns
- Hybrid services, contact and developer notes
- Pattern QA

## Shared drafting format

Use literal Markdown:

```markdown
# Page title

Short opening sentence.

## Section heading

Content.
```

Developer notes use:

`[Dev note: ...]`

Do not include decorative symbols or emojis in public copy.

## Opening sentence

Usually state what the user can do:

`Use this service to [complete the task].`

Use another form when more natural:

- Find out how to [task].
- Use this page to understand [topic].
- Contact [office] about [specific purpose].

Do not overload the opening with:

- rationale
- history
- legal explanation
- examples
- detailed eligibility
- process steps

Add a second sentence only when it provides an essential qualifier.

## Heading library

### What this service lets you do

Use on:

- entry pages
- routing pages
- unclear or multi-service entry points

Do not use when the title and opening sentence already make the task obvious.

### Who this service is for

Use on:

- entry pages
- routing pages

Job: help users recognise whether they are in the right place.

### Who can apply

Use on:

- start pages
- combined entry/start pages
- application guidance

Job: state short, confirmed eligibility.

Do not use both “Who this service is for” and “Who can apply” on one page unless they answer clearly different questions.

Use routing when eligibility depends on several answers.

### How this service works

Use when:

- the service is hybrid
- the service is partly offline
- several stages need a short overview
- more than one organisation is involved

Job: explain the route at a high level.

Do not duplicate “What happens after you apply”.

### Before you start

Use for:

- route blockers
- important conditions
- save-and-return limitations
- attendance requirements
- short warnings
- critical timing

Do not use as a general container for everything before the form.

### What you need before you start

Use for:

- information
- documents
- reference numbers
- details from someone else
- practical preparation

Keep the list short.

Link to a what-you-need page when detail is substantial.

If “Before you start” and “What you need before you start” overlap, combine or remove one.

### What the form will ask for

Use when a high-level preview reduces surprise or helps preparation.

Use nouns or short descriptions, not every question.

Do not repeat the full preparation list.

### Cost

Use to state:

- the fee
- several fee conditions
- that there is no fee, only when confirmed and useful

Never guess.

### Payment

Use only when users need to know:

- how to pay
- when to pay
- where to pay
- what payment method is accepted

Do not use when there is no fee.

Keep Cost and Payment separate when mechanics matter.

### How long it takes

Clarify whether this means:

- time to complete the form
- processing time
- time until an outcome

Use only confirmed or properly estimated information.

Do not imply a guarantee.

### Important dates or deadlines

Use when timing affects:

- eligibility
- fees
- access
- the user’s next action

Place critical timing near the top.

### What happens next

Use when the user is not submitting an application on this page.

Job: explain the next stage or destination.

### What happens after you apply

Use when the user submits an application.

State:

- who reviews it
- any action the user must take
- payment or attendance
- how the user receives an outcome

Include only confirmed information.

Do not use both “What happens next” and “What happens after you apply” for the same process.

### If you need help

Use when a confirmed support route exists.

State what the support route can help with.

### If you cannot use the online service

Use when an online service has a confirmed assisted or alternative route.

Do not promise another route when none is confirmed.

### Other ways to access this service

Use for valid:

- in-person
- telephone
- post
- email
- paper

routes.

Do not create a competing start point.

### Start the service

Use near the bottom of a start or combined page when repeating the primary action helps after a substantial amount of content.

Do not use for an offline instruction.

### Get help

Use near the end of guidance or offline content.

## CTA rules

### Application, registration and request

Use the term that matches the confirmed service decision:

- use `application` when information is assessed and the person may be approved, refused or shortlisted
- use `registration` when the person is signing up or enrolling and no approval decision is made
- use `request` when the person asks for information, an appointment, a document or an action

Do not choose a term from the source title alone. Check what happens after submission.

When a process includes both registration and selection, state the distinction clearly. Receiving a registration does not mean the person has been selected.

If the outcome is unclear, ask the service owner before using approval, acceptance, enrolment or selection wording.

### Calculators and estimates

This skill may design or review:

- content around a calculator
- questions and answer labels
- explanations of what an estimate means
- routing before and after a result
- warnings and next actions

It must not approve a formula, statutory rate, rounding rule, legal entitlement rule or calculated outcome unless the responsible policy, legal and technical owners have confirmed those rules.

Label an estimate as an estimate. Explain material limits without using a disclaimer to hide uncertainty in the calculation.

Refer formula and entitlement rules to the policy or legal owner. Refer implementation accuracy to the technical owner.

Use buttons only for the primary action.

Use links for navigation between content pages.

### Transaction

Default:

`Start now`

Use when the action begins a form or clear digital flow.

Use a more specific action when appropriate:

- Book an appointment
- Sign in
- Pay online
- Check eligibility

### Navigation

Use descriptive links:

- Continue to the application
- Check what documents you need
- Find the correct office
- Read the guidance

Avoid making navigation look like the final commitment.

### Offline or external action

Use:

- Download the form
- Contact the department
- Call to make an appointment
- Find out where to go

Do not use “Start now” when no digital service starts.

### Repeated action

The same primary action may appear near the top and bottom of one page when:

- the page length justifies it
- both actions go to the same destination
- both have the same accessible name

Place a critical warning before the first action when the user must know it before proceeding.

## Pattern A: Simple combined application page

```markdown
# Apply for [service]

Use this service to [task].

[Primary action, after any critical blocker]

## Who can apply

## What you need before you start

## Cost

## How long it takes

## What happens after you apply

## If you need help or cannot use the online service

## Start the service

[Primary action]
```

Use when:

- one main route
- simple eligibility
- short preparation
- no substantial supporting guidance

Remove unsupported or unnecessary sections.

## Pattern B: Simple combined certificate page

```markdown
# Get a [certificate]

Use this service to request [confirmed certificate description].

## Before you start

[Primary action where appropriate]

## What the form will ask for

## Cost

## Payment

## How long it takes

## If you need help or cannot use the online service

## Start the service

[Primary action when useful]
```

Use for related certificate services when:

- parity helps users
- the route is genuinely comparable
- the source supports each section

Do not preserve parity by:

- adding irrelevant headings
- hiding service-specific exclusions
- using the wrong CTA
- implying online completion where later attendance is required

“Certified copy” may be retained when it is the correct official term. Explain it if the distinction matters.

## Pattern C: Separate entry and start

Entry:

```markdown
# [Service title]

[Short recognition and routing content.]

## What this service lets you do

## Who this service is for

## How this service works

[Descriptive navigation link]
```

Start:

```markdown
# [Transaction title]

[Short task sentence.]

[Primary action after critical blockers]

## Before you start

## What you need before you start

## Cost

## Payment

## How long it takes

## What happens after you apply

## If you need help or cannot use the online service

## Start the service

[Primary action when useful]
```

Do not repeat full explanations across both pages.

## Pattern D: Routing page

```markdown
# Find the right [service, route or office]

Answer [a short description] to find out what to do next.

[Routing questions or route choices]

## Before you continue

[Only information needed for a safe routing decision.]
```

Do not use “Start now” unless the next action begins the routing flow.

Do not describe a routing result as approval.

## Pattern E: Offline or external service

```markdown
# [Task title]

[What the user can do and how the service is accessed.]

## Who this service is for

## What you need

## Cost

## Where to go or how to continue

## What happens next

## Get help
```

Use task-specific instructions instead of a transaction CTA.

## Pattern F: What-you-need page

```markdown
# What you need to [complete task]

## Documents you need

## Information you need

## Information you may need from someone else

## If you do not have everything
```

Keep the start-page preview short and link here.

Do not duplicate this full content on start.

## Pattern G: Guidance page

```markdown
# [Task-based guidance title]

[Short explanation of what the guidance helps with.]

## [User-question heading]

## [User-question heading]

## Get help
```

Use headings shaped by user tasks, not a fixed generic sequence.

Do not add “When to use this guidance” when the title and opening already make that clear.

## Pattern H: Hybrid service

Make clear:

- what happens online
- what happens in person
- when the user must attend
- what they must bring
- whether submitting online completes the task

Use:

- “How this service works” for the whole route
- “Before you start” for blockers
- guidance for detailed attendance or document rules

Do not allow “Apply online” to imply the service is fully online.

## Contact format

Use only confirmed details:

```markdown
Contact [office] about [purpose].

[Department or office]
[Address]

Telephone: [number]
Email: [email]
Opening hours: [hours]
```

Remove unused contact methods.

Do not include a response time unless confirmed.

## Page-specific developer notes

Use only when implementation affects meaning:

`[Dev note: Both Start now buttons must go to the same form route and use the same accessible name.]`

`[Dev note: Use a descriptive navigation link here, not a second primary start button.]`

`[Dev note: Keep this deadline visible without expanding an accordion.]`

Do not prescribe ARIA text when the visible label can be made clear.

## Pattern QA

Before returning:

- the model was selected before the pattern
- every heading has useful supported content
- no heading duplicates another
- the opening states the task
- critical information appears early
- cost, payment and time are distinct when needed
- entry and start do not duplicate each other
- the CTA matches the action
- guidance links appear where users need them
- contact information has a purpose
- the page does not imply a channel or outcome not supported by the source
