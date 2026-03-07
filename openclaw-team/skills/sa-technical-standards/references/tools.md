# Tools & MCP Tools -- sa-technical-standards

## Standard Tools

| Tool ID | Tool | Purpose |
|:---|:---|:---|
| TL-001 | Web Search | Research coding standards, design patterns, industry best practices |
| TL-002 | Web Fetch | Retrieve detailed style guides, linting documentation, framework conventions |
| TL-003 | File Read/Write | Read project files, write standards documents, output configs |
| TL-004 | Bash / Shell | Execute linting scripts, inspect project structures |
| TL-005 | Glob / Grep | Search codebase for existing standards, configuration files, patterns |
| TL-006 | Task (Sub-agent) | Delegate parallel research or standards section generation |

## MCP Tools

| MCP ID | MCP Tool | Purpose |
|:---|:---|:---|
| MCP-001 | Context7 (resolve-library-id + query-docs) | Query up-to-date documentation for frameworks, linters, testing tools |
| MCP-002 | GitHub (via gh CLI) | Inspect repositories, existing .editorconfig, linting configs, CI pipelines |
| MCP-003 | Custom MCP servers (if configured) | Access organization-specific standards, internal style guides |

## Tool Usage Guidelines

- Use **Web Search** and **Context7** for standards and best practices research in Step 3
- Use **File Write** to produce standards documents and configuration templates
- Use **Glob/Grep** to find existing linting configs, style guides, and CI pipeline definitions
- Use **Task sub-agents** to parallelize independent standards section research
- Save all research results locally per requirement #17
