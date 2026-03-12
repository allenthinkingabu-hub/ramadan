# Trigger Mechanisms — Project Structure Scan (SA-DISC-001)

## Trigger Events

| # | Trigger Event | Source | Format | Priority |
|---|---------------|--------|--------|----------|
| 1 | PM Agent assigns SA-DISC-001 | RACI matrix task assignment | Structured JSON/message with task ID, project path, scope | High |
| 2 | New feature request on existing system | Feature request pipeline | Feature ticket with target system reference | Medium |
| 3 | Architecture discovery phase initiated | Sprint/phase planning | Phase kickoff notification | High |
| 4 | Manual invocation by architect | Direct user command | CLI invocation or chat command | Medium |
| 5 | Upstream task completion (e.g., project onboarding) | Upstream agent signal | Completion notification with project context | Medium |
| 6 | Code review or audit request requiring structure understanding | Quality/compliance process | Audit request with scope | Low |

## Trigger Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|---------|
| project_path | ✅ | Local filesystem path to the target project | `/Users/dev/projects/my-app` |
| project_name | ⬜ | Human-readable project name (can infer from path) | `my-app` |
| scan_scope | ⬜ | full / partial / exclude-list (default: full) | `full` |
| scan_purpose | ⬜ | Why this scan is needed | `Planning new auth module` |
| git_url | ⬜ | Git remote URL | `https://github.com/org/repo` |
| git_branch | ⬜ | Branch to scan (default: current) | `main` |
| exclude_dirs | ⬜ | Comma-separated directories to exclude | `node_modules,vendor,.git` |

## Pre-conditions

Before any trigger fires, the following must be true (see `references/dor.md` for full DoR):
- Target codebase is accessible at the specified path
- Read permissions are available for project files
- At least one build/manifest file exists
- Output directory is writable

---

## Project Intake Checklist

**CRITICAL**: Before any scanning begins, the agent MUST collect the following information. If any item is not provided via trigger parameters, the agent MUST ask the user interactively.

| # | Information | Required | How to Ask | Validation |
|---|-------------|:--------:|------------|------------|
| 1 | **Project local path** | ✅ Yes | "What is the local file path of the project you want me to scan? (e.g., `/Users/you/projects/my-app`)" | Path exists, is a directory, contains files |
| 2 | **Git repository URL** | ⬜ Optional | "Is this project in a Git repository? If so, what is the remote URL? (e.g., `https://github.com/org/repo`)" | Valid URL format or "N/A" |
| 3 | **Git branch** | ⬜ Optional | "Which branch should I scan? (default: current branch)" | Branch exists in the repo |
| 4 | **Project name** | ✅ Yes | "What is the project name? (I can infer from the directory name if you prefer)" | Non-empty string |
| 5 | **Scan scope** | ✅ Yes | "Should I scan the entire project, or focus on specific modules/directories?" Options: (a) Full project scan (b) Specific directories only (c) Exclude certain directories | One of: full / partial / exclude-list |
| 6 | **Directories to exclude** | ⬜ Conditional | Only if scan scope = partial or exclude-list: "Which directories should I exclude? (e.g., `node_modules`, `vendor`, `.git`, `build`)" | Valid directory names |
| 7 | **Scan purpose** | ✅ Yes | "Why do you need this project structure scan? (e.g., planning a new feature, onboarding to an existing project, preparing for architecture review)" | Non-empty string |

## Agent Behavior

1. On startup, check which items are already provided via trigger parameters.
2. For each missing REQUIRED item, ask the user using the "How to Ask" prompt.
3. For each missing OPTIONAL item, ask only if contextually relevant (e.g., don't ask Git URL if user says it's not a Git project).
4. After collecting all items, validate each one:
   - **Project local path**: Run `ls {path}` to verify it exists and is accessible.
   - **Git info**: If provided, run `git -C {path} status` to verify it's a valid repo.
   - **Git branch**: If provided, run `git -C {path} branch --list {branch}` to verify.
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
7. Store project info in `knowledge_base` table for future re-invocations (via `memory_ops.record_knowledge()`).
8. Only proceed to Phase 1 after user confirms the intake summary.
