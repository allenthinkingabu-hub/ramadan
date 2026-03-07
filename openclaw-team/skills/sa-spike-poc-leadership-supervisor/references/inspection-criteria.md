# Inspection Criteria — sa-spike-poc-leadership-supervisor

## Detailed Verification Criteria

### Item 1: Trigger Mechanism Config
- **File**: `spike-poc/config/triggers.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least one trigger event definition
  - Each trigger has: id, event, source, condition fields
  - Metadata section includes task_id "IA-DEV-003"

### Item 2: RACI Matrix Config
- **File**: `spike-poc/config/raci.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains role names (at minimum: SA, PM)
  - Contains task names mapped to each role
  - Each entry has one of: R, A, C, I assignment
  - Downstream notification section is present

### Item 3: Skills List Config
- **File**: `spike-poc/config/skills.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 5 skill items
  - Each skill has: id, name, proficiency fields

### Item 4: Knowledge Base Checklist
- **File**: `spike-poc/config/knowledge-domains.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 5 knowledge domain items
  - Each domain has: id, domain, scope fields

### Item 5: Tools List
- **File**: `spike-poc/config/tools.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 3 tool items
  - Each tool has: id, tool, purpose fields

### Item 6: MCP Tools List
- **File**: `spike-poc/config/mcp-tools.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 1 MCP tool item
  - Each MCP tool has: id, tool, purpose fields

### Item 7: Output Content List + Templates
- **Files**: `spike-poc/config/outputs.yaml` + `spike-poc/templates/`
- **Checks**:
  - outputs.yaml exists, is valid YAML, lists all deliverables
  - templates/ directory exists and contains template files
  - Each output item has: id, deliverable, file_path, format fields

### Item 8: SOP Process Checklist
- **File**: `spike-poc/config/sop.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains sequential phases (Phase 0 through Phase 5)
  - Each phase has numbered steps

### Item 9: DoD Checklist
- **File**: `spike-poc/config/dod.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 13 DoD items
  - Each item has: id, check_item, verification_criteria fields

### Item 10: DoR Checklist
- **File**: `spike-poc/config/dor.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 4 DoR items
  - Each item has: id, prerequisite, verification fields

### Item 11: Conversation Log
- **File**: `spike-poc/conversation-log.md`
- **Checks**:
  - File exists and is non-empty
  - Contains session info header (Topic, Started timestamp)
  - Contains at least one logged entry with: Phase, Timestamp, Agent Question, User Response

### Item 12: Work Log
- **File**: `spike-poc/work-log.md`
- **Checks**:
  - File exists and is non-empty
  - Contains session info header
  - Contains timestamped entries with: Phase, Action, Result

### Item 13: DoD Verification
- **Checks**:
  - Evidence that self-verification was performed (logged in work-log.md)
  - All DoD-01 through DoD-12 items have been addressed
  - Any remediation actions are logged in work-log.md

### Item 14: Technology Comparison
- **File**: `spike-poc/findings/technology-comparison.md`
- **Checks**:
  - File exists and is non-empty (may be marked N/A if single-option spike)
  - Contains evaluation criteria with weights
  - Contains comparison table with scores per option
  - Contains recommendation with rationale

### Item 15: Recommendation & Decision Record
- **File**: `spike-poc/findings/recommendation-decision.md`
- **Checks**:
  - File exists and is non-empty
  - Contains decision ID, topic, decision, rationale
  - Contains alternatives considered
  - Documents impact on architecture design
  - Status is one of: Proposed, Accepted, Rejected

### Item 16: Risk Assessment Update
- **File**: `spike-poc/findings/risk-assessment.md`
- **Checks**:
  - File exists and is non-empty
  - Contains pre-spike and post-spike risk levels
  - Documents residual risks
  - Documents new risks identified during spike
  - Risk mitigations are actionable

### Item 17: Upstream Traceability
- **Checks**:
  - References to IA-REQ-001 (Architecture Design) appear in spike report
  - References to SA-REQ-001, SA-REQ-004 where applicable
  - Spike hypothesis is traceable to an architecture uncertainty
  - Findings document impact on upstream architecture decisions
