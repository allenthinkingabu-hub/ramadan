# Trigger Mechanisms Configuration — sa-spike-poc-leadership

## Trigger Events

| Trigger ID | Event | Source | Condition |
|:---|:---|:---|:---|
| TRG-001 | User invokes skill directly | User | User requests a technical spike or proof-of-concept |
| TRG-002 | PM Agent assigns task | PM Agent | IA-DEV-003 task assigned via RACI matrix |
| TRG-003 | Technical uncertainty identified | SA / TL | Architectural uncertainty needs investigation |
| TRG-004 | Technology selection needed | SA Agent | Competing technology options require PoC evaluation |
| TRG-005 | Integration risk flagged | SA / TL | Third-party integration risk needs de-risking |

## Delivery Playbook Context

- **Wave**: 10 | **Step**: 3
- **Upstream**: IA-REQ-001 (Architecture Design), IA-DEV-001 (Technical Guidance), SA-REQ-001 (SAD), SA-REQ-004 (Technology Blueprint)
- **Downstream**: TL-DEV-001..005 (Technical Lead Development tasks)

## Trigger Keywords

The agent activates when the user's request matches these contexts:
- "technical spike"
- "proof of concept"
- "PoC"
- "technology evaluation"
- "de-risk"
- "feasibility test"
- "benchmark"
- "prototype"
- "technology comparison"
- "spike investigation"

## Activation Parameters

| Parameter | Required | Description |
|:---|:---|:---|
| topic | Yes | The uncertainty area or technology to investigate |
| scope | No | Specific aspects to focus on (default: full investigation) |
| output_dir | No | Directory for outputs (default: `./spike-poc/`) |
| architecture_design_ref | No | Path to Architecture Design artifacts (IA-REQ-001) |
| time_box | No | Maximum duration for the spike (default: defined in dialogue) |
| success_criteria | No | Measurable criteria for PoC success |
