# Inspection Criteria -- sa-security-review-supervisor

## Detailed Verification Criteria

### Item 1: Trigger Mechanism Config
- **File**: `security-review/config/triggers.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least one trigger event definition
  - Metadata section includes task_id "IA-QA-002"

### Item 2: RACI Matrix Config
- **File**: `security-review/config/raci.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains role names (at minimum: SA, PM)
  - Contains task names mapped to each role
  - Downstream notification section is present

### Item 3: Skills List Config
- **File**: `security-review/config/skills.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 5 skill items
  - Each skill has: id, name, proficiency fields

### Item 4: Knowledge Base Checklist
- **File**: `security-review/config/knowledge-domains.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 5 knowledge domain items

### Item 5: Tools List
- **File**: `security-review/config/tools.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 3 tool items

### Item 6: MCP Tools List
- **File**: `security-review/config/mcp-tools.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 1 MCP tool item

### Item 7: Output Content List + Templates
- **Files**: `security-review/config/outputs.yaml` + `security-review/templates/`
- **Checks**:
  - outputs.yaml exists, is valid YAML, lists all deliverables
  - templates/ directory exists and contains template files

### Item 8: SOP Process Checklist
- **File**: `security-review/config/sop.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains sequential phases (Phase 0 through Phase 5)

### Item 9: DoD Checklist
- **File**: `security-review/config/dod.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 13 DoD items

### Item 10: DoR Checklist
- **File**: `security-review/config/dor.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 4 DoR items

### Item 11: Conversation Log
- **File**: `security-review/conversation-log.md`
- **Checks**:
  - File exists and is non-empty
  - Contains session info header (Topic, Started timestamp)
  - Contains at least one logged entry with: Phase, Timestamp, Agent Question, User Response

### Item 12: Work Log
- **File**: `security-review/work-log.md`
- **Checks**:
  - File exists and is non-empty
  - Contains timestamped entries with: Phase, Action, Result

### Item 13: DoD Verification
- **Checks**:
  - Evidence that self-verification was performed (logged in work-log.md)
  - All DoD-01 through DoD-12 items have been addressed

### Item 14: Threat Model
- **File**: `security-review/assessments/threat-model.md`
- **Checks**:
  - File exists and is non-empty
  - Contains structured content for threat model
  - STRIDE/DREAD threat model with mitigations

### Item 15: Vulnerability Assessment
- **File**: `security-review/assessments/vulnerability-assessment.md`
- **Checks**:
  - File exists and is non-empty
  - Contains structured content for vulnerability assessment
  - Identified vulnerabilities with severity and remediation

### Item 16: Security Policy Compliance
- **File**: `security-review/security-policy-compliance.md`
- **Checks**:
  - File exists and is non-empty
  - Contains structured content for security policy compliance
  - Policy compliance matrix with gap analysis

### Item 17: Security Test Plan
- **File**: `security-review/security-test-plan.md`
- **Checks**:
  - File exists and is non-empty
  - Contains structured content for security test plan
  - Penetration test and security scan planning

### Item 18: Upstream Traceability
- **Checks**:
  - Deliverables reference upstream architecture inputs
  - Decisions and findings are traceable to requirements
  - Rationale documented for key decisions
