
# Create an AI Agent Skill for Completing the "Transformation Target Current State Analysis" Task. Details as follows:

# Basic Requirements:

- **Requirement 1**: Collect the trigger mechanisms for a qualified Transformation Target Current State Analysis AI Agent. Define what events or conditions trigger this task (e.g., PM Agent assigns task SA-TRF-001 via RACI matrix, user designates a specific method or component for transformation, Project Structure Scan SA-DISC-001 completes and a transformation target is identified, refactoring initiative begins on a specific module). Create a configurable trigger file that supports future modifications.

- **Requirement 2**: Collect the RACI matrix for a qualified Transformation Target Current State Analysis AI Agent. The RACI matrix must include both role names AND corresponding task names. Create a configurable RACI file with two purposes: Purpose 1 — allow the AI Agent to know all stakeholders each time it starts; Purpose 2 — after the AI Agent completes the task, send this RACI matrix to the Project Manager AI Agent to help the PM Agent trigger downstream tasks (e.g., Transformation Design Agent, Test Coverage Agent). Support future modifications.

- **Requirement 3**: Collect the skills a qualified Transformation Target Current State Analysis AI Agent should possess (e.g., code reading and deep comprehension, dependency graph tracing (inbound and outbound), API contract and interface analysis, data flow and event tracing, test coverage assessment, technical debt and code smell identification, anti-pattern recognition, configuration and environment dependency mapping, coupling metrics analysis, refactoring risk assessment). Create a configurable skills file that the AI Agent loads on startup. Support future modifications.

- **Requirement 4**: Collect the knowledge base a qualified Transformation Target Current State Analysis AI Agent should have (e.g., software design patterns — GoF Creational/Structural/Behavioral, SOLID principles, Clean Code principles, technical debt taxonomy — Cunningham/Fowler classification, code smell catalogue — Fowler's 24 smells, refactoring catalogue — Fowler's Refactoring 2nd Ed., coupling and cohesion metrics, API contract principles — REST/GraphQL/gRPC/Event contracts, test coverage standards — line/branch/mutation, dependency inversion and injection patterns, architectural layering patterns for context understanding). Create a configurable knowledge file that the AI Agent loads on startup. Support future modifications.

- **Requirement 5**: Collect the tools a qualified Transformation Target Current State Analysis AI Agent should use (e.g., Glob for locating target files and related components, Grep for tracing usages, references, and callers, Read for deep code reading and analysis, Bash for test execution, coverage reporting, call graph generation, dependency listing commands per ecosystem). Create a configurable tools file that the AI Agent loads on startup. Support future modifications.

- **Requirement 6**: Collect the MCP tools a qualified Transformation Target Current State Analysis AI Agent should use (e.g., context7 for authoritative documentation lookup on frameworks used by the target, IDE diagnostics for type analysis and symbol resolution, code intelligence tools for call graph and reference traversal). Create a configurable MCP tools file that the AI Agent loads on startup. Support future modifications.

- **Requirement 7**: Collect the output deliverables a qualified Transformation Target Current State Analysis AI Agent should produce, and create a template for each output item. The AI Agent loads these templates on startup and strictly follows them when producing outputs. Support future modifications. The output deliverables include:
  - **OUT-01**: Transformation Target Code Structure Map — annotated file and directory layout of the target scope, showing all files involved, their roles, and line counts
  - **OUT-02**: Current Responsibility & Behavior Analysis — what the target does today: every responsibility, behavior, side effect, and entry/exit point documented
  - **OUT-03**: Dependency Map (Inbound & Outbound) — what the target depends on (outbound) and what depends on the target (inbound), with interface contracts documented
  - **OUT-04**: Data Flow & Interface Analysis — all data flows through the target: APIs, events, shared state, database interactions, external integrations
  - **OUT-05**: Test Coverage Assessment — existing unit and integration test inventory, coverage percentages, untested paths, and coverage gap analysis
  - **OUT-06**: Technical Debt & Risk Register — identified code smells, anti-patterns, known issues, coupling hotspots, and transformation risk areas with severity ratings
  - **OUT-07**: Transformation Target Current State Report — enterprise-level consolidated report covering all findings above, including hard constraints, soft constraints, risk summary, and recommended investigation follow-ups. This report serves as the baseline for transformation design and must be confirmed by the user before any transformation work begins.

