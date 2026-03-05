---
name: sa-performance-load-testing
description: "Interactive AI Agent skill for defining test scenarios and benchmarks for NFR validation (latency, throughput, concurrency). Use when: (1) performance or load testing planning is needed, (2) defining latency, throughput, or concurrency benchmarks, (3) creating NFR validation test scenarios, (4) PM Agent assigns task IA-QA-001 via RACI matrix, (5) translating architecture NFRs into executable performance test plans, (6) establishing baseline metrics and acceptance thresholds, or (7) designing stress, soak, and spike test strategies."
---

# SA Performance & Load Testing Agent

Role: IT Architect (SA) | Task ID: IA-QA-001 | Wave: 10, Step: 1

## Objective

Define comprehensive performance and load test scenarios, establish benchmarks, and validate non-functional requirements (latency, throughput, concurrency) against architecture specifications.

## Upstream Inputs

- Architecture Design outputs (IA-REQ-001)
- Non-Functional Requirements mapping
- Infrastructure specifications
- Deployment architecture documentation
- Capacity planning estimates

## Downstream Triggers (Technical Lead)

Upon completion, PM Agent triggers: TL-QA-001 (Critical Bug Investigation), TL-QA-002 (Performance & Scalability Review), TL-QA-003 (Release Candidate Validation), TL-QA-004 (Technical Go/No-Go Input).

## Workflow Overview

Create performance test plans through an interactive, phased process:

```
Phase 0: Initialization
  -> Verify DoR, create output directory, init logs
Phase 1: Understand Task Purpose (Step 1)
  -> Present understanding of why performance testing is needed -> user confirms
Phase 2: Understand the Topic (Step 2)
  -> Understand NFRs, architecture constraints, SLA targets, workload profiles -> user confirms
Phase 3: Research & Question Generation (Step 3)
  -> Industry research -> generate question list -> iterative dialogue -> validated requirements
Phase 4: Execute & Produce Deliverables (Step 4)
  -> Design test scenarios -> produce benchmarks, test plans, acceptance criteria -> DoD self-verify
Phase 5: Completion & Handoff
  -> Trigger Supervisor -> remediate if needed -> notify PM Agent -> trigger TL-QA-001..004
```

## Phase 0: Initialization

1. Check DoR prerequisites -- see [references/dor.md](references/dor.md)
2. Create `performance-load-testing/` directory under parent directory
3. Create subdirectories: `config/`, `templates/`, `research/`, `scenarios/`
4. Initialize `performance-load-testing/conversation-log.md` using template from [references/output-templates.md](references/output-templates.md)
5. Initialize `performance-load-testing/work-log.md` using template from [references/output-templates.md](references/output-templates.md)
6. Log activation in work log

## Phase 1: Understand Task Purpose

1. Analyze why performance and load testing is needed for this context
2. Formulate understanding of: goals, scope, NFR targets, test types required
3. Present structured understanding to user, ask for confirmation
4. If rejected -> refine and repeat. If confirmed -> log and proceed
5. Record all questions in `performance-load-testing/phase1-questions.md`

## Phase 2: Understand the Topic

1. Gather upstream inputs:
   - Architecture design documents and NFR mapping
   - SLA/SLO targets (latency, throughput, availability)
   - Deployment topology and infrastructure specs
   - Expected workload profiles and user concurrency
   - Integration points and external dependency SLAs
2. Gather additional context:
   - Business-critical user journeys
   - Peak load expectations and seasonal patterns
   - Historical performance data (if available)
   - Technology stack performance characteristics
3. Present structured understanding to user, ask for confirmation
4. If rejected -> return to Phase 1. If confirmed -> log and proceed
5. Record all questions in `performance-load-testing/phase2-questions.md`

## Phase 3: Research & Question Generation

1. Research industry performance testing practices for this topic
   - Save all research to `performance-load-testing/research/`
2. Generate comprehensive question list -> save to `performance-load-testing/phase3-questions.md`
3. Iterative dialogue with user through the question list
4. Produce validated requirements list -> save to `performance-load-testing/validated-requirements.md`

## Phase 4: Execute & Produce Deliverables

1. Conduct research based on validated requirements
2. Design performance test scenarios:
   - **Load Tests**: Steady-state concurrent user simulation
   - **Stress Tests**: Beyond-capacity threshold testing
   - **Soak Tests**: Extended duration stability testing
   - **Spike Tests**: Sudden traffic burst handling
   - **Scalability Tests**: Horizontal/vertical scaling validation
3. Produce **Benchmark Definitions**:
   - Latency targets (p50, p95, p99) per endpoint/transaction
   - Throughput targets (TPS/RPS) per service
   - Concurrency targets (max concurrent users/connections)
   - Resource utilization thresholds (CPU, memory, disk I/O, network)
   - Save to `performance-load-testing/scenarios/benchmarks.md`
4. Produce **Test Execution Plan**:
   - Test environment requirements
   - Data preparation and seeding strategy
   - Test tool selection and configuration
   - Execution schedule and dependencies
   - Save to `performance-load-testing/test-execution-plan.md`
5. Produce **Acceptance Criteria Matrix**:
   - NFR-to-test mapping with pass/fail thresholds
   - Save to `performance-load-testing/acceptance-criteria.md`
6. Generate all configuration files (OUT-01 through OUT-10) -- see [references/output-templates.md](references/output-templates.md)
7. Generate Performance Load Testing report using report template
8. Run DoD self-verification with `scripts/verify_dod.py` -- see [references/dod.md](references/dod.md)
9. If any item fails -> fix and re-verify until all pass

## Phase 5: Completion & Handoff

1. Trigger `sa-performance-load-testing-supervisor` skill for inspection
2. If inspection returns failures -> remediate item-by-item, re-trigger supervisor
3. Once 100% pass -> notify PM Agent with:
   - Performance Load Testing report path
   - RACI matrix (see [references/raci.md](references/raci.md))
   - Final inspection report
4. PM Agent uses RACI matrix to trigger downstream Technical Lead tasks:
   - TL-QA-001: Critical Bug Investigation
   - TL-QA-002: Performance & Scalability Review
   - TL-QA-003: Release Candidate Validation
   - TL-QA-004: Technical Go/No-Go Input

## Logging Requirements

- **Conversation log**: Record every user interaction question-by-question in `conversation-log.md`
- **Work log**: Record every action entry-by-entry on timeline in `work-log.md`
- **Phase questions**: Save question lists from each phase in `phase{N}-questions.md`
- **Research artifacts**: Save all research process and results in `research/`

## Reference Files

- **Trigger mechanisms**: [references/triggers.md](references/triggers.md)
- **RACI matrix**: [references/raci.md](references/raci.md)
- **Skills & knowledge**: [references/skills-and-knowledge.md](references/skills-and-knowledge.md)
- **Tools & MCP tools**: [references/tools.md](references/tools.md)
- **SOP process**: [references/sop.md](references/sop.md)
- **DoD checklist**: [references/dod.md](references/dod.md)
- **DoR checklist**: [references/dor.md](references/dor.md)
- **Output templates**: [references/output-templates.md](references/output-templates.md)
