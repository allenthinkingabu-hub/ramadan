# Inspection Criteria — SA-integration-design-supervisor

## Detailed Verification Criteria

### Item 1: Trigger Mechanism Config
- **File**: `integration-design/config/triggers.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least one trigger event definition
  - Each trigger has: id, event, source, condition fields
  - Metadata section includes task_id "IA-REQ-003"

### Item 2: RACI Matrix Config
- **File**: `integration-design/config/raci.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains role names (at minimum: SA, PM, TL)
  - Contains task names mapped to each role
  - Each entry has one of: R, A, C, I assignment
  - Downstream notification section is present

### Item 3: Skills List Config
- **File**: `integration-design/config/skills.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 5 skill items
  - Each skill has: id, name, proficiency fields

### Item 4: Knowledge Base Checklist
- **File**: `integration-design/config/knowledge-domains.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 5 knowledge domain items
  - Each domain has: id, domain, scope fields

### Item 5: Tools List
- **File**: `integration-design/config/tools.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 3 tool items
  - Each tool has: id, tool, purpose fields

### Item 6: MCP Tools List
- **File**: `integration-design/config/mcp-tools.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 1 MCP tool item
  - Each MCP tool has: id, tool, purpose fields

### Item 7: Output Content List + Templates
- **Files**: `integration-design/config/outputs.yaml` + `integration-design/templates/`
- **Checks**:
  - outputs.yaml exists, is valid YAML, lists all deliverables
  - templates/ directory exists and contains template files
  - Each output item has: id, deliverable, file_path, format fields

### Item 8: SOP Process Checklist
- **File**: `integration-design/config/sop.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains sequential phases (Phase 0 through Phase 5)
  - Each phase has numbered steps

### Item 9: DoD Checklist
- **File**: `integration-design/config/dod.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 24 DoD items (DOD-001 through DOD-024)
  - Each item has: id, check_item, verification_criteria fields

### Item 10: DoR Checklist
- **File**: `integration-design/config/dor.yaml`
- **Checks**:
  - File exists and is valid YAML
  - Contains at least 4 DoR items
  - Each item has: id, prerequisite, verification fields

### Item 11: Conversation Log
- **File**: `integration-design/conversation-log.md`
- **Checks**:
  - File exists and is non-empty
  - Contains session info header (Topic, Started timestamp)
  - Contains at least one logged entry with: Phase, Timestamp, Agent Question, User Response

### Item 12: Work Log
- **File**: `integration-design/work-log.md`
- **Checks**:
  - File exists and is non-empty
  - Contains session info header
  - Contains timestamped entries with: Phase, Action, Result

### Item 13: DoD Verification
- **Checks**:
  - Evidence that self-verification was performed (logged in work-log.md)
  - All DOD-001 through DOD-024 items have been addressed
  - Any remediation actions are logged in work-log.md

### Item 14: Integration Design Report
- **File**: `integration-design/integration-design-report.md`
- **Checks**:
  - File exists and is non-empty
  - Contains all required sections: Executive Summary, Design Scope, Integration Strategy, API Contracts, Data Flows, Third-Party Dependencies, Security, Error Handling, Protocols, Testing, Monitoring, Decision Records, Risks
  - Integration decisions include rationale and trade-offs

### Item 15: API Contract Specifications
- **Directory**: `integration-design/api-specs/`
- **Checks**:
  - Directory exists and contains at least one specification file
  - Specifications are in valid format (OpenAPI YAML/JSON, AsyncAPI, Proto)
  - Each API contract covers: endpoints/operations, request/response schemas, error codes

### Item 16: Data Flow Diagrams
- **Files**: `integration-design/diagrams/data-flow-*.md`
- **Checks**:
  - At least one data flow diagram file exists
  - Each file contains a Mermaid or PlantUML diagram
  - Diagrams show source, transformation, and destination
  - Key integration scenarios are covered

### Item 17: Third-Party Dependency Register
- **File**: `integration-design/third-party-register.md`
- **Checks**:
  - File exists and is non-empty
  - Contains dependency catalog table with: name, provider, type, SLA, risk level
  - Each dependency has a fallback strategy defined
  - Risk assessment summary is included

### Item 18: Integration Security Design
- **File**: `integration-design/integration-security-design.md`
- **Checks**:
  - File exists and is non-empty
  - Contains authentication/authorization matrix per integration point
  - Contains data encryption specifications (in transit and at rest)
  - Contains API threat protection measures (rate limiting, input validation)
  - References OWASP API Top 10 where applicable

### Item 19: Error Handling Strategy
- **File**: `integration-design/error-handling-strategy.md`
- **Checks**:
  - File exists and is non-empty
  - Contains retry strategies per integration (exponential backoff, jitter)
  - Contains circuit breaker configuration (threshold, timeout, reset)
  - Contains fallback and degradation strategies
  - Contains timeout configuration (connect, read)
  - Contains dead-letter queue handling approach

### Item 20: Integration Test Strategy
- **File**: `integration-design/integration-test-strategy.md`
- **Checks**:
  - File exists and is non-empty
  - Contains contract testing approach (consumer-driven contracts)
  - Contains integration test scenarios with systems involved
  - Contains E2E test plan covering key integration flows
  - Contains mock service / service virtualization approach

### Item 21: Monitoring & Alerting Plan
- **File**: `integration-design/monitoring-alerting-plan.md`
- **Checks**:
  - File exists and is non-empty
  - Contains SLO/SLI targets with alert thresholds per integration
  - Contains health check endpoint definitions
  - Contains distributed tracing configuration
  - Contains dashboard metrics and visualization plan

### Item 22: Phase Question Lists
- **Files**: `integration-design/phase{N}-questions.md`
- **Checks**:
  - At least phase1, phase2, and phase3 question files exist
  - Each file contains questions in tabular format with: Q#, Question, Category, Status

### Item 23: Research Records
- **Directory**: `integration-design/research/`
- **Checks**:
  - Directory exists and contains at least one file
  - Research covers integration patterns, best practices, vendor documentation
  - Research process and sources are documented

### Item 24: Upstream Traceability
- **Checks**:
  - References to IA-REQ-001 (Architecture Design) appear in report or logs
  - References to IA-REQ-002 (Technology Stack Decision) appear in report or logs
  - Integration design decisions are traceable to upstream architecture and technology choices
  - Design rationale documented in Integration Decision Records
