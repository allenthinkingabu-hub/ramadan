# Trigger Mechanisms Configuration -- sa-data-privacy-governance

## Trigger Events

| Trigger ID | Event | Source | Condition |
|:---|:---|:---|:---|
| TRG-001 | User invokes skill directly | User | User requests data privacy governance or data classification |
| TRG-002 | PM Agent assigns task | PM Agent | IA-REQ-006 task assigned via RACI matrix |
| TRG-003 | Wave 9 completion | Solutions Architect | All SA-REQ-001..005 outputs available (SAD, Integration Architecture, NFR Mapping, Technology Blueprint, ARB Feedback) |
| TRG-004 | Post-architecture-design | SA Agent | Architecture Design (IA-REQ-001) completed, governance needed |
| TRG-005 | Privacy governance review request | Stakeholder | Request to create or update data privacy governance |

## Delivery Playbook Context

- **Wave**: 10 | **Step**: 6
- **Upstream (Wave 9)**: SA-REQ-001 (SAD), SA-REQ-002 (Integration Architecture), SA-REQ-003 (NFR Mapping), SA-REQ-004 (Technology Blueprint), SA-REQ-005 (ARB Feedback)
- **Downstream (Wave 11)**: TL-REQ-001..005 (Technical Lead tasks)

## Trigger Keywords

The agent activates when the user's request matches these contexts:
- "data privacy"
- "data governance"
- "data classification"
- "data retention"
- "data residency"
- "access control model"
- "GDPR compliance"
- "privacy framework"
- "consent management"
- "data protection"

## Activation Parameters

| Parameter | Required | Description |
|:---|:---|:---|
| topic | Yes | The project or system to define data privacy governance for |
| scope | No | Specific governance aspects to focus on (default: full framework) |
| output_dir | No | Directory for outputs (default: `./data-privacy-governance/`) |
| technical_discovery_ref | No | Path to Technical Discovery report (IA-INC-001) |
| feasibility_analysis_ref | No | Path to Feasibility Analysis report (IA-INC-002) |
