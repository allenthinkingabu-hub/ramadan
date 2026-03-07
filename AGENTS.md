# AGENTS.md -- OpenClaw Team Configuration

## Agent Registry

| Agent | Role | Type | Description |
|:---|:---|:---|:---|
| PM Agent | Project Manager | Orchestrator | Sole orchestrator; broadcasts tasks, collects completions, re-broadcasts for supervisor QA |
| SA Agent | IT Architect | Role Agent | Executes system architecture tasks across Inception, Requirements, Development, QA, Release phases |
| IPM Agent | IT Product Manager | Role Agent | Manages product requirements, BRDs, PRDs, and product lifecycle across Inception, Requirements, Development, QA, Release phases |
| TL Agent | Technical Lead | Role Agent | Executes technical leadership tasks across Inception, Requirements, Development, QA, Release phases |

## Event Protocol

PM is the only orchestrator. SA and TL run symmetrical flows.

### Event Types

| Event | Direction | Payload |
|:---|:---|:---|
| `TaskTriggered` | PM -> Role Agent | `{ task_id, skill_dir, inputs, context }` |
| `TaskCompleted` | Role Agent -> PM | `{ task_id, status, artifacts, supervisor_report }` |
| `SupervisorTriggered` | Role Agent -> Supervisor | `{ task_id, output_dir }` |
| `SupervisorCompleted` | Supervisor -> Role Agent | `{ task_id, pass_rate, report, remediation_items }` |

### Role Agent Flow (SA and TL -- symmetrical)

```
PM broadcasts TaskTriggered { task_id, skill_dir }
     |
     v
Role Agent receives event
     |
     v
[1] Check DoR (Definition of Ready)
     |-- FAIL -> request missing inputs from PM
     |-- PASS -> proceed
     v
[2] Execute Skill (Phase 0-5)
     |-- Phase 0: Initialization (create output dir, init logs)
     |-- Phase 1: Understand Task Purpose (dialogue)
     |-- Phase 2: Understand the Topic (gather context)
     |-- Phase 3: Research & Question Generation (iterative Q&A)
     |-- Phase 4: Execute & Produce Deliverables (core work + DoD self-verify)
     |-- Phase 5: Completion & Handoff
     v
[3] Self-Check (verify DoD items 1-19)
     |-- auto-remediate any failures
     v
[4] Invoke Supervisor
     |-- Supervisor inspects all checklist items
     |-- FAIL -> return report; agent remediates; re-invoke supervisor
     |-- PASS (100%) -> proceed
     v
[5] Report to PM
     |-- send TaskCompleted { task_id, status: "DONE", artifacts, supervisor_report }
     v
PM re-broadcasts for downstream tasks (parallel fan-out per delivery_playbook.md)
```

### PM Orchestration Flow

```
PM selects next task(s) from tasks-index.json
     |
     v
PM broadcasts TaskTriggered to target role agent(s)
     |-- multiple tasks in same wave -> parallel fan-out
     |-- tasks across waves -> sequential (complete Wave N before N+1)
     v
PM waits for TaskCompleted from all triggered tasks
     |
     v
PM validates supervisor_report.pass_rate == 100%
     |-- FAIL -> re-trigger task with remediation context
     |-- PASS -> mark task done in state.json
     v
PM triggers downstream tasks (Next column from delivery_playbook.md)
```

### State Management

- **Task index**: `{role}-agent/config/tasks-index.json` -- maps task_id to skill_dir, wave, step, next
- **State file**: `{role}-agent/config/state.json` -- tracks task status for idempotence
- **Output root**: `{role}-agent/outputs/{task_id}/` -- all deliverables per task execution

### Idempotence Rules

1. Before executing a task, check `state.json` for existing status
2. If `status == "DONE"` and `supervisor_pass_rate == 100%`, skip (already complete)
3. If `status == "IN_PROGRESS"`, resume from last checkpoint
4. If `status == "FAILED"`, re-execute with remediation context
5. Log all state transitions in work log

### Mandatory Execution Rule

Every AI Agent must execute tasks strictly according to its corresponding skill instructions. All phases, DoR prerequisites, and DoD quality gates must be honored. No phase may be skipped. The supervisor must achieve 100% pass rate before the task is marked complete.
