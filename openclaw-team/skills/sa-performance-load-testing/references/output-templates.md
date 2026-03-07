# Output Content List & Templates -- sa-performance-load-testing

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
| OUT-13 | Performance Load Testing Report | `performance-load-testing-report.md` | Markdown |
| OUT-14 | Phase Question Lists | `phase{N}-questions.md` | Markdown |
| OUT-15 | Research Artifacts | `research/` | Mixed |
| OUT-16 | Test Scenarios | `scenarios/` | Markdown |
| OUT-17 | Benchmark Definitions | `scenarios/benchmarks.md` | Markdown |
| OUT-18 | Test Execution Plan | `test-execution-plan.md` | Markdown |
| OUT-19 | Acceptance Criteria Matrix | `acceptance-criteria.md` | Markdown |

All paths are relative to the `performance-load-testing/` output directory.

---

## Templates

### Template: YAML Config File (OUT-01 through OUT-10)

```yaml
# {Config Name} -- sa-performance-load-testing Agent
# Task: IA-QA-001 Performance & Load Testing
# Generated: {timestamp}
# Modifiable: Yes

metadata:
  task_id: "IA-QA-001"
  task_name: "Performance & Load Testing"
  role: "System Architect (SA)"
  generated_at: "{timestamp}"

items:
  - id: "{PREFIX}-001"
    name: "{item_name}"
    description: "{item_description}"
```

### Template: Conversation Log (OUT-11)

```markdown
# Conversation Log -- Performance & Load Testing (IA-QA-001)

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
# Work Log -- Performance & Load Testing (IA-QA-001)

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

### Template: Performance Load Testing Report (OUT-13)

```markdown
# Performance & Load Testing Report

## 1. Executive Summary
{One-paragraph overview of performance testing strategy and key NFR targets}

## 2. Test Scope & Objectives
- **Purpose**: {why performance testing is needed}
- **Scope**: {systems, services, and endpoints under test}
- **NFR Targets**: {key latency, throughput, concurrency goals}
- **Upstream References**: {links to Architecture Design, NFR mapping}

## 3. Workload Model
### 3.1 User Profiles
{Description of user types, behavior patterns, and concurrency levels}

### 3.2 Transaction Mix
{Weighted distribution of transactions/API calls}

### 3.3 Data Volume
{Test data requirements, seeding strategy}

## 4. Test Scenarios
### 4.1 Load Test
{Steady-state simulation parameters and expected outcomes}

### 4.2 Stress Test
{Beyond-capacity parameters and failure thresholds}

### 4.3 Soak Test
{Extended duration parameters and stability criteria}

### 4.4 Spike Test
{Sudden burst parameters and recovery expectations}

### 4.5 Scalability Test
{Scaling trigger points and resource elasticity validation}

## 5. Benchmark Definitions
| Metric | Target | Threshold | Measurement Point |
|:---|:---|:---|:---|
| Latency p50 | {target} | {threshold} | {endpoint} |
| Latency p95 | {target} | {threshold} | {endpoint} |
| Latency p99 | {target} | {threshold} | {endpoint} |
| Throughput (TPS) | {target} | {threshold} | {service} |
| Concurrency | {target} | {threshold} | {system} |
| Error Rate | {target} | {threshold} | {scope} |
| CPU Utilization | {target} | {threshold} | {resource} |
| Memory Utilization | {target} | {threshold} | {resource} |

## 6. Test Environment
- **Infrastructure**: {environment specs matching production topology}
- **Data**: {test data strategy}
- **Tools**: {selected performance testing tools}
- **Monitoring**: {APM, metrics, log aggregation setup}

## 7. Execution Plan
| Phase | Duration | Objective | Success Criteria |
|:---|:---|:---|:---|
| Baseline | {duration} | Establish baseline metrics | {criteria} |
| Load | {duration} | Validate NFR targets | {criteria} |
| Stress | {duration} | Find breaking point | {criteria} |
| Soak | {duration} | Validate stability | {criteria} |

## 8. Acceptance Criteria
| NFR Requirement | Test Scenario | Pass Criteria | Fail Action |
|:---|:---|:---|:---|
| {nfr} | {scenario} | {criteria} | {action} |

## 9. Risks & Mitigations
| Risk | Impact | Probability | Mitigation |
|:---|:---|:---|:---|
| {risk} | High/Med/Low | High/Med/Low | {mitigation} |

## 10. Appendices
- A: Detailed test scripts and configurations
- B: Tool configuration templates
- C: Historical performance baselines
- D: NFR traceability matrix
```

### Template: Phase Question List (OUT-14)

```markdown
# Phase {N} Question List -- Performance & Load Testing

## Phase: {phase_name}
## Generated: {timestamp}

| Q# | Question | Category | Status | Answer Summary |
|:---|:---|:---|:---|:---|
| Q{N}-001 | {question_text} | {category} | Asked / Answered / Skipped | {summary} |
```
