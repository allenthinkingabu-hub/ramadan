# SOP: Project Structure Scan (SA-DISC-001)

> Standard Operating Procedure for the Project Structure Scan AI Agent skill.
> This document defines the detailed sub-steps for each of the 6 operational phases (Phase 0 through Phase 6, where Phase 5 is conditional).

---

## Phase 0: Initialization & Project Intake

### Part A: Project Intake (Interactive)

| Step | Sub-Step | Description |
|------|----------|-------------|
| 0A-1 | Check Trigger Parameters | Inspect the incoming trigger payload for pre-supplied parameters (project path, scan scope, purpose, exclude list). |
| 0A-2 | Identify Missing Required Items | Compare trigger parameters against the required intake checklist: project path, scan scope, purpose of scan. Compile a list of missing items. |
| 0A-3 | Prompt for Missing Required Items | Present the user with focused questions for each missing required item. Collect responses one item at a time. |
| 0A-4 | Prompt for Optional Items (if relevant) | If the project context suggests relevance, ask optional questions: directories to exclude, specific modules of interest, output format preferences, prior scan references. |
| 0A-5 | Validate All Inputs | Verify project path exists and is a directory, scan scope is one of (full / partial / exclude-list), and purpose string is non-empty. |
| 0A-6 | Present Intake Summary | Compile and display a formatted intake summary table showing all collected parameters, their values, and validation status. |
| 0A-7 | User Confirmation | Ask the user to explicitly confirm the intake summary. If rejected, loop back to the relevant step to correct. |
| 0A-8 | Store in SQLite | Persist the confirmed intake summary into the memory SQLite database (`scan_intake` table) with a unique scan ID and timestamp. |

- **Inputs:** Trigger parameters, user responses to intake questions.
- **Outputs:** Confirmed intake summary document, scan ID.
- **Memory Operations:** `start_scan()`, `record_knowledge(category='intake', key=<param>, value=<value>)`.

### Part B: System Initialization

| Step | Sub-Step | Description |
|------|----------|-------------|
| 0B-1 | Verify Definition of Ready (DoR) | Run all DoR checks (see `references/dor.md`). Halt and report if any mandatory check fails. |
| 0B-2 | Create Output Directory | Create the timestamped output directory under `outputs/` (e.g., `outputs/scan-YYYYMMDD-HHMMSS/`). |
| 0B-3 | Initialize Memory Database | Open or create the SQLite memory database. Run schema migrations if needed. Insert scan_history record with status `in_progress`. |
| 0B-4 | Load Project History | Query memory DB for previous scans of the same project path. Load prior findings, lessons learned, and known tech stack. |
| 0B-5 | Determine Scan Mode | Based on project history, determine scan mode: **fresh** (no prior scans), **re-scan** (prior scan exists, full re-execution), or **incremental** (prior scan exists, delta only). Present mode to user for confirmation. |

- **Inputs:** Confirmed intake summary, memory database.
- **Outputs:** Initialized memory DB, output directory, scan mode.
- **Memory Operations:** `start_scan()`, `record_knowledge(category='scan_mode', ...)`.

---

## Phase 1: Understand Task Purpose (Interactive)

| Step | Sub-Step | Description |
|------|----------|-------------|
| 1-1 | Load Previous Purpose | Query memory DB for any prior purpose statements related to this project. If found, present them as context. |
| 1-2 | Load Lessons Learned | Execute `load_lessons_learned(phase='phase1')` to retrieve any Phase 1 lessons from prior scans. Apply relevant adjustments. |
| 1-3 | Present Understanding | Formulate and present the agent's understanding of the scan purpose, incorporating intake data and historical context. |
| 1-4 | User Confirms Purpose | Ask the user to explicitly confirm or correct the purpose understanding. Loop until confirmed. |
| 1-5 | Record Decision | Execute `record_decision(phase='phase1', decision='purpose_confirmed', details=<confirmed purpose>)`. |
| 1-6 | Log Phase 1 Dialogue | Append the full Phase 1 conversation exchange to the conversation log (`logs/conversation-log.md`). |

