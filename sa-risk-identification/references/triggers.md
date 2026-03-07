# Trigger Mechanisms Configuration -- sa-risk-identification

## Trigger Events

| Trigger ID | Event | Source | Condition |
|:---|:---|:---|:---|
| TRG-001 | User invokes skill directly | User | User requests technical risk identification or risk assessment |
| TRG-002 | PM Agent assigns task | PM Agent | IA-INC-004 task assigned via RACI matrix |
| TRG-003 | Wave 9 completion | Solutions Architect | All SA-REQ-001..005 outputs available (SAD, Integration Architecture, NFR Mapping, Technology Blueprint, ARB Feedback) |
| TRG-004 | Post-architecture-design | SA Agent | Architecture Design (IA-INC-003) completed, risk identification needed |
| TRG-005 | Risk assessment request | Stakeholder | Request to identify technical risks and dependencies |

## Delivery Playbook Context

- **Wave**: 10 | **Step**: 4
- **Upstream (Wave 9)**: SA-REQ-001 (SAD), SA-REQ-002 (Integration Architecture), SA-REQ-003 (NFR Mapping), SA-REQ-004 (Technology Blueprint), SA-REQ-005 (ARB Feedback)
- **Downstream (Wave 11)**: TL-INC-001..005 (Technical Lead tasks)

## Trigger Keywords

The agent activates when the user's request matches these contexts:
- "risk identification"
- "technical risk"
- "risk assessment"
- "dependency analysis"
- "integration challenges"
- "risk register"
- "dependency mapping"
- "risk mitigation"
- "technical risks"
- "system dependencies"

## Activation Parameters

| Parameter | Required | Description |
|:---|:---|:---|
| topic | Yes | The project or system to assess for technical risks |
| scope | No | Specific risk areas to focus on (default: comprehensive assessment) |
| output_dir | No | Directory for outputs (default: `./risk-identification/`) |
| technical_discovery_ref | No | Path to Technical Discovery report (IA-INC-001) |
| feasibility_analysis_ref | No | Path to Feasibility Analysis report (IA-INC-002) |
