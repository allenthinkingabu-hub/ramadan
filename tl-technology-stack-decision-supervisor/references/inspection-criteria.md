# Inspection Criteria — tl-technology-stack-decision-supervisor

## Detailed Verification Criteria

### Item 1: Trigger Mechanism Config
- **File**: `technology-stack-decision/config/triggers.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least one trigger event definition
  - Each trigger has: id, event, source, condition fields
  - Metadata section includes task_id "TL-INC-002"

### Item 2: RACI Matrix Config
- **File**: `technology-stack-decision/config/raci.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains role names (at minimum: TL, PM)
  - Contains task names mapped to each role
  - Each entry has one of: R, A, C, I assignment
  - Downstream notification section is present

### Item 3: Skills List Config
- **File**: `technology-stack-decision/config/skills.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 5 skill items
  - Each skill has: id, name, proficiency fields

### Item 4: Knowledge Base Checklist
- **File**: `technology-stack-decision/config/knowledge-domains.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 5 knowledge domain items
  - Each domain has: id, domain, scope fields

### Item 5: Tools List
- **File**: `technology-stack-decision/config/tools.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 3 tool items
  - Each tool has: id, tool, purpose fields

### Item 6: MCP Tools List
- **File**: `technology-stack-decision/config/mcp-tools.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 1 MCP tool item
  - Each MCP tool has: id, tool, purpose fields

### Item 7: Output Content List + Templates
- **Files**: `technology-stack-decision/config/outputs.yaml` + `technology-stack-decision/templates/`
- **Checks**:
  - outputs.yaml exists, is valid YAML, lists all deliverables
  - templates/ directory exists and contains template files
  - Each output item has: id, deliverable, file_path, format fields

### Item 8: SOP Process Checklist
- **File**: `technology-stack-decision/config/sop.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains sequential phases (Phase 0 through Phase 5)
  - Each phase has numbered steps

### Item 9: DoD Checklist
- **File**: `technology-stack-decision/config/dod.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 13 DoD items
  - Each item has: id, check_item, verification_criteria fields

### Item 10: DoR Checklist
- **File**: `technology-stack-decision/config/dor.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 4 DoR items
  - Each item has: id, prerequisite, verification fields

### Item 11: Conversation Log
- **File**: `technology-stack-decision/conversation-log.md`
- **Checks**:
  - File exists and is non-empty
  - Contains session info header (Topic, Started timestamp)
  - Contains at least one logged entry with: Phase, Timestamp, Agent Question, User Response

### Item 12: Work Log
- **File**: `technology-stack-decision/work-log.md`
- **Checks**:
  - File exists and is non-empty
  - Contains session info header
  - Contains timestamped entries with: Phase, Action, Result

### Item 13: DoD Verification
- **Checks**:
  - Evidence that self-verification was performed (logged in work-log.md)
  - All DoD-01 through DoD-12 items have been addressed
  - Any remediation actions are logged in work-log.md

### Item 14: Technology Decision Matrix
- **File**: `technology-stack-decision/technology-decision-matrix.md`
- **Checks**:
  - File exists and is non-empty
  - Contains evaluation criteria with weights
  - Contains candidate technologies scored against criteria
  - Includes final recommendation with justification
  - Covers all required technology categories (languages, frameworks, infrastructure)

### Item 15: Stack Specification
- **File**: `technology-stack-decision/stack-specification.md`
- **Checks**:
  - File exists and is non-empty
  - Specifies concrete versions for all selected technologies
  - Covers languages, frameworks, libraries, infrastructure, DevOps tooling
  - Includes license information for each component

### Item 16: Compatibility Analysis
- **File**: `technology-stack-decision/compatibility-analysis.md`
- **Checks**:
  - File exists and is non-empty
  - Contains inter-component compatibility verification
  - Documents version compatibility matrix
  - Lists known issues and workarounds

### Item 17: Upstream Traceability
- **Checks**:
  - References to IA-INC-001..008 (Wave 10 inputs) appear in conversation log or work log
  - Technology decisions are traceable to upstream architect inputs and NFRs
  - Architect's technology recommendations are acknowledged and addressed
