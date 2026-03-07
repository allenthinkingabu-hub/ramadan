# Trigger Mechanisms Configuration -- sa-security-review

## Trigger Events

| Trigger ID | Event | Source | Condition |
|:---|:---|:---|:---|
| TRG-001 | User invokes skill directly | User | User requests security review |
| TRG-002 | PM Agent assigns task | PM Agent | IA-QA-002 task assigned via RACI matrix |
| TRG-003 | Upstream task completion | SA Agent | Prerequisite tasks completed, security review needed |
| TRG-004 | QA phase requirement | Process | QA phase requires security review validation |
| TRG-005 | Stakeholder request | Stakeholder | Request for security review or update |

## Delivery Playbook Context

- **Wave**: 10 | **Step**: 2
- **Upstream**: Architecture Design outputs, related upstream deliverables
- **Downstream**: TL-QA-001..004 (Technical Lead tasks)

## Trigger Keywords

The agent activates when the user's request matches these contexts:
- "security review"
- "threat model"
- "vulnerability assessment"
- "penetration test"
- "security audit"
- "compliance review"
- "OWASP"
- "security policy"
- "threat analysis"
- "security scan"

## Activation Parameters

| Parameter | Required | Description |
|:---|:---|:---|
| topic | Yes | The system or project for security review |
| scope | No | Specific aspects to focus on (default: full scope) |
| output_dir | No | Directory for outputs (default: `./security-review/`) |
| upstream_refs | No | Paths to upstream deliverable documents |