- **Requirement 8**: Collect the SOP process a qualified Transformation Target Current State Analysis AI Agent should follow. Create a configurable SOP file that the AI Agent loads on startup. Support future modifications.

- **Requirement 9**: Collect the DoD (Definition of Done) quality gates a qualified Transformation Target Current State Analysis AI Agent must satisfy. Create a configurable DoD file that the AI Agent loads on startup. Support future modifications.

- **Requirement 10**: Collect the DoR (Definition of Ready) prerequisites a qualified Transformation Target Current State Analysis AI Agent must verify before starting (e.g., target project repository is cloned and accessible locally, transformation target (method/component/module) is explicitly identified, read permissions on target files are available, project build system or language ecosystem is known, no active merge conflicts in the target scope). Create a configurable DoR file that the AI Agent loads on startup. Support future modifications.

- **Requirement 11**: The AI Agent must record every conversation with the user, question by question, logged entry by entry in a conversation log document (`logs/conversation-log.md`).

- **Requirement 12**: The AI Agent must record its own work log, entry by entry on a chronological timeline, in a work log document (`logs/work-log.md`).

- **Requirement 13**: The AI Agent must check against the DoD checklist whether the task is complete. If any check item fails, go back and fix the issue, then re-check until all items pass.

- **Requirement 14**: **[Supervisor AI Agent Skill Specification]** — Create a separate, independent **Supervisor AI Agent Skill (transformation-target-supervisor)** responsible for full quality inspection and closed-loop remediation of the Transformation Target Current State Analysis AI Agent's outputs. Specific requirements:

  ---

  ### 14.1 Role Definition
  - **Skill Name**: `transformation-target-supervisor`
  - **Role**: Quality Supervisor — independent from the Transformation Target Current State Analysis Agent, does not participate in the analysis itself, only responsible for inspection and feedback.
  - **Trigger Timing**: Automatically triggered after the Transformation Target Current State Analysis AI Agent completes one round of output.
  - **Execution Mechanism**: This Skill automatically inspects the AI Agent's outputs and generates a structured inspection report.

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
  | ✅ Req 7 | All output templates have been generated (OUT-01 through OUT-07) |
  | ✅ Req 8 | SOP process file has been generated |
  | ✅ Req 9 | DoD quality gates file has been generated |
  | ✅ Req 10 | DoR prerequisites file has been generated |
  | ✅ Req 11 | User conversation log document exists (logged question by question) |
  | ✅ Req 12 | AI Agent work log document exists (logged entry by entry on timeline) |
  | ✅ Req 13 | DoD check results have passed, closed-loop remediation completed |

  ---

  ### 14.3 Inspection Process (Closed-Loop Mechanism)

  ```
  [Trigger] Transformation Target Current State Analysis Agent completes output
       ↓
  [Inspect] Supervisor Agent checks Requirements 1–13 item by item
       ↓
  [Generate Report] Output inspection report (see 14.4)
       ↓
  [Decide] Report pass rate = 100%?
       ├── No → Send report back to Transformation Target Agent,
       │         request item-by-item remediation.
       │         After remediation, re-trigger Supervisor Agent.
       │         (Repeat this loop until 100% pass)
       └── Yes → Call Project Manager AI Agent, submit completion report
  ```

  ---

  ### 14.4 Inspection Report Format

  Each inspection generates a structured report in the following format:

  ```markdown
  # Transformation Target Supervisor Inspection Report

  - Inspection Time: {timestamp}
  - Inspection Round: Round {N}
  - Transformation Target: {target_method_or_component}
  - Output Directory: {output_directory_path}

  ## Inspection Results Summary

  | Check Item | Status | Notes |
  | :--- | :---: | :--- |
  | Req 1: Trigger Config | ✅ Pass / ❌ Fail | {notes} |
  | Req 2: RACI Matrix Config | ✅ Pass / ❌ Fail | {notes} |
  | Req 3: Skills List | ✅ Pass / ❌ Fail | {notes} |
  | Req 4: Knowledge Base | ✅ Pass / ❌ Fail | {notes} |
  | Req 5: Tools List | ✅ Pass / ❌ Fail | {notes} |
  | Req 6: MCP Tools List | ✅ Pass / ❌ Fail | {notes} |
  | Req 7: Output Templates (OUT-01~07) | ✅ Pass / ❌ Fail | {notes} |
  | Req 8: SOP File | ✅ Pass / ❌ Fail | {notes} |
  | Req 9: DoD File | ✅ Pass / ❌ Fail | {notes} |
  | Req 10: DoR File | ✅ Pass / ❌ Fail | {notes} |
  | Req 11: Conversation Log | ✅ Pass / ❌ Fail | {notes} |
  | Req 12: Work Log | ✅ Pass / ❌ Fail | {notes} |
  | Req 13: DoD Self-Check Passed | ✅ Pass / ❌ Fail | {notes} |

  ## Overall Pass Rate: {X}% ({M}/13 items passed)

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
       - Transformation Target Current State Report path (`OUT-07`) and all deliverable file paths (OUT-01 through OUT-06)
       - RACI matrix configuration (for PM Agent to trigger downstream transformation design tasks)
       - Final inspection report

- **Requirement 15**: After the AI Agent completes the task, notify the Project Manager AI Agent that task SA-TRF-001 is done, and send all deliverable file paths and names to the PM Agent. The PM Agent uses the RACI matrix from this task to call the corresponding AI Agents for downstream tasks (e.g., Transformation Design Agent, Test Strategy Agent).

- **Requirement 16**: Record all question lists generated in each phase, saved in dedicated phase question files (`phase1-questions.md`, `phase2-questions.md`, `phase3-questions.md`) for future review.

- **Requirement 17**: When the AI Agent uses tools to conduct research and code investigation, save all research processes, tool invocation records, and results in the `research/` directory locally for future use.

---

# Long-Term Memory Architecture (Hybrid: Markdown + SQLite)

The AI Agent must maintain **long-term memory** across sessions using a hybrid storage strategy. This ensures the agent can recall past analyses, decisions, and lessons learned when re-invoked on the same or similar transformation targets.

## Memory Storage Principle

| Data Type | Storage | Reason |
|-----------|---------|--------|
| Conversation logs, work logs, research reports | **Markdown** | Human-reviewable, Git-trackable, AI-native friendly |
| Task state, execution progress, DoD check results | **SQLite** | Requires structured queries (e.g., "which DoD items failed?") |
| Cross-session memory (findings, decisions, lessons, constraints) | **SQLite** | Requires persistent retrieval (e.g., "what constraints did we find last time analyzing this target?") |
| Configuration files (RACI, triggers, tools list) | **Markdown** | Human-editable, version-controlled |

## SQLite Database Design

The AI Agent must initialize and maintain `memory/agent_memory.db` with the following schema:

```sql
-- Task execution memory: records findings, decisions, constraints, and lessons per session
CREATE TABLE IF NOT EXISTS task_memory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id TEXT NOT NULL,
    task_id TEXT NOT NULL,           -- e.g., 'SA-TRF-001'
    project_name TEXT,               -- target project being analyzed
    target_name TEXT,                -- target method/component/module name
    target_path TEXT,                -- file path(s) of the target
    phase TEXT,                      -- e.g., 'phase1', 'phase2', 'phase3', 'phase4'
    memory_type TEXT NOT NULL,       -- 'finding', 'decision', 'lesson', 'question', 'risk', 'constraint'
    title TEXT,
    content TEXT NOT NULL,
    context TEXT,                    -- related module/file/line for traceability
    tags TEXT,                       -- comma-separated tags (e.g., 'dependency,hard-constraint,api')
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- DoD check records: tracks pass/fail status per check item per session
CREATE TABLE IF NOT EXISTS dod_checks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id TEXT NOT NULL,
    task_id TEXT NOT NULL,
    check_round INTEGER NOT NULL,    -- inspection round number
    check_item TEXT NOT NULL,        -- e.g., 'req_01_trigger_config'
    status TEXT NOT NULL,            -- 'pass', 'fail', 'pending'
    evidence TEXT,                   -- file path or description proving the status
    notes TEXT,
    checked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Cross-session knowledge base: accumulates reusable insights across targets and projects
