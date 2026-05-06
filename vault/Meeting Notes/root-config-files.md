# Root Config Files

## Overview
Top-level configuration files at the project root of **the-five-agents**. These set project guidance for Claude Code, declare environment variables, define git-ignore rules, and provide a template for local secrets. They are the first files any new contributor (or new Claude session) encounters.

## Open Questions
- none

## File-by-file reference

### `CLAUDE.md`
- **Purpose:** Project-level instructions for Claude Code. Describes the project as a content-creation agent team led by a "CEO" agent that orchestrates specialized sub-agents (to be defined later).
- **Audience:** Future Claude Code sessions opening this repo.
- **Contains:** Project Overview (Hebrew), Repository Layout (`.claude/agents`, `.claude/skills`, `.claude/commands`), Status (scaffolding only).
- **Tracked in git:** yes.
- **Related:** [[claude-folder-structure]]

### `.env`
- **Purpose:** Local environment variables — secrets and runtime config (currently `ANTHROPIC_API_KEY=`).
- **Audience:** the local machine only.
- **Tracked in git:** **NO** — gitignored. Must never be committed.
- **Related:** [[root-config-files#`.env.example`]], [[root-config-files#`.gitignore`]]

### `.env.example`
- **Purpose:** Committed template showing which environment variables are needed. Contributors copy it to `.env` and fill real values.
- **Contains:** `ANTHROPIC_API_KEY` placeholder, optional `ANTHROPIC_MODEL`, `LOG_LEVEL`.
- **Tracked in git:** yes.
- **Related:** [[root-config-files#`.env`]]

### `.gitignore`
- **Purpose:** Tells git which files/folders to skip. Critical for keeping `.env` out of version control.
- **Excludes:** `.env*` (except `.env.example`), `.DS_Store`, `Thumbs.db`, editor folders (`.vscode/`, `.idea/`), logs, Python (`__pycache__`, `.venv`), Node (`node_modules`, `dist`, `build`).
- **Tracked in git:** yes.
- **Related:** [[root-config-files#`.env`]]

## Session Log

### 2026-05-06 — initial inventory of root config files [shipped]
- **What was done:** Documented the four root-level files (`CLAUDE.md`, `.env`, `.env.example`, `.gitignore`) — purpose, audience, git-tracked status, and inter-relationships.
- **Decisions:** Use `@users.noreply.github.com` form for git identity to keep email private. Keep `.env` out of git via `.gitignore`. Keep CLAUDE.md minimal until project takes shape.
- **Notes / Caveats:** A GitHub PAT was leaked in chat earlier in the session and should be revoked at https://github.com/settings/tokens.
- **Related:** [[claude-folder-structure]], [[obsidian-vault-setup]]
