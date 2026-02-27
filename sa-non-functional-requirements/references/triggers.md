# Trigger Mechanisms Configuration — sa-non-functional-requirements

## Trigger Events

| Trigger ID | Event | Source | Condition |
|:---|:---|:---|:---|
| TRG-001 | User invokes skill directly | User | User requests NFR definition or quality attribute specification |
| TRG-002 | PM Agent assigns task | PM Agent | IA-REQ-002 task assigned via RACI matrix |
| TRG-003 | Post-architecture-design | SA Agent | Architecture Design (IA-REQ-001) completed, NFR definition needed |
| TRG-004 | Quality attribute review request | Stakeholder | Request to define or update non-functional requirements |

## Trigger Keywords

The agent activates when the user's request matches these contexts:
- "non-functional requirements"
- "NFR"
- "performance requirements"
- "scalability requirements"
- "SLA definition"
- "quality attributes"
- "availability targets"
- "security requirements"
- "SLO targets"
- "SLI metrics"

## Activation Parameters

| Parameter | Required | Description |
|:---|:---|:---|
| topic | Yes | The project or system to define non-functional requirements for |
| scope | No | Specific NFR categories to focus on (default: all categories) |
| output_dir | No | Directory for outputs (default: `./non-functional-requirements/`) |
| architecture_design_ref | No | Path to Architecture Design report (IA-REQ-001) |
| technical_discovery_ref | No | Path to Technical Discovery report (IA-INC-001) |
