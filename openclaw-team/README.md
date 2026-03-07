# OpenClaw AI Agent Team — Deployment & Usage Guide

A self-contained package for deploying a complete OpenClaw multi-agent IT delivery team. Three specialized AI agents collaborate under a PM orchestrator to execute end-to-end IT project lifecycles.

## Team Overview

| Agent | Role | Type | Skills | Phases |
|:------|:-----|:-----|-------:|:-------|
| **PM** | IT Project Manager | Orchestrator | 24 + 24 supervisors | Inception, Requirements, Development, QA, Release |
| **IPM** | IT Product Manager | Role Agent | 21 + 21 supervisors | Inception, Requirements, Development, QA, Release |
| **SA** | System Architect | Role Agent | 37 + 37 supervisors | Inception, Requirements, Development, QA, Release |
| **TL** | Technical Lead | Role Agent | (registered, skills pending) | — |

**Total: 82 main skills + 82 supervisors = 164 skill directories, 940 files**

---

## Prerequisites

- Python 3.8+
- OpenClaw runtime environment
- Claude API access (model: `claude-opus-4-6`)

---

## Quick Start

```bash
# 1. Copy openclaw-team/ to the target machine

# 2. Run the installer
cd openclaw-team
python3 scripts/install_team.py --target ~/my-project --force

# 3. Verify installation
python3 scripts/install_team.py --target ~/my-project --validate
```

---

## Installation Options

### Default Install

Installs skills to the target directory and creates `~/.openclaw/workspace-{pm,ipm,sa}/` agent workspaces.

```bash
cd openclaw-team
python3 scripts/install_team.py --target /path/to/workspace
```

### Install with Validation

Runs `quick_validate.py` on every skill after installation to confirm structural integrity.

```bash
python3 scripts/install_team.py --target /path/to/workspace --force --validate
```

### Skills Only (No Agent Workspaces)

Copies skills, config, and bootstrap files but skips `~/.openclaw/` workspace setup.

```bash
python3 scripts/install_team.py --target /path/to/workspace --skip-workspaces
```

### Force Overwrite

Overwrites existing `~/.openclaw/workspace-*` directories. Useful for clean reinstalls.

```bash
python3 scripts/install_team.py --target /path/to/workspace --force
```

### Installer CLI Reference

```
python3 scripts/install_team.py [OPTIONS]

Options:
  --target PATH        Target workspace directory (default: current directory)
  --force              Overwrite existing ~/.openclaw workspaces
  --skip-workspaces    Only copy skills, skip ~/.openclaw setup
  --validate           Run quick_validate.py on all skills after install
```

---

## What Gets Installed

### Target Workspace (your project directory)

```
<target>/
├── AGENTS.md                     # Agent registry + event protocol
├── SOUL.md                       # Team persona boundaries
├── IDENTITY.md                   # Team identity
├── USER.md                       # User context
├── TOOLS.md                      # Tool usage conventions
├── config/
│   ├── agents-registry.json      # Agent definitions (PM, IPM, SA, TL)
│   ├── openclaw.json             # Agent config + skill bindings
│   └── event-bus.json            # Event routing rules
├── pm-project-charter-development/
│   ├── SKILL.md                  # Skill instructions (Phase 0-5 workflow)
│   ├── references/               # DoR, DoD, RACI, SOP, triggers, templates
│   └── scripts/verify_dod.py     # Automated DoD checker
├── pm-project-charter-development-supervisor/
│   ├── SKILL.md                  # Supervisor inspection checklist
│   └── references/inspection-criteria.md
├── ... (162 more skill directories)
└── task/                         # Delivery playbook + role task definitions
```

### Agent Workspaces (`~/.openclaw/`)

