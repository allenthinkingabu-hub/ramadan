# Inspection Criteria -- sa-cost-estimation-support-supervisor

## Detailed Verification Criteria

### Item 1: Trigger Mechanism Config
- **File**: `cost-estimation/config/triggers.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least one trigger event definition
  - Each trigger has: id, event, source, condition fields
  - Metadata section includes task_id "IA-INC-005"

### Item 2: RACI Matrix Config
- **File**: `cost-estimation/config/raci.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains role names (at minimum: SA, PM)
  - Contains task names mapped to each role
  - Each entry has one of: R, A, C, I assignment
  - Downstream notification section is present

### Item 3: Skills List Config
- **File**: `cost-estimation/config/skills.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 5 skill items
  - Each skill has: id, name, proficiency fields

### Item 4: Knowledge Base Checklist
- **File**: `cost-estimation/config/knowledge-domains.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 5 knowledge domain items
  - Each domain has: id, domain, scope fields

### Item 5: Tools List
- **File**: `cost-estimation/config/tools.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 3 tool items
  - Each tool has: id, tool, purpose fields

### Item 6: MCP Tools List
- **File**: `cost-estimation/config/mcp-tools.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 1 MCP tool item
  - Each MCP tool has: id, tool, purpose fields

### Item 7: Output Content List + Templates
- **Files**: `cost-estimation/config/outputs.yaml` + `cost-estimation/templates/`
- **Checks**:
  - outputs.yaml exists, is valid YAML, lists all deliverables
  - templates/ directory exists and contains template files
  - Each output item has: id, deliverable, file_path, format fields

### Item 8: SOP Process Checklist
- **File**: `cost-estimation/config/sop.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains sequential phases (Phase 0 through Phase 5)
  - Each phase has numbered steps

### Item 9: DoD Checklist
- **File**: `cost-estimation/config/dod.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 13 DoD items
  - Each item has: id, check_item, verification_criteria fields

### Item 10: DoR Checklist
- **File**: `cost-estimation/config/dor.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 4 DoR items
  - Each item has: id, prerequisite, verification fields

### Item 11: Conversation Log
- **File**: `cost-estimation/conversation-log.md`
- **Checks**:
  - File exists and is non-empty
  - Contains session info header (Topic, Started timestamp)
  - Contains at least one logged entry with: Phase, Timestamp, Agent Question, User Response

### Item 12: Work Log
- **File**: `cost-estimation/work-log.md`
- **Checks**:
  - File exists and is non-empty
  - Contains session info header
  - Contains timestamped entries with: Phase, Action, Result

### Item 13: DoD Verification
- **Checks**:
  - Evidence that self-verification was performed (logged in work-log.md)
  - All DoD-01 through DoD-12 items have been addressed
  - Any remediation actions are logged in work-log.md
  - Cost estimates contain numeric values, not just placeholders

### Item 14: Cost Breakdown Structure
- **File**: `cost-estimation/cost-breakdown.md`
- **Checks**:
  - File exists and is non-empty
  - Contains infrastructure costs with itemized compute, storage, networking
  - Contains licensing costs with software/service names and pricing models
  - Contains development effort with roles, durations, and rates
  - Contains operational costs with recurring items
  - Each line item has unit cost and total calculations

### Item 15: TCO Projection
- **File**: `cost-estimation/tco-projection.md`
- **Checks**:
  - File exists and is non-empty
  - Contains multi-year (minimum 3-year) cost projections
  - Contains build vs. buy analysis where applicable
  - Contains cost scaling model describing growth patterns
  - Year-over-year totals are consistent with cost breakdown

### Item 16: FinOps Guardrails
- **File**: `cost-estimation/finops-guardrails.md`
- **Checks**:
  - File exists and is non-empty
  - Contains budget thresholds per environment
  - Contains cost optimization recommendations with potential savings
  - Contains cost allocation tags and chargeback model
  - Alert thresholds are defined (80%, 100% of budget)

### Item 17: Upstream Traceability
- **Checks**:
  - References to SA-REQ-001..005 (Wave 9 inputs) appear in conversation log or work log
  - Cost estimates are traceable to Technology Blueprint (SA-REQ-004)
  - Infrastructure costs align with SAD (SA-REQ-001) deployment architecture
  - Integration costs reference SA-REQ-002 Integration Architecture
