#!/usr/bin/env python3
"""DoD Self-Verification Script for SA-technical-discovery Agent.

Checks all DoD items and reports pass/fail status.

Usage:
    python3 verify_dod.py <technical-discovery-dir>

Example:
    python3 verify_dod.py ./technical-discovery
"""

import sys
import os
import yaml
from pathlib import Path
from datetime import datetime


def check_yaml_file(filepath, required_fields=None, min_items=0):
    """Check if a YAML file exists, is valid, and meets criteria."""
    if not filepath.exists():
        return False, f"File not found: {filepath}"
    try:
        with open(filepath) as f:
            data = yaml.safe_load(f)
        if data is None:
            return False, f"File is empty: {filepath}"
        if min_items > 0:
            items = data.get("items", [])
            if len(items) < min_items:
                return False, f"Expected at least {min_items} items, found {len(items)}"
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


def check_directory(dirpath):
    """Check if a directory exists and is non-empty."""
    if not dirpath.exists():
        return False, f"Directory not found: {dirpath}"
    if not dirpath.is_dir():
        return False, f"Not a directory: {dirpath}"
    if not any(dirpath.iterdir()):
        return False, f"Directory is empty: {dirpath}"
    return True, "OK"


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 verify_dod.py <technical-discovery-dir>")
        sys.exit(1)

    base = Path(sys.argv[1])
    if not base.exists():
        print(f"Error: Directory not found: {base}")
        sys.exit(1)

    config = base / "config"
    results = []

    # DoD-01: Trigger mechanism config
    results.append(("DoD-01", "Trigger mechanism config",
                     *check_yaml_file(config / "triggers.yaml")))

    # DoD-02: RACI matrix config
    results.append(("DoD-02", "RACI matrix config",
                     *check_yaml_file(config / "raci.yaml")))

    # DoD-03: Skills list config
    results.append(("DoD-03", "Skills list config",
                     *check_yaml_file(config / "skills.yaml")))

    # DoD-04: Knowledge base checklist
    results.append(("DoD-04", "Knowledge base checklist",
                     *check_yaml_file(config / "knowledge-domains.yaml")))

    # DoD-05: Tools list
    results.append(("DoD-05", "Tools list",
                     *check_yaml_file(config / "tools.yaml")))

    # DoD-06: MCP tools list
    results.append(("DoD-06", "MCP tools list",
                     *check_yaml_file(config / "mcp-tools.yaml")))

    # DoD-07: Output content list + templates
    yaml_ok, yaml_msg = check_yaml_file(config / "outputs.yaml")
    tmpl_ok, tmpl_msg = check_directory(base / "templates")
    if yaml_ok and tmpl_ok:
        results.append(("DoD-07", "Output list + templates", True, "OK"))
    else:
        msgs = []
        if not yaml_ok:
            msgs.append(yaml_msg)
        if not tmpl_ok:
            msgs.append(tmpl_msg)
        results.append(("DoD-07", "Output list + templates", False, "; ".join(msgs)))

    # DoD-08: SOP process checklist
    results.append(("DoD-08", "SOP process checklist",
                     *check_yaml_file(config / "sop.yaml")))

    # DoD-09: DoD checklist
    results.append(("DoD-09", "DoD checklist",
                     *check_yaml_file(config / "dod.yaml")))

    # DoD-10: DoR checklist
    results.append(("DoD-10", "DoR checklist",
                     *check_yaml_file(config / "dor.yaml")))

    # DoD-11: Conversation log
    results.append(("DoD-11", "Conversation log",
                     *check_md_file(base / "conversation-log.md")))

    # DoD-12: Work log
    results.append(("DoD-12", "Work log",
                     *check_md_file(base / "work-log.md")))

    # DoD-13: DoD self-verification (this script running is evidence)
    results.append(("DoD-13", "DoD self-verification", True,
                     "Self-verification script executed"))

    # DoD-14: Technical Discovery report
    results.append(("DoD-14", "Technical Discovery report",
                     *check_md_file(base / "technical-discovery-report.md")))

    # DoD-15: Phase question lists
    phase_files = list(base.glob("phase*-questions.md"))
    if phase_files:
        results.append(("DoD-15", "Phase question lists", True,
                         f"Found {len(phase_files)} phase question file(s)"))
    else:
        results.append(("DoD-15", "Phase question lists", False,
                         "No phase question files found"))

    # DoD-16: Research artifacts
    results.append(("DoD-16", "Research artifacts",
                     *check_directory(base / "research")))

    # Print report
    passed = sum(1 for r in results if r[2])
    total = len(results)

    print(f"\n{'='*70}")
    print(f"DoD Verification Report — Technical Discovery (IA-INC-001)")
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
