# Obsidian Skills Catalog

## Overview
Three Obsidian-related skills installed by the user under `.claude/skills/`. They govern how Claude Code reads from and writes to the project vault, how it formats Obsidian Flavored Markdown (wikilinks, callouts, frontmatter), and how it works with Obsidian Bases (database-like views). The most important of the three — **`obsidian-vault-workflow`** — defines the mandatory protocol for reading topic files at task start and appending dated session entries at task end.

## Open Questions
- none

## File-by-file reference

### `obsidian-bases/`
- **What it does:** Create and edit Obsidian Bases (`.base` files) — views, filters, formulas, summaries. Use when working with `.base` files or building database-like views of notes.
- **Files:** `SKILL.md` only.
- **Owner:** user (manually installed).

### `obsidian-markdown/`
- **What it does:** Create and edit Obsidian Flavored Markdown — wikilinks, embeds, callouts, properties, frontmatter, tags. Use for any `.md` files inside an Obsidian vault.
- **Files:** `SKILL.md` only.
- **Owner:** user.

### `obsidian-vault-workflow/`
- **What it does:** Enforces the mandatory vault read/write protocol — read the topic file (Overview + Open Questions + Session Log) at task start, append a dated session entry at task end. Defines folder conventions (`Meeting Notes/`, `Content Briefs/`, `Publishing Log/`, `Brand Guidelines/`), the topic-file template, status tags (`[shipped|spiked|wip|reverted|planned|debug]`), and `_index.md` requirements.
- **Files:** `SKILL.md` only.
- **Owner:** user.
- **Critical:** This skill drives the structure of every other note in this vault.

## Session Log

### 2026-05-06 — first vault session under the new workflow [shipped]
- **What was done:** Documented the three Obsidian skills. Created the initial vault structure (`vault/_index.md`, `vault/Meeting Notes/_index.md`) and five inventory topic files.
- **Decisions:** Treat `obsidian-vault-workflow` as the primary discipline for all future sessions. The other two skills (`obsidian-bases`, `obsidian-markdown`) are utilities loaded by content/format need.
- **Notes / Caveats:** These three skills are not yet committed/pushed. The user wants the workflow auto-loaded every session — that needs a hook (see Open Questions).
- **Related:** [[claude-folder-structure]], [[obsidian-vault-setup]], [[superpowers-skills-catalog]]

### 2026-05-06 — SessionStart hook + push to GitHub [shipped]
- **What was done:** Created `.claude/settings.json` with a `SessionStart` hook that emits `hookSpecificOutput.additionalContext` reminding Claude to invoke the obsidian-vault-workflow skill before any task. Committed everything (3 obsidian skills, vault scaffolding, hook config, .obsidian/ config) as `0e345f6` and pushed to `origin/main`.
- **Decisions:** Chose `SessionStart` over `UserPromptSubmit` — fires once per session (less noisy) and is enough to anchor the workflow. Used `echo`-based command (no jq/python/node needed; portable on the user's Windows + Git Bash setup).
- **Notes / Caveats:** The hook fires at session start, but Claude Code only watches `.claude/settings.json` for changes if it existed when the session started. First activation may require opening `/hooks` once or restarting Claude Code. Verified the JSON structure by Read-back.
- **Related:** [[claude-folder-structure]], [[obsidian-vault-setup]]
