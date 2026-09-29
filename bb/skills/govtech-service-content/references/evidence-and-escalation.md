# Evidence and escalation

Use this reference for every task.

It controls what may be treated as fact, when drafting is safe, what must remain visible, and who must resolve decisions outside content design.

## Contents

- Source hierarchy and paper forms
- Information classification and consequential facts
- Drafting thresholds
- Questions and visible notes
- Privacy and internal information
- Escalation ownership
- Final evidence check

## Source hierarchy

Use this order when sources conflict:

1. law and binding policy
2. confirmed service rules and current operational reality
3. approved GovTech content and service standards
4. confirmed MDA facts
5. approved live service content and forms
6. current reusable patterns and approved templates
7. previous drafts, examples and service-specific decisions
8. notes and structural assumptions

Do not assume a source is accurate merely because it is official-looking, published, newer or supplied by a senior person.

## Paper forms

Treat a paper form as evidence of:

- information currently or previously collected
- existing legal or operational wording
- roles, declarations and evidence requirements
- the paper process

Do not automatically treat it as the highest authority.

A paper form may be:

- outdated
- incomplete
- designed around manual processing
- inconsistent with law, policy or current operation
- unsuitable for direct digital reproduction

Preserve legal and policy meaning. Do not preserve unclear wording, question order or paper layout merely because it appears on the source.

## Classify information before drafting

Internally classify consequential information as one of:

### Confirmed fact

Supported by the strongest relevant source and not contradicted.

May be used in public copy.

### Source claim

Present in a source but not sufficiently verified for consequential public use.

May support structure. Mark for confirmation before publication.

### Conflict

Two or more sources disagree.

Do not silently choose one.

### Missing fact

Required to produce accurate content but absent.

Decide whether it blocks drafting.

### Structural assumption

An inference used only to organise the proposed journey or draft.

List separately when it affects the recommendation. Never present it as a service fact.

## Consequential facts

Check support for:

- service purpose
- intended users
- eligibility and exclusions
- service channel
- online and in-person steps
- deadlines
- fees and payment
- processing time
- required documents
- information the form collects
- legal requirements
- office locations
- contact routes
- response expectations
- approval outcomes
- what happens next

Never invent these.

## Drafting threshold

### Not ready to draft

Use when the task, service or audience is too unclear to plan safely.

Examples:

- the source does not reveal what the service does
- it is unclear whether the content is public or internal
- several unrelated services are mixed together

Output:

- what is understood
- up to 3 blocking questions
- likely owner
- status

### Structure only

Use when the likely content journey can be planned but public wording would imply unconfirmed facts.

Examples:

- eligibility materially affects the route but is unknown
- online versus in-person operation is unclear
- legal wording would need interpretation
- sources conflict about a key requirement

Output:

- proposed structure or journey
- affected gaps
- questions and owners
- status

### Draft with confirmation notes

Use when the main content is supported and gaps do not make the draft misleading.

Examples:

- a secondary contact route is missing
- an optional response time is unconfirmed
- a destination link is not yet available

Keep notes beside the affected section or in a clearly linked confirmation list.

### Ready for content review

Use when:

- the draft and journey are coherent
- blocking gaps are resolved
- material assumptions are visible
- relevant QA has been run

This is not factual approval.

### Ready for factual confirmation

Use when:

- content and journey decisions are sufficiently resolved
- the MDA or service owner needs to verify operational facts
- all facts requiring confirmation are listed clearly

MDA factual review does not determine GovTech wording, patterns or accessibility standards.

### Ready for developer handover

Use when:

- wording and structure are sufficiently resolved for implementation
- required behaviour and logic are specified
- known implementation gaps are visible
- outstanding factual, testing or approval actions are listed

This does not mean ready to publish.

## Blocking versus non-blocking questions

A question is blocking when its answer could change:

- whether the service is appropriate
- who may use it
- the user’s route
- the data collected
- a legal or policy meaning
- the fee or deadline
- whether the service is online, offline or hybrid
- what happens after submission
- whether publishing would expose internal or personal information

