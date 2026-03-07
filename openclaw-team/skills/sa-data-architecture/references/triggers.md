# Trigger Mechanisms Configuration -- sa-data-architecture

## Trigger Events

| Trigger ID | Event | Source | Condition |
|:---|:---|:---|:---|
| TRG-001 | User invokes skill directly | User | User requests data architecture design or data modelling |
| TRG-002 | PM Agent assigns task | PM Agent | IA-REQ-004 task assigned via RACI matrix |
| TRG-003 | Wave 9 completion | Solutions Architect | All SA-REQ-001..005 outputs available (SAD, Integration Architecture, NFR Mapping, Technology Blueprint, ARB Feedback) |
| TRG-004 | Post-architecture-design | SA Agent | Architecture Design (IA-REQ-001) completed, data architecture needed |
| TRG-005 | Data architecture review request | Stakeholder | Request to create or update data architecture |

## Delivery Playbook Context

- **Wave**: 10 | **Step**: 4
- **Upstream (Wave 9)**: SA-REQ-001 (SAD), SA-REQ-002 (Integration Architecture), SA-REQ-003 (NFR Mapping), SA-REQ-004 (Technology Blueprint), SA-REQ-005 (ARB Feedback)
- **Downstream (Wave 11)**: TL-REQ-001..005 (Technical Lead tasks)

## Trigger Keywords

The agent activates when the user's request matches these contexts:
- "data architecture"
- "data model"
- "data modelling"
- "database design"
- "storage strategy"
- "data migration"
- "ETL pipeline"
- "data flow"
- "data lineage"
- "schema design"

## Activation Parameters

| Parameter | Required | Description |
|:---|:---|:---|
| topic | Yes | The project or system to design data architecture for |
| scope | No | Specific data domains or aspects to focus on (default: full design) |
| output_dir | No | Directory for outputs (default: `./data-architecture/`) |
| technical_discovery_ref | No | Path to Technical Discovery report (IA-INC-001) |
| feasibility_analysis_ref | No | Path to Feasibility Analysis report (IA-INC-002) |
