#!/usr/bin/env python3
"""
OpenClaw Workspace Bootstrap Script

Run this on a new machine after cloning the repo to set up:
  1. ~/.openclaw/workspace-pm/   (PM Agent workspace)
  2. ~/.openclaw/workspace-ipm/  (IPM Agent workspace)
  3. ~/.openclaw/workspace-sa/   (SA Agent workspace)

Each workspace gets:
  - config/tasks-index.json  (task registry)
  - config/state.json        (execution state)
  - AGENTS.md, SOUL.md, IDENTITY.md, USER.md, TOOLS.md (bootstrap files)

Usage:
  cd <repo-root>
  python3 scripts/bootstrap_workspaces.py

Prerequisites:
  - Git repo cloned with all skill directories
  - Python 3.8+
"""

import json
import sys
from pathlib import Path
from datetime import date

TODAY = date.today().isoformat()

# Auto-detect repo root (script is in <repo>/scripts/)
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
OPENCLAW_ROOT = Path.home() / ".openclaw"


# ═══════════════════════════════════════════════════════════════
# TASK DEFINITIONS (must match generate_team.py)
# ═══════════════════════════════════════════════════════════════

PM_TASKS = [
    {"task_id": "PM-INC-001", "name": "Project Charter Development", "phase": "Inception", "wave": 1, "step": 1,
     "skill_dir": "pm-project-charter-development",
     "next": ["IPM-INC-001", "IPM-INC-002", "IPM-INC-003", "IPM-INC-004", "IPM-INC-005"],
     "description": "Drafting the project charter defining objectives, scope, stakeholders, constraints, and success criteria."},
    {"task_id": "PM-INC-002", "name": "Stakeholder Analysis", "phase": "Inception", "wave": 1, "step": 2,
     "skill_dir": "pm-stakeholder-analysis",
     "next": ["IPM-INC-001", "IPM-INC-002", "IPM-INC-003", "IPM-INC-004", "IPM-INC-005"],
     "description": "Identifying stakeholders, assessing their influence and interest, and developing a stakeholder engagement plan."},
    {"task_id": "PM-INC-003", "name": "Resource Planning", "phase": "Inception", "wave": 1, "step": 3,
     "skill_dir": "pm-resource-planning",
     "next": ["IPM-INC-001", "IPM-INC-002", "IPM-INC-003", "IPM-INC-004", "IPM-INC-005"],
     "description": "Estimating team composition, skillsets, and resource availability needed for project execution."},
    {"task_id": "PM-INC-004", "name": "Budget Estimation", "phase": "Inception", "wave": 1, "step": 4,
     "skill_dir": "pm-budget-estimation",
     "next": ["IPM-INC-001", "IPM-INC-002", "IPM-INC-003", "IPM-INC-004", "IPM-INC-005"],
     "description": "Developing initial cost estimates covering personnel, infrastructure, licensing, and contingency reserves."},
    {"task_id": "PM-INC-005", "name": "Risk Register Initialization", "phase": "Inception", "wave": 1, "step": 5,
     "skill_dir": "pm-risk-register-initialization",
     "next": ["IPM-INC-001", "IPM-INC-002", "IPM-INC-003", "IPM-INC-004", "IPM-INC-005"],
     "description": "Identifying early project risks, assessing probability and impact, and defining initial mitigation strategies."},
    {"task_id": "PM-REQ-001", "name": "Project Plan & WBS", "phase": "Requirements", "wave": 1, "step": 1,
     "skill_dir": "pm-project-plan-wbs",
     "next": ["IPM-REQ-001", "IPM-REQ-002", "IPM-REQ-003", "IPM-REQ-004", "IPM-REQ-005"],
     "description": "Creating the detailed project plan with Work Breakdown Structure, milestones, and critical path analysis."},
    {"task_id": "PM-REQ-002", "name": "Schedule Development", "phase": "Requirements", "wave": 1, "step": 2,
     "skill_dir": "pm-schedule-development",
     "next": ["IPM-REQ-001", "IPM-REQ-002", "IPM-REQ-003", "IPM-REQ-004", "IPM-REQ-005"],
     "description": "Building project timelines using Gantt charts, defining dependencies, and setting baseline schedules."},
    {"task_id": "PM-REQ-003", "name": "RACI Matrix Definition", "phase": "Requirements", "wave": 1, "step": 3,
     "skill_dir": "pm-raci-matrix-definition",
     "next": ["IPM-REQ-001", "IPM-REQ-002", "IPM-REQ-003", "IPM-REQ-004", "IPM-REQ-005"],
     "description": "Establishing clear roles and responsibilities across all workstreams using RACI."},
    {"task_id": "PM-REQ-004", "name": "Communication Plan", "phase": "Requirements", "wave": 1, "step": 4,
     "skill_dir": "pm-communication-plan",
     "next": ["IPM-REQ-001", "IPM-REQ-002", "IPM-REQ-003", "IPM-REQ-004", "IPM-REQ-005"],
     "description": "Defining reporting cadence, meeting schedules, escalation paths, and communication channels."},
    {"task_id": "PM-REQ-005", "name": "Vendor & Procurement Management", "phase": "Requirements", "wave": 1, "step": 5,
     "skill_dir": "pm-vendor-procurement-management",
     "next": ["IPM-REQ-001", "IPM-REQ-002", "IPM-REQ-003", "IPM-REQ-004", "IPM-REQ-005"],
     "description": "Coordinating vendor selection, contract negotiation, SOWs, and third-party onboarding."},
    {"task_id": "PM-DEV-001", "name": "Progress Tracking & Reporting", "phase": "Development", "wave": 1, "step": 1,
     "skill_dir": "pm-progress-tracking-reporting",
     "next": ["IPM-DEV-001", "IPM-DEV-002", "IPM-DEV-003", "IPM-DEV-004"],
     "description": "Monitoring project health through status reports, dashboards, earned value metrics."},
    {"task_id": "PM-DEV-002", "name": "Risk & Issue Management", "phase": "Development", "wave": 1, "step": 2,
     "skill_dir": "pm-risk-issue-management",
     "next": ["IPM-DEV-001", "IPM-DEV-002", "IPM-DEV-003", "IPM-DEV-004"],
     "description": "Continuously updating the risk register, managing issue logs, driving resolution."},
    {"task_id": "PM-DEV-003", "name": "Scope Management", "phase": "Development", "wave": 1, "step": 3,
     "skill_dir": "pm-scope-management",
     "next": ["IPM-DEV-001", "IPM-DEV-002", "IPM-DEV-003", "IPM-DEV-004"],
     "description": "Controlling scope through formal change request processes and impact assessments."},
    {"task_id": "PM-DEV-004", "name": "Resource Management", "phase": "Development", "wave": 1, "step": 4,
     "skill_dir": "pm-resource-management",
     "next": ["IPM-DEV-001", "IPM-DEV-002", "IPM-DEV-003", "IPM-DEV-004"],
     "description": "Balancing team workloads, resolving resource conflicts, adjusting allocations."},
    {"task_id": "PM-DEV-005", "name": "Stakeholder Communication", "phase": "Development", "wave": 1, "step": 5,
     "skill_dir": "pm-stakeholder-communication",
     "next": ["IPM-DEV-001", "IPM-DEV-002", "IPM-DEV-003", "IPM-DEV-004"],
     "description": "Conducting regular status meetings, steering committee updates, executive briefings."},
    {"task_id": "PM-QA-001", "name": "UAT Coordination", "phase": "QA", "wave": 1, "step": 1,
     "skill_dir": "pm-uat-coordination",
     "next": ["IPM-QA-001", "IPM-QA-002", "IPM-QA-003"],
     "description": "Planning UAT timelines, coordinating business user participation."},
    {"task_id": "PM-QA-002", "name": "Go/No-Go Decision Facilitation", "phase": "QA", "wave": 1, "step": 2,
     "skill_dir": "pm-go-no-go-decision-facilitation",
     "next": ["IPM-QA-001", "IPM-QA-002", "IPM-QA-003"],
     "description": "Organizing go/no-go review meetings with key stakeholders."},
    {"task_id": "PM-QA-003", "name": "Release Planning", "phase": "QA", "wave": 1, "step": 3,
     "skill_dir": "pm-release-planning",
     "next": ["IPM-QA-001", "IPM-QA-002", "IPM-QA-003"],
     "description": "Coordinating release schedules, deployment windows, rollback contingencies."},
    {"task_id": "PM-QA-004", "name": "Compliance & Audit Readiness", "phase": "QA", "wave": 1, "step": 4,
     "skill_dir": "pm-compliance-audit-readiness",
     "next": ["IPM-QA-001", "IPM-QA-002", "IPM-QA-003"],
     "description": "Ensuring all project documentation and approvals are complete for audit."},
    {"task_id": "PM-REL-001", "name": "Go-Live Coordination", "phase": "Release", "wave": 1, "step": 1,
     "skill_dir": "pm-go-live-coordination",
     "next": ["IPM-REL-001", "IPM-REL-002", "IPM-REL-003", "IPM-REL-004"],
     "description": "Orchestrating the production launch across all teams."},
    {"task_id": "PM-REL-002", "name": "Hypercare Management", "phase": "Release", "wave": 1, "step": 2,
     "skill_dir": "pm-hypercare-management",
     "next": ["IPM-REL-001", "IPM-REL-002", "IPM-REL-003", "IPM-REL-004"],
     "description": "Managing the post-launch support period."},
    {"task_id": "PM-REL-003", "name": "Project Closure", "phase": "Release", "wave": 1, "step": 3,
     "skill_dir": "pm-project-closure", "next": [],
     "description": "Conducting formal project closure."},
    {"task_id": "PM-REL-004", "name": "Lessons Learned & Retrospective", "phase": "Release", "wave": 1, "step": 4,
     "skill_dir": "pm-lessons-learned-retrospective", "next": [],
     "description": "Facilitating post-project retrospectives."},
    {"task_id": "PM-REL-005", "name": "Benefits Handover", "phase": "Release", "wave": 1, "step": 5,
     "skill_dir": "pm-benefits-handover", "next": [],
     "description": "Transitioning project deliverables to operations."},
]

