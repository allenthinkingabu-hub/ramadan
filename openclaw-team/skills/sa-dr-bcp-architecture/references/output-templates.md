# Output Content List & Templates -- sa-dr-bcp-architecture

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
| OUT-13 | DR/BCP Architecture Report | `dr-bcp-architecture-report.md` | Markdown |
| OUT-14 | Phase Question Lists | `phase{N}-questions.md` | Markdown |
| OUT-15 | Research Artifacts | `research/` | Mixed |
| OUT-16 | DR/BCP Diagrams | `diagrams/` | Mermaid/PlantUML/Markdown |
| OUT-17 | Resilience Architecture View | `diagrams/resilience-architecture-view.md` | Markdown + Mermaid |
| OUT-18 | NFR Alignment Note | `nfr-alignment.md` | Markdown |

All paths are relative to the `dr-bcp-architecture/` output directory.

---

## Templates

### Template: YAML Config File (OUT-01 through OUT-10)

```yaml
# {Config Name} -- sa-dr-bcp-architecture Agent
# Task: IA-REQ-007 DR/BCP Architecture
# Generated: {timestamp}
# Modifiable: Yes

metadata:
  task_id: "IA-REQ-007"
  task_name: "DR/BCP Architecture"
  role: "System Architect (SA)"
  generated_at: "{timestamp}"

items:
  - id: "{PREFIX}-001"
    name: "{item_name}"
    description: "{item_description}"
```

### Template: Conversation Log (OUT-11)

```markdown
# Conversation Log -- DR/BCP Architecture (IA-REQ-007)

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
# Work Log -- DR/BCP Architecture (IA-REQ-007)

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

### Template: DR/BCP Architecture Report (OUT-13)

```markdown
# DR/BCP Architecture Report

## 1. Executive Summary
{One-paragraph overview of DR/BCP architecture decisions and approach}

## 2. Scope & Objectives
- **Purpose**: {why this DR/BCP architecture was created}
- **Scope**: {services, tiers, and environments covered}
- **Constraints**: {budget, regulatory, infrastructure constraints}
- **Upstream References**: {links to SAD, NFR Mapping, Technology Blueprint}

## 3. RPO/RTO Target Matrix
| Service/Tier | RPO | RTO | Business Justification | Recovery Strategy |
|:---|:---|:---|:---|:---|
| Tier 1 (Critical) | {rpo} | {rto} | {justification} | {strategy} |
| Tier 2 (Important) | {rpo} | {rto} | {justification} | {strategy} |
| Tier 3 (Standard) | {rpo} | {rto} | {justification} | {strategy} |

## 4. Failover Topology
### 4.1 Architecture Pattern
{Active-passive, active-active, pilot light, warm standby selection and rationale}
See: `diagrams/failover-topology.md`

### 4.2 DNS & Traffic Management
{Route53/CloudFlare health checks, failover routing, TTL configuration}

### 4.3 Multi-Region Deployment
{Region selection, data sovereignty alignment, latency considerations}

## 5. Backup/Restore Strategy
### 5.1 Backup Schedule
| Component | Scope | Frequency | Retention | Storage Location | Encryption |
|:---|:---|:---|:---|:---|:---|
| {component} | {full/incremental} | {frequency} | {retention} | {location} | {yes/no} |

### 5.2 Restore Procedures
{Step-by-step restore for each component, validation checkpoints}

### 5.3 Backup Validation
{Testing frequency, automated restore verification, integrity checks}

## 6. Recovery Procedures (Runbooks)
### 6.1 Failure Scenarios
| Scenario | Detection | Trigger | Procedure | Estimated Recovery |
|:---|:---|:---|:---|:---|
| {scenario} | {monitoring/alert} | {automatic/manual} | {runbook_ref} | {time} |

### 6.2 Escalation Paths
{Escalation matrix, communication channels, stakeholder notification}

### 6.3 Communication Plan
{Internal/external communication templates, status page updates}

