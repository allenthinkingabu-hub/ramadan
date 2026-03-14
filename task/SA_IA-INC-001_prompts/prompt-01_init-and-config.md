# Prompt 01 — Skill Initialization & Configuration Files

## Context

You are creating the **Project Structure Scan** AI Agent Skill (Task ID: SA-DISC-001). This is Step 1 of 5 in the skill generation process. The full requirements are defined in `task/SA_IA-INC-001_Project_Structure_Scan_agent_skill_definition.md`.

## Scope — Requirements 1 through 6

This prompt covers ONLY the following:
- Requirement 1: Trigger mechanisms
- Requirement 2: RACI matrix
- Requirement 3: Skills list
- Requirement 4: Knowledge base
- Requirement 5: Tools list
- Requirement 6: MCP tools list
- SKILL.md skeleton (frontmatter + structure outline)

## Instructions

### 1. Create the skill directory

Create the `project-structure-scan/` directory with subdirectories: `config/`, `templates/`, `references/`, `scripts/`, `memory/`, `logs/`, `research/`, `diagrams/`.

### 2. Create SKILL.md skeleton

Create `project-structure-scan/SKILL.md` with:

**Frontmatter**:
```yaml
---
name: project-structure-scan
description: "Interactive AI Agent skill for scanning and analyzing existing codebase project structures through structured iterative dialogue. Use when: (1) a project structure scan or code archaeology is needed on an existing system, (2) analyzing directory structure, module decomposition, and package dependencies, (3) identifying architectural layering patterns (MVC/DDD/Hexagonal/Clean Architecture/Layered/etc.), (4) PM Agent assigns task SA-DISC-001 via RACI matrix, (5) a new feature is being planned on an existing system and the current structure must be understood first, (6) producing project structure trees, module relationship diagrams, and dependency maps, or (7) conducting technical discovery on an unfamiliar codebase."
---
```

**Body skeleton** (section headers only, content will be filled by subsequent prompts):
```markdown
# Project Structure Scan Agent

Role: IT Architect (SA) | Task ID: SA-DISC-001 | Phase: Code Archaeology — Step 1.1

## Objective
## Upstream Inputs
## Downstream Triggers
## Workflow Overview
## Phase 0: Initialization & Project Intake
## Phase 1: Understand Task Purpose
## Phase 2: Understand the Target Project
## Phase 3: Research & Question Generation
## Phase 4: Execute & Produce Deliverables
## Phase 5: Completion & Handoff
## Memory Utilization Protocol
## Logging Requirements
## Reference Files
```

### 3. Create config/triggers.md

Research and produce a comprehensive trigger mechanisms file. Content must include:

- **Trigger events**: What events cause this skill to be invoked (e.g., PM Agent assigns SA-DISC-001, new feature request on existing system, architecture discovery phase initiated, manual invocation by architect)
- **Trigger format**: How the trigger is communicated (e.g., RACI matrix task assignment, direct user command, upstream task completion)
- **Pre-conditions**: What must be true before the trigger fires (link to DoR)
- **Trigger parameters**: What information is passed with the trigger (e.g., project path, scan scope, purpose description)
- **Project Intake Questions**: If trigger parameters are incomplete, the agent MUST interactively ask the user before proceeding. See Section 2.1 below.

Use a structured table format. Make it configurable — each trigger should be an editable entry.

### 2.1 Project Intake — Required Information Collection

**CRITICAL**: Before any scanning begins, the agent MUST collect the following project information from the user. If any item is not provided via trigger parameters, the agent MUST ask the user interactively.

Include this section in `config/triggers.md` as a **Project Intake Checklist**:

| # | Information | Required | How to Ask | Validation |
|---|-------------|:--------:|------------|------------|
| 1 | **Project local path** | ✅ Yes | "What is the local file path of the project you want me to scan? (e.g., `/Users/you/projects/my-app`)" | Path exists, is a directory, contains files |
| 2 | **Git repository URL** | ⬜ Optional | "Is this project in a Git repository? If so, what is the remote URL? (e.g., `https://github.com/org/repo`)" | Valid URL format or "N/A" |
| 3 | **Git branch** | ⬜ Optional | "Which branch should I scan? (default: current branch)" | Branch exists in the repo |
| 4 | **Project name** | ✅ Yes | "What is the project name? (I can infer from the directory name if you prefer)" | Non-empty string |
| 5 | **Scan scope** | ✅ Yes | "Should I scan the entire project, or focus on specific modules/directories?" Options: (a) Full project scan (b) Specific directories only (c) Exclude certain directories | One of: full / partial / exclude-list |
| 6 | **Directories to exclude** | ⬜ Conditional | Only if scan scope = partial or exclude-list: "Which directories should I exclude? (e.g., `node_modules`, `vendor`, `.git`, `build`)" | Valid directory names |
| 7 | **Scan purpose** | ✅ Yes | "Why do you need this project structure scan? (e.g., planning a new feature, onboarding to an existing project, preparing for architecture review)" | Non-empty string |

