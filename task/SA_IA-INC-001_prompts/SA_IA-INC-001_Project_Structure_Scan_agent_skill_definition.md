
# Create an AI Agent Skill for Completing the "Project Structure Scan" Task. Details as follows:

# Basic Requirements:

- **Requirement 1**: Collect the trigger mechanisms for a qualified Project Structure Scan AI Agent. Define what events or conditions trigger the Project Structure Scan task (e.g., PM Agent assigns task SA-DISC-001 via RACI matrix, new feature request received for an existing system, architecture discovery phase initiated). Create a configurable trigger file that supports future modifications.

- **Requirement 2**: Collect the RACI matrix for a qualified Project Structure Scan AI Agent. The RACI matrix must include both role names AND corresponding task names. Create a configurable RACI file with two purposes: Purpose 1 — allow the AI Agent to know all stakeholders each time it starts; Purpose 2 — after the AI Agent completes the task, send this RACI matrix to the Project Manager AI Agent to help the PM Agent trigger downstream tasks. Support future modifications.

- **Requirement 3**: Collect the skills a qualified Project Structure Scan AI Agent should possess (e.g., directory structure analysis, module decomposition recognition, dependency graph construction, layering pattern identification, codebase navigation, build system analysis, package manager parsing). Create a configurable skills file that the AI Agent loads on startup. Support future modifications.

- **Requirement 4**: Collect the knowledge base a qualified Project Structure Scan AI Agent should have (e.g., software architecture patterns — MVC/MVP/MVVM/DDD/Hexagonal/Clean Architecture/Onion Architecture/Layered Architecture/Microservices/Monolithic, module decomposition principles, package dependency management, build system conventions for major languages/frameworks, design patterns, SOLID principles). Create a configurable knowledge file that the AI Agent loads on startup. Support future modifications.

- **Requirement 5**: Collect the tools a qualified Project Structure Scan AI Agent should use (e.g., Glob for file pattern matching, Grep for content search, Read for file reading, Bash for tree/find/wc commands, dependency analysis commands per language ecosystem). Create a configurable tools file that the AI Agent loads on startup. Support future modifications.

- **Requirement 6**: Collect the MCP tools a qualified Project Structure Scan AI Agent should use (e.g., IDE diagnostics, code intelligence, context7 documentation lookup). Create a configurable MCP tools file that the AI Agent loads on startup. Support future modifications.

- **Requirement 7**: Collect the output deliverables a qualified Project Structure Scan AI Agent should produce, and create a template for each output item. The AI Agent loads these templates on startup and strictly follows them when producing outputs. Support future modifications. The output deliverables include:
  - **OUT-01**: Project Structure Tree — annotated directory hierarchy showing all top-level and key nested directories with purpose descriptions
  - **OUT-02**: Module Relationship Diagram — Mermaid diagram showing dependencies and communication between modules
  - **OUT-03**: Layering Pattern Analysis — identified architectural patterns (MVC/DDD/Hexagonal/Clean/Layered/etc.) with evidence from the codebase
  - **OUT-04**: Package Dependency Map — third-party and internal dependency inventory with version info
  - **OUT-05**: Module Responsibility Summary — concise description of what each top-level module/package does
  - **OUT-06**: Project Structure Scan Report — comprehensive final report consolidating all findings
  - **OUT-07**: Transformation Target Current State Report — focused deep-dive report on the specific area to be transformed, documenting current implementation, dependencies, interfaces, test coverage, constraints, and risk areas (only produced when scan purpose involves transformation/refactoring)

- **Requirement 8**: Collect the SOP process a qualified Project Structure Scan AI Agent should follow. Create a configurable SOP file that the AI Agent loads on startup. Support future modifications.

- **Requirement 9**: Collect the DoD (Definition of Done) quality gates a qualified Project Structure Scan AI Agent must satisfy. Create a configurable DoD file that the AI Agent loads on startup. Support future modifications.

- **Requirement 10**: Collect the DoR (Definition of Ready) prerequisites a qualified Project Structure Scan AI Agent must verify before starting (e.g., codebase repository is cloned and accessible, build files or project manifest files exist, read permissions are available, target scan scope is defined). Create a configurable DoR file that the AI Agent loads on startup. Support future modifications.

- **Requirement 11**: The AI Agent must record every conversation with the user, question by question, logged entry by entry in a conversation log document (`conversation-log.md`).

