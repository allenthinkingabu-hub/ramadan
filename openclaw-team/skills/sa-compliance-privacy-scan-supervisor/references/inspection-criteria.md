# Inspection Criteria — IA-INC-007 Compliance & Privacy Scan Supervisor

Detailed verification rules for each inspection item. The supervisor must check every item below.

---

## Infrastructure Checks

### INS-01: Triggers Configuration
- **Verify**: `references/triggers.md` exists in the skill directory
- **Content**: Contains primary triggers, context conditions, and output signals
- **Severity**: Critical

### INS-02: RACI Matrix Configuration
- **Verify**: `references/raci.md` exists with role definitions AND task-level RACI assignments
- **Content**: At least 7 roles defined, at least 10 task assignments with R/A/C/I values
- **Severity**: Critical

### INS-03: Output Template
- **Verify**: `references/output-templates.md` exists with deliverable template
- **Content**: Document Control, Executive Summary, Objectives, Stakeholders, and core sections present
- **Severity**: Critical

### INS-04: SOP Process
- **Verify**: `references/sop.md` exists with Phase 0 through Phase 5 defined
- **Content**: Each phase has step-by-step actions with expected outputs
- **Severity**: Critical

### INS-05: DoD Checklist
- **Verify**: `references/dod.md` exists with completeness, deliverable quality, process quality categories
- **Content**: At least 20 check items with severity levels
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
- **Content**: Phase-labeled sections, numbered question entries, answered summaries
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
  3. Requirements/deliverable validation (Phase 3)
- **Severity**: Critical

---

## Deliverable Quality Checks

### INS-DQ-01: Deliverable Complete
- **Verify**: All required sections from output template are present and populated
- **Content**: No empty sections or placeholder-only content
- **Severity**: Critical

### INS-DQ-02: No Unresolved TBDs
- **Verify**: Search entire deliverable for TBD, TODO, FIXME, XXX markers
- **Content**: Zero matches found
- **Severity**: Critical

### INS-DQ-03: Template Followed
- **Verify**: Deliverable structure matches output-templates.md format
- **Content**: All required sections in correct order
- **Severity**: High

### INS-DQ-04: Acceptance Criteria
- **Verify**: All requirements/deliverables have testable acceptance criteria
- **Content**: Criteria are measurable and specific
- **Severity**: High

### INS-DQ-05: Upstream Traceability
- **Verify**: Upstream inputs are referenced and decisions traceable to requirements
- **Content**: Clear linkage between inputs and outputs
- **Severity**: High
