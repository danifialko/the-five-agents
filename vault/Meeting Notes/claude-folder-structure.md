# `.claude/` Folder Structure

## Overview
The `.claude/` directory holds project-specific customizations for Claude Code: subagents, skills, and slash commands. The convention follows Claude Code's standard layout — anything under `.claude/agents`, `.claude/skills`, or `.claude/commands` is auto-discovered by Claude Code when working in this repo. All three subdirectories were created during initial scaffolding and seeded with `.gitkeep` files so git would track the empty structure.

## Open Questions
- The `agents/` and `commands/` directories are still empty. Will the "CEO" main agent and team be defined as subagents under `agents/`, or as a different mechanism?

## File-by-file reference

### `.claude/agents/`
- **Purpose:** Project-specific subagents. Each agent is a `.md` file describing the agent's role, tools, and behavior.
- **Status:** empty (only `.gitkeep`). The "CEO" agent and the content-team sub-agents will live here once defined.
- **Owner:** project maintainers.

### `.claude/agents/.gitkeep`
- **Purpose:** Empty marker so git tracks the otherwise-empty directory.
- **Tracked in git:** yes.

### `.claude/commands/`
- **Purpose:** Project-specific slash commands. Each is a `.md` file invoked as `/command-name`.
- **Status:** empty (only `.gitkeep`).
- **Owner:** project maintainers.

### `.claude/commands/.gitkeep`
- **Purpose:** Directory placeholder for git.
- **Tracked in git:** yes.

### `.claude/skills/`
- **Purpose:** Project-specific skills (capability bundles loaded by name). Each skill is a folder containing `SKILL.md` plus optional helper files.
- **Status:** populated. Currently holds 14 skills from `obra/superpowers` and 3 user-installed Obsidian skills.
- **Detail:** see [[superpowers-skills-catalog]], [[obsidian-skills-catalog]], and [[anthropic-skills-catalog]].

### `.claude/skills/.gitkeep`
- **Purpose:** Original placeholder from initial scaffolding. Now redundant since the directory has real content, but harmless.
- **Tracked in git:** yes.

## Session Log

### 2026-05-06 — initial scaffolding [shipped]
- **What was done:** Created `.claude/{agents,skills,commands}/` with `.gitkeep` files. Documented the layout in `CLAUDE.md`. Pushed to `origin/main` (commit `ad09f19`).
- **Decisions:** Use `.gitkeep` to track empty directories rather than leaving them out of git.
- **Related:** [[root-config-files]]

### 2026-05-06 — superpowers and obsidian skills installed [shipped]
- **What was done:** Manually copied 14 skills from `obra/superpowers` into `.claude/skills/` (commit `366f5bf`). Three Obsidian-related skills (`obsidian-bases`, `obsidian-markdown`, `obsidian-vault-workflow`) were added separately by the user.
- **Decisions:** Manual `git clone` + `cp -rn` (no-clobber) instead of `claude /plugin install`, since the plugin command isn't available in the user's environment.
- **Notes / Caveats:** `agents/` and `commands/` remain empty pending definition of the agent team. The 3 Obsidian skills are local-only — not yet pushed.
- **Related:** [[superpowers-skills-catalog]], [[obsidian-skills-catalog]]