- **Inputs:** Intake summary, prior purpose records.
- **Outputs:** Confirmed purpose statement.
- **Memory Operations:** `load_lessons_learned(phase='phase1')`, `record_decision()`.
- **Success Criteria:** User explicitly confirms purpose understanding.

---

## Phase 2: Understand Target Project (Interactive)

| Step | Sub-Step | Description |
|------|----------|-------------|
| 2-1 | Load Known Tech Stack | Query memory DB for previously recorded tech stack knowledge about this project (languages, frameworks, build tools). |
| 2-2 | Pre-fill Known Answers | Populate the project understanding template with any known information from prior scans or intake data. |
| 2-3 | Quick Filesystem Probe | Run a lightweight directory listing and manifest file detection (package.json, pom.xml, etc.) to auto-detect project type. |
| 2-4 | Ask Delta Questions | Present the user with questions only for information not already known or auto-detected: primary language, architecture style, deployment model, team structure. |
| 2-5 | User Confirms Understanding | Present the complete project understanding summary. Ask the user to confirm or correct. |
| 2-6 | Record Project Knowledge | Execute `record_knowledge(category='tech_stack', ...)` for each confirmed item. |
| 2-7 | Log Phase 2 Dialogue | Append the full Phase 2 conversation exchange to the conversation log. |

- **Inputs:** Prior project knowledge, filesystem probe results, user responses.
- **Outputs:** Confirmed project understanding document.
- **Memory Operations:** `load_project_knowledge()`, `record_knowledge()`.
- **Success Criteria:** User confirms project understanding.

---

## Phase 3: Research & Question Generation (Interactive)

| Step | Sub-Step | Description |
|------|----------|-------------|
| 3-1 | Load Previous Research | Query memory DB for prior research findings related to this project's tech stack and architecture patterns. |
| 3-2 | Conduct Industry Research | Based on the confirmed tech stack, research industry-standard patterns, common project structures, and best practices for the identified technologies. |
| 3-3 | Generate Scan Questions | Produce a prioritized list of questions that will guide the scan execution: What patterns to look for? What anti-patterns to flag? What depth of analysis per module? |
| 3-4 | Present Questions to User | Display the generated questions and proposed scan approach. Enter iterative dialogue to refine. |
| 3-5 | Iterative Refinement | Engage in back-and-forth with the user to refine questions, add context, and prioritize areas of interest. Continue until the user is satisfied. |
| 3-6 | Validate Requirements | Compile the final validated scan requirements list. Present for user agreement. |
| 3-7 | Save Questions | Write the finalized questions to `outputs/phase3-questions.md`. |
| 3-8 | Save Research | Write research findings to the `research/` directory with appropriate filenames. |
| 3-9 | Record in Memory | Execute `record_finding()` for each research insight. Execute `record_question()` for each finalized question. |
| 3-10 | Log Phase 3 Dialogue | Append the full Phase 3 conversation exchange to the conversation log. |

- **Inputs:** Project understanding, prior research, user refinements.
- **Outputs:** Validated scan requirements list, phase3-questions.md, research documents.
- **Memory Operations:** Load previous findings, `record_finding()`, `record_question()`.
- **Success Criteria:** Validated scan requirements list agreed by user.

---

## Phase 4: Execute & Produce Deliverables

