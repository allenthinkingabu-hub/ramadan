#!/usr/bin/env python3
"""
Project Structure Scan — Automated Inspection Script

Performs 22 automated checks against the output of the Project Structure Scan Agent
(SA-DISC-001). Generates a structured inspection report.

Usage:
    python inspect.py --output-dir /path/to/project-structure-scan --report-dir /path/to/reports --round 1

Exit codes:
    0 - All 22 checks passed
    1 - One or more checks failed
"""

import argparse
import os
import re
import sqlite3
import sys
from datetime import datetime
from pathlib import Path


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def file_exists(path: str) -> bool:
    return os.path.isfile(path)


def dir_exists(path: str) -> bool:
    return os.path.isdir(path)


def file_size(path: str) -> int:
    try:
        return os.path.getsize(path)
    except OSError:
        return 0


def read_file(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            return f.read()
    except Exception:
        return ""


def count_lines_matching(text: str, pattern: str) -> int:
    return len(re.findall(pattern, text, re.MULTILINE))


def count_table_rows(text: str) -> int:
    """Count markdown table data rows (lines starting with |, excluding header separator)."""
    rows = 0
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("|") and not re.match(r"^\|[\s\-:|]+\|$", stripped):
            rows += 1
    # Subtract header row if present
    return max(rows - 1, 0) if rows > 0 else 0


def has_placeholder(text: str) -> bool:
    """Check for unreplaced template placeholders."""
    placeholders = [r"\{project_name\}", r"\{date\}", r"\{session_id\}"]
    for p in placeholders:
        if re.search(p, text):
            return True
    return False


# ---------------------------------------------------------------------------
# Check result container
# ---------------------------------------------------------------------------

class CheckResult:
    def __init__(self, check_id: str, category: str, description: str):
        self.check_id = check_id
        self.category = category
        self.description = description
        self.status = "fail"  # "pass" or "fail"
        self.evidence = ""

    def passed(self, evidence: str = ""):
        self.status = "pass"
        self.evidence = evidence

    def failed(self, evidence: str = ""):
        self.status = "fail"
        self.evidence = evidence

    @property
    def is_pass(self) -> bool:
        return self.status == "pass"


# ---------------------------------------------------------------------------
# Individual checks
# ---------------------------------------------------------------------------

def chk_01(output_dir: str) -> CheckResult:
    r = CheckResult("CHK-01", "Configuration", "Trigger config exists with >= 3 triggers")
    candidates = [
        os.path.join(output_dir, "trigger-config.md"),
        os.path.join(output_dir, "triggers.md"),
        os.path.join(output_dir, "config", "triggers.md"),
    ]
    for path in candidates:
        if file_exists(path):
            text = read_file(path)
            count = count_lines_matching(text, r"(?i)^\s*[-*]\s+.+trigger")
            # Also try table rows
            if count < 3:
                count = max(count, count_table_rows(text))
            if count >= 3:
                r.passed(f"Found {count} triggers in {os.path.basename(path)}")
            else:
                r.failed(f"File exists but only {count} triggers found (need >= 3)")
            return r
    # Also search SKILL.md or any config file
    skill_path = os.path.join(output_dir, "SKILL.md")
    if file_exists(skill_path):
        text = read_file(skill_path)
        trigger_section = re.search(r"(?i)##\s*trigger.*?\n(.*?)(?=\n##|\Z)", text, re.DOTALL)
        if trigger_section:
            count = count_lines_matching(trigger_section.group(1), r"^\s*[-*]\s+")
            if count < 3:
                count = max(count, count_table_rows(trigger_section.group(1)))
            if count >= 3:
                r.passed(f"Found {count} triggers in SKILL.md trigger section")
                return r
    r.failed("No trigger config file found")
    return r


def chk_02(output_dir: str) -> CheckResult:
    r = CheckResult("CHK-02", "RACI", "RACI matrix with >= 6 roles")
    for fname in os.listdir(output_dir) if dir_exists(output_dir) else []:
        fpath = os.path.join(output_dir, fname)
        if not os.path.isfile(fpath):
            continue
        text = read_file(fpath)
        if re.search(r"(?i)raci", text):
            # Count columns in first table header as roles
            header_match = re.search(r"^\|(.+)\|", text, re.MULTILINE)
            if header_match:
                cols = [c.strip() for c in header_match.group(1).split("|") if c.strip()]
                if len(cols) >= 6:
                    r.passed(f"RACI matrix found in {fname} with {len(cols)} columns")
                    return r
                else:
                    r.failed(f"RACI table in {fname} has {len(cols)} columns (need >= 6)")
                    return r
    # Search in SKILL.md
    skill_path = os.path.join(output_dir, "SKILL.md")
    if file_exists(skill_path):
        text = read_file(skill_path)
        if re.search(r"(?i)raci", text):
            header_match = re.search(r"(?i)raci.*?\n.*?\|(.+)\|", text, re.DOTALL)
            if header_match:
                cols = [c.strip() for c in header_match.group(1).split("|") if c.strip()]
                if len(cols) >= 6:
                    r.passed(f"RACI matrix found in SKILL.md with {len(cols)} columns")
                    return r
    r.failed("No RACI matrix found with >= 6 roles")
    return r


def chk_03(output_dir: str) -> CheckResult:
    r = CheckResult("CHK-03", "Capabilities", "Skills list >= 9 items")
    for fname in _scan_files(output_dir):
        text = read_file(os.path.join(output_dir, fname))
        skills_section = re.search(r"(?i)##\s*skills.*?\n(.*?)(?=\n##|\Z)", text, re.DOTALL)
        if skills_section:
            count = count_lines_matching(skills_section.group(1), r"^\s*[-*]\s+")
            if count < 9:
                count = max(count, count_table_rows(skills_section.group(1)))
            if count >= 9:
                r.passed(f"Found {count} skills in {fname}")
                return r
            else:
                r.failed(f"Skills section in {fname} has {count} items (need >= 9)")
                return r
    r.failed("No skills section found")
    return r


def chk_04(output_dir: str) -> CheckResult:
    r = CheckResult("CHK-04", "Knowledge", "Knowledge base >= 7 items")
    for fname in _scan_files(output_dir):
        text = read_file(os.path.join(output_dir, fname))
        kb_section = re.search(r"(?i)##\s*knowledge.*?\n(.*?)(?=\n##|\Z)", text, re.DOTALL)
        if kb_section:
            count = count_lines_matching(kb_section.group(1), r"^\s*[-*]\s+")
            if count < 7:
                count = max(count, count_table_rows(kb_section.group(1)))
            if count >= 7:
                r.passed(f"Found {count} knowledge base items in {fname}")
                return r
            else:
                r.failed(f"Knowledge base in {fname} has {count} items (need >= 7)")
                return r
    r.failed("No knowledge base section found")
    return r


def chk_05(output_dir: str) -> CheckResult:
    r = CheckResult("CHK-05", "Tools", "Tools list >= 5 tools")
    for fname in _scan_files(output_dir):
        text = read_file(os.path.join(output_dir, fname))
        tools_section = re.search(r"(?i)##\s*tools\b.*?\n(.*?)(?=\n##|\Z)", text, re.DOTALL)
        if tools_section:
            count = count_lines_matching(tools_section.group(1), r"^\s*[-*]\s+")
            if count < 5:
                count = max(count, count_table_rows(tools_section.group(1)))
            if count >= 5:
                r.passed(f"Found {count} tools in {fname}")
                return r
            else:
                r.failed(f"Tools section in {fname} has {count} items (need >= 5)")
                return r
    r.failed("No tools section found")
    return r


def chk_06(output_dir: str) -> CheckResult:
    r = CheckResult("CHK-06", "Tools", "MCP tools >= 3 tools")
    for fname in _scan_files(output_dir):
        text = read_file(os.path.join(output_dir, fname))
        mcp_section = re.search(r"(?i)##\s*mcp.*?tool.*?\n(.*?)(?=\n##|\Z)", text, re.DOTALL)
        if mcp_section:
            count = count_lines_matching(mcp_section.group(1), r"^\s*[-*]\s+")
            if count < 3:
                count = max(count, count_table_rows(mcp_section.group(1)))
            if count >= 3:
                r.passed(f"Found {count} MCP tools in {fname}")
                return r
            else:
                r.failed(f"MCP tools section in {fname} has {count} items (need >= 3)")
                return r
    r.failed("No MCP tools section found")
    return r


def chk_07(output_dir: str) -> CheckResult:
    r = CheckResult("CHK-07", "Templates", "All 6 template files exist, each > 100 bytes")
    templates_dir = os.path.join(output_dir, "templates")
    if not dir_exists(templates_dir):
        r.failed("templates/ directory does not exist")
        return r
    files = [f for f in os.listdir(templates_dir) if os.path.isfile(os.path.join(templates_dir, f))]
    if len(files) < 6:
        r.failed(f"templates/ has {len(files)} files (need 6)")
        return r
    small_files = []
    for f in files[:6]:
        sz = file_size(os.path.join(templates_dir, f))
        if sz <= 100:
            small_files.append(f"{f} ({sz}B)")
    if small_files:
        r.failed(f"Files too small (<= 100 bytes): {', '.join(small_files)}")
    else:
        r.passed(f"All {len(files)} template files exist and are > 100 bytes")
    return r


def chk_08(output_dir: str) -> CheckResult:
    r = CheckResult("CHK-08", "SOP", "SOP defines 5 phases with sub-steps")
    for fname in _scan_files(output_dir):
        text = read_file(os.path.join(output_dir, fname))
        if re.search(r"(?i)(sop|standard operating procedure)", text):
            phases = re.findall(r"(?i)##\s*phase\s*\d", text)
            if not phases:
                phases = re.findall(r"(?i)(?:phase|stage)\s*\d", text)
            if len(phases) >= 5:
                r.passed(f"Found {len(phases)} phases in {fname}")
                return r
            else:
                r.failed(f"SOP in {fname} has {len(phases)} phases (need 5)")
                return r
    r.failed("No SOP document found with phase definitions")
    return r


def chk_09(output_dir: str) -> CheckResult:
    r = CheckResult("CHK-09", "Quality", "DoD has >= 12 checkable items")
    for fname in _scan_files(output_dir):
        text = read_file(os.path.join(output_dir, fname))
        dod_section = re.search(r"(?i)##\s*definition\s+of\s+done.*?\n(.*?)(?=\n##|\Z)", text, re.DOTALL)
        if dod_section:
            count = count_lines_matching(dod_section.group(1), r"^\s*[-*]\s+\[.\]")
            if count < 12:
                # Also count plain list items
                count = max(count, count_lines_matching(dod_section.group(1), r"^\s*[-*]\s+"))
            if count >= 12:
                r.passed(f"DoD has {count} checkable items")
                return r
            else:
                r.failed(f"DoD has {count} items (need >= 12)")
                return r
    r.failed("No Definition of Done section found")
    return r


def chk_10(output_dir: str) -> CheckResult:
    r = CheckResult("CHK-10", "Quality", "DoR has >= 8 prerequisites")
    for fname in _scan_files(output_dir):
        text = read_file(os.path.join(output_dir, fname))
        dor_section = re.search(r"(?i)##\s*definition\s+of\s+ready.*?\n(.*?)(?=\n##|\Z)", text, re.DOTALL)
        if dor_section:
            count = count_lines_matching(dor_section.group(1), r"^\s*[-*]\s+")
            if count >= 8:
                r.passed(f"DoR has {count} prerequisites")
                return r
            else:
                r.failed(f"DoR has {count} prerequisites (need >= 8)")
                return r
    r.failed("No Definition of Ready section found")
    return r


def chk_11(output_dir: str) -> CheckResult:
    r = CheckResult("CHK-11", "Logging", "Conversation log has Phase 1-3 dialogue")
    candidates = [
        os.path.join(output_dir, "conversation-log.md"),
        os.path.join(output_dir, "logs", "conversation-log.md"),
        os.path.join(output_dir, "conversation_log.md"),
    ]
    for path in candidates:
        if file_exists(path):
            text = read_file(path)
            phases_found = []
            for i in range(1, 4):
                if re.search(rf"(?i)phase\s*{i}", text):
                    phases_found.append(i)
            if len(phases_found) == 3:
                r.passed("Conversation log contains Phase 1, 2, and 3 entries")
            else:
                missing = [i for i in [1, 2, 3] if i not in phases_found]
                r.failed(f"Missing Phase {missing} in conversation log")
            return r
    r.failed("No conversation log file found")
    return r


def chk_12(output_dir: str) -> CheckResult:
    r = CheckResult("CHK-12", "Logging", "Work log has timestamped entries")
    candidates = [
        os.path.join(output_dir, "work-log.md"),
        os.path.join(output_dir, "logs", "work-log.md"),
        os.path.join(output_dir, "work_log.md"),
    ]
    for path in candidates:
        if file_exists(path):
            text = read_file(path)
            timestamps = re.findall(r"\d{4}-\d{2}-\d{2}", text)
            if timestamps:
                r.passed(f"Found {len(timestamps)} timestamped entries")
            else:
                r.failed("Work log exists but no timestamped entries found")
            return r
    r.failed("No work log file found")
    return r


def chk_13(output_dir: str) -> CheckResult:
    r = CheckResult("CHK-13", "Quality", "DoD self-verification passed (query dod_checks)")
    db_path = os.path.join(output_dir, "agent_memory.db")
    if not file_exists(db_path):
        r.failed("agent_memory.db not found")
        return r
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        # Check if dod_checks table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='dod_checks'")
        if not cursor.fetchone():
            r.failed("dod_checks table does not exist in agent_memory.db")
            conn.close()
            return r
        cursor.execute("SELECT COUNT(*) FROM dod_checks WHERE status != 'passed'")
        failed_count = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM dod_checks")
        total = cursor.fetchone()[0]
        conn.close()
        if total == 0:
            r.failed("dod_checks table is empty")
        elif failed_count == 0:
            r.passed(f"All {total} DoD checks have status = 'passed'")
        else:
            r.failed(f"{failed_count} of {total} DoD checks have not passed")
    except sqlite3.Error as e:
        r.failed(f"SQLite error: {e}")
    return r


def chk_14(output_dir: str) -> CheckResult:
    r = CheckResult("CHK-14", "Output", "OUT-01 exists, non-empty, no placeholders")
    candidates = _find_output_file(output_dir, "OUT-01", "directory-tree")
    for path in candidates:
        if file_exists(path):
            text = read_file(path)
            if len(text.strip()) == 0:
                r.failed(f"{os.path.basename(path)} is empty")
                return r
            if has_placeholder(text):
                r.failed(f"{os.path.basename(path)} contains unreplaced placeholders")
                return r
            r.passed(f"{os.path.basename(path)} exists, {len(text)} chars, no placeholders")
            return r
    r.failed("OUT-01 file not found")
    return r


def chk_15(output_dir: str) -> CheckResult:
    r = CheckResult("CHK-15", "Output", "OUT-02 exists, valid Mermaid")
    candidates = _find_output_file(output_dir, "OUT-02", "diagram")
    for path in candidates:
        if file_exists(path):
            text = read_file(path)
            if re.search(r"```mermaid", text):
                r.passed(f"{os.path.basename(path)} contains Mermaid diagram block")
            else:
                r.failed(f"{os.path.basename(path)} exists but no ```mermaid block found")
            return r
    r.failed("OUT-02 file not found")
    return r


def chk_16(output_dir: str) -> CheckResult:
    r = CheckResult("CHK-16", "Output", "OUT-03 exists, >= 1 pattern identified")
    candidates = _find_output_file(output_dir, "OUT-03", "pattern")
    for path in candidates:
        if file_exists(path):
            text = read_file(path)
            if len(text.strip()) > 50:
                r.passed(f"{os.path.basename(path)} exists with content ({len(text)} chars)")
            else:
                r.failed(f"{os.path.basename(path)} exists but content too short")
            return r
    r.failed("OUT-03 file not found")
    return r


def chk_17(output_dir: str) -> CheckResult:
    r = CheckResult("CHK-17", "Output", "OUT-04 covers internal + third-party deps")
    candidates = _find_output_file(output_dir, "OUT-04", "dependenc")
    for path in candidates:
        if file_exists(path):
            text = read_file(path)
            has_internal = bool(re.search(r"(?i)internal", text))
            has_third = bool(re.search(r"(?i)third.party|external|npm|pip|maven|gradle", text))
            if has_internal and has_third:
                r.passed(f"{os.path.basename(path)} covers both internal and third-party deps")
            elif not has_internal:
                r.failed(f"{os.path.basename(path)} missing internal dependency coverage")
            else:
                r.failed(f"{os.path.basename(path)} missing third-party dependency coverage")
            return r
    r.failed("OUT-04 file not found")
    return r


def chk_18(output_dir: str) -> CheckResult:
    r = CheckResult("CHK-18", "Output", "OUT-05 all modules have descriptions")
    candidates = _find_output_file(output_dir, "OUT-05", "module")
    for path in candidates:
        if file_exists(path):
            text = read_file(path)
            # Look for module headers and check they have following content
            modules = re.findall(r"(?i)###?\s+.+module", text)
            if not modules:
                # Try table-based format
                rows = count_table_rows(text)
                if rows > 0:
                    r.passed(f"{os.path.basename(path)} has {rows} module entries in table")
                    return r
            if len(text.strip()) > 100:
                r.passed(f"{os.path.basename(path)} exists with module descriptions ({len(text)} chars)")
            else:
                r.failed(f"{os.path.basename(path)} exists but content insufficient")
            return r
    r.failed("OUT-05 file not found")
    return r


def chk_19(output_dir: str) -> CheckResult:
    r = CheckResult("CHK-19", "Output", "OUT-06 exists, > 500 bytes, executive summary")
    candidates = _find_output_file(output_dir, "OUT-06", "summary|report")
    for path in candidates:
        if file_exists(path):
            sz = file_size(path)
            if sz <= 500:
                r.failed(f"{os.path.basename(path)} is only {sz} bytes (need > 500)")
                return r
            text = read_file(path)
            if re.search(r"(?i)executive\s+summary", text):
                r.passed(f"{os.path.basename(path)} is {sz} bytes with executive summary")
            else:
                r.failed(f"{os.path.basename(path)} is {sz} bytes but no executive summary section")
            return r
    r.failed("OUT-06 file not found")
    return r


def chk_20(output_dir: str) -> CheckResult:
    r = CheckResult("CHK-20", "Memory", "SQLite DB exists and has entries")
    db_path = os.path.join(output_dir, "agent_memory.db")
    if not file_exists(db_path):
        r.failed("agent_memory.db not found")
        return r
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()
        if not tables:
            r.failed("agent_memory.db has no tables")
            conn.close()
            return r
        total_rows = 0
        for (table_name,) in tables:
            try:
                cursor.execute(f"SELECT COUNT(*) FROM [{table_name}]")
                total_rows += cursor.fetchone()[0]
            except sqlite3.Error:
                pass
        conn.close()
        if total_rows > 0:
            r.passed(f"agent_memory.db has {len(tables)} tables with {total_rows} total rows")
        else:
            r.failed(f"agent_memory.db has {len(tables)} tables but 0 rows")
    except sqlite3.Error as e:
        r.failed(f"SQLite error: {e}")
    return r


def chk_21(output_dir: str) -> CheckResult:
    r = CheckResult("CHK-21", "Research", "research/ has >= 1 file")
    research_dir = os.path.join(output_dir, "research")
    if not dir_exists(research_dir):
        r.failed("research/ directory does not exist")
        return r
    files = [f for f in os.listdir(research_dir) if os.path.isfile(os.path.join(research_dir, f))]
    if len(files) >= 1:
        r.passed(f"research/ contains {len(files)} file(s)")
    else:
        r.failed("research/ directory is empty")
    return r


def chk_22(output_dir: str) -> CheckResult:
    r = CheckResult("CHK-22", "Dialogue", "phase1-questions.md and phase3-questions.md exist")
    p1 = os.path.join(output_dir, "phase1-questions.md")
    p3 = os.path.join(output_dir, "phase3-questions.md")
    missing = []
    if not file_exists(p1):
        missing.append("phase1-questions.md")
    if not file_exists(p3):
        missing.append("phase3-questions.md")
    if not missing:
        r.passed("Both phase1-questions.md and phase3-questions.md exist")
    else:
        r.failed(f"Missing: {', '.join(missing)}")
    return r


# ---------------------------------------------------------------------------
# Utility helpers
# ---------------------------------------------------------------------------

def _scan_files(directory: str) -> list:
    """Return list of filenames in directory (non-recursive, files only)."""
    if not dir_exists(directory):
        return []
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]