IPM_TASKS = [
    {"task_id": "IPM-INC-001", "name": "Requirement Gathering", "phase": "Inception", "wave": 2, "step": 1,
     "skill_dir": "ipm-requirement-gathering",
     "next": ["SM-INC-001", "SM-INC-002", "SM-INC-003", "SM-INC-004", "SM-INC-005"],
     "description": "In-depth interviews with stakeholders/customers to collect raw requirements."},
    {"task_id": "IPM-INC-002", "name": "Market Research", "phase": "Inception", "wave": 2, "step": 2,
     "skill_dir": "ipm-market-research",
     "next": ["SM-INC-001", "SM-INC-002", "SM-INC-003", "SM-INC-004", "SM-INC-005"],
     "description": "Analyzing competitors, industry trends, and user pain points."},
    {"task_id": "IPM-INC-003", "name": "BRD Writing", "phase": "Inception", "wave": 2, "step": 3,
     "skill_dir": "ipm-brd-writing",
     "next": ["SM-INC-001", "SM-INC-002", "SM-INC-003", "SM-INC-004", "SM-INC-005"],
     "description": "Creating the Business Requirement Document."},
    {"task_id": "IPM-INC-004", "name": "Feasibility Assessment", "phase": "Inception", "wave": 2, "step": 4,
     "skill_dir": "ipm-feasibility-assessment",
     "next": ["SM-INC-001", "SM-INC-002", "SM-INC-003", "SM-INC-004", "SM-INC-005"],
     "description": "Collaborating with technical teams to evaluate technical viability."},
    {"task_id": "IPM-INC-005", "name": "Alignment", "phase": "Inception", "wave": 2, "step": 5,
     "skill_dir": "ipm-alignment",
     "next": ["SM-INC-001", "SM-INC-002", "SM-INC-003", "SM-INC-004", "SM-INC-005"],
     "description": "Achieving consensus among business, technical, and design stakeholders."},
    {"task_id": "IPM-REQ-001", "name": "PRD Writing", "phase": "Requirements", "wave": 2, "step": 1,
     "skill_dir": "ipm-prd-writing",
     "next": ["SM-REQ-001", "SM-REQ-002", "SM-REQ-003", "SM-REQ-004", "SM-REQ-005"],
     "description": "Creating the Product Requirement Document."},
    {"task_id": "IPM-REQ-002", "name": "User Story Decomposition", "phase": "Requirements", "wave": 2, "step": 2,
     "skill_dir": "ipm-user-story-decomposition",
     "next": ["SM-REQ-001", "SM-REQ-002", "SM-REQ-003", "SM-REQ-004", "SM-REQ-005"],
     "description": "Breaking down large requirements into deliverable User Stories."},
    {"task_id": "IPM-REQ-003", "name": "Prioritization", "phase": "Requirements", "wave": 2, "step": 3,
     "skill_dir": "ipm-prioritization",
     "next": ["SM-REQ-001", "SM-REQ-002", "SM-REQ-003", "SM-REQ-004", "SM-REQ-005"],
     "description": "Ranking requirements using MoSCoW or RICE frameworks."},
    {"task_id": "IPM-REQ-004", "name": "Prototype Review", "phase": "Requirements", "wave": 2, "step": 4,
     "skill_dir": "ipm-prototype-review",
     "next": ["SM-REQ-001", "SM-REQ-002", "SM-REQ-003", "SM-REQ-004", "SM-REQ-005"],
     "description": "Collaborating with designers to finalize UI/UX solutions."},
    {"task_id": "IPM-REQ-005", "name": "Refinement Meetings", "phase": "Requirements", "wave": 2, "step": 5,
     "skill_dir": "ipm-refinement-meetings",
     "next": ["SM-REQ-001", "SM-REQ-002", "SM-REQ-003", "SM-REQ-004", "SM-REQ-005"],
     "description": "Organizing requirement reviews for shared understanding."},
    {"task_id": "IPM-DEV-001", "name": "Requirement Clarification", "phase": "Development", "wave": 2, "step": 1,
     "skill_dir": "ipm-requirement-clarification",
     "next": ["SM-DEV-001", "SM-DEV-002", "SM-DEV-003", "SM-DEV-004"],
     "description": "Responding to developer and tester queries in real-time."},
    {"task_id": "IPM-DEV-002", "name": "Acceptance Criteria", "phase": "Development", "wave": 2, "step": 2,
     "skill_dir": "ipm-acceptance-criteria",
     "next": ["SM-DEV-001", "SM-DEV-002", "SM-DEV-003", "SM-DEV-004"],
     "description": "Defining specific conditions for each feature."},
    {"task_id": "IPM-DEV-003", "name": "PRD Change Management", "phase": "Development", "wave": 2, "step": 3,
     "skill_dir": "ipm-prd-change-management",
     "next": ["SM-DEV-001", "SM-DEV-002", "SM-DEV-003", "SM-DEV-004"],
     "description": "Managing requirement changes and assessing impact."},
    {"task_id": "IPM-DEV-004", "name": "Progress Tracking", "phase": "Development", "wave": 2, "step": 4,
     "skill_dir": "ipm-progress-tracking",
     "next": ["SM-DEV-001", "SM-DEV-002", "SM-DEV-003", "SM-DEV-004"],
     "description": "Monitoring delivery timelines and identifying risks."},
    {"task_id": "IPM-QA-001", "name": "UAT Organization", "phase": "QA", "wave": 2, "step": 1,
     "skill_dir": "ipm-uat-organization",
     "next": ["SM-QA-001", "SM-QA-002", "SM-QA-003"],
     "description": "Coordinating User Acceptance Testing."},
    {"task_id": "IPM-QA-002", "name": "Bug Prioritization", "phase": "QA", "wave": 2, "step": 2,
     "skill_dir": "ipm-bug-prioritization",
     "next": ["SM-QA-001", "SM-QA-002", "SM-QA-003"],
     "description": "Deciding which bugs are critical and block release."},
    {"task_id": "IPM-QA-003", "name": "Launch Checklist", "phase": "QA", "wave": 2, "step": 3,
     "skill_dir": "ipm-launch-checklist",
     "next": ["SM-QA-001", "SM-QA-002", "SM-QA-003"],
     "description": "Confirming release standards (Definition of Done)."},
    {"task_id": "IPM-REL-001", "name": "Release Coordination", "phase": "Release", "wave": 2, "step": 1,
     "skill_dir": "ipm-release-coordination",
     "next": ["SM-REL-001", "SM-REL-002", "SM-REL-003", "SM-REL-004"],
     "description": "Planning release schedules and rollback strategies."},
    {"task_id": "IPM-REL-002", "name": "Data Analysis", "phase": "Release", "wave": 2, "step": 2,
     "skill_dir": "ipm-data-analysis",
     "next": ["SM-REL-001", "SM-REL-002", "SM-REL-003", "SM-REL-004"],
     "description": "Analyzing KPIs after launch."},
    {"task_id": "IPM-REL-003", "name": "User Feedback", "phase": "Release", "wave": 2, "step": 3,
     "skill_dir": "ipm-user-feedback",
     "next": ["SM-REL-001", "SM-REL-002", "SM-REL-003", "SM-REL-004"],
     "description": "Collecting continuous feedback for next iteration."},
    {"task_id": "IPM-REL-004", "name": "Retrospectives", "phase": "Release", "wave": 2, "step": 4,
     "skill_dir": "ipm-retrospectives", "next": [],
     "description": "Organizing project/sprint retrospectives."},
]

