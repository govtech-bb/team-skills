# Service-page patterns

Use this reference only after selecting the service-page model.

Patterns are starting structures. Include a section only when the source supports it and it helps the user.

Do not let a pattern determine the page model.

## Contents

- Drafting format and opening
- Heading library
- CTA rules
- GovBB platform page structures and route lists
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

## GovBB platform page structures

These are the house structures for Government of Barbados service pages on alpha.gov.bb.

Where a page is one of these two types, use the structure below instead of Patterns A to H in this file. Patterns A to H remain the fallback for services that fit neither.

Choose one pattern per page. Never blend them.

### The live ruleset

`apps/form_builder_api/src/ai/content-prompt.ts` in the `govtech-bb/gov-bb` repo is the single live source of truth. Its `PROMPT_BODY` is what the platform's own content generation follows, and it changes as content designers learn things.

When working in that repo, read it before writing or editing a page and follow it where it differs from this summary. Never write platform page copy from memory of the house style. Most unaided mistakes are pattern violations on a small edit.

### Combined certificate service and start page

Use for certificate services, for example birth, death and marriage certificates.

```markdown
## Before you start
## What the form will ask for
## Cost
## Payment
## How long it takes
## If you need help or cannot use the online service
## Start the service
```

- Keep the sequence aligned across related certificate services unless the source makes a section irrelevant.
- Do not introduce extra headings such as "Apply online" or "Apply with a paper form".
- Service-specific exclusions, paper fallback, overseas restrictions and contact details sit inside the standard headings above.
- "Certified copy" may be kept where the source supports it and parity across the certificate services helps users.

### Licence and application start page

Use for licence applications and other application services, for example an embalmer licence, a funeral director licence or a business registration.

```markdown
## Who is this licence for
## Before you start
## When to apply
## Complete the form
## Cost
## What happens after you apply
## Contact
```

Omit any section the source does not support.

**Who is this licence for.** Use this heading for a licence. For an application that is not a licence, use "Who can apply". One or two sentences on who needs the licence or who may apply.

**Before you start.** Lead with a "You must:" bulleted list of restrictions and eligibility conditions where the source has any, then a "You will need:" bulleted list of the mandatory documents and information. Where a requirement applies to one case only, open the bullet with that case, for example "New licences: a site plan of the pool". Close the section with a link to the governing regulation where the source provides one, for example "Read the [Health Services (Swimming Pools) Regulations, 1970](url) for the full legal requirements." Do not add a separate "What the form will ask for" heading in this pattern. The "You will need" list does that job.

**When to apply.** Cover new applications, renewals, and any deadline or expiry date. Use `###` sub-headings only where there is genuinely more than one case to separate, for example "Renewing your licence".

**Complete the form.** Fixed wording. Do not write the service task into it and do not use a "How to ..." heading. The section carries the service's routes and the page's only start link. Follow the route list rules below. How long the online form takes to fill in goes inside the online route's list item, not under a heading of its own. This pattern has no "How long does it take?" section.

**Cost.** State the fee from the source. This section sits after "Complete the form", not before it. Where the service charges a fee, this section also carries the payment method, for example a debit or credit card, or an EZPay+ account. This pattern has no separate "Payment" heading. Where the service is genuinely free both to apply for and to receive, the preferred wording is "There is neither a cost to apply, nor to receive your licence." Do not state that a service is free unless the source says so.

**What happens after you apply.** A bulleted list of what happens next: which department handles the application, that they may make contact for more information, any inspection, and how an approved licence is delivered or collected. Close the section with a plain sentence outside the list saying that submitting an application does not mean the licence has been granted. Processing time after submission belongs here, not under "Complete the form".

**Contact.** Contact details at the end of the page, one line per office. Use the contact format later in this reference.

### Route list rules for "Complete the form"

Where the service has more than one route, introduce them with a short lead-in paragraph and write each route as a numbered list item. Each item opens with a bold title naming the route, with its detail indented underneath.

```markdown
There are 2 ways to apply for a swimming pool licence. You can:

1. **Apply for a licence online**

   Allow about 5-10 minutes to complete the form.

   <a data-start-link>Start now</a>

2. **Get a paper application from the polyclinic**

   You must complete it by hand and submit the application to the polyclinic
   associated with the district where the pool is located.
```

Style rules:

- Bold the route title, write it in sentence case, and end it without a full stop. These titles are the only bold text on the page.
- Keep each title short and start it with a verb, for example "Apply for a licence online", "Get a paper application from the polyclinic".
- Indent the description, the completion time and the start link under their route so they belong to that list item.
- The line saying how long the online form takes to fill in sits inside the online route's item, above the start link. Give a figure only where the source supports it.

The next four rules are mechanical, not stylistic. The site rewrites this section for a visitor who cannot use the online route: it removes the online method and counts the remaining routes down.

- Write the count as a plain digit or a plain word, "There are 2 ways to" or "There are two ways to". Never write it as "two (2)". The count rewrite does not recognise that form, so the page would claim more routes than it shows.
- The online route must be a single list item holding its title, its completion time and the start link, because the site removes that whole list item. A start link outside a list item leaves an orphaned title or description behind.
- Keep the lead-in on its own paragraph and keep it plain text. Links, bold and other inline formatting inside it are lost when the count is rewritten.
- Where the online route is the only route, do not write a route list or a count at all. Put the completion-time line and the start link on their own lines under the "Complete the form" heading.

Some existing pages write the route titles as `###` sub-headings inside the list items. New pages use bold.

### Hand-built pages

Where a Government of Barbados service page is hand-built rather than authored as markdown in `apps/landing`, keep the same section order and the same numbered route list.

The rewrite does not run on a hand-built page, so the four mechanical rules protect nothing there. Keep the shape anyway: the page then reads consistently with the rest of the platform and ports cleanly if it moves onto the landing pipeline. Use an ordered list, put the route title in bold, and keep the completion time and the start button inside the online route's list item.

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
