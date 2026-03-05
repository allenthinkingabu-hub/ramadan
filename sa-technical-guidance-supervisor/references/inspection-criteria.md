# Inspection Criteria — sa-technical-guidance-supervisor

## Detailed Verification Criteria

### Item 1: Trigger Mechanism Config
- **File**: `technical-guidance/config/triggers.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least one trigger event definition
  - Each trigger has: id, event, source, condition fields
  - Metadata section includes task_id "IA-DEV-001"

### Item 2: RACI Matrix Config
- **File**: `technical-guidance/config/raci.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains role names (at minimum: SA, PM)
  - Contains task names mapped to each role
  - Each entry has one of: R, A, C, I assignment
  - Downstream notification section is present

### Item 3: Skills List Config
- **File**: `technical-guidance/config/skills.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 5 skill items
  - Each skill has: id, name, proficiency fields

### Item 4: Knowledge Base Checklist
- **File**: `technical-guidance/config/knowledge-domains.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 5 knowledge domain items
  - Each domain has: id, domain, scope fields

### Item 5: Tools List
- **File**: `technical-guidance/config/tools.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 3 tool items
  - Each tool has: id, tool, purpose fields

### Item 6: MCP Tools List
- **File**: `technical-guidance/config/mcp-tools.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 1 MCP tool item
  - Each MCP tool has: id, tool, purpose fields

### Item 7: Output Content List + Templates
- **Files**: `technical-guidance/config/outputs.yaml` + `technical-guidance/templates/`
- **Checks**:
  - outputs.yaml exists, is valid YAML, lists all deliverables
  - templates/ directory exists and contains template files
  - Each output item has: id, deliverable, file_path, format fields

### Item 8: SOP Process Checklist
- **File**: `technical-guidance/config/sop.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains sequential phases (Phase 0 through Phase 5)
  - Each phase has numbered steps

### Item 9: DoD Checklist
- **File**: `technical-guidance/config/dod.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 13 DoD items
  - Each item has: id, check_item, verification_criteria fields

### Item 10: DoR Checklist
- **File**: `technical-guidance/config/dor.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 4 DoR items
  - Each item has: id, prerequisite, verification fields

### Item 11: Conversation Log
- **File**: `technical-guidance/conversation-log.md`
- **Checks**:
  - File exists and is non-empty
  - Contains session info header (Topic, Started timestamp)
  - Contains at least one logged entry with: Phase, Timestamp, Agent Question, User Response

### Item 12: Work Log
- **File**: `technical-guidance/work-log.md`
- **Checks**:
  - File exists and is non-empty
  - Contains session info header
  - Contains timestamped entries with: Phase, Action, Result

### Item 13: DoD Verification
- **Checks**:
  - Evidence that self-verification was performed (logged in work-log.md)
  - All DoD-01 through DoD-12 items have been addressed
  - Any remediation actions are logged in work-log.md

### Item 14: Pattern Catalog
- **File**: `technical-guidance/patterns/pattern-catalog.md`
- **Checks**:
  - File exists and is non-empty
  - Contains at least one design pattern entry
  - Each pattern has: category, problem, solution, applicability, trade-offs
  - Patterns are relevant to the project architecture and technology stack

### Item 15: Architecture-to-Code Mapping
- **File**: `technical-guidance/architecture-code-mapping.md`
- **Checks**:
  - File exists and is non-empty
  - Contains component-to-module mapping table
  - Contains dependency rules (allowed and prohibited)
  - Mappings are consistent with upstream architecture design (IA-REQ-001)

### Item 16: Guidance Decision Log
- **File**: `technical-guidance/guidance-decision-log.md`
- **Checks**:
  - File exists and is non-empty
  - Contains at least one decision entry
  - Each decision has: ID, topic, decision, rationale, alternatives considered, status
  - Decisions are traceable to architecture requirements

### Item 17: Upstream Traceability
- **Checks**:
  - References to IA-REQ-001 (Architecture Design) appear in guidance report or work log
  - References to SA-REQ-001, SA-REQ-004, SA-REQ-005 where applicable
  - Guidance decisions are traceable to upstream architecture decisions
  - Pattern recommendations are consistent with Technology Blueprint