- **Requirement 12**: The AI Agent must record its own work log, entry by entry on a timeline, in a work log document (`work-log.md`).

- **Requirement 13**: The AI Agent must check against the DoD checklist whether the task is complete. If any check item fails, go back and fix the issue, then re-check until all items pass.

- **Requirement 14**: **[Supervisor AI Agent Skill Specification]** — Create a separate, independent **Supervisor AI Agent Skill (project-structure-scan-supervisor)** responsible for full quality inspection and closed-loop remediation of the Project Structure Scan AI Agent's outputs. Specific requirements:

  ---

  ### 14.1 Role Definition
  - **Skill Name**: `project-structure-scan-supervisor`
  - **Role**: Quality Supervisor — independent from the Project Structure Scan Agent, does not participate in the scan itself, only responsible for inspection and feedback.
  - **Trigger Timing**: Automatically triggered after the Project Structure Scan AI Agent completes one round of output.
  - **Execution Mechanism**: This Skill automatically inspects the Project Structure Scan AI Agent's outputs and generates an inspection report.

  ---

  ### 14.2 Inspection Scope (Checklist)
  The Supervisor AI Agent inspects the execution status of **Requirements 1 through 13** item by item:

  | Check Item | Inspection Content |
  | :--- | :--- |
  | ✅ Req 1 | Trigger mechanism configuration file has been generated |
  | ✅ Req 2 | RACI matrix configuration file has been generated (with role names + corresponding task names) |
  | ✅ Req 3 | Skills list configuration file has been generated |
  | ✅ Req 4 | Knowledge base list has been generated |
  | ✅ Req 5 | Tools list has been generated |
  | ✅ Req 6 | MCP tools list has been generated |
  | ✅ Req 7 | Output templates have been generated (OUT-01 through OUT-06) |
  | ✅ Req 8 | SOP process file has been generated |
  | ✅ Req 9 | DoD quality gates file has been generated |
  | ✅ Req 10 | DoR prerequisites file has been generated |
  | ✅ Req 11 | User conversation log document exists (logged question by question) |
  | ✅ Req 12 | AI Agent work log document exists (logged entry by entry on timeline) |
  | ✅ Req 13 | DoD check results have passed, closed-loop remediation completed |

  ---

  ### 14.3 Inspection Process (Closed-Loop Mechanism)

  ```
  [Trigger] Project Structure Scan Agent completes output
       ↓
  [Inspect] Supervisor Agent checks Requirements 1–13 item by item
       ↓
  [Generate Report] Output inspection report (see 14.4)
       ↓
  [Decide] Report pass rate = 100%?
       ├── No → Send report back to Project Structure Scan Agent,
       │         request item-by-item remediation.
       │         After remediation, re-trigger Supervisor Agent.
       │         (Repeat this loop until 100% pass)
       └── Yes → Call Project Manager AI Agent, submit completion report
  ```

  ---

  ### 14.4 Inspection Report Format

  Each inspection generates a structured report in the following format:

  ```markdown
  # Project Structure Scan Supervisor Inspection Report

  - Inspection Time: {timestamp}
  - Inspection Round: Round {N}
  - Output Directory: {output_directory_path}

  ## Inspection Results Summary

  | Check Item | Status | Notes |
  | :--- | :---: | :--- |
  | Req 1: Trigger Config | ✅ Pass / ❌ Fail | {notes} |
  | Req 2: RACI Matrix Config | ✅ Pass / ❌ Fail | {notes} |
  | ... | ... | ... |

  ## Overall Pass Rate: {X}% ({M}/{N} items passed)

  ## Issues Requiring Remediation
  1. {Issue description} — Remediation suggestion: {suggestion}
  2. ...

  ## Conclusion: [Fail → Return for remediation | Pass → Call Project Manager AI Agent]
  ```

  ---

  ### 14.5 Post-Completion: Call Project Manager AI Agent
  - When the report pass rate reaches **100%**, the Supervisor Agent performs the following:
    1. Generate the final inspection report (marked "All Passed").
    2. Call the **Project Manager AI Agent** with the following information:
       - Project Structure Scan deliverables directory path and file names
       - RACI matrix configuration (for PM Agent to trigger downstream tasks)
       - Final inspection report

- **Requirement 15**: After the AI Agent completes the task, notify the Project Manager AI Agent that the task is done, and send the deliverable file paths and names to the PM Agent. The PM Agent uses the RACI matrix from this task to call the corresponding AI Agents for downstream RACI matrix tasks.

