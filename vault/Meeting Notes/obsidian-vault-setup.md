# Obsidian Vault Setup

## Overview
The project uses an Obsidian vault rooted at `vault/` as long-term memory for Claude Code sessions, following the **obsidian-vault-workflow** skill. The `.obsidian/` directory holds Obsidian's per-vault configuration. The vault stores topic-based Meeting Notes, Content Briefs, Publishing Log entries, and Brand Guidelines — created on first use.

## Open Questions
- Should `.obsidian/workspace.json` be gitignored? It tracks per-machine UI state (open panels, last viewed file) and tends to churn.

## File-by-file reference

### `.obsidian/app.json`
- **Purpose:** Core Obsidian app preferences for this vault (e.g. attachment folder, default view).
- **Owner:** Obsidian (auto-generated when the vault is opened).
- **Tracked in git:** yes (currently).

### `.obsidian/appearance.json`
- **Purpose:** Theme, font, accent color settings.
- **Owner:** Obsidian.
- **Tracked in git:** yes.

### `.obsidian/core-plugins.json`
- **Purpose:** Lists which built-in Obsidian plugins are enabled in this vault.
- **Owner:** Obsidian.
- **Tracked in git:** yes.

### `.obsidian/workspace.json`
- **Purpose:** Per-machine workspace state (open tabs, panel layout). Changes frequently.
- **Owner:** Obsidian.
- **Tracked in git:** yes — but a candidate for gitignore.

### `vault/_index.md`
- **Purpose:** Vault-root index linking to all top-level folders.
- **Audience:** Future Claude sessions navigating the vault.
- **Related:** [[_index]]

### `vault/Meeting Notes/`
- **Purpose:** Topic notes for code, architecture, design decisions, and file inventories. Each `.md` follows the Overview → Open Questions → Session Log format.
- **Index:** `vault/Meeting Notes/_index.md`

### `vault/Content Briefs/` *(not yet created)*
- **Purpose:** Editorial briefs and campaign specs.
- **Will be created on first use.**

### `vault/Publishing Log/` *(not yet created)*
- **Purpose:** Publish runs, outcomes, post-mortems.
- **Will be created on first use.**

### `vault/Brand Guidelines/` *(not yet created)*
- **Purpose:** Voice, visuals, tone, UI primitives.
- **Will be created on first use.**

## Session Log

### 2026-05-06 — vault scaffolding and first inventory [shipped]
- **What was done:** Created `vault/_index.md` and `vault/Meeting Notes/_index.md`. Documented the four `.obsidian/` config files and the planned vault folder layout.
- **Decisions:** Follow the obsidian-vault-workflow skill verbatim — one file per topic, dated session entries appended at the bottom, `[[wikilinks]]` for cross-references.
- **Notes / Caveats:** `Content Briefs/`, `Publishing Log/`, `Brand Guidelines/` will be created lazily when first needed (skill says directories are auto-created by Write).
- **Related:** [[root-config-files]], [[obsidian-skills-catalog]]
