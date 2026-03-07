#!/usr/bin/env python3
"""DoD Verification Script for IA-INC-008 Third-Party/Vendor Strategy.

Checks the output directory against the Definition of Done criteria.
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

    # Find deliverable files
    log_names = {l[0] for l in logs}
    deliverable_files = [
        f for f in os.listdir(output_dir)
        if f.endswith(".md") and f not in log_names
    ]

    if not deliverable_files:
        results.append(("DOD-C01", "Critical", False, "No deliverable found in output directory"))
        failures += 1
    else:
        deliverable_path = os.path.join(output_dir, deliverable_files[0])

        # Document quality: No unresolved TBDs
        passed, msg = check_no_todos(deliverable_path, "DOD-D05")
        results.append(("DOD-D05", "Critical", passed, msg))
        if not passed:
            failures += 1

    # Print results
    print("=" * 60)
    print("DoD Verification Report — IA-INC-008 Third-Party/Vendor Strategy")
    print("=" * 60)
    print(f"Output directory: {output_dir}")
    print()
    print(f"{\'ID\':<10} {\'Severity\':<10} {\'Status\':<8} {\'Details\'}")
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
