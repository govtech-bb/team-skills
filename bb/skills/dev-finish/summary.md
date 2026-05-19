# What makes a good session summary

A session summary is a short narrative answering "**why** does the code look this way now?" — written for a future reader (often a future agent, sometimes a future you) coming to this area cold months later.

The diff already shows what changed. The summary captures the reasoning that doesn't survive in the diff.

## Format

- **Path.** `docs/summaries/<YYYY-MM-DD>-<slug>.md`, or the project's own convention if it has one. Create the directory if missing.
- **Length.** Short. A handful of sections, not a wall of text. Aim for what a busy reader will actually read.
- **Plain markdown.** No required frontmatter.

## Sections

Adapt to the session, but the bones are:

- **Context.** One or two sentences on what triggered the session and the state of things going in.
- **What we did.** A terse scaffold — bullets are fine. Just enough to anchor the next section. Reference commits, files, or decision records by name; don't restate them.
- **Why we did it that way.** The meat. The constraints that bit, alternatives considered and rejected, tradeoffs named. If a user correction changed direction, that goes here. If something looked easy and turned out hard, that goes here.
- **Open questions.** Unresolved or deliberately deferred. Empty is fine — write "none" rather than omitting the section.

Optionally, when the session was particularly messy or instructive:

- **What we almost got wrong.** Approaches abandoned, assumptions that broke. Honest, not padded.

## Principles

- **Why over what.** If the summary could be regenerated from the diff, it's not earning its place. Center the reasoning.
- **Name both sides of a tradeoff.** "We chose X over Y because Z" — never just "we chose X."
- **Be honest about messes.** The half-finished approach you abandoned is more useful to a future reader than the polished version.
- **Don't restate decision records.** If the session produced one, link to it and move on. The record is the source of truth on its specific decision.

## When to skip

If the session was mechanical — a single-line fix, a dependency bump with no debate, a pre-decided rename — don't write a summary. There's no why to capture. When in doubt, ask the user.