## 7. DR Testing Plan
### 7.1 Test Cadence
| Test Type | Frequency | Scope | Success Criteria |
|:---|:---|:---|:---|
| Tabletop exercise | {frequency} | {scope} | {criteria} |
| Component failover | {frequency} | {scope} | {criteria} |
| Full DR drill | {frequency} | {scope} | {criteria} |
| Chaos engineering | {frequency} | {scope} | {criteria} |

### 7.2 Last/Next Planned Drill
- Last drill: {date} -- Result: {pass/fail/findings}
- Next planned: {date} -- Scope: {scope}

## 8. Resilience Architecture View
See: `diagrams/resilience-architecture-view.md`

## 9. NFR Alignment Note
See: `nfr-alignment.md`

## 10. Architecture Decision Records
| ADR# | Decision | Rationale | Status |
|:---|:---|:---|:---|
| ADR-001 | {decision} | {rationale} | Accepted |

## 11. Risks & Mitigations
| Risk | Impact | Probability | Mitigation |
|:---|:---|:---|:---|
| {risk} | High/Med/Low | High/Med/Low | {mitigation} |

## 12. Appendices
- A: Full BIA results summary
- B: Research references
- C: Stakeholder input summary
- D: Alternative DR strategies considered
```

### Template: Resilience Architecture View (OUT-17)

```markdown
# Resilience Architecture View -- DR/BCP Architecture

## Generated: {timestamp}

## 1. Failure Domain Mapping

| Failure Domain | Components Affected | Blast Radius | Mitigation |
|:---|:---|:---|:---|
| AZ failure | {components} | {impact} | {mitigation} |
| Region failure | {components} | {impact} | {mitigation} |
| Service dependency | {components} | {impact} | {mitigation} |

## 2. Data Replication Patterns

| Data Store | Replication Type | RPO Impact | Consistency Model | Failover Mechanism |
|:---|:---|:---|:---|:---|
| {data_store} | Sync / Async / Multi-region | {rpo} | {strong/eventual} | {auto/manual} |

## 3. Graceful Degradation Strategies

| Service | Degradation Level | Trigger | User Impact | Recovery |
|:---|:---|:---|:---|:---|
| {service} | {partial/feature-flag/read-only} | {condition} | {impact} | {recovery_action} |

## 4. DNS & Traffic Management

| Component | Health Check | Failover Type | TTL | Configuration |
|:---|:---|:---|:---|:---|
| {component} | {endpoint} | {active-passive/weighted} | {ttl} | {config} |

## 5. Failover Topology Diagram

\`\`\`mermaid
{failover topology diagram source}
\`\`\`
```

### Template: NFR Alignment Note (OUT-18)

```markdown
# NFR Alignment Note -- DR/BCP Architecture

## Generated: {timestamp}

## NFR-to-DR/BCP Mapping

| NFR Category | NFR Requirement | DR/BCP Decision | How Addressed |
|:---|:---|:---|:---|
| Availability | {nfr_requirement} | {decision} | {explanation} |
| Durability | {nfr_requirement} | {decision} | {explanation} |
| Recovery | {nfr_requirement} | {decision} | {explanation} |
| Resilience | {nfr_requirement} | {decision} | {explanation} |

## Availability SLO/SLI Targets

| Metric | SLI Definition | SLO Target | Alert Threshold |
|:---|:---|:---|:---|
| Uptime | {definition} | {target} | {threshold} |
| Failover time | {definition} | {target} | {threshold} |
| Backup success rate | {definition} | {target} | {threshold} |
| Recovery validation | {definition} | {target} | {threshold} |

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
# Phase {N} Question List -- DR/BCP Architecture

## Phase: {phase_name}
## Generated: {timestamp}

| Q# | Question | Category | Status | Answer Summary |
|:---|:---|:---|:---|:---|
| Q{N}-001 | {question_text} | {category} | Asked / Answered / Skipped | {summary} |
```
