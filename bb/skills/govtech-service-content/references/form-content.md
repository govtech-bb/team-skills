# Form content

Use this reference to plan, create or rewrite the content specification for an online form.

Use [form-qa.md](form-qa.md) after drafting.

Use [confirmation-and-email.md](confirmation-and-email.md) for submission outcomes.

## Contents

- Source and no-deviation rules
- Journey and actor planning
- Sections, headings and questions
- Field format, hints and optionality
- Branching and repeatables
- Names, contacts and addresses
- Dates, uploads and declarations
- Check-your-answers and specification output

## Role and output

Produce a plain-English form-content specification developers can build.

Content design may improve:

- sequence
- grouping
- labels
- hints
- progressive disclosure
- error prevention
- digital clarity

It must not silently change:

- legal meaning
- policy
- eligibility
- evidence requirements
- outcomes
- data scope

## Source and no-deviation rule

Use the approved evidence hierarchy.

The source form is evidence of the existing process, not automatically the highest authority.

Do not add, remove or reinterpret a data requirement without:

- clear support from the source hierarchy, or
- a visible question or risk for the responsible owner

Permitted digital clarification:

- separate combined questions into discrete data points
- make an implied condition explicit
- show a question only when relevant
- use a structured answer where the source clearly supplies fixed options
- explain a term
- reduce avoidable error

Not permitted without authority:

- new facts
- new eligibility decisions
- new policy outcomes
- speculative “useful” data
- broader consent
- a new declaration

## Plan the journey first

Before writing questions, identify:

1. the user’s task
2. the person completing the form
3. the subject of the application
4. any representative, parent, guardian, employer or organisation
5. decisions and branches
6. repeatable records
7. supporting evidence
8. payment
9. review and agreement
10. submission and next steps

Write a short sequence before drafting.

When answers change later questions, evidence, validation, outcomes or next steps, use [journey-logic-and-mapping.md](journey-logic-and-mapping.md) to establish the routes before writing field-level conditional display.

Example:

`Preferences → Child details → Parent or guardian → Emergency contact → Health and care → Uploads → Check answers → Agree and submit → Confirmation`

Do not make the user understand the internal actor model.

## Actor and role clarity

Use “Tell us about yourself” only when:

- one primary actor exists
- the person completing the form is the subject
- no representative or multi-role logic applies

Otherwise name the role:

- Tell us about the applicant
- Tell us about the child
- Tell us about the parent or guardian
- Tell us about the business
- Tell us about the deceased

Do not switch role terms within the journey.

## Section headings

Use short questions or “Tell us...” statements.

Headings must make sense out of context.

Useful blocks, only when relevant:

- Before you start
- Tell us about [role]
- Identification numbers
- Contact details
- Employment and income
- Assets
- Land
- Supporting documents
- Check your answers
- Your agreement
- Application submitted

Avoid:

- About
- Details
- Information
- Part A
- Section 2

Do not add a heading merely because it appears in a standard list.

## Grouping

Group related questions under descriptive headings.

Each field captures one discrete data point.

Do not merge several questions into one field to reduce screen count.

Use subheadings when they help distinguish categories within a section.

Avoid a heading that simply repeats the first field label.

## Question labels

Write labels as direct questions or concise requests.

Examples:

- What is the applicant’s date of birth?
- Email address
- Select up to 3 camp locations

A label must:

- ask for one thing
- use the user’s language
- identify the relevant person or object
- work without relying on visual position

Do not mirror the section heading unnecessarily.

## Answer types

Choose the answer type that supports the known data and decision:

- textbox
- text area
- radio buttons
- checkboxes
- dropdown menu
- date field
- file upload
- repeatable section

Use radio buttons for one answer from a short visible list.

Use checkboxes when several answers may be selected.

Use a dropdown when a long stable list is easier to navigate and users know the answer, such as parish.

Do not use free text when the service needs a known structured choice.

Do not create a fixed list when the source does not establish the options.

## Developer field format

After each field label, include the field type:

```markdown
What is the applicant’s first name? (textbox)
```

Use the approved field-type terms consistently.

Include content-relevant behaviour and validation. Do not add routine technical implementation detail.