- **Requirement 16**: Record all question lists from each phase, saved in dedicated phase question files for future review.

- **Requirement 17**: When the AI Agent uses tools to conduct research, save all research processes and results locally for future use.

---

# Long-Term Memory Architecture (Hybrid: Markdown + SQLite)

The AI Agent must maintain **long-term memory** across sessions using a hybrid storage strategy. This ensures the agent can recall past findings, decisions, and lessons learned when re-invoked on the same or similar projects.

## Memory Storage Principle

| Data Type | Storage | Reason |
|-----------|---------|--------|
| Conversation logs, work logs, research reports | **Markdown** | Human-reviewable, Git-trackable, AI-native friendly |
| Task state, execution progress, DoD check results | **SQLite** | Requires structured queries (e.g., "which DoD items failed?") |
| Cross-session memory (findings, decisions, lessons, patterns) | **SQLite** | Requires persistent retrieval (e.g., "what did we find last time scanning this project?") |
| Configuration files (RACI, triggers, tools list) | **Markdown** | Human-editable, version-controlled |

## SQLite Database Design

The AI Agent must initialize and maintain `memory/agent_memory.db` with the following schema:

```sql
-- Task execution memory: records findings, decisions, and lessons per session
CREATE TABLE IF NOT EXISTS task_memory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id TEXT NOT NULL,
    task_id TEXT NOT NULL,           -- e.g., 'SA-DISC-001'
    project_name TEXT,               -- target project being scanned
    phase TEXT,                      -- e.g., 'phase1', 'phase2', 'phase3', 'phase4'
    memory_type TEXT NOT NULL,       -- 'finding', 'decision', 'lesson', 'question', 'risk'
    title TEXT,
    content TEXT NOT NULL,
    context TEXT,                    -- related module/component/file
    tags TEXT,                       -- comma-separated tags for categorization
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- DoD check records: tracks pass/fail status per check item per session
CREATE TABLE IF NOT EXISTS dod_checks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id TEXT NOT NULL,
    task_id TEXT NOT NULL,
    check_round INTEGER NOT NULL,    -- inspection round number
    check_item TEXT NOT NULL,         -- e.g., 'req_01_trigger_config'
    status TEXT NOT NULL,             -- 'pass', 'fail', 'pending'
    evidence TEXT,                    -- file path or description proving the status
    notes TEXT,
    checked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Cross-session knowledge base: accumulates reusable insights across projects
CREATE TABLE IF NOT EXISTS knowledge_base (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_name TEXT NOT NULL,
    category TEXT NOT NULL,          -- 'pattern', 'dependency', 'risk', 'insight', 'tech_stack', 'convention'
    key TEXT NOT NULL,
    value TEXT NOT NULL,
    confidence REAL DEFAULT 0.8,     -- 0.0 to 1.0
    source TEXT,                     -- where this knowledge came from
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Scan history: records each scan execution for traceability
CREATE TABLE IF NOT EXISTS scan_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id TEXT NOT NULL,
    task_id TEXT NOT NULL,
    project_name TEXT NOT NULL,
    project_path TEXT NOT NULL,
    scan_scope TEXT,                 -- full scan, partial scan, incremental scan
    status TEXT NOT NULL,            -- 'in_progress', 'completed', 'failed'
    deliverables_path TEXT,
    started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP
);
```

## Memory Operations

The AI Agent must perform the following memory operations:

### On Startup
1. Check if `memory/agent_memory.db` exists; if not, create it with the schema above.
2. Query `scan_history` for previous scans of the same project: `SELECT * FROM scan_history WHERE project_name = ? ORDER BY started_at DESC LIMIT 5`
3. Query `knowledge_base` for accumulated knowledge about the project: `SELECT * FROM knowledge_base WHERE project_name = ? ORDER BY confidence DESC`
4. Query `task_memory` for lessons learned from previous sessions: `SELECT * FROM task_memory WHERE task_id = 'SA-DISC-001' AND memory_type = 'lesson' ORDER BY created_at DESC LIMIT 20`
5. Present relevant historical context to user before beginning the scan.

### During Execution
1. After each significant finding, insert into `task_memory` with `memory_type = 'finding'`.
2. After each key decision, insert into `task_memory` with `memory_type = 'decision'`.
3. After each user Q&A exchange, insert into `task_memory` with `memory_type = 'question'`.
4. After identifying a risk, insert into `task_memory` with `memory_type = 'risk'`.

