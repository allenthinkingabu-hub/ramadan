#!/usr/bin/env python3
"""
Package the entire OpenClaw AI Agent Team into a single deployable directory.

Collects all skills, configs, workspace templates, and tools into:
  openclaw-team/

Usage:
  cd <repo-root>
  python3 scripts/package_team.py
"""

import json
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DEST = REPO / "openclaw-team"


def copy_dir(src, dst):
    """Copy directory tree, skip __pycache__."""
    if src.is_dir():
        shutil.copytree(src, dst, ignore=shutil.ignore_patterns("__pycache__", ".DS_Store"), dirs_exist_ok=True)
    return sum(1 for _ in dst.rglob("*") if _.is_file())


def copy_file(src, dst):
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def main():
    if DEST.exists():
        print(f"Removing existing {DEST.name}/...")
        shutil.rmtree(DEST)

    DEST.mkdir()
    total = 0

    # ── 1. Skills ──
    skills_dir = DEST / "skills"
    skills_dir.mkdir()
    prefixes = ("pm-", "ipm-", "sa-", "SA-")
    skill_count = 0
    for d in sorted(REPO.iterdir()):
        if d.is_dir() and d.name.startswith(prefixes) and (d / "SKILL.md").exists():
            n = copy_dir(d, skills_dir / d.name)
            total += n
            skill_count += 1
    print(f"  skills/  — {skill_count} skill directories, {total} files")

    # ── 2. Config ──
    config_src = REPO / "config"
    if config_src.exists():
        n = copy_dir(config_src, DEST / "config")
        total += n
        print(f"  config/  — {n} files")

    # ── 3. Workspace bootstrap files ──
    for f in ["AGENTS.md", "SOUL.md", "IDENTITY.md", "USER.md", "TOOLS.md"]:
        src = REPO / f
        if src.exists():
            copy_file(src, DEST / f)
            total += 1
    print(f"  Bootstrap files — AGENTS.md, SOUL.md, IDENTITY.md, USER.md, TOOLS.md")

    # ── 4. Agent workspace templates (from ~/.openclaw/) ──
    openclaw = Path.home() / ".openclaw"
    ws_dest = DEST / "workspaces"
    ws_count = 0
    for code in ("pm", "ipm", "sa"):
        ws = openclaw / f"workspace-{code}"
        if ws.exists():
            n = copy_dir(ws, ws_dest / code)
            total += n
            ws_count += n
    print(f"  workspaces/ — pm, ipm, sa templates ({ws_count} files)")

    # ── 5. SA tasks-index from repo ──
    sa_tasks = REPO / "system-architect-agent" / "config" / "tasks-index.json"
    if sa_tasks.exists():
        dst = ws_dest / "sa" / "config" / "tasks-index.json"
        if not dst.exists():
            copy_file(sa_tasks, dst)
            total += 1
            print(f"  workspaces/sa/config/tasks-index.json — from system-architect-agent")

    # ── 6. Tool scripts ──
    scripts_dest = DEST / "scripts"
    scripts_dest.mkdir(exist_ok=True)
    for script in ["quick_validate.py", "init_skill.py", "package_skill.py"]:
        src = REPO / "skill-creator" / "scripts" / script
        if src.exists():
            copy_file(src, scripts_dest / script)
            total += 1
    print(f"  scripts/ — quick_validate.py, init_skill.py, package_skill.py")

    # ── 7. Task reference files ──
    task_src = REPO / "task"
    if task_src.exists():
        n = copy_dir(task_src, DEST / "task")
        total += n
        print(f"  task/    — {n} reference files")

    # ── 8. Prompt (skill-creator prompt) ──
    prompt_src = REPO / "prompt" / "openclaw-skill-creator-prompt.md"
    if prompt_src.exists():
        copy_file(prompt_src, DEST / "docs" / "openclaw-skill-creator-prompt.md")
        total += 1
        print(f"  docs/    — openclaw-skill-creator-prompt.md")

    print(f"\n  Total: {total} files packaged into {DEST.name}/")
    print(f"  Size:  ", end="")
    # Calculate size
    size = sum(f.stat().st_size for f in DEST.rglob("*") if f.is_file())
    if size > 1_000_000:
        print(f"{size / 1_000_000:.1f} MB")
    else:
        print(f"{size / 1_000:.0f} KB")


if __name__ == "__main__":
    main()
