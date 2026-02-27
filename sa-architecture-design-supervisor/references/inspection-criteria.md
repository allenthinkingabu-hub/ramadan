# Inspection Criteria — sa-architecture-design-supervisor

## Detailed Verification Criteria

### Item 1: Trigger Mechanism Config
- **File**: `architecture-design/config/triggers.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least one trigger event definition
  - Each trigger has: id, event, source, condition fields
  - Metadata section includes task_id "IA-REQ-001"

### Item 2: RACI Matrix Config
- **File**: `architecture-design/config/raci.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains role names (at minimum: SA, PM)
  - Contains task names mapped to each role
  - Each entry has one of: R, A, C, I assignment
  - Downstream notification section is present

### Item 3: Skills List Config
- **File**: `architecture-design/config/skills.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 5 skill items
  - Each skill has: id, name, proficiency fields

### Item 4: Knowledge Base Checklist
- **File**: `architecture-design/config/knowledge-domains.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 5 knowledge domain items
  - Each domain has: id, domain, scope fields

### Item 5: Tools List
- **File**: `architecture-design/config/tools.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 3 tool items
  - Each tool has: id, tool, purpose fields

### Item 6: MCP Tools List
- **File**: `architecture-design/config/mcp-tools.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 1 MCP tool item
  - Each MCP tool has: id, tool, purpose fields

### Item 7: Output Content List + Templates
- **Files**: `architecture-design/config/outputs.yaml` + `architecture-design/templates/`
- **Checks**:
  - outputs.yaml exists, is valid YAML, lists all deliverables
  - templates/ directory exists and contains template files
  - Each output item has: id, deliverable, file_path, format fields

### Item 8: SOP Process Checklist
- **File**: `architecture-design/config/sop.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains sequential phases (Phase 0 through Phase 5)
  - Each phase has numbered steps

### Item 9: DoD Checklist
- **File**: `architecture-design/config/dod.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 13 DoD items
  - Each item has: id, check_item, verification_criteria fields

### Item 10: DoR Checklist
- **File**: `architecture-design/config/dor.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 4 DoR items
  - Each item has: id, prerequisite, verification fields

### Item 11: Conversation Log
- **File**: `architecture-design/conversation-log.md`
- **Checks**:
  - File exists and is non-empty
  - Contains session info header (Topic, Started timestamp)
  - Contains at least one logged entry with: Phase, Timestamp, Agent Question, User Response

### Item 12: Work Log
- **File**: `architecture-design/work-log.md`
- **Checks**:
  - File exists and is non-empty
  - Contains session info header
  - Contains timestamped entries with: Phase, Action, Result

### Item 13: DoD Verification
- **Checks**:
  - Evidence that self-verification was performed (logged in work-log.md)
  - All DoD-01 through DoD-12 items have been addressed
  - Any remediation actions are logged in work-log.md
  - Architecture diagrams directory contains at minimum C4 context and container diagrams

### Item 14: Interface/Integration View
- **File**: `architecture-design/diagrams/integration-view.md`
- **Checks**:
  - File exists and is non-empty
  - Contains communication protocols section (REST, gRPC, messaging patterns)
  - Contains interface contracts section (API specs, message schemas, error codes)
  - Contains error handling and resilience patterns (retry, circuit breaker, fallback)
  - Contains integration diagram (Mermaid or PlantUML)

### Item 15: NFR Alignment Note
- **File**: `architecture-design/nfr-alignment.md`
- **Checks**:
  - File exists and is non-empty
  - Contains NFR-to-architecture mapping table
  - Covers key NFR categories: performance, availability, security, resiliency
  - Contains constraints section with identified limitations
  - Contains assumptions section with risk-if-invalid assessments

### Item 16: Upstream Traceability
- **Checks**:
  - References to SA-REQ-001..005 (Wave 9 inputs) appear in conversation log or work log
  - Architecture decisions are traceable to upstream requirements and NFRs
  - Design rationale documented in Architecture Decision Records