# SA tasks from system-architect-agent/config/tasks-index.json (already in repo)
# We read it at runtime rather than duplicating here.


# ═══════════════════════════════════════════════════════════════
# BOOTSTRAP FILE GENERATORS
# ═══════════════════════════════════════════════════════════════

def gen_agents_md(role_name, role_code):
    agent_type = "Orchestrator" if role_code == "PM" else "Role Agent"
    return f"""# AGENTS.md — {role_name} Agent Workspace

## Agent Identity

| Field | Value |
|:---|:---|
| Role | {role_name} |
| Type | {agent_type} |
| Status | Active |

## Operating Instructions

1. Listen for TaskTriggered events from PM Agent
2. Check DoR prerequisites before starting
3. Execute skill Phase 0-5 in strict order
4. Self-check against DoD criteria
5. Invoke supervisor for independent quality review
6. Report TaskCompleted to PM Agent (only after supervisor 100% pass)

## Mandatory Rules

- No phase may be skipped
- All DoD quality gates must pass
- Supervisor must achieve 100% pass rate
- All actions logged in work-log.md and conversation-log.md
"""


def gen_soul_md(role_name):
    return f"""# SOUL.md — {role_name} Agent Persona

You are a {role_name} agent in an OpenClaw multi-agent team.

## Boundaries

- PM is your sole orchestrator. Only act on TaskTriggered events from PM.
- Follow your skill instructions exactly. No phase skipping.
- Always run self-check and supervisor before reporting TaskCompleted.
- Maintain professional, precise communication.
- Document all decisions with rationale.
- When uncertain, research first, then ask the user.

## Communication Style

- Clear, structured, and actionable
- Use tables and lists for clarity
- Cite sources for all research findings
- Present options with trade-offs when multiple approaches exist
"""


