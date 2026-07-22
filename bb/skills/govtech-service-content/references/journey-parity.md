# Journey parity

Use this reference whenever two or more service components are created, changed or reviewed.

Components may include:

- entry page
- start page
- combined page
- routing
- guidance
- what-you-need page
- form
- check-your-answers
- declaration
- confirmation screen
- confirmation email
- paper, telephone or in-person route

The journey should use the same facts, terms, logic and next steps.

## Contents

- Journey and component jobs
- Facts, terms and eligibility
- Preparation, channels and routes
- Form, check-your-answers and confirmation
- Alternative routes and guidance
- Change impact and builder limitations
- Review output and QA

## Map the journey

Start with the actual sequence.

Example:

`Entry → Start → Form → Check answers → Agree and submit → Confirmation`

For branches, show:

- decision
- route
- outcome
- return or recovery path

Do not assume the published page order matches the real journey.

## Assign one job to each component

Check:

- entry recognises or routes
- start prepares and begins
- guidance explains
- what-you-need supports preparation
- form asks only what is needed
- check-your-answers supports review
- declaration records agreement
- confirmation gives the correct outcome and next step

Flag components that:

- duplicate another
- have no clear job
- introduce a new rule late
- send the user backwards unnecessarily

## Factual parity

Compare:

- service name
- purpose
- audience
- eligibility
- exclusions
- age or date rules
- fees
- payment
- deadlines
- processing time
- documents
- required information
- service channels
- locations
- contact routes
- attendance
- approval process
- next steps

Do not treat a difference as harmless until its effect is understood.

## Terminology parity

Use one preferred term for the same thing across the journey.

Check:

- apply versus register versus request
- applicant versus user versus customer
- programme and service names
- document names
- office and MDA names
- payment terms
- status terms
- identity terms

Different words may be correct when the action changes.

Confirm that submission states also match the term. A received registration is not selection, and a received application is not approval.

Do not force consistency that changes meaning.

## Eligibility parity

Check:

- who pages say may use the service
- who the form permits to continue
- date and age boundaries
- exclusions
- whether someone may act for another person
- special routes

The form must not:

- allow a clearly ineligible route without explanation
- reject someone the page says may apply
- introduce an eligibility condition not shown or supported

Use routing when answers determine the correct route.

## Preparation parity

The start page preview, what-you-need page and form must agree on:

- documents
- information
- reference numbers
- details from another person
- uploads
- payment method
- attendance

Do not list every form field on the start page.

Do not require an item in the form that the preparation content says is unnecessary.

## Channel parity

Check whether the service is:

- fully online
- partly online
- in person
- telephone
- email
- post
- external

Make clear what each channel accomplishes.

Submitting an online form must not be described as completing the whole service when later payment, attendance or document presentation is required.

## CTA and route parity

Check:

- entry navigation goes to the correct start or route
- start actions go to the correct form
- repeated actions share destination and accessible name
- guidance returns users to a useful next step
- offline links and contacts match the stated route
- users do not commit twice before reaching the form

Flag:

- circular journeys
- dead ends
- competing primary actions
- links that return users to the same information

## Form-logic parity

Compare page claims with form behaviour:

- required and optional information
- branches
- repeatable sections
- maximum selections
- validation
- upload requirements
- payment state
- exit routes

Do not assume correct wording compensates for broken form logic.

## Check-your-answers parity

The review step should:

- use the same labels as the form
- show material answers users need to verify
- allow changes before submission
- preserve grouped and repeatable information clearly
- avoid exposing internal-only derived information without need

The declaration must apply to the information the user has just reviewed.

## Confirmation parity

The confirmation screen and email must agree on:

- whether submission succeeded
- service name
- reference number
- payment status
- review status
- next steps
- user actions
- deadlines
- attendance
- expected contact

Do not include a reference number unless the system creates one.

Do not include sensitive answers in email solely to mirror the screen.

## Alternative-route parity

For paper, telephone, email or in-person routes, check:

- the route genuinely exists
- eligibility matches the online route or differences are explained
- fees and payment are accurate
- document requirements are clear
- contact information has a purpose
- next steps are not inferred from the online process

Do not describe an alternative route as equivalent when it has different outcomes or processing.

## Guidance parity

Guidance may contain detail absent from start.

It must not:

- contradict the transaction
- introduce a hidden mandatory document
- create a new eligibility rule
- describe an obsolete route
- shift a routing decision into self-diagnosis

Link guidance from the point where users need it.

## Change-impact check

When one component changes, check the others.

Examples:

- eligibility changes: entry, start, routing, form and guidance
- fee changes: start, payment, form and confirmation
- document changes: start preview, what-you-need, form and confirmation
- service name changes: all public and transactional components
- next-step changes: start, confirmation screen and email
- channel changes: entry, start, help, form and guidance

Do not approve an isolated change when it creates a known contradiction elsewhere.

## Builder limitation

When the platform cannot implement the intended journey:

1. state the intended experience
2. identify the limitation
3. recommend the safest achievable implementation
4. identify affected components
5. keep the remaining gap visible

Do not silently change the content standard to match the limitation.

## Parity review output

Use:

```markdown
## Journey reviewed

[Sequence]

## Conflicts

| Topic | Component A | Component B | Required decision |
|---|---|---|---|
| [topic] | [content or behaviour] | [content or behaviour] | [owner and action] |

## Missing links or steps

- [gap and impact]

## Recommended corrections

1. [highest-priority correction]

Status: [status]
```

Hide the conflict table when there are no conflicts.

## End-to-end QA

Confirm:

- each component has one job
- facts match
- terms match unless the action differs
- routes work
- guidance appears at the right point
- the form asks only for needed information
- the user can review before agreeing
- confirmation matches the completed route
- alternative routes are accurate
- links and actions reach the correct destination
- validation works in the real environment
- no internal information appears publicly
- no sensitive information appears unnecessarily in email
- outstanding facts and owners remain visible
