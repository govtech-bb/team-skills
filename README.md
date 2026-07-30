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
| `/bb:standup` | You want a bulleted recap of what you've shipped since your last standup, ready to read aloud |
| `/bb:govtech-service-content` | You're building, reviewing, auditing or preparing GovTech service content — pages, forms, confirmation screens, MDA pages — and want content-design guidance plus a QA gate |
| `/bb:product-shape` | A prototype has to become a real service and you need it shaped first — give it the project history and the prototype URL, get a delivery document plus a one-page artifact covering what the platform already expresses, the custom features required and their MVP fallbacks, and the phase order |

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add new ones.

## How this is laid out

```
.claude-plugin/marketplace.json   ← makes this repo a Claude Code marketplace
bb/
  .claude-plugin/plugin.json      ← the single plugin shipped from this marketplace
  skills/
    dev-plan/SKILL.md
    dev-start/SKILL.md
    dev-finish/
      SKILL.md
      summary.md                  ← referenced helper file; independently iterable
    standup/SKILL.md
    govtech-service-content/
      SKILL.md
      MODULE-CONTRACTS.md         ← module ownership map
      references/                 ← 13 pattern & QA reference files
      assets/                     ← handover & MDA-question templates
    product-shape/
      SKILL.md
      assets/
        product-shape-template.md        ← the markdown output contract
        artifact-template.html           ← the one-page artifact's design
        render-flow.py                   ← mermaid → theme-paired inline SVG
README.md
CONTRIBUTING.md
```

One plugin (`bb`) holds all the skills. Skills are invoked as `/bb:<skill-name>` — the `bb:` prefix is Claude Code's plugin namespace, and the `dev-` / `content-` / `security-` part inside the skill name marks the discipline.

## Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md).
