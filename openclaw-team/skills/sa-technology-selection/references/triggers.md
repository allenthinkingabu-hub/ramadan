# Trigger Mechanisms Configuration — sa-technology-selection

## Trigger Events

| Trigger ID | Event | Source | Condition |
|:---|:---|:---|:---|
| TRG-001 | User invokes skill directly | User | User requests technology selection or stack evaluation |
| TRG-002 | PM Agent assigns task | PM Agent | IA-INC-003 task assigned via RACI matrix |
| TRG-003 | Post-technical-discovery | SA Agent | Technical Discovery (IA-INC-001) completed, technology selection needed |
| TRG-004 | Post-feasibility-analysis | SA Agent | Feasibility Analysis (IA-INC-002) completed, technology selection needed |

## Trigger Keywords

The agent activates when the user's request matches these contexts:
- "technology selection"
- "stack evaluation"
- "framework comparison"
- "build vs buy"
- "vendor evaluation"
- "platform selection"

## Activation Parameters

| Parameter | Required | Description |
|:---|:---|:---|
| topic | Yes | The project or system to select technologies for |
| scope | No | Specific technology categories to focus on (default: full evaluation) |
| output_dir | No | Directory for outputs (default: `./technology-selection/`) |
| technical_discovery_ref | No | Path to Technical Discovery report (IA-INC-001) |
| feasibility_analysis_ref | No | Path to Feasibility Analysis report (IA-INC-002) |
