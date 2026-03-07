# Trigger Mechanisms Configuration -- tl-technical-decision-making

## Trigger Events

| Trigger ID | Event | Source | Condition |
|:---|:---|:---|:---|
| TRG-001 | User invokes skill directly | User | User requests technical decision support |
| TRG-002 | PM Agent assigns task | PM Agent | TL-DEV-003 task assigned via RACI matrix |
| TRG-003 | Implementation decision needed | Development Team | Team encounters decision point requiring TL guidance |
| TRG-004 | Library/framework evaluation | Sprint Planning | New dependency needs evaluation |
| TRG-005 | Architecture trade-off required | IT Architect | Architecture options need TL-level trade-off analysis |

## Delivery Playbook Context

- **Wave**: 11 | **Step**: 3
- **Upstream (Wave 10)**: IA-REQ-001 (Architecture Design)
- **Downstream**: Next wave tasks as needed

## Trigger Keywords

The agent activates when the user's request matches these contexts:
- "technical decision"
- "library selection"
- "framework comparison"
- "trade-off analysis"
- "implementation approach"
- "technology evaluation"
- "ADR"
- "architecture decision"
- "build vs buy"

## Activation Parameters

| Parameter | Required | Description |
|:---|:---|:---|
| topic | Yes | The decision context or technical question |
| scope | No | Specific decision areas to focus on (default: full evaluation) |
| output_dir | No | Directory for outputs (default: `./technical-decision-making/`) |
| architecture_ref | No | Path to Architecture Design documents (IA-REQ-001) |
