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
- Names, contacts and addresses, including scoped former-name hints
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

Example:

`Preferences → Child details → Parent or guardian → Emergency contact → Health and care → Uploads → Check answers → Agree and submit → Confirmation`

Do not make the user understand the internal actor model.

## Actor and role clarity

Establish who is completing the form and who or what the service concerns before using ambiguous personal headings.

Use `Your details` for the completing person's core identity and contact record when their role is already clear.

Use `Tell us about yourself` only when the person is the substantive subject of a broader section, such as their experience, qualifications, work or relevant circumstances.

Do not use `Tell us about yourself` as a catch-all for route, permission, relationship, identity, address, contact and business information.

Otherwise name the role or subject clearly, for example:

- Tell us about the applicant
- Tell us about the child
- Tell us about the parent or guardian
- Tell us about the business
- Tell us about the deceased

Do not switch role terms within the journey.

### Applicant capacity, family relationship and eligibility

For an applicant-role question, check that `Who can apply`, the answer options, any branching and the declaration describe **the same permitted applicant roles**. Distinguish *capacity to apply* (such as parent or recognised guardian) from *family relationship* (such as grandparent). Do not create an actor question unless the role changes something material for the service.

If the confirmed service rule permits **parents or guardians only**, use `Parent` and `Guardian` for an applicant-capacity question unless a further distinction has a supported purpose. A grandparent or other relative who is a recognised guardian selects `Guardian`; being a relative alone does not establish permission to apply. Do not offer `Grandparent` or `Other` as additional eligible applicant roles without supporting service evidence. Relationship choices may legitimately be broader for a separate purpose, such as emergency contacts or people collecting a child.

If the current form offers `Grandparent` or `Other` but its eligibility or declaration says `parent or guardian`, flag the contradiction. Ask the service owner whether other applicants are permitted **only if that is genuinely unresolved**. Propose aligned wording conditionally; do not silently delete existing options, change stored values or routes, or assume an answer to the eligibility question. Ensure a permitted applicant can truthfully make the declaration.

## Reuse known answers safely

Do not automatically ask users to enter the same information again.

Reuse or offer a previously collected answer when:

- it belongs to the same person, organisation, place or record
- it has the same meaning and purpose
- it still applies on the current route
- the user can review or change it where needed

Ask again when:

- the actor, subject, property, business, event or record is different
- the new question has a different meaning
- the service requires a separate confirmation
- the answer may no longer apply
- reusing it would hide an important distinction

When an earlier answer changes, clear or recheck dependent reused information that may no longer apply.

Do not assume that an address already collected for a person or business is automatically the address of a regulated property, premises, event or place of work.

When one or more earlier addresses could be the required regulated-place address, offer the eligible, distinguishable choices plus `Another address` under a subject-specific question such as `Which address is the property at?`. If none can logically fit, ask for the address. Preserve separate person, organisation and place records; choosing the same address does not merge the actors. Recheck reuse when the originating answer changes.

## Section headings and page-group serviceability

Start with one coherent user job per page.

Use the direct question as the H1 when one substantive question can do the whole page job.

Use a grouped statement heading when several questions belong to the same actor, subject and user job.

A form heading must accurately describe the whole page, not merely the first question.

Before accepting a grouped heading, check:

- actor scope
- subject scope
- task scope
- whether the questions form a sensible review group on Check your answers

Ask:

> Would a user reasonably expect every substantive question on this page after reading only the heading?

If no, rename, regroup, move or split the content.

Do not use a grouped heading immediately followed by a question that simply restates it.

For example, avoid:

`Tell us about your relationship to the property`

followed by:

`What is your relationship to the property?`

For one relationship decision, use the direct question.

For several relationship or permission questions, `Tell us about your relationship to [subject]` can be appropriate.

Use `permission`, `have permission`, `give permission` or `need permission` in ordinary public-facing form content. Use `authorised`, `authorisation` or similar formal wording only when a binding legal or prescribed source requires it.

Controlled headings are not a closed list. If no existing heading fits:

1. test whether the page should be regrouped
2. test whether it should be split
3. test whether a direct question works
4. test whether an existing formula works with a clearer subject
5. create a service-specific heading when needed

Do not reopen approved service copy solely to normalise a serviceable heading or permission phrase. Change it when the service is under review, there is a material serviceability problem or an approved standard explicitly requires migration.

**Evaluate whether a section earns its place.** A one-question section may be justified if that question has a distinct actor, decision or user job. A longer section may need splitting when it mixes unrelated purposes. Where short eligibility can be understood naturally in the opening, a separate `Who can apply` section is not compulsory. Where it is decision-critical or hard to scan, retain a distinct eligibility section. Do not impose an ideal number of headings or force a service into another service's structure.

When consolidating or removing questions, check the exact information needed and how it is used downstream. Distinguish duplicated data entry from a separate, meaningful permission, consent, safeguarding or eligibility decision. In repeatable contexts, preserve the link between each item and its own answers (for example, experience for each sport or the origin of each kind of goods). Do not create new stored values or change required information solely to simplify the layout.

## Structured answer and taxonomy integrity

When reorganising an existing answer list, distinguish a presentation change from a change to the information model.

For a presentation-only redesign:

- preserve existing structured values unless evidence or an explicitly accepted decision supports changing them
- do not move an existing structured value under `Other` merely because free text could capture it
- do not promote an example, hint or free-text answer into a new structured value merely because it is mentioned in guidance
- do not silently broaden a stored category, for example `Spouse` to `Spouse or partner`, unless the broader meaning is supported
- preserve or explicitly map backend/reporting values when the service evidence shows those values are used operationally

