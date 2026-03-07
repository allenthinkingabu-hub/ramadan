# Inspection Criteria -- sa-data-privacy-governance-supervisor

## Detailed Verification Criteria

### Item 1: Trigger Mechanism Config
- **File**: `data-privacy-governance/config/triggers.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least one trigger event definition
  - Each trigger has: id, event, source, condition fields
  - Metadata section includes task_id "IA-REQ-006"

### Item 2: RACI Matrix Config
- **File**: `data-privacy-governance/config/raci.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains role names (at minimum: SA, PM)
  - Contains task names mapped to each role
  - Each entry has one of: R, A, C, I assignment
  - Downstream notification section is present

### Item 3: Skills List Config
- **File**: `data-privacy-governance/config/skills.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 5 skill items
  - Each skill has: id, name, proficiency fields

### Item 4: Knowledge Base Checklist
- **File**: `data-privacy-governance/config/knowledge-domains.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 5 knowledge domain items
  - Each domain has: id, domain, scope fields

### Item 5: Tools List
- **File**: `data-privacy-governance/config/tools.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 3 tool items
  - Each tool has: id, tool, purpose fields

### Item 6: MCP Tools List
- **File**: `data-privacy-governance/config/mcp-tools.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 1 MCP tool item
  - Each MCP tool has: id, tool, purpose fields

### Item 7: Output Content List + Templates
- **Files**: `data-privacy-governance/config/outputs.yaml` + `data-privacy-governance/templates/`
- **Checks**:
  - outputs.yaml exists, is valid YAML, lists all deliverables
  - templates/ directory exists and contains template files
  - Each output item has: id, deliverable, file_path, format fields

### Item 8: SOP Process Checklist
- **File**: `data-privacy-governance/config/sop.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains sequential phases (Phase 0 through Phase 5)
  - Each phase has numbered steps

### Item 9: DoD Checklist
- **File**: `data-privacy-governance/config/dod.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 13 DoD items
  - Each item has: id, check_item, verification_criteria fields

### Item 10: DoR Checklist
- **File**: `data-privacy-governance/config/dor.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 4 DoR items
  - Each item has: id, prerequisite, verification fields

### Item 11: Conversation Log
- **File**: `data-privacy-governance/conversation-log.md`
- **Checks**:
  - File exists and is non-empty
  - Contains session info header (Topic, Started timestamp)
  - Contains at least one logged entry with: Phase, Timestamp, Agent Question, User Response

### Item 12: Work Log
- **File**: `data-privacy-governance/work-log.md`
- **Checks**:
  - File exists and is non-empty
  - Contains session info header
  - Contains timestamped entries with: Phase, Action, Result

### Item 13: DoD Verification
- **Checks**:
  - Evidence that self-verification was performed (logged in work-log.md)
  - All DoD-01 through DoD-12 items have been addressed
  - Any remediation actions are logged in work-log.md
  - Governance diagrams directory contains at minimum classification taxonomy and access control model

### Item 14: Regulatory Compliance View
- **File**: `data-privacy-governance/diagrams/regulatory-compliance-view.md`
- **Checks**:
  - File exists and is non-empty
  - Contains regulation-to-control mapping (GDPR, CCPA, HIPAA as applicable)
  - Contains Privacy Impact Assessment template and triggers
  - Contains Data Processing Agreement requirements
  - Contains breach notification procedures with timelines
  - Contains compliance flow diagram (Mermaid or PlantUML)

### Item 15: NFR Alignment Note
- **File**: `data-privacy-governance/nfr-alignment.md`
- **Checks**:
  - File exists and is non-empty
  - Contains NFR-to-governance mapping table
  - Covers key NFR categories: security, compliance, auditability, privacy
  - Lists privacy SLO/SLI targets (consent response time, DSAR response time, encryption coverage)
  - Contains constraints section with identified limitations
  - Contains assumptions section with risk-if-invalid assessments

### Item 16: Governance Completeness
- **File**: `data-privacy-governance/data-privacy-governance-report.md`
- **Checks**:
  - Data classification taxonomy with sensitivity levels and handling requirements
  - Data retention policy with periods, legal basis, deletion methods
  - Data residency requirements with geographic constraints and transfer mechanisms
  - Access control model with RBAC/ABAC design and review cadence
  - Consent management framework with data subject rights workflows

### Item 17: Upstream Traceability
- **Checks**:
  - References to SA-REQ-001..005 (Wave 9 inputs) appear in conversation log or work log
  - Governance decisions are traceable to upstream requirements and NFRs
  - Design rationale documented in Architecture Decision Records
