# SOP: Transformation Target Current State Analysis (SA-TRF-001)

> Standard Operating Procedure for the Transformation Target Current State Analysis AI Agent.
> Defines detailed sub-steps for each of the 5 operational steps (Step 0 through Step 5).

---

## Step 0: Target Intake (Interactive)

### Part A: Target Information Collection

| Sub-Step | Description |
|----------|-------------|
| 0A-1 | Check trigger payload for pre-supplied parameters (project_path, target_name, target_path, transformation_intent, analysis_scope, known_constraints, project_name) |
| 0A-2 | Identify missing required parameters from trigger payload |
| 0A-3 | For each missing required item, ask user interactively: Project path → validate with `ls {path}`; Target name + path → validate with `ls {target_path}`; Transformation intent → must be non-empty; Analysis scope → present 3 options |
| 0A-4 | Ask optional items if contextually relevant: Known constraints, project name (can infer from directory) |
| 0A-5 | Validate all inputs per DoR checklist (see `references/dor.md`) |
| 0A-6 | Present Target Intake Summary to user for confirmation |
| 0A-7 | If user rejects → re-ask corrected items; if confirms → proceed to Part B |
| 0A-8 | Insert record into `analysis_history` (status = 'in_progress') and `knowledge_base` for project/target info |

### Part B: System Initialization

| Sub-Step | Description |
|----------|-------------|
| 0B-1 | Run all DoR checks. Halt if any mandatory check fails |
| 0B-2 | Create output directory: `outputs/analysis-{YYYYMMDD-HHMMSS}/` |
| 0B-3 | Initialize/open SQLite memory DB. Run `scripts/init_memory.py` if DB doesn't exist |
| 0B-4 | Query `analysis_history` for previous analyses of same target. Load prior findings if found |
| 0B-5 | Determine analysis mode: Fresh (no prior) / Re-analysis (prior exists). Present mode to user |
| 0B-6 | If Re-analysis Mode: query `task_memory` and `knowledge_base`, present Memory Summary, offer options (incremental / full re-analysis / review previous findings) |
| 0B-7 | Apply confidence decay: reduce confidence by 0.2 for `knowledge_base` entries > 90 days old |

**Outputs**: Confirmed intake summary, session ID, initialized DB, output directory, analysis mode

---

## Step 1: Understand Task Purpose (Interactive)

| Sub-Step | Description |
|----------|-------------|
| 1-1 | Query `task_memory` for previous purpose records (`memory_type = 'decision'`, `phase = 'phase1'`). If found, present previous purpose and ask if it still applies |
| 1-2 | Query `task_memory` for Phase 1 lessons (`memory_type = 'lesson'`, `phase = 'phase1'`). Apply relevant lessons proactively |
| 1-3 | Formulate understanding of transformation purpose from intake data: why this target needs to change, what problem it solves, expected outcome |
| 1-4 | Present understanding to user. User confirms → Step 2. User corrects → refine and repeat |
| 1-5 | `record_decision(phase='phase1', decision='purpose_confirmed', details={confirmed_purpose})` |
| 1-6 | Append Phase 1 Q&A to `logs/conversation-log.md`. Save question list to `phase1-questions.md` |

**Success Criteria**: User explicitly confirms purpose understanding

---

## Step 2: Understand the Target (Interactive)

| Sub-Step | Description |
|----------|-------------|
| 2-1 | Query `knowledge_base` for previously recorded tech stack, interface, dependency, constraint knowledge about this target |
| 2-2 | Pre-fill known answers. Perform lightweight probe: identify language from file extension + manifest, estimate LOC with `wc -l` |
| 2-3 | Ask delta questions only (skip previously answered): primary language, framework, approximate size (LOC/callers/dependencies), architectural context |
| 2-4 | Present project/target understanding summary. User confirms → Step 3. User corrects → refine |
| 2-5 | `record_knowledge(category='tech_stack', ...)` for each confirmed item |
| 2-6 | Append Phase 2 Q&A to `logs/conversation-log.md`. Save question list to `phase2-questions.md` |

**Success Criteria**: User confirms target understanding summary

---

## Step 3: Research & Question Generation (Interactive)

