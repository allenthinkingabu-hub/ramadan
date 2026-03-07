# Output Content List & Templates -- sa-data-architecture

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
| OUT-13 | Data Architecture Report | `data-architecture-report.md` | Markdown |
| OUT-14 | Phase Question Lists | `phase{N}-questions.md` | Markdown |
| OUT-15 | Research Artifacts | `research/` | Mixed |
| OUT-16 | Data Model Diagrams | `diagrams/` | Mermaid/PlantUML/Markdown |
| OUT-17 | Data Integration View | `diagrams/data-integration-view.md` | Markdown + Mermaid |
| OUT-18 | NFR Alignment Note | `nfr-alignment.md` | Markdown |

All paths are relative to the `data-architecture/` output directory.

---

## Templates

### Template: YAML Config File (OUT-01 through OUT-10)

```yaml
# {Config Name} -- sa-data-architecture Agent
# Task: IA-REQ-004 Data Architecture
# Generated: {timestamp}
# Modifiable: Yes

metadata:
  task_id: "IA-REQ-004"
  task_name: "Data Architecture"
  role: "System Architect (SA)"
  generated_at: "{timestamp}"

items:
  - id: "{PREFIX}-001"
    name: "{item_name}"
    description: "{item_description}"
```

### Template: Conversation Log (OUT-11)

```markdown
# Conversation Log -- Data Architecture (IA-REQ-004)

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
# Work Log -- Data Architecture (IA-REQ-004)

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

### Template: Data Architecture Report (OUT-13)

```markdown
# Data Architecture Report

## 1. Executive Summary
{One-paragraph overview of data architecture decisions and design approach}

## 2. Design Scope & Objectives
- **Purpose**: {why this data architecture was created}
- **Scope**: {what data domains/systems are covered}
- **Constraints**: {data architecture constraints and limitations}
- **Upstream References**: {links to SAD, Integration Architecture, Technology Blueprint}

## 3. Logical Data Model
### 3.1 Domain Entity Model
{Entity-relationship diagram showing domain entities and relationships}
See: `diagrams/logical-data-model.md`

### 3.2 Data Domain Boundaries
{Data domain decomposition and ownership}
See: `diagrams/data-domains.md`

## 4. Physical Data Model
### 4.1 Database Schema Design
{Table definitions, indexes, constraints}
See: `diagrams/physical-data-model.md`

### 4.2 Partitioning & Sharding Strategy
{Partitioning keys, shard distribution, rebalancing approach}

### 4.3 Indexing Strategy
{Primary, secondary, composite indexes; covering indexes}

## 5. Storage Strategy
### 5.1 Technology Selection
| Data Domain | Storage Technology | Justification |
|:---|:---|:---|
| {domain} | {RDBMS/NoSQL/DataLake/Cache} | {rationale} |

### 5.2 Data Lifecycle & Tiering
{Hot/warm/cold storage tiers, archival policies, TTL rules}

## 6. Data Flow & Integration
### 6.1 ETL/ELT Pipeline Design
{Pipeline architecture, transformation logic, scheduling}
See: `diagrams/data-flow-pipeline.md`

### 6.2 Data Lineage
{End-to-end data lineage from source to consumption}
See: `diagrams/data-lineage.md`

### 6.3 Change Data Capture (CDC)
{CDC patterns, tools, latency targets}

## 7. Data Migration Plan
### 7.1 Source-Target Mapping
| Source System | Source Object | Target System | Target Object | Transformation |
|:---|:---|:---|:---|:---|
| {source} | {table/collection} | {target} | {table/collection} | {transform_rule} |

### 7.2 Migration Sequence & Dependencies
{Ordered migration phases, dependency graph}

### 7.3 Rollback Strategy
{Rollback checkpoints, data reconciliation, validation gates}

### 7.4 Migration Window & Volume Estimates
{Data volumes, throughput targets, downtime constraints}

## 8. Data Integration View
### 8.1 Data Exchange Protocols
{CDC, batch, streaming, API patterns}

### 8.2 Schema Contracts
{Avro, Parquet, JSON Schema standards}

### 8.3 Data Quality & Validation
{Quality rules, reconciliation checks, completeness gates}

### 8.4 Data Masking & Anonymization
{Sensitive data handling, masking rules per environment}

See: `diagrams/data-integration-view.md`

## 9. NFR Alignment Note
### 9.1 Performance & Scalability
{Query latency targets, throughput, read/write scaling}

### 9.2 Availability & Consistency
{Consistency model (strong/eventual), replication, failover}

### 9.3 Data Freshness & Completeness
{SLO/SLI targets for data freshness, completeness, accuracy}

### 9.4 Constraints & Assumptions
{Data architecture constraints, technology limitations, key assumptions}

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
- A: Full storage technology comparison
- B: Research references
- C: Stakeholder input summary
- D: Alternative data architectures considered
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

### Template: Data Integration View (OUT-17)

```markdown
# Data Integration View -- Data Architecture

## Generated: {timestamp}

## 1. Data Exchange Protocols

| Interface | Protocol | Pattern | Description |
|:---|:---|:---|:---|
| {interface_name} | CDC / Batch / Streaming / REST API | Real-time / Near-real-time / Batch | {description} |

## 2. Schema Contracts

| Contract ID | Producer | Consumer | Format | Schema Location |
|:---|:---|:---|:---|:---|
| {contract_id} | {producer_system} | {consumer_system} | Avro / Parquet / JSON Schema | {schema_path_or_url} |

## 2.1 Schema Versioning & Evolution
- Schema compatibility mode (backward/forward/full)
- Schema registry configuration
- Breaking change notification process

## 3. Data Quality & Validation

| Rule ID | Scope | Rule | Threshold | Action on Failure |
|:---|:---|:---|:---|:---|
| DQ-001 | {pipeline/table} | {completeness/accuracy/freshness} | {threshold} | {alert/reject/quarantine} |

## 3.1 Data Masking & Anonymization
- Sensitive data classification per domain
- Masking rules per environment (dev/staging/prod)
- Anonymization approach for analytics/ML pipelines

## 4. Data Flow Diagram

\`\`\`mermaid
{data flow diagram source}
\`\`\`
```

### Template: NFR Alignment Note (OUT-18)

```markdown
# NFR Alignment Note -- Data Architecture

## Generated: {timestamp}

## NFR-to-Data-Architecture Mapping

| NFR Category | NFR Requirement | Architecture Decision | How Addressed |
|:---|:---|:---|:---|
| Performance | {nfr_requirement} | {decision} | {explanation} |
| Availability | {nfr_requirement} | {decision} | {explanation} |
| Consistency | {nfr_requirement} | {decision} | {explanation} |
| Scalability | {nfr_requirement} | {decision} | {explanation} |
| Data Freshness | {nfr_requirement} | {decision} | {explanation} |

## Data SLO/SLI Targets

| Metric | SLI Definition | SLO Target | Alert Threshold |
|:---|:---|:---|:---|
| Query latency (p99) | {definition} | {target} | {threshold} |
| Data freshness | {definition} | {target} | {threshold} |
| Completeness | {definition} | {target} | {threshold} |

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
# Phase {N} Question List -- Data Architecture

## Phase: {phase_name}
## Generated: {timestamp}

| Q# | Question | Category | Status | Answer Summary |
|:---|:---|:---|:---|:---|
| Q{N}-001 | {question_text} | {category} | Asked / Answered / Skipped | {summary} |
```
