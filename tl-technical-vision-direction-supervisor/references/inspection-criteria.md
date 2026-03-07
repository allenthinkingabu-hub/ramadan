# Inspection Criteria — tl-technical-vision-direction-supervisor

## Detailed Verification Criteria

### Item 1: Trigger Mechanism Config
- **File**: `technical-vision-direction/config/triggers.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least one trigger event definition
  - Each trigger has: id, event, source, condition fields
  - Metadata section includes task_id "TL-INC-001"

### Item 2: RACI Matrix Config
- **File**: `technical-vision-direction/config/raci.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains role names (at minimum: TL, PM)
  - Contains task names mapped to each role
  - Each entry has one of: R, A, C, I assignment
  - Downstream notification section is present

### Item 3: Skills List Config
- **File**: `technical-vision-direction/config/skills.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 5 skill items
  - Each skill has: id, name, proficiency fields

### Item 4: Knowledge Base Checklist
- **File**: `technical-vision-direction/config/knowledge-domains.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 5 knowledge domain items
  - Each domain has: id, domain, scope fields

### Item 5: Tools List
- **File**: `technical-vision-direction/config/tools.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 3 tool items
  - Each tool has: id, tool, purpose fields

### Item 6: MCP Tools List
- **File**: `technical-vision-direction/config/mcp-tools.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 1 MCP tool item
  - Each MCP tool has: id, tool, purpose fields

### Item 7: Output Content List + Templates
- **Files**: `technical-vision-direction/config/outputs.yaml` + `technical-vision-direction/templates/`
- **Checks**:
  - outputs.yaml exists, is valid YAML, lists all deliverables
  - templates/ directory exists and contains template files
  - Each output item has: id, deliverable, file_path, format fields

### Item 8: SOP Process Checklist
- **File**: `technical-vision-direction/config/sop.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains sequential phases (Phase 0 through Phase 5)
  - Each phase has numbered steps

### Item 9: DoD Checklist
- **File**: `technical-vision-direction/config/dod.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 13 DoD items
  - Each item has: id, check_item, verification_criteria fields

### Item 10: DoR Checklist
- **File**: `technical-vision-direction/config/dor.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 4 DoR items
  - Each item has: id, prerequisite, verification fields

### Item 11: Conversation Log
- **File**: `technical-vision-direction/conversation-log.md`
- **Checks**:
  - File exists and is non-empty
  - Contains session info header (Topic, Started timestamp)
  - Contains at least one logged entry with: Phase, Timestamp, Agent Question, User Response

### Item 12: Work Log
- **File**: `technical-vision-direction/work-log.md`
- **Checks**:
  - File exists and is non-empty
  - Contains session info header
  - Contains timestamped entries with: Phase, Action, Result

### Item 13: DoD Verification
- **Checks**:
  - Evidence that self-verification was performed (logged in work-log.md)
  - All DoD-01 through DoD-12 items have been addressed
  - Any remediation actions are logged in work-log.md

### Item 14: Technical Vision Statement
- **File**: `technical-vision-direction/technical-vision-statement.md`
- **Checks**:
  - File exists and is non-empty
  - Contains clear vision articulation (not just placeholder text)
  - Includes time horizon (short-term, mid-term, long-term)
  - Documents alignment with business strategy

### Item 15: Guiding Principles
- **File**: `technical-vision-direction/guiding-principles.md`
- **Checks**:
  - File exists and is non-empty
  - Contains at least 3 guiding principles with descriptions and rationale
  - Includes trade-off decision framework

### Item 16: Business-Technology Alignment
- **File**: `technical-vision-direction/alignment-matrix.md`
- **Checks**:
  - File exists and is non-empty
  - Contains objective-to-capability mapping table
  - Identifies current state, target state, and gaps
  - Includes investment priority assessment

### Item 17: Upstream Traceability
- **Checks**:
  - References to IA-INC-001..008 (Wave 10 inputs) appear in conversation log or work log
  - Vision decisions are traceable to upstream architect inputs
  - Key architectural constraints from upstream are acknowledged
