# Trigger Mechanisms Configuration -- tl-code-review-quality-gatekeeping

## Trigger Events

| Trigger ID | Event | Source | Condition |
|:---|:---|:---|:---|
| TRG-001 | User invokes skill directly | User | User requests code review standards or quality gate setup |
| TRG-002 | PM Agent assigns task | PM Agent | TL-DEV-001 task assigned via RACI matrix |
| TRG-003 | Wave 10 completion | IT Architect | Architecture design outputs available for compliance checks |
| TRG-004 | Quality issue escalation | Development Team | Code quality metrics breach threshold |
| TRG-005 | New project onboarding | PM Agent | New project requires review standards setup |

## Delivery Playbook Context

- **Wave**: 11 | **Step**: 1
- **Upstream (Wave 10)**: IA-REQ-001 (Architecture Design)
- **Downstream**: Next wave tasks as needed

## Trigger Keywords

The agent activates when the user's request matches these contexts:
- "code review"
- "PR review"
- "quality gate"
- "review checklist"
- "code quality"
- "review standards"
- "architectural compliance"
- "static analysis"
- "review process"
- "merge criteria"

## Activation Parameters

| Parameter | Required | Description |
|:---|:---|:---|
| topic | Yes | The project or codebase requiring review gatekeeping |
| scope | No | Specific review aspects to focus on (default: full review standards) |
| output_dir | No | Directory for outputs (default: `./code-review-quality-gatekeeping/`) |
| architecture_ref | No | Path to Architecture Design documents (IA-REQ-001) |