```
~/.openclaw/
├── workspace-pm/
│   ├── config/
│   │   ├── tasks-index.json      # 24 PM tasks with dependencies
│   │   └── state.json            # Execution state tracker
│   ├── AGENTS.md                 # PM-specific operating instructions
│   ├── SOUL.md                   # PM persona
│   ├── IDENTITY.md               # PM identity
│   ├── USER.md                   # Team context
│   └── TOOLS.md                  # Tool conventions
├── workspace-ipm/
│   ├── config/
│   │   ├── tasks-index.json      # 21 IPM tasks
│   │   └── state.json
│   └── ... (same bootstrap files)
└── workspace-sa/
    ├── config/
    │   ├── tasks-index.json      # 33 SA tasks
    │   └── state.json
    └── ... (same bootstrap files)
```

---

## Package Structure

```
openclaw-team/                     # This package
├── AGENTS.md, SOUL.md, ...        # Team-level bootstrap files
├── config/                        # Shared configuration
├── skills/                        # 164 skill directories
│   ├── pm-* (48 dirs)             #   24 main + 24 supervisor
│   ├── ipm-* (42 dirs)            #   21 main + 21 supervisor
│   └── sa-*/SA-* (74 dirs)        #   37 main + 37 supervisor
├── workspaces/                    # Agent workspace templates
│   ├── pm/                        #   PM tasks-index + state + bootstrap
│   ├── ipm/                       #   IPM tasks-index + state + bootstrap
│   └── sa/                        #   SA tasks-index + state + bootstrap
├── task/                          # Delivery playbook + role task files
├── docs/                          # Skill creator prompt reference
├── scripts/
│   ├── install_team.py            #   One-click installer
│   ├── quick_validate.py          #   Skill structure validator
│   ├── init_skill.py              #   New skill scaffold generator
│   └── package_skill.py           #   Skill packager for distribution
└── README.md                      # This file
```

---

## Architecture

### Event Flow

```
PM Agent (Orchestrator)
    │
    ├── TaskTriggered ──> IPM Agent ──> SupervisorTriggered ──> IPM Supervisor
    │                         │                                      │
    │                         │ <── SupervisorCompleted (100% pass) ──┘
    │ <── TaskCompleted ──────┘
    │
    ├── TaskTriggered ──> SA Agent  ──> SupervisorTriggered ──> SA Supervisor
    │                         │                                      │
    │                         │ <── SupervisorCompleted (100% pass) ──┘
    │ <── TaskCompleted ──────┘
    │
    └── (triggers next wave)
```

### Wave Execution Model

Tasks are organized into waves. All tasks in Wave N must complete before Wave N+1 begins. Within a wave, tasks execute in parallel.

```
Wave 1:  PM-INC-001..005  (Project Charter, Stakeholder Analysis, ...)
Wave 2:  IPM-INC-001..005 (Requirement Gathering, Market Research, BRD, ...)
Wave 3:  SM-INC-001..005  (Agile Framework Setup, ...)
  ...
Wave 10: IA-INC-001..008  (Technical Discovery, Feasibility, ...)
Wave 11: TL-INC-001..005  (Technical Vision, Stack Decision, ...)
```

### Skill Execution (Phase 0-5)

Every skill follows the same six-phase workflow:

| Phase | Name | Purpose |
|:------|:-----|:--------|
| 0 | Initialization | Create output directory, initialize logs, check DoR |
| 1 | Understand Task Purpose | Clarify why the task is needed, get user confirmation |
| 2 | Understand the Topic | Deep-dive into context, incorporate upstream inputs |
| 3 | Research & Q&A | Industry research, generate questions, iterative dialogue |
| 4 | Execute & Deliver | Produce deliverables using templates, self-check against DoD |
| 5 | Completion & Handoff | Invoke supervisor, remediate if needed, report to PM |

### Quality Gate (Supervisor)

Every skill has a paired supervisor that independently verifies:

- **Infrastructure** (INS-01 to INS-06): Reference files exist and are properly structured
- **Process** (INS-07 to INS-12): Logs maintained, DoD verified, user confirmations obtained
- **Deliverable Quality** (INS-DQ-01 to INS-DQ-05): Content complete, no TBDs, template followed

