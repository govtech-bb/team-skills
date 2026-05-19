---
name: dev-plan
description: Discuss a feature, bug fix, or refactor before writing code. Discussion-first — ask questions, surface alternatives, then produce a short written plan. Use when the user invokes /bb:dev-plan.
---

# dev-plan

Run a planning conversation before any code is written. The shape is **discussion first, plan second** — don't draft the plan until you've asked questions, the user has had a chance to push back, and you can name the goal in one sentence.

If the line below has content after the colon, treat it as the topic. Otherwise ask the user for one.

Topic: $ARGUMENTS

## 1. Orient

Before the first substantive reply, do a light context pass. Adapt to what the project actually has:

- Read the project's `CLAUDE.md` if present.
- Skim any architecture, design, or decision records the project lists (e.g. an ADR directory, prior plan files). Note titles; don't read each end to end.
- Look at the code area the topic touches — names, shape, how it's wired up.

Pull specific docs in as their relevance becomes clear during discussion. Don't read everything upfront.

## 2. Discuss

Open with one or two focused questions. Iterate.

Use the conversation to:

- Understand the goal and the **why** behind it — what problem this solves, what triggered it now.
- Identify constraints — existing decisions, in-flight work, tools already in use, tests that would break.
- Decide whether the existing code shape fits the change. If it doesn't, say so plainly. Refactoring as part of feature work is fine; pretending it's not needed is not.
- Surface alternatives — including using an existing library, doing it differently, or not doing it at all.

Conversation rules:

- **Short messages.** One or two questions per turn, not essays.
- **Ask, don't speculate.** Don't say "likely" or "probably." If you don't know, read the code, fetch the docs, or ask.
- **Reuse before reinvent.** Prefer mature libraries and the patterns already in the codebase over inventing new ones. Don't swerve from existing tech choices without a named reason.
- **Push back when invited.** If the user expresses doubt or otherwise asks for debate, give the strongest counter-case you have. Stress-test, don't perform agreement.

Don't draft the plan during discussion. Don't make assumptions and proceed. Ask.

## 3. Signal readiness

When you think the topic is well enough understood that a useful plan could be written, say so explicitly and ask if the user is ready for you to draft. **Do not draft before asking.**

If they want more discussion, return to step 2.

## 4. Write the plan

Once the user gives the nod, write the plan. A reasonable default shape:

- **Goal** — what this delivers, in user-facing terms.
- **Approach** — the chosen path and the one or two alternatives considered.
- **Scope** — bullet list of work in this change.
- **Files** — files to add or modify (when known).
- **Verify** — how you'll know it's done.
- **Open questions** — anything unresolved.

Drop sections that don't apply for a small, focused change.

Ask the user where the plan should live. If they don't have a preference, default to a markdown file under `docs/plans/<slug>.md` in the project, creating the directory if needed.

If the feature is long, break it up into multiple named sessions.

After writing, stop. Implementation is a separate session — typically `/bb:dev-start`.

## Edge cases

- **No topic given.** Ask for one. Don't proceed without.
- **Topic is too vague.** Discuss until it's specific. If the user resists narrowing, name the ambiguity and ask which slice to plan.
- **User wants to skip discussion** ("just write the plan"). Ask once whether they're sure. If they confirm, write it but include an explicit "Open questions" section flagging what wasn't discussed.
- **Mid-discussion you discover the planned approach won't work.** Surface it. Don't quietly route around it in the plan.
