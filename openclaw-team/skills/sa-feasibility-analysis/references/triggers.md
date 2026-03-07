# Trigger Mechanisms Configuration — SA-feasibility-analysis

## Trigger Events

| Trigger ID | Event | Source | Condition |
|:---|:---|:---|:---|
| TRG-001 | User invokes skill directly | User | User requests feasibility analysis or feasibility assessment |
| TRG-002 | PM Agent assigns task | PM Agent | IA-INC-002 task assigned via RACI matrix |
| TRG-003 | New requirement evaluation | System | New requirements need feasibility assessment |
| TRG-004 | Post-technical-discovery | SA Agent | Technical Discovery (IA-INC-001) completed, downstream feasibility needed |

## Trigger Keywords

The agent activates when the user's request matches these contexts:
- "feasibility analysis"
- "feasibility assessment"
- "feasibility study"
- "is this feasible"
- "can we build this"
- "technical feasibility"
- "evaluate requirements feasibility"
- "cost-benefit analysis"
- "risk assessment for requirements"

## Activation Parameters

| Parameter | Required | Description |
|:---|:---|:---|
| topic | Yes | The client's requirements to assess for feasibility |
| scope | No | Specific feasibility dimensions to focus on (default: full assessment) |
| output_dir | No | Directory for outputs (default: `./feasibility-analysis/`) |
| technical_discovery_ref | No | Path to Technical Discovery report if available |
