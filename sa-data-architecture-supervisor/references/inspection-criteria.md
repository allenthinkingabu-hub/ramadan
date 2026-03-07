# Inspection Criteria -- sa-data-architecture-supervisor

## Detailed Verification Criteria

### Item 1: Trigger Mechanism Config
- **File**: `data-architecture/config/triggers.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least one trigger event definition
  - Each trigger has: id, event, source, condition fields
  - Metadata section includes task_id "IA-REQ-004"

### Item 2: RACI Matrix Config
- **File**: `data-architecture/config/raci.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains role names (at minimum: SA, PM)
  - Contains task names mapped to each role
  - Each entry has one of: R, A, C, I assignment
  - Downstream notification section is present

### Item 3: Skills List Config
- **File**: `data-architecture/config/skills.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 5 skill items
  - Each skill has: id, name, proficiency fields

### Item 4: Knowledge Base Checklist
- **File**: `data-architecture/config/knowledge-domains.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 5 knowledge domain items
  - Each domain has: id, domain, scope fields

### Item 5: Tools List
- **File**: `data-architecture/config/tools.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 3 tool items
  - Each tool has: id, tool, purpose fields

### Item 6: MCP Tools List
- **File**: `data-architecture/config/mcp-tools.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 1 MCP tool item
  - Each MCP tool has: id, tool, purpose fields

### Item 7: Output Content List + Templates
- **Files**: `data-architecture/config/outputs.yaml` + `data-architecture/templates/`
- **Checks**:
  - outputs.yaml exists, is valid YAML, lists all deliverables
  - templates/ directory exists and contains template files
  - Each output item has: id, deliverable, file_path, format fields

### Item 8: SOP Process Checklist
- **File**: `data-architecture/config/sop.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains sequential phases (Phase 0 through Phase 5)
  - Each phase has numbered steps

### Item 9: DoD Checklist
- **File**: `data-architecture/config/dod.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 13 DoD items
  - Each item has: id, check_item, verification_criteria fields

### Item 10: DoR Checklist
- **File**: `data-architecture/config/dor.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 4 DoR items
  - Each item has: id, prerequisite, verification fields

### Item 11: Conversation Log
- **File**: `data-architecture/conversation-log.md`
- **Checks**:
  - File exists and is non-empty
  - Contains session info header (Topic, Started timestamp)
  - Contains at least one logged entry with: Phase, Timestamp, Agent Question, User Response

### Item 12: Work Log
- **File**: `data-architecture/work-log.md`
- **Checks**:
  - File exists and is non-empty
  - Contains session info header
  - Contains timestamped entries with: Phase, Action, Result

### Item 13: DoD Verification
- **Checks**:
  - Evidence that self-verification was performed (logged in work-log.md)
  - All DoD-01 through DoD-12 items have been addressed
  - Any remediation actions are logged in work-log.md
  - Data model diagrams directory contains at minimum logical and physical data model diagrams

### Item 14: Data Integration View
- **File**: `data-architecture/diagrams/data-integration-view.md`
- **Checks**:
  - File exists and is non-empty
  - Contains data exchange protocols section (CDC, batch, streaming, API)
  - Contains schema contracts section (Avro, Parquet, JSON Schema, versioning/evolution)
  - Contains data quality and validation rules (completeness, accuracy, freshness, reconciliation)
  - Documents data masking/anonymization rules for sensitive data per environment
  - Contains data flow diagram (Mermaid or PlantUML)

### Item 15: NFR Alignment Note
- **File**: `data-architecture/nfr-alignment.md`
- **Checks**:
  - File exists and is non-empty
  - Contains NFR-to-data-architecture mapping table
  - Covers key NFR categories: performance, availability, consistency, scalability
  - Lists data SLO/SLI targets (query latency, throughput, freshness, completeness)
  - Contains constraints section with identified limitations
  - Contains assumptions section with risk-if-invalid assessments

### Item 16: Data Model Completeness
- **File**: `data-architecture/diagrams/` (logical and physical models) + report sections
- **Checks**:
  - Logical data model diagram exists with entity relationships
  - Physical data model diagram exists with table definitions and indexes
  - Storage strategy documented with technology selection and justification per data domain
  - Data migration plan includes source-target mapping, sequence, rollback strategy
  - Data lifecycle/tiering policy documented (hot/warm/cold, archival, TTL)

### Item 17: Upstream Traceability
- **Checks**:
  - References to SA-REQ-001..005 (Wave 9 inputs) appear in conversation log or work log
  - Data architecture decisions are traceable to upstream requirements and NFRs
  - Design rationale documented in Architecture Decision Records
