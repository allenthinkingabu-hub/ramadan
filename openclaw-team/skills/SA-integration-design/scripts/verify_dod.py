#!/usr/bin/env python3
"""DoD Self-Verification Script for SA-integration-design Agent.

Checks all DoD items and reports pass/fail status.

Usage:
    python3 verify_dod.py <integration-design-dir>

Example:
    python3 verify_dod.py ./integration-design
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
        print("Usage: python3 verify_dod.py <integration-design-dir>")
        sys.exit(1)

    base = Path(sys.argv[1])
    if not base.exists():
        print(f"Error: Directory not found: {base}")
        sys.exit(1)

    config = base / "config"
    results = []

    # Quality Gates (DOD-001 through DOD-010)
    results.append(("DOD-001", "Integration Strategy Document",
                     *check_md_file(base / "integration-design-report.md")))
    results.append(("DOD-002", "API Contract Specifications",
                     *check_directory(base / "api-specs")))
    results.append(("DOD-003", "Data Flow Diagrams",
                     bool(list(base.glob("diagrams/data-flow-*.md"))),
                     f"Found {len(list(base.glob('diagrams/data-flow-*.md')))} file(s)"
                     if list(base.glob("diagrams/data-flow-*.md"))
                     else "No data flow diagram files found"))
    results.append(("DOD-004", "Third-Party Dependency Register",
                     *check_md_file(base / "third-party-register.md")))
    results.append(("DOD-005", "Integration Security Design",
                     *check_md_file(base / "integration-security-design.md")))
    results.append(("DOD-006", "Message Protocol Specifications",
                     *check_md_file(base / "integration-design-report.md")))
    results.append(("DOD-007", "Error Handling Strategy",
                     *check_md_file(base / "error-handling-strategy.md")))
    results.append(("DOD-008", "Integration Test Strategy",
                     *check_md_file(base / "integration-test-strategy.md")))
    results.append(("DOD-009", "Monitoring & Alerting Plan",
                     *check_md_file(base / "monitoring-alerting-plan.md")))
    results.append(("DOD-010", "Data Transformation Mappings",
                     *check_md_file(base / "integration-design-report.md")))

    # Artifact Completeness Checks (DOD-011 through DOD-024)
    results.append(("DOD-011", "Trigger mechanism config",
                     *check_yaml_file(config / "triggers.yaml")))
    results.append(("DOD-012", "RACI matrix config",
                     *check_yaml_file(config / "raci.yaml")))
    results.append(("DOD-013", "Skills list config",
                     *check_yaml_file(config / "skills.yaml")))
    results.append(("DOD-014", "Knowledge base checklist",
                     *check_yaml_file(config / "knowledge-domains.yaml")))
    results.append(("DOD-015", "Tools checklist",
                     *check_yaml_file(config / "tools.yaml")))
    results.append(("DOD-016", "MCP tools checklist",
                     *check_yaml_file(config / "mcp-tools.yaml")))

    yaml_ok, yaml_msg = check_yaml_file(config / "outputs.yaml")
    tmpl_ok, tmpl_msg = check_directory(base / "templates")
    if yaml_ok and tmpl_ok:
        results.append(("DOD-017", "Output templates", True, "OK"))
    else:
        msgs = [m for ok, m in [(yaml_ok, yaml_msg), (tmpl_ok, tmpl_msg)] if not ok]
        results.append(("DOD-017", "Output templates", False, "; ".join(msgs)))

    results.append(("DOD-018", "SOP process checklist",
                     *check_yaml_file(config / "sop.yaml")))
    results.append(("DOD-019", "DoD checklist",
                     *check_yaml_file(config / "dod.yaml")))
    results.append(("DOD-020", "DoR checklist",
                     *check_yaml_file(config / "dor.yaml")))
    results.append(("DOD-021", "Conversation log",
                     *check_md_file(base / "conversation-log.md")))
    results.append(("DOD-022", "Work log",
                     *check_md_file(base / "work-log.md")))

    phase_files = list(base.glob("phase*-questions.md"))
    results.append(("DOD-023", "Question lists",
                     bool(phase_files),
                     f"Found {len(phase_files)} file(s)" if phase_files
                     else "No phase question files found"))

    results.append(("DOD-024", "Research records",
                     *check_directory(base / "research")))

    # Print report
    passed = sum(1 for r in results if r[2])
    total = len(results)

    print(f"\n{'='*70}")
    print(f"DoD Verification Report — Integration Design (IA-REQ-003)")
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
