# MDA office and role-holder pages

Use this reference for:

- public office or MDA pages
- public role-holder pages
- internal MDA routing pages

Do not use it for general programme guidance or transactional service pages.

## Contents

- Audience and page decisions
- Public office pages
- Contact and exclusion guidance
- Role-holder need, content and freshness
- Internal MDA routing pages
- Phrase and placeholder rules
- Review states and MDA QA

## Core rule

Create only the page types supported by:

- a real audience need
- available information
- a clear maintenance owner

Do not automatically create:

- a public office page
- an internal routing page
- a role-holder page

merely because the MDA exists.

## One audience per page

Public office pages are for members of the public.

Role-holder pages are for members of the public who need to identify the current holder and understand the role.

Internal MDA pages are for government staff who need to route, escalate or understand authority.

Do not mix:

- public and staff instructions
- internal contacts and public contacts
- public service guidance and staff case handling
- institutional profile content and user tasks

## Decide what is needed

Ask:

1. What does the audience need to decide or do?
2. Is the office itself the useful destination?
3. Does the public need the name of the current role-holder?
4. Do staff need operational routing information?
5. Is the information actually programme or service guidance?
6. Who maintains names, contacts and authority information?

Use:

- public office page for contact and responsibility decisions
- role-holder page only for a demonstrated identification need
- internal routing page for staff decisions
- [mda-public-guidance.md](mda-public-guidance.md) for broader guidance or programme information
- service-page modules for transactions

## Public office page purpose

Help users understand:

- what the office does
- whether they should contact it
- what they can contact it about
- where to go instead when necessary

Do not use the page to:

- promote the office
- describe its history
- explain government structure
- list achievements
- publish a biography
- reproduce legislation

## Public office page structure

Use only supported sections:

```markdown
[USER-FACING PAGE]

# [Office or MDA name]

## What this office does

[1 or 2 sentences.]

## What this office is responsible for

- [Outcome or function]

## When to contact this office

Contact this office for:

- [User-recognisable reason]

## Do not contact this office for

- [Reason and useful alternative]
```

“Do not contact” is optional.

Add contact details only when users have a valid reason and route to contact the office.

The review header is not public content and must be removed before publication.

## What this office does

The first sentence should stand alone as a summary.

Default phrase:

`This office is responsible for [primary function].`

Use a clearer task-based alternative when the default becomes vague.

Do not add:

- mission statements
- reputational claims
- policy aspirations
- praise

## Responsibilities

Describe:

- outcomes
- functions
- areas of authority

Use language the public can recognise.

Do not list:

- internal team structures
- every administrative duty
- individual staff tasks
- responsibilities already explained on a separate service page

## When to contact

Derive public contact reasons from confirmed:

- authority
- scope
- routing rules
- service ownership

Use:

`Contact this office for:`

Then list specific user-recognisable reasons.

Do not invent contact reasons from a general responsibility statement.

## “Do not contact” decision

Use only when it prevents likely misuse.

Every exclusion must trace to:

- an authority limit, or
- a routing rule

Give a useful alternative when confirmed.

Avoid:

- other services
- general matters
- anything unrelated

Do not publish an exclusion list that only tells users they are wrong.

## Public contact details

Include only when:

- public contact is permitted
- the contact has a clear purpose
- the office can handle the expected enquiry

For each route, make clear what it is for.

Do not include:

- internal contacts
- personal staff details without authority
- response times without confirmation
- a generic email copied from an unrelated source

Remove the whole section when contact is not appropriate.

Do not write a public explanation for an internal decision to omit contact.

## Contact placeholders

When public contact reasons cannot be drafted until internal routing is confirmed, use the locked review note:

```text
[Dev note:
 PLACEHOLDER ONLY. Populate this “Contact this office for” list using the MDA-facing routing rules.
 ]
```

For exclusions:

```text
[Dev note:
 PLACEHOLDER ONLY. Populate this “Do not contact this office for” list using the MDA-facing routing rules.
 ]
```

Use these verbatim when the placeholder is needed.

Do not show an empty public list.

Make placeholder notes clearly distinguishable from public content. For Markdown output, use the approved note labels. For formatted review documents, use a consistent visual treatment that reviewers can identify easily.

Remove placeholder notes before publication.

## Role-holder need test

Create a role-holder page only when the public reasonably needs to know who holds the role.

Strong reasons may include:

- the role has constitutional or national significance
- the role-holder acts publicly in their own name
- the role has a formal international or statutory representation function
- users must identify the holder to understand an official decision or communication

