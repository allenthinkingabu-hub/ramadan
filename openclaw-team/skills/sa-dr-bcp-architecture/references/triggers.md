# Trigger Mechanisms Configuration -- sa-dr-bcp-architecture

## Trigger Events

| Trigger ID | Event | Source | Condition |
|:---|:---|:---|:---|
| TRG-001 | User invokes skill directly | User | User requests DR/BCP architecture or disaster recovery design |
| TRG-002 | PM Agent assigns task | PM Agent | IA-REQ-007 task assigned via RACI matrix |
| TRG-003 | Wave 9 completion | Solutions Architect | All SA-REQ-001..005 outputs available (SAD, Integration Architecture, NFR Mapping, Technology Blueprint, ARB Feedback) |
| TRG-004 | Post-architecture-design | SA Agent | Architecture Design (IA-REQ-001) completed, DR/BCP needed |
| TRG-005 | DR/BCP review request | Stakeholder | Request to create or update DR/BCP architecture |

## Delivery Playbook Context

- **Wave**: 10 | **Step**: 7
- **Upstream (Wave 9)**: SA-REQ-001 (SAD), SA-REQ-002 (Integration Architecture), SA-REQ-003 (NFR Mapping), SA-REQ-004 (Technology Blueprint), SA-REQ-005 (ARB Feedback)
- **Downstream (Wave 11)**: TL-REQ-001..005 (Technical Lead tasks)

## Trigger Keywords

The agent activates when the user's request matches these contexts:
- "disaster recovery"
- "business continuity"
- "DR/BCP"
- "failover"
- "RPO/RTO"
- "backup strategy"
- "recovery architecture"
- "resilience architecture"
- "chaos testing"
- "DR testing"

## Activation Parameters

| Parameter | Required | Description |
|:---|:---|:---|
| topic | Yes | The project or system to design DR/BCP architecture for |
| scope | No | Specific DR/BCP aspects to focus on (default: full design) |
| output_dir | No | Directory for outputs (default: `./dr-bcp-architecture/`) |
| technical_discovery_ref | No | Path to Technical Discovery report (IA-INC-001) |
| feasibility_analysis_ref | No | Path to Feasibility Analysis report (IA-INC-002) |
