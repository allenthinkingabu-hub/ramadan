# Templates — sa-architecture-design

Templates used during the architecture design process. Refer to `config/outputs.yaml` for the full output content list.

## Template Sources
All templates are defined in the skill reference: `sa-architecture-design/references/output-templates.md`

## Templates Applied

| Template | Applied To | Notes |
|:---|:---|:---|
| YAML Config File | `config/*.yaml` (10 files) | Standard metadata + items structure |
| Conversation Log | `conversation-log.md` | Entry-by-entry Q&A log |
| Work Log | `work-log.md` | Timeline-based action log |
| Architecture Design Report | `architecture-design-report.md` | Full report with 10 sections |
| Mermaid Diagram File | `diagrams/*.md` (10 files) | Description + Mermaid diagram + Notes |
| Interface/Integration View | `diagrams/integration-view.md` | Protocols + Contracts + Error Handling + Diagram |
| NFR Alignment Note | `nfr-alignment.md` | NFR mapping + Constraints + Assumptions |
| Phase Question List | `phase{1,2,3}-questions.md` | Tabular Q&A with status tracking |
