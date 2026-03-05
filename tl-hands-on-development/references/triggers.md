# Trigger Mechanisms Configuration -- tl-hands-on-development

## Trigger Events

| Trigger ID | Event | Source | Condition |
|:---|:---|:---|:---|
| TRG-001 | User invokes skill directly | User | User requests TL-level implementation support |
| TRG-002 | PM Agent assigns task | PM Agent | TL-DEV-002 task assigned via RACI matrix |
| TRG-003 | Critical path identified | Sprint Planning | Feature on critical path requires senior implementation |
| TRG-004 | Pattern establishment needed | Architecture | New pattern needs reference implementation |
| TRG-005 | Complex feature assignment | PM Agent | Feature complexity exceeds team capability |

## Delivery Playbook Context

- **Wave**: 11 | **Step**: 2
- **Upstream (Wave 10)**: IA-REQ-001 (Architecture Design)
- **Downstream**: Next wave tasks as needed

## Trigger Keywords

The agent activates when the user's request matches these contexts:
- "hands-on development"
- "implement feature"
- "reference implementation"
- "critical path coding"
- "pattern implementation"
- "prototype development"
- "proof of concept"
- "complex feature"
- "lead by example"

## Activation Parameters

| Parameter | Required | Description |
|:---|:---|:---|
| topic | Yes | The feature or component requiring TL development |
| scope | No | Specific implementation aspects to focus on (default: full implementation) |
| output_dir | No | Directory for outputs (default: `./hands-on-development/`) |
| architecture_ref | No | Path to Architecture Design documents (IA-REQ-001) |
