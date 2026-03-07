# TOOLS.md — Tool Usage Conventions

## File Operations

- Use Read tool for file access (not cat/head/tail)
- Use Edit tool for modifications (not sed/awk)
- Use Write tool for new files (not echo/cat heredoc)
- Use Glob for file search (not find/ls)
- Use Grep for content search (not grep/rg)

## Git Conventions

- Commit after each completed phase
- Use descriptive commit messages referencing task ID
- Never force push or amend published commits

## External APIs

- Log all external API calls in research-log.md
- Cache research results to avoid redundant calls
- Cite sources for all findings
