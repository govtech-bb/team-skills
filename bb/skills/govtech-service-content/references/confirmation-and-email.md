# Confirmation screens and emails

Use this reference for submission outcomes, confirmation screens and confirmation emails.

Confirmation content completes the service journey. It is not a generic receipt.

## Contents

- Purpose and evidence
- Screen structure
- Reference numbers and next steps
- Payment, attendance and review states
- Email structure
- Contact and sensitive-information rules
- Failure, duplicate and partial submissions
- Parity and QA

## Purpose

Confirmation should help users understand:

- whether submission succeeded
- what was received
- what happens next
- what they must do
- when they must act
- what communication to expect

Do not add unsupported reassurance.

Do not promise an outcome or timeframe merely because the form submitted successfully.

## Confirm the actual system behaviour

Before drafting, confirm where possible:

- what counts as successful submission
- whether a reference number is generated
- whether an email is sent
- when the email is sent
- whether payment occurred
- whether payment happens later
- whether attendance is required
- who reviews the submission
- how the outcome is communicated
- what happens when submission fails

If unknown, use a visible confirmation note.

## Confirmation-screen title

Default for an application:

`# Application submitted`

Use the actual transaction:

- Request submitted
- Registration submitted
- Report submitted
- Booking confirmed

Do not use “Application submitted” for every service.

Do not show a success title until the system confirms success.

## Confirmation-screen structure

Use only relevant sections:

```markdown
# [Submission status]

[What was received.]

Reference number: [number]

## What happens next

[Confirmed review and communication steps.]

## What you need to do

[Required action and deadline.]
```

Do not create empty sections.

If the user has no further action, do not add “What you need to do”.

## What was received

Use a short sentence:

`We have received your application for [service name].`

Use the same service name as the form and start page.

Do not imply the application is:

- approved
- complete
- valid
- accepted for payment

unless the system or process confirms it.

## Reference number

Include only when the system generates and displays one.

Use:

`Reference number: [reference number]`

Tell users what it is for only when confirmed.

Do not:

- invent a number
- promise it will appear in email unless confirmed
- expose an identification number as the reference
- label a temporary tracking value as an approval number

## What happens next

State the real process:

- review
- document check
- payment request
- attendance
- decision
- communication channel

Use direct language.

Example:

```markdown
## What happens next

We will review the information you provided.

If we need more information, we may contact you.
```

Include “If we need more information...” only when contact details were collected for that purpose and the service may actually contact the user.

Do not use it as a universal filler sentence.

## User action

Give the action its own section when the user must:

- pay
- attend
- bring originals
- send evidence
- contact an office
- meet a deadline

State:

- what to do
- when
- where or how
- what to bring

Do not hide a required action inside a review paragraph.

## No further action

When confirmed:

`You do not need to do anything else now.`

Use only when accurate.

Do not add this if the user must monitor email, attend, pay or retain documents as an active requirement.

## Payment after approval

Use when payment is not yet due:

```markdown
If your application is approved, we will tell you how to pay.
```

Add timing, amount or method only when confirmed.

Do not imply approval is likely.

## Payment already made

Use only when the system confirms payment:

```markdown
We have received your payment.
```

State what happens next.

Do not repeat card details, bank information or full transaction identifiers.

## Payment required now

If payment is a separate next action, state:

- amount
- method
- deadline
- consequence of not paying

only when confirmed.

Use a payment action only if it is safe and functional.

## Attendance required

State:

- who must attend
- where
- when or how an appointment is arranged
- what to bring

Do not say “Your application is complete” when attendance remains.

## Documents required later

Name the documents.

State whether users must:

- bring originals
- send copies
- wait to be asked

Do not tell users to keep originals “in case” unless the service supports that instruction.

## Processing time

Include only a confirmed timeframe.

Clarify the starting point:

- from submission
- after payment
- after attendance
- after all documents are received

Do not write a target as a guarantee.

If the timeframe varies materially, explain the condition briefly or omit it pending confirmation.

## Contact information

Do not include contact details by default.

Include them only when:

