# Meeting Notes — Index

Code, architecture, decisions, and file-inventory notes for **the-five-agents**.

## Topics

- [[root-config-files]] — top-level project files (`CLAUDE.md`, `.env`, `.env.example`, `.gitignore`)
- [[obsidian-vault-setup]] — `.obsidian/` config and `vault/` structure
- [[claude-folder-structure]] — `.claude/` layout (agents, commands, skills) and customization conventions
- [[superpowers-skills-catalog]] — 14 skills installed from `obra/superpowers`
- [[obsidian-skills-catalog]] — 3 Obsidian-related skills (`obsidian-bases`, `obsidian-markdown`, `obsidian-vault-workflow`)
- [[anthropic-skills-catalog]] — official Anthropic skills installed at project scope (`skill-creator`)
- [[enzo-ceo-agent]] — Enzo, the CEO agent (orchestrator + QC, project entry point)
- [[forlan-creative-agent]] — Forlan, the creative / image-generation agent (hybrid `.claude/agents/forlan.md` + `forlan/` workspace)
- [[gpt-image-gen-skill]] — wrapper around OpenAI Images API (`gpt-image-2`); shared by all agents that need to generate images
- [[cavani-content-agent]] — Cavani (קבי), the content writer / rewriter agent (LLM-only: Read/Write/Edit/Glob/Grep)
- [[suarez-research-agent]] — Suarez, the web research agent (WebSearch/WebFetch + search memory log to prevent duplicate searches)