def gen_identity_md(role_name, emoji):
    return f"""# IDENTITY.md — {role_name} Agent

- **Name**: {role_name} Agent
- **Emoji**: {emoji}
- **Role**: {role_name}
- **Team**: OpenClaw AI Agent Team
"""


USER_MD = """# USER.md — Team Context

## Team Structure

- **PM Agent**: Project Manager (Orchestrator)
- **IPM Agent**: IT Product Manager (Role Agent)
- **SA Agent**: System Architect (Role Agent)
- **TL Agent**: Technical Lead (Role Agent)

## Communication Protocol

- All task assignments flow from PM Agent
- All task completions report to PM Agent
- Supervisor reviews are independent quality gates
"""

TOOLS_MD = """# TOOLS.md — Tool Usage Conventions

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
"""


def create_tasks_index(tasks, role_name, agent_name):
    entries = []
    for t in tasks:
        entries.append({
            "task_id": t["task_id"],
            "name": t["name"],
            "phase": t["phase"],
            "wave": t["wave"],
            "step": t["step"],
            "next": t["next"],
            "skill_dir": t["skill_dir"],
            "supervisor_dir": f"{t['skill_dir']}-supervisor",
            "description": t["description"]
        })
    return json.dumps({
        "metadata": {
            "role": role_name,
            "agent": agent_name,
            "source": "task/delivery_playbook.md",
            "generated_at": TODAY
        },
        "tasks": entries
    }, indent=2)


