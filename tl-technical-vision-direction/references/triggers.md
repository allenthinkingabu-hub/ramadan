# Trigger Mechanisms Configuration — tl-technical-vision-direction

## Trigger Events

| Trigger ID | Event | Source | Condition |
|:---|:---|:---|:---|
| TRG-001 | User invokes skill directly | User | User requests technical vision or technical direction definition |
| TRG-002 | PM Agent assigns task | PM Agent | TL-INC-001 task assigned via RACI matrix |
| TRG-003 | Wave 10 completion | IT Architect | All IA-INC-001..008 outputs available |
| TRG-004 | Project kickoff | PM Agent | New project inception requires technical direction |
| TRG-005 | Strategy pivot request | Stakeholder | Request to redefine or update technical direction |

## Delivery Playbook Context

- **Wave**: 11 | **Step**: 1
- **Upstream (Wave 10)**: IA-INC-001 (Technical Discovery), IA-INC-002 (Feasibility), IA-INC-003 (PoC), IA-INC-004 (NFR), IA-INC-005 (Tech Landscape), IA-INC-006 (Risk), IA-INC-007 (Integration), IA-INC-008 (Architecture Patterns)
- **Downstream (Wave 12)**: SE-INC-001..005 (Software Engineer Inception tasks)

## Trigger Keywords

The agent activates when the user's request matches these contexts:
- "technical vision"
- "technical direction"
- "technology strategy"
- "technical approach"
- "technology alignment"
- "guiding principles"
- "technical roadmap"
- "technology vision"

## Activation Parameters

| Parameter | Required | Description |
|:---|:---|:---|
| topic | Yes | The project or product for which technical vision is needed |
| scope | No | Specific aspects of technical direction to focus on (default: full vision) |
| output_dir | No | Directory for outputs (default: `./technical-vision-direction/`) |
| architect_reports_ref | No | Path to IT Architect reports directory (IA-INC-001..008) |
