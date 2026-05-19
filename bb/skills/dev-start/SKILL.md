---
name: dev-start
description: Begin a coding session. Read the reference, orient to the code, repeat back intent, wait for confirmation, then build. Use when the user invokes /bb:dev-start.
---

# dev-start

Start a coding session cleanly. The goal is to make sure you and the user agree on what's being built before any code is written — even if there's a written plan, your mental model and theirs may not match yet.

If the line below has content after the colon, treat it as the user's pointer to the change (a plan file path, an issue link, a free-text description). Otherwise ask.

Pointer: $ARGUMENTS

## 1. Read the pointer

If the user provided a plan file, issue link, or other document: **read it in full.** Don't skim. If the document references other docs (design notes, related plans, decision records), read those too if they're load-bearing.

If they gave a free-text description, treat the conversation itself as the spec.

If there's no pointer at all, ask the user to describe what they're working on before continuing.

## 2. Orient

Check the current state of the code the change will touch. Names, shape, tests, callers. If a plan was written days or weeks ago, code drift is common — note any gap between what the plan assumes and what's there now.

If the project has a `CLAUDE.md`, read it for conventions (test commands, lint, anything project-specific you'd otherwise have to guess).

## 3. Ask questions

If anything is ambiguous, under-specified, or seems wrong, ask before building. Batch questions into one message where possible.

If everything is clear, skip this step rather than inventing questions.

## 4. Repeat back intent

In your own words, state:

- **What you'll build** in plain terms — not a re-draft of the plan, just the scoped outcome.
- **Approach** — the key decisions you'll make as you go.
- **Anything you'd deviate from** — if the plan or pointer is stale or wrong in places, name it now.

Keep it tight. A few bullets, not a paragraph.

## 5. Wait for confirmation

Do not start building until the user confirms. If they correct your understanding, revise and confirm again.

## 6. Build

Once confirmed, implement. Follow the project's normal workflow — write tests as you go, commits at meaningful checkpoints, align to the project's `CLAUDE.md` conventions.

When the implementation work is done, hand back to the user. This skill ends at "I'm done coding." Wrapping up — tests, decisions worth recording, the commit — is `/bb:dev-finish`, a separate invocation.
