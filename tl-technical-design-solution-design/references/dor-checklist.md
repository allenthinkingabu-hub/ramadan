# Definition of Ready (DoR) Checklist

## Role: Technical Lead (TL) — Technical Design & Solution Design Agent

## DoR Checklist

The agent must verify all "Required" items pass before beginning work. "Recommended" items should be requested but do not block activation.

### A. Required Inputs

| # | Readiness Criterion | Source | Status Check | Required |
|:--|:--|:--|:--|:--|
| R1 | **Project name and scope defined** | PM Agent / User | Project name and feature scope provided | **Required** |
| R2 | **Business requirements document available** | BA Agent / PM Agent | File path provided and file is readable | **Required** |
| R3 | **Architecture design document available** | SA Agent | File path provided and file is readable | **Required** |
| R4 | **Task assignment confirmed** | PM Agent / User | TL-REQ-001 task explicitly assigned with clear scope | **Required** |
| R5 | **Upstream architecture approved** | SA Agent / PM Agent | Architecture design has passed SA supervisor inspection | **Required** |

### B. Recommended Inputs

| # | Readiness Criterion | Source | Status Check | Required |
|:--|:--|:--|:--|:--|
| R6 | **Technology stack selection document** | SA Agent / TL | File path provided and file is readable | Recommended |
| R7 | **Non-functional requirements document** | SA Agent / BA Agent | File path provided and file is readable | Recommended |
| R8 | **Existing API contracts** | DEV team / SA Agent | File path provided (if any exist) | Recommended |
| R9 | **Existing data models** | DEV team / SA Agent | File path provided (if any exist) | Recommended |
| R10 | **Integration constraints documentation** | SA Agent / DEV team | Third-party systems and protocols documented | Recommended |

### C. Agent Readiness

| # | Readiness Criterion | Verification | Required |
|:--|:--|:--|:--|
| R11 | **RACI matrix loaded** | `references/raci-matrix.md` is accessible | **Required** |
| R12 | **Skills list loaded** | `references/skills-list.md` is accessible | **Required** |
| R13 | **Knowledge base loaded** | `references/knowledge-base.md` is accessible | **Required** |
| R14 | **Tools list loaded** | `references/tools-list.md` is accessible | **Required** |
| R15 | **MCP tools available** | Context7 MCP server is accessible | **Required** |
| R16 | **Output templates loaded** | `references/output-templates.md` is accessible | **Required** |
| R17 | **SOP process loaded** | `references/sop-process.md` is accessible | **Required** |
| R18 | **DoD checklist loaded** | `references/dod-checklist.md` is accessible | **Required** |
| R19 | **Output directory writable** | Target directory exists and is writable | **Required** |

### D. Stakeholder Availability

| # | Readiness Criterion | Verification | Required |
|:--|:--|:--|:--|
| R20 | **User available for dialogue** | User is present and responsive for iterative Q&A (Phases 1-3) | **Required** |
| R21 | **SA Agent consultable** | SA Agent can be reached for architecture clarification | Recommended |
| R22 | **PM Agent reachable** | PM Agent can receive completion notification | Recommended |

---

## DoR Verification Process

1. On activation, load this checklist
2. Verify each "Required" item — all must pass
3. Check each "Recommended" item — request missing items but do not block
4. If any "Required" item fails:
   - Identify what is missing
   - Request the missing input from the appropriate source (PM Agent, SA Agent, User)
   - Wait for the input before proceeding
5. Log DoR verification results in the work log
6. Proceed to Phase 1 only when all "Required" items pass

## DoR Verification Report Format

```markdown
## DoR Verification — {YYYY-MM-DD HH:MM}

| # | Item | Status | Notes |
|:--|:--|:--|:--|
| R1 | Project name and scope | PASS / FAIL | {notes} |
| R2 | Business requirements doc | PASS / FAIL | {file path or "missing"} |
| ... | ... | ... | ... |

**Result**: READY / NOT READY
**Missing Items**: {list of missing required items, if any}
```

## Configuration Notes

- Add new readiness criteria by appending rows to the appropriate section
- "Required" items are mandatory — agent cannot start work without them
- "Recommended" items enhance quality but do not block activation
- Update source information when organizational structure changes