# ═══════════════════════════════════════════════════════════════
# WORKSPACE SETUP
# ═══════════════════════════════════════════════════════════════

def write_file(path, content):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")


def setup_workspace(workspace_code, role_name, role_code, emoji, tasks, agent_name):
    ws = OPENCLAW_ROOT / f"workspace-{workspace_code}"
    count = 0

    if ws.exists():
        print(f"  [SKIP] {ws} already exists. Use --force to overwrite.")
        return 0

    print(f"  Creating {ws}/")

    # Config
    write_file(ws / "config" / "tasks-index.json", create_tasks_index(tasks, role_name, agent_name))
    count += 1
    write_file(ws / "config" / "state.json", json.dumps({"tasks": {}, "last_updated": TODAY}, indent=2))
    count += 1

    # Bootstrap files
    write_file(ws / "AGENTS.md", gen_agents_md(role_name, role_code))
    write_file(ws / "SOUL.md", gen_soul_md(role_name))
    write_file(ws / "IDENTITY.md", gen_identity_md(role_name, emoji))
    write_file(ws / "USER.md", USER_MD)
    write_file(ws / "TOOLS.md", TOOLS_MD)
    count += 5

    print(f"    config/tasks-index.json ({len(tasks)} tasks)")
    print(f"    config/state.json")
    print(f"    AGENTS.md, SOUL.md, IDENTITY.md, USER.md, TOOLS.md")
    print(f"    Total: {count} files")
    return count