If a value itself appears unnecessary, apply the normal data-necessity and evidence rules. Do not preserve it solely because it exists.

Check whether all options answer the same question. A list may mix:

- family relationships
- social relationships
- professional relationships
- legal or representative roles

If those categories need to remain, use a question broad enough for all retained options, or separate the dimensions only where the service genuinely needs both.

Branching may reorganise an existing ask without creating a new data requirement. Treat that as an interaction change, not as `No change`. Check that the same users provide the same required information and that downstream meaning is preserved.

## New application and renewal

When both routes exist and the answer changes the journey, use:

`Are you applying for a new [licence] or renewing one?`

Use the confirmed permission noun and service-supported answer options. Do not assume that “new” means the user has never applied before. Do not assume the new-application requirements, processing steps or confirmation wording also apply to renewals. Where renewal rules are unverified, leave them as service-owner dependencies rather than inventing a renewal route. Show route-specific evidence only when supported. Ask an eligibility or actor question first when that determines whether this decision applies. A single substantive decision can be the H1 without a generic application-type heading.

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

- show only relevant questions
- make an implied condition explicit
- keep users on the correct route

It must not:

- introduce new data
- invent an outcome
- create unsupported eligibility
- hide a required safe exit

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

Use a recognisable user-entered name or location to identify repeated records where appropriate. Do not use “Floor 1” for the first record if it may describe the ground floor or another physical floor. Provide distinguishable neutral record labels when no name exists, without inventing one. Keep add/edit/remove controls and meaningful answers distinct.

Do not replace structured repeatables with one large text area when the service must process, compare, route or validate each entry.

## Multi-line fields

Use a text area for one coherent description.

Do not use it to collect several unrelated data points.

Do not ask users to create their own bullet structure when separate questions would reduce error.

## Name fields

Collect only the name information the service requires.

When a full legal name is needed, use:

- First name (textbox)
- Middle name or names (textbox), when supported
- Last name (textbox)

Preferred hint when all middle names are required:

`Enter all middle names in order.`

Use `Optional` or “if known” only when the service permits omission.

Do not introduce a middle-name field absent from the service need. Do not split each middle name into a separate field. Use `Middle name or names (optional)` when the service permits omission; the exact hint remains `Enter all middle names in order.` when all names are needed. Do not add “Leave this blank if you do not have a middle name” when the optional marker already explains it.

### Former names and surname at birth

First identify the required data and whose name it is. Surname at birth, surname before marriage and all previous names are different concepts. Do not automatically rename one as another.

For a confirmed surname-at-birth field on the self route, the scoped hint is:

`Your surname at birth, if different from your current surname.`

Do not attach it to a broader “Other names or maiden name” field or treat it as a universal definition of maiden name. Name the subject on another-person routes. Preserve a supplied approved service label only where the hint describes the actual data; flag a material mismatch. Collect previous names only for a supported service need.

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

Explain a shared contact purpose once where possible rather than repeating it under both telephone and email. Use only the actual supported purpose. Do not turn an example contact-purpose sentence into a universal promise.

## Telephone numbers

Use labels that match the need:

- Telephone number
- Mobile number
- Home number
- Work number

Accept appropriate Barbados and international formats when the service supports overseas contact.

Allow harmless spaces and hyphens when the system can normalise them.

Do not infer an international service route from international-number support.

When an example is useful, apply the exact conditional telephone hint in [content-style-guide.md](content-style-guide.md). Do not paraphrase its labelled examples or stack an older generic format hint on top of it.

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

For one named document, prefer `Upload [document]` rather than a generic heading plus an identical instruction. Specify replacement, removal and useful errors where relevant. Never invent a 5 MB limit, file formats or multiple-file support from another form. A requirement to bring evidence later does not establish an upload requirement now.

Do not ask for “supporting documents” without identifying what is accepted.

## Check your answers

Use `# Check your answers`.

Intro: `Review the information you have given before submitting.`

Show material answers the user needs to verify, with labels that match the form. Show repeated records in recognisable groups and provide Change actions. Handle unanswered optional fields clearly. Do not introduce new questions.

Do not show purely navigational controls such as “Do you need to add another job?” as submitted answers. Keep a meaningful eligibility, role or Yes/No answer when it is part of the submitted record. Do not expose internal-only values as user answers.

After a change, update dependent questions and the review before commitment. Make the intended submitted information consistent with what the user can review; distinguish this specification from verified backend behaviour. State a capture limit rather than calling a partial review complete.

## Agreement and declaration

Place the declaration after Check your answers and immediately before the actual commitment.

For a genuinely combined application commitment screen, use:

```markdown
# Confirm and submit your application

I confirm that the information I have provided is true and correct to the best of my knowledge. (checkbox)

[Submit application button]
```

Use this general truth statement only when supported and no statutory or approved service-specific declaration governs. Do not paraphrase the default for variety. Use `Confirm and submit your [transaction]` only when the transaction and action fit. Use `Declaration` when a separate declaration step is genuinely required. Do not force a combined screen where submission/payment commitment happens elsewhere.

Do not collect a signature or re-entered full name/date by default. Preserve them when there is a supported legal or operational need; do not remove existing required fields solely for consistency. Avoid collecting a date already recorded by the system unless the service requires a separate answer.

Keep additional confirmed commitments and verification consent distinct. Do not invent or broaden consent, rejection warnings, prosecution risks or other consequences. A shorter declaration or a rejection warning accepted in one service is not the universal default.

Use a required, initially unselected checkbox where this agreement is required. Do not repeat the declaration elsewhere. Preserve prescribed wording exactly unless the proper authority permits a change.

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