| Sub-Step | Description |
|----------|-------------|
| 3-1 | Load previous research from `research/` directory. Query `task_memory` for prior Phase 3 findings |
| 3-2 | Research industry best practices for analyzing this type of transformation using Context7 + WebSearch. Focus on gaps not covered in previous sessions |
| 3-3 | Proactively present known risks from `task_memory` (`memory_type = 'risk'`) and ask if they have been resolved |
| 3-4 | Generate comprehensive question list: module boundary conventions, known architectural decisions, areas of concern, performance/SLA requirements, external caller expectations |
| 3-5 | Engage in iterative dialogue with user based on question list. Refine until user is satisfied |
| 3-6 | Compile **validated analysis requirements list**: what to investigate, what depth, what to skip, expected output format |
| 3-7 | Save validated requirements to `validated-requirements.md` |
| 3-8 | Save research findings to `research/{topic}.md` |
| 3-9 | `record_finding()` for each research insight. `record_question()` for each Q&A. `record_risk()` for identified risks |
| 3-10 | Append Phase 3 Q&A to `logs/conversation-log.md`. Save question list to `phase3-questions.md` |

**Success Criteria**: Validated analysis requirements list agreed by user. Saved as `validated-requirements.md`

---

## Step 4: Investigate Current State & Produce Deliverables

| Sub-Step | Description |
|----------|-------------|
| 4-1 | Determine investigation strategy: Fresh (full investigation) or Incremental (diff against previous OUT-01) |
| 4-2 | **Produce OUT-01 (Code Structure Map)**: Use Glob + Bash (tree) to map target directory layout. Annotate each file with role and LOC |
| 4-3 | **Produce OUT-02 (Responsibility & Behavior Analysis)**: Read key implementation files. Document every responsibility, behavior, side effect, entry/exit point |
| 4-4 | **Produce OUT-03 (Dependency Map)**: Grep for all callers (inbound). Read all imports inside target (outbound). Document interface contracts |
| 4-5 | **Produce OUT-04 (Data Flow & Interface Analysis)**: Trace all data flows: APIs, events, shared state, DB interactions, external integrations |
| 4-6 | **Produce OUT-05 (Test Coverage Assessment)**: Glob for test files. Read test classes. Classify coverage level (High/Medium/Low/None) per test type. Identify untested paths |
| 4-7 | **Produce OUT-06 (Technical Debt & Risk Register)**: Grep for TODO/FIXME/HACK. Inspect for code smells, anti-patterns, hardcoded values. Rate severity |
| 4-8 | **Identify Transformation Constraints**: Classify hard constraints (cannot change), soft constraints (preserve if possible), risk areas (high-coupling, untested, shared state) |
| 4-9 | **Produce OUT-07 (Current State Report)**: Consolidate OUT-01~06 + constraints into enterprise-level report. Must include hard constraints, soft constraints, risk summary |
| 4-10 | Present OUT-07 summary to user. User confirms → Step 5. User requests more investigation → loop back to relevant sub-steps |
| 4-11 | `record_finding()` after each significant finding. `record_constraint()` for each constraint. `record_risk()` for each risk area |
| 4-12 | Log all actions to `logs/work-log.md` with timestamps |

**Memory Operations**: `record_finding()`, `record_constraint()`, `record_risk()`, `record_knowledge()`, `record_dod_check()`

**Success Criteria**: OUT-01 through OUT-07 produced, all templates populated, user confirms OUT-07

---

## Step 5: DoD Self-Verification & Completion

| Sub-Step | Description |
|----------|-------------|
| 5-1 | Run `python scripts/verify_dod.py --output-dir {output_dir} --session-id {session_id} --round 1` |
| 5-2 | For any failing DoD item, fix the issue and re-run verification. Repeat until 20/20 pass |
| 5-3 | `record_lesson()` for each insight from the analysis session |
| 5-4 | Update `analysis_history` record: `status = 'completed'`, record end timestamp, summary stats |
| 5-5 | Extract key insights to `knowledge_base` for future reuse |
| 5-6 | Trigger Supervisor Agent (`transformation-target-supervisor`). Pass all deliverable paths and DoD results |
| 5-7 | If Supervisor reports failures → remediate and re-trigger. Max 3 rounds before escalation |
| 5-8 | Notify PM Agent: deliverables path, file list (OUT-01~07), RACI matrix path, final inspection report, target summary |
| 5-9 | Finalize and close conversation log and work log |

**Success Criteria**: Supervisor passes 100%, PM Agent notified, downstream tasks triggered

---

## Cross-Step Rules

1. Every step must log start and end time in `logs/work-log.md`
2. Interactive steps (0, 1, 2, 3) must record dialogue in `logs/conversation-log.md`
3. All memory operations must succeed before proceeding. On failure, retry once then halt with error
4. Template placeholders (`{placeholder}`) must never remain in final outputs
5. Agent must not proceed past Step 0 if any mandatory DoR check fails
