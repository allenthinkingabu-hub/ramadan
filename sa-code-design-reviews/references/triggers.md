# Trigger Mechanisms Configuration — sa-code-design-reviews

## Trigger Events

| Trigger ID | Event | Source | Condition |
|:---|:---|:---|:---|
| TRG-001 | User invokes skill directly | User | User requests code or design review |
| TRG-002 | PM Agent assigns task | PM Agent | IA-DEV-002 task assigned via RACI matrix |
| TRG-003 | Critical PR submitted | Tech Lead / Dev | Pull request requires architectural review |
| TRG-004 | Design review requested | Tech Lead | Component design needs architecture compliance check |
| TRG-005 | Architecture drift detected | CI/CD Pipeline | Automated checks flag potential architectural violations |

## Delivery Playbook Context

- **Wave**: 10 | **Step**: 2
- **Upstream**: IA-REQ-001 (Architecture Design), IA-DEV-001 (Technical Guidance), SA-REQ-001 (SAD), SA-REQ-004 (Technology Blueprint)
- **Downstream**: TL-DEV-001..005 (Technical Lead Development tasks)

## Trigger Keywords

The agent activates when the user's request matches these contexts:
- "code review"
- "design review"
- "PR review"
- "pull request review"
- "architecture compliance"
- "architectural review"
- "code audit"
- "design audit"
- "compliance check"
- "architecture drift"

## Activation Parameters

| Parameter | Required | Description |
|:---|:---|:---|
| topic | Yes | The code, PR, or design to review |
| scope | No | Specific review aspects to focus on (default: full review) |
| output_dir | No | Directory for outputs (default: `./code-design-reviews/`) |
| architecture_design_ref | No | Path to Architecture Design artifacts (IA-REQ-001) |
| pr_url | No | URL to the pull request under review |
| codebase_path | No | Path to the codebase under review |
