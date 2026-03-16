---
name: project-structure-scan
description: "Interactive AI Agent skill for scanning and analyzing existing codebase project structures through structured iterative dialogue. Use when: (1) a project structure scan or code archaeology is needed on an existing system, (2) analyzing directory structure, module decomposition, and package dependencies, (3) identifying architectural layering patterns (MVC/DDD/Hexagonal/Clean Architecture/Layered/etc.), (4) PM Agent assigns task SA-DISC-001 via RACI matrix, (5) a new feature is being planned on an existing system and the current structure must be understood first, (6) producing project structure trees, module relationship diagrams, and dependency maps, or (7) conducting technical discovery on an unfamiliar codebase."
---

# Project Structure Scan Agent

Role: IT Architect (SA) | Task ID: SA-DISC-001 | Phase: Code Archaeology — Step 1.1

## Objective

Produce a comprehensive project structure analysis for an existing codebase, covering directory hierarchy, module decomposition, architectural patterns, dependency mapping, and module responsibilities. Deliver 6 standard output deliverables (OUT-01 through OUT-06) and, when the scan purpose involves transformation/refactoring, a 7th conditional deliverable (OUT-07: Transformation Target Current State Report). All diagrams are produced in draw.io format (`.drawio` files).

## Upstream Inputs

- PM Agent task assignment (SA-DISC-001 via RACI matrix)
- Target project path (collected via Project Intake if not provided)
- Git repository URL and branch (optional, collected via Project Intake)
- Scan purpose description (collected via Project Intake if not provided)
- Scan scope (full / partial / specific modules, collected via Project Intake)

## Downstream Triggers

Upon completion, PM Agent triggers:
- Step 1.2: Technology Stack Inventory
- Step 1.3: Entry-Point Tracing
- Step 1.4: Data Model Analysis
- Step 1.5: Configuration & Environments
- Step 2: Architecture Recovery (once all Step 1.x complete)

See `config/raci.md` for the full RACI matrix used to trigger downstream tasks.

## Workflow Overview

```
Phase 0: Initialization & Project Intake
  → Verify DoR → collect project info (path/git/scope/purpose) → user confirms intake
  → create output dir → init memory DB → load history → determine scan mode

Phase 1: Understand Task Purpose (Interactive + Memory-Enhanced)
  → Load previous purpose if exists → present understanding → user confirms → log

Phase 2: Understand Target Project (Interactive + Memory-Accelerated)
  → Load known tech stack if exists → pre-fill answers → ask delta questions → user confirms → log

Phase 3: Research & Question Generation (Interactive + Memory-Informed)
  → Load previous research if exists → skip known areas → focus on gaps
  → generate questions → dialogue → validated requirements

Phase 4: Execute & Produce Deliverables (Memory-Optimized)
  → Determine scan strategy (full/incremental) → scan codebase
  → produce OUT-01~06 + draw.io diagrams → record findings → DoD self-verify

Phase 5: Transformation Target Deep-Dive Investigation (Conditional)
  → Triggered when scan purpose involves transformation/refactoring
  → confirm target scope with user → deep-dive investigate current state
  → produce OUT-07 (core logic + data structures + draw.io sequence diagrams) → user confirms

Phase 6: Completion & Handoff
  → Trigger supervisor → remediate if needed → record lessons → notify PM → trigger downstream
```

---

## Phase 0: Initialization & Project Intake

### Part A — Project Intake (Interactive)

Before any scanning begins, collect target project information from the user. See `config/triggers.md` for the full Project Intake Checklist with 7 items.

**Steps**:
1. Check which items are already provided via trigger parameters.
2. For each missing **required** item, ask the user interactively:
   - **Project local path** (REQUIRED): validate with `ls {path}`
   - **Project name** (REQUIRED): can infer from directory name
   - **Scan scope** (REQUIRED): full / partial / exclude-list
   - **Scan purpose** (REQUIRED): why this scan is needed
