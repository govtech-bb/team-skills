# Service-page patterns

Use this reference only after selecting the service-page model.

Patterns are starting structures. Include a section only when the source supports it and it helps the user.

Do not let a pattern determine the page model.

## Contents

- Drafting format and opening
- Heading library
- CTA rules
- Conditional heading flow, cost states and combined application/certificate patterns
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

Use `Before you start` for short mixed preparation, prerequisites and conditions that help users begin correctly. Include information or documents they must find, obtain or arrange. Do not recount routine form fields people can answer without preparation.

### What you will need

Use `What you will need` when practical preparation is substantial enough to need its own section. `What you need` is an accepted existing variant. Do not generate `What you need before you start` as the default heading.

Keep `Before you start` and a preparation section separate only when each has a distinct job. Otherwise combine or remove the duplication. Do not put `You will need:` immediately under `What you will need` merely to repeat it.

Separate genuinely optional preparation from mandatory items without making optional information look required. Link to a dedicated preparation page when detail would obscure the start action.

### What the form will ask for

Use when a high-level preview reduces surprise or helps preparation.

Use nouns or short descriptions, not every question.

Do not repeat the full preparation list.

### Cost

Include a `Cost` section on a transactional start page whether there is a charge or no charge. Confirm what the cost fact covers: application, whole mandatory service, per-item fee or a later stage.

When the whole mandatory service has no cost, use exactly:

`There is no cost for this service.`

When only applying has no cost, use exactly, including in review logs and replacement copy:

`There is no cost to apply.`

Then explain any confirmed later mandatory or conditional charges. Do not broaden an application-only fact to the whole service or narrow a whole-service fact to applying. Do not substitute `free` or invent a fee to complete the section.

For a charge, state the confirmed amount, currency, unit, conditions and relevant payment stage. Do not import another service’s rate or discount. Use `BDS $[amount]` consistently unless an applicable standard requires another format.

If cost is unknown, keep an internal confirmation note or unresolved section in a marked draft. Do not omit the uncertainty and do not publish a guessed cost claim. Cost is not a compulsory section in unrelated guidance, directories or office profiles.

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

For annual programmes and seasonal services, distinguish ordinary year-to-year maintenance from a content-design defect. Check that published current-year deadlines and dates are accurate; do not invent new dates when the next programme cycle is unconfirmed.

Use when timing affects:

- eligibility
- fees
- access
- the user’s next action

Place critical timing near the top.

### What happens next

Use `What happens next` in the supported certificate/service-request start-page pattern and for submission outcomes. It describes the next stage from the current point in the journey.

### What happens after you apply

Use `What happens after you apply` in the application-family start-page pattern. State confirmed review, payment, attendance, decision and communication steps. Do not put both headings over the same process.

Keep accepted service-family variants when they describe the same job clearly. Do not force a universal label or order simply because another service uses it.

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

## Heading flow and conditional sections

Use the progression Recognise → Decide → Prepare → Act → Expect → Get help as a design principle, not six compulsory headings.

Fold short audience or scope facts into the opening when natural. Use a separate eligibility section when users need it to decide. Useful opening bullets are allowed; avoid repeating the title without adding scope or purpose.

Application-family order commonly uses preparation, Cost, How to apply, then What happens after you apply. The accepted certificate-family structure puts How to apply before Cost, then What happens next. Preserve a supported service-specific sequence; these are defaults, not policy rules.

Move a critical eligibility, fee, deadline or channel condition before the action it affects. Do not hide important costs below an action when users need them to decide.

Use `How to apply`, `Apply online` and `Apply using a paper form` when those routes exist. For one online route, avoid redundant parent/subheadings. Place a supported form-time estimate near the online action; do not confuse it with processing time or invent one. Link the actual paper form and explain its supported return route.

Use `Get help` or an accepted service-specific help heading only where a confirmed useful support route exists. Omit unsupported help sections and invented contacts.

## Pattern A: Simple combined application page

```markdown
# Apply for [service]

Use this service to [task and useful scope].

[Primary action after any critical blocker]

## Who can apply

## Before you start

## Cost

## How to apply

### Apply online

[Supported completion-time sentence and Start now action]

### Apply using a paper form

[Supported download/collection and return instructions]

## What happens after you apply

## Get help
```

Use for one main application task with short preparation. Include eligibility only when needed. For online-only services, simplify the route headings and omit the paper route. Omit empty optional modules. Retain a marked cost dependency when cost is unknown. Use `What you will need` instead of or separately from `Before you start` only where the preparation job warrants it. A repeated primary action near the bottom is conditional on page length and user need.

## Pattern B: Combined certificate request page

```markdown
# Get a copy of a [certificate]

Use this service to [confirmed task and scope].

## Before you start

## How to apply

### Apply online

[Supported completion-time sentence and Start now action]

### Apply using a paper form

[Supported route]

## If you need it overseas

[Only a confirmed exception for this service]

## Cost

## What happens next
```

Use this structure only where the service facts and channels fit. Do not import an overseas exception, payment method, discount, processing time or attendance requirement from another certificate. Surface decision-critical fees or route restrictions before the affected action. `Certified copy` may remain where it is the accurate official term. Do not add an extra entry/start page that merely duplicates this job.

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

## What you will need

## Cost

## Payment

## How long it takes

## What happens after you apply

## If you need help or cannot use the online service

## Start the service

[Primary action when useful]
```

Do not repeat full explanations across both pages. Include both preparation headings only when they serve distinct jobs; otherwise use one. Omit other optional modules that do not apply.

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
