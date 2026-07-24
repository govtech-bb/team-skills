# Form QA

Use this reference after drafting or when reviewing a form or prototype.

Check content, sequence, logic, validation, accessibility and implementation together.

Do not limit QA to spelling and wording.

## Contents

- QA order and severity
- Journey, actor and data checks
- Branching, exclusivity and repeatables
- Validation and error content
- Names, contacts, dates and uploads
- Health, assets and preferences
- Check-your-answers, agreement and submission
- Prototype and implementation checks

## QA order

Review in this order:

1. service and policy accuracy
2. user journey
3. data necessity
4. branching and outcomes
5. question sequence
6. validation and recovery
7. wording and accessibility
8. confirmation parity
9. implementation

Do not polish wording before identifying a broken route.

## Severity

### Red flag

Use when an issue may:

- mislead users
- change eligibility
- create the wrong route
- collect unsupported or sensitive data
- prevent submission
- produce a legal or policy error
- exclude users
- expose private information
- create an unusable form

### Yellow flag

Use when an issue creates:

- avoidable effort
- inconsistent terminology
- unclear wording
- mobile scanning difficulty
- minor recovery problems
- non-blocking implementation friction

Do not classify personal preference as a defect.

## Journey check

For material branching, first distinguish the applicable observed, required or proposed flows and identify the materially different routes using [journey-logic-and-mapping.md](journey-logic-and-mapping.md). Do not manufacture a flow type that is not supported by the task or evidence.

Confirm:

- the form starts at the correct point
- the sequence follows the user’s task
- questions appear when users can answer them
- related questions are grouped
- later questions do not change earlier meaning
- users can move back without losing or corrupting answers
- every branch has a valid next step or safe exit
- the journey reaches review, agreement, submission and confirmation

Flag:

- repeated pages
- circular routes
- dead ends
- unnecessary screens
- important questions appearing too late

## Actor check

Confirm the form consistently distinguishes:

- person completing the form
- applicant or subject
- representative
- parent or guardian
- emergency contact
- employer or organisation
- other named people

Check pronouns and labels.

Do not allow “you” to refer to different people within one section.

## Data-necessity check

For every question, ask:

- what service decision or process uses this?
- is it required by law or policy?
- can the user reasonably provide it?
- is a less sensitive answer sufficient?
- is it already collected elsewhere?

Flag any question without a clear purpose.

Do not retain a field merely because it exists on paper.

## One-data-point check

Check that each field captures one thing.

Split questions such as:

- name and address
- job and income
- condition and treatment
- item and value
- person and relationship

Do not split a coherent description into unnatural fragments.

## Sequence check

Use this general order where relevant:

1. route or preference
2. primary subject
3. other actors
4. contact
5. service-specific details
6. sensitive information
7. uploads
8. check your answers
9. agreement
10. submit
11. confirmation

Change the order when the service logic requires it.

Ask sensitive or effortful questions only after users understand why they are needed.

## Branching check

For every branch, verify:

- the trigger answer exists
- the rule or user need behind the branch is supported or visibly unconfirmed
- the condition is unambiguous
- the question appears early enough to prevent irrelevant effort
- the answer changes something material
- all relevant users see the follow-up
- irrelevant users do not see it
- changing the trigger clears or safely preserves dependent answers
- every outcome has a next step
- the branch does not invent policy
- routes with genuinely different requirements or outcomes have not been falsely combined
- users are not separated where the distinction changes nothing
- check-your-answers and confirmation reflect the route taken

Test every materially different route, not every theoretical combination.

Test both Yes and No where they exist.

Test returning to change an earlier answer, including dependent answers, validation, review and confirmation.

## “None of these” check

For multi-select questions:

- “None of these” is exclusive
- selecting it clears other answers
- selecting another answer clears it
- follow-ups do not display when it is selected

Do not add a separate No answer to the same multi-select.

For yes-or-no questions, use Yes and No.

## “Other” check

Use “Other” only when:

- the option list is not exhaustive
- an unlisted answer is valid
- the service can process free text

When selected, show a concise textbox.

Do not use “Other” to avoid confirming a complete policy list.

## Repeatable-section check

Verify:

- multiple entries are permitted
- minimum and maximum counts are confirmed
- required fields apply within each record
- users can add, review, edit and remove records
- the repeat label names the item
- records display clearly on check-your-answers
- ranking is preserved where relevant

Do not use a repeatable section for one unstructured narrative.

## Required and optional check

Confirm:

- every required question is genuinely required
- optional questions are marked “Optional”
- conditionally required questions are required only when shown
- hidden fields do not block submission
- a source phrase such as “if applicable” has been translated into working logic

Do not mark all visible contact fields required when only one is needed.

## At-least-one check

When at least one answer is required:

- state the rule before or near the fields
- validate the group, not every individual field
- write an error that explains the recovery

Example:

`Enter at least one telephone number.`

Error:

`Enter a mobile, home or work telephone number.`

## Selection-limit check

When users may choose a limited number:

- state the maximum
- prevent or clearly recover from too many selections
- preserve ranking if order matters
- do not imply all options are required

Example:

`Select up to 3 locations.`

Error:

`Select no more than 3 locations.`

## Validation rule

Include content-relevant validation when it affects whether users can answer correctly.

Do not assume a developer can infer:

- service-specific formats
- eligibility dates
- selection limits
- cross-field requirements
- upload rules
- mutually exclusive options
- minimum records

Avoid validation that is stricter than the service need.

## Error-message pattern

An error should:

- identify the question
- state what is wrong
- tell the user how to fix it
- use the same term as the label
- avoid blame

Examples:

- Enter the applicant’s first name.
- Select whether the child takes medicine.
- Enter a date before 17 July 2026.
- Upload the health certificate.
- Select no more than 3 camp locations.