3. For each missing **optional** item, ask only if contextually relevant:
   - **Git repository URL**: skip if user says not a Git project
   - **Git branch**: skip if no Git URL
   - **Directories to exclude**: only if scope is partial/exclude
4. Validate each collected item (path exists, git status succeeds, etc.).
5. Present **Project Intake Summary** for user confirmation:
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
6. If user rejects → re-ask corrected items. If confirms → proceed.

**Memory ops**:
- `memory_ops.start_scan()` — record scan in `scan_history`
- `memory_ops.record_knowledge()` — store project info for future sessions

### Part B — System Initialization

1. **Verify DoR**: Check all prerequisites in `references/dor.md`. If any fail, inform user and request resolution.
2. **Create output directory**: Set up the deliverables output path under the target project's parent directory.
3. **Initialize memory DB**: If `memory/agent_memory.db` does not exist, run `python scripts/init_memory.py`.
4. **Load project history**: Call `memory_ops.load_project_history()`.
   - If previous scans found → enter **Re-scan Mode**
   - If no history → check `memory_ops.get_similar_projects()` for cross-project knowledge
   - If no similar projects → enter **Fresh Scan Mode**
5. **Memory maintenance**: Call `memory_ops.apply_confidence_decay()` and `memory_ops.prune_low_confidence()`.

**Re-scan Mode**:
- Call `memory_ops.generate_memory_summary()`, present to user.
- Offer options: (a) Incremental scan, (b) Full re-scan, (c) Review and update previous findings.

**Fresh Scan Mode with Similar Projects**:
- Present pattern hypothesis from similar projects:
  ```
  "I've scanned similar projects before. Project X used DDD with Hexagonal architecture.
   Should I look for similar patterns here?"
  ```

**Success criteria**: DoR verified, memory initialized, scan mode determined.

---

## Phase 1: Understand Task Purpose

**Goal**: Understand WHY this project structure scan is needed for this specific project.

**Memory queries** (at start):
- `memory_ops.load_lessons_learned(task_id='SA-DISC-001', project_name=...)` filtered by `phase='phase1'`
- If previous purpose records exist, present them to user

**Steps**:
1. If Re-scan Mode and previous purpose exists:
   ```
   "Last time we scanned this project, the purpose was: {previous_purpose}.
    Is the purpose the same this time, or has it changed?"
   ```
2. If Fresh Scan Mode: Formulate understanding of scan purpose based on intake info:
   ```
   "Based on what you've told me, we need to scan this project because {understanding}.
    Is this correct?"
   ```
3. If lessons exist about user preferences, proactively incorporate:
   ```
   "Based on previous experience, I know you particularly care about {lesson_content}.
    I'll make sure to focus on that again."
   ```
4. Iterate until user explicitly confirms purpose understanding.

**Memory writes**:
- `memory_ops.record_decision()` — record confirmed purpose
- Log questions to `logs/conversation-log.md`
- Save question list to `phase1-questions.md`

**Success criteria**: User explicitly confirms purpose understanding.

---

## Phase 2: Understand the Target Project

**Goal**: Understand WHAT the target project is — domain, tech stack, scale, structure.

**Memory queries** (at start):
- `memory_ops.load_project_knowledge()` — get known tech stack, patterns, conventions
- Query previous phase2 questions to skip already-answered items

**Steps**:
1. If knowledge exists, pre-fill and present:
   ```
   "Based on my records, this project uses:
    - Language: {language}
    - Framework: {framework}
    - Build Tool: {build_tool}
    - Architecture: {pattern}
    - Database: {database}

    Has any of this changed? And I have a few new questions: ..."
   ```
2. If no knowledge: Perform initial analysis using tools:
   - **Glob**: `**/{pom.xml,package.json,build.gradle,requirements.txt,go.mod,Cargo.toml}` — identify build system
   - **Read**: Build/manifest files to identify tech stack
   - **Bash**: `tree -L 2 -d {project_path}` — get directory overview
   - **Bash**: `wc -l $(find {path} -name '*.{ext}' -not -path '*/node_modules/*')` — estimate LOC
