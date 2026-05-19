# Contributing

## How a skill works

A skill is a markdown file (`SKILL.md`) with some information formatted using [YAML](https://yaml.org/) that Claude Code loads as instructions. When the user invokes `/bb:<skill-name>`, the contents of that skill's `SKILL.md` are read into the conversation and Claude follows them.

Skills can reference other files (more markdown, JSON, examples, shell scripts etc.) that are useful or part of how the skill works, or that you want to be able to iterate and commit to separately. See `bb/skills/dev-finish/summary.md` for an example.

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

The `description` is what Claude reads to decide whether to apply the skill. Write it specifically and end with the invocation phrase so the trigger is unambiguous.

### Naming

Skill names follow `<discipline>-<verb>`:

- `dev-*` — software development workflow
- `content-*` — content writing and review
- `security-*` — security related tasks and processes
- (add more disciplines as the team grows)

Names should describe an action the user is taking. `dev-plan`, `content-review`, `security-audit` — not `dev-planner`, `content-reviewing-tool`, `security-auditor`.

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
- The skill contains steps that will be relevant to everyone every time a task is carried out, and that we want to be consistent for the whole team

## Updating an existing skill

Same flow. When the PR merges to `main`, the change reaches all installed users at their next Claude Code startup via marketplace auto-update.