Do not use:

- Invalid input
- Error
- Incorrect
- Required field

as the complete message.

## Text validation

Allow:

- spaces
- apostrophes
- hyphens
- full stops where appropriate
- accented letters

Do not use a restrictive letters-only rule for names, schools, organisations or addresses without a confirmed need.

Do not reject harmless punctuation the service can safely process.

## Name check

Confirm:

- name fields match the service need
- first, middle and last names are ordered consistently
- middle names are optional only when permitted
- labels identify whose name is required
- validation accepts real name variation

Do not add title, maiden name or preferred name without need.

## Identification-number check

Confirm:

- the number is necessary
- the label uses the official term
- format rules are confirmed
- users without the number have an appropriate route when policy permits
- the number is not repeated unnecessarily

Do not expose the full number in confirmation email.

## Sex and gender check

Confirm:

- the service needs the data
- the label matches the intended data concept
- “Sex” has not been changed to “Gender” for stylistic reasons
- answer options are approved
- the form does not collect both concepts without need

## Telephone check

When local and international numbers are supported, test:

- `421-1234`
- `246-421-1234`
- `+1 246 421 1234`
- another valid international country code
- spaces and hyphens

Confirm:

- at least one rule works at group level
- optional fields do not trigger required errors
- extension handling is clear when needed

Do not assume every Barbados number has the same user-entered format.

## Email check

Confirm:

- email is needed
- required or optional status is clear
- obvious invalid formats are rejected
- leading or trailing spaces are handled
- the confirmation route matches the address collected

Do not require email twice by default.

## Address check

Confirm:

- the address is needed
- Barbados and international branches match the service
- Parish appears for Barbados when needed
- Country appears only when needed
- postal code is not required for places where it may not exist
- landmark or directions are not requested without operational need

## Date check

Test:

- impossible dates
- future dates
- leap years
- minimum and maximum
- exact boundary dates
- dates before a relevant event
- dates after a relevant event

When age matters:

- calculate against the correct date
- confirm inclusive boundaries
- do not use an arbitrary year such as 1903 as the only lower limit
- show a useful eligibility or error message

Do not use today when the programme start date or closing date is the actual reference.

## Money and number check

Confirm:

- currency is clear
- decimals are handled correctly
- zero and negative values are handled
- units and timeframes are present
- totals are not introduced without authority

Do not mix BDS, BBD and dollar-only formats within one service.

## Upload check

For each upload, test:

- required or optional
- accepted file types
- size limit
- single or multiple files
- clear document name
- replacement and removal
- error recovery
- mobile upload

Confirm the service has authority to collect it.

Do not use one generic upload when separate evidence must be checked independently.

Do not claim the original must be kept unless confirmed.

## Health and medicine check

Confirm:

- allergies, medicine, conditions, limitations and support needs are distinct
- No or “None of these” suppresses follow-ups
- Yes displays only relevant follow-ups
- medicine records repeat when several are permitted
- the service need justifies the detail
- sensitive answers are not repeated in email

Avoid asking for diagnosis detail when functional support information is sufficient.

## Employment and income check

Confirm:

- employment status controls work questions
- self-employment is not counted twice
- income timeframes match
- work address appears only when relevant
- unrelated programme obligations are not grouped as employment

## Assets, land and ownership check

Confirm:

- ownership alone, joint ownership, business assets and overseas assets are distinct when they change the route
- duplicate asset options are removed
- repeatables support several assets
- complex ownership reaches a safe route
- users are not asked to make an unsupported legal judgement

## Preference check

Confirm:

- choice types remain separate
- maximum selections work
- first, second and third preferences are preserved
- optional later preferences do not block submission
- “No preference” is exclusive where appropriate

## Check-your-answers check

Confirm:

- labels match the questions
- answers are grouped
- repeated records are distinguishable
- users can change answers
- optional unanswered fields are handled clearly
- sensitive data is not displayed unnecessarily
- derived or internal values are not shown as user answers

## Agreement check

Confirm:

- users review answers first
- declaration wording is approved
- agreement appears once
- checkbox is required
- full name and date are included only when needed
- service rules added to the declaration are consequential and confirmed

Do not silently replace statutory wording.

## Submission check

Confirm:

- final button describes submission
- repeated clicks do not create duplicate applications where the system can prevent them
- errors preserve answers
- successful submission has a distinct outcome
- failed submission gives a recovery route

Do not show “Application submitted” before success is confirmed.

## Confirmation check

Use [confirmation-and-email.md](confirmation-and-email.md).

Confirm screen and email parity without copying sensitive answers.

## Prototype and real-environment check

Test:

- desktop and mobile
- keyboard
- screen reader labels and order
- Back and change-answer behaviour
- conditional display
- validation
- uploads
- save and return
- links
- submission
- confirmation email

A correct specification does not prove the build is correct.

## Platform limitation

When the builder cannot implement the intended rule:

1. state the intended experience
2. identify the limitation
3. recommend the safest available implementation
4. record the remaining gap

Do not silently weaken the requirement.

Examples:

- no Back link
- unsupported exclusive checkbox behaviour
- no repeatable sections
- limited validation
- missing feedback component

## QA output

Prioritise:

1. broken journey or unsafe data
2. branching and validation
3. accessibility
4. sequence
5. wording

For each issue, state:

- where it occurs
- what is wrong
- user or service impact
- required correction

Avoid low-value nitpicks.

## Final form QA

Confirm:

- facts and policy are supported
- page and form logic agree
- only needed data is collected
- all branches work
- validation supports real users
- errors help recovery
- exclusive options behave correctly
- repeatables and limits work
- sensitive information is controlled
- check-your-answers, agreement and submission are sequenced
- confirmation reflects the submitted route
- the real build was tested or the need for testing is visible
