# Inspection Criteria -- tl-unblocking-the-team-supervisor

## Detailed Verification Criteria

### Item 1: Trigger Mechanism Config
- **File**: `unblocking-the-team/config/triggers.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least one trigger event definition
  - Each trigger has: id, event, source, condition fields
  - Metadata section includes task_id "TL-DEV-004"

### Item 2: RACI Matrix Config
- **File**: `unblocking-the-team/config/raci.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains role names (at minimum: TL, PM)
  - Contains task names mapped to each role

### Item 3: Skills List Config
- **File**: `unblocking-the-team/config/skills.yaml`
- **Checks**: File exists, valid YAML, at least 5 skill items with id, name, proficiency

### Item 4: Knowledge Base Checklist
- **File**: `unblocking-the-team/config/knowledge-domains.yaml`
- **Checks**: File exists, valid YAML, at least 5 domains with id, domain, scope

### Item 5: Tools List
- **File**: `unblocking-the-team/config/tools.yaml`
- **Checks**: File exists, valid YAML, at least 3 tools with id, tool, purpose

### Item 6: MCP Tools List
- **File**: `unblocking-the-team/config/mcp-tools.yaml`
- **Checks**: File exists, valid YAML, at least 1 MCP tool

### Item 7: Output Content List + Templates
- **Files**: `unblocking-the-team/config/outputs.yaml` + `unblocking-the-team/templates/`
- **Checks**: Both exist with proper content

### Item 8: SOP Process Checklist
- **File**: `unblocking-the-team/config/sop.yaml`
- **Checks**: File exists, valid YAML, contains Phase 0-5

### Item 9: DoD Checklist
- **File**: `unblocking-the-team/config/dod.yaml`
- **Checks**: File exists, valid YAML, at least 13 items

### Item 10: DoR Checklist
- **File**: `unblocking-the-team/config/dor.yaml`
- **Checks**: File exists, valid YAML, at least 4 items

### Item 11: Conversation Log
- **File**: `unblocking-the-team/conversation-log.md`
- **Checks**: File exists, non-empty, contains session info and logged entries

### Item 12: Work Log
- **File**: `unblocking-the-team/work-log.md`
- **Checks**: File exists, non-empty, contains timestamped entries

### Item 13: DoD Verification
- **Checks**: Self-verification performed, remediation logged

### Item 14: Blocker Resolution Report
- **File**: `unblocking-the-team/blocker-resolution-report.md`
- **Checks**:
  - File exists and is non-empty
  - Contains blocker inventory with severity classification
  - Each blocker has root cause analysis
  - Resolutions are documented with preventive actions

### Item 15: Escalation Framework
- **File**: `unblocking-the-team/escalation-framework.md`
- **Checks**:
  - File exists and is non-empty
  - Contains escalation levels with criteria
  - Contains escalation paths by blocker type
  - Contains SLAs for each level

### Item 16: Resolution Completeness
- **Checks**:
  - All identified blockers have documented status (resolved or escalated)
  - No blocker left without a resolution plan
  - Knowledge transfer documented for team learning

### Item 17: Upstream Traceability
- **Checks**:
  - System context from architecture design referenced
  - Resolutions consider architectural constraints
  - Debugging and resolution aligned with system design
