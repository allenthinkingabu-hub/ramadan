# Trigger Mechanisms Configuration — tl-team-capability-assessment

## Trigger Events

| Trigger ID | Event | Source | Condition |
|:---|:---|:---|:---|
| TRG-001 | User invokes skill directly | User | User requests team capability assessment or skills evaluation |
| TRG-002 | PM Agent assigns task | PM Agent | TL-INC-003 task assigned via RACI matrix |
| TRG-003 | Wave 10 completion | IT Architect | All IA-INC-001..008 outputs available |
| TRG-004 | Post-stack-decision | TL Agent | Technology Stack Decision (TL-INC-002) completed, team readiness check needed |
| TRG-005 | Team restructuring event | Stakeholder | Team changes require capability reassessment |

## Delivery Playbook Context

- **Wave**: 11 | **Step**: 3
- **Upstream (Wave 10)**: IA-INC-001..008 (IT Architect Inception tasks)
- **Downstream (Wave 12)**: SE-INC-001..005 (Software Engineer Inception tasks)

## Trigger Keywords

The agent activates when the user's request matches these contexts:
- "team capability"
- "skills assessment"
- "skill gap analysis"
- "team readiness"
- "capability assessment"
- "training needs"
- "hiring plan"
- "knowledge transfer"

## Activation Parameters

| Parameter | Required | Description |
|:---|:---|:---|
| topic | Yes | The project or team for capability assessment |
| scope | No | Specific skill domains or team segments to focus on (default: full assessment) |
| output_dir | No | Directory for outputs (default: `./team-capability-assessment/`) |
| architect_reports_ref | No | Path to IT Architect reports directory (IA-INC-001..008) |
