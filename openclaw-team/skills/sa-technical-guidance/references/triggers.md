# Trigger Mechanisms Configuration — sa-technical-guidance

## Trigger Events

| Trigger ID | Event | Source | Condition |
|:---|:---|:---|:---|
| TRG-001 | User invokes skill directly | User | User requests architectural guidance for development |
| TRG-002 | PM Agent assigns task | PM Agent | IA-DEV-001 task assigned via RACI matrix |
| TRG-003 | Developer raises architecture question | Developer / TL | Architecture clarification needed during implementation |
| TRG-004 | Design pattern selection needed | Tech Lead | Pattern selection or evaluation requested |
| TRG-005 | Implementation alignment check | SA Agent | Verify implementation aligns with architecture design |

## Delivery Playbook Context

- **Wave**: 10 | **Step**: 1
- **Upstream**: IA-REQ-001 (Architecture Design), SA-REQ-001 (SAD), SA-REQ-004 (Technology Blueprint), SA-REQ-005 (ARB Feedback)
- **Downstream**: TL-DEV-001..005 (Technical Lead Development tasks)

## Trigger Keywords

The agent activates when the user's request matches these contexts:
- "technical guidance"
- "architectural guidance"
- "design pattern"
- "implementation guidance"
- "architecture decision"
- "code architecture"
- "developer support"
- "pattern selection"
- "architecture-to-code"
- "implementation alignment"

## Activation Parameters

| Parameter | Required | Description |
|:---|:---|:---|
| topic | Yes | The area or component requiring architectural guidance |
| scope | No | Specific guidance aspects to focus on (default: full guidance) |
| output_dir | No | Directory for outputs (default: `./technical-guidance/`) |
| architecture_design_ref | No | Path to Architecture Design artifacts (IA-REQ-001) |
| codebase_path | No | Path to the codebase being developed |
