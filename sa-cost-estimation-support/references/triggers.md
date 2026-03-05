# Trigger Mechanisms Configuration -- sa-cost-estimation-support

## Trigger Events

| Trigger ID | Event | Source | Condition |
|:---|:---|:---|:---|
| TRG-001 | User invokes skill directly | User | User requests cost estimation or budget analysis |
| TRG-002 | PM Agent assigns task | PM Agent | IA-INC-005 task assigned via RACI matrix |
| TRG-003 | Wave 9 completion | Solutions Architect | All SA-REQ-001..005 outputs available (SAD, Integration Architecture, NFR Mapping, Technology Blueprint, ARB Feedback) |
| TRG-004 | Post-risk-identification | SA Agent | Risk Identification (IA-INC-004) completed, cost estimation needed |
| TRG-005 | Budget estimation request | Stakeholder | Request for ROM cost estimates for proposed architecture |

## Delivery Playbook Context

- **Wave**: 10 | **Step**: 5
- **Upstream (Wave 9)**: SA-REQ-001 (SAD), SA-REQ-002 (Integration Architecture), SA-REQ-003 (NFR Mapping), SA-REQ-004 (Technology Blueprint), SA-REQ-005 (ARB Feedback)
- **Downstream (Wave 11)**: TL-INC-001..005 (Technical Lead tasks)

## Trigger Keywords

The agent activates when the user's request matches these contexts:
- "cost estimation"
- "ROM estimate"
- "rough order of magnitude"
- "infrastructure cost"
- "licensing cost"
- "development effort"
- "TCO analysis"
- "total cost of ownership"
- "budget estimate"
- "FinOps"

## Activation Parameters

| Parameter | Required | Description |
|:---|:---|:---|
| topic | Yes | The project or system to estimate costs for |
| scope | No | Specific cost areas to focus on (default: comprehensive estimation) |
| output_dir | No | Directory for outputs (default: `./cost-estimation/`) |
| technical_discovery_ref | No | Path to Technical Discovery report (IA-INC-001) |
| feasibility_analysis_ref | No | Path to Feasibility Analysis report (IA-INC-002) |
