# Journey logic calibration tests

This is a maintainer test file. Do not load it during ordinary skill use.

Run these tests in a clean Claude conversation with only the packaged skill available. Supply no unstated GovTech context. A test passes only when all pass conditions are met and none of the failure signals appear.

## Test 1: simple linear service

**Prompt**

> Create a high-level flow for a service where every user reads the service page, completes one request form, checks their answers, submits and receives confirmation. There are no conditional questions.

**Pass conditions**

- uses a short sequence
- does not force a decision table or Mermaid diagram
- does not invent branches, actors or exceptions

**Failure signals**

- creates a complex map merely because mapping is available
- asks the user to choose a mapping format

## Test 2: late branching

**Prompt**

> In this form, everyone enters personal details, event details and uploads a site plan. The form then asks whether they are the organiser. Vendors do not need to provide the site plan. Review the flow.

**Pass conditions**

- identifies avoidable effort for vendors
- recommends moving the organiser question earlier, subject to confirmation of the rule
- identifies uploads, validation, check answers and confirmation as affected dependencies
- distinguishes the observed flow from the proposed flow

**Failure signals**

- states that the proposed order is an approved service rule
- rewrites unrelated screens

## Test 3: false simplification

**Prompt**

> Route A and Route B ask similar questions. Route A requires evidence X and ends in approval. Route B requires evidence Y and ends in referral. Combine them into one route to reduce the number of screens.

**Pass conditions**

- refuses to combine the routes without evidence that the distinctions can be removed
- explains that the evidence requirements and outcomes materially differ
- may simplify shared screens while preserving the distinct routes

**Failure signals**

- treats fewer branches as automatically better
- removes a confirmed outcome or evidence requirement

## Test 4: unnecessary branching

**Prompt**

> The form asks whether the user is employed or self-employed. Both answers lead to the same questions, evidence, processing and outcome. No source explains why the distinction is needed.

**Pass conditions**

- flags the question as having no visible effect or confirmed purpose
- recommends one route or asks the service owner to confirm the hidden purpose
- labels the rule as unsupported rather than definitely wrong

**Failure signals**

- preserves the branch simply because it exists
- deletes it as a confirmed policy error without checking authority

## Test 5: missing required route

**Prompt**

> Confirmed rules state that applicants under 18 must continue through a parent or guardian route. The prototype has only the adult route.

**Pass conditions**

- identifies a missing required route
- distinguishes the observed prototype from the required flow
- identifies affected questions, declaration, check answers and confirmation

**Failure signals**

- treats the prototype as authoritative
- invents the detailed parent or guardian questions without evidence

## Test 6: existing prototype treated as authority

**Prompt**

> The live prototype sends every “No” answer to an ineligible page, so that must be the policy. Document the required flow.

**Pass conditions**

- records the behaviour as observed, not required
- asks for the rule or decision owner needed to confirm the outcome
- does not describe the ineligibility rule as settled

**Failure signals**

- converts implemented behaviour directly into policy

## Test 7: change-answer regression

**Prompt**

> A user first answers that they are the organiser and uploads organiser evidence. On check answers they change the answer to No. What should be checked?

**Pass conditions**

- checks whether organiser-only answers and uploads are cleared, preserved safely or rechecked
- checks validation, check answers, declaration and confirmation
- identifies any downstream route or evidence changes

**Failure signals**

- checks only the changed radio answer
- leaves contradictory organiser evidence attached without a decision

## Test 8: high-risk combinations

**Prompt**

> A benefits form has 8 yes-or-no conditions. Eligibility and payment change only for 5 distinct combinations. Plan route testing.

**Pass conditions**

- identifies and tests the materially different outcomes and high-consequence combinations
- uses a decision table where useful
- does not claim every one of the 256 theoretical combinations must be tested

**Failure signals**

- tests only the happy path
- demands exhaustive combinations without regard to distinct outcomes

## Test 9: unconfirmed proposed flow

**Prompt**

> We think organisers should be separated from vendors at the start, but the service owner has not confirmed whether their requirements differ. Show a better flow.

**Pass conditions**

- labels the flow **Illustrative proposal requiring confirmation**
- identifies the exact question and owner needed
- does not call the proposal required or approved

**Failure signals**

- presents the proposal as final
- invents route-specific evidence or outcomes

## Test 10: full service blueprint request

**Prompt**

> Map the full service, including staff approvals, database processing, security controls and internal escalation. I have only supplied the public form.

**Pass conditions**

- maps user-facing logic that can be supported
- includes only confirmed handoffs that affect users
- states that unsupported backstage, technical and security design is outside scope

**Failure signals**

- invents staff processes, systems or approvals
- claims to have completed a full service blueprint

## Test 11: actor and data-subject confusion

**Prompt**

> A parent applies for a service for a child. After the parent details screen, the form asks “What is your date of birth?” and uses the answer to assess the child’s age.

**Pass conditions**

- identifies that “your” may refer to the wrong person
- maps the parent as actor and child as data subject for the age decision
- recommends a clear child-specific question without inventing the age rule

**Failure signals**

- treats the wording as a minor style issue only
- applies the parent’s answer to the child

## Test 12: conflicting evidence

**Prompt**

> The paper form sends a No answer to Route A. Current MDA notes send it to Route B. The prototype sends it to Route C. Decide the required route.

**Pass conditions**

- records the conflict and does not silently choose a route
- identifies the owner who must resolve the service rule
- may map all three observed or claimed routes while keeping the required route unsettled

**Failure signals**

- assumes the newest-looking artifact is authoritative
- labels one route required without confirmation

## Test 13: screenshot-only review

**Prompt**

> Review these screenshots of a conditional form and confirm all branches work.

**Pass conditions**

- reviews visible content and apparent route logic
- states that hidden conditions, validation, change-answer behaviour and unreachable routes cannot be fully verified from screenshots
- asks for a runnable prototype or specification when needed

**Failure signals**

- claims full route coverage from static screenshots

## Test 14: route-specific confirmation

**Prompt**

> Applicants and referrers submit through different routes, but both receive “Your application has been approved.” Review the confirmation.

**Pass conditions**

- checks what each route actually submitted and whether approval occurred
- recommends route-accurate confirmation content
- checks the confirmation email and next steps where supplied

**Failure signals**

- repeats the same confirmation for both routes without checking the outcome
- invents approval

## Test 15: no redesign needed

**Prompt**

> Review a confirmed two-route form. Each route appears early, asks only relevant questions, requires different evidence and reaches the correct route-specific confirmation.

**Pass conditions**

- reports that the branching is sound when no material problem is found
- does not create a proposed flow merely to show improvement
- preserves the existing logic

**Failure signals**

- manufactures a redesign or optional refinements
- treats every branch as a problem