Ask blocking questions first.

A question is non-blocking when a useful and non-misleading draft can proceed without the answer.

Do not ask optional improvement questions before blockers.

## Progressive questioning

Ask no more than 3 questions at once.

For each consequential question:

- use ordinary language
- use terms from the supplied source
- explain briefly what the answer affects
- identify the likely owner if the user does not know

Do not ask the user to confirm:

- information already supplied
- harmless editorial choices the skill can make
- content terminology they are not expected to know

## Source conflict format

Use:

`[Content risk: Source conflict. Confirm whether to follow X or Y before publishing.]`

Replace X and Y with short, identifiable descriptions.

If the conflict affects only one section, place the note there.

If it affects the whole journey, show it before the draft or structure.

## MDA confirmation format

Use:

`[MDA note: Confirm...]`

Use an MDA note for a factual or operational question, not a content-style preference.

Do not use MDA notes to transfer responsibility for GovTech content decisions.

## Design note format

Use:

`[Design note: ...]`

Use when:

- a hidden decision should become structured
- the interaction may cause error
- content alone cannot resolve the issue
- a service or interaction change should be considered

## Developer note format

Use:

`[Dev note: ...]`

Use only for implementation behaviour that affects the content or user journey.

Do not put ordinary content advice into developer notes.

## Minor fixes versus visible changes

Silently fix:

- spelling
- punctuation
- grammar
- harmless formatting inconsistencies
- obvious duplication

Show:

- changed meaning
- removed or added data collection
- changed eligibility or route
- broken logic
- accessibility risks
- legal uncertainty
- privacy or security concerns
- material assumptions
- implementation limitations
- source conflicts

## Privacy and data minimisation

Before using a source, check for unnecessary:

- names
- identification numbers
- addresses
- telephone numbers
- email addresses
- financial information
- medical information
- uploaded evidence
- case details
- staff-only contacts

Do not repeat real personal data in:

- rewritten forms
- examples
- QA findings
- developer handover
- confirmation templates

Use neutral placeholders where an example is needed.

If a completed form or case record is supplied, assess the structure without copying the person’s details.

## Public and internal information

Treat these as internal unless public use is confirmed:

- staff contacts
- internal escalation routes
- staff instructions
- routing rules
- case-handling notes
- internal service limitations
- unpublished policy or operational detail

Do not convert internal information into public guidance merely because it might be useful.

## Escalation ownership

### Content team

Refer:

- uncertain page or journey model after applying the rules
- conflicting approved patterns
- high-risk public wording
- complex content across several services
- final content review

Do not refer minor edits the skill can safely complete.

### MDA or service owner

Refer:

- eligibility
- fees
- documents
- timelines
- service channels
- locations
- contacts
- current operation
- what happens after submission

### Policy owner

Refer:

- entitlement
- exceptions
- approval criteria
- policy intent
- rules not established in available sources

### Legal advisers

Refer:

- legal interpretation
- statutory wording
- uncertainty about legal effect
- proposed changes to required declarations

### Privacy or security specialists

Refer:

- unclear need for personal or sensitive information
- retention
- identity evidence
- unsafe disclosure
- confirmation-email sensitivity
- access to internal information

### Accessibility specialists

Refer when established content and component standards do not resolve an accessibility risk.

### Developer or technical owner

Refer:

- validation capability
- saving and returning
- uploads
- integrations
- routing implementation
- reference numbers
- email behaviour
- platform constraints

## Escalation response format

State:

1. what cannot be decided
2. why it matters
3. who should decide
4. what can continue meanwhile

Example:

> The sources give two different age limits. This changes who can apply, so I have not drafted that eligibility statement. The programme owner needs to confirm the correct age range. I can still prepare the remaining page and form structure.

Do not say only:

- ask the team
- get specialist help
- confirm this

## Final evidence check

Before returning an output, confirm:

- no assumption appears as a public fact
- every material conflict remains visible
- unanswered blockers have not been written around
- personal and internal information has not leaked into public copy
- the status matches the evidence
- the next owner and action are clear
