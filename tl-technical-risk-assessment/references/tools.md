# Tools & MCP Tools — tl-technical-risk-assessment

## Standard Tools

| Tool ID | Tool | Purpose |
|:---|:---|:---|
| TL-001 | Web Search | Research risk management frameworks, known technology vulnerabilities, outage history |
| TL-002 | Web Fetch | Retrieve SLA documentation, vendor status pages, CVE databases |
| TL-003 | File Read/Write | Read architecture docs, write risk assessment documents, output configs |
| TL-004 | Bash / Shell | Execute verification scripts, check dependency versions |
| TL-005 | Glob / Grep | Search codebase for dependency files, configuration vulnerabilities |
| TL-006 | Task (Sub-agent) | Delegate parallel risk analysis for different categories |

## MCP Tools

| MCP ID | MCP Tool | Purpose |
|:---|:---|:---|
| MCP-001 | Context7 (resolve-library-id + query-docs) | Query documentation for technology risk profiles |
| MCP-002 | GitHub (via gh CLI) | Inspect dependency graphs, security advisories, issue trackers |
| MCP-003 | Custom MCP servers (if configured) | Access organization incident history, risk databases |

## Tool Usage Guidelines

- Use **Web Search** for risk research, CVE lookups, and vendor reliability history
- Use **GitHub** to analyze dependency graphs and security advisories
- Use **Glob/Grep** to find dependency manifests and configuration files
- Use **Task sub-agents** to parallelize risk analysis across categories
- Save all research results locally per logging requirements