GOV.UK precedent may inform structure. It does not decide Barbados public need.

If the need is uncertain, refer the page-creation decision to the content team.

Do not create a page merely because:

- the person is senior
- a photograph is available
- another MDA has one
- the MDA wants a profile

## Role-holder page content

Use:

```markdown
[ROLE-HOLDER PAGE (USER-FACING)]

# [Full name]

[Official title]

[Date assumed office, when confirmed and useful.]

This page identifies the person who currently holds the role and explains what the role does.

[Short paragraph explaining the role.]
```

Include:

- confirmed current name
- official title
- confirmed date assumed office when required
- concise role explanation

Do not include:

- biography
- achievements
- political or reputational content
- responsibility bullet lists
- contact routing
- services delivered by the office
- duplicated office-page content

## Role explanation

Default:

`This role leads [area of responsibility] across government.`

Use only when accurate.

Write in paragraph form.

Explain the role at a high level.

Do not repeat the office responsibility list.

## Role-holder freshness

Names and dates are time-sensitive.

Before drafting or updating, require:

- a current reliable source
- the date checked
- the named content owner or maintenance route

Do not infer that a person remains in office from an old page.

If the current holder cannot be confirmed:

- do not publish a name
- provide the role structure
- identify who must confirm it

Recommend review:

- when an appointment changes
- after elections or formal transitions where relevant
- on a scheduled content-review date

## Internal MDA page purpose

Support staff decisions about:

- authority
- scope
- routing
- escalation

Never assume internal content is public.

## Internal page structure

```markdown
[MDA-FACING PAGE]

# [Office name]: internal routing

Use this page to support routing, authority and escalation decisions for matters involving [office name].

## Official details

## Authority and scope

This office can:

- [Capability]

This office cannot:

- [Exclusion]

## Routing guidance

Route the following to this office:

- [Item]

Do not route the following to this office:

- [Item and destination]

## Internal contact details

## Escalation

## Notes for staff
```

Remove unsupported sections.

## Authority and scope

Separate what the office can and cannot do.

Use confirmed legal, policy or operational authority.

Do not infer authority from:

- the office name
- a public responsibility statement
- an individual’s seniority

## Routing guidance

Make routing rules:

- specific
- operational
- distinguishable
- connected to a destination

Avoid:

- send relevant matters
- route as appropriate
- other enquiries
- escalate when necessary

State the actual condition or category.

## Internal contacts

Include only when staff are expected to use them.

State:

- purpose
- route
- role or team

Avoid personal contact details when a role-based route exists.

Do not copy these details to the public page without authority.

## Escalation

Include only when a confirmed path exists.

Default:

`Escalate unresolved matters through [authority].`

Replace the placeholder with the real role or route.

Do not invent an escalation route.

## Notes for staff

Use for short operational instructions that do not belong in routing or authority.

Do not use as a dumping ground for policy history, meeting notes or unresolved questions.

## Phrase-library rule

The standard phrases are approved defaults, not mandatory wording when inaccurate or unclear.

Preserve exact wording only for:

- genuinely locked placeholders
- legal or formally approved phrases

Do not create creative variation for its own sake.

Do adapt a phrase when needed to:

- make the user action clear
- reflect the office’s actual function
- avoid misleading generic wording

## Review and publication states

Review copy may include:

- page-type headers
- locked placeholders
- MDA notes
- content risks

Publication copy must remove:

- review headers
- developer notes
- placeholders
- internal routing
- unresolved facts

Do not label review copy ready to publish.

## MDA-specific QA

### Page decision

- each page has a demonstrated audience need
- no automatic two-page requirement
- role-holder page passes the need test

### Public page

- helps users decide whether to contact
- summary stands alone
- no biography, history or promotion
- responsibilities are user-recognisable
- contact reasons derive from confirmed routing
- exclusions prevent real misuse
- alternatives are useful
- internal information is absent

### Role-holder

- current holder and date are verified
- maintenance owner exists
- role is explained briefly
- office responsibilities are not duplicated
- no routing or promotional content appears

### Internal page

- purpose is operational
- authority is explicit
- can and cannot are separated
- routing conditions are unambiguous
- contacts have a staff purpose
- escalation exists before it is stated
- no public-facing filler appears

### Review output

- page-type headers are correct
- placeholders are verbatim when used
- no empty sections
- UK spelling
- no em dashes
- public and internal content remain separate
