# Inspection Criteria — sa-code-design-reviews-supervisor

## Detailed Verification Criteria

### Item 1: Trigger Mechanism Config
- **File**: `code-design-reviews/config/triggers.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least one trigger event definition
  - Each trigger has: id, event, source, condition fields
  - Metadata section includes task_id "IA-DEV-002"

### Item 2: RACI Matrix Config
- **File**: `code-design-reviews/config/raci.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains role names (at minimum: SA, PM)
  - Contains task names mapped to each role
  - Each entry has one of: R, A, C, I assignment
  - Downstream notification section is present

### Item 3: Skills List Config
- **File**: `code-design-reviews/config/skills.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 5 skill items
  - Each skill has: id, name, proficiency fields

### Item 4: Knowledge Base Checklist
- **File**: `code-design-reviews/config/knowledge-domains.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 5 knowledge domain items
  - Each domain has: id, domain, scope fields

### Item 5: Tools List
- **File**: `code-design-reviews/config/tools.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 3 tool items
  - Each tool has: id, tool, purpose fields

### Item 6: MCP Tools List
- **File**: `code-design-reviews/config/mcp-tools.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 1 MCP tool item
  - Each MCP tool has: id, tool, purpose fields

### Item 7: Output Content List + Templates
- **Files**: `code-design-reviews/config/outputs.yaml` + `code-design-reviews/templates/`
- **Checks**:
  - outputs.yaml exists, is valid YAML, lists all deliverables
  - templates/ directory exists and contains template files
  - Each output item has: id, deliverable, file_path, format fields

### Item 8: SOP Process Checklist
- **File**: `code-design-reviews/config/sop.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains sequential phases (Phase 0 through Phase 5)
  - Each phase has numbered steps

### Item 9: DoD Checklist
- **File**: `code-design-reviews/config/dod.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 13 DoD items
  - Each item has: id, check_item, verification_criteria fields

### Item 10: DoR Checklist
- **File**: `code-design-reviews/config/dor.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 4 DoR items
  - Each item has: id, prerequisite, verification fields

### Item 11: Conversation Log
- **File**: `code-design-reviews/conversation-log.md`
- **Checks**:
  - File exists and is non-empty
  - Contains session info header (Topic, Started timestamp)
  - Contains at least one logged entry with: Phase, Timestamp, Agent Question, User Response

### Item 12: Work Log
- **File**: `code-design-reviews/work-log.md`
- **Checks**:
  - File exists and is non-empty
  - Contains session info header
  - Contains timestamped entries with: Phase, Action, Result

### Item 13: DoD Verification
- **Checks**:
  - Evidence that self-verification was performed (logged in work-log.md)
  - All DoD-01 through DoD-12 items have been addressed
  - Any remediation actions are logged in work-log.md

### Item 14: Compliance Matrix
- **File**: `code-design-reviews/compliance-matrix.md`
- **Checks**:
  - File exists and is non-empty
  - Contains architecture compliance mapping table
  - Contains NFR compliance assessment
  - Each requirement has status (Compliant/Non-Compliant/Partial) and evidence
  - Coverage includes all key architecture components

### Item 15: Remediation Plan
- **File**: `code-design-reviews/remediation-plan.md`
- **Checks**:
  - File exists and is non-empty
  - Contains prioritized list of issues (P1/P2/P3)
  - Each issue has: finding ID, component, issue description, suggested fix, effort estimate
  - Issues are linked to findings in the review report

### Item 16: Review Decision Log
- **File**: `code-design-reviews/review-decision-log.md`
- **Checks**:
  - File exists and is non-empty
  - Contains at least one decision entry
  - Each decision has: ID, review subject, decision, conditions, rationale
  - Decision is one of: Approve, Request Changes, Reject

### Item 17: Upstream Traceability
- **Checks**:
  - References to IA-REQ-001 (Architecture Design) appear in review report
  - References to IA-DEV-001 (Technical Guidance) where applicable
  - Findings are traceable to specific architecture requirements or design patterns
  - Compliance assessment references upstream architecture decisions
