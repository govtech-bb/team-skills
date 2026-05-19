# Contributing

## How a skill works

A skill is a markdown file (`SKILL.md`) with YAML frontmatter that Claude Code loads as instructions. When the user invokes `/bb:<skill-name>`, the contents of that skill's `SKILL.md` are read into the conversation and Claude follows them.

Skills can reference sibling files (other markdown, JSON, examples, etc.) for content that should be independently iterable — see `bb/skills/dev-finish/summary.md` for an example.

## Add a new skill

Create a directory under `bb/skills/<skill-name>/` with at minimum a `SKILL.md`:

```
bb/skills/<skill-name>/
  SKILL.md
  <optional-sibling>.md   ← referenced helper files, if any
```

### Frontmatter

Every `SKILL.md` starts with:

```yaml
---
name: <skill-name>
description: <one sentence on what the skill does and when to invoke it, ending with "Use when the user invokes /bb:<skill-name>.">
---
```

The `description` is what Claude reads to decide whether to apply the skill — write it specifically and end with the invocation phrase so the trigger is unambiguous.

### Naming

Skill names follow `<discipline>-<verb>`:

- `dev-*` — software development workflow
- `ops-*` — operations and infrastructure
- `sec-*` — security
- (add more disciplines as the team grows)

Names should describe an action the user is taking. `dev-plan`, `ops-deploy`, `sec-audit` — not `dev-planner`, `ops-deployment-tool`, `sec-auditor`.

## Testing a skill locally before opening the PR

You can install this repo as a local marketplace to try changes end-to-end:

```
/plugin marketplace add /absolute/path/to/your/clone
/plugin install bb@team-skills
```

Reload Claude Code, invoke your skill, iterate. Remove the local marketplace before switching back to the official one:

```
/plugin marketplace remove team-skills
```

## Opening a PR

- Branch off `main`.
- One coherent change per PR — a new skill, or a focused edit to an existing one.
- In the PR description, say what the skill does and when a user would invoke it. If you tested it locally, mention the scenarios you tried.

## Reviewing a PR

Reviewer should check:

- Frontmatter is present and the `description` ends with the `Use when the user invokes /bb:<skill-name>.` phrase.
- Name follows the `<discipline>-<verb>` convention.
- Content reads as **instructions to Claude**, not documentation *about* Claude.
- The skill scaffolds a conversation or process — it doesn't mandate a workflow or lock in a tool choice.
- If a sub-spec belongs in a sibling file (because it'll evolve on its own cadence), it lives there, not inline.

## Updating an existing skill

Same flow. When the PR merges to `main`, the change reaches all installed users at their next Claude Code startup via marketplace auto-update.