def setup_sa_workspace():
    """SA workspace — reads tasks-index.json from the repo."""
    ws = OPENCLAW_ROOT / "workspace-sa"
    count = 0

    if ws.exists():
        print(f"  [SKIP] {ws} already exists. Use --force to overwrite.")
        return 0

    print(f"  Creating {ws}/")

    # Copy tasks-index.json from repo
    sa_tasks_file = REPO_ROOT / "system-architect-agent" / "config" / "tasks-index.json"
    if sa_tasks_file.exists():
        content = sa_tasks_file.read_text(encoding="utf-8")
        write_file(ws / "config" / "tasks-index.json", content)
        count += 1
        tasks_data = json.loads(content)
        task_count = len(tasks_data.get("tasks", []))
        print(f"    config/tasks-index.json ({task_count} tasks, copied from repo)")
    else:
        print(f"    [WARN] {sa_tasks_file} not found — skipping tasks-index.json")

    write_file(ws / "config" / "state.json", json.dumps({"tasks": {}, "last_updated": TODAY}, indent=2))
    count += 1

    # Bootstrap files
    write_file(ws / "AGENTS.md", gen_agents_md("System Architect", "SA"))
    write_file(ws / "SOUL.md", gen_soul_md("System Architect"))
    write_file(ws / "IDENTITY.md", gen_identity_md("System Architect", "🏗️"))
    write_file(ws / "USER.md", USER_MD)
    write_file(ws / "TOOLS.md", TOOLS_MD)
    count += 5

    print(f"    config/state.json")
    print(f"    AGENTS.md, SOUL.md, IDENTITY.md, USER.md, TOOLS.md")
    print(f"    Total: {count} files")
    return count