def _find_output_file(output_dir: str, out_id: str, name_pattern: str) -> list:
    """Find candidate output files matching OUT-XX or name pattern."""
    candidates = []
    outputs_dir = os.path.join(output_dir, "outputs")
    search_dirs = [output_dir]
    if dir_exists(outputs_dir):
        search_dirs.insert(0, outputs_dir)
    for d in search_dirs:
        if not dir_exists(d):
            continue
        for f in os.listdir(d):
            fpath = os.path.join(d, f)
            if not os.path.isfile(fpath):
                continue
            if out_id.lower().replace("-", "") in f.lower().replace("-", ""):
                candidates.append(fpath)
            elif re.search(name_pattern, f, re.IGNORECASE):
                candidates.append(fpath)
    return candidates


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------

def generate_report(results: list, output_dir: str, report_dir: str, round_num: int) -> str:
    """Generate markdown inspection report and return its path."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    passed = sum(1 for r in results if r.is_pass)
    failed = len(results) - passed
    rate = round(passed / len(results) * 100, 1) if results else 0

    if failed == 0:
        verdict = "ALL PASSED"
    elif round_num >= 3:
        verdict = "ESCALATED"
    else:
        verdict = "NEEDS REMEDIATION"

    lines = []
    lines.append("# Inspection Report\n")
    lines.append("## Header\n")
    lines.append("| Field | Value |")
    lines.append("|-------|-------|")
    lines.append(f"| Inspection Time | {now} |")
    lines.append(f"| Round | {round_num} |")
    lines.append(f"| Output Directory | {output_dir} |")
    lines.append("| Inspector | Project Structure Scan Supervisor (Automated) |")
    lines.append("")
    lines.append("---\n")
    lines.append("## Results\n")
    lines.append("| Check ID | Category | Check Item | Status | Evidence / Notes |")
    lines.append("|----------|----------|------------|--------|------------------|")
    for r in results:
        status_icon = "PASS" if r.is_pass else "FAIL"
        evidence = r.evidence.replace("|", "/")
        lines.append(f"| {r.check_id} | {r.category} | {r.description} | {status_icon} | {evidence} |")
    lines.append("")
    lines.append("---\n")
    lines.append("## Summary\n")
    lines.append("| Metric | Value |")
    lines.append("|--------|-------|")
    lines.append(f"| Total Checks | {len(results)} |")
    lines.append(f"| Passed | {passed} |")
    lines.append(f"| Failed | {failed} |")
    lines.append(f"| Pass Rate | {rate}% |")
    lines.append("")
    lines.append("---\n")
    lines.append("## Failed Items — Remediation Required\n")
    failed_results = [r for r in results if not r.is_pass]
    if failed_results:
        lines.append("| Check ID | Check Item | Failure Reason | Suggested Remediation |")
        lines.append("|----------|------------|----------------|----------------------|")
        for r in failed_results:
            evidence = r.evidence.replace("|", "/")
            lines.append(f"| {r.check_id} | {r.description} | {evidence} | Review and fix the identified issue |")
    else:
        lines.append("No failed items. All checks passed.")
    lines.append("")
    lines.append("---\n")
    lines.append(f"## Conclusion\n")
    lines.append(f"**Verdict: {verdict}**\n")
    if verdict == "ALL PASSED":
        lines.append("All 22 checks passed. Output is ready for PM Agent handoff.")
    elif verdict == "ESCALATED":
        lines.append("Maximum remediation rounds (3) reached with remaining failures. Escalating to human operator / PM Agent for manual review.")
    else:
        lines.append("One or more checks failed. Failed items have been sent back to the Scan Agent for correction. Re-inspection will follow.")

    report_content = "\n".join(lines) + "\n"
    os.makedirs(report_dir, exist_ok=True)
    report_path = os.path.join(report_dir, f"inspection-report-round-{round_num}.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report_content)
    return report_path


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Project Structure Scan — Automated Inspection (22 checks)"
    )
    parser.add_argument(
        "--output-dir",
        required=True,
        help="Path to project-structure-scan/ output directory",
    )
    parser.add_argument(
        "--report-dir",
        default=".",
        help="Path to write inspection report (default: current directory)",
    )
    parser.add_argument(
        "--round",
        type=int,
        default=1,
        help="Inspection round number (default: 1)",
    )
    args = parser.parse_args()

    output_dir = os.path.abspath(args.output_dir)
    report_dir = os.path.abspath(args.report_dir)

    if not dir_exists(output_dir):
        print(f"ERROR: Output directory does not exist: {output_dir}", file=sys.stderr)
        sys.exit(1)

    # Run all 22 checks
    checks = [
        chk_01, chk_02, chk_03, chk_04, chk_05, chk_06,
        chk_07, chk_08, chk_09, chk_10, chk_11, chk_12,
        chk_13, chk_14, chk_15, chk_16, chk_17, chk_18,
        chk_19, chk_20, chk_21, chk_22,
    ]

    results = []
    for check_fn in checks:
        try:
            result = check_fn(output_dir)
        except Exception as e:
            # If a check crashes, mark as fail with error details
            check_id = check_fn.__name__.replace("chk_", "CHK-")
            result = CheckResult(check_id, "Error", check_fn.__name__)
            result.failed(f"Exception during check: {e}")
        results.append(result)

    # Generate report
    report_path = generate_report(results, output_dir, report_dir, args.round)

    # Print summary
    passed = sum(1 for r in results if r.is_pass)
    failed = len(results) - passed
    rate = round(passed / len(results) * 100, 1)

    print(f"\n{'='*60}")
    print(f"  INSPECTION REPORT — Round {args.round}")
    print(f"{'='*60}")
    print(f"  Output directory: {output_dir}")
    print(f"  Passed: {passed}/22  |  Failed: {failed}/22  |  Rate: {rate}%")
    print(f"{'='*60}")

    if failed > 0:
        print("\n  Failed checks:")
        for r in results:
            if not r.is_pass:
                print(f"    {r.check_id}: {r.description}")
                print(f"      -> {r.evidence}")
        print()

    print(f"  Full report: {report_path}")

    if rate == 100:
        print("\n  VERDICT: ALL PASSED — Ready for PM Agent handoff.")
    elif args.round >= 3:
        print("\n  VERDICT: ESCALATED — Max remediation rounds reached.")
    else:
        print(f"\n  VERDICT: NEEDS REMEDIATION — Re-run with --round {args.round + 1} after fixes.")

    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
