#!/usr/bin/env python3
"""DoD Verification Script for IPM-INC-003 BRD Writing.

Checks the BRD output directory against the Definition of Done criteria.
Usage: python3 verify_dod.py <output_dir>

Exit code 0 = all critical/high checks pass, 1 = failures found.
"""

import os
import sys
import re
from pathlib import Path


def check_file_exists(path, name):
    """Check if a file exists and is non-empty."""
    if not os.path.isfile(path):
        return False, f"{name}: File not found at {path}"
    if os.path.getsize(path) == 0:
        return False, f"{name}: File is empty at {path}"
    return True, f"{name}: OK"


def check_no_todos(path, name):
    """Check that file has no unresolved TBD/TODO placeholders."""
    if not os.path.isfile(path):
        return False, f"{name}: File not found"
    content = Path(path).read_text(encoding="utf-8")
    todos = re.findall(r'\b(TBD|TODO|FIXME|XXX)\b', content, re.IGNORECASE)
    if todos:
        return False, f"{name}: Found {len(todos)} unresolved placeholders: {todos[:5]}"
    return True, f"{name}: No unresolved placeholders"


def check_brd_sections(brd_path):
    """Check that all 19 standard BRD sections are present."""
    if not os.path.isfile(brd_path):
        return False, "BRD file not found"
    content = Path(brd_path).read_text(encoding="utf-8")

    required_sections = [
        "Document Control", "Executive Summary", "Business Objectives",
        "Project Background", "Project Scope", "Stakeholders",
        "Business Requirements", "Functional Requirements",
        "Non-Functional Requirements", "Data Requirements",
        "Assumptions", "Constraints", "Dependencies",
        "Risks", "Success Metrics", "Cost-Benefit",
        "Implementation Timeline", "Glossary", "Appendic"
    ]

    missing = []
    for section in required_sections:
        if section.lower() not in content.lower():
            missing.append(section)

    if missing:
        return False, f"Missing sections: {', '.join(missing)}"
    return True, "All standard BRD sections present"


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 verify_dod.py <output_dir>")
        sys.exit(1)

    output_dir = sys.argv[1]
    if not os.path.isdir(output_dir):
        print(f"Error: Output directory not found: {output_dir}")
        sys.exit(1)

    results = []
    failures = 0

    # Process quality: Check required logs exist
    logs = [
        ("conversation-log.md", "DOD-P04"),
        ("work-log.md", "DOD-P05"),
        ("question-lists.md", "DOD-P06"),
        ("research-log.md", "DOD-P07"),
    ]
    for log_file, dod_id in logs:
        passed, msg = check_file_exists(os.path.join(output_dir, log_file), f"{dod_id} {log_file}")
        results.append((dod_id, "High", passed, msg))
        if not passed:
            failures += 1

    # Find BRD file (the main .md file that isn't a log)
    log_names = {l[0] for l in logs}
    brd_files = [
        f for f in os.listdir(output_dir)
        if f.endswith(".md") and f not in log_names
    ]

    if not brd_files:
        results.append(("DOD-C01", "Critical", False, "No BRD document found in output directory"))
        failures += 1
    else:
        brd_path = os.path.join(output_dir, brd_files[0])

        # Completeness: All sections present
        passed, msg = check_brd_sections(brd_path)
        results.append(("DOD-C01", "Critical", passed, msg))
        if not passed:
            failures += 1

        # Document quality: No unresolved TBDs
        passed, msg = check_no_todos(brd_path, "DOD-D05")
        results.append(("DOD-D05", "Critical", passed, msg))
        if not passed:
            failures += 1

    # Print results
    print("=" * 60)
    print("DoD Verification Report — IPM-INC-003 BRD Writing")
    print("=" * 60)
    print(f"Output directory: {output_dir}")
    print()
    print(f"{'ID':<10} {'Severity':<10} {'Status':<8} {'Details'}")
    print("-" * 60)
    for dod_id, severity, passed, msg in results:
        status = "PASS" if passed else "FAIL"
        print(f"{dod_id:<10} {severity:<10} {status:<8} {msg}")

    print()
    total = len(results)
    passed_count = total - failures
    print(f"Result: {passed_count}/{total} checks passed ({failures} failures)")

    if failures > 0:
        print("\nSTATUS: FAIL — Fix the above issues and re-run verification.")
        sys.exit(1)
    else:
        print("\nSTATUS: PASS — All automated DoD checks passed.")
        sys.exit(0)


if __name__ == "__main__":
    main()