3. Present understanding of the project:
   ```
   "Here's what I've gathered about this project:
    - Domain: {domain}
    - Technology Stack: {tech_stack}
    - Scale: {loc} LOC, {file_count} files, {module_count} modules
    - Build System: {build_tool}
    - Repository Type: {monorepo/polyrepo}

    Is this accurate?"
   ```
4. Ask delta questions for unknowns. Skip questions answered in previous sessions.
5. Iterate until user confirms.

**Memory writes**:
- `memory_ops.record_knowledge()` — store tech stack, patterns, conventions
- Log questions to `logs/conversation-log.md`
- Save question list to `phase2-questions.md`

**Success criteria**: User confirms project understanding.

---

## Phase 3: Research & Question Generation

**Goal**: Research best practices and generate a validated scan requirements list.

**Memory queries** (at start):
- Load previous research from `research/` directory
- Query findings from previous phase3 sessions
- `memory_ops.load_project_knowledge()` for known patterns

**Steps**:
1. If previous research exists, skip redundant research. Focus on:
   - New modules added since last scan
   - Changed dependency relationships
   - New integration points
2. Research industry best practices:
   - Use **Context7** to look up framework-specific conventions (e.g., Spring Boot project structure best practices)
   - Use **WebSearch** for architecture analysis methodologies
   - Save all research to `research/{topic}.md`
3. Proactively revisit known risks:
   ```
   "Last time I identified these risks:
    - Risk 1: {risk_description}
    - Risk 2: {risk_description}
    Should I verify if these have been resolved?"
   ```
4. Generate comprehensive question list covering:
   - Module boundary conventions
   - Naming patterns and organization strategy
   - Known architecture decisions
   - Expected patterns vs. actual patterns
   - Integration points and external systems
   - Areas of concern or technical debt
5. Engage in iterative dialogue with user based on question list.
6. Produce **validated scan requirements list** — what to scan, what to focus on, what to ignore, expected output format.

**Memory writes**:
- `memory_ops.record_finding()` — research results
- `memory_ops.record_question()` — each Q&A exchange
- `memory_ops.record_risk()` — identified risks
- Save to `research/`, `phase3-questions.md`

**Success criteria**: User agrees on validated scan requirements list. Save as `validated-requirements.md`.

---

## Phase 4: Execute & Produce Deliverables

**Goal**: Scan the codebase and produce all 6 deliverables (OUT-01 through OUT-06).

**Memory queries** (at start):
- Load previous OUT-01 for incremental scan comparison
- Load previous patterns for confirmation
- Query previous failed DoD items to prioritize fixing

**Scan Strategy**:
- **Full scan**: Analyze entire project from scratch
- **Incremental scan**: Load previous OUT-01, Glob current structure, diff to find added/removed/modified directories, only deep-scan changed areas, merge with previous deliverables

**Step 4.1 — Produce OUT-01: Project Structure Tree**
- **Tools**: `Bash: tree -L 4 -d {path}`, `Glob: **/*`, `Read: key files`
- **Template**: `templates/structure-tree-template.md`
- **Action**: Generate annotated directory tree with purpose descriptions for each directory
- **Memory**: `record_finding()` for each significant directory

**Step 4.2 — Produce OUT-02: Module Relationship Diagram**
- **Tools**: `Grep: import/require/include statements`, `Read: build files for module dependencies`
- **Template**: `templates/module-relationship-template.md`
- **Action**: Construct module dependency graph, generate draw.io XML diagram saved as `diagrams/module-relationship.drawio`, build dependency matrix
- **Memory**: `record_finding()` for circular dependencies, `record_risk()` for tight coupling

**Step 4.3 — Produce OUT-03: Layering Pattern Analysis**
- **Tools**: `Glob: directory structure patterns`, `Grep: layer-specific annotations/decorators`
- **Template**: `templates/layering-analysis-template.md`
- **Action**: Test against each known architecture pattern (MVC/DDD/Hexagonal/Clean/Layered/etc.), identify primary pattern with evidence, check layer dependency rules
- **Memory**: `record_knowledge(category='pattern')`, update confidence for existing patterns