## Hint text

Add hint text only when it:

- removes ambiguity
- prevents a likely error
- explains a non-obvious term
- clarifies a format the interface does not make clear

Keep it short and user-facing.

Do not:

- repeat the label
- carry a long policy rule
- use it to repair a vague question
- tell users to use bullets or line breaks
- add examples without a demonstrated need

## Examples

Use an example when:

- users may not recognise the expected format
- several plausible interpretations exist
- the source supports the example

Do not use real personal information.

Do not make an example look like the only valid answer.

## Required and optional questions

Mark a user-visible question `Optional` when it is genuinely not required.

Do not mark a question optional because:

- only some users see it
- it appears after a “Yes” answer
- the source says “if applicable” but it is mandatory when applicable

A conditionally displayed question may be required for users to whom it applies.

Do not use `[Dev: optional]`.

## Branching

Use:

`(If condition, display:)`

Example:

```markdown
Does the child take any medicine? (radio buttons)

- Yes
- No

(If Yes, display:)

What medicine does the child take? (repeatable section)
```

Branching should:

- use a confirmed rule or a clearly labelled structural assumption
- show only relevant questions
- make an implied condition explicit
- appear early enough to prevent avoidable work
- keep users on the correct route
- have a clear effect on content, evidence, validation, outcome or next step

It must not:

- introduce new data
- invent an outcome
- create unsupported eligibility
- hide a required safe exit
- treat current technical behaviour as authority for the service rule
- combine routes whose requirements or outcomes materially differ
- separate users when the distinction changes nothing and has no confirmed purpose

Do not assume fewer branches are always better. Use the journey-logic reference when deciding whether to move, combine, separate or remove a branch.

## Yes and no questions

Ask yes or no only when the answer controls:

- relevance
- route
- eligibility
- required follow-up

Do not add a redundant “No” question when the existing answer already establishes no.

Use positive, neutral wording.

## Exclusive options

Use “None of these” only in a multi-select list when it allows users to state that no listed answer applies.

It must be mutually exclusive.

Use “No” for a yes-or-no question.

Do not combine “None of these” with “Other” unless both are logically meaningful.

## Repeatable sections

Use a repeatable section when the service supports several distinct:

- people
- children
- beneficiaries
- executors
- properties
- assets
- jobs
- qualifications
- skills
- references
- medicines
- preferences

Each repeated record should contain only fields that belong to that record.

Set a minimum or maximum only when confirmed.

Preserve order when ranking matters.

Place the repeat action at the end of the relevant group.

Do not replace structured repeatables with one large text area when the service must process, compare, route or validate each entry.

## Multi-line fields

Use a text area for one coherent description.

Do not use it to collect several unrelated data points.

Do not ask users to create their own bullet structure when separate questions would reduce error.

## Name fields

Collect only the name information the service requires.

When a full legal name is needed, use:

- First name (textbox)
- Middle name(s) (textbox), when supported
- Last name (textbox)

Preferred hint when all middle names are required:

`Enter all middle names in order.`

Use `Optional` or “if known” only when the service permits omission.

Do not introduce a middle-name field absent from the service need.

## Identification numbers

Use the confirmed official term.

GovTech standard:

`Barbados National Identification (ID) number`

Do not use an unexplained acronym as the primary label.

Do not collect an ID number merely because another service does.

## Sex and gender

When the confirmed service requirement is sex, use:

`Sex`

Do not silently rename it “Gender”.

Sex and gender identity are different data concepts. Do not collect both unless the service has a confirmed need and approved answer options.

Use only answer options supported by the source hierarchy.

## Contact details

Explain why contact information is needed when not obvious.

Example:

`We will use these details to contact you if we need more information.`

Do not add:

- “Can we use this number?”
- a preferred-contact question
- consent language

unless the service genuinely needs the answer.

When several telephone fields are offered but only one is required, state:

`Enter at least one telephone number.`

Do not mark every number field required.

## Telephone numbers

Use labels that match the need:

- Telephone number
- Mobile number
- Home number
- Work number

Accept appropriate Barbados and international formats when the service supports overseas contact.

Allow harmless spaces and hyphens when the system can normalise them.

