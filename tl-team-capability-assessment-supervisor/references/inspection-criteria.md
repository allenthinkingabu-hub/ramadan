# Inspection Criteria — tl-team-capability-assessment-supervisor

## Detailed Verification Criteria

### Item 1: Trigger Mechanism Config
- **File**: `team-capability-assessment/config/triggers.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least one trigger event definition
  - Each trigger has: id, event, source, condition fields
  - Metadata section includes task_id "TL-INC-003"

### Item 2: RACI Matrix Config
- **File**: `team-capability-assessment/config/raci.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains role names (at minimum: TL, PM)
  - Contains task names mapped to each role
  - Each entry has one of: R, A, C, I assignment

### Item 3: Skills List Config
- **File**: `team-capability-assessment/config/skills.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 5 skill items
  - Each skill has: id, name, proficiency fields

### Item 4: Knowledge Base Checklist
- **File**: `team-capability-assessment/config/knowledge-domains.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 5 knowledge domain items
  - Each domain has: id, domain, scope fields

### Item 5: Tools List
- **File**: `team-capability-assessment/config/tools.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 3 tool items
  - Each tool has: id, tool, purpose fields

### Item 6: MCP Tools List
- **File**: `team-capability-assessment/config/mcp-tools.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 1 MCP tool item

### Item 7: Output Content List + Templates
- **Files**: `team-capability-assessment/config/outputs.yaml` + `team-capability-assessment/templates/`
- **Checks**:
  - outputs.yaml exists, is valid YAML, lists all deliverables
  - templates/ directory exists and contains template files

### Item 8: SOP Process Checklist
- **File**: `team-capability-assessment/config/sop.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains sequential phases (Phase 0 through Phase 5)

### Item 9: DoD Checklist
- **File**: `team-capability-assessment/config/dod.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 13 DoD items

### Item 10: DoR Checklist
- **File**: `team-capability-assessment/config/dor.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 4 DoR items

### Item 11: Conversation Log
- **File**: `team-capability-assessment/conversation-log.md`
- **Checks**:
  - File exists and is non-empty
  - Contains session info header
  - Contains at least one logged entry

### Item 12: Work Log
- **File**: `team-capability-assessment/work-log.md`
- **Checks**:
  - File exists and is non-empty
  - Contains timestamped entries

### Item 13: DoD Verification
- **Checks**:
  - Evidence that self-verification was performed
  - All DoD items have been addressed

### Item 14: Team Skills Matrix
- **File**: `team-capability-assessment/skills-matrix.md`
- **Checks**:
  - File exists and is non-empty
  - Contains individual skill ratings per team member
  - Contains required vs. current proficiency comparison
  - Uses consistent rating scale

### Item 15: Gap Analysis
- **File**: `team-capability-assessment/gap-analysis.md`
- **Checks**:
  - File exists and is non-empty
  - Identifies specific skill gaps with severity ratings
  - Assesses impact of each gap on project delivery
  - Provides actionable recommendations per gap

### Item 16: Development Plan
- **File**: `team-capability-assessment/development-plan.md`
- **Checks**:
  - File exists and is non-empty
  - Contains training recommendations with timelines
  - Contains hiring recommendations if gaps cannot be filled by training
  - Includes knowledge transfer strategies and mentoring plans

### Item 17: Upstream Traceability
- **Checks**:
  - References to IA-INC-001..008 (Wave 10 inputs) appear in conversation log or work log
  - Assessment criteria are derived from project technical requirements
  - Technology stack requirements from architect inputs are reflected in skill requirements