**Step 4.4 — Produce OUT-04: Package Dependency Map**
- **Tools**: `Read: pom.xml/package.json/build.gradle/requirements.txt`, `Bash: mvn dependency:tree / npm ls / pip list`
- **Template**: `templates/dependency-map-template.md`
- **Action**: Inventory all third-party and internal dependencies, generate draw.io XML diagram saved as `diagrams/dependency-map.drawio`, assess risks
- **Smart dependency diff** (incremental): Compare current manifest with previous OUT-04, report only changes
- **Memory**: `record_knowledge(category='dependency')`

**Step 4.5 — Produce OUT-05: Module Responsibility Summary**
- **Tools**: `Read: entry point files, main classes, package-info.java`, `Grep: public interfaces`
- **Template**: `templates/module-summary-template.md`
- **Action**: Describe each module's responsibility, assess cohesion and coupling
- **Memory**: `record_finding()` for each module analysis

**Step 4.6 — Produce OUT-06: Project Structure Scan Report**
- **Template**: `templates/scan-report-template.md`
- **Action**: Consolidate all findings into comprehensive final report, write executive summary, list recommendations
- **Output**: Save as `project-structure-report.md` in output directory

**Step 4.7 — DoD Self-Verification**
- Run `python scripts/verify_dod.py --output-dir {output_dir} --session-id {session_id} --round 1`
- If any checks fail → fix the issues → re-run verification
- Repeat until all DoD items pass
- **Memory**: Results recorded via `record_dod_check()`

**Memory writes**:
- `record_finding()` after each significant finding
- `record_knowledge()` for reusable insights
- `record_dod_check()` for DoD results
- Log all actions to `logs/work-log.md`

**Success criteria**: All 6 deliverables produced, all draw.io diagrams generated in `diagrams/`, DoD self-check passes 100%.

---

## Phase 5: Transformation Target Deep-Dive Investigation

**Trigger condition**: This phase is ONLY executed when the scan purpose (from Phase 0 intake or Phase 1 confirmation) involves any form of change, refactoring, feature addition, or system evolution.

**Goal**: Produce a focused **Transformation Target Current State Report** (OUT-07) that serves as the baseline for transformation design.

**Memory queries** (at start):
- Query `task_memory` for previous Phase 5 findings on this project
- If prior OUT-07 exists, present delta and ask if scope has changed

**Step 5.1 — Confirm Transformation Target Scope**
1. If target was specified in intake/Phase 1, confirm:
   ```
   "The transformation target appears to be: {target_scope}.
    Is this correct, or should we focus on a different module/component/area?"
   ```
2. If not yet specified, ask:
   ```
   "Which specific module(s), component(s), file(s), or functional area(s) will be transformed?
    Please be as specific as possible."
   ```
3. Iterate until user confirms exact target scope. Save confirmed scope to `validated-requirements.md`.

**Step 5.2 — Investigate Current State**

Using tools (Glob, Grep, Read, Bash), deep-dive the transformation target:

| Investigation Area | Tools | What to Capture |
|-------------------|-------|----------------|
| Code structure & file layout | Glob, Bash: tree | Directory structure within target scope, key files with LOC |
| Core logic | Read: key files | Main processing flow, decision branches, error handling |
| Key data structures | Read: model/entity files | Domain models, DTOs, enums, persistence schema |
| Inbound dependencies | Grep: import/usage of target's classes | Who depends on this target |
| Outbound dependencies | Read: imports inside target | What this target depends on |
| Public interfaces/APIs | Grep: public/exported declarations | Exposed contracts and entry points |
| Shared state & data stores | Grep: DB/cache/queue access | Tables, collections, queues accessed |
| Test coverage | Glob: test files, Read: test classes | Unit/integration/E2E tests, coverage level |
| Technical debt | Read: code, Grep: TODO/FIXME/HACK | Code smells, anti-patterns, hardcoded values |
| Configuration dependencies | Grep: env vars, config keys | External config dependencies |