Do not infer an international service route from international-number support.

## Email

State when email is required for:

- confirmation
- communication
- account access

Do not collect email by default.

Do not ask users to confirm an email twice unless the error risk and interface justify it.

## Address

Collect an address only when needed.

Use fields supported by the service.

For a Barbados address, a common structure is:

- Street address line 1
- Street address line 2, Optional
- Parish

Include Country only when the service supports or needs addresses outside Barbados.

Use international branching only when supported:

```markdown
Country (dropdown menu)

(If Barbados, display:)

Parish (dropdown menu)

(If outside Barbados, display:)

State or region (textbox)
Postal code (textbox), Optional where permitted
```

Do not ask for a landmark by default.

Use directions or landmark information only where location finding is a real operational need.

## Dates

Ask for the level of precision needed:

- full date
- month and year
- year

Use a date field for a full date.

Do not add a date merely to capture when a user completed a screen if the system already records it and no legal need exists.

## Employment and income

Separate:

- employment
- self-employment
- other income

Avoid double counting.

Use the source timeframe.

Do not introduce totals, calculations or income categories absent from the service rule.

Tie work-address questions to current employment when relevant.

Do not connect unrelated programme or “give back” information to employment merely because it appears nearby on paper.

## Assets and land

Separate distinct ownership types when they change the route:

- owned alone
- owned jointly
- business ownership
- overseas ownership

Use repeatable records for several properties or assets.

Do not make users interpret legal ownership categories without explanation.

Use routing when ownership changes whether the service can continue.

## Health and care information

Separate questions about:

- allergies
- medicine
- medical conditions
- activity limitations
- support or access needs

Ask follow-ups only when relevant.

Do not collect detailed health information without a clear service need.

Do not surface sensitive answers unnecessarily in later communications.

## Preferences

When users can choose several preferences:

- state the maximum
- distinguish required and optional rankings
- preserve first, second and third order
- keep different preference dimensions separate

Do not merge location and programme type when they are independently meaningful.

## File uploads

For each upload, state:

- what document to upload
- whether it is required
- whether several files are accepted
- accepted file types and size, when confirmed
- whether the original must be kept or shown later, when confirmed

Use separate upload questions when documents are processed separately.

Do not ask for “supporting documents” without identifying what is accepted.

## Check your answers

Use:

`# Check your answers`

Intro:

`Review the information you have given before submitting.`

Show labels that match the form.

Allow users to change answers.

Show repeated records in clear groups.

Do not introduce new questions here.

## Agreement and declaration

Place the agreement after users review their answers and immediately before submission.

Use the GovTech standard only when no statutory or approved service-specific declaration applies:

```markdown
# Your agreement

Full name (textbox)

Date (date field)

I confirm that the information I have provided is true and correct to the best of my knowledge. (checkbox)
```

Do not replace legally required wording without authority.

Do not repeat the agreement elsewhere.

If the service includes rules the user must accept, include only confirmed, consequential commitments.

## Submit action

Use a button label that describes the action:

- Submit application
- Send request
- Confirm and submit

Do not use “Continue” for the final submission.

Make clear when submission creates a legal declaration or payment.

## Specification output

Use visible Markdown headings.

For each question:

```markdown
Question label (field type)

Hint text, if needed.

- Answer option
- Answer option

(If condition, display:)
```

Include:

- section order
- question order
- answer types
- required or optional status
- branching
- repeatables
- content-relevant validation
- user-facing errors where needed
- check-your-answers
- agreement
- submit action
- confirmation-screen and email requirements

Do not include routine code, database schema or component implementation.

## Digital improvement note

When a clarification question is added, include one short internal reason:

`[Design note: This question makes the source form’s implied condition explicit so users see only relevant fields.]`

Do not justify routine wording edits field by field.

## Form-content QA before specialist QA

Check:

- the journey is mapped
- actors are clear
- the form asks only for needed information
- each question captures one thing
- labels and headings do not duplicate
- hints prevent real errors
- optionality is accurate
- branches have safe outcomes
- repeatables match the service
- sensitive data has a clear purpose
- check-your-answers precedes agreement
- submission action is clear
- confirmation content is included