| Step | Sub-Step | Description |
|------|----------|-------------|
| 4-1 | Determine Scan Strategy | Based on scan mode and validated requirements, plan the execution: which directories to scan first, depth limits, tool selection (glob, grep, read). |
| 4-2 | Scan Codebase — Directory Tree | Traverse the project directory tree, respecting exclude lists. Build the annotated structure hierarchy. |
| 4-3 | Scan Codebase — Module Detection | Identify logical modules based on directory structure, build files, namespace patterns, and import graphs. |
| 4-4 | Scan Codebase — Dependency Analysis | Parse manifest files and import statements to map internal and third-party dependencies. |
| 4-5 | Scan Codebase — Pattern Recognition | Analyze the codebase for architecture patterns (layered, hexagonal, microservices, monolith, MVC, etc.) and collect evidence. |
| 4-6 | Produce OUT-01 | Generate the Project Structure Tree using `templates/structure-tree-template.md`. Populate all placeholders. |
| 4-7 | Produce OUT-02 | Generate the Module Relationship Diagram using `templates/module-relationship-template.md`. Generate draw.io XML and save as `diagrams/module-relationship.drawio`. Verify the file opens as valid XML. |
| 4-8 | Produce OUT-03 | Generate the Layering Pattern Analysis using `templates/layering-analysis-template.md`. Include evidence for each identified pattern. |
| 4-9 | Produce OUT-04 | Generate the Package Dependency Map using `templates/dependency-map-template.md`. Cover both internal and third-party. Generate draw.io XML and save as `diagrams/dependency-map.drawio`. |
| 4-10 | Produce OUT-05 | Generate the Module Responsibility Summary using `templates/module-summary-template.md`. Every identified module must have a description. |
| 4-11 | Produce OUT-06 | Generate the Final Scan Report using `templates/scan-report-template.md`. Must exceed 500 bytes. |
| 4-12 | Record Findings | Execute `record_finding()` for each significant finding. Execute `record_knowledge()` for architectural insights. |
| 4-13 | DoD Self-Verify | Run all DoD checks (see `references/dod.md`) against the produced deliverables. Log results via `record_dod_check()`. If any check fails, loop back to the relevant production step. |

- **Inputs:** Validated scan requirements, project codebase access, templates.
- **Outputs:** OUT-01 through OUT-06, draw.io diagrams in `diagrams/`, all placed in the output directory.
- **Memory Operations:** `record_finding()`, `record_knowledge()`, `record_dod_check()`.
- **Success Criteria:** All 6 deliverables produced, draw.io diagrams valid, DoD self-check passes.

---

## Phase 5: Transformation Target Deep-Dive Investigation (Conditional)

> This phase is executed **only** when the scan purpose involves transformation, refactoring, feature addition, or system evolution.

| Step | Sub-Step | Description |
|------|----------|-------------|
| 5-1 | Check Trigger Condition | Verify whether the scan purpose (from Phase 0/1) involves transformation. If not, skip Phase 5 and proceed to Phase 6. |
| 5-2 | Confirm Target Scope | Present the transformation target identified in the scan purpose. Ask user to confirm the exact module(s), component(s), or file(s) to investigate. Iterate until confirmed. |
| 5-3 | Investigate Code Structure | Use Glob and Bash to map the directory layout and key files within the target scope. |
| 5-4 | Document Core Logic | Read key implementation files. Describe the main processing flow, critical decision branches, and error handling strategies. |
| 5-5 | Map Key Data Structures | Identify domain models, DTOs, enumerations, and persistence schemas owned or used by the target. |
| 5-6 | Analyze Inbound Dependencies | Grep for all usages of the target's public classes/functions/APIs across the codebase. List who depends on the target. |
| 5-7 | Analyze Outbound Dependencies | Read imports within the target scope. List all internal modules and third-party libraries the target depends on. |
| 5-8 | Document Data Flows & Interfaces | Identify all public APIs, event contracts, and shared data stores the target participates in. |
| 5-9 | Assess Test Coverage | Locate test files for the target. Classify coverage level: high / medium / low / none per test type. |
| 5-10 | Identify Technical Debt | Grep for TODO/FIXME/HACK markers and inspect for code smells, anti-patterns, and hardcoded values. |
| 5-11 | Identify Configuration Dependencies | Grep for environment variables and config keys consumed within the target. |
| 5-12 | Produce draw.io Sequence Diagrams | For the main success flow and at least one error/alternative flow, generate draw.io XML files saved as `diagrams/seq-{use-case-name}-main.drawio` and `diagrams/seq-{use-case-name}-error.drawio`. Use Section 5 of `templates/transformation-target-template.md`. |
| 5-13 | Identify Transformation Constraints | Based on the investigation, classify hard constraints (cannot change), soft constraints (should preserve), and risk areas (high-coupling, untested, shared state). |
| 5-14 | Produce OUT-07 | Compile all Phase 5 findings into the Transformation Target Current State Report using `templates/transformation-target-template.md`. Save as `OUT-07_transformation-target-current-state.md`. |
| 5-15 | Present and Confirm | Present the OUT-07 summary to the user. If confirmed → proceed to Phase 6. If deeper investigation needed → loop back to relevant steps. |
| 5-16 | Record in Memory | Execute `record_finding(phase='phase5')` for all findings. Execute `record_finding(phase='phase5', memory_type='risk')` for risks. Execute `record_decision(phase='phase5')` for confirmed scope and constraints. |

