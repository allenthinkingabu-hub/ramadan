# Trigger Mechanisms Configuration — tl-technical-risk-assessment

## Trigger Events

| Trigger ID | Event | Source | Condition |
|:---|:---|:---|:---|
| TRG-001 | User invokes skill directly | User | User requests technical risk assessment or dependency analysis |
| TRG-002 | PM Agent assigns task | PM Agent | TL-INC-004 task assigned via RACI matrix |
| TRG-003 | Wave 10 completion | IT Architect | All IA-INC-001..008 outputs available |
| TRG-004 | Post-capability-assessment | TL Agent | Team Capability Assessment (TL-INC-003) completed |
| TRG-005 | Risk review request | Stakeholder | Request to assess or re-assess technical risks |

## Delivery Playbook Context

- **Wave**: 11 | **Step**: 4
- **Upstream (Wave 10)**: IA-INC-001..008 (IT Architect Inception tasks)
- **Downstream (Wave 12)**: SE-INC-001..005 (Software Engineer Inception tasks)

## Trigger Keywords

The agent activates when the user's request matches these contexts:
- "technical risk"
- "risk assessment"
- "risk analysis"
- "dependency risk"
- "risk register"
- "risk mitigation"
- "technical dependencies"
- "risk management"

## Activation Parameters

| Parameter | Required | Description |
|:---|:---|:---|
| topic | Yes | The project or system for risk assessment |
| scope | No | Specific risk categories to focus on (default: full assessment) |
| output_dir | No | Directory for outputs (default: `./technical-risk-assessment/`) |
| architect_reports_ref | No | Path to IT Architect reports directory (IA-INC-001..008) |
