# The delivery pipeline

The canonical form intake process a service moves through on its way to going live.
Twenty-four steps in five phases. Keep this shape across services so the whole team
reads a Super Delivery Manager page the same way; only change a step if the service
genuinely differs.

Each step in the template's `STAGES` array takes:

```js
{ n:13, phase:"Get it approved", owner:"Engineering",
  status:"current",            // "done" | "current" | "pending"
  date:"2026-08-11",           // date it passed (done) or started (current); omit for pending
  since:"2026-08-11",          // when work/waiting started — drives aging (current + gate steps)
  target:5,                    // SLA in days; the step turns "overdue" past it
  name:"Engineering check and build",
  why:"A final quality check, then build it properly.",
  gist:"Shannon has made the changes and built the form. It's on the test site, ready to try.",
  ev:{ label:"Ready for testing", url:"…#issuecomment-…" },   // evidence: comment or sub-issue
  next:{ who:"Engineering and Delivery", what:"review the sandbox build" }   // current/gate only
}
```

## The steps

Suggested owners and SLAs are defaults — adjust to the service.

### Understand the service
| # | Step | Why | Owner | SLA |
|---|------|-----|-------|-----|
| 1 | Get the paper form from the department | So we start from the real, official form, not from a guess. | Delivery | — |
| 2 | Log it on GitHub | So everything about this form stays in one place. | Delivery | — |
| 3 | Build a first version with Claude | To turn the paper form into a working online draft, fast. | Delivery | — |
| 4 | Meet the department to learn how it works | So we understand the real process, from the people who run it. | Delivery | — |
| 5 | Fill in the discovery questions | To capture the details each form needs: where it goes, how fast, and who handles it. | Delivery | — |
| 6 | Check the tricky parts with engineering | To make sure we can actually build what we've designed. | Engineering | — |
| 7 | Walk the department through the draft | To catch anything missing before we go further. | Delivery | — |

### Write and test the content
| # | Step | Why | Owner | SLA |
|---|------|-----|-------|-----|
| 8 | Review the words | To make the form clear and easy to read. | Content | — |
| 9 | Make the changes | So the department's feedback shows up in the form. | Delivery | — |
| 10 | Test it with real people | To check the form works for the people who'll use it. | Delivery | — |
| 11 | Review the words again | To fold in the department's latest changes. | Content | — |
| 12 | Make the changes again | So the form matches what users and the department need. | Delivery | — |

### Get it approved
| # | Step | Why | Owner | SLA |
|---|------|-----|-------|-----|
| 13 | Engineering check and build | A final quality check, then build it properly. | Engineering | 5 |
| 14 | Final review with the department | To walk them through what we found in testing and the finished form. | Department | 5 |
| 15 | Department signs it off | They agree the form is ready to go live. **Usual gate/blocker.** | Department | 7 |

### Build and go live
| # | Step | Why | Owner | SLA |
|---|------|-----|-------|-----|
| 16 | Build the live form | To get it ready to publish on alpha.gov.bb. | Engineering | 5 |
| 17 | Hand over to engineering | To connect the emails and case management system, then move it to staging. | Engineering | 5 |
| 18 | Test it end to end | To check the whole form works on the staging site and in the chatbot. | Engineering | 5 |
| 19 | Show the department how to use it | So the team knows how to use the case management system. | Platform | 5 |
| 20 | Go live | Publish the form on alpha.gov.bb. | Delivery | — |

### After go-live
| # | Step | Why | Owner | SLA |
|---|------|-----|-------|-----|
| 21 | Tell the Comms team | So they can promote it, about 3 days after it goes live. | Comms | — |
| 22 | Check in after go-live | To make sure the form is working as it should. | Delivery | — |
| 23 | Check in at 1, 3 and 6 months | To get feedback and check people are using it as we hoped. | Delivery | — |
| 24 | Check in at 12 months | To check the form is still useful and up to date. | Delivery | — |

## Reading GitHub and Slack into the steps

### Status
- **done** — there is clear evidence the step happened: a comment describing it, a
  closed sub-issue, a shared review doc or prototype update.
- **current** — work is actively happening now (a recent comment says so, a sub-issue
  is open and being worked). More than one step can be current if workstreams run in
  parallel (build, test and sign-off prep can overlap). Set `since` so aging works.
- **pending** — not started yet. Omit `date`; the timeline shows "To do".

### Date and evidence
- Take a step's **date** from the real event: the comment's `createdAt`, or a
  sub-issue's `closedAt`. Do not invent dates.
- Set **ev** to the strongest proof: a comment **permalink** (`.../issues/N#issuecomment-…`)
  or a sub-issue (`.../issues/M`). Give it a short label ("Content review",
  "#641 End-to-end test"). If a `done` step has no evidence, keep it honest in the
  gist rather than fabricating a link.

### Owners
Map each step to the role that owns it: **Delivery, Engineering, Content, Department,
Platform, Comms.** The template colours the owner dot per role from the alpha.gov.bb
palette.

### Blockers (the "Blocking go-live" band)
List what is genuinely holding up go-live, each with a `since` date and a link:
- an **open gate sub-issue** (for example "Secure sign-off");
- a **named approver** who must see it first (the Permanent Secretary, the Chief
  Environmental Health Officer);
- a **paired form or dependency** that must ship together.
Mark the sign-off step with `blocker:true` so it also reads as the gate in the list.

### Aging and SLA
The template computes time-in-stage from `since` to `SYNCED_AT`:
- a **current** step shows "in progress N days of T day target";
- the **gate** step shows "waiting N days of T day target";
- past the `target`, it turns amber and reads "overdue".
Set `since` on current and gate steps. Set a `target` where a wait matters (the
approval and build steps); leave it off for early discovery steps.

### Now / Waiting on / Next (console)
These derive automatically: **Now** from the current steps, **Waiting on** from the
gate step, **Next** from the next pending steps. You do not write them by hand — set
the step data correctly and they follow.