def verify_repo():
    """Check that the repo has the expected structure."""
    errors = []

    # Check config exists
    if not (REPO_ROOT / "config" / "agents-registry.json").exists():
        errors.append("config/agents-registry.json missing")
    if not (REPO_ROOT / "config" / "openclaw.json").exists():
        errors.append("config/openclaw.json missing")

    # Check a sample of skill dirs
    samples = ["pm-project-charter-development", "ipm-brd-writing", "sa-architecture-design"]
    for s in samples:
        if not (REPO_ROOT / s / "SKILL.md").exists():
            errors.append(f"{s}/SKILL.md missing")

    # Check shared bootstrap files
    for f in ["AGENTS.md", "SOUL.md", "IDENTITY.md", "USER.md", "TOOLS.md"]:
        if not (REPO_ROOT / f).exists():
            errors.append(f"{f} missing")

    return errors


def main():
    force = "--force" in sys.argv

    print("=" * 60)
    print("  OpenClaw Workspace Bootstrap")
    print("=" * 60)
    print(f"\n  Repo root:  {REPO_ROOT}")
    print(f"  Target:     {OPENCLAW_ROOT}/workspace-{{pm,ipm,sa}}/\n")

    # Verify repo
    print("  Verifying repo structure...")
    errors = verify_repo()
    if errors:
        print("\n  [ERROR] Repo verification failed:")
        for e in errors:
            print(f"    - {e}")
        print("\n  Make sure you've cloned the complete repo first.")
        sys.exit(1)
    print("  Repo structure OK\n")

    if force:
        # Remove existing workspaces
        import shutil
        for ws in ["workspace-pm", "workspace-ipm", "workspace-sa"]:
            p = OPENCLAW_ROOT / ws
            if p.exists():
                shutil.rmtree(p)
                print(f"  [FORCE] Removed {p}")

    total = 0

    # PM workspace
    total += setup_workspace("pm", "IT Project Manager", "PM", "📊", PM_TASKS, "PM Agent")

    # IPM workspace
    total += setup_workspace("ipm", "IT Product Manager", "IPM", "📋", IPM_TASKS, "IPM Agent")

    # SA workspace
    total += setup_sa_workspace()

    print(f"\n{'=' * 60}")
    print(f"  Bootstrap complete: {total} files created")
    print(f"{'=' * 60}")

    if total == 0:
        print("\n  All workspaces already exist. Use --force to recreate.")
    else:
        print(f"\n  Workspaces ready at:")
        print(f"    ~/.openclaw/workspace-pm/")
        print(f"    ~/.openclaw/workspace-ipm/")
        print(f"    ~/.openclaw/workspace-sa/")
        print(f"\n  Next steps:")
        print(f"    1. Verify with: ls ~/.openclaw/workspace-*/config/")
        print(f"    2. Skills are already in the repo — no additional setup needed")
        print(f"    3. Start the team by triggering PM Agent")


if __name__ == "__main__":
    main()
