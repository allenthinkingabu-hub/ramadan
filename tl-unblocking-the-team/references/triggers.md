# Trigger Mechanisms Configuration -- tl-unblocking-the-team

## Trigger Events

| Trigger ID | Event | Source | Condition |
|:---|:---|:---|:---|
| TRG-001 | User invokes skill directly | User | User requests help with a technical blocker |
| TRG-002 | PM Agent assigns task | PM Agent | TL-DEV-004 task assigned via RACI matrix |
| TRG-003 | Team member escalation | Development Team | Developer blocked for more than configured threshold |
| TRG-004 | CI/CD pipeline failure | CI System | Build/deploy pipeline failing repeatedly |
| TRG-005 | Cross-team dependency block | PM Agent | External dependency blocking progress |

## Delivery Playbook Context

- **Wave**: 11 | **Step**: 4
- **Upstream (Wave 10)**: IA-REQ-001 (Architecture Design)
- **Downstream**: Next wave tasks as needed

## Trigger Keywords

- "blocked"
- "unblock"
- "stuck"
- "debugging help"
- "can't resolve"
- "build failing"
- "dependency issue"
- "impediment"
- "technical blocker"

## Activation Parameters

| Parameter | Required | Description |
|:---|:---|:---|
| topic | Yes | The blocker or impediment requiring resolution |
| scope | No | Specific area of investigation (default: full investigation) |
| output_dir | No | Directory for outputs (default: `./unblocking-the-team/`) |
| urgency | No | Urgency level: critical, high, medium, low (default: high) |
