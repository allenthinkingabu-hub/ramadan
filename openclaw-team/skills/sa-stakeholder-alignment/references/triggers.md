# Trigger Mechanisms Configuration -- sa-stakeholder-alignment

## Trigger Events

| Trigger ID | Event | Source | Condition |
|:---|:---|:---|:---|
| TRG-001 | User invokes skill directly | User | User requests stakeholder alignment or architecture workshop |
| TRG-002 | PM Agent assigns task | PM Agent | IA-INC-006 task assigned via RACI matrix |
| TRG-003 | Wave 9 completion | Solutions Architect | All SA-REQ-001..005 outputs available (SAD, Integration Architecture, NFR Mapping, Technology Blueprint, ARB Feedback) |
| TRG-004 | Post-cost-estimation | SA Agent | Cost Estimation (IA-INC-005) completed, stakeholder alignment needed |
| TRG-005 | Stakeholder conflict escalation | Stakeholder | Conflicting priorities require structured alignment workshop |

## Delivery Playbook Context

- **Wave**: 10 | **Step**: 6
- **Upstream (Wave 9)**: SA-REQ-001 (SAD), SA-REQ-002 (Integration Architecture), SA-REQ-003 (NFR Mapping), SA-REQ-004 (Technology Blueprint), SA-REQ-005 (ARB Feedback)
- **Downstream (Wave 11)**: TL-INC-001..005 (Technical Lead tasks)

## Trigger Keywords

The agent activates when the user's request matches these contexts:
- "stakeholder alignment"
- "architecture workshop"
- "stakeholder workshop"
- "cross-functional alignment"
- "decision criteria"
- "scope alignment"
- "risk alignment"
- "consensus building"
- "stakeholder mapping"
- "priority alignment"

## Activation Parameters

| Parameter | Required | Description |
|:---|:---|:---|
| topic | Yes | The project or system requiring stakeholder alignment |
| scope | No | Specific alignment areas to focus on (default: comprehensive alignment) |
| output_dir | No | Directory for outputs (default: `./stakeholder-alignment/`) |
| technical_discovery_ref | No | Path to Technical Discovery report (IA-INC-001) |
| feasibility_analysis_ref | No | Path to Feasibility Analysis report (IA-INC-002) |
