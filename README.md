<p align="center">
  <strong>English</strong> |
  <a href="README.zh-CN.md">中文</a> |
  <a href="README.ar.md">العربية</a> |
  <a href="README.ja.md">日本語</a> |
  <a href="README.de.md">Deutsch</a>
</p>

# Ramadan AI AI Agent Team

**Automated end-to-end IT project delivery through specialized, orchestrated AI agents.**

Ramadan AI transforms the software delivery lifecycle into a system of composable AI Agent Skills. Each task in the project lifecycle — from project chartering to post-release retrospectives — is codified as a structured skill with its own SOP, Definition of Ready (DoR), Definition of Done (DoD), RACI matrix, and tooling references. A multi-agent team executes these skills under orchestration, producing auditable, quality-gated deliverables at every stage.

---

## Table of Contents

- [Motivation](#motivation)
- [Core Concepts](#core-concepts)
- [Agent Team](#agent-team)
- [Skill Anatomy](#skill-anatomy)
- [Delivery Playbook](#delivery-playbook)
- [Execution Model](#execution-model)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Deep Dive: Project Structure Scan & Agent Memory](#deep-dive-project-structure-scan--agent-memory)
- [Contributing](#contributing)
- [License](#license)

---

## Motivation

Enterprise IT projects follow well-established lifecycle phases — Inception, Requirements, Development, QA, and Release — yet the operational knowledge for each task typically lives in scattered wikis, tribal knowledge, or ad-hoc checklists. Ramadan AI addresses this by:

1. **Decomposing the delivery lifecycle** into discrete, well-defined tasks across all phases.
2. **Encoding each task as an AI Agent Skill** with formal quality dimensions (SOP, DoR, DoD, RACI, Tools).
3. **Orchestrating skill execution** through an event-driven multi-agent architecture with built-in supervisor quality gates.

The result is a reproducible, inspectable, and continuously improvable delivery system powered by AI agents.

---

## Core Concepts

### Skill-per-Task Model

Every task in the software delivery lifecycle maps to exactly one AI Agent Skill. A skill is not a generic prompt — it is a structured execution unit containing:

| Dimension | Purpose | Example |
|:---|:---|:---|
| **SOP** | Step-by-step operating procedure (Phases 0–5) | How to conduct a technical discovery assessment |
| **DoR** | Prerequisites that must be satisfied before execution begins | Scope defined, stakeholders identified, tools available |
| **DoD** | Quality checklist that must pass before the task is marked complete | 19-point checklist covering deliverables, process, and documentation |
| **RACI** | Responsibility assignment for all stakeholders | SA = Responsible, PM = Accountable, TL = Consulted |
| **Tools** | Tool references and usage guidance | WebSearch, file operations, diagram generators |
| **Triggers** | Conditions that activate the skill | Upstream task completion, PM directive |
| **Output Templates** | Standardized deliverable formats | Report structure, decision log format |

### Supervisor Quality Gates

Every main skill has a paired **supervisor skill** that performs independent quality inspection. A task is not considered complete until the supervisor achieves a 100% pass rate on all inspection criteria. Failed items trigger automatic remediation and re-inspection.

### Event-Driven Orchestration

Agents communicate through a structured event protocol:

```
PM broadcasts TaskTriggered → Role Agent executes skill → Self-check DoD
  → Supervisor inspects → 100% pass → TaskCompleted reported to PM
  → PM triggers downstream tasks
```

---

## Agent Team

Ramadan AI operates as a four-agent team, each with a distinct role and skill portfolio:

| Agent | Role | Type | Skills | Coverage |
|:---|:---|:---|:---:|:---|
| **PM Agent** | Project Manager | Orchestrator | 24 | Charter, stakeholder analysis, resource planning, risk management, release coordination, project closure |
| **IPM Agent** | IT Product Manager | Role Agent | 21 | Requirement gathering, BRD/PRD writing, user stories, acceptance criteria, UAT, launch coordination |
| **SA Agent** | System Architect | Role Agent | 37 | Technical discovery, architecture design, NFRs, integration design, security review, deployment architecture |
| **TL Agent** | Technical Lead | Role Agent | 24 | Technical vision, solution design, code review leadership, development standards, technical risk assessment |

Each main skill has a paired supervisor, bringing the total to **212 skill directories** (106 main + 106 supervisors).

---

## Skill Anatomy

Every skill follows a standardized directory structure:

```
{role}-{skill-name}/
├── SKILL.md                        # Skill definition with Phase 0-5 workflow
└── references/
    ├── sop.md                      # Standard Operating Procedure
    ├── dor.md                      # Definition of Ready
    ├── dod.md                      # Definition of Done
    ├── raci.md                     # RACI matrix
    ├── tools.md                    # Tool usage reference
    ├── triggers.md                 # Activation conditions
    ├── output-templates.md         # Deliverable templates
    └── skills-and-knowledge.md     # Required competencies
```

Supervisor skills add an `inspection-criteria.md` file and a `scripts/verify_dod.py` automated verification script.

### Universal Phase 0–5 Workflow

Every skill executes the same six-phase workflow to ensure consistency:

| Phase | Name | Purpose |
|:---:|:---|:---|
| 0 | Initialization | Create output directory, initialize logs, verify DoR |
| 1 | Understand Task Purpose | Clarify objectives through dialogue, obtain user confirmation |
| 2 | Understand the Topic | Deep-dive into domain context, gather background information |
| 3 | Research & Q&A | Industry research, iterative question generation, expert consultation |
| 4 | Execute & Deliver | Produce deliverables using templates, self-check against DoD |
| 5 | Completion & Handoff | Invoke supervisor, remediate failures, report to PM |

---

## Delivery Playbook

The [`delivery_playbook.md`](task/delivery_playbook.md) defines the complete task execution order across five project phases, organized into sequential waves:

### Phases and Task Distribution

| Phase | Description | Key Activities |
|:---|:---|:---|
| **Inception** | Project initiation and feasibility | Charter development, stakeholder analysis, requirement gathering, technology selection, risk identification |
| **Requirements** | Detailed specification and design | Architecture design, NFR definition, integration design, data architecture, PRD writing, technical standards |
| **Development** | Implementation and technical guidance | Code/design reviews, spike/PoC leadership, technical debt management, ADR documentation |
| **QA** | Validation and compliance | Performance testing, security review, compliance validation, infrastructure validation, UAT coordination |
| **Release** | Deployment and stabilization | Deployment architecture, monitoring setup, capacity planning, go-live coordination, hypercare, retrospectives |

### Wave Execution Model

Tasks within a wave execute in parallel. All tasks in Wave N must complete before Wave N+1 begins. This enables maximum parallelism while respecting task dependencies.

---

## Execution Model

### Event Protocol

| Event | Direction | Payload |
|:---|:---|:---|
| `TaskTriggered` | PM → Role Agent | `{ task_id, skill_dir, inputs, context }` |
| `TaskCompleted` | Role Agent → PM | `{ task_id, status, artifacts, supervisor_report }` |
| `SupervisorTriggered` | Role Agent → Supervisor | `{ task_id, output_dir }` |
| `SupervisorCompleted` | Supervisor → Role Agent | `{ task_id, pass_rate, report, remediation_items }` |

### Quality Assurance Flow

```
Role Agent completes skill execution
       │
       ▼
Self-check: Verify all 19 DoD items
       │
       ├── FAIL → Auto-remediate, re-verify
       │
       ▼
Invoke paired Supervisor skill
       │
       ├── FAIL → Receive remediation report, fix, re-invoke supervisor
       │
       ▼
100% pass rate achieved → Report TaskCompleted to PM
```

### Idempotence

All task execution is idempotent. The system tracks task state (`PENDING`, `IN_PROGRESS`, `DONE`, `FAILED`) and resumes or skips appropriately, preventing duplicate work and enabling reliable recovery.

---

## Project Structure

```
ramadan/
├── IDENTITY.md                     # Team identity definition
├── SOUL.md                         # Team persona and operational boundaries
├── AGENTS.md                       # Agent registry and event protocol
├── USER.md                         # User interaction model
├── TOOLS.md                        # Tool usage conventions
│
├── config/
│   ├── agents-registry.json        # Agent definitions and metadata
│   ├── openclaw.json               # Skill bindings, tool profiles, event bus config
│   └── event-bus.json              # Event routing rules
│
├── pm-*/                           # 24 PM skills + 24 supervisors
├── ipm-*/                          # 21 IPM skills + 21 supervisors
├── sa-*/                           # 37 SA skills + 37 supervisors
├── tl-*/                           # TL skills + supervisors
│
├── task/
│   ├── delivery_playbook.md        # Complete task execution order
│   └── *_agent_skill_definition.md # Task-level skill specifications
│
├── prompt/
│   ├── generate_team.py            # Team scaffolding generator
│   └── openclaw-skill-creator-prompt.md  # Skill creation guide
│
├── openclaw-team/                  # Deployable team package
│   ├── skills/                     # All skills consolidated
│   ├── workspaces/                 # Agent workspace templates
│   ├── scripts/
│   │   ├── install_team.py         # One-click installer
│   │   ├── quick_validate.py       # Structure validator
│   │   ├── init_skill.py           # New skill scaffolder
│   │   └── package_skill.py        # Skill packager
│   └── config/                     # Deployment configuration
│
└── scripts/
    ├── install_team.py             # Team deployment script
    ├── bootstrap_workspaces.py     # Workspace initializer
    └── package_team.py             # Distribution packager
```

---

## Getting Started

### Prerequisites

- Python 3.8+
- Claude Code CLI with Claude Opus 4.6 model access
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ramadan
   ```

2. **Install the team package**
   ```bash
   python scripts/install_team.py
   ```

3. **Bootstrap agent workspaces**
   ```bash
   python scripts/bootstrap_workspaces.py
   ```

4. **Validate skill structure**
   ```bash
   python openclaw-team/scripts/quick_validate.py
   ```

### Creating a New Skill

Use the skill scaffolding tool to generate a new skill with all required reference files:

```bash
python openclaw-team/scripts/init_skill.py --role sa --name my-new-skill
```

This creates the full directory structure with template files for SOP, DoR, DoD, RACI, tools, triggers, and output templates.

---

## Deep Dive: Project Structure Scan & Agent Memory

The **Project Structure Scan** skill (`project-structure-scan`) is the most architecturally advanced skill in Ramadan AI. It serves as the reference implementation for a key capability that most AI agent skills lack: **persistent, structured memory that survives across sessions and transfers knowledge across projects**.

### The Problem: Stateless AI Agents

By default, AI agents are stateless. Every conversation starts from zero. When an agent scans a codebase today and the user returns next week to scan the same project, the agent has no recollection of previous findings, no awareness of what changed, and no ability to skip redundant work. This leads to:

- Repeated analysis of unchanged code
- Re-asking questions the user has already answered
- No ability to track how a project evolves over time
- No cross-project learning (insights from Project A never benefit Project B)

The Project Structure Scan skill solves this with a **SQLite-backed memory system** that makes the agent progressively smarter with each invocation.

### Memory Architecture

The memory system uses a local SQLite database (`memory/agent_memory.db`) with four purpose-built tables:

```
┌─────────────────────────────────────────────────────────────┐
│                    agent_memory.db                           │
│                                                             │
│  ┌─────────────┐  ┌──────────────┐  ┌───────────────────┐  │
│  │ task_memory  │  │ knowledge    │  │   scan_history    │  │
│  │             │  │ _base        │  │                   │  │
│  │ findings    │  │              │  │ session tracking  │  │
│  │ decisions   │  │ patterns     │  │ scope & status    │  │
│  │ lessons     │  │ dependencies │  │ deliverables path │  │
│  │ questions   │  │ tech_stack   │  │ timestamps        │  │
│  │ risks       │  │ conventions  │  │                   │  │
│  │             │  │ insights     │  │                   │  │
│  │ (per phase, │  │              │  │                   │  │
│  │  per session)│  │ (confidence  │  │                   │  │
│  │             │  │  scored,     │  │                   │  │
│  │             │  │  cross-      │  │                   │  │
│  │             │  │  project)    │  │                   │  │
│  └─────────────┘  └──────────────┘  └───────────────────┘  │
│                                                             │
│  ┌─────────────┐                                            │
│  │ dod_checks  │    Supplementary Files:                    │
│  │             │    ├── logs/conversation-log.md             │
│  │ per-round   │    ├── logs/work-log.md                    │
│  │ pass/fail   │    ├── research/{topic}.md                 │
│  │ evidence    │    └── phase{N}-questions.md                │
│  └─────────────┘                                            │
└─────────────────────────────────────────────────────────────┘
```

| Table | Purpose | Key Fields |
|:---|:---|:---|
| `task_memory` | Per-session findings, decisions, lessons, Q&A, and risks | `session_id`, `phase`, `memory_type`, `content`, `tags` |
| `knowledge_base` | Cross-session reusable knowledge with confidence scores | `category`, `key`, `value`, `confidence` (0.0–1.0) |
| `scan_history` | Audit trail of every scan execution | `project_name`, `scan_scope`, `status`, `deliverables_path` |
| `dod_checks` | Quality gate verification results per round | `check_round`, `check_item`, `status`, `evidence` |

### How Memory Integrates with Each Workflow Phase

The memory system is not a bolt-on feature — it is woven into every phase of the skill's execution:

**Phase 0 — Memory-Driven Initialization**

On startup, the agent queries `scan_history` to determine whether this project has been scanned before. This single query determines the entire execution path:

```
load_project_history(project_name)
  │
  ├── Previous scans found → Re-scan Mode
  │   └── generate_memory_summary() → present to user
  │       └── User chooses: Incremental / Full re-scan / Review previous
  │
  ├── No history, but similar projects exist → Hypothesis Mode
  │   └── get_similar_projects(tech_stack_tags)
  │       └── "Project X used DDD with Hexagonal. Look for similar patterns?"
  │
  └── No history, no similar projects → Fresh Scan Mode
```

Before any work begins, the agent also runs maintenance operations: `apply_confidence_decay()` reduces the confidence score of knowledge entries not updated in 90 days, and `prune_low_confidence()` removes entries that have decayed below a 0.3 threshold.

**Phase 1 — Memory-Enhanced Purpose Understanding**

Instead of asking the user "Why do you need this scan?" from scratch every time, the agent queries previous purpose records:

```python
load_lessons_learned(task_id='SA-DISC-001', project_name=...) # filtered by phase='phase1'
```

If records exist, it presents: *"Last time we scanned this project, the purpose was: {previous_purpose}. Is the purpose the same this time?"* — reducing a 5-minute dialogue to a single confirmation.

**Phase 2 — Memory-Accelerated Discovery**

The agent queries `knowledge_base` for previously recorded tech stack, patterns, and conventions:

```python
load_project_knowledge(project_name)  # returns entries sorted by confidence DESC
```

Known answers are pre-filled. Only delta questions — things that are unknown or may have changed — are asked. On re-scans, this eliminates 60–80% of the questions.

**Phase 3 — Memory-Informed Research**

Previous research files and risk records are loaded. The agent skips redundant research, focuses on gaps, and proactively revisits known risks: *"Last time I identified these risks: {list}. Should I verify if they've been resolved?"*

**Phase 4 — Memory-Optimized Execution**

For incremental scans, the agent loads the previous `OUT-01` (Project Structure Tree), diffs it against the current directory structure, and only deep-scans changed areas. Previous `OUT-04` (Package Dependency Map) is compared against the current manifest to produce a change-only dependency report. This reduces execution time by 40–70% on re-scans.

### Cross-Project Knowledge Transfer

The most powerful memory feature operates across project boundaries. When the agent encounters a new project, it searches the knowledge base for projects with similar tech stacks:

```python
get_similar_projects(db_path, tech_stack_tags=["spring-boot", "postgresql", "redis"])
# Returns: [{"project_name": "ProjectX", "matching_tags": [...], "match_count": 3}]
```

High-confidence patterns from similar projects become hypotheses for the new project. If the agent has previously identified that three Spring Boot projects all use a Hexagonal architecture pattern, it can proactively ask: *"Similar projects in my records use Hexagonal architecture. Should I look for that pattern here?"* — accelerating first-scan analysis by approximately 30%.

### Confidence Decay & Contradiction Detection

Knowledge does not remain valid forever. The memory system implements two mechanisms to maintain integrity:

1. **Confidence Decay**: Every 90 days, entries that have not been updated lose 0.2 confidence points (minimum 0.0). An entry recorded at 0.8 confidence will decay to 0.6 → 0.4 → 0.2 → 0.0 over successive periods if never re-confirmed. Entries below 0.3 are pruned and reported to the user.

2. **Contradiction Detection**: Before writing a new knowledge entry, the agent checks for conflicts:

   ```python
   contradiction = detect_contradictions(db_path, project_name, category, key, new_value)
   # Returns existing vs. new value if they differ
   ```

   When a contradiction is found (e.g., the architecture pattern was previously recorded as "MVC" but new evidence suggests "Hexagonal"), the agent flags the conflict and asks the user to resolve it — rather than silently overwriting.

### Memory Operations API

All memory operations are implemented in `scripts/memory_ops.py` as pure functions with explicit database path parameters:

| Operation | Function | When Used |
|:---|:---|:---|
| Load scan history | `load_project_history()` | Phase 0 — determine scan mode |
| Load knowledge | `load_project_knowledge()` | Phases 1–4 — pre-fill known answers |
| Load lessons | `load_lessons_learned()` | Phases 1–3 — skip redundant work |
| Find similar projects | `get_similar_projects()` | Phase 0 — cross-project transfer |
| Generate summary | `generate_memory_summary()` | Phase 0 — present history to user |
| Record finding | `record_finding()` | Phase 4 — persist scan results |
| Record decision | `record_decision()` | Phases 1–3 — persist confirmed decisions |
| Record risk | `record_risk()` | Phases 3–4 — persist identified risks |
| Record knowledge | `record_knowledge()` | All phases — UPSERT to knowledge base |
| Record lesson | `record_lesson()` | Phase 5 — capture session insights |
| Start/complete scan | `start_scan()` / `complete_scan()` | Phases 0/5 — scan lifecycle |
| Record DoD check | `record_dod_check()` | Phase 4 — quality gate results |
| Apply decay | `apply_confidence_decay()` | Phase 0 — maintain freshness |
| Detect contradictions | `detect_contradictions()` | Before any knowledge write |
| Prune low confidence | `prune_low_confidence()` | Phase 0 — remove stale entries |

### Skill Directory Structure

The Project Structure Scan skill extends the standard skill anatomy with dedicated memory, research, and template directories:

```
project-structure-scan/
├── SKILL.md                          # Skill definition (memory-enhanced Phase 0-5)
├── memory/
│   ├── index.md                      # Memory architecture documentation
│   └── agent_memory.db               # SQLite database (created at runtime)
├── config/
│   ├── triggers.md                   # Project Intake Checklist (7 items)
│   ├── raci.md                       # RACI matrix with downstream triggers
│   ├── tools.md                      # Tool usage reference
│   ├── mcp-tools.md                  # MCP tool configurations
│   └── skills-and-knowledge.md       # Required agent competencies
├── references/
│   ├── sop.md                        # Standard Operating Procedure
│   ├── dor.md                        # Definition of Ready
│   ├── dod.md                        # Definition of Done
│   └── output-templates.md           # Template index
├── templates/
│   ├── structure-tree-template.md    # OUT-01 template
│   ├── module-relationship-template.md # OUT-02 template
│   ├── layering-analysis-template.md # OUT-03 template
│   ├── dependency-map-template.md    # OUT-04 template
│   ├── module-summary-template.md    # OUT-05 template
│   └── scan-report-template.md       # OUT-06 template
├── scripts/
│   ├── init_memory.py                # Database schema initialization
│   ├── memory_ops.py                 # Memory CRUD operations library
│   └── verify_dod.py                 # Automated DoD verification
├── research/                         # Research artifacts (populated at runtime)
├── logs/                             # Execution logs (populated at runtime)
└── diagrams/                         # Generated diagrams (populated at runtime)
```

### Design Principles

The memory architecture follows several deliberate design choices:

1. **SQLite over cloud storage**: Memory is local, portable, and requires zero infrastructure. The database file can be committed to the repository or shared between team members.

2. **Confidence scoring over binary truth**: Knowledge is not simply "known" or "unknown" — it carries a confidence score that degrades over time, reflecting the reality that software projects evolve and yesterday's truths may not hold today.

3. **UPSERT semantics**: `record_knowledge()` performs an upsert — if the same `(project_name, category, key)` tuple already exists, the value and confidence are updated rather than creating a duplicate entry.

4. **Separation of task memory and knowledge**: `task_memory` is session-scoped and captures the raw Q&A, decisions, and findings of a single execution. `knowledge_base` is project-scoped and captures distilled, reusable knowledge that persists across sessions.

5. **WAL journal mode**: The database uses Write-Ahead Logging for better concurrency, allowing reads during writes without blocking.

---

## Contributing

### Adding Skills

1. Define the task in `task/` as an agent skill definition document.
2. Map the task to a delivery phase and wave in the playbook.
3. Scaffold the skill using `init_skill.py`.
4. Populate all reference files (SOP, DoR, DoD, RACI, tools, triggers, output templates).
5. Create the paired supervisor skill with inspection criteria.
6. Register the skill in `config/openclaw.json`.
7. Validate with `quick_validate.py`.

### Skill Quality Standards

Every skill must include:
- A complete Phase 0–5 SOP with no skipped phases
- A DoR checklist with verifiable prerequisites
- A DoD checklist with 19 quality gate items
- A RACI matrix assigning all relevant stakeholders
- Output templates for all deliverables
- A paired supervisor skill with inspection criteria

---

## License

This project is proprietary. All rights reserved.
