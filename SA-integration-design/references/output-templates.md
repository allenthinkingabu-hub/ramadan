# Output Content List & Templates — SA-integration-design

## Output Content List

| Output ID | Deliverable | File Path | Format |
|:---|:---|:---|:---|
| OUT-01 | Trigger Mechanism Config | `config/triggers.yaml` | YAML |
| OUT-02 | RACI Matrix Config | `config/raci.yaml` | YAML |
| OUT-03 | Skills List Config | `config/skills.yaml` | YAML |
| OUT-04 | Knowledge Domains Config | `config/knowledge-domains.yaml` | YAML |
| OUT-05 | Tools List Config | `config/tools.yaml` | YAML |
| OUT-06 | MCP Tools Config | `config/mcp-tools.yaml` | YAML |
| OUT-07 | Output Content List Config | `config/outputs.yaml` | YAML |
| OUT-08 | SOP Process Config | `config/sop.yaml` | YAML |
| OUT-09 | DoD Checklist Config | `config/dod.yaml` | YAML |
| OUT-10 | DoR Checklist Config | `config/dor.yaml` | YAML |
| OUT-11 | Conversation Log | `conversation-log.md` | Markdown |
| OUT-12 | Work Log | `work-log.md` | Markdown |
| OUT-13 | Integration Design Report | `integration-design-report.md` | Markdown |
| OUT-14 | Phase Question Lists | `phase{N}-questions.md` | Markdown |
| OUT-15 | Research Artifacts | `research/` | Mixed |
| OUT-16 | Integration Diagrams | `diagrams/` | Mermaid/PlantUML/Markdown |
| OUT-17 | API Contract Specifications | `api-specs/` | OpenAPI/AsyncAPI/Proto |
| OUT-18 | Data Flow Diagrams | `diagrams/data-flow-*.md` | Markdown + Mermaid |
| OUT-19 | Third-Party Dependency Register | `third-party-register.md` | Markdown |
| OUT-20 | Integration Security Design | `integration-security-design.md` | Markdown |
| OUT-21 | Error Handling Strategy | `error-handling-strategy.md` | Markdown |
| OUT-22 | Integration Test Strategy | `integration-test-strategy.md` | Markdown |
| OUT-23 | Monitoring & Alerting Plan | `monitoring-alerting-plan.md` | Markdown |

All paths are relative to the `integration-design/` output directory.

---

## Templates

### Template: YAML Config File (OUT-01 through OUT-10)

```yaml
# {Config Name} — SA-integration-design Agent
# Task: IA-REQ-003 Integration Design
# Generated: {timestamp}
# Modifiable: Yes

metadata:
  task_id: "IA-REQ-003"
  task_name: "Integration Design"
  role: "System Architect (SA)"
  generated_at: "{timestamp}"

items:
  - id: "{PREFIX}-001"
    name: "{item_name}"
    description: "{item_description}"
```

### Template: Conversation Log (OUT-11)

```markdown
# Conversation Log — Integration Design (IA-REQ-003)

## Session Info
- Topic: {topic}
- Started: {timestamp}

---

## Entry #{N}
- **Phase**: {phase_name}
- **Timestamp**: {timestamp}
- **Agent Question**: {question}
- **User Response**: {response}
- **Notes**: {any_observations}
```

### Template: Work Log (OUT-12)

```markdown
# Work Log — Integration Design (IA-REQ-003)

## Session Info
- Topic: {topic}
- Started: {timestamp}

---

## [{timestamp}] {action_title}
- **Phase**: {phase}
- **Action**: {description_of_action}
- **Result**: {outcome}
- **Next Step**: {what_follows}
```

### Template: Integration Design Report (OUT-13)