### On Completion
1. Insert scan record into `scan_history` with `status = 'completed'`.
2. Extract key insights and insert into `knowledge_base` for future reuse.
3. Insert lessons learned into `task_memory` with `memory_type = 'lesson'`.
4. Run all DoD checks and record results in `dod_checks`.

### On Re-invocation (Same Project)
1. Load previous scan results and present delta/changes to user.
2. Offer incremental scan option instead of full re-scan.
3. Validate whether previous findings still hold.

---

## Memory Utilization Protocol — How Memory Drives Agent Behavior

The core principle: **Memory is not just storage — it must actively shape the Agent's decisions, questions, focus areas, and outputs at every phase.** Below defines exactly how the Agent must use memory at each workflow step.

### Phase 0 (Startup): Memory-Driven Context Loading

```
[Agent Starts]
    ↓
[Query scan_history] → Has this project been scanned before?
    ├── YES → Enter "Re-scan Mode" (see below)
    └── NO  → Query knowledge_base for SIMILAR projects
                 ├── Found similar → Pre-load patterns, present to user:
                 │   "I've scanned similar projects before. Project X used
                 │    DDD with Hexagonal architecture. Should I look for
                 │    similar patterns here?"
                 └── Not found → Enter "Fresh Scan Mode" (standard workflow)
```

**Re-scan Mode Behavior:**
1. Load previous scan's `project-structure-report.md` and all OUT-01~06 deliverables.
2. Query: `SELECT * FROM task_memory WHERE project_name = ? AND memory_type IN ('finding', 'risk', 'lesson') ORDER BY created_at DESC`
3. Present a **Memory Summary** to the user:
   ```
   📋 Previous Scan Summary (Session: {session_id}, Date: {date}):
   - Architecture Pattern Found: {pattern}
   - Key Modules: {module_list}
   - Known Risks: {risk_list}
   - Lessons Learned: {lesson_list}
   - Last DoD Pass Rate: {rate}%

   Would you like to:
   (a) Run an incremental scan (only detect changes since last scan)
   (b) Run a full re-scan (ignore previous results)
   (c) Review and update previous findings
   ```
4. If user selects incremental scan → Agent compares current file tree with previous OUT-01, only scans changed/new directories.

### Phase 1 (Understand Task Purpose): Memory-Enhanced Understanding

**Without Memory** (standard): Agent guesses why the scan is needed.

**With Memory** (enhanced):
1. Query: `SELECT * FROM task_memory WHERE project_name = ? AND memory_type = 'decision' AND phase = 'phase1'`
2. If previous purpose records exist, present them:
   ```
   "Last time we scanned this project, the purpose was: {previous_purpose}.
    Is the purpose the same this time, or has it changed?"
   ```
3. Query: `SELECT * FROM task_memory WHERE memory_type = 'lesson' AND phase = 'phase1'`
4. If lessons exist (e.g., "user cared most about module boundaries"), proactively incorporate:
   ```
   "Based on previous experience, I know you particularly care about
    {lesson_content}. I'll make sure to focus on that again."
   ```

### Phase 2 (Understand Target Project): Memory-Accelerated Discovery

**Without Memory**: Agent asks many basic questions about the project from scratch.

**With Memory**:
1. Query: `SELECT * FROM knowledge_base WHERE project_name = ? AND category IN ('tech_stack', 'pattern', 'convention')`
2. Pre-fill known answers and only ask about unknowns:
   ```
   "Based on my records, this project uses:
    - Language: Java 17
    - Framework: Spring Boot 3.x
    - Build Tool: Gradle
    - Architecture: Layered (Controller → Service → Repository)
    - Database: PostgreSQL

    Has any of this changed? And I have a few new questions: ..."
   ```
3. Query: `SELECT * FROM task_memory WHERE project_name = ? AND memory_type = 'question' AND phase = 'phase2'`
4. Skip questions that were already answered in previous sessions (unless user indicates changes).
5. **Time saved**: Instead of 15 questions, only ask 3-5 delta questions.

### Phase 3 (Research & Question Generation): Memory-Informed Research

**Without Memory**: Agent researches generic best practices.