**Agent Behavior**:
1. On startup, check which items are already provided via trigger parameters.
2. For each missing REQUIRED item, ask the user using the "How to Ask" prompt.
3. For each missing OPTIONAL item, ask only if contextually relevant (e.g., don't ask Git URL if user says it's not a Git project).
4. After collecting all items, validate each one:
   - **Project local path**: Run `ls {path}` to verify it exists and is accessible.
   - **Git info**: If provided, run `git -C {path} status` to verify it's a valid repo.
   - **Scan scope**: If "partial", confirm the specified directories exist under the project path.
5. Present a **Project Intake Summary** for user confirmation:
   ```
   📋 Project Intake Summary:
   - Project Name: {name}
   - Local Path: {path}
   - Git Remote: {url} (branch: {branch})
   - Scan Scope: {scope}
   - Exclusions: {exclusion_list}
   - Purpose: {purpose}

   Is this correct? (yes / no — I'll ask again for any corrections)
   ```
6. Store confirmed intake in SQLite `scan_history` table (via `memory_ops.start_scan()`).
7. Store project info in `knowledge_base` table for future re-invocations.
8. Only proceed to Phase 1 after user confirms the intake summary.

### 4. Create config/raci.md

Research and produce the RACI matrix for the Project Structure Scan task. Must include:

| Role | Task | R/A/C/I |
|------|------|---------|

Roles to include (at minimum):
- IT Architect (SA) — the agent executing this task
- Solutions Architect — upstream input provider
- Technical Lead — downstream consumer of scan results
- Project Manager — task coordinator and trigger manager
- Development Team — informed of scan results
- Enterprise Architect — consulted on architecture pattern decisions

Tasks to include (at minimum):
- Initiate project structure scan
- Define scan scope and requirements
- Execute codebase scanning
- Produce structure tree (OUT-01)
- Produce module relationship diagram (OUT-02)
- Produce layering pattern analysis (OUT-03)
- Produce package dependency map (OUT-04)
- Produce module responsibility summary (OUT-05)
- Produce final scan report (OUT-06)
- Review and approve scan results
- Trigger downstream tasks

Include a section explaining how PM Agent uses this matrix to trigger downstream tasks after completion.

### 5. Create config/skills-and-knowledge.md

Research and produce a combined skills + knowledge base file. Two sections:

**Skills Section** — capabilities the agent must possess:
- Directory structure analysis and traversal
- Build system recognition (Maven/Gradle/npm/pip/cargo/go.mod/etc.)
- Module boundary identification
- Dependency graph construction (internal and external)
- Architectural pattern recognition (MVC/MVP/MVVM/DDD/Hexagonal/Clean/Onion/Layered/Microservices)
- Code convention detection (naming patterns, package organization)
- Configuration analysis (env files, config classes, feature flags)
- Multi-language project navigation
- Monorepo structure recognition

**Knowledge Base Section** — knowledge domains the agent must draw from:
- Software architecture patterns and styles (with brief descriptions of each)
- Module decomposition principles (cohesion, coupling, separation of concerns)
- SOLID principles and their structural implications
- Package-by-feature vs. package-by-layer organization
- Build tool conventions per language ecosystem
- Dependency management strategies
- Common project structure conventions per framework (Spring Boot, Django, Rails, Next.js, etc.)

### 6. Create config/tools.md

Research and produce the tools list. For each tool:

| Tool | Purpose | Usage Example |
|------|---------|---------------|

Tools to include:
- **Glob**: File pattern matching for directory discovery
- **Grep**: Content search for pattern identification (imports, annotations, decorators)
- **Read**: File reading for build files, config files, entry points
- **Bash**: System commands — `tree`, `wc -l`, `find`, dependency analysis commands
- **Bash (language-specific)**: `mvn dependency:tree`, `npm ls`, `pip list`, `go mod graph`, `cargo tree`, etc.

### 7. Create config/mcp-tools.md

Research and produce the MCP tools list:

| MCP Tool | Purpose | When to Use |
|----------|---------|-------------|

MCP tools to include:
- **IDE Diagnostics** (`mcp__ide__getDiagnostics`): Get language diagnostics for code quality signals
- **Context7 Resolve Library** (`mcp__plugin_context7_context7__resolve-library-id`): Look up documentation for identified dependencies
- **Context7 Query Docs** (`mcp__plugin_context7_context7__query-docs`): Query framework/library documentation to understand conventions

## Validation Checklist

After completing all files, verify:
- [ ] `project-structure-scan/` directory exists with all subdirectories
- [ ] `SKILL.md` exists with valid YAML frontmatter (name + description)
- [ ] `config/triggers.md` exists with at least 3 trigger definitions
- [ ] `config/raci.md` exists with at least 6 roles and 10 tasks
- [ ] `config/skills-and-knowledge.md` exists with skills section (9+ items) and knowledge section (7+ items)
- [ ] `config/tools.md` exists with at least 5 tools
- [ ] `config/mcp-tools.md` exists with at least 3 MCP tools

If any item fails, fix it before reporting completion.