The supervisor must achieve **100% pass rate** before TaskCompleted is sent to PM.

---

## Skill Inventory

### PM — IT Project Manager (24 skills)

| Phase | Task ID | Skill |
|:------|:--------|:------|
| Inception | PM-INC-001 | Project Charter Development |
| Inception | PM-INC-002 | Stakeholder Analysis |
| Inception | PM-INC-003 | Resource Planning |
| Inception | PM-INC-004 | Budget Estimation |
| Inception | PM-INC-005 | Risk Register Initialization |
| Requirements | PM-REQ-001 | Project Plan & WBS |
| Requirements | PM-REQ-002 | Schedule Development |
| Requirements | PM-REQ-003 | RACI Matrix Definition |
| Requirements | PM-REQ-004 | Communication Plan |
| Requirements | PM-REQ-005 | Vendor & Procurement Management |
| Development | PM-DEV-001 | Progress Tracking & Reporting |
| Development | PM-DEV-002 | Risk & Issue Management |
| Development | PM-DEV-003 | Scope Management |
| Development | PM-DEV-004 | Resource Management |
| Development | PM-DEV-005 | Stakeholder Communication |
| QA | PM-QA-001 | UAT Coordination |
| QA | PM-QA-002 | Go/No-Go Decision Facilitation |
| QA | PM-QA-003 | Release Planning |
| QA | PM-QA-004 | Compliance & Audit Readiness |
| Release | PM-REL-001 | Go-Live Coordination |
| Release | PM-REL-002 | Hypercare Management |
| Release | PM-REL-003 | Project Closure |
| Release | PM-REL-004 | Lessons Learned & Retrospective |
| Release | PM-REL-005 | Benefits Handover |

### IPM — IT Product Manager (21 skills)

| Phase | Task ID | Skill |
|:------|:--------|:------|
| Inception | IPM-INC-001 | Requirement Gathering |
| Inception | IPM-INC-002 | Market Research |
| Inception | IPM-INC-003 | BRD Writing |
| Inception | IPM-INC-004 | Feasibility Assessment |
| Inception | IPM-INC-005 | Alignment |
| Requirements | IPM-REQ-001 | PRD Writing |
| Requirements | IPM-REQ-002 | User Story Decomposition |
| Requirements | IPM-REQ-003 | Prioritization |
| Requirements | IPM-REQ-004 | Prototype Review |
| Requirements | IPM-REQ-005 | Refinement Meetings |
| Development | IPM-DEV-001 | Requirement Clarification |
| Development | IPM-DEV-002 | Acceptance Criteria |
| Development | IPM-DEV-003 | PRD Change Management |
| Development | IPM-DEV-004 | Progress Tracking |
| QA | IPM-QA-001 | UAT Organization |
| QA | IPM-QA-002 | Bug Prioritization |
| QA | IPM-QA-003 | Launch Checklist |
| Release | IPM-REL-001 | Release Coordination |
| Release | IPM-REL-002 | Data Analysis |
| Release | IPM-REL-003 | User Feedback |
| Release | IPM-REL-004 | Retrospectives |

### SA — System Architect (37 skills)

