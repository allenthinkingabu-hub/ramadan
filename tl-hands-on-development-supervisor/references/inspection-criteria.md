# Inspection Criteria -- tl-hands-on-development-supervisor

## Detailed Verification Criteria

### Item 1: Trigger Mechanism Config
- **File**: `hands-on-development/config/triggers.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least one trigger event definition
  - Each trigger has: id, event, source, condition fields
  - Metadata section includes task_id "TL-DEV-002"

### Item 2: RACI Matrix Config
- **File**: `hands-on-development/config/raci.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains role names (at minimum: TL, PM)
  - Contains task names mapped to each role
  - Each entry has one of: R, A, C, I assignment

### Item 3: Skills List Config
- **File**: `hands-on-development/config/skills.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 5 skill items
  - Each skill has: id, name, proficiency fields

### Item 4: Knowledge Base Checklist
- **File**: `hands-on-development/config/knowledge-domains.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 5 knowledge domain items
  - Each domain has: id, domain, scope fields

### Item 5: Tools List
- **File**: `hands-on-development/config/tools.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 3 tool items
  - Each tool has: id, tool, purpose fields

### Item 6: MCP Tools List
- **File**: `hands-on-development/config/mcp-tools.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 1 MCP tool item
  - Each MCP tool has: id, tool, purpose fields

### Item 7: Output Content List + Templates
- **Files**: `hands-on-development/config/outputs.yaml` + `hands-on-development/templates/`
- **Checks**:
  - outputs.yaml exists, is valid YAML, lists all deliverables
  - templates/ directory exists and contains template files
  - Each output item has: id, deliverable, file_path, format fields

### Item 8: SOP Process Checklist
- **File**: `hands-on-development/config/sop.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains sequential phases (Phase 0 through Phase 5)
  - Each phase has numbered steps

### Item 9: DoD Checklist
- **File**: `hands-on-development/config/dod.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 13 DoD items
  - Each item has: id, check_item, verification_criteria fields

### Item 10: DoR Checklist
- **File**: `hands-on-development/config/dor.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 4 DoR items
  - Each item has: id, prerequisite, verification fields

### Item 11: Conversation Log
- **File**: `hands-on-development/conversation-log.md`
- **Checks**:
  - File exists and is non-empty
  - Contains session info header (Topic, Started timestamp)
  - Contains at least one logged entry with: Phase, Timestamp, Agent Question, User Response

### Item 12: Work Log
- **File**: `hands-on-development/work-log.md`
- **Checks**:
  - File exists and is non-empty
  - Contains session info header
  - Contains timestamped entries with: Phase, Action, Result

### Item 13: DoD Verification
- **Checks**:
  - Evidence that self-verification was performed (logged in work-log.md)
  - All DoD-01 through DoD-12 items have been addressed
  - Any remediation actions are logged in work-log.md

### Item 14: Implementation Patterns
- **File**: `hands-on-development/implementation-patterns.md`
- **Checks**:
  - File exists and is non-empty
  - Contains pattern definitions with rationale
  - Contains anti-patterns to avoid
  - Patterns are linked to reference implementation code

### Item 15: Reference Implementations
- **Directory**: `hands-on-development/implementations/`
- **Checks**:
  - Directory exists and contains code files
  - Code includes tests (unit and/or integration)
  - Code follows established coding standards
  - Code includes inline documentation

### Item 16: Architecture Alignment
- **Checks**:
  - Implementations conform to IA-REQ-001 architecture design
  - Design patterns match architectural decisions
  - Integration points follow specified protocols

### Item 17: Upstream Traceability
- **Checks**:
  - References to upstream architecture design documents appear in conversation log or work log
  - Implementation decisions are traceable to upstream requirements
  - Technical decisions documented with rationale
