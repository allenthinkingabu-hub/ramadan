# Trigger Mechanism Configuration

## Trigger Events

| # | Trigger Type | Trigger Condition | Source |
|:--|:--|:--|:--|
| T1 | **PM Task Assignment** | Project Manager AI Agent assigns TL-REQ-001 task via RACI matrix | PM Agent |
| T2 | **Manual Invocation** | User explicitly requests technical design for a complex feature | User |
| T3 | **Upstream Completion** | SA Architecture Design Agent completes architecture deliverables and notifies PM | SA Agent → PM Agent |
| T4 | **Sprint Planning** | Task is allocated to a sprint and the TL Agent is activated | PM Agent |
| T5 | **Change Request** | Existing technical design requires revision due to requirement changes | PM Agent / User |

## Trigger Input Requirements

When triggered, the agent expects the following inputs:

| Input | Required | Description |
|:--|:--|:--|
| `project_name` | Yes | Name of the project or system |
| `feature_scope` | Yes | Description of the complex feature(s) to design |
| `architecture_doc_path` | Yes | Path to the SA architecture design document |
| `requirements_doc_path` | Yes | Path to the business requirements document |
| `technology_stack_doc_path` | Recommended | Path to the technology stack selection document |
| `nfr_doc_path` | Recommended | Path to the non-functional requirements document |
| `api_contracts_path` | Optional | Path to existing API contracts or specifications |
| `data_model_path` | Optional | Path to existing data model documentation |

## Trigger Output

Upon activation, the agent:
1. Validates all required inputs are available (DoR check)
2. Loads the RACI matrix to identify stakeholders
3. Initializes the conversation log and work log
4. Begins the phased SOP process (Step 1 → Step 4)

## Configuration Notes

- Triggers can be extended by adding new rows to the Trigger Events table
- Input requirements can be adjusted based on project needs
- The agent will not proceed if required inputs are missing — it will request them from the user or PM Agent
