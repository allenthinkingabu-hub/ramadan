# Inspection Criteria -- sa-performance-load-testing-supervisor

## Detailed Verification Criteria

### Item 1: Trigger Mechanism Config
- **File**: `performance-load-testing/config/triggers.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least one trigger event definition
  - Each trigger has: id, event, source, condition fields
  - Metadata section includes task_id "IA-QA-001"

### Item 2: RACI Matrix Config
- **File**: `performance-load-testing/config/raci.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains role names (at minimum: SA, PM)
  - Contains task names mapped to each role
  - Each entry has one of: R, A, C, I assignment
  - Downstream notification section is present

### Item 3: Skills List Config
- **File**: `performance-load-testing/config/skills.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 5 skill items
  - Each skill has: id, name, proficiency fields

### Item 4: Knowledge Base Checklist
- **File**: `performance-load-testing/config/knowledge-domains.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 5 knowledge domain items
  - Each domain has: id, domain, scope fields

### Item 5: Tools List
- **File**: `performance-load-testing/config/tools.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 3 tool items
  - Each tool has: id, tool, purpose fields

### Item 6: MCP Tools List
- **File**: `performance-load-testing/config/mcp-tools.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 1 MCP tool item
  - Each MCP tool has: id, tool, purpose fields

### Item 7: Output Content List + Templates
- **Files**: `performance-load-testing/config/outputs.yaml` + `performance-load-testing/templates/`
- **Checks**:
  - outputs.yaml exists, is valid YAML, lists all deliverables
  - templates/ directory exists and contains template files
  - Each output item has: id, deliverable, file_path, format fields

### Item 8: SOP Process Checklist
- **File**: `performance-load-testing/config/sop.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains sequential phases (Phase 0 through Phase 5)
  - Each phase has numbered steps

### Item 9: DoD Checklist
- **File**: `performance-load-testing/config/dod.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 13 DoD items
  - Each item has: id, check_item, verification_criteria fields

### Item 10: DoR Checklist
- **File**: `performance-load-testing/config/dor.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 4 DoR items
  - Each item has: id, prerequisite, verification fields

### Item 11: Conversation Log
- **File**: `performance-load-testing/conversation-log.md`
- **Checks**:
  - File exists and is non-empty
  - Contains session info header (Topic, Started timestamp)
  - Contains at least one logged entry with: Phase, Timestamp, Agent Question, User Response

### Item 12: Work Log
- **File**: `performance-load-testing/work-log.md`
- **Checks**:
  - File exists and is non-empty
  - Contains session info header
  - Contains timestamped entries with: Phase, Action, Result

### Item 13: DoD Verification
- **Checks**:
  - Evidence that self-verification was performed (logged in work-log.md)
  - All DoD-01 through DoD-12 items have been addressed
  - Any remediation actions are logged in work-log.md

### Item 14: Test Scenarios
- **Directory**: `performance-load-testing/scenarios/`
- **Checks**:
  - Directory exists and contains scenario files
  - Covers load, stress, soak, and spike test types
  - Each scenario defines: objective, workload profile, duration, success criteria

### Item 15: Benchmark Definitions
- **File**: `performance-load-testing/scenarios/benchmarks.md`
- **Checks**:
  - File exists and is non-empty
  - Contains latency targets (p50, p95, p99)
  - Contains throughput targets (TPS/RPS)
  - Contains concurrency targets
  - Contains resource utilization thresholds

### Item 16: Test Execution Plan
- **File**: `performance-load-testing/test-execution-plan.md`
- **Checks**:
  - File exists and is non-empty
  - Contains test environment requirements
  - Contains tool selection and configuration
  - Contains execution schedule

### Item 17: Acceptance Criteria Matrix
- **File**: `performance-load-testing/acceptance-criteria.md`
- **Checks**:
  - File exists and is non-empty
  - Contains NFR-to-test mapping
  - Each criterion has pass/fail thresholds
  - Covers all identified NFR targets

### Item 18: NFR Traceability
- **Checks**:
  - Test scenarios reference specific NFR requirements
  - Benchmark targets are derived from architecture NFR mapping
  - Acceptance criteria link back to SLA/SLO definitions
