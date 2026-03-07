# Inspection Criteria — IPM-INC-003 BRD Writing Supervisor

Detailed verification rules for each inspection item. The supervisor must check every item below.

---

## Infrastructure Checks

### INS-01: Triggers Configuration
- **Verify**: `references/triggers.md` exists in the skill directory
- **Content**: Contains primary triggers, context conditions, and output signals
- **Severity**: Critical

### INS-02: RACI Matrix Configuration
- **Verify**: `references/raci.md` exists with role definitions AND task-level RACI assignments
- **Content**: At least 8 roles defined, at least 15 task assignments with R/A/C/I values
- **Severity**: Critical

### INS-03: Output Template
- **Verify**: `references/output-templates.md` exists and contains all 19 standard BRD sections
- **Required sections**: Document Control, Executive Summary, Business Objectives, Project Background, Project Scope, Stakeholders, Business Requirements, Functional Requirements, Non-Functional Requirements, Data Requirements, Assumptions, Constraints, Dependencies, Risks & Mitigation, Success Metrics, Cost-Benefit Analysis, Implementation Timeline, Glossary, Appendices
- **Severity**: Critical

### INS-04: SOP Process
- **Verify**: `references/sop.md` exists with Phase 0 through Phase 5 defined
- **Content**: Each phase has step-by-step actions with expected outputs
- **Severity**: Critical

### INS-05: DoD Checklist
- **Verify**: `references/dod.md` exists with four categories: completeness, requirement quality, document quality, process quality
- **Content**: At least 25 check items with severity levels
- **Severity**: Critical

### INS-06: DoR Checklist
- **Verify**: `references/dor.md` exists with prerequisite entries
- **Content**: Each entry has required/optional flag and fallback strategy
- **Severity**: Critical

---

## Process Checks

### INS-07: Conversation Log
- **Verify**: `conversation-log.md` exists in output directory
- **Content**: Entries are numbered, each has timestamp and agent/user labels
- **Format**: `### Question #N — {timestamp}` followed by `**Agent**:` and `**User**:` lines
- **Severity**: Critical

### INS-08: Work Log
- **Verify**: `work-log.md` exists in output directory
- **Content**: Entries have timestamps and status indicators (completed/in-progress/failed)
- **Format**: `- [{timestamp}] {action} — Status: {status}`
- **Severity**: Critical

### INS-09: DoD Verification Passed
- **Verify**: Evidence that DoD self-check was performed
- **Content**: All critical severity items show as passed; high severity items show as passed
- **Severity**: Critical

### INS-10: Question Lists Log
- **Verify**: `question-lists.md` exists in output directory
- **Content**: Phase-labeled sections, numbered question entries, answered summaries for each Q&A round
- **Format**: `## Phase {N}: {name} — {timestamp}` + `### Question List #{seq}` + `### Answered Summary`
- **Severity**: Critical

### INS-11: Research Log
- **Verify**: `research-log.md` exists in output directory
- **Content**: Sequentially numbered entries, each with Tool, Query/URL, Purpose, Key Findings, Source
- **Format**: `## Research #{seq} — {timestamp}` with structured fields
- **Severity**: Critical

### INS-12: User Confirmation
- **Verify**: Conversation log shows explicit user confirmation for:
  1. Task purpose understanding (Phase 1)
  2. Topic understanding (Phase 2)
  3. Requirements list validation (Phase 3)
- **Severity**: Critical

---

## BRD Content Quality Checks

### INS-BRD-01: Executive Summary
- **Verify**: Section exists and provides meaningful overview (not placeholder text)
- **Content**: Covers project purpose, key objectives, expected outcomes
- **Severity**: Critical

### INS-BRD-02: SMART Objectives
- **Verify**: All business objectives follow SMART criteria
- **Content**: Each objective is Specific, Measurable, Achievable, Relevant, Time-bound
- **Severity**: High

### INS-BRD-03: Scope Defined
- **Verify**: Both "In Scope" and "Out of Scope" subsections exist with explicit items
- **Severity**: Critical

### INS-BRD-04: Acceptance Criteria
- **Verify**: Every BR, FR, and NFR has a non-empty "Acceptance Criteria" column
- **Content**: Criteria are testable/measurable, not vague
- **Severity**: Critical

### INS-BRD-05: Requirements Prioritized
- **Verify**: All requirements have MoSCoW priority (Must/Should/Could/Won't)
- **Severity**: High

### INS-BRD-06: No Unresolved TBDs
- **Verify**: Search entire BRD for TBD, TODO, FIXME, XXX, placeholder markers
- **Content**: Zero matches found
- **Severity**: Critical

### INS-BRD-07: Risks Documented
- **Verify**: Risk table exists with Probability, Impact, and Mitigation Strategy columns
- **Content**: At least 3 risks identified with all fields populated
- **Severity**: High

### INS-BRD-08: Traceability
- **Verify**: Requirements Traceability Matrix exists in appendices
- **Content**: Each requirement linked to source and related requirements
- **Severity**: High
