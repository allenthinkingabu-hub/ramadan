# Tools Checklist

## Role: Technical Lead (TL) — Technical Design & Solution Design Agent

### Diagramming Tools

| # | Tool | Purpose | Usage Context |
|:--|:--|:--|:--|
| T1 | **Mermaid** | Primary diagram notation — generates flowcharts, sequence diagrams, C4 diagrams, ER diagrams, state diagrams | All diagram creation; rendered natively in GitHub, GitLab, Notion |
| T2 | **PlantUML** | Secondary diagram notation — advanced C4 diagrams with C4-PlantUML macros | Complex C4 Component diagrams requiring precise layout control |
| T3 | **draw.io / diagrams.net** | Visual diagramming tool for architecture and deployment diagrams | Optional — when stakeholders prefer visual drag-and-drop diagrams |

### Documentation Tools

| # | Tool | Purpose | Usage Context |
|:--|:--|:--|:--|
| T4 | **Markdown** | Primary documentation format | All technical design documents, ADRs, reports |
| T5 | **arc42 Template** | Document structure framework | Structuring the technical design document |
| T6 | **ADR Template** | Architecture Decision Record template | Documenting design decisions in Alternatives Considered section |

### Research & Analysis Tools

| # | Tool | Purpose | Usage Context |
|:--|:--|:--|:--|
| T7 | **Web Search** | Search the internet for industry best practices, technology comparisons, design patterns | Research phase (Step 3) |
| T8 | **Context7** | Query up-to-date documentation for libraries and frameworks | Technology-specific research during design |
| T9 | **WebFetch** | Fetch and analyze content from specific URLs | Retrieving reference documentation, API specs, framework guides |

### File Management Tools

| # | Tool | Purpose | Usage Context |
|:--|:--|:--|:--|
| T10 | **Read** | Read existing project files, requirements, architecture documents | Input gathering (Steps 1-2), reference validation |
| T11 | **Write** | Create new documents, diagrams, configuration files | Output production (Step 4) |
| T12 | **Edit** | Modify existing documents during iterative refinement | Remediation cycles, updates based on feedback |
| T13 | **Glob** | Find files by pattern in the project structure | Locating existing documentation, templates, configs |
| T14 | **Grep** | Search file contents for specific patterns | Finding references, API endpoints, configuration values |

### Validation Tools

| # | Tool | Purpose | Usage Context |
|:--|:--|:--|:--|
| T15 | **Bash** | Execute shell commands for file operations, validation scripts | Directory creation, file management, script execution |
| T16 | **DoD Checklist** | Self-verification against Definition of Done criteria | Quality gate validation before submission |
| T17 | **Supervisor Agent** | Independent quality inspection of all outputs | Post-completion quality assurance |

### Communication Tools

| # | Tool | Purpose | Usage Context |
|:--|:--|:--|:--|
| T18 | **AskUserQuestion** | Interactive dialogue with the user for requirements gathering | Steps 1-3 (understanding and validation) |
| T19 | **TaskCreate / TaskUpdate** | Track progress of multi-step work | Throughout the entire SOP process |

## Tool Selection Guide

| Scenario | Primary Tool | Fallback |
|:--|:--|:--|
| Create a sequence diagram | Mermaid | PlantUML |
| Create a C4 Context/Container diagram | Mermaid | PlantUML |
| Create a C4 Component diagram (complex) | PlantUML | Mermaid |
| Write technical design document | Markdown + arc42 | — |
| Research technology options | Web Search + Context7 | WebFetch |
| Gather user requirements | AskUserQuestion | — |
| Validate output quality | DoD Checklist → Supervisor | — |

## Configuration Notes

- Add new tools by appending rows to the appropriate table
- Update the Tool Selection Guide when new tools are added
- Mermaid is always the first choice for diagrams due to native rendering support
- All tools marked in the Research & Analysis section require saving results locally (Item 17)