CREATE TABLE IF NOT EXISTS knowledge_base (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_name TEXT NOT NULL,
    target_name TEXT,                -- specific method/component if applicable
    category TEXT NOT NULL,          -- 'constraint', 'dependency', 'risk', 'pattern', 'debt', 'tech_stack', 'interface'
    key TEXT NOT NULL,
    value TEXT NOT NULL,
    confidence REAL DEFAULT 0.8,     -- 0.0 to 1.0
    source TEXT,                     -- where this knowledge came from (file path, tool output, user input)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Analysis history: records each analysis execution for traceability
CREATE TABLE IF NOT EXISTS analysis_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id TEXT NOT NULL,
    task_id TEXT NOT NULL,
    project_name TEXT NOT NULL,
    project_path TEXT NOT NULL,
    target_name TEXT NOT NULL,       -- method/component/module being analyzed
    target_path TEXT NOT NULL,       -- file path(s) of the target
    analysis_scope TEXT,             -- full analysis, partial analysis, incremental
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
2. Query `analysis_history` for previous analyses of the same target: `SELECT * FROM analysis_history WHERE project_name = ? AND target_name = ? ORDER BY started_at DESC LIMIT 5`
3. Query `knowledge_base` for accumulated knowledge about the target: `SELECT * FROM knowledge_base WHERE project_name = ? AND target_name = ? ORDER BY confidence DESC`
4. Query `task_memory` for lessons learned from previous sessions: `SELECT * FROM task_memory WHERE task_id = 'SA-TRF-001' AND target_name = ? AND memory_type = 'lesson' ORDER BY created_at DESC LIMIT 20`
5. Present relevant historical context to user before beginning the analysis.

### During Execution
1. After each significant finding (dependency, interface, behavior), insert into `task_memory` with `memory_type = 'finding'`.
2. After identifying a hard or soft constraint, insert into `task_memory` with `memory_type = 'constraint'`.
3. After each key decision (e.g., scope boundary agreed with user), insert into `task_memory` with `memory_type = 'decision'`.
4. After each user Q&A exchange, insert into `task_memory` with `memory_type = 'question'`.
5. After identifying a risk area, insert into `task_memory` with `memory_type = 'risk'`.

### On Completion
1. Insert analysis record into `analysis_history` with `status = 'completed'`.
2. Extract key insights (constraints, interface contracts, risk hotspots) and insert into `knowledge_base` for future reuse.
3. Insert lessons learned into `task_memory` with `memory_type = 'lesson'`.
4. Run all DoD checks and record results in `dod_checks`.

### On Re-invocation (Same Target)
1. Load previous analysis results and present delta/changes to user.
2. Offer incremental analysis option (only re-investigate changed files) instead of full re-analysis.
3. Validate whether previously identified constraints and interfaces still hold.

---

## Memory Utilization Protocol — How Memory Drives Agent Behavior

The core principle: **Memory is not just storage — it must actively shape the Agent's decisions, questions, focus areas, and outputs at every phase.** Below defines exactly how the Agent must use memory at each workflow step.

### Phase 0 (Startup): Memory-Driven Context Loading

```
[Agent Starts]
    ↓
[Query analysis_history] → Has this target been analyzed before?
    ├── YES → Enter "Re-analysis Mode" (see below)
    └── NO  → Query knowledge_base for SIMILAR targets in the same project
                 ├── Found similar → Pre-load patterns, present to user:
                 │   "I've analyzed similar components before. Component X had
                 │    a hard constraint on its public API and high coupling to
                 │    the persistence layer. Should I look for similar patterns here?"
                 └── Not found → Enter "Fresh Analysis Mode" (standard workflow)
```

**Re-analysis Mode Behavior:**
1. Load previous analysis's `OUT-07` (Current State Report) and all OUT-01~06 deliverables.
2. Query: `SELECT * FROM task_memory WHERE target_name = ? AND memory_type IN ('finding', 'risk', 'constraint', 'lesson') ORDER BY created_at DESC`
3. Present a **Memory Summary** to the user:
   ```
   📋 Previous Analysis Summary (Session: {session_id}, Date: {date}):
   - Target: {target_name} at {target_path}
   - Hard Constraints Found: {constraint_list}
   - Key Dependencies: {dependency_list}
   - Risk Areas: {risk_list}
   - Test Coverage: {coverage_pct}%
   - Lessons Learned: {lesson_list}
   - Last DoD Pass Rate: {rate}%

   Would you like to:
   (a) Run an incremental analysis (only re-investigate changed files)
   (b) Run a full re-analysis (ignore previous results)
   (c) Review and update previous findings
   ```
4. If user selects incremental analysis → Agent compares current file state with previous OUT-01, only re-investigates modified or new files.

### Phase 1 (Understand Task Purpose): Memory-Enhanced Understanding

**Without Memory** (standard): Agent guesses why the transformation is needed.

**With Memory** (enhanced):
1. Query: `SELECT * FROM task_memory WHERE target_name = ? AND memory_type = 'decision' AND phase = 'phase1'`
2. If previous purpose records exist, present them:
   ```
   "Last time we analyzed this target, the transformation purpose was: {previous_purpose}.
    Is the purpose the same this time, or has it changed?"
   ```
3. Query: `SELECT * FROM task_memory WHERE memory_type = 'lesson' AND phase = 'phase1'`
4. If lessons exist (e.g., "user cared most about backward compatibility"), proactively incorporate:
   ```
   "Based on previous experience with this target, I know backward compatibility
    is a top priority. I'll make sure to flag any finding that could affect external callers."
   ```

### Phase 2 (Understand Target Method/Component): Memory-Accelerated Discovery

**Without Memory**: Agent asks many basic questions about the target from scratch.

**With Memory**:
1. Query: `SELECT * FROM knowledge_base WHERE target_name = ? AND category IN ('tech_stack', 'interface', 'dependency', 'constraint')`
2. Pre-fill known answers and only ask about unknowns:
   ```
   "Based on my records, this target:
    - Language: Java 17
    - Framework: Spring Boot 3.x
    - Known Callers: {caller_list}
    - Known Dependencies: {dependency_list}
    - Previous Hard Constraint: public API {api_name} cannot be changed

    Has any of this changed? And I have a few new questions: ..."
   ```
3. Query: `SELECT * FROM task_memory WHERE target_name = ? AND memory_type = 'question' AND phase = 'phase2'`
4. Skip questions already answered in previous sessions (unless user indicates changes).
5. **Time saved**: Instead of 15 discovery questions, only ask 3-5 delta questions.

### Phase 3 (Research & Question Generation): Memory-Informed Research

**Without Memory**: Agent researches generic refactoring best practices.

**With Memory**:
1. Query: `SELECT * FROM task_memory WHERE target_name = ? AND memory_type = 'finding' AND phase = 'phase3'`
2. Load previous research results from `research/` directory.
3. Query: `SELECT * FROM knowledge_base WHERE category IN ('risk', 'debt', 'pattern') AND confidence >= 0.7`
4. **Skip redundant research**: If the agent already identified the coupling risks in the previous session, skip re-researching and go directly to targeted gap questions.
5. **Focus on gaps**: Generate questions only about areas NOT covered in previous sessions:
   ```
   "In previous sessions, we covered dependency mapping and interface contracts.
    This time I'd like to focus on:
    1. Any new callers added since last analysis?
    2. Has test coverage changed?
    3. Are previously identified risks still present?"
   ```
6. Query: `SELECT * FROM task_memory WHERE memory_type = 'risk'`
7. **Proactively revisit known risks**:
   ```
   "Last time I identified these risks:
    - Risk 1: {target_name} has tight coupling to {component_x} via shared mutable state
    - Risk 2: No unit tests cover the {method_y} code path
    Should I verify if these have been resolved?"
   ```

### Phase 4 (Investigate & Produce Deliverables): Memory-Optimized Execution

**Without Memory**: Agent investigates everything from scratch.

**With Memory**:
1. **Incremental Investigation Strategy**:
   ```
   [Load previous OUT-01 code structure map]
       ↓
   [Glob + Read current target files]
       ↓
   [Diff: identify ADDED / REMOVED / MODIFIED files in target scope]
       ↓
   [Only deep-investigate changed areas]
       ↓
   [Merge: update previous deliverables with new findings]
   ```

2. **Constraint Confirmation**:
   - Query: `SELECT * FROM knowledge_base WHERE target_name = ? AND category = 'constraint'`
   - Instead of re-discovering all constraints, verify they still hold:
     ```sql
     -- If previous finding: "hard constraint: public API interface X cannot change, confidence = 0.95"
     -- Agent checks: does interface X still exist? Is its signature unchanged?
     -- If yes → keep constraint, update confidence
     -- If no → flag as "constraint lifted", alert user
     UPDATE knowledge_base SET confidence = ?, updated_at = CURRENT_TIMESTAMP
     WHERE target_name = ? AND category = 'constraint' AND key = ?
     ```

3. **Smart Dependency Diff**:
   - Load previous OUT-03 (Dependency Map)
   - Compare with current import statements, call graph, and dependency manifests
   - Report only: new dependencies added, dependencies removed, interface contract changes
   - Flag: any new coupling that increases transformation risk

4. **Quality Improvement Over Time**:
   - Query: `SELECT check_item, status, notes FROM dod_checks WHERE task_id = 'SA-TRF-001' AND status = 'fail' ORDER BY checked_at DESC`
   - If previous DoD failures exist, **proactively address them first**:
     ```
     "In the last analysis, these DoD items failed:
      - {check_item}: {notes}
      I will prioritize addressing these in this round."
     ```

### Cross-Target Knowledge Transfer

When analyzing a **new target** in the same or similar project:

1. Query: `SELECT DISTINCT target_name, category, key, value, confidence FROM knowledge_base WHERE project_name = ? AND confidence >= 0.8 ORDER BY category`
2. Build a **pattern library** from all previously analyzed targets in this project.
3. Use pattern matching to accelerate analysis:
   ```
   "I've analyzed 4 components in this project before. Based on the package structure,
    this target most closely resembles {target_x} which had high coupling to the
    persistence layer and a hard constraint on its service interface.
    I'll use that as my initial hypothesis and verify."
   ```
4. After analysis completes, compare findings with the hypothesis and record accuracy:
   ```sql
   INSERT INTO task_memory (session_id, task_id, project_name, target_name, phase,
     memory_type, title, content)
   VALUES (?, 'SA-TRF-001', ?, ?, 'phase4', 'lesson',
     'Cross-target pattern prediction accuracy',
     'Predicted high persistence coupling based on similarity to {target_x}.
      Actual: medium coupling via repository pattern. Partial match.
      Note: service-layer components in this project vary in coupling style.')
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

2. **Contradiction detection**: If a new finding contradicts an existing `knowledge_base` entry:
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
   "I have some low-confidence memories about this target that may be outdated:
    - {key}: {value} (confidence: 0.2)
    Should I discard these or re-verify?"
   ```

### Memory Utilization Summary Per Phase

| Phase | Without Memory | With Memory | Time Savings |
|-------|---------------|-------------|-------------|
| Phase 0: Startup | Cold start, no context | Load history, present summary, offer incremental analysis | Skip entire re-discovery |
| Phase 1: Purpose | Guess from scratch | Recall previous purpose, ask for delta only | ~70% fewer questions |
| Phase 2: Understand Target | Ask 15+ basic questions | Pre-fill knowns, ask 3-5 delta questions | ~60-80% fewer questions |
| Phase 3: Research | Generic research from scratch | Skip known areas, focus on gaps and new risks | ~50% less research |
| Phase 4: Investigate | Full deep-dive of everything | Incremental diff, constraint verification, smart dependency diff | ~40-70% faster execution |
| Cross-target | No prior knowledge | Pattern library, hypothesis-driven analysis | ~30% faster first analysis |

---

## Output Directory Structure (with Memory)

```
transformation-target-current-state/
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
│   ├── code-structure-map-template.md        ← OUT-01 template
│   ├── responsibility-analysis-template.md   ← OUT-02 template
│   ├── dependency-map-template.md            ← OUT-03 template
│   ├── data-flow-analysis-template.md        ← OUT-04 template
│   ├── test-coverage-report-template.md      ← OUT-05 template
│   ├── tech-debt-risk-register-template.md   ← OUT-06 template
│   └── current-state-report-template.md      ← OUT-07 template
├── research/                        ← Research processes and tool invocation results (Req 17)
├── logs/
│   ├── conversation-log.md          ← Req 11: user conversation log (per question)
│   └── work-log.md                  ← Req 12: agent work log (chronological timeline)
├── phase1-questions.md              ← Req 16: Phase 1 question list
├── phase2-questions.md              ← Req 16: Phase 2 question list
├── phase3-questions.md              ← Req 16: Phase 3 question list
├── validated-requirements.md        ← Confirmed analysis scope and requirements
├── OUT-01-code-structure-map.md     ← Target code structure map
├── OUT-02-responsibility-analysis.md ← Current responsibility & behavior analysis
├── OUT-03-dependency-map.md         ← Inbound and outbound dependency map
├── OUT-04-data-flow-analysis.md     ← Data flows and interface analysis
├── OUT-05-test-coverage-report.md   ← Test coverage assessment
├── OUT-06-tech-debt-risk-register.md ← Technical debt and risk register
├── OUT-07-current-state-report.md   ← Enterprise-level consolidated current state report
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

This AI Agent must be highly interactive. When the AI Agent receives a transformation target designation, referred to as the **Target**:

- **Step 0 (Target Intake)**: Before any analysis begins, the AI Agent MUST collect the transformation target information from the user. The agent asks the following questions interactively (skipping any already provided via trigger parameters):
  1. **Project local path** (REQUIRED): "What is the local file path of the project containing the target?" — validate path exists with `ls {path}`
  2. **Transformation target** (REQUIRED): "What is the specific method, class, component, or module you want to transform? Please provide the name and file path." — validate file exists with `ls {path}`
  3. **Transformation intent** (REQUIRED): "What do you intend to change about this target? (e.g., extract to a service, add caching, split responsibilities, migrate to async)"
  4. **Analysis scope** (REQUIRED): "Should I analyze only the target itself, or should I also include closely related components that interact with it?" — options: target-only / include-direct-dependencies / broad
  5. **Known constraints** (OPTIONAL): "Are there any known constraints I should be aware of upfront? (e.g., this API is used by external clients, database schema cannot change)"
  6. **Project name** (REQUIRED): "What is the project name? (I can infer from the directory name if you prefer)"

  After collecting and validating all items, the agent presents a **Target Intake Summary** to the user for confirmation. User confirms → proceed to Step 1. User rejects → re-ask corrected items. The confirmed intake is stored in SQLite (`analysis_history` and `knowledge_base`) for future re-invocations.

- **Step 1 (Understand Task Purpose)**: The AI Agent first tries to understand the purpose of the transformation — why this method or component needs to change, what problem it solves, and what outcome is expected. It presents its understanding to the user (e.g., "We need to analyze this method because you intend to extract its orchestration logic into a dedicated service, improving single-responsibility and testability"). The user confirms → proceed to Step 2. The user rejects → the AI Agent refines its understanding and repeats Step 1 until the user fully agrees.

- **Step 2 (Understand the Target)**: The AI Agent tries to understand the target at a high level — what it belongs to, what technology stack it uses, its approximate size (lines of code, number of callers, number of dependencies). It presents its understanding to the user. The user confirms → proceed to Step 3. The user rejects → the AI Agent refines and repeats Step 2 until agreed.

- **Step 3 (Research & Question Generation)**: The AI Agent researches industry best practices for analyzing transformation targets using the internet and authoritative knowledge bases. It tells the user how similar transformations are typically analyzed in the industry, generates a comprehensive question list, and engages in iterative dialogue with the user based on the question list. The goal is to produce a **validated analysis requirements list** — exactly what to investigate, what to focus on, what depth is required, what output format is expected.

- **Step 4 (Investigate Current State & Produce Deliverables)**: Based on the validated analysis requirements list and the output templates, the AI Agent executes the deep investigation using tools (Glob, Grep, Read, Bash). It produces deliverables OUT-01 through OUT-06, then consolidates them into the enterprise-level **OUT-07: Transformation Target Current State Report**. Specifically:

  1. **Investigate current state** using tools (Glob, Grep, Read, Bash):
     - Current code structure and file layout within the target scope → **OUT-01**
     - Current responsibilities and behaviors (what it does today) → **OUT-02**
     - Current dependencies: what the target depends on (outbound) and what depends on the target (inbound) → **OUT-03**
     - Current data flows and interfaces (APIs, events, shared state) → **OUT-04**
     - Current test coverage (unit/integration tests present or absent) → **OUT-05**
     - Known technical debt, code smells, or anti-patterns within the target → **OUT-06**
     - Configuration and environment dependencies → included in **OUT-06**

  2. **Identify transformation constraints** based on the current state investigation:
     - Hard constraints (things that cannot change — public APIs, database schemas, SLAs, contracts with external systems)
     - Soft constraints (things that should be preserved if possible — internal conventions, performance characteristics, error handling behavior)
     - Risk areas (high-coupling zones, untested code paths, shared mutable state, complex initialization logic)

  3. **Present Current State Summary**: The agent compiles all findings into the structured **OUT-07: Transformation Target Current State Report** and presents it to the user. The user confirms → proceed to Step 5. The user rejects or requests deeper investigation → the agent refines and repeats until agreed.

  4. **Save to memory**: Record all findings in SQLite (`task_memory` with `memory_type = 'finding'` and `memory_type = 'constraint'` and `phase = 'phase4'`) and save all deliverables to the output directory.

- **Step 5 (DoD Self-Verification & Completion)**: The AI Agent runs `scripts/verify_dod.py` to verify all DoD items pass. If any DoD item fails, the agent goes back to fix the issue and re-runs verification until 100% pass. Then it triggers the Supervisor Agent (`transformation-target-supervisor`) for independent quality inspection. Upon 100% Supervisor pass, it notifies the Project Manager AI Agent with all deliverable paths and the RACI matrix for downstream transformation design task triggering.