```markdown
# Integration Design Report

## 1. Executive Summary
{One-paragraph overview of integration design decisions and approach}

## 2. Design Scope & Objectives
- **Purpose**: {why this integration design was created}
- **Scope**: {what systems/integrations are covered}
- **Constraints**: {integration constraints and limitations}
- **Upstream References**: {links to Architecture Design / Technology Stack reports}

## 3. Integration Strategy Overview
### 3.1 Integration Approach
{Overall integration philosophy: API-first, event-driven, hybrid, etc.}

### 3.2 Integration Topology
{Mermaid diagram showing high-level integration topology}
See: `diagrams/integration-topology.md`

### 3.3 Middleware & Gateway Architecture
{API gateway, service mesh, message broker topology}
See: `diagrams/middleware-topology.md`

## 4. API Contract Specifications
### 4.1 REST API Contracts
{Summary of REST API contracts with links to OpenAPI specs}
See: `api-specs/`

### 4.2 Event-Driven / Async Contracts
{Summary of async API contracts with links to AsyncAPI specs}
See: `api-specs/`

### 4.3 gRPC / Protocol Buffer Contracts
{Summary of gRPC service definitions}
See: `api-specs/`

### 4.4 API Versioning & Deprecation Policy
- Versioning strategy (path/header/query)
- Deprecation window and notification process
- Backward-compatibility testing approach

## 5. Data Flow Design
### 5.1 End-to-End Data Flows
{Data flow diagrams for key integration scenarios}
See: `diagrams/data-flow-*.md`

### 5.2 Data Transformation Mappings
{Schema mappings between source and target formats}

### 5.3 Data Validation Rules
{Validation rules at integration boundaries}

## 6. Third-Party Dependencies
{Catalog of all external dependencies with risk assessment}
See: `third-party-register.md`

| Dependency | Provider | SLA | Risk Level | Fallback Strategy |
|:---|:---|:---|:---|:---|
| {name} | {provider} | {sla} | High/Med/Low | {fallback} |

## 7. Integration Security Design
### 7.1 Authentication & Authorization
{OAuth2, mTLS, API key management per integration point}

### 7.2 Data Encryption
{Encryption in transit and at rest for integration data}

### 7.3 API Threat Protection
{Rate limiting, input validation, OWASP API Top 10 mitigations}

See: `integration-security-design.md`

## 8. Error Handling & Resilience
### 8.1 Retry Strategies
{Retry policies per integration (exponential backoff, jitter)}

### 8.2 Circuit Breaker Configuration
{Circuit breaker settings per integration}

### 8.3 Fallback & Degradation
{Graceful degradation and fallback strategies}

### 8.4 Dead-Letter Queue Handling
{DLQ configuration and poison message handling}

### 8.5 Timeout Configuration
{Connection and read timeouts per integration}

See: `error-handling-strategy.md`

## 9. Message Protocol Specifications
| Integration | Protocol | Pattern | Justification |
|:---|:---|:---|:---|
| {integration} | REST/gRPC/Kafka/AMQP | Sync/Async/Event | {rationale} |

## 10. Integration Testing Strategy
### 10.1 Contract Testing
{Consumer-driven contract testing approach}

### 10.2 Integration Testing
{Integration test scope, environment, data}

### 10.3 End-to-End Testing
{E2E test scenarios covering integration flows}

### 10.4 Mock Services
{Service virtualization and mock approach}

See: `integration-test-strategy.md`

## 11. Monitoring & Alerting
### 11.1 Distributed Tracing
{OpenTelemetry/Jaeger tracing setup}

### 11.2 Health Checks
{Health check endpoints and monitoring}

### 11.3 SLA/SLO Monitoring
{SLO/SLI targets with alert thresholds}

### 11.4 Integration Dashboards
{Key metrics and dashboard design}

See: `monitoring-alerting-plan.md`

## 12. Integration Decision Records
| IDR# | Decision | Rationale | Status |
|:---|:---|:---|:---|
| IDR-001 | {decision} | {rationale} | Accepted |

## 13. Risks & Mitigations
| Risk | Impact | Probability | Mitigation |
|:---|:---|:---|:---|
| {risk} | High/Med/Low | High/Med/Low | {mitigation} |

## 14. Appendices
- A: Full API contract index
- B: Research references
- C: Stakeholder input summary
- D: Alternative integration approaches considered
```

### Template: Phase Question List (OUT-14)

```markdown
# Phase {N} Question List — Integration Design

## Phase: {phase_name}
## Generated: {timestamp}

| Q# | Question | Category | Status | Answer Summary |
|:---|:---|:---|:---|:---|
| Q{N}-001 | {question_text} | {category} | Asked / Answered / Skipped | {summary} |
```

### Template: Mermaid Diagram File (OUT-16)

