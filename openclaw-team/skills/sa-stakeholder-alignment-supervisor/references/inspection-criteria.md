# Inspection Criteria -- sa-stakeholder-alignment-supervisor

## Detailed Verification Criteria

### Item 1: Trigger Mechanism Config
- **File**: `stakeholder-alignment/config/triggers.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least one trigger event definition
  - Each trigger has: id, event, source, condition fields
  - Metadata section includes task_id "IA-INC-006"

### Item 2: RACI Matrix Config
- **File**: `stakeholder-alignment/config/raci.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains role names (at minimum: SA, PM)
  - Contains task names mapped to each role
  - Each entry has one of: R, A, C, I assignment
  - Downstream notification section is present

### Item 3: Skills List Config
- **File**: `stakeholder-alignment/config/skills.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 5 skill items
  - Each skill has: id, name, proficiency fields

### Item 4: Knowledge Base Checklist
- **File**: `stakeholder-alignment/config/knowledge-domains.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 5 knowledge domain items
  - Each domain has: id, domain, scope fields

### Item 5: Tools List
- **File**: `stakeholder-alignment/config/tools.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 3 tool items
  - Each tool has: id, tool, purpose fields

### Item 6: MCP Tools List
- **File**: `stakeholder-alignment/config/mcp-tools.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 1 MCP tool item
  - Each MCP tool has: id, tool, purpose fields

### Item 7: Output Content List + Templates
- **Files**: `stakeholder-alignment/config/outputs.yaml` + `stakeholder-alignment/templates/`
- **Checks**:
  - outputs.yaml exists, is valid YAML, lists all deliverables
  - templates/ directory exists and contains template files
  - Each output item has: id, deliverable, file_path, format fields

### Item 8: SOP Process Checklist
- **File**: `stakeholder-alignment/config/sop.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains sequential phases (Phase 0 through Phase 5)
  - Each phase has numbered steps

### Item 9: DoD Checklist
- **File**: `stakeholder-alignment/config/dod.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 13 DoD items
  - Each item has: id, check_item, verification_criteria fields

### Item 10: DoR Checklist
- **File**: `stakeholder-alignment/config/dor.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 4 DoR items
  - Each item has: id, prerequisite, verification fields

### Item 11: Conversation Log
- **File**: `stakeholder-alignment/conversation-log.md`
- **Checks**:
  - File exists and is non-empty
  - Contains session info header (Topic, Started timestamp)
  - Contains at least one logged entry with: Phase, Timestamp, Agent Question, User Response

### Item 12: Work Log
- **File**: `stakeholder-alignment/work-log.md`
- **Checks**:
  - File exists and is non-empty
  - Contains session info header
  - Contains timestamped entries with: Phase, Action, Result

### Item 13: DoD Verification
- **Checks**:
  - Evidence that self-verification was performed (logged in work-log.md)
  - All DoD-01 through DoD-12 items have been addressed
  - Any remediation actions are logged in work-log.md
  - Alignment deliverables contain substantive stakeholder-specific content

### Item 14: Stakeholder Map
- **File**: `stakeholder-alignment/stakeholder-map.md`
- **Checks**:
  - File exists and is non-empty
  - Contains influence/interest matrix with stakeholder groups
  - Each stakeholder has engagement strategy defined
  - Communication plan is present with channels and frequency
  - Covers minimum stakeholder groups: business, product, security, operations

### Item 15: Decision Criteria Matrix
- **File**: `stakeholder-alignment/decision-criteria.md`
- **Checks**:
  - File exists and is non-empty
  - Contains weighted evaluation criteria with numeric weights
  - Contains priority rankings per stakeholder group
  - Contains trade-off analysis with resolution approaches
  - Criteria weights sum to 100%

### Item 16: Workshop Outcomes
- **File**: `stakeholder-alignment/workshop-outcomes.md`
- **Checks**:
  - File exists and is non-empty
  - Contains agreed scope boundaries (in-scope and out-of-scope)
  - Contains risk posture per stakeholder group
  - Contains action items with owners and due dates
  - Contains escalation paths for unresolved conflicts

### Item 17: Upstream Traceability
- **Checks**:
  - References to SA-REQ-001..005 (Wave 9 inputs) appear in conversation log or work log
  - Alignment decisions reference SAD (SA-REQ-001) and Technology Blueprint (SA-REQ-004)
  - Security alignment references NFR Mapping (SA-REQ-003)
  - ARB feedback (SA-REQ-005) is incorporated into decision criteria
