# Tools & MCP Tools -- tl-code-review-quality-gatekeeping

## Standard Tools

| Tool ID | Tool | Purpose |
|:---|:---|:---|
| TL-001 | Web Search | Research code review best practices, quality gate patterns |
| TL-002 | Web Fetch | Retrieve detailed guides on review tooling and static analysis |
| TL-003 | File Read/Write | Read project files, write review standards, output documents and configs |
| TL-004 | Bash / Shell | Execute static analysis tools, inspect codebase structure |
| TL-005 | Glob / Grep | Search codebase for patterns, existing review configurations |
| TL-006 | Task (Sub-agent) | Delegate parallel research or analysis tasks |

## MCP Tools

| MCP ID | MCP Tool | Purpose |
|:---|:---|:---|
| MCP-001 | Context7 (resolve-library-id + query-docs) | Query up-to-date documentation for linting tools, frameworks |
| MCP-002 | GitHub (via gh CLI) | Inspect PRs, review comments, repository settings, branch protections |
| MCP-003 | Custom MCP servers (if configured) | Access organization-specific code quality APIs |

## Tool Usage Guidelines

- Use **Web Search** and **Context7** for code review practice research in Step 3
- Use **GitHub CLI** to inspect existing PR workflows and branch protection rules
- Use **Glob/Grep** to find existing linter configs, test coverage reports
- Use **File Write** to produce review checklists, quality gate definitions
- Use **Task sub-agents** to parallelize independent analysis tasks