**With Memory**:
1. Query: `SELECT * FROM task_memory WHERE project_name = ? AND memory_type = 'finding' AND phase = 'phase3'`
2. Load previous research results from `research/` directory.
3. Query: `SELECT * FROM knowledge_base WHERE category = 'pattern' AND confidence >= 0.7`
4. **Skip redundant research**: If the agent already knows the project uses Spring Boot + DDD, skip researching "how to identify architecture patterns in Java projects" and go directly to targeted questions.
5. **Focus on gaps**: Generate questions only about areas NOT covered in previous sessions:
   ```
   "In previous sessions, we covered module structure and layering.
    This time I'd like to focus on:
    1. Any new modules added since last scan?
    2. Have dependency relationships changed?
    3. Any new integration points?"
   ```
6. Query: `SELECT * FROM task_memory WHERE memory_type = 'risk'`
7. **Proactively revisit known risks**:
   ```
   "Last time I identified these risks:
    - Risk 1: Circular dependency between module-A and module-B
    - Risk 2: module-C has no clear layering pattern
    Should I verify if these have been resolved?"
   ```

### Phase 4 (Execute & Produce Deliverables): Memory-Optimized Execution

**Without Memory**: Agent scans everything from scratch.

**With Memory**:
1. **Incremental Scan Strategy**:
   ```
   [Load previous OUT-01 structure tree]
       ↓
   [Glob current directory structure]
       ↓
   [Diff: identify ADDED / REMOVED / MODIFIED directories]
       ↓
   [Only deep-scan changed areas]
       ↓
   [Merge: update previous deliverables with new findings]
   ```

2. **Pattern Confirmation**:
   - Query: `SELECT * FROM knowledge_base WHERE project_name = ? AND category = 'pattern'`
   - Instead of re-identifying the architecture pattern, verify it still holds:
     ```sql
     -- If previous finding: "pattern = DDD, confidence = 0.9"
     -- Agent checks: do domain/application/infrastructure layers still exist?
     -- If yes → keep finding, update confidence
     -- If no → flag as "pattern drift", alert user
     UPDATE knowledge_base SET confidence = ?, updated_at = CURRENT_TIMESTAMP
     WHERE project_name = ? AND category = 'pattern' AND key = ?
     ```

3. **Smart Dependency Diff**:
   - Load previous OUT-04 (Package Dependency Map)
   - Compare with current `package.json` / `pom.xml` / `build.gradle` / `requirements.txt`
   - Report only: new dependencies added, dependencies removed, version changes
   - Flag: any newly added dependency that conflicts with known architecture patterns

4. **Quality Improvement Over Time**:
   - Query: `SELECT check_item, status, notes FROM dod_checks WHERE task_id = 'SA-DISC-001' AND status = 'fail' ORDER BY checked_at DESC`
   - If previous DoD failures exist, **proactively address them first**:
     ```
     "In the last scan, these DoD items failed:
      - {check_item}: {notes}
      I will prioritize fixing these in this round."
     ```

### Cross-Project Knowledge Transfer

When scanning a **new project** that the agent has never seen:

1. Query: `SELECT DISTINCT project_name, category, key, value, confidence FROM knowledge_base WHERE confidence >= 0.8 ORDER BY category`
2. Build a **pattern library** from all previously scanned projects.
3. Use pattern matching to accelerate analysis:
   ```
   "I've scanned 5 projects before. Based on the build files I see
    (pom.xml, Spring Boot starter), this project most closely resembles
    Project-X which used a Layered Architecture with DDD tactical patterns.
    I'll use that as my initial hypothesis and verify."
   ```
4. After scan completes, compare findings with the hypothesis and record accuracy:
   ```sql
   INSERT INTO task_memory (session_id, task_id, project_name, phase,
     memory_type, title, content)
   VALUES (?, 'SA-DISC-001', ?, 'phase4', 'lesson',
     'Cross-project pattern prediction accuracy',
     'Predicted Layered+DDD based on Project-X similarity. Actual: Hexagonal.
      Accuracy: partial. Note: Spring Boot projects can vary widely.')
   ```

### Memory Confidence Decay & Validation

To prevent stale memory from misleading the agent:

1. **Time-based decay**: On startup, query entries older than 90 days:
   ```sql
   SELECT * FROM knowledge_base
   WHERE updated_at < datetime('now', '-90 days')
   AND confidence > 0.5
   ```
   Reduce confidence by 20% for entries not validated in 90 days:
   ```sql
   UPDATE knowledge_base
   SET confidence = MAX(confidence - 0.2, 0.1),
       updated_at = CURRENT_TIMESTAMP
   WHERE updated_at < datetime('now', '-90 days')
   ```

