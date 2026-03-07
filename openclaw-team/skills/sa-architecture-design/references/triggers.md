# Trigger Mechanisms Configuration — sa-architecture-design

## Trigger Events

| Trigger ID | Event | Source | Condition |
|:---|:---|:---|:---|
| TRG-001 | User invokes skill directly | User | User requests architecture design or system design |
| TRG-002 | PM Agent assigns task | PM Agent | IA-REQ-001 task assigned via RACI matrix |
| TRG-003 | Wave 9 completion | Solutions Architect | All SA-REQ-001..005 outputs available (SAD, Integration Architecture, NFR Mapping, Technology Blueprint, ARB Feedback) |
| TRG-004 | Post-feasibility-analysis | SA Agent | Feasibility Analysis (IA-INC-002) completed, architecture design needed |
| TRG-005 | Architecture review request | Stakeholder | Request to create or update system architecture |

## Delivery Playbook Context

- **Wave**: 10 | **Step**: 1
- **Upstream (Wave 9)**: SA-REQ-001 (SAD), SA-REQ-002 (Integration Architecture), SA-REQ-003 (NFR Mapping), SA-REQ-004 (Technology Blueprint), SA-REQ-005 (ARB Feedback)
- **Downstream (Wave 11)**: TL-REQ-001..005 (Technical Lead tasks)

## Trigger Keywords

The agent activates when the user's request matches these contexts:
- "architecture design"
- "system design"
- "C4 diagram"
- "UML diagram"
- "sequence diagram"
- "component diagram"
- "deployment architecture"
- "system architecture"
- "high-level design"
- "detailed design"

## Activation Parameters

| Parameter | Required | Description |
|:---|:---|:---|
| topic | Yes | The project or system to design architecture for |
| scope | No | Specific architecture aspects to focus on (default: full design) |
| output_dir | No | Directory for outputs (default: `./architecture-design/`) |
| technical_discovery_ref | No | Path to Technical Discovery report (IA-INC-001) |
| feasibility_analysis_ref | No | Path to Feasibility Analysis report (IA-INC-002) |
