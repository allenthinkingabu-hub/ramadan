#!/usr/bin/env python3
"""
Add an agent to an existing OpenClaw team.

Usage:
    add_agent.py <team-path> --role-id <id> --name <name> --description <desc> [options]

Options:
    --model <model>          LLM model override
    --depends-on <ids>       Comma-separated role IDs this agent depends on
    --tools-allow <tools>    Comma-separated allowed tools
    --tools-deny <tools>     Comma-separated denied tools

Examples:
    add_agent.py ~/.openclaw/teams/my-team --role-id pm --name "Product Manager" --description "Manages requirements"
    add_agent.py ./teams/dev-team --role-id backend --name "Backend Dev" --description "API development" --depends-on pm
"""

import json
import sys
from pathlib import Path
from datetime import datetime


SOUL_MD_TEMPLATE = """# {name}

## Identity
{description}

## Personality
- Professional and focused on the task at hand
- Communicates clearly and concisely
- Proactively flags risks and blockers

## Boundaries
- Stay within the scope of assigned tasks
- Do not modify files outside the project workspace without approval
- Escalate decisions that affect other team members

## Capabilities
{capabilities}

## Handoffs
{handoffs}

## Workflow
{workflow}
"""


def add_agent(team_path, role_id, name, description, model=None,
              depends_on=None, tools_allow=None, tools_deny=None,
              workflow_steps=None):
    """Add an agent role to a team."""
    team_dir = Path(team_path).resolve()
    config_path = team_dir / "config.json"

    if not config_path.exists():
        print(f"Error: Team config not found at {config_path}")
        return False

    # Load config
    config = json.loads(config_path.read_text())

    # Check for duplicate role
    for role in config.get("roles", []):
        if role["id"] == role_id:
            print(f"Error: Role '{role_id}' already exists in team")
            return False

    # Build role entry
    role = {
        "id": role_id,
        "name": name,
        "description": description
    }

    if model:
        role["model"] = model
    if depends_on:
        role["dependsOn"] = depends_on
    if tools_allow or tools_deny:
        role["tools"] = {}
        if tools_allow:
            role["tools"]["allow"] = tools_allow
        if tools_deny:
            role["tools"]["deny"] = tools_deny
    if workflow_steps:
        role["workflow"] = workflow_steps

    config["roles"].append(role)
    config_path.write_text(json.dumps(config, indent=2))

    # Create teammate directory with SOUL.md
    teammate_dir = team_dir / "teammates" / role_id
    teammate_dir.mkdir(parents=True, exist_ok=True)

    # Build SOUL.md content
    capabilities = "- " + "\n- ".join(tools_allow) if tools_allow else "- All core tools (read, write, exec)"

    handoff_lines = []
    if depends_on:
        for dep in depends_on:
            handoff_lines.append(f"- @{dep}: Receive tasks and requirements from this role")
    handoff_lines.append("- @team-lead: Escalate blockers and report completion")
    handoffs = "\n".join(handoff_lines)

    workflow_text = ""
    if workflow_steps:
        for i, step in enumerate(workflow_steps, 1):
            step_text = step.get("step", f"Step {i}")
            action = step.get("action", "")
            workflow_text += f"{i}. **{step_text}**: {action}\n"
    else:
        workflow_text = "1. Review assigned tasks\n2. Execute work\n3. Report completion"

    soul_content = SOUL_MD_TEMPLATE.format(
        name=name,
        description=description,
        capabilities=capabilities,
        handoffs=handoffs,
        workflow=workflow_text
    )

    soul_path = teammate_dir / "SOUL.md"
    soul_path.write_text(soul_content)

    # Create status.json
    status = {
        "roleId": role_id,
        "status": "idle",
        "lastActive": datetime.now().isoformat()
    }
    (teammate_dir / "status.json").write_text(json.dumps(status, indent=2))

    print(f"Added agent '{name}' (role: {role_id}) to team")
    print(f"  SOUL.md: {soul_path}")
    print(f"  Status: {teammate_dir / 'status.json'}")
    return True


def main():
    if len(sys.argv) < 7:
        print("Usage: add_agent.py <team-path> --role-id <id> --name <name> --description <desc> [options]")
        sys.exit(1)

    team_path = sys.argv[1]
    role_id = name = description = model = None
    depends_on = tools_allow = tools_deny = None

    i = 2
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg == "--role-id" and i + 1 < len(sys.argv):
            role_id = sys.argv[i + 1]; i += 2
        elif arg == "--name" and i + 1 < len(sys.argv):
            name = sys.argv[i + 1]; i += 2
        elif arg == "--description" and i + 1 < len(sys.argv):
            description = sys.argv[i + 1]; i += 2
        elif arg == "--model" and i + 1 < len(sys.argv):
            model = sys.argv[i + 1]; i += 2
        elif arg == "--depends-on" and i + 1 < len(sys.argv):
            depends_on = [d.strip() for d in sys.argv[i + 1].split(",")]; i += 2
        elif arg == "--tools-allow" and i + 1 < len(sys.argv):
            tools_allow = [t.strip() for t in sys.argv[i + 1].split(",")]; i += 2
        elif arg == "--tools-deny" and i + 1 < len(sys.argv):
            tools_deny = [t.strip() for t in sys.argv[i + 1].split(",")]; i += 2
        else:
            i += 1

    if not all([role_id, name, description]):
        print("Error: --role-id, --name, and --description are required")
        sys.exit(1)

    result = add_agent(team_path, role_id, name, description,
                       model, depends_on, tools_allow, tools_deny)
    sys.exit(0 if result else 1)


if __name__ == "__main__":
    main()
