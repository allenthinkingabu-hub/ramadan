# Integration Design Agent — Trigger Mechanism Configuration

## Trigger Conditions

| Trigger ID | Trigger Type | Condition | Description |
| :--- | :--- | :--- | :--- |
| TRG-001 | Manual | User invokes SA-integration-design skill | User explicitly requests integration design |
| TRG-002 | Upstream Task | Architecture Design (IA-REQ-001) completed | Architecture design output is ready as input |
| TRG-003 | Upstream Task | Technology Stack Decision (IA-REQ-002) completed | Technology stack decisions are finalized |
| TRG-004 | PM Dispatch | PM Agent assigns IA-REQ-003 | Project Manager AI Agent dispatches this task |
| TRG-005 | RACI Trigger | Downstream RACI dependency met | All prerequisite RACI tasks are completed |

## Trigger Parameters

| Parameter | Required | Description |
| :--- | :--- | :--- |
| project_name | Yes | Name of the project or system |
| architecture_doc_path | Yes | Path to the architecture design document |
| tech_stack_doc_path | Yes | Path to the technology stack decision document |
| existing_system_inventory | No | Path to existing system landscape documentation |
| api_standards_doc | No | Path to API standards/guidelines |
| security_requirements_doc | No | Path to security requirements |

## Configuration Notes

- This file supports future modifications; add new triggers by appending rows to the Trigger Conditions table.
- Trigger parameters can be extended as project requirements evolve.
