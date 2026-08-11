# Shared Claude Code skills for GovTech Barbados

These skills give the team a common scaffold for everyday work — planning a change, starting a coding session, finishing one — without prescribing any single workflow. Each discipline (dev, ops, sec, …) contributes skills under one shared namespace.

This repo is the team's single marketplace. It ships two plugins:

| Plugin | Holds | Lives in |
|---|---|---|
| `bb` | How we work — process and workflow, whatever you're building | This repo |
| `govbb` | How to build with the GovBB Design System | The [design system repo](https://github.com/govtech-bb/govbb-design-system), referenced from here |

## Install

First, add the team-skills repo as a marketplace:

```
/plugin marketplace add govtech-bb/team-skills
```

Then install the plugins you want:

```
/plugin install bb@team-skills
/plugin install govbb@team-skills
```

Restart Claude Code, or run `/reload-plugins`. The skills are now available as `/bb:<name>` and `/govbb:<name>`.

Updates auto-propagate: when a PR merges to `main`, Claude Code picks up the new version at the next startup. That applies to `govbb` too — its source is the design system repo, so a merge there reaches you without any change here.

If you already had this marketplace before `govbb` existed, run `/plugin marketplace update team-skills` first. Auto-update covers new versions of a plugin, not the appearance of a new one.

## What's here

| Skill | Use it when |
|---|---|
| `/bb:dev-plan` | You're about to change code and want to think the approach through before writing any |
| `/bb:dev-start` | You're sitting down to a known change and want to ground the session before coding |
| `/bb:dev-finish` | You're ready to wrap up — tests, docs, decisions worth recording, commit |
| `/bb:standup` | You want a bulleted recap of what you've shipped since your last standup, ready to read aloud |
| `/bb:govtech-service-content` | You're building, reviewing, auditing or preparing GovTech service content — pages, forms, confirmation screens, MDA pages — and want content-design guidance plus a QA gate |
| `/govbb:accessibility-review` | You want a page, component or service checked against WCAG 2.2 AA and the design system's own accessibility contracts, before it goes live |

`bb:` skills are documented here. `govbb:` skills are documented in the [design system repo](https://github.com/govtech-bb/govbb-design-system/tree/main/skills) and on the [design system site](https://design-system.service.alpha.gov.bb/ai-skills/) — this table lists them so there is one place to look, but it is not where they are maintained.

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add new ones.

## How this is laid out

```
.claude-plugin/marketplace.json   ← makes this repo a Claude Code marketplace;
                                    lists `bb` (below) and `govbb` (another repo)
bb/
  .claude-plugin/plugin.json      ← the plugin whose skills live in this repo
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
README.md
CONTRIBUTING.md
```

The `bb` plugin holds every skill kept in this repo. Skills are invoked as `/bb:<skill-name>` — the `bb:` prefix is Claude Code's plugin namespace, and the `dev-` / `content-` / `security-` part inside the skill name marks the discipline.

The `govbb` plugin has no directory here. Its marketplace entry uses a `git-subdir` source pointing at the `skills/` directory of the design system repo, so this repo carries a pointer and never a copy. Nothing to sync, and nothing here goes stale when a design-system skill changes.

That split is deliberate. Design-system skills describe the system as it is now — which components exist, what each guarantees — so they have to change in the same pull request as the system itself. Keeping them in the design system repo is what makes that possible; keeping the catalogue here is what keeps one marketplace for the team.

## Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md).
