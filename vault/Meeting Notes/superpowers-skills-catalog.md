# Superpowers Skills Catalog

## Overview
14 skills installed from [obra/superpowers](https://github.com/obra/superpowers) into `.claude/skills/`. They cover engineering disciplines — TDD, debugging, code review, planning, brainstorming, parallel agent dispatch, and worktree-based isolation. Each skill is a folder containing a `SKILL.md` (the instructions Claude loads) plus optional reference files, prompts, scripts, and examples. They were copied manually with `cp -rn` so existing files were preserved.

## Open Questions
- Are all 14 skills relevant to a content-creation agent team, or should some be pruned (e.g. `using-git-worktrees`, `test-driven-development` may be dev-centric)?

## File-by-file reference

Each skill below is a folder under `.claude/skills/`. The owner of every file in this section is the upstream `obra/superpowers` repo.

### `brainstorming/`
- **What it does:** Mandatory before any creative work — explores user intent, requirements, and design before implementation.
- **Files:** `SKILL.md`, `spec-document-reviewer-prompt.md`, `visual-companion.md`, `scripts/{frame-template.html, helper.js, server.cjs, start-server.sh, stop-server.sh}`.

### `dispatching-parallel-agents/`
- **What it does:** Use when facing 2+ independent tasks that can be worked without shared state.
- **Files:** `SKILL.md`.

### `executing-plans/`
- **What it does:** Use when you have a written implementation plan to execute in a separate session with review checkpoints.
- **Files:** `SKILL.md`.

### `finishing-a-development-branch/`
- **What it does:** Guides completion of dev work — merge, PR, or cleanup decisions.
- **Files:** `SKILL.md`.

### `receiving-code-review/`
- **What it does:** Discipline for handling code review feedback — verify before agreeing.
- **Files:** `SKILL.md`.

### `requesting-code-review/`
- **What it does:** Verify completed work meets requirements, before merging.
- **Files:** `SKILL.md`, `code-reviewer.md`.

### `subagent-driven-development/`
- **What it does:** Execute implementation plans with independent tasks in the current session.
- **Files:** `SKILL.md`, `code-quality-reviewer-prompt.md`, `implementer-prompt.md`, `spec-reviewer-prompt.md`.

### `systematic-debugging/`
- **What it does:** Required method for any bug, test failure, or unexpected behavior — diagnose before fixing.
- **Files:** `SKILL.md`, `CREATION-LOG.md`, `condition-based-waiting{.md,-example.ts}`, `defense-in-depth.md`, `find-polluter.sh`, `root-cause-tracing.md`, `test-academic.md`, `test-pressure-{1,2,3}.md`.

### `test-driven-development/`
- **What it does:** Use before writing implementation code — tests first.
- **Files:** `SKILL.md`, `testing-anti-patterns.md`.

### `using-git-worktrees/`
- **What it does:** Isolated workspaces via git worktree for feature work.
- **Files:** `SKILL.md`.

### `using-superpowers/`
- **What it does:** Required at conversation start — establishes how to find and use skills.
- **Files:** `SKILL.md`, `references/{codex-tools.md, copilot-tools.md, gemini-tools.md}`.

### `verification-before-completion/`
- **What it does:** Run verification commands and confirm output before claiming work is done.
- **Files:** `SKILL.md`.

### `writing-plans/`
- **What it does:** Required before touching code on multi-step tasks — produces an implementation plan.
- **Files:** `SKILL.md`, `plan-document-reviewer-prompt.md`.

### `writing-skills/`
- **What it does:** Use when creating, editing, or testing skills.
- **Files:** `SKILL.md`, `anthropic-best-practices.md`, `examples/CLAUDE_MD_TESTING.md`, `graphviz-conventions.dot`, `persuasion-principles.md`, `render-graphs.js`, `testing-skills-with-subagents.md`.

## Session Log

### 2026-05-06 — superpowers installation [shipped]
- **What was done:** Cloned `obra/superpowers` to `/tmp`, copied `skills/*` into `.claude/skills/` with `cp -rn` (no overwrite). Committed as `366f5bf` and pushed to `origin/main`. Documented all 14 skills and their files here.
- **Decisions:** Manual install via `git clone` + `cp` because `claude /plugin install` is not available in this environment. No `commands/` or `agents/` directories exist in upstream, so only `skills/` was copied.
- **Notes / Caveats:** Skills do not auto-trigger across all sessions unless the harness loads them via `using-superpowers` or hooks. Some skills (TDD, worktrees) are dev-oriented and may be irrelevant for the content-team direction.
- **Related:** [[claude-folder-structure]], [[obsidian-skills-catalog]]
