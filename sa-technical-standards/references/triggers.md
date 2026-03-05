# Trigger Mechanisms Configuration -- sa-technical-standards

## Trigger Events

| Trigger ID | Event | Source | Condition |
|:---|:---|:---|:---|
| TRG-001 | User invokes skill directly | User | User requests technical standards or coding guidelines |
| TRG-002 | PM Agent assigns task | PM Agent | IA-REQ-005 task assigned via RACI matrix |
| TRG-003 | Wave 9 completion | Solutions Architect | All SA-REQ-001..005 outputs available (SAD, Integration Architecture, NFR Mapping, Technology Blueprint, ARB Feedback) |
| TRG-004 | Post-architecture-design | SA Agent | Architecture Design (IA-REQ-001) completed, standards needed |
| TRG-005 | Standards review request | Stakeholder | Request to create or update technical standards |

## Delivery Playbook Context

- **Wave**: 10 | **Step**: 5
- **Upstream (Wave 9)**: SA-REQ-001 (SAD), SA-REQ-002 (Integration Architecture), SA-REQ-003 (NFR Mapping), SA-REQ-004 (Technology Blueprint), SA-REQ-005 (ARB Feedback)
- **Downstream (Wave 11)**: TL-REQ-001..005 (Technical Lead tasks)

## Trigger Keywords

The agent activates when the user's request matches these contexts:
- "technical standards"
- "coding standards"
- "coding guidelines"
- "design patterns"
- "architectural guidelines"
- "code quality"
- "code review standards"
- "naming conventions"
- "error handling standards"
- "logging standards"

## Activation Parameters

| Parameter | Required | Description |
|:---|:---|:---|
| topic | Yes | The project or technology stack to define standards for |
| scope | No | Specific standards aspects to focus on (default: full standards) |
| output_dir | No | Directory for outputs (default: `./technical-standards/`) |
| technical_discovery_ref | No | Path to Technical Discovery report (IA-INC-001) |
| feasibility_analysis_ref | No | Path to Feasibility Analysis report (IA-INC-002) |
