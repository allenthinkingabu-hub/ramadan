#!/usr/bin/env python3
"""
OpenClaw AI Agent Team — One-Click Installer

Install the complete team from the openclaw-team/ package directory.

What it does:
  1. Copies skills/ to <target-workspace>/skills/     (or current repo)
  2. Copies config/ to <target-workspace>/config/
  3. Copies bootstrap files (AGENTS.md etc.) to <target-workspace>/
  4. Creates ~/.openclaw/workspace-{pm,ipm,sa}/ from templates
  5. Validates all skills with quick_validate.py

Usage:
  cd openclaw-team
  python3 scripts/install_team.py                     # install to current directory
  python3 scripts/install_team.py --target /path/to   # install to specific directory
  python3 scripts/install_team.py --force              # overwrite existing workspaces
  python3 scripts/install_team.py --skip-workspaces    # only copy skills, no ~/.openclaw setup
  python3 scripts/install_team.py --validate           # run validation after install
"""

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

# Auto-detect package root
SCRIPT_DIR = Path(__file__).resolve().parent
PACKAGE_ROOT = SCRIPT_DIR.parent


def copy_tree(src, dst, label=""):
    """Copy directory tree, return file count."""
    if not src.exists():
        print(f"  [WARN] {label or src} not found — skipping")
        return 0
    shutil.copytree(src, dst, ignore=shutil.ignore_patterns("__pycache__", ".DS_Store"), dirs_exist_ok=True)
    count = sum(1 for _ in dst.rglob("*") if _.is_file())
    return count


def main():
    parser = argparse.ArgumentParser(description="Install OpenClaw AI Agent Team")
    parser.add_argument("--target", type=str, default=".",
                        help="Target workspace directory (default: current dir)")
    parser.add_argument("--force", action="store_true",
                        help="Overwrite existing ~/.openclaw workspaces")
    parser.add_argument("--skip-workspaces", action="store_true",
                        help="Skip creating ~/.openclaw/workspace-* directories")
    parser.add_argument("--validate", action="store_true",
                        help="Run quick_validate.py on all skills after install")
    args = parser.parse_args()

    target = Path(args.target).resolve()
    openclaw_root = Path.home() / ".openclaw"

    print("=" * 60)
    print("  OpenClaw AI Agent Team — Installer")
    print("=" * 60)
    print(f"\n  Package:  {PACKAGE_ROOT}")
    print(f"  Target:   {target}")
    print(f"  Openclaw: {openclaw_root}")
    print()

    # Verify package structure
    required = ["skills", "config", "AGENTS.md"]
    missing = [r for r in required if not (PACKAGE_ROOT / r).exists()]
    if missing:
        print(f"  [ERROR] Package incomplete. Missing: {', '.join(missing)}")
        print(f"  Run this from the openclaw-team/ directory or specify --target")
        sys.exit(1)

    total = 0

    # ── Step 1: Copy skills ──
    skills_src = PACKAGE_ROOT / "skills"
    skills_dst = target / "skills" if target != PACKAGE_ROOT else target / "skills"

    # If target is a flat workspace (skills at root), put skills at root level
    # If target has a skills/ subdir convention, use that
    # Default: copy skill dirs directly to target root for compatibility
    print("  [1/5] Installing skills...")
    skill_count = 0
    for skill_dir in sorted(skills_src.iterdir()):
        if skill_dir.is_dir() and (skill_dir / "SKILL.md").exists():
            dst = target / skill_dir.name
            if dst.exists():
                shutil.rmtree(dst)
            n = copy_tree(skill_dir, dst)
            total += n
            skill_count += 1
    print(f"        {skill_count} skill directories installed")

    # ── Step 2: Copy config ──
    print("  [2/5] Installing config/...")
    n = copy_tree(PACKAGE_ROOT / "config", target / "config", "config/")
    total += n
    print(f"        {n} config files")

    # ── Step 3: Copy bootstrap files ──
    print("  [3/5] Installing bootstrap files...")
    bootstrap_count = 0
    for f in ["AGENTS.md", "SOUL.md", "IDENTITY.md", "USER.md", "TOOLS.md"]:
        src = PACKAGE_ROOT / f
        if src.exists():
            dst = target / f
            shutil.copy2(src, dst)
            total += 1
            bootstrap_count += 1
    print(f"        {bootstrap_count} bootstrap files")

    # ── Step 4: Copy task references ──
    print("  [4/5] Installing task references...")
    task_src = PACKAGE_ROOT / "task"
    if task_src.exists():
        n = copy_tree(task_src, target / "task", "task/")
        total += n
        print(f"        {n} task reference files")
    else:
        print(f"        [SKIP] no task/ directory in package")

    # ── Step 5: Set up agent workspaces ──
    if args.skip_workspaces:
        print("  [5/5] Skipping workspace setup (--skip-workspaces)")
    else:
        print("  [5/5] Setting up agent workspaces...")
        ws_src = PACKAGE_ROOT / "workspaces"
        ws_count = 0

        for code, label in [("pm", "PM Agent"), ("ipm", "IPM Agent"), ("sa", "SA Agent")]:
            ws_template = ws_src / code
            ws_target = openclaw_root / f"workspace-{code}"

            if ws_target.exists() and not args.force:
                print(f"        [SKIP] {ws_target} exists (use --force to overwrite)")
                continue

            if ws_target.exists():
                shutil.rmtree(ws_target)

            if ws_template.exists():
                n = copy_tree(ws_template, ws_target, f"workspace-{code}")
                total += n
                ws_count += n
                print(f"        {ws_target} — {label} ({n} files)")
            else:
                print(f"        [WARN] No template for workspace-{code}")

        print(f"        Total workspace files: {ws_count}")

    # ── Validation ──
    if args.validate:
        print("\n  Running validation...")
        validator = PACKAGE_ROOT / "scripts" / "quick_validate.py"
        if not validator.exists():
            validator = target / "skill-creator" / "scripts" / "quick_validate.py"

        if validator.exists():
            passed = 0
            failed = 0
            for skill_dir in sorted(target.iterdir()):
                if skill_dir.is_dir() and (skill_dir / "SKILL.md").exists():
                    result = subprocess.run(
                        [sys.executable, str(validator), str(skill_dir)],
                        capture_output=True, text=True, cwd=str(target)
                    )
                    if "valid" in result.stdout.lower():
                        passed += 1
                    else:
                        failed += 1
                        print(f"    [FAIL] {skill_dir.name}: {result.stdout.strip()}")
            print(f"  Validation: {passed} passed, {failed} failed")
        else:
            print(f"  [WARN] quick_validate.py not found — skipping validation")

    print(f"\n{'=' * 60}")
    print(f"  Installation complete: {total} files installed")
    print(f"{'=' * 60}")
    print(f"\n  Workspace: {target}")
    if not args.skip_workspaces:
        print(f"  Agent workspaces:")
        print(f"    ~/.openclaw/workspace-pm/")
        print(f"    ~/.openclaw/workspace-ipm/")
        print(f"    ~/.openclaw/workspace-sa/")
    print(f"\n  To start: trigger PM Agent with a project request")


if __name__ == "__main__":
    main()