- **Inputs:** Validated scan requirements (from Phase 3), codebase access, OUT-01 through OUT-06.
- **Outputs:** `OUT-07_transformation-target-current-state.md`, `diagrams/seq-*.drawio` files.
- **Memory Operations:** `record_finding(phase='phase5')`, `record_decision()`.
- **Success Criteria:** User confirms OUT-07 Transformation Target Current State Report.

---

## Phase 6: Completion & Handoff

| Step | Sub-Step | Description |
|------|----------|-------------|
| 5-1 | Record Lessons Learned | Reflect on the scan process. Execute `record_lesson()` for each insight about what worked well, what was difficult, and what could be improved. |
| 5-2 | Complete Scan Record | Update the `scan_history` record in SQLite: set status to `completed`, record end timestamp, store summary statistics (modules found, dependencies mapped, patterns identified). |
| 5-3 | Trigger Supervisor | Invoke the supervisor validation process (`project-structure-scan-supervisor` skill). Pass all deliverables (OUT-01 through OUT-06, and OUT-07 + draw.io sequence diagrams if produced) and DoD results for independent verification. |
| 5-4 | Remediate if Needed | If the supervisor identifies issues, loop back to the relevant phase or step to correct. Re-run supervisor after remediation. |
| 5-5 | Prepare RACI Handoff | Compile the RACI matrix for PM Agent handoff, indicating responsibilities for follow-up actions on findings. |
| 5-6 | Notify PM Agent | Send completion notification to the PM Agent with: scan summary, deliverable locations (including OUT-07 if produced), RACI matrix, and any flagged items requiring human attention. |
| 5-7 | Archive Logs | Finalize and close the conversation log and work log. Ensure all entries are timestamped. |

- **Inputs:** Completed deliverables (OUT-01 through OUT-07 as applicable), all draw.io diagram files, DoD results, supervisor feedback.
- **Outputs:** Lessons learned records, completed scan history, RACI matrix, PM notification.
- **Memory Operations:** `record_lesson()`, `complete_scan()`.
- **Success Criteria:** Supervisor passes 100%, PM notified.

---

## Cross-Phase Rules

1. **Every phase must log its start and end time** in the work log (`logs/work-log.md`).
2. **Interactive phases (1-3 and 5) must record dialogue** in the conversation log.
3. **All memory operations must succeed** before proceeding to the next step. On failure, retry once, then halt with error.
4. **Template placeholders** (`{placeholder}`) must never remain in final outputs.
5. **The agent must not proceed past Phase 0** if any DoR check fails.
6. **All diagrams must be draw.io format** (`.drawio` files). No Mermaid diagrams in final deliverables. Each `.drawio` file must be valid XML with `<mxfile>` as the root element.
