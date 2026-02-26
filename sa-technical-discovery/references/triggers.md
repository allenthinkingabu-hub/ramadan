# Trigger Mechanisms Configuration — SA-technical-discovery

## Trigger Events

| Trigger ID | Event | Source | Condition |
|:---|:---|:---|:---|
| TRG-001 | User invokes skill directly | User | User requests technical discovery or technology assessment |
| TRG-002 | PM Agent assigns task | PM Agent | IA-INC-001 task assigned via RACI matrix |
| TRG-003 | New project onboarding | System | New project requires technology landscape assessment |
| TRG-004 | Architecture review request | Stakeholder | Request to evaluate existing systems and infrastructure |

## Trigger Keywords

The agent activates when the user's request matches these contexts:
- "technical discovery"
- "technology assessment"
- "system landscape analysis"
- "infrastructure evaluation"
- "current state assessment"
- "technology audit"
- "existing systems review"

## Activation Parameters

| Parameter | Required | Description |
|:---|:---|:---|
| topic | Yes | The project or system to assess |
| scope | No | Specific areas to focus on (default: full assessment) |
| output_dir | No | Directory for outputs (default: `./technical-discovery/`) |
