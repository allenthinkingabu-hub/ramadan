# Inspection Criteria -- sa-risk-identification-supervisor

## Detailed Verification Criteria

### Item 1: Trigger Mechanism Config
- **File**: `risk-identification/config/triggers.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least one trigger event definition
  - Each trigger has: id, event, source, condition fields
  - Metadata section includes task_id "IA-INC-004"

### Item 2: RACI Matrix Config
- **File**: `risk-identification/config/raci.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains role names (at minimum: SA, PM)
  - Contains task names mapped to each role
  - Each entry has one of: R, A, C, I assignment
  - Downstream notification section is present

### Item 3: Skills List Config
- **File**: `risk-identification/config/skills.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 5 skill items
  - Each skill has: id, name, proficiency fields

### Item 4: Knowledge Base Checklist
- **File**: `risk-identification/config/knowledge-domains.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 5 knowledge domain items
  - Each domain has: id, domain, scope fields

### Item 5: Tools List
- **File**: `risk-identification/config/tools.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 3 tool items
  - Each tool has: id, tool, purpose fields

### Item 6: MCP Tools List
- **File**: `risk-identification/config/mcp-tools.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 1 MCP tool item
  - Each MCP tool has: id, tool, purpose fields

### Item 7: Output Content List + Templates
- **Files**: `risk-identification/config/outputs.yaml` + `risk-identification/templates/`
- **Checks**:
  - outputs.yaml exists, is valid YAML, lists all deliverables
  - templates/ directory exists and contains template files
  - Each output item has: id, deliverable, file_path, format fields

### Item 8: SOP Process Checklist
- **File**: `risk-identification/config/sop.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains sequential phases (Phase 0 through Phase 5)
  - Each phase has numbered steps

### Item 9: DoD Checklist
- **File**: `risk-identification/config/dod.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 13 DoD items
  - Each item has: id, check_item, verification_criteria fields

### Item 10: DoR Checklist
- **File**: `risk-identification/config/dor.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 4 DoR items
  - Each item has: id, prerequisite, verification fields

### Item 11: Conversation Log
- **File**: `risk-identification/conversation-log.md`
- **Checks**:
  - File exists and is non-empty
  - Contains session info header (Topic, Started timestamp)
  - Contains at least one logged entry with: Phase, Timestamp, Agent Question, User Response

### Item 12: Work Log
- **File**: `risk-identification/work-log.md`
- **Checks**:
  - File exists and is non-empty
  - Contains session info header
  - Contains timestamped entries with: Phase, Action, Result

### Item 13: DoD Verification
- **Checks**:
  - Evidence that self-verification was performed (logged in work-log.md)
  - All DoD-01 through DoD-12 items have been addressed
  - Any remediation actions are logged in work-log.md
  - Risk register contains categorized and scored risks

### Item 14: Risk Register
- **File**: `risk-identification/risk-register.md`
- **Checks**:
  - File exists and is non-empty
  - Contains risk entries with Risk ID, Category, Description, Likelihood, Impact, Severity
  - Covers multiple risk categories (Technical, Integration, Dependency, NFR)
  - Each risk has an assigned owner and mitigation strategy
  - Severity is derived from likelihood x impact matrix

### Item 15: Dependency Map
- **File**: `risk-identification/diagrams/dependency-map.md`
- **Checks**:
  - File exists and is non-empty
  - Contains system dependency graph (Mermaid or PlantUML diagram)
  - Identifies critical path dependencies
  - Documents external/third-party dependencies
  - Notes circular dependencies if any exist

### Item 16: Mitigation Strategies
- **File**: `risk-identification/mitigation-strategies.md`
- **Checks**:
  - File exists and is non-empty
  - Contains risk-to-mitigation mapping table
  - Each high-severity risk has a contingency plan
  - Residual risk assessment is documented
  - Strategy types are classified (Avoid/Reduce/Transfer/Accept)

### Item 17: Upstream Traceability
- **Checks**:
  - References to SA-REQ-001..005 (Wave 9 inputs) appear in conversation log or work log
  - Risks are traceable to upstream architecture decisions and requirements
  - Integration risks reference SA-REQ-002 Integration Architecture
  - NFR risks reference SA-REQ-003 NFR Mapping