| Phase | Task ID | Skill |
|:------|:--------|:------|
| Inception | IA-INC-001 | Technical Discovery |
| Inception | IA-INC-002 | Feasibility Analysis |
| Inception | IA-INC-003 | Technology Selection |
| Inception | IA-INC-004 | Risk Identification |
| Inception | IA-INC-005 | Cost Estimation Support |
| Inception | IA-INC-006 | Stakeholder Alignment |
| Inception | IA-INC-007 | Compliance & Privacy Scan |
| Inception | IA-INC-008 | Third-Party/Vendor Strategy |
| Requirements | IA-REQ-001 | Architecture Design |
| Requirements | IA-REQ-002 | Non-Functional Requirements |
| Requirements | IA-REQ-003 | Integration Design |
| Requirements | IA-REQ-004 | Data Architecture |
| Requirements | IA-REQ-005 | Technical Standards |
| Requirements | IA-REQ-006 | Data Privacy & Governance |
| Requirements | IA-REQ-007 | DR/BCP Architecture |
| Requirements | IA-REQ-008 | Vendor & Third-Party Controls |
| Requirements | IA-REQ-009 | Requirements Traceability |
| Development | IA-DEV-001 | Technical Guidance |
| Development | IA-DEV-002 | Code & Design Reviews |
| Development | IA-DEV-003 | Spike & PoC Leadership |
| Development | IA-DEV-004 | Technical Debt Management |
| Development | IA-DEV-005 | Architecture Decision Records (ADRs) |
| Development | IA-DEV-006 | IaC & Environment Baseline |
| QA | IA-QA-001 | Performance & Load Testing |
| QA | IA-QA-002 | Security Review |
| QA | IA-QA-003 | Infrastructure Validation |
| QA | IA-QA-004 | Integration Testing Support |
| QA | IA-QA-005 | Compliance Validation |
| Release | IA-REL-001 | Deployment Architecture |
| Release | IA-REL-002 | Monitoring & Observability |
| Release | IA-REL-003 | Capacity Planning |
| Release | IA-REL-004 | Post-Mortem Analysis |
| Release | IA-REL-005 | Architecture Evolution |
| Release | IA-REL-006 | Runbooks & Knowledge Transfer |
| Release | IA-REL-007 | FinOps & Cost Guardrails |
| Release | IA-REL-008 | Resilience/Chaos Testing |
| Release | IA-REL-009 | Architecture Governance & Change Control |

---

## Configuration Files

### `config/agents-registry.json`

Central registry of all agents. Each entry defines role code, task prefix, workspace path, and list of skill directories.

### `config/openclaw.json`

OpenClaw gateway configuration. Contains agent list with model and tool profiles, skill entries (enabled/disabled), and event bus bindings.

### `config/event-bus.json`

Event routing rules: TaskTriggered (PM to agents), TaskCompleted (agents to PM), SupervisorTriggered/Completed (agents to supervisors).

### `workspaces/<role>/config/tasks-index.json`

Per-agent task registry. Maps each task ID to its skill directory, phase, wave, step, and downstream triggers (`next` array).

### `workspaces/<role>/config/state.json`

Execution state tracker. Records task status (PENDING/IN_PROGRESS/DONE/FAILED) for idempotent resumption.

---

## Extending the Team

### Add a New Skill

```bash
# Scaffold a new skill
python3 scripts/init_skill.py my-new-skill --path skills/

# Edit the generated SKILL.md — replace TODOs with actual content
# Add references/ files (dor.md, dod.md, etc.)

# Validate
python3 scripts/quick_validate.py skills/my-new-skill
```

### Add a New Role

Use the skill-creator prompt (`docs/openclaw-skill-creator-prompt.md`) with ACTION=create to generate a complete new role with all skills, config, and workspace.

### Complete the TL Agent

The Technical Lead agent is registered in `agents-registry.json` but has no skills yet. Follow the same pattern as PM/IPM/SA to create TL skills from `task/technical-lead-main-tasks.md`.

---

## Troubleshooting

| Issue | Solution |
|:------|:---------|
| `install_team.py` says workspace exists | Use `--force` flag to overwrite |
| Skill validation fails | Check SKILL.md frontmatter: `name` must be lowercase hyphen-case, `description` must not contain `<` or `>` |
| Missing tasks-index.json for SA | The installer copies it from `workspaces/sa/config/tasks-index.json` |
| Agent can't find skills | Verify `openclaw.json` has correct `skills.entries` and skill directories exist in workspace |
| Supervisor always fails | Check that all `references/` files exist in the main skill directory |

---

## License

Internal team tooling. Refer to your organization's policies for usage and distribution.
