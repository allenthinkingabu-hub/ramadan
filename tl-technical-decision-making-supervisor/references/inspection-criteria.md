# Inspection Criteria -- tl-technical-decision-making-supervisor

## Detailed Verification Criteria

### Item 1: Trigger Mechanism Config
- **File**: `technical-decision-making/config/triggers.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least one trigger event definition
  - Each trigger has: id, event, source, condition fields
  - Metadata section includes task_id "TL-DEV-003"

### Item 2: RACI Matrix Config
- **File**: `technical-decision-making/config/raci.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains role names (at minimum: TL, PM)
  - Contains task names mapped to each role
  - Each entry has one of: R, A, C, I assignment

### Item 3: Skills List Config
- **File**: `technical-decision-making/config/skills.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 5 skill items
  - Each skill has: id, name, proficiency fields

### Item 4: Knowledge Base Checklist
- **File**: `technical-decision-making/config/knowledge-domains.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 5 knowledge domain items
  - Each domain has: id, domain, scope fields

### Item 5: Tools List
- **File**: `technical-decision-making/config/tools.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 3 tool items
  - Each tool has: id, tool, purpose fields

### Item 6: MCP Tools List
- **File**: `technical-decision-making/config/mcp-tools.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 1 MCP tool item
  - Each MCP tool has: id, tool, purpose fields

### Item 7: Output Content List + Templates
- **Files**: `technical-decision-making/config/outputs.yaml` + `technical-decision-making/templates/`
- **Checks**:
  - outputs.yaml exists, is valid YAML, lists all deliverables
  - templates/ directory exists and contains template files
  - Each output item has: id, deliverable, file_path, format fields

### Item 8: SOP Process Checklist
- **File**: `technical-decision-making/config/sop.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains sequential phases (Phase 0 through Phase 5)
  - Each phase has numbered steps

### Item 9: DoD Checklist
- **File**: `technical-decision-making/config/dod.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 13 DoD items
  - Each item has: id, check_item, verification_criteria fields

### Item 10: DoR Checklist
- **File**: `technical-decision-making/config/dor.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 4 DoR items
  - Each item has: id, prerequisite, verification fields

### Item 11: Conversation Log
- **File**: `technical-decision-making/conversation-log.md`
- **Checks**:
  - File exists and is non-empty
  - Contains session info header (Topic, Started timestamp)
  - Contains at least one logged entry

### Item 12: Work Log
- **File**: `technical-decision-making/work-log.md`
- **Checks**:
  - File exists and is non-empty
  - Contains session info header
  - Contains timestamped entries with: Phase, Action, Result

### Item 13: DoD Verification
- **Checks**:
  - Evidence that self-verification was performed
  - All DoD items have been addressed
  - Any remediation actions are logged

### Item 14: Trade-off Analysis
- **File**: `technical-decision-making/trade-off-analysis.md`
- **Checks**:
  - File exists and is non-empty
  - Contains evaluation criteria with weights
  - Contains options comparison with scores
  - Contains recommendation with rationale

### Item 15: Decision Register
- **File**: `technical-decision-making/decision-register.md`
- **Checks**:
  - File exists and is non-empty
  - Contains all decisions with ID, date, status
  - Each decision has rationale and impact documented

### Item 16: ADR Quality
- **Checks**:
  - ADRs follow standard format (context, decision, alternatives, consequences)
  - Each ADR has clear rationale
  - Alternatives considered are documented
  - Consequences (positive and negative) are identified

### Item 17: Upstream Traceability
- **Checks**:
  - References to upstream architecture design documents present
  - Decisions aligned with IA-REQ-001 architecture
  - Decision rationale traceable to requirements and constraints
