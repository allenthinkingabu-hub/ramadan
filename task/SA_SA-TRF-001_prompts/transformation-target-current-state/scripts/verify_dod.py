#!/usr/bin/env python3
"""
verify_dod.py — SA-TRF-001: Transformation Target Current State Analysis
Runs all 20 DoD checks against the current analysis output directory.

Usage:
    python scripts/verify_dod.py --output-dir outputs/analysis-20260315-143000 \
                                  --session-id SESSION-001 \
                                  [--db-path memory/agent_memory.db] \
                                  [--round 1]

Exit codes:
    0 — all checks pass
    1 — one or more checks fail
"""

import argparse
import os
import re
import sqlite3
import sys
from datetime import datetime
from typing import Callable, Dict, List, Tuple

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

PLACEHOLDER_PATTERN = re.compile(r"\{[a-zA-Z_]+\}")
MIN_OUT07_BYTES = 1000
REQUIRED_PHASE_FILES = ["phase1-questions.md", "phase2-questions.md", "phase3-questions.md"]
RACI_PATH = "config/raci.md"
CONVERSATION_LOG = "logs/conversation-log.md"
WORK_LOG = "logs/work-log.md"

OUTPUT_FILES = {
    "OUT-01": "OUT-01-code-structure-map.md",
    "OUT-02": "OUT-02-responsibility-analysis.md",
    "OUT-03": "OUT-03-dependency-map.md",
    "OUT-04": "OUT-04-data-flow-analysis.md",
    "OUT-05": "OUT-05-test-coverage-report.md",
    "OUT-06": "OUT-06-tech-debt-risk-register.md",
    "OUT-07": "OUT-07-current-state-report.md",
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _read(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        return ""


def _file_size(path: str) -> int:
    try:
        return os.path.getsize(path)
    except Exception:
        return 0


def _out_path(output_dir: str, filename: str) -> str:
    return os.path.join(output_dir, filename)


def _find_output_file(output_dir: str, out_id: str) -> str:
    """Find a file matching OUT-0N pattern in output_dir (exact or glob fallback)."""
    exact = _out_path(output_dir, OUTPUT_FILES[out_id])
    if os.path.exists(exact):
        return exact
    # fallback: find any file starting with out_id prefix (case-insensitive)
    prefix = out_id.lower()
    for fname in os.listdir(output_dir) if os.path.isdir(output_dir) else []:
        if fname.lower().startswith(prefix):
            return _out_path(output_dir, fname)
    return exact  # return expected path even if missing (will fail size check)


def _db_connect(db_path: str) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


# ---------------------------------------------------------------------------
# Check functions — each returns (passed: bool, detail: str)
# ---------------------------------------------------------------------------

def chk_01(output_dir: str, **_) -> Tuple[bool, str]:
    p = _find_output_file(output_dir, "OUT-01")
    size = _file_size(p)
    return (size > 0, f"OUT-01 size={size} bytes at {p}")


def chk_02(output_dir: str, **_) -> Tuple[bool, str]:
    p = _find_output_file(output_dir, "OUT-02")
    size = _file_size(p)
    return (size > 0, f"OUT-02 size={size} bytes at {p}")


def chk_03(output_dir: str, **_) -> Tuple[bool, str]:
    p = _find_output_file(output_dir, "OUT-03")
    size = _file_size(p)
    return (size > 0, f"OUT-03 size={size} bytes at {p}")


def chk_04(output_dir: str, **_) -> Tuple[bool, str]:
    p = _find_output_file(output_dir, "OUT-04")
    size = _file_size(p)
    return (size > 0, f"OUT-04 size={size} bytes at {p}")


def chk_05(output_dir: str, **_) -> Tuple[bool, str]:
    p = _find_output_file(output_dir, "OUT-05")
    size = _file_size(p)
    return (size > 0, f"OUT-05 size={size} bytes at {p}")


def chk_06(output_dir: str, **_) -> Tuple[bool, str]:
    p = _find_output_file(output_dir, "OUT-06")
    size = _file_size(p)
    return (size > 0, f"OUT-06 size={size} bytes at {p}")


def chk_07(output_dir: str, **_) -> Tuple[bool, str]:
    p = _find_output_file(output_dir, "OUT-07")
    size = _file_size(p)
    return (size > MIN_OUT07_BYTES, f"OUT-07 size={size} bytes (min {MIN_OUT07_BYTES}) at {p}")


def chk_08(output_dir: str, **_) -> Tuple[bool, str]:
    """All output files must be free of {placeholder} patterns."""
    violations = []
    for out_id, filename in OUTPUT_FILES.items():
        p = _find_output_file(output_dir, out_id)
        content = _read(p)
        if not content:
            continue
        matches = PLACEHOLDER_PATTERN.findall(content)
        if matches:
            violations.append(f"{filename}: {set(matches)}")
    if violations:
        return (False, "Unfilled placeholders found: " + "; ".join(violations))
    return (True, "No unfilled placeholders found")


def chk_09(output_dir: str, **kwargs) -> Tuple[bool, str]:
    """Conversation log must contain explicit user confirmation of OUT-07."""
    log_path = os.path.join(os.path.dirname(output_dir), CONVERSATION_LOG)
    # also check alongside output_dir
    alt_log = os.path.join(output_dir, "..", CONVERSATION_LOG)
    content = _read(log_path) or _read(alt_log)
    confirmed = re.search(r"(confirmed|approved|accept|looks good|proceed).*OUT-07", content, re.IGNORECASE)
    if confirmed:
        return (True, "OUT-07 user confirmation found in conversation log")
    return (False, "OUT-07 user confirmation NOT found in conversation log")


def chk_10(output_dir: str, **_) -> Tuple[bool, str]:
    """OUT-03 must contain both inbound AND outbound dependency sections."""
    p = _find_output_file(output_dir, "OUT-03")
    content = _read(p)
    has_inbound = bool(re.search(r"inbound|no inbound|who calls", content, re.IGNORECASE))
    has_outbound = bool(re.search(r"outbound|what.*depends|internal depend", content, re.IGNORECASE))
    if has_inbound and has_outbound:
        return (True, "OUT-03 contains both inbound and outbound sections")
    missing = []
    if not has_inbound:
        missing.append("inbound")
    if not has_outbound:
        missing.append("outbound")
    return (False, f"OUT-03 missing sections: {missing}")


def chk_11(output_dir: str, **_) -> Tuple[bool, str]:
    """OUT-05 must contain a coverage level rating."""
    p = _find_output_file(output_dir, "OUT-05")
    content = _read(p)
    has_level = bool(re.search(r"\b(High|Medium|Low|None)\b.*(%|coverage)", content, re.IGNORECASE))
    if not has_level:
        # also accept table rows with coverage level words
        has_level = bool(re.search(r"\|\s*(High|Medium|Low|None)\s*\|", content, re.IGNORECASE))
    return (has_level, "OUT-05 contains coverage level rating" if has_level else "OUT-05 missing coverage level (High/Medium/Low/None)")


def chk_12(output_dir: str, **_) -> Tuple[bool, str]:
    """OUT-06 must contain at least one debt/risk item or explicit 'no debt' statement."""
    p = _find_output_file(output_dir, "OUT-06")
    content = _read(p)
    no_debt = bool(re.search(r"no (technical )?debt|no (debt|risk) (identified|found)", content, re.IGNORECASE))
    has_item = bool(re.search(r"\|\s*(CS|AP|KI|CH|SEC|PR|HV|RSK)-\d+\s*\|", content))
    if no_debt or has_item:
        return (True, "OUT-06 contains debt/risk items or explicit no-debt statement")
    return (False, "OUT-06 missing debt/risk entries and no explicit 'no debt' statement")


def chk_13(output_dir: str, **_) -> Tuple[bool, str]:
    """OUT-07 must contain a Hard Constraints section."""
    p = _find_output_file(output_dir, "OUT-07")
    content = _read(p)
    has_section = bool(re.search(r"##.*hard constraint", content, re.IGNORECASE))
    has_entry_or_none = bool(re.search(r"(HC-\d+|no hard constraint)", content, re.IGNORECASE))
    ok = has_section and has_entry_or_none
    return (ok, "OUT-07 Hard Constraints section present" if ok else "OUT-07 missing Hard Constraints section")


def chk_14(output_dir: str, **kwargs) -> Tuple[bool, str]:
    """Conversation log must have entries for Steps 0-4."""
    log_path = os.path.join(os.path.dirname(output_dir), CONVERSATION_LOG)
    content = _read(log_path)
    missing_steps = []
    for step in ["Step 0", "Step 1", "Step 2", "Step 3", "Step 4"]:
        if step.lower() not in content.lower():
            missing_steps.append(step)
    if missing_steps:
        return (False, f"Conversation log missing entries for: {missing_steps}")
    return (True, "Conversation log contains entries for Steps 0-4")


def chk_15(output_dir: str, **kwargs) -> Tuple[bool, str]:
    """Work log must have timestamped entries for Steps 0-5."""
    log_path = os.path.join(os.path.dirname(output_dir), WORK_LOG)
    content = _read(log_path)
    missing_steps = []
    for step in ["Step 0", "Step 1", "Step 2", "Step 3", "Step 4", "Step 5"]:
        if step.lower() not in content.lower():
            missing_steps.append(step)
    has_timestamps = bool(re.search(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}", content))
    if missing_steps:
        return (False, f"Work log missing entries for: {missing_steps}")
    if not has_timestamps:
        return (False, "Work log exists but no ISO timestamps found")
    return (True, "Work log contains timestamped entries for Steps 0-5")


def chk_16(output_dir: str, session_id: str, db_path: str, **_) -> Tuple[bool, str]:
    """task_memory must have at least one finding for this session."""
    if not db_path or not os.path.exists(db_path):
        return (False, f"Database not found: {db_path}")
    try:
        conn = _db_connect(db_path)
        row = conn.execute(
            "SELECT COUNT(*) FROM task_memory WHERE session_id = ?", (session_id,)
        ).fetchone()
        count = row[0]
        conn.close()
        return (count > 0, f"task_memory has {count} records for session {session_id}")
    except Exception as e:
        return (False, f"DB query failed: {e}")


def chk_17(output_dir: str, session_id: str, db_path: str, **_) -> Tuple[bool, str]:
    """analysis_history must have exactly one completed record for this session."""
    if not db_path or not os.path.exists(db_path):
        return (False, f"Database not found: {db_path}")
    try:
        conn = _db_connect(db_path)
        row = conn.execute("""
            SELECT COUNT(*) FROM analysis_history
            WHERE session_id = ? AND status = 'completed'
        """, (session_id,)).fetchone()
        count = row[0]
        conn.close()
        return (count == 1, f"analysis_history completed records: {count} (expected 1)")
    except Exception as e:
        return (False, f"DB query failed: {e}")


def chk_18(output_dir: str, **_) -> Tuple[bool, str]:
    """Phase question files must exist."""
    base = os.path.dirname(output_dir)
    missing = []
    for fname in REQUIRED_PHASE_FILES:
        path = os.path.join(base, fname)
        if not os.path.exists(path):
            missing.append(fname)
    if missing:
        return (False, f"Missing phase question files: {missing}")
    return (True, "All phase question files exist")


def chk_19(output_dir: str, **_) -> Tuple[bool, str]:
    """research/ directory must contain at least 1 file."""
    base = os.path.dirname(output_dir)
    research_dir = os.path.join(base, "research")
    if not os.path.isdir(research_dir):
        return (False, f"research/ directory not found at {research_dir}")
    files = [f for f in os.listdir(research_dir) if os.path.isfile(os.path.join(research_dir, f))]
    count = len(files)
    return (count > 0, f"research/ directory contains {count} file(s)")


def chk_20(output_dir: str, **_) -> Tuple[bool, str]:
    """config/raci.md must exist with downstream task entries."""
    base = os.path.dirname(output_dir)
    raci_path = os.path.join(base, RACI_PATH)
    if not os.path.exists(raci_path):
        return (False, f"config/raci.md not found at {raci_path}")
    content = _read(raci_path)
    has_downstream = bool(re.search(r"(SA-TRF-002|SA-TST-001|SA-TDB-001|SA-ARC-001)", content))
    return (has_downstream, "config/raci.md exists with downstream task entries" if has_downstream
            else "config/raci.md exists but missing downstream task entries (SA-TRF-002 etc.)")


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------

CHECKS: List[Tuple[str, Callable, str]] = [
    ("DoD-01", chk_01,  "OUT-01 produced and non-empty"),
    ("DoD-02", chk_02,  "OUT-02 produced and non-empty"),
    ("DoD-03", chk_03,  "OUT-03 produced and non-empty"),
    ("DoD-04", chk_04,  "OUT-04 produced and non-empty"),
    ("DoD-05", chk_05,  "OUT-05 produced and non-empty"),
    ("DoD-06", chk_06,  "OUT-06 produced and non-empty"),
    ("DoD-07", chk_07,  "OUT-07 produced and substantial (>1000 bytes)"),
    ("DoD-08", chk_08,  "All templates fully populated (no {placeholder})"),
    ("DoD-09", chk_09,  "OUT-07 confirmed by user"),
    ("DoD-10", chk_10,  "OUT-03 covers inbound AND outbound dependencies"),
    ("DoD-11", chk_11,  "OUT-05 includes coverage level rating"),
    ("DoD-12", chk_12,  "OUT-06 has at least one debt/risk item or no-debt statement"),
    ("DoD-13", chk_13,  "OUT-07 includes Hard Constraints section"),
    ("DoD-14", chk_14,  "Conversation log covers Steps 0-4"),
    ("DoD-15", chk_15,  "Work log has timestamped entries for Steps 0-5"),
    ("DoD-16", chk_16,  "Findings recorded in SQLite (task_memory)"),
    ("DoD-17", chk_17,  "Analysis history completed in SQLite"),
    ("DoD-18", chk_18,  "Phase question files exist"),
    ("DoD-19", chk_19,  "research/ directory has at least 1 file"),
    ("DoD-20", chk_20,  "config/raci.md ready for PM Agent handoff"),
]


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

def run_all_checks(output_dir: str, session_id: str, db_path: str,
                   check_round: int = 1) -> List[Dict]:
    results = []
    kwargs = dict(output_dir=output_dir, session_id=session_id,
                  db_path=db_path, check_round=check_round)
    for check_id, fn, description in CHECKS:
        try:
            passed, detail = fn(**kwargs)
        except Exception as e:
            passed, detail = False, f"Check error: {e}"
        results.append({
            "check_id": check_id,
            "description": description,
            "status": "pass" if passed else "fail",
            "detail": detail,
        })
    return results


def print_report(results: List[Dict], output_dir: str, session_id: str, check_round: int) -> int:
    total = len(results)
    passed = sum(1 for r in results if r["status"] == "pass")
    failed = total - passed

    print("\n" + "=" * 70)
    print(f"  SA-TRF-001 DoD Verification Report")
    print(f"  Session   : {session_id}")
    print(f"  Output Dir: {output_dir}")
    print(f"  Round     : {check_round}")
    print(f"  Timestamp : {datetime.utcnow().isoformat()}Z")
    print("=" * 70)

    for r in results:
        icon = "✓" if r["status"] == "pass" else "✗"
        print(f"  {icon} [{r['check_id']}] {r['description']}")
        if r["status"] == "fail":
            print(f"      → {r['detail']}")

    print("=" * 70)
    print(f"  Result: {passed}/{total} checks passed  |  {failed} failed")
    print("=" * 70 + "\n")

    return 0 if failed == 0 else 1


def save_report(results: List[Dict], output_dir: str, session_id: str, check_round: int) -> str:
    report_path = os.path.join(output_dir, f"dod-report-round{check_round}.md")
    lines = [
        f"# DoD Verification Report — Round {check_round}\n",
        f"**Session**: {session_id}  \n",
        f"**Output Dir**: {output_dir}  \n",
        f"**Timestamp**: {datetime.utcnow().isoformat()}Z  \n\n",
        "| Check | Description | Status | Detail |\n",
        "|-------|-------------|--------|--------|\n",
    ]
    for r in results:
        status = "PASS" if r["status"] == "pass" else "FAIL"
        lines.append(f"| {r['check_id']} | {r['description']} | {status} | {r['detail']} |\n")
    passed = sum(1 for r in results if r["status"] == "pass")
    lines.append(f"\n**Result**: {passed}/{len(results)} checks passed\n")
    with open(report_path, "w", encoding="utf-8") as f:
        f.writelines(lines)
    return report_path


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="SA-TRF-001 DoD verification")
    parser.add_argument("--output-dir", required=True, help="Path to analysis output directory")
    parser.add_argument("--session-id", required=True, help="Analysis session ID")
    parser.add_argument("--db-path", default=None, help="Path to SQLite database")
    parser.add_argument("--round", type=int, default=1, help="Check round number (1-3)")
    parser.add_argument("--save-report", action="store_true", help="Save markdown report to output-dir")
    args = parser.parse_args()

    db_path = args.db_path
    if db_path is None:
        base = os.path.dirname(os.path.abspath(args.output_dir))
        db_path = os.path.join(base, "memory", "agent_memory.db")

    if not os.path.isdir(args.output_dir):
        print(f"ERROR: output directory not found: {args.output_dir}", file=sys.stderr)
        return 1

    results = run_all_checks(
        output_dir=args.output_dir,
        session_id=args.session_id,
        db_path=db_path,
        check_round=args.round,
    )

    if args.save_report:
        report_path = save_report(results, args.output_dir, args.session_id, args.round)
        print(f"Report saved: {report_path}")

    return print_report(results, args.output_dir, args.session_id, args.round)


if __name__ == "__main__":
    sys.exit(main())
