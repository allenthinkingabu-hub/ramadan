# Trigger Configuration — IA-REL-005 Architecture Evolution

## Primary Triggers (any one activates)

| ID | Type | Description |
|----|------|-------------|
| T-001 | TaskTriggered event | PM dispatches IA-REL-005 via event bus |
| T-002 | Upstream completion | Upstream prerequisite tasks completed |
| T-003 | User invocation | User explicitly requests architecture evolution for the project |

## Context Conditions (must be satisfied)

| ID | Description | Required |
|----|-------------|----------|
| C-001 | Task context or business problem is provided | Yes |
| C-002 | DoR prerequisites available or can be gathered interactively | Yes |
| C-003 | Upstream artifacts accessible | Yes |

## Output Signals (emitted on completion)

| ID | Target | Signal | Description |
|----|--------|--------|-------------|
| S-001 | sa-architecture-evolution-supervisor | SupervisorTriggered | Triggers supervisor review of output |
| S-002 | PM Agent | TaskCompleted | Notifies PM that Architecture Evolution is finalized (after supervisor approval) |

### S-002 Payload
- `deliverable_path`: Path to the final deliverable
- `raci_matrix`: RACI configuration for downstream task activation
- `final_inspection_report`: Supervisor inspection results
