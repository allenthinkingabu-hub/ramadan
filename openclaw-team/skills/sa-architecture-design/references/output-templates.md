# Output Content List & Templates — sa-architecture-design

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
| OUT-13 | Architecture Design Report | `architecture-design-report.md` | Markdown |
| OUT-14 | Phase Question Lists | `phase{N}-questions.md` | Markdown |
| OUT-15 | Research Artifacts | `research/` | Mixed |
| OUT-16 | Architecture Diagrams | `diagrams/` | Mermaid/PlantUML/Markdown |
| OUT-17 | Interface/Integration View | `diagrams/integration-view.md` | Markdown + Mermaid |
| OUT-18 | NFR Alignment Note | `nfr-alignment.md` | Markdown |

All paths are relative to the `architecture-design/` output directory.

---

## Templates

### Template: YAML Config File (OUT-01 through OUT-10)

```yaml
# {Config Name} — sa-architecture-design Agent
# Task: IA-REQ-001 Architecture Design
# Generated: {timestamp}
# Modifiable: Yes

metadata:
  task_id: "IA-REQ-001"
  task_name: "Architecture Design"
  role: "System Architect (SA)"
  generated_at: "{timestamp}"

items:
  - id: "{PREFIX}-001"
    name: "{item_name}"
    description: "{item_description}"
```

### Template: Conversation Log (OUT-11)

```markdown
# Conversation Log — Architecture Design (IA-REQ-001)

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
# Work Log — Architecture Design (IA-REQ-001)

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

### Template: Architecture Design Report (OUT-13)

```markdown
# Architecture Design Report

## 1. Executive Summary
{One-paragraph overview of architecture decisions and design approach}

## 2. Design Scope & Objectives
- **Purpose**: {why this architecture design was created}
- **Scope**: {what systems/components are covered}
- **Constraints**: {architectural constraints and limitations}
- **Upstream References**: {links to Technical Discovery / Feasibility Analysis reports}

## 3. Architecture Overview
### 3.1 C4 Context Diagram
{Mermaid/PlantUML diagram showing system context}
See: `diagrams/c4-context.md`

### 3.2 C4 Container Diagram
{Mermaid/PlantUML diagram showing containers}
See: `diagrams/c4-container.md`

### 3.3 C4 Component Diagrams
{Mermaid/PlantUML diagrams for key components}
See: `diagrams/c4-component-*.md`

## 4. Detailed Design
### 4.1 UML Sequence Diagrams
{Key interaction flows}
See: `diagrams/uml-sequence-*.md`

### 4.2 UML Class Diagrams
{Domain model and key class structures}
See: `diagrams/uml-class-*.md`

### 4.3 Data Flow Diagrams
{Data flows between components}
See: `diagrams/data-flow-*.md`

## 5. Deployment Architecture
{Infrastructure and deployment topology}
- Capture RPO/RTO targets per tier
- Describe backup/restore strategy (scope, frequency, retention, validation)
- Note chaos/DR test cadence and last/next planned drill
See: `diagrams/deployment.md`

## 6. Interface/Integration View
### 6.1 Communication Protocols
{REST, gRPC, GraphQL, messaging patterns used between components}

### 6.2 Interface Contracts
{API specifications, message schemas, data formats, **versioning/deprecation policy**}

### 6.3 Error Handling & Resilience
{Retry policies, circuit breaker patterns, **rate limits/backpressure**, fallback strategies, timeout configurations}

### 6.4 Data Minimization & External Calls
{What data leaves the boundary, minimization/anonymization rules for LLMs/3rd parties}

See: `diagrams/integration-view.md`

## 7. NFR Alignment Note
### 7.1 Performance & Scalability
{How the architecture addresses performance and scalability NFRs}

### 7.2 Security
{Security architecture decisions mapped to security NFRs}

### 7.3 Availability & Reliability
{HA, DR, and resilience patterns mapped to availability NFRs}

### 7.4 Resiliency
{Fault tolerance, graceful degradation, recovery patterns}

### 7.5 Observability
{Logging, monitoring, tracing strategy, **service SLO/SLI targets with alert thresholds, business KPIs (e.g., cost per grade, cache hit rate)**}

### 7.6 Constraints & Assumptions
{Architectural constraints, technology limitations, and key assumptions}

See: `nfr-alignment.md`

## 8. Architecture Decision Records
| ADR# | Decision | Rationale | Status |
|:---|:---|:---|:---|
| ADR-001 | {decision} | {rationale} | Accepted |

## 9. Risks & Mitigations
| Risk | Impact | Probability | Mitigation |
|:---|:---|:---|:---|
| {risk} | High/Med/Low | High/Med/Low | {mitigation} |

## 10. Appendices
- A: Full technology stack details
- B: Research references
- C: Stakeholder input summary
- D: Alternative architectures considered
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

### Template: Interface/Integration View (OUT-17)

```markdown
# Interface/Integration View — Architecture Design

## Generated: {timestamp}

## 1. Communication Protocols

| Interface | Protocol | Pattern | Description |
|:---|:---|:---|:---|
| {interface_name} | REST / gRPC / GraphQL / AMQP / Kafka | Sync / Async / Event-driven | {description} |

## 2. Interface Contracts

| Contract ID | Producer | Consumer | Format | Schema Location |
|:---|:---|:---|:---|:---|
| {contract_id} | {producer_system} | {consumer_system} | JSON / Protobuf / Avro | {schema_path_or_url} |

## 2.1 API Versioning & Deprecation
- Versioning strategy (path/header)
- Deprecation window and notification channel
- Backward-compat testing approach

## 3. Error Handling & Resilience

| Pattern | Scope | Configuration | Description |
|:---|:---|:---|:---|
| Retry | {interface} | max_retries: 3, backoff: exponential | {description} |
| Circuit Breaker | {interface} | threshold: 5, timeout: 30s | {description} |
| Rate Limit / Backpressure | {interface} | global/tenant limits; shed policy | {description} |
| Fallback | {interface} | strategy: cache / default | {description} |
| Timeout | {interface} | connect: 5s, read: 30s | {description} |

## 3.1 Data Minimization (External/LLM Calls)
- What data leaves boundary
- Anonymization/redaction rules
- Allowed providers per region

## 4. Integration Diagram

\`\`\`mermaid
{integration diagram source}
\`\`\`
```

### Template: NFR Alignment Note (OUT-18)

```markdown
# NFR Alignment Note — Architecture Design

## Generated: {timestamp}

## NFR-to-Architecture Mapping

| NFR Category | NFR Requirement | Architecture Decision | How Addressed |
|:---|:---|:---|:---|
| Performance | {nfr_requirement} | {decision} | {explanation} |
| Availability | {nfr_requirement} | {decision} | {explanation} |
| Security | {nfr_requirement} | {decision} | {explanation} |
| Resiliency | {nfr_requirement} | {decision} | {explanation} |
| Scalability | {nfr_requirement} | {decision} | {explanation} |

## Constraints

| Constraint ID | Description | Impact | Mitigation |
|:---|:---|:---|:---|
| CON-001 | {constraint} | {impact} | {mitigation} |

## Assumptions

| Assumption ID | Description | Risk if Invalid |
|:---|:---|:---|
| ASM-001 | {assumption} | {risk} |
```

### Template: Phase Question List (OUT-14)

```markdown
# Phase {N} Question List — Architecture Design

## Phase: {phase_name}
## Generated: {timestamp}

| Q# | Question | Category | Status | Answer Summary |
|:---|:---|:---|:---|:---|
| Q{N}-001 | {question_text} | {category} | Asked / Answered / Skipped | {summary} |
```
