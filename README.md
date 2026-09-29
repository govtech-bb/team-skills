# Shared Claude Code skills for GovTech Barbados

These skills give the team a common scaffold for everyday work — planning a change, starting a coding session, finishing one — without prescribing any single workflow. Each discipline (dev, ops, sec, …) contributes skills under one shared namespace.

## Install

First, add the team-skills repo as a marketplace:

```
/plugin marketplace add govtech-bb/team-skills
```

Then install the bb skills plugin:

```
/plugin install bb@team-skills
```

Restart Claude Code, or run `/reload-plugins`. The skills are now available as `/bb:<name>`.

Updates auto-propagate: when a PR merges to `main`, Claude Code picks up the new version at the next startup.

## What's here

| Skill | Use it when |
|---|---|
| `/bb:dev-plan` | You're about to change code and want to think the approach through before writing any |
| `/bb:dev-start` | You're sitting down to a known change and want to ground the session before coding |
| `/bb:dev-finish` | You're ready to wrap up — tests, docs, decisions worth recording, commit |
| `/bb:dev-review` | You're reviewing a PR (or relaying `/code-review` findings) and want every finding verified against the PR's head commit, then posted as one review |
| `/bb:standup` | You want a bulleted recap of what you've shipped since your last standup, ready to read aloud |
| `/bb:govtech-service-content` | You're building, reviewing, auditing or preparing GovTech service content — pages, forms, confirmation screens, MDA pages — and want content-design guidance plus a QA gate |

| Agent | Use it when |
|---|---|
| `bb:dev-reviewer` | Dispatched by `/bb:dev-review` to review one PR at pinned commits and return a draft review, e.g. one per PR when reviewing several at once. It never posts |

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add new ones.

## How this is laid out

```
.claude-plugin/marketplace.json   ← makes this repo a Claude Code marketplace
bb/
  .claude-plugin/plugin.json      ← the single plugin shipped from this marketplace
  agents/
    dev-reviewer.md               ← subagent dispatched by dev-review
  skills/
    dev-plan/SKILL.md
    dev-start/SKILL.md
    dev-finish/
      SKILL.md
      summary.md                  ← referenced helper file; independently iterable
    dev-review/
      SKILL.md
      references/worked-examples.md
    standup/SKILL.md
    govtech-service-content/
      SKILL.md
      MODULE-CONTRACTS.md         ← module ownership map
      references/                 ← 13 pattern & QA reference files
      assets/                     ← handover & MDA-question templates
README.md
CONTRIBUTING.md
```

One plugin (`bb`) holds all the skills and agents. Skills are invoked as `/bb:<skill-name>` — the `bb:` prefix is Claude Code's plugin namespace, and the `dev-` / `content-` / `security-` part inside the skill name marks the discipline.

## Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md).