2. **Contradiction detection**: If a new finding contradicts an existing knowledge_base entry:
   - Flag the contradiction to the user
   - Ask which is correct
   - Update or replace the old entry
   - Record the contradiction as a lesson:
     ```sql
     INSERT INTO task_memory (..., memory_type, title, content)
     VALUES (..., 'lesson', 'Knowledge correction',
       'Previous: {old_value}. Corrected to: {new_value}. Reason: {reason}')
     ```

3. **Low-confidence pruning**: On startup, report entries with confidence < 0.3:
   ```
   "I have some low-confidence memories about this project that may be outdated:
    - {key}: {value} (confidence: 0.2)
    Should I discard these or re-verify?"
   ```

### Memory Utilization Summary Per Phase

| Phase | Without Memory | With Memory | Time Savings |
|-------|---------------|-------------|-------------|
| Phase 0: Startup | Cold start, no context | Load history, present summary, offer incremental scan | Skip entire re-discovery |
| Phase 1: Purpose | Guess from scratch | Recall previous purpose, ask for delta only | ~70% fewer questions |
| Phase 2: Understand | Ask 15+ basic questions | Pre-fill knowns, ask 3-5 delta questions | ~60-80% fewer questions |
| Phase 3: Research | Generic research from scratch | Skip known areas, focus on gaps and new risks | ~50% less research |
| Phase 4: Execute | Full scan of everything | Incremental scan, pattern verification, smart diff | ~40-70% faster execution |
| Cross-project | No prior knowledge | Pattern library, hypothesis-driven scan | ~30% faster first scan |

## Output Directory Structure (with Memory)

```
project-structure-scan/
├── memory/
│   ├── agent_memory.db              ← SQLite: structured long-term memory
│   └── index.md                     ← Memory index and usage description
├── config/
│   ├── triggers.md                  ← Configurable trigger mechanisms
│   ├── raci.md                      ← Configurable RACI matrix
│   ├── skills-and-knowledge.md      ← Configurable skills + knowledge base
│   ├── tools.md                     ← Configurable tools list
│   └── mcp-tools.md                 ← Configurable MCP tools list
├── templates/
│   ├── structure-tree-template.md   ← OUT-01 template
│   ├── module-relationship-template.md  ← OUT-02 template
│   ├── layering-analysis-template.md    ← OUT-03 template
│   ├── dependency-map-template.md       ← OUT-04 template
│   ├── module-summary-template.md       ← OUT-05 template
│   └── scan-report-template.md          ← OUT-06 template
├── research/                        ← Research processes and results
├── diagrams/                        ← Generated Mermaid/PlantUML diagrams
├── logs/
│   ├── conversation-log.md          ← Req 11: user conversation log
│   └── work-log.md                  ← Req 12: agent work log
├── phase1-questions.md              ← Req 16: Phase 1 question list
├── phase2-questions.md              ← Req 16: Phase 2 question list
├── phase3-questions.md              ← Req 16: Phase 3 question list
├── validated-requirements.md        ← Validated scan requirements
├── project-structure-report.md      ← OUT-06: final comprehensive report
├── scripts/
│   └── verify_dod.py                ← DoD verification script
├── references/
│   ├── dod.md                       ← Req 9: DoD quality gates
│   ├── dor.md                       ← Req 10: DoR prerequisites
│   ├── sop.md                       ← Req 8: SOP process
│   └── output-templates.md          ← Output template reference
└── SKILL.md                         ← Main skill definition file
```

---

# Functional Requirements: Interactive AI Agent Workflow

This AI Agent must be highly interactive. When the AI Agent receives a target codebase to scan, referred to as the **Target Project**:

- **Step 0 (Project Intake)**: Before any analysis begins, the AI Agent MUST collect the target project information from the user. The agent asks the following questions interactively (skipping any already provided via trigger parameters):
  1. **Project local path** (REQUIRED): "What is the local file path of the project you want me to scan?" — validate path exists with `ls {path}`
  2. **Git repository URL** (OPTIONAL): "Is this project in a Git repository? If so, what is the remote URL?" — validate with `git -C {path} status`
  3. **Git branch** (OPTIONAL): "Which branch should I scan? (default: current branch)" — validate branch exists
  4. **Project name** (REQUIRED): "What is the project name? (I can infer from the directory name if you prefer)"
  5. **Scan scope** (REQUIRED): "Should I scan the entire project, or focus on specific modules/directories?" — options: full / partial / exclude-list
  6. **Directories to exclude** (CONDITIONAL): Only if scope is partial/exclude — "Which directories should I exclude?"
  7. **Scan purpose** (REQUIRED): "Why do you need this project structure scan?"
  After collecting and validating all items, the agent presents a **Project Intake Summary** to the user for confirmation. User confirms → proceed to Step 1. User rejects → re-ask corrected items. The confirmed intake is stored in SQLite (`scan_history` and `knowledge_base`) for future re-invocations.

