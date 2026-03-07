# Output Content List & Templates — sa-non-functional-requirements

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
| OUT-13 | NFR Specification Report | `nfr-report.md` | Markdown |
| OUT-14 | Phase Question Lists | `phase{N}-questions.md` | Markdown |
| OUT-15 | Research Artifacts | `research/` | Mixed |

All paths are relative to the `non-functional-requirements/` output directory.

---

## Templates

### Template: YAML Config File (OUT-01 through OUT-10)

```yaml
# {Config Name} — sa-non-functional-requirements Agent
# Task: IA-REQ-002 Non-Functional Requirements
# Generated: {timestamp}
# Modifiable: Yes

metadata:
  task_id: "IA-REQ-002"
  task_name: "Non-Functional Requirements"
  role: "System Architect (SA)"
  generated_at: "{timestamp}"

items:
  - id: "{PREFIX}-001"
    name: "{item_name}"
    description: "{item_description}"
```

### Template: Conversation Log (OUT-11)

```markdown
# Conversation Log — Non-Functional Requirements (IA-REQ-002)

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
# Work Log — Non-Functional Requirements (IA-REQ-002)

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

### Template: NFR Specification Report (OUT-13)

```markdown
# Non-Functional Requirements Report

## 1. Executive Summary
{One-paragraph overview of NFR scope, key quality attributes, and overall service-level strategy}

## 2. NFR Scope & Objectives
- **Purpose**: {why these NFRs are being defined}
- **Scope**: {what systems/components are covered}
- **Constraints**: {organizational, technical, and regulatory constraints}
- **Upstream References**: {links to Architecture Design / Technical Discovery / Feasibility Analysis reports}

## 3. Performance Requirements
### 3.1 Response Time Targets
| Endpoint / Operation | P50 Target | P95 Target | P99 Target |
|:---|:---|:---|:---|
| {endpoint} | {target} | {target} | {target} |

### 3.2 Throughput Targets
| Scenario | Target (req/s) | Peak (req/s) |
|:---|:---|:---|
| {scenario} | {target} | {peak} |

### 3.3 Latency Budgets
{Latency budget breakdown across service chain}

## 4. Scalability Requirements
### 4.1 Scaling Strategy
{Horizontal vs vertical scaling approach}

### 4.2 Auto-Scaling Thresholds
| Metric | Scale-Up Threshold | Scale-Down Threshold | Min Instances | Max Instances |
|:---|:---|:---|:---|:---|
| {metric} | {threshold} | {threshold} | {min} | {max} |

### 4.3 Capacity Planning
{Expected growth, capacity forecasts, resource projections}

## 5. Security Requirements
### 5.1 Authentication & Authorization
{Authentication methods, authorization model, session management}

### 5.2 Encryption
{Data at rest, data in transit, key management}

### 5.3 Compliance
{Regulatory requirements: GDPR, SOC2, HIPAA, PCI-DSS, etc.}

### 5.4 Vulnerability Management
{Scanning, patching cadence, dependency management}

## 6. Availability & Disaster Recovery
### 6.1 Uptime SLA
| Service Tier | Uptime Target | Allowed Downtime / Month |
|:---|:---|:---|
| {tier} | {target}% | {downtime} |

### 6.2 RTO & RPO
| Scenario | RTO | RPO |
|:---|:---|:---|
| {scenario} | {rto} | {rpo} |

### 6.3 Failover Strategy
{Active-passive, active-active, multi-region, etc.}

## 7. Maintainability Requirements
### 7.1 Code Quality Standards
{Linting, test coverage targets, code review process}

### 7.2 Deployment Frequency
{Release cadence, deployment strategy, rollback procedures}

### 7.3 Documentation Standards
{API docs, runbooks, architecture decision records}

## 8. Observability Requirements
### 8.1 Logging
{Log levels, retention, centralized logging platform}

### 8.2 Monitoring
{Metrics collection, dashboards, health checks}

### 8.3 Alerting
{Alert thresholds, escalation paths, on-call rotation}

### 8.4 Distributed Tracing
{Tracing framework, sampling rate, trace retention}

## 9. SLA/SLO/SLI Specification Table
| Service | SLI (Metric) | SLO (Target) | SLA (Commitment) | Error Budget |
|:---|:---|:---|:---|:---|
| {service} | {sli} | {slo} | {sla} | {budget} |

## 10. NFR-to-Architecture Mapping
| NFR Category | NFR ID | Architecture Component | Implementation Notes |
|:---|:---|:---|:---|
| {category} | {nfr_id} | {component} | {notes} |

## 11. Risks & Mitigations
| Risk | Impact | Probability | Mitigation |
|:---|:---|:---|:---|
| {risk} | High/Med/Low | High/Med/Low | {mitigation} |

## 12. Appendices
- A: Full NFR traceability matrix
- B: Research references and benchmarks
- C: Stakeholder input summary
- D: Load testing strategy
- E: Compliance checklist details
```

### Template: Phase Question List (OUT-14)

```markdown
# Phase {N} Question List — Non-Functional Requirements

## Phase: {phase_name}
## Generated: {timestamp}

| Q# | Question | Category | Status | Answer Summary |
|:---|:---|:---|:---|:---|
| Q{N}-001 | {question_text} | {category} | Asked / Answered / Skipped | {summary} |
```