**Step 5.3 — Produce draw.io Sequence Diagrams**
- For each significant flow of the transformation target, produce a draw.io sequence diagram:
  - **Main success flow**: `diagrams/seq-{use-case-name}-main.drawio`
  - **Error/alternative flow**: `diagrams/seq-{use-case-name}-error.drawio`
- Use `templates/transformation-target-template.md` Section 5 as the template
- Each `.drawio` file must be valid XML with `<mxfile>` root element

**Step 5.4 — Identify Transformation Constraints**
- **Hard constraints**: Public APIs, DB schemas, SLAs, external contracts — things that CANNOT change
- **Soft constraints**: Internal conventions, behaviors to preserve if possible
- **Risk areas**: High-coupling zones, untested code, shared state, blast radius

**Step 5.5 — Produce OUT-07**
- Use `templates/transformation-target-template.md`
- Must include all sections: Overview, Code Structure, Core Logic Description, Key Data Structures, Sequence Diagrams (draw.io file references), Responsibilities, Dependency Analysis, Data Flows, Test Coverage, Technical Debt, Configuration, Constraints, Readiness Assessment
- Save to output directory as `OUT-07_transformation-target-current-state.md`

**Step 5.6 — Present & Confirm**
1. Present the Transformation Target Current State Report summary to user
2. User confirms → proceed to Phase 6
3. User requests deeper investigation → repeat relevant sub-steps → re-present until confirmed

**Memory writes**:
- `record_finding(phase='phase5')` for each investigation finding
- `record_finding(phase='phase5', memory_type='risk')` for each identified risk
- `record_decision(phase='phase5')` for confirmed target scope and constraints
- Log all actions to `logs/work-log.md`, all Q&A to `logs/conversation-log.md` Phase 5 section

**Success criteria**: User confirms the Transformation Target Current State Report (OUT-07).

---

## Phase 6: Completion & Handoff

**Steps**:
1. **Record lessons learned**: Extract key insights from the session, call `memory_ops.record_lesson()`.
2. **Update knowledge base**: Call `memory_ops.record_knowledge()` with high-confidence findings.
3. **Complete scan record**: Call `memory_ops.complete_scan()` to update `scan_history`.
4. **Trigger supervisor**: Signal the `project-structure-scan-supervisor` skill to inspect outputs.
5. **Remediation loop**: If supervisor returns failures, fix issues and signal re-inspection. Repeat until 100% pass or 3 rounds.
6. **Notify PM Agent**: After supervisor passes, send to PM Agent:
   - Deliverables directory path and file names
   - RACI matrix (`config/raci.md`) for downstream task triggering
   - Final inspection report
   - Scan summary (project name, scope, modules found, primary pattern)

**Success criteria**: Supervisor passes 100%, PM Agent notified, downstream tasks triggered.

---

## Memory Utilization Protocol

### Phase 0 (Startup): Memory-Driven Context Loading
- Check if `memory/agent_memory.db` exists; if not, run `scripts/init_memory.py`
- Call `load_project_history()` → determine Re-scan Mode vs Fresh Scan Mode
- Re-scan Mode: call `generate_memory_summary()`, present to user, offer options (incremental/full/review)
- Fresh Scan Mode: call `get_similar_projects()`, if found present pattern hypothesis
- Call `apply_confidence_decay()` to maintain memory freshness
- Call `prune_low_confidence()`, report low-confidence entries to user

### Phase 1 (Understand Task Purpose): Memory-Enhanced Understanding
- Query previous purpose records: `load_lessons_learned()` filtered by phase='phase1'
- If found, present previous purpose and ask if it still applies (skip redundant questions)
- If lessons exist about user preferences, proactively incorporate

### Phase 2 (Understand Target Project): Memory-Accelerated Discovery
- Query `load_project_knowledge()` for known tech stack, patterns, conventions
- Pre-fill known answers, only ask about unknowns or changes
- Query previous phase2 questions to skip already-answered items
- **Time saved**: ~60-80% fewer questions on re-scans

