# Trigger Configuration — PM-REQ-005 Vendor & Procurement Management

## Primary Triggers (any one activates)

| ID | Type | Description |
|----|------|-------------|
| T-001 | TaskTriggered event | PM dispatches PM-REQ-005 via event bus |
| T-002 | Upstream completion | Upstream prerequisite tasks completed |
| T-003 | User invocation | User explicitly requests vendor & procurement management for the project |

## Context Conditions (must be satisfied)

| ID | Description | Required |
|----|-------------|----------|
| C-001 | Task context or business problem is provided | Yes |
| C-002 | DoR prerequisites available or can be gathered interactively | Yes |
| C-003 | Upstream artifacts accessible | Yes |

## Output Signals (emitted on completion)

| ID | Target | Signal | Description |
|----|--------|--------|-------------|
| S-001 | pm-vendor-procurement-management-supervisor | SupervisorTriggered | Triggers supervisor review of output |
| S-002 | PM Agent | TaskCompleted | Notifies PM that Vendor & Procurement Management is finalized (after supervisor approval) |

### S-002 Payload
- `deliverable_path`: Path to the final deliverable
- `raci_matrix`: RACI configuration for downstream task activation
- `final_inspection_report`: Supervisor inspection results