```markdown
# {Diagram Title}

## Description
{What this diagram shows and its purpose}

## Diagram

\`\`\`mermaid
{mermaid diagram source}
\`\`\`

## Notes
{Any additional notes or considerations}
```

### Template: Third-Party Dependency Register (OUT-19)

```markdown
# Third-Party Dependency Register — Integration Design

## Generated: {timestamp}

## Dependencies

| Dep ID | Name | Provider | Type | SLA | Risk Level | Fallback | Owner |
|:---|:---|:---|:---|:---|:---|:---|:---|
| DEP-001 | {name} | {provider} | SaaS/API/Library | {sla} | High/Med/Low | {fallback} | {owner} |

## Risk Assessment Summary

| Risk Level | Count | Mitigation Strategy |
|:---|:---|:---|
| High | {n} | {strategy} |
| Medium | {n} | {strategy} |
| Low | {n} | {strategy} |
```

### Template: Integration Security Design (OUT-20)

```markdown
# Integration Security Design — Integration Design

## Generated: {timestamp}

## 1. Authentication & Authorization Matrix

| Integration Point | Auth Method | Token/Key Rotation | Notes |
|:---|:---|:---|:---|
| {integration} | OAuth2 / mTLS / API Key / JWT | {rotation_policy} | {notes} |

## 2. Data Encryption

| Data Flow | In Transit | At Rest | Classification |
|:---|:---|:---|:---|
| {flow} | TLS 1.3 / mTLS | AES-256 | PII / Sensitive / Public |

## 3. API Threat Protection

| Threat | Mitigation | Configuration |
|:---|:---|:---|
| Rate limiting | {approach} | {config} |
| Input validation | {approach} | {config} |
| Injection attacks | {approach} | {config} |
```

### Template: Error Handling Strategy (OUT-21)

```markdown
# Error Handling Strategy — Integration Design

## Generated: {timestamp}

## Resilience Patterns per Integration

| Integration | Retry | Circuit Breaker | Timeout | Fallback | DLQ |
|:---|:---|:---|:---|:---|:---|
| {integration} | max: 3, backoff: exp | threshold: 5, reset: 30s | connect: 5s, read: 30s | cache/default | {queue} |

## Error Classification

| Error Type | Category | Response | Escalation |
|:---|:---|:---|:---|
| {error} | Transient/Permanent | Retry/Fail/Degrade | {escalation} |
```

### Template: Integration Test Strategy (OUT-22)

```markdown
# Integration Test Strategy — Integration Design

## Generated: {timestamp}

## 1. Contract Testing

| Contract | Producer | Consumer | Tool | Frequency |
|:---|:---|:---|:---|:---|
| {contract} | {producer} | {consumer} | Pact/Schemathesis | CI/Nightly |

## 2. Integration Test Scenarios

| Scenario ID | Description | Systems Involved | Priority |
|:---|:---|:---|:---|
| IT-001 | {scenario} | {systems} | P1/P2/P3 |

## 3. Mock Services

| Service | Mock Tool | Scope | Notes |
|:---|:---|:---|:---|
| {service} | WireMock/Mockoon | Contract/Behavior | {notes} |
```

### Template: Monitoring & Alerting Plan (OUT-23)

```markdown
# Monitoring & Alerting Plan — Integration Design

## Generated: {timestamp}

## 1. SLO/SLI Targets

| Integration | SLI | SLO Target | Alert Threshold | Escalation |
|:---|:---|:---|:---|:---|
| {integration} | Latency p99 | < 200ms | > 500ms for 5min | PagerDuty |
| {integration} | Availability | 99.9% | < 99.5% for 15min | PagerDuty |
| {integration} | Error rate | < 0.1% | > 1% for 5min | Slack alert |

## 2. Health Check Endpoints

| Service | Endpoint | Interval | Timeout |
|:---|:---|:---|:---|
| {service} | /health | 30s | 5s |

## 3. Distributed Tracing

- Tracing framework: {OpenTelemetry/Jaeger/Zipkin}
- Sampling rate: {percentage}
- Trace propagation: {W3C Trace Context / B3}

## 4. Dashboard Metrics

| Metric | Source | Visualization | Alert |
|:---|:---|:---|:---|
| {metric} | {source} | Graph/Counter/Gauge | {threshold} |
```