### Phase 3 (Research & Question Generation): Memory-Informed Research
- Load previous research from `research/` directory
- Query findings from previous phase3 sessions
- Skip redundant research, focus on gaps and new risks
- Proactively revisit known risks and ask if resolved
- **Time saved**: ~50% less research on re-scans

### Phase 4 (Execute & Produce Deliverables): Memory-Optimized Execution
- Incremental scan: compare current structure with previous OUT-01
- Pattern confirmation: verify previous patterns still hold, update confidence
- Smart dependency diff: compare current manifest with previous OUT-04
- Quality improvement: query previous failed DoD items, prioritize fixing them
- **Time saved**: ~40-70% faster execution on re-scans

### Phase 5 (Transformation Target Deep-Dive): Memory-Enhanced Investigation
- Query previous Phase 5 findings for same project: if OUT-07 exists, offer delta update vs. full re-investigation
- Pre-load known risks and constraints from previous sessions
- Skip already-investigated areas, focus on what has changed since last scan

### Cross-Project Knowledge Transfer
- Query all high-confidence knowledge entries across projects
- Build pattern library, use for hypothesis-driven analysis on new projects
- Record prediction accuracy as lessons for future improvement
- **Time saved**: ~30% faster on first scan of similar projects

### Confidence Decay & Contradiction Detection
- **90-day decay**: reduce confidence by 0.2 for entries not updated in 90 days (min 0.1)
- **Contradiction detection**: flag conflicts between new findings and existing knowledge, ask user
- **Low-confidence pruning**: report entries below 0.3 threshold for user review

---

## Logging Requirements

### Conversation Log
- Record every user interaction in `logs/conversation-log.md`
- Each entry: question text, who asked (Agent/User), timestamp, response, status

### Work Log
- Record every action with timestamp in `logs/work-log.md`
- Each entry: timestamp, phase, action, details, status, memory operation used

### Phase Questions
- Save question lists from each phase in `phase{N}-questions.md` (Requirement 16)
- At minimum: `phase1-questions.md`, `phase2-questions.md`, `phase3-questions.md`

### Research Artifacts
- Save all research processes and results to `research/` directory (Requirement 17)
- Each research topic gets its own file: `research/{topic}.md`

---

## Reference Files

| Category | File | Purpose |
|----------|------|---------|
| **Config** | `config/triggers.md` | Trigger mechanisms and Project Intake Checklist |
| **Config** | `config/raci.md` | RACI matrix for stakeholders and downstream triggers |
| **Config** | `config/skills-and-knowledge.md` | Agent skills and knowledge base |
| **Config** | `config/tools.md` | Tools list with usage examples |
| **Config** | `config/mcp-tools.md` | MCP tools list |
| **Templates** | `templates/structure-tree-template.md` | OUT-01 template |
| **Templates** | `templates/module-relationship-template.md` | OUT-02 template |
| **Templates** | `templates/layering-analysis-template.md` | OUT-03 template |
| **Templates** | `templates/dependency-map-template.md` | OUT-04 template |
| **Templates** | `templates/module-summary-template.md` | OUT-05 template |
| **Templates** | `templates/scan-report-template.md` | OUT-06 template |
| **Templates** | `templates/transformation-target-template.md` | OUT-07 template (conditional — transformation scans only) |
| **References** | `references/sop.md` | Standard Operating Procedure |
| **References** | `references/dod.md` | Definition of Done quality gates |
| **References** | `references/dor.md` | Definition of Ready prerequisites |
| **References** | `references/output-templates.md` | Output template index |
| **Scripts** | `scripts/init_memory.py` | Initialize SQLite memory database |
| **Scripts** | `scripts/memory_ops.py` | Memory CRUD operations library |
| **Scripts** | `scripts/verify_dod.py` | DoD self-verification script |
| **Memory** | `memory/index.md` | Memory architecture documentation |
