# Module contracts

These contracts define what each reference file owns. They prevent duplication and contradictory instructions.

Maintainer document: This file defines where rules are owned and helps prevent duplication or contradictions. It is not loaded by the skill at runtime.

## Shared rule

A rule should live in one authoritative module.

Other modules may link to it but should not restate it unless a short reminder is essential to prevent error.

## evidence-and-escalation.md

Owns:

- source hierarchy
- confirmed fact, source claim, conflict, gap and assumption definitions
- blocking versus non-blocking thresholds
- privacy and internal-information gate
- MDA note, content risk, design note and dev note use
- escalation owners
- status prerequisites

Does not own:

- page-model decisions
- writing style
- form patterns
- MDA page structures

## voice-accessibility-and-mobile.md

Owns:

- GovTech voice
- plain-language and reading-age rules
- headings, paragraphs, bullets and links
- screen-reader content rules
- mobile content order and density
- accordions as a shared accessibility principle
- minor editorial QA

Does not own:

- page-specific heading sequences
- form logic
- audit scoring

## content-style-guide.md

Owns:

- punctuation
- capitalisation
- written dates
- times
- numbers and ranges
- money and percentages
- abbreviations
- list punctuation

Does not own:

- plain-English decisions
- reading age
- accessibility
- page or form structure
- service facts

## service-page-models.md

Owns:

- definitions and decision rules for entry, start, combined, routing, guidance, what-you-need and offline entry pages
- model recommendation format
- guidance versus routing versus preparation
- CTA role by page type
- page-combination logic

Does not own:

- full copy patterns
- form structure
- MDA office pages

## content-decision-matrix.md

Owns:

- first classification when the requested output is unclear
- cross-family model comparison
- combine-or-separate gateway rules
- correction of common non-content-user requests

Does not own:

- detailed page-model rules
- service facts
- evidence thresholds
- specialist drafting patterns

## service-page-patterns.md

Owns:

- approved heading library
- recommended heading sequences
- certificate patterns and other specialist page patterns
- CTA wording patterns
- contact and help section patterns
- developer notes for service pages

Does not own:

- whether a page type is needed
- shared voice rules
- form labels

## form-content.md

Owns:

- form journey planning
- section and question design
- one-data-point rule
- grouping
- branching notation
- no-new-data rule
- optionality
- names and addresses
- repeatables
- uploads
- declarations
- developer specification format

Does not own:

- detailed QA test list
- confirmation wording
- service-page content

## form-qa.md

Owns:

- logic and sequence checks
- validation and error-content checks
- mutually exclusive options
- at-least-one rules
- telephone formats
- dates and age
- uploads
- repeatables
- health questions
- ownership and asset logic
- implementation limitation handling

Does not own:

- initial drafting format
- general voice
- final confirmation templates

Load after a substantial form draft or for a full review. For a small field or section change, use only the relevant QA section.

## confirmation-and-email.md

Owns:

- submission status
- reference number rules
- next-step content
- payment and attendance states
- confirmation-screen and email parity
- sensitive-information controls
- contact inclusion decision

Does not own:

- form question design
- page-model selection

## mda-and-role-holder-pages.md

Owns:

- public office pages
- role-holder need test
- internal MDA routing pages
- authority, scope and routing
- public-contact derivation
- separation of public and internal audiences
- review and maintenance of office-holder facts

Does not own:

- public programme guidance
- service start pages
- news or communications content

## mda-public-guidance.md

Owns:

- evergreen MDA guidance
- programme information
- non-transactional service information
- contact and location content connected to a user need
- deciding when guidance should link to a transaction

Does not own:

- office profiles
- role-holder pages
- press releases, campaigns or social media

## journey-parity.md

Owns:

- cross-component factual parity
- terminology
- eligibility
- fees
- documents
- timelines
- routes
- next steps
- confirmation parity
- end-to-end read-through

Does not own:

- primary drafting standards already held elsewhere

## audit-and-prioritisation.md

Owns:

- C1 to C7
- scoring
- trigger rules
- priority bands
- using traffic only as a tie-breaker when current data is provided
- audit output

Does not own:

- historical scores
- rewriting rules
- analytics implementation

## output-contracts.md

Owns:

- small response format
- full creation format
- review format
- MDA-question format
- developer-handover format
- Markdown and internal-note conventions
- status display

Does not own:

- content rules used to produce the output

Load for full creation, formal review, MDA-question documents, audit output, confirmation packages and developer handover. Do not load for a small wording correction.
