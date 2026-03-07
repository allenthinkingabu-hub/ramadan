# Trigger Mechanisms Configuration — tl-technology-stack-decision

## Trigger Events

| Trigger ID | Event | Source | Condition |
|:---|:---|:---|:---|
| TRG-001 | User invokes skill directly | User | User requests technology stack decision or selection |
| TRG-002 | PM Agent assigns task | PM Agent | TL-INC-002 task assigned via RACI matrix |
| TRG-003 | Wave 10 completion | IT Architect | All IA-INC-001..008 outputs available |
| TRG-004 | Post-vision-definition | TL Agent | Technical Vision (TL-INC-001) completed, stack decisions needed |
| TRG-005 | Technology refresh request | Stakeholder | Request to evaluate and update technology choices |

## Delivery Playbook Context

- **Wave**: 11 | **Step**: 2
- **Upstream (Wave 10)**: IA-INC-001..008 (IT Architect Inception tasks)
- **Downstream (Wave 12)**: SE-INC-001..005 (Software Engineer Inception tasks)

## Trigger Keywords

The agent activates when the user's request matches these contexts:
- "technology stack"
- "tech stack decision"
- "framework selection"
- "language selection"
- "infrastructure choice"
- "technology selection"
- "stack evaluation"
- "technology comparison"

## Activation Parameters

| Parameter | Required | Description |
|:---|:---|:---|
| topic | Yes | The project or system requiring technology stack decisions |
| scope | No | Specific technology layers to focus on (default: full stack) |
| output_dir | No | Directory for outputs (default: `./technology-stack-decision/`) |
| architect_reports_ref | No | Path to IT Architect reports directory (IA-INC-001..008) |
