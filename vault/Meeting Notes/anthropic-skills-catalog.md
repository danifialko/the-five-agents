# Anthropic Skills Catalog

## Overview
Skills installed at project scope from the official Anthropic skills repo, [anthropics/skills](https://github.com/anthropics/skills). Currently a single skill: **`skill-creator`** — for authoring, editing, evaluating, and benchmarking new skills. Installed via manual sparse-clone + `cp` because the `claude` CLI is not on PATH in this environment (the `claude plugin install` flow from the original 3-step request was unavailable).

## Open Questions
- none

## File-by-file reference

### `skill-creator/`
- **What it does:** Create new skills from scratch, edit/optimize existing ones, run evals, benchmark performance with variance analysis, and optimize skill descriptions for better triggering accuracy.
- **Source:** `anthropics/skills` → `skills/skill-creator/`.
- **Owner:** Anthropic (upstream).
- **Top-level files & folders:**
  - `SKILL.md` — primary instructions (the file Claude Code loads).
  - `LICENSE.txt` — upstream license.
  - `agents/` — sub-agent prompts used by the skill.
  - `assets/` — images, templates, and reference assets.
  - `eval-viewer/` — UI/scripts for viewing eval results.
  - `references/` — supplementary reference docs the skill cites.
  - `scripts/` — helper scripts the skill invokes (eval runners, etc.).
- **Total files:** 18.
- **Scope:** project (lives in `.claude/skills/skill-creator/`). A separate user-scoped copy exists as `anthropic-skills:skill-creator` and is unaffected.

## Session Log

### 2026-05-06 — install skill-creator at project scope [shipped]
- **What was done:** Sparse-cloned `anthropics/skills` to `/tmp` (cone-mode, only `skills/skill-creator`), copied the folder with no-clobber to `.claude/skills/skill-creator/`. Claude Code auto-discovered it — the skill list now shows both project-scoped `skill-creator` and user-scoped `anthropic-skills:skill-creator`.
- **Decisions:** Used the manual clone+copy path because `claude` is not in the user's PATH (steps 1–3 of the requested CLI flow all fail at step 0). Sparse-checkout in non-cone mode was needed because the file actually lives at `skills/skill-creator/` (nested) inside the repo.
- **Notes / Caveats:** No conflict with existing files — the destination directory didn't exist prior. Both copies of the skill are now visible to Claude; in-conversation invocation defaults to the unprefixed (project) one.
- **Related:** [[claude-folder-structure]], [[superpowers-skills-catalog]], [[obsidian-skills-catalog]]
