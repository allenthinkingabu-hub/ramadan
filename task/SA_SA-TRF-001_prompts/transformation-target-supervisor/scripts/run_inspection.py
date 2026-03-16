#!/usr/bin/env python3
"""
run_inspection.py — transformation-target-supervisor
Independent DoD inspection script for SA-TRF-001 deliverables.
Re-implements all 20 checks independently of the primary agent's verify_dod.py.

Usage:
    python scripts/run_inspection.py \
        --output-dir outputs/analysis-20260315-143000 \
        --session-id SA-TRF-001-20260315-143000 \
        [--db-path memory/agent_memory.db] \
        [--round 1] \
        [--save-report]

Exit codes:
    0 — all 20 checks pass
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

PLACEHOLDER_RE = re.compile(r"\{[a-zA-Z_]+\}")
MIN_OUT07_BYTES = 1000
PHASE_FILES = ["phase1-questions.md", "phase2-questions.md", "phase3-questions.md"]
CONVERSATION_LOG = "logs/conversation-log.md"
WORK_LOG = "logs/work-log.md"
RACI_PATH = "config/raci.md"

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
        with open(path, encoding="utf-8") as f:
            return f.read()
    except Exception:
        return ""


def _size(path: str) -> int:
    try:
        return os.path.getsize(path)
    except Exception:
        return 0


def _locate_output(output_dir: str, out_id: str) -> str:
    """Find output file — exact match first, then prefix match."""
    exact = os.path.join(output_dir, OUTPUT_FILES[out_id])
    if os.path.exists(exact):
        return exact
    if os.path.isdir(output_dir):
        prefix = out_id.lower()
        for fname in os.listdir(output_dir):
            if fname.lower().startswith(prefix):
                return os.path.join(output_dir, fname)
    return exact  # return expected path even if missing


def _skill_base(output_dir: str) -> str:
    """Base directory of the skill (parent of output_dir)."""
    return os.path.dirname(os.path.abspath(output_dir))


def _db_connect(db_path: str) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


# ---------------------------------------------------------------------------
# Check functions (independent implementations)
# ---------------------------------------------------------------------------

def chk_01(output_dir, **_): return _check_output_nonempty(output_dir, "OUT-01")
def chk_02(output_dir, **_): return _check_output_nonempty(output_dir, "OUT-02")
def chk_03(output_dir, **_): return _check_output_nonempty(output_dir, "OUT-03")
def chk_04(output_dir, **_): return _check_output_nonempty(output_dir, "OUT-04")
def chk_05(output_dir, **_): return _check_output_nonempty(output_dir, "OUT-05")
def chk_06(output_dir, **_): return _check_output_nonempty(output_dir, "OUT-06")

def _check_output_nonempty(output_dir: str, out_id: str) -> Tuple[bool, str]:
    p = _locate_output(output_dir, out_id)
    size = _size(p)
    ok = size > 0
    return (ok, f"{out_id} {'found' if ok else 'MISSING or empty'} at {p} ({size} bytes)")


def chk_07(output_dir, **_) -> Tuple[bool, str]:
    p = _locate_output(output_dir, "OUT-07")
    size = _size(p)
    ok = size > MIN_OUT07_BYTES
    return (ok, f"OUT-07 size={size} bytes (min {MIN_OUT07_BYTES}) at {p}")


def chk_08(output_dir, **_) -> Tuple[bool, str]:
    """No {placeholder} in any output file."""
    violations = []
    for out_id in OUTPUT_FILES:
        p = _locate_output(output_dir, out_id)
        content = _read(p)
        if not content:
            continue
        found = set(PLACEHOLDER_RE.findall(content))
        if found:
            violations.append(f"{out_id}: {found}")
    ok = len(violations) == 0
    return (ok, "No unfilled placeholders" if ok else "Placeholders remain: " + "; ".join(violations))


def chk_09(output_dir, **_) -> Tuple[bool, str]:
    """Conversation log must show OUT-07 confirmation."""
    base = _skill_base(output_dir)
    log = _read(os.path.join(base, CONVERSATION_LOG))
    confirmed = bool(re.search(
        r"(confirm|approved|accept|looks good|proceed|yes).*OUT-07|OUT-07.*(confirm|approved|accepted)",
        log, re.IGNORECASE
    ))
    return (confirmed, "OUT-07 user confirmation found" if confirmed else
            "OUT-07 user confirmation NOT found in conversation-log.md")


def chk_10(output_dir, **_) -> Tuple[bool, str]:
    """OUT-03 must have both inbound and outbound sections."""
    p = _locate_output(output_dir, "OUT-03")
    content = _read(p)
    has_in = bool(re.search(r"inbound|callers|who calls|no inbound", content, re.IGNORECASE))
    has_out = bool(re.search(r"outbound|depends on|internal depend|external depend", content, re.IGNORECASE))
    ok = has_in and has_out
    missing = [s for s, flag in [("inbound", has_in), ("outbound", has_out)] if not flag]
    return (ok, "Both sections present" if ok else f"Missing: {missing}")


def chk_11(output_dir, **_) -> Tuple[bool, str]:
    """OUT-05 must contain a coverage level rating."""
    p = _locate_output(output_dir, "OUT-05")
    content = _read(p)
    has_level = bool(re.search(r"\b(High|Medium|Low|None)\b", content, re.IGNORECASE)) and \
                bool(re.search(r"(coverage|%|unit)", content, re.IGNORECASE))
    if not has_level:
        has_level = bool(re.search(r"\|\s*(High|Medium|Low|None)\s*\|", content, re.IGNORECASE))
    return (has_level, "Coverage level rating found" if has_level else
            "Coverage level (High/Medium/Low/None) NOT found in OUT-05")


def chk_12(output_dir, **_) -> Tuple[bool, str]:
    """OUT-06 must have debt item or no-debt statement."""
    p = _locate_output(output_dir, "OUT-06")
    content = _read(p)
    no_debt = bool(re.search(r"no (technical )?debt|no (debt|risk) (identified|found)", content, re.IGNORECASE))
    has_item = bool(re.search(r"\|\s*(CS|AP|KI|CH|SEC|PR|HV|RSK)-\d+\s*\|", content))
    ok = no_debt or has_item
    return (ok, "Debt/risk items present" if ok else
            "OUT-06 missing debt items and no 'no debt' statement")


def chk_13(output_dir, **_) -> Tuple[bool, str]:
    """OUT-07 must have Hard Constraints section."""
    p = _locate_output(output_dir, "OUT-07")
    content = _read(p)
    has_section = bool(re.search(r"##.*hard constraint", content, re.IGNORECASE))
    has_content = bool(re.search(r"(HC-\d+|no hard constraint)", content, re.IGNORECASE))
    ok = has_section and has_content
    return (ok, "Hard Constraints section present" if ok else
            "OUT-07 missing Hard Constraints section or content")


def chk_14(output_dir, **_) -> Tuple[bool, str]:
    """Conversation log must cover Steps 0-4."""
    base = _skill_base(output_dir)
    content = _read(os.path.join(base, CONVERSATION_LOG))
    missing = [s for s in ["Step 0", "Step 1", "Step 2", "Step 3", "Step 4"]
               if s.lower() not in content.lower()]
    ok = len(missing) == 0
    return (ok, "All steps present in conversation log" if ok else
            f"Conversation log missing: {missing}")


def chk_15(output_dir, **_) -> Tuple[bool, str]:
    """Work log must have timestamped entries for Steps 0-5."""
    base = _skill_base(output_dir)
    content = _read(os.path.join(base, WORK_LOG))
    missing = [s for s in ["Step 0", "Step 1", "Step 2", "Step 3", "Step 4", "Step 5"]
               if s.lower() not in content.lower()]
    has_ts = bool(re.search(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}", content))
    if missing:
        return (False, f"Work log missing steps: {missing}")
    if not has_ts:
        return (False, "Work log missing ISO timestamps")
    return (True, "Work log complete with timestamps")


def chk_16(output_dir, session_id, db_path, **_) -> Tuple[bool, str]:
    """SQLite task_memory must have records for this session."""
    if not db_path or not os.path.exists(db_path):
        # try default location
        base = _skill_base(output_dir)
        db_path = os.path.join(base, "memory", "agent_memory.db")
    if not os.path.exists(db_path):
        return (False, f"Database not found: {db_path}")
    try:
        conn = _db_connect(db_path)
        count = conn.execute(
            "SELECT COUNT(*) FROM task_memory WHERE session_id = ?", (session_id,)
        ).fetchone()[0]
        conn.close()
        return (count > 0, f"task_memory: {count} records for session {session_id}")
    except Exception as e:
        return (False, f"DB error: {e}")


def chk_17(output_dir, session_id, db_path, **_) -> Tuple[bool, str]:
    """analysis_history must have one completed record."""
    if not db_path or not os.path.exists(db_path):
        base = _skill_base(output_dir)
        db_path = os.path.join(base, "memory", "agent_memory.db")
    if not os.path.exists(db_path):
        return (False, f"Database not found: {db_path}")
    try:
        conn = _db_connect(db_path)
        count = conn.execute("""
            SELECT COUNT(*) FROM analysis_history
            WHERE session_id = ? AND status = 'completed'
        """, (session_id,)).fetchone()[0]
        conn.close()
        return (count == 1, f"analysis_history completed records: {count} (expected 1)")
    except Exception as e:
        return (False, f"DB error: {e}")


def chk_18(output_dir, **_) -> Tuple[bool, str]:
    """Phase question files must exist."""
    base = _skill_base(output_dir)
    missing = [f for f in PHASE_FILES if not os.path.exists(os.path.join(base, f))]
    ok = len(missing) == 0
    return (ok, "All phase question files exist" if ok else f"Missing: {missing}")


def chk_19(output_dir, **_) -> Tuple[bool, str]:
    """research/ directory must have at least 1 file."""
    base = _skill_base(output_dir)
    research_dir = os.path.join(base, "research")
    if not os.path.isdir(research_dir):
        return (False, f"research/ directory not found")
    files = [f for f in os.listdir(research_dir) if os.path.isfile(os.path.join(research_dir, f))]
    ok = len(files) > 0
    return (ok, f"research/ contains {len(files)} file(s)")


def chk_20(output_dir, **_) -> Tuple[bool, str]:
    """config/raci.md must exist with downstream task entries."""
    base = _skill_base(output_dir)
    raci = os.path.join(base, RACI_PATH)
    if not os.path.exists(raci):
        return (False, f"config/raci.md not found")
    content = _read(raci)
    ok = bool(re.search(r"SA-TRF-002|SA-TST-001|SA-TDB-001|SA-ARC-001", content))
    return (ok, "config/raci.md present with downstream tasks" if ok else
            "config/raci.md exists but missing downstream task entries")


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------

CHECKS: List[Tuple[str, Callable, str]] = [
    ("DoD-01", chk_01, "OUT-01 produced and non-empty"),
    ("DoD-02", chk_02, "OUT-02 produced and non-empty"),
    ("DoD-03", chk_03, "OUT-03 produced and non-empty"),
    ("DoD-04", chk_04, "OUT-04 produced and non-empty"),
    ("DoD-05", chk_05, "OUT-05 produced and non-empty"),
    ("DoD-06", chk_06, "OUT-06 produced and non-empty"),
    ("DoD-07", chk_07, "OUT-07 produced and substantial (>1000 bytes)"),
    ("DoD-08", chk_08, "All templates fully populated"),
    ("DoD-09", chk_09, "OUT-07 confirmed by user"),
    ("DoD-10", chk_10, "OUT-03 covers inbound AND outbound"),
    ("DoD-11", chk_11, "OUT-05 includes coverage level rating"),
    ("DoD-12", chk_12, "OUT-06 has debt/risk item or no-debt statement"),
    ("DoD-13", chk_13, "OUT-07 has Hard Constraints section"),
    ("DoD-14", chk_14, "Conversation log covers Steps 0-4"),
    ("DoD-15", chk_15, "Work log has timestamped entries for Steps 0-5"),
    ("DoD-16", chk_16, "Findings recorded in SQLite task_memory"),
    ("DoD-17", chk_17, "Analysis history completed in SQLite"),
    ("DoD-18", chk_18, "Phase question files exist"),
    ("DoD-19", chk_19, "research/ directory has at least 1 file"),
    ("DoD-20", chk_20, "config/raci.md ready for PM Agent handoff"),
]


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

def run_all(output_dir: str, session_id: str, db_path: str) -> List[Dict]:
    kwargs = dict(output_dir=output_dir, session_id=session_id, db_path=db_path)
    results = []
    for check_id, fn, description in CHECKS:
        try:
            passed, detail = fn(**kwargs)
        except Exception as e:
            passed, detail = False, f"Check error: {e}"
        results.append({"check_id": check_id, "description": description,
                         "status": "PASS" if passed else "FAIL", "detail": detail})
    return results


def save_report(results: List[Dict], output_dir: str, session_id: str,
                check_round: int, target_name: str = "") -> str:
    passed = sum(1 for r in results if r["status"] == "PASS")
    verdict = "PASS" if passed == 20 else "FAIL"
    path = os.path.join(output_dir, "inspection-report.md")

    lines = [
        "# Transformation Target Current State — Inspection Report\n\n",
        f"**Supervisor**: transformation-target-supervisor  \n",
        f"**Session ID**: {session_id}  \n",
        f"**Target**: {target_name}  \n",
        f"**Inspection Date**: {datetime.utcnow().isoformat()}Z  \n",
        f"**Inspection Round**: {check_round}  \n\n",
        f"## Verdict: {verdict}\n\n",
        f"**Checks Passed**: {passed}/20  \n",
        f"**Checks Failed**: {20 - passed}/20  \n\n",
        "## DoD Check Results\n\n",
        "| Check ID | Description | Status | Detail |\n",
        "|----------|-------------|--------|--------|\n",
    ]
    for r in results:
        lines.append(f"| {r['check_id']} | {r['description']} | {r['status']} | {r['detail']} |\n")
    with open(path, "w", encoding="utf-8") as f:
        f.writelines(lines)
    return path


def print_report(results: List[Dict], session_id: str, output_dir: str, check_round: int) -> int:
    passed = sum(1 for r in results if r["status"] == "PASS")
    failed = 20 - passed

    print("\n" + "=" * 70)
    print("  TRANSFORMATION TARGET SUPERVISOR — Inspection Report")
    print(f"  Session   : {session_id}")
    print(f"  Output Dir: {output_dir}")
    print(f"  Round     : {check_round}")
    print(f"  Timestamp : {datetime.utcnow().isoformat()}Z")
    print("=" * 70)
    for r in results:
        icon = "✓" if r["status"] == "PASS" else "✗"
        print(f"  {icon} [{r['check_id']}] {r['description']}")
        if r["status"] == "FAIL":
            print(f"      → {r['detail']}")
    print("=" * 70)
    print(f"  Result: {passed}/20 PASS  |  {failed} FAIL")
    verdict = "ALL CHECKS PASS — ready for PM Agent handoff" if failed == 0 else \
              f"{failed} checks failing — remediation required"
    print(f"  Verdict: {verdict}")
    print("=" * 70 + "\n")
    return 0 if failed == 0 else 1


def main():
    parser = argparse.ArgumentParser(description="transformation-target-supervisor inspection")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--session-id", required=True)
    parser.add_argument("--db-path", default=None)
    parser.add_argument("--round", type=int, default=1, dest="check_round")
    parser.add_argument("--save-report", action="store_true")
    parser.add_argument("--target-name", default="")
    args = parser.parse_args()

    db_path = args.db_path
    if db_path is None:
        base = os.path.dirname(os.path.abspath(args.output_dir))
        db_path = os.path.join(base, "memory", "agent_memory.db")

    if not os.path.isdir(args.output_dir):
        print(f"ERROR: output directory not found: {args.output_dir}", file=sys.stderr)
        return 1

    results = run_all(args.output_dir, args.session_id, db_path)

    if args.save_report:
        rpath = save_report(results, args.output_dir, args.session_id,
                            args.check_round, args.target_name)
        print(f"Inspection report saved: {rpath}")

    return print_report(results, args.session_id, args.output_dir, args.check_round)


if __name__ == "__main__":
    sys.exit(main())
