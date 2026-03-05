# Inspection Criteria -- tl-code-review-quality-gatekeeping-supervisor

## Detailed Verification Criteria

### Item 1: Trigger Mechanism Config
- **File**: `code-review-quality-gatekeeping/config/triggers.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least one trigger event definition
  - Each trigger has: id, event, source, condition fields
  - Metadata section includes task_id "TL-DEV-001"

### Item 2: RACI Matrix Config
- **File**: `code-review-quality-gatekeeping/config/raci.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains role names (at minimum: TL, PM)
  - Contains task names mapped to each role
  - Each entry has one of: R, A, C, I assignment
  - Downstream notification section is present

### Item 3: Skills List Config
- **File**: `code-review-quality-gatekeeping/config/skills.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 5 skill items
  - Each skill has: id, name, proficiency fields

### Item 4: Knowledge Base Checklist
- **File**: `code-review-quality-gatekeeping/config/knowledge-domains.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 5 knowledge domain items
  - Each domain has: id, domain, scope fields

### Item 5: Tools List
- **File**: `code-review-quality-gatekeeping/config/tools.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 3 tool items
  - Each tool has: id, tool, purpose fields

### Item 6: MCP Tools List
- **File**: `code-review-quality-gatekeeping/config/mcp-tools.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 1 MCP tool item
  - Each MCP tool has: id, tool, purpose fields

### Item 7: Output Content List + Templates
- **Files**: `code-review-quality-gatekeeping/config/outputs.yaml` + `code-review-quality-gatekeeping/templates/`
- **Checks**:
  - outputs.yaml exists, is valid YAML, lists all deliverables
  - templates/ directory exists and contains template files
  - Each output item has: id, deliverable, file_path, format fields

### Item 8: SOP Process Checklist
- **File**: `code-review-quality-gatekeeping/config/sop.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains sequential phases (Phase 0 through Phase 5)
  - Each phase has numbered steps

### Item 9: DoD Checklist
- **File**: `code-review-quality-gatekeeping/config/dod.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 13 DoD items
  - Each item has: id, check_item, verification_criteria fields

### Item 10: DoR Checklist
- **File**: `code-review-quality-gatekeeping/config/dor.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 4 DoR items
  - Each item has: id, prerequisite, verification fields

### Item 11: Conversation Log
- **File**: `code-review-quality-gatekeeping/conversation-log.md`
- **Checks**:
  - File exists and is non-empty
  - Contains session info header (Topic, Started timestamp)
  - Contains at least one logged entry with: Phase, Timestamp, Agent Question, User Response

### Item 12: Work Log
- **File**: `code-review-quality-gatekeeping/work-log.md`
- **Checks**:
  - File exists and is non-empty
  - Contains session info header
  - Contains timestamped entries with: Phase, Action, Result

### Item 13: DoD Verification
- **Checks**:
  - Evidence that self-verification was performed (logged in work-log.md)
  - All DoD-01 through DoD-12 items have been addressed
  - Any remediation actions are logged in work-log.md

### Item 14: Review Standards Document
- **File**: `code-review-quality-gatekeeping/review-standards.md`
- **Checks**:
  - File exists and is non-empty
  - Contains review types section (quick, standard, deep review)
  - Contains severity classification (critical, major, minor, suggestion)
  - Contains escalation procedures

### Item 15: Quality Gate Report
- **File**: `code-review-quality-gatekeeping/quality-gate-report.md`
- **Checks**:
  - File exists and is non-empty
  - Contains quality gate definitions with entry/exit criteria
  - Contains compliance tracking metrics
  - Contains threshold definitions

### Item 16: Architectural Compliance
- **Checks**:
  - Review checklist includes architecture pattern verification
  - References to IA-REQ-001 architecture design outputs
  - Compliance checks mapped to specific architectural decisions

### Item 17: Upstream Traceability
- **Checks**:
  - References to upstream architecture design documents appear in conversation log or work log
  - Review standards are traceable to upstream requirements
  - Quality gates aligned with project quality objectives
