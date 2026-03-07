#!/usr/bin/env python3
"""DoD Self-Verification Script for tl-team-capability-assessment Agent.

Checks all DoD items and reports pass/fail status.

Usage:
    python3 verify_dod.py <team-capability-assessment-dir>

Example:
    python3 verify_dod.py ./team-capability-assessment
"""

import sys
import yaml
from pathlib import Path
from datetime import datetime


def check_yaml_file(filepath):
    """Check if a YAML file exists and is valid."""
    if not filepath.exists():
        return False, f"File not found: {filepath}"
    try:
        with open(filepath) as f:
            data = yaml.safe_load(f)
        if data is None:
            return False, f"File is empty: {filepath}"
        return True, "OK"
    except yaml.YAMLError as e:
        return False, f"Invalid YAML: {e}"
    except Exception as e:
        return False, f"Error reading file: {e}"


def check_md_file(filepath):
    """Check if a markdown file exists and is non-empty."""
    if not filepath.exists():
        return False, f"File not found: {filepath}"
    content = filepath.read_text().strip()
    if not content:
        return False, f"File is empty: {filepath}"
    return True, "OK"


def check_directory(dirpath, min_files=0):
    """Check if a directory exists and optionally has minimum files."""
    if not dirpath.exists():
        return False, f"Directory not found: {dirpath}"
    if not dirpath.is_dir():
        return False, f"Not a directory: {dirpath}"
    files = list(dirpath.iterdir())
    if not files:
        return False, f"Directory is empty: {dirpath}"
    if min_files > 0 and len(files) < min_files:
        return False, f"Expected at least {min_files} files, found {len(files)}"
    return True, f"OK ({len(files)} files)"


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 verify_dod.py <team-capability-assessment-dir>")
        sys.exit(1)

    base = Path(sys.argv[1])
    if not base.exists():
        print(f"Error: Directory not found: {base}")
        sys.exit(1)

    config = base / "config"
    results = []

    results.append(("DoD-01", "Trigger mechanism config", *check_yaml_file(config / "triggers.yaml")))
    results.append(("DoD-02", "RACI matrix config", *check_yaml_file(config / "raci.yaml")))
    results.append(("DoD-03", "Skills list config", *check_yaml_file(config / "skills.yaml")))
    results.append(("DoD-04", "Knowledge base checklist", *check_yaml_file(config / "knowledge-domains.yaml")))
    results.append(("DoD-05", "Tools list", *check_yaml_file(config / "tools.yaml")))
    results.append(("DoD-06", "MCP tools list", *check_yaml_file(config / "mcp-tools.yaml")))

    yaml_ok, yaml_msg = check_yaml_file(config / "outputs.yaml")
    tmpl_ok, tmpl_msg = check_directory(base / "templates")
    if yaml_ok and tmpl_ok:
        results.append(("DoD-07", "Output list + templates", True, "OK"))
    else:
        msgs = [m for ok, m in [(yaml_ok, yaml_msg), (tmpl_ok, tmpl_msg)] if not ok]
        results.append(("DoD-07", "Output list + templates", False, "; ".join(msgs)))

    results.append(("DoD-08", "SOP process checklist", *check_yaml_file(config / "sop.yaml")))
    results.append(("DoD-09", "DoD checklist", *check_yaml_file(config / "dod.yaml")))
    results.append(("DoD-10", "DoR checklist", *check_yaml_file(config / "dor.yaml")))
    results.append(("DoD-11", "Conversation log", *check_md_file(base / "conversation-log.md")))
    results.append(("DoD-12", "Work log", *check_md_file(base / "work-log.md")))
    results.append(("DoD-13", "DoD self-verification", True, "Self-verification script executed"))
    results.append(("DoD-14", "Team Capability Assessment report", *check_md_file(base / "team-capability-assessment-report.md")))

    phase_files = list(base.glob("phase*-questions.md"))
    results.append(("DoD-15", "Phase question lists",
                     bool(phase_files), f"Found {len(phase_files)} file(s)" if phase_files else "No phase question files found"))

    results.append(("DoD-16", "Research artifacts", *check_directory(base / "research")))
    results.append(("DoD-17", "Team Skills Matrix", *check_md_file(base / "skills-matrix.md")))
    results.append(("DoD-18", "Gap Analysis", *check_md_file(base / "gap-analysis.md")))
    results.append(("DoD-19", "Development & Remediation Plan", *check_md_file(base / "development-plan.md")))

    passed = sum(1 for r in results if r[2])
    total = len(results)

    print(f"\n{'='*70}")
    print(f"DoD Verification Report — Team Capability Assessment (TL-INC-003)")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print(f"Directory: {base}")
    print(f"{'='*70}\n")

    for dod_id, name, status, notes in results:
        icon = "PASS" if status else "FAIL"
        print(f"  [{icon}] {dod_id}: {name}")
        if not status:
            print(f"         -> {notes}")

    print(f"\n{'='*70}")
    print(f"  Overall: {passed}/{total} items passed ({100*passed//total}%)")
    print(f"{'='*70}\n")

    sys.exit(0 if passed == total else 1)


if __name__ == "__main__":
    main()
