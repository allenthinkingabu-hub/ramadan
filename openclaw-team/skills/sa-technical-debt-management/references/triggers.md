# Trigger Mechanisms Configuration — sa-technical-debt-management

## Trigger Events

| Trigger ID | Event | Source | Condition |
|:---|:---|:---|:---|
| TRG-001 | User invokes skill directly | User | User requests technical debt assessment |
| TRG-002 | PM Agent assigns task | PM Agent | IA-DEV-004 task assigned via RACI matrix |
| TRG-003 | Code review flags debt | SA / TL | Code reviews identify significant technical debt |
| TRG-004 | Quality metrics decline | CI/CD Pipeline | Code quality metrics fall below thresholds |
| TRG-005 | Sprint planning debt allocation | PM / TL | Sprint capacity allocated for debt remediation |

## Delivery Playbook Context

- **Wave**: 10 | **Step**: 4
- **Upstream**: IA-REQ-001 (Architecture Design), IA-DEV-001..003 (Technical Guidance, Reviews, Spike/PoC), SA-REQ-001 (SAD), SA-REQ-004 (Technology Blueprint)
- **Downstream**: TL-DEV-001..005 (Technical Lead Development tasks)

## Trigger Keywords

The agent activates when the user's request matches these contexts:
- "technical debt"
- "tech debt"
- "debt management"
- "debt assessment"
- "code quality"
- "refactoring plan"
- "debt remediation"
- "debt backlog"
- "debt governance"
- "architecture drift"

## Activation Parameters

| Parameter | Required | Description |
|:---|:---|:---|
| topic | Yes | The system or codebase to assess for technical debt |
| scope | No | Specific debt categories to focus on (default: all categories) |
| output_dir | No | Directory for outputs (default: `./technical-debt/`) |
| architecture_design_ref | No | Path to Architecture Design artifacts (IA-REQ-001) |
| codebase_path | No | Path to the codebase for analysis |
| static_analysis_ref | No | Path to static analysis results |