- **Step 1 (Understand Task Purpose)**: The AI Agent first tries to understand the purpose of performing a Project Structure Scan on this specific project. It presents its understanding to the user (e.g., "We need to scan this project because a new feature is being planned, and we need to understand the existing structure before designing the extension"). The user confirms → proceed to Step 2. The user rejects → the AI Agent refines its understanding and repeats Step 1 until the user fully agrees.

- **Step 2 (Understand the Target Project)**: The AI Agent tries to understand the target codebase — what domain it belongs to, what technology stack it uses, what scale it is (monolith vs. microservices, number of modules, approximate LOC). It presents its understanding to the user. The user confirms → proceed to Step 3. The user rejects → the AI Agent refines and repeats Step 2 until agreed.

- **Step 3 (Research & Question Generation)**: The AI Agent researches industry best practices for project structure analysis using the internet and authoritative knowledge bases. It tells the user how similar projects are typically analyzed in the industry, generates a comprehensive question list, and engages in iterative dialogue with the user based on the question list. The goal is to produce a **validated scan requirements list** — what exactly to scan, what to focus on, what to ignore, what output formats are expected.

- **Step 4 (Execute & Produce Deliverables)**: Based on the validated scan requirements list and the output templates, the AI Agent executes the actual scan of the codebase using tools (Glob, Grep, Read, Bash). It produces all deliverables (OUT-01 through OUT-06), runs DoD self-verification using `scripts/verify_dod.py`, records all memory entries in SQLite, and saves all outputs to the `project-structure-scan/` directory under the parent directory of the target project.

- **Step 5 (Transformation Target Deep-Dive Investigation)**: After the overall project structure is understood and deliverables OUT-01~06 are produced, the AI Agent conducts a focused investigation on the **specific transformation target** identified in the scan purpose. This step is triggered when the scan purpose involves any form of change, refactoring, feature addition, or system evolution. The agent:
  1. **Identify the transformation target**: Ask the user to confirm or specify the exact module(s), component(s), file(s), or functional area(s) that will be transformed. If already stated in Step 0 or Step 1, confirm and refine.
  2. **Investigate current state**: Using tools (Glob, Grep, Read, Bash), deeply investigate the transformation target's current implementation:
     - Current code structure and file layout within the target scope
     - Current responsibilities and behaviors (what it does today)
     - Current dependencies: what the target depends on (inbound) and what depends on the target (outbound)
     - Current data flows and interfaces (APIs, events, shared state)
     - Current test coverage (unit/integration tests present or absent)
     - Known technical debt, code smells, or anti-patterns within the target
     - Configuration and environment dependencies
  3. **Identify transformation constraints**: Based on the current state investigation, identify:
     - Hard constraints (things that cannot change — public APIs, database schemas, SLAs)
     - Soft constraints (things that should be preserved if possible)
     - Risk areas (high-coupling zones, untested code, shared state)
  4. **Present Current State Summary**: The agent presents a structured **Transformation Target Current State Report** to the user, covering all findings above. The user confirms → proceed to Step 6. The user rejects or requests deeper investigation → the agent refines and repeats until agreed.
  5. **Save to memory**: Record all findings in SQLite (`task_memory` with `memory_type = 'finding'` and `phase = 'phase5'`) and save the Current State Report as `OUT-07` in the output directory.

  > **OUT-07: Transformation Target Current State Report** — A focused report on the specific area to be transformed, documenting its current implementation, dependencies, interfaces, test coverage, constraints, and risk areas. This report serves as the baseline for transformation design.

- **Step 6 (Completion & Handoff)**: The AI Agent runs final DoD verification across all outputs (OUT-01 through OUT-07), triggers the Supervisor Agent for quality inspection, and upon 100% pass, notifies the Project Manager AI Agent with all deliverable paths and the RACI matrix for downstream task triggering.