- users may need help with the submitted application
- the contact route is confirmed
- its purpose is clear
- using it will not bypass the process

Do not add contact details merely because Master Prompt v8.8 listed them.

Do not include public contact details in both the confirmation screen and email unless users genuinely need them in both places.

Never expose internal contacts.

## Confirmation email purpose

The email should:

- confirm receipt
- repeat essential next steps
- provide the reference number when confirmed
- preserve a record the user may need

It should not:

- reproduce the full application
- repeat sensitive answers
- include unnecessary personal information
- introduce new requirements
- contradict the screen

## Email subject

Use:

`Application received: [service name]`

Adapt the transaction:

- Request received: [service]
- Registration received: [service]
- Booking confirmed: [service]

Avoid a full stop at the end of the subject.

Do not use vague subjects such as:

- Confirmation
- Thank you
- Application

## Email structure

```markdown
Subject: [Transaction received]: [service name]

We have received your [application, request or registration] for [service name].

Reference number: [number]

## What happens next

[Confirmed next steps.]

## What you need to do

[Confirmed action, if any.]
```

Remove unsupported sections.

Use the same terms and service name as the screen.

## Sensitive information

Do not include:

- medical answers
- allergy or medicine details
- full identification numbers
- bank details
- card details
- uploaded-document contents
- detailed legal or family information
- children’s sensitive information
- full addresses without need

Do not surface medical information again merely to reassure the user that it was received.

If evidence of submission is needed, confirm the category rather than reproduce the answer.

Example:

`We have received the documents you uploaded.`

Use only when the system confirms receipt.

## Personalisation

Use the person’s name only when:

- the system can insert it reliably
- it helps the communication
- the correct person is clear

Avoid including a child’s or third party’s name in the email subject.

Do not personalise with sensitive case details.

## Unsuccessful submission

Use a distinct error state.

State:

- the submission was not received
- whether answers were saved
- what the user can do
- how to get help when a confirmed route exists

Example:

```markdown
# We could not submit your application

Your application has not been sent.

Try again. If the problem continues, [confirmed recovery action].
```

Do not show success content after a failed submission.

Do not tell the user to submit again when the system may have received it but cannot confirm.

## Uncertain submission state

When the system cannot confirm success:

- do not claim receipt
- do not tell the user to resubmit immediately
- provide a safe checking or recovery route
- identify possible duplicate-submission risk

This is a technical and service issue, not only a wording problem.

## Duplicate-submission prevention

Use:

`Do not submit another application unless we ask you to.`

only when:

- duplicate submissions create a real problem
- the service has a route for follow-up
- the statement does not trap users after a technical failure

Do not use it as a universal confirmation sentence.

## Partial or draft submission

Do not call saved progress “submitted”.

Use:

- Application saved
- Draft saved

only when the system confirms it.

State:

- how to return
- how long it is saved
- what remains

## Screen and email parity

Compare:

- success status
- service name
- reference number
- payment status
- next steps
- user action
- deadline
- attendance
- processing time
- expected contact

Differences are permitted only when the channel requires them and meaning remains aligned.

Email may omit sensitive or interface-only information.

## Conditional pattern

Do not output every state to the user.

Use the state matching the completed route:

- no payment
- payment later
- payment received
- attendance required
- additional evidence required
- fixed next step

In a specification, label alternatives clearly as conditional developer content.

Example:

`(If payment was received, display: We have received your payment.)`

## Confirmation developer notes

Use only where needed:

`[Dev note: Display the same reference number on the screen and in the email.]`

`[Dev note: Do not include the applicant’s ID number in the email.]`

`[Dev note: Send this email only after the submission is confirmed as received.]`

Do not use developer notes to hide missing service facts.

## Confirmation QA

Confirm:

- the title matches the transaction
- success is real
- the service name matches
- reference number is system-supported
- next steps are confirmed
- user action is prominent
- payment state is correct
- attendance is not hidden
- processing time has the right starting point
- contact details are included only for a demonstrated need
- screen and email agree
- sensitive answers are not repeated
- failure and uncertain states are safe
- duplicate-submission wording is justified
- no new policy or requirement appears after submission
