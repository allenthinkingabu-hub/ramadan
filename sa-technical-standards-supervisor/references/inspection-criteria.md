# Inspection Criteria -- sa-technical-standards-supervisor

## Detailed Verification Criteria

### Item 1: Trigger Mechanism Config
- **File**: `technical-standards/config/triggers.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least one trigger event definition
  - Each trigger has: id, event, source, condition fields
  - Metadata section includes task_id "IA-REQ-005"

### Item 2: RACI Matrix Config
- **File**: `technical-standards/config/raci.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains role names (at minimum: SA, PM)
  - Contains task names mapped to each role
  - Each entry has one of: R, A, C, I assignment
  - Downstream notification section is present

### Item 3: Skills List Config
- **File**: `technical-standards/config/skills.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 5 skill items
  - Each skill has: id, name, proficiency fields

### Item 4: Knowledge Base Checklist
- **File**: `technical-standards/config/knowledge-domains.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 5 knowledge domain items
  - Each domain has: id, domain, scope fields

### Item 5: Tools List
- **File**: `technical-standards/config/tools.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 3 tool items
  - Each tool has: id, tool, purpose fields

### Item 6: MCP Tools List
- **File**: `technical-standards/config/mcp-tools.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 1 MCP tool item
  - Each MCP tool has: id, tool, purpose fields

### Item 7: Output Content List + Templates
- **Files**: `technical-standards/config/outputs.yaml` + `technical-standards/templates/`
- **Checks**:
  - outputs.yaml exists, is valid YAML, lists all deliverables
  - templates/ directory exists and contains template files
  - Each output item has: id, deliverable, file_path, format fields

### Item 8: SOP Process Checklist
- **File**: `technical-standards/config/sop.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains sequential phases (Phase 0 through Phase 5)
  - Each phase has numbered steps

### Item 9: DoD Checklist
- **File**: `technical-standards/config/dod.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 13 DoD items
  - Each item has: id, check_item, verification_criteria fields

### Item 10: DoR Checklist
- **File**: `technical-standards/config/dor.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 4 DoR items
  - Each item has: id, prerequisite, verification fields

### Item 11: Conversation Log
- **File**: `technical-standards/conversation-log.md`
- **Checks**:
  - File exists and is non-empty
  - Contains session info header (Topic, Started timestamp)
  - Contains at least one logged entry with: Phase, Timestamp, Agent Question, User Response

### Item 12: Work Log
- **File**: `technical-standards/work-log.md`
- **Checks**:
  - File exists and is non-empty
  - Contains session info header
  - Contains timestamped entries with: Phase, Action, Result

### Item 13: DoD Verification
- **Checks**:
  - Evidence that self-verification was performed (logged in work-log.md)
  - All DoD-01 through DoD-12 items have been addressed
  - Any remediation actions are logged in work-log.md
  - Standards documentation directory contains at minimum one standards document

### Item 14: Standards Enforcement View
- **File**: `technical-standards/diagrams/standards-enforcement-view.md`
- **Checks**:
  - File exists and is non-empty
  - Contains linting and static analysis section (tools, scope, configuration)
  - Contains code review checklist (check items, categories, required/optional)
  - Contains CI/CD quality gates (build, test, coverage, security scan thresholds)
  - Contains automated vs. manual enforcement matrix
  - Contains enforcement flow diagram (Mermaid or PlantUML)

### Item 15: NFR Alignment Note
- **File**: `technical-standards/nfr-alignment.md`
- **Checks**:
  - File exists and is non-empty
  - Contains NFR-to-standards mapping table
  - Covers key NFR categories: performance, security, maintainability, reliability
  - Lists code quality SLO/SLI targets (coverage, complexity, duplication, vulnerability count)
  - Contains constraints section with identified limitations
  - Contains assumptions section with risk-if-invalid assessments

### Item 16: Standards Completeness
- **File**: `technical-standards/technical-standards-report.md`
- **Checks**:
  - Coding standards section covers naming, formatting, file organization, commenting
  - Design patterns catalog covers presentation, business, data, integration layers
  - Error handling standards cover exception hierarchy, error codes, retry policies
  - Logging standards cover log levels, structured logging, correlation IDs
  - Testing standards cover test types, coverage thresholds, naming conventions
  - Security coding standards cover input validation, output encoding, secrets management

### Item 17: Upstream Traceability
- **Checks**:
  - References to SA-REQ-001..005 (Wave 9 inputs) appear in conversation log or work log
  - Technical standards decisions are traceable to upstream requirements and NFRs
  - Design rationale documented in Architecture Decision Records
