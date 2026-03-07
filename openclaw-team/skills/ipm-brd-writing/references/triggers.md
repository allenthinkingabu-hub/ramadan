# Trigger Configuration — IPM-INC-003 BRD Writing

## Primary Triggers (any one activates)

| ID | Type | Description |
|----|------|-------------|
| T-001 | TaskTriggered event | PM dispatches IPM-INC-003 via event bus |
| T-002 | Upstream completion | IPM-INC-001 (Requirement Gathering) AND IPM-INC-002 (Market Research) both completed |
| T-003 | User invocation | User explicitly requests BRD creation for the project |

## Context Conditions (must be satisfied)

| ID | Description | Required |
|----|-------------|----------|
| C-001 | A topic or business problem is provided | Yes |
| C-002 | DoR prerequisites available or can be gathered interactively | Yes |
| C-003 | Upstream artifacts from IPM-INC-001 and IPM-INC-002 accessible | Yes |

## Output Signals (emitted on completion)

| ID | Target | Signal | Description |
|----|--------|--------|-------------|
| S-001 | ipm-brd-writing-supervisor | SupervisorTriggered | Triggers supervisor review of BRD output |
| S-002 | PM Agent | TaskCompleted | Notifies PM that BRD is finalized (after supervisor approval) |

### S-002 Payload
- `brd_file_path`: Path to the final BRD document
- `raci_matrix`: RACI configuration for downstream SM task activation
- `final_inspection_report`: Supervisor inspection results
