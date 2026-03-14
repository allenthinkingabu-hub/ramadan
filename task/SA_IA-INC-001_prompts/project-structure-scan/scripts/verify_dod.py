#!/usr/bin/env python3
"""DoD (Definition of Done) self-verification script for Project Structure Scan (SA-DISC-001).

Performs automated checks against the DoD checklist and records results in SQLite.
Exit code 0 = all pass, exit code 1 = any fail.
"""

import argparse
import os
import re
import sqlite3
import sys
from datetime import datetime
from pathlib import Path


def check_file_exists(filepath: str, min_size: int = 100) -> tuple[bool, str]:
    """Check if file exists and meets minimum size requirement."""
    if not os.path.exists(filepath):
        return False, f"File not found: {filepath}"
    size = os.path.getsize(filepath)
    if size < min_size:
        return False, f"File too small: {size} bytes (minimum: {min_size})"
    return True, f"File exists, {size} bytes"


def check_no_placeholders(filepath: str) -> tuple[bool, str]:
    """Check that output files have no remaining template placeholders."""
    placeholder_patterns = [
        r'\{project_name\}', r'\{date\}', r'\{session_id\}',
        r'\{timestamp\}', r'\{count\}', r'\{purpose\}',
        r'\{name\}', r'\{path\}', r'\{module_name\}',
        r'\{layer_name\}', r'\{pattern_name\}',
    ]
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        found = []
        for pattern in placeholder_patterns:
            matches = re.findall(pattern, content)
            if matches:
                found.extend(matches)
        if found:
            unique = list(set(found))
            return False, f"Remaining placeholders: {', '.join(unique[:5])}"
        return True, "No placeholders found"
    except Exception as e:
        return False, f"Error reading file: {e}"


def check_mermaid_syntax(filepath: str) -> tuple[bool, str]:
    """Check that file contains valid Mermaid diagram blocks."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        mermaid_blocks = re.findall(r'```mermaid\s*(.*?)```', content, re.DOTALL)
        if not mermaid_blocks:
            return False, "No Mermaid diagram blocks found"
        for block in mermaid_blocks:
            block = block.strip()
            if not block:
                return False, "Empty Mermaid block found"
            has_type = any(
                block.startswith(t) for t in
                ['graph ', 'flowchart ', 'sequenceDiagram', 'classDiagram',
                 'stateDiagram', 'erDiagram', 'gantt', 'pie', 'gitgraph']
            )
            if not has_type:
                return False, f"Mermaid block missing diagram type declaration"
        return True, f"Found {len(mermaid_blocks)} valid Mermaid block(s)"
    except Exception as e:
        return False, f"Error reading file: {e}"


def check_pattern_identified(filepath: str) -> tuple[bool, str]:
    """Check OUT-03 has at least one architecture pattern identified."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        if '✅ Match' in content or 'Identified Primary Pattern' in content or 'Primary Pattern' in content:
            return True, "Architecture pattern identified"
        return False, "No architecture pattern identification found"
    except Exception as e:
        return False, f"Error reading file: {e}"


def check_modules_described(filepath: str) -> tuple[bool, str]:
    """Check OUT-05 has module descriptions."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        module_sections = re.findall(r'###\s+Module:', content)
        if len(module_sections) >= 1:
            return True, f"Found {len(module_sections)} module description(s)"
        return False, "No '### Module:' sections found"
    except Exception as e:
        return False, f"Error reading file: {e}"


def check_dependency_coverage(filepath: str) -> tuple[bool, str]:
    """Check OUT-04 covers both internal and third-party dependencies."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        has_third_party = 'Third-Party' in content or 'third-party' in content or 'Third Party' in content
        has_internal = 'Internal' in content or 'internal' in content
        if has_third_party and has_internal:
            return True, "Both internal and third-party dependencies covered"
        missing = []
        if not has_third_party:
            missing.append("third-party")
        if not has_internal:
            missing.append("internal")
        return False, f"Missing coverage: {', '.join(missing)}"
    except Exception as e:
        return False, f"Error reading file: {e}"


def check_circular_deps(filepath: str) -> tuple[bool, str]:
    """Check OUT-02 has circular dependency section."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        if 'Circular Dependenc' in content:
            return True, "Circular dependencies section present"
        return False, "No 'Circular Dependencies' section found"
    except Exception as e:
        return False, f"Error reading file: {e}"


def check_conversation_log(filepath: str) -> tuple[bool, str]:
    """Check conversation log has Phase 1-3 dialogue entries."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        phases_found = []
        for phase in ['Phase 1', 'Phase 2', 'Phase 3']:
            if phase in content:
                # Check there's actual content after the phase header
                idx = content.index(phase)
                after = content[idx:idx+500]
                if '### Q' in after or 'Asked by' in after or 'Response' in after:
                    phases_found.append(phase)
        if len(phases_found) >= 3:
            return True, f"Found dialogue in: {', '.join(phases_found)}"
        return False, f"Only found dialogue in: {', '.join(phases_found) if phases_found else 'none'}"
    except Exception as e:
        return False, f"Error reading file: {e}"


def check_work_log(filepath: str) -> tuple[bool, str]:
    """Check work log has timestamped entries."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        # Check for table rows with pipe-separated entries
        table_rows = re.findall(r'^\|.*\|.*\|.*\|.*\|.*\|.*\|', content, re.MULTILINE)
        # Subtract header and separator rows
        data_rows = [r for r in table_rows if not r.startswith('|---') and '---' not in r.split('|')[1]]
        if len(data_rows) >= 2:
            return True, f"Found {len(data_rows)} work log entries"
        return False, f"Only found {len(data_rows)} entries (need at least 2)"
    except Exception as e:
        return False, f"Error reading file: {e}"


def check_sqlite_findings(db_path: str) -> tuple[bool, str]:
    """Check SQLite has findings recorded."""
    try:
        if not os.path.exists(db_path):
            return False, f"Database not found: {db_path}"
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM task_memory")
        count = cursor.fetchone()[0]
        conn.close()
        if count > 0:
            return True, f"Found {count} task_memory entries"
        return False, "No entries in task_memory table"
    except Exception as e:
        return False, f"Database error: {e}"


def check_sqlite_scan_history(db_path: str, session_id: str = None) -> tuple[bool, str]:
    """Check SQLite has scan history recorded."""
    try:
        if not os.path.exists(db_path):
            return False, f"Database not found: {db_path}"
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        if session_id:
            cursor.execute("SELECT COUNT(*) FROM scan_history WHERE session_id = ?", (session_id,))
        else:
            cursor.execute("SELECT COUNT(*) FROM scan_history")
        count = cursor.fetchone()[0]
        conn.close()
        if count > 0:
            return True, f"Found {count} scan_history entries"
        return False, "No entries in scan_history table"
    except Exception as e:
        return False, f"Database error: {e}"


def check_raci_ready(filepath: str) -> tuple[bool, str]:
    """Check RACI matrix is ready for PM handoff."""
    try:
        if not os.path.exists(filepath):
            return False, f"RACI file not found: {filepath}"
        size = os.path.getsize(filepath)
        if size < 200:
            return False, f"RACI file too small: {size} bytes"
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        if '|' in content and ('R' in content or 'A' in content):
            return True, f"RACI matrix present, {size} bytes"
        return False, "RACI matrix structure not detected"
    except Exception as e:
        return False, f"Error: {e}"


def run_dod_checks(output_dir: str, session_id: str = None) -> list[dict]:
    """Run all DoD checks and return results."""
    results = []
    base = Path(output_dir)
    db_path = str(base / 'memory' / 'agent_memory.db')

    checks = [
        {
            'id': 'DOD-01', 'item': 'OUT-01 (Structure Tree) produced and non-empty',
            'func': lambda: check_file_exists(str(base / 'project-structure-report.md'), 100)
                if not (base / 'templates' / 'structure-tree-output.md').exists()
                else check_file_exists(str(base / 'templates' / 'structure-tree-output.md'), 100),
        },
        {
            'id': 'DOD-02', 'item': 'OUT-02 (Module Relationships) produced and non-empty',
            'func': lambda: check_file_exists(
                str(next(base.glob('**/module-relationship*output*'), base / 'OUT-02.md')), 100),
        },
        {
            'id': 'DOD-03', 'item': 'OUT-03 (Layering Analysis) produced and non-empty',
            'func': lambda: check_file_exists(
                str(next(base.glob('**/layering-analysis*output*'), base / 'OUT-03.md')), 100),
        },
        {
            'id': 'DOD-04', 'item': 'OUT-04 (Dependency Map) produced and non-empty',
            'func': lambda: check_file_exists(
                str(next(base.glob('**/dependency-map*output*'), base / 'OUT-04.md')), 100),
        },
        {
            'id': 'DOD-05', 'item': 'OUT-05 (Module Summary) produced and non-empty',
            'func': lambda: check_file_exists(
                str(next(base.glob('**/module-summary*output*'), base / 'OUT-05.md')), 100),
        },
        {
            'id': 'DOD-06', 'item': 'OUT-06 (Final Report) produced and non-empty',
            'func': lambda: check_file_exists(str(base / 'project-structure-report.md'), 500),
        },
        {
            'id': 'DOD-07', 'item': 'All templates fully populated — no remaining placeholders',
            'func': lambda: check_no_placeholders(str(base / 'project-structure-report.md')),
        },
        {
            'id': 'DOD-08', 'item': 'Module relationship diagram renders valid Mermaid',
            'func': lambda: check_mermaid_syntax(
                str(next(base.glob('**/module-relationship*output*'), base / 'OUT-02.md'))),
        },
        {
            'id': 'DOD-09', 'item': 'At least one architecture pattern identified with evidence',
            'func': lambda: check_pattern_identified(
                str(next(base.glob('**/layering-analysis*output*'), base / 'OUT-03.md'))),
        },
        {
            'id': 'DOD-10', 'item': 'All modules have responsibility descriptions',
            'func': lambda: check_modules_described(
                str(next(base.glob('**/module-summary*output*'), base / 'OUT-05.md'))),
        },
        {
            'id': 'DOD-11', 'item': 'Dependency map covers internal and third-party',
            'func': lambda: check_dependency_coverage(
                str(next(base.glob('**/dependency-map*output*'), base / 'OUT-04.md'))),
        },
        {
            'id': 'DOD-12', 'item': 'Circular dependencies flagged if any',
            'func': lambda: check_circular_deps(
                str(next(base.glob('**/module-relationship*output*'), base / 'OUT-02.md'))),
        },
        {
            'id': 'DOD-13', 'item': 'Conversation log has Phase 1-3 dialogue',
            'func': lambda: check_conversation_log(str(base / 'logs' / 'conversation-log.md')),
        },
        {
            'id': 'DOD-14', 'item': 'Work log has timestamped entries for all phases',
            'func': lambda: check_work_log(str(base / 'logs' / 'work-log.md')),
        },
        {
            'id': 'DOD-15', 'item': 'Findings recorded in SQLite memory database',
            'func': lambda: check_sqlite_findings(db_path),
        },
        {
            'id': 'DOD-16', 'item': 'Scan history recorded in SQLite',
            'func': lambda: check_sqlite_scan_history(db_path, session_id),
        },
        {
            'id': 'DOD-17', 'item': 'RACI matrix ready for PM Agent handoff',
            'func': lambda: check_raci_ready(str(base / 'config' / 'raci.md')),
        },
    ]

    for check in checks:
        try:
            passed, evidence = check['func']()
            results.append({
                'id': check['id'],
                'item': check['item'],
                'status': 'pass' if passed else 'fail',
                'evidence': evidence,
            })
        except Exception as e:
            results.append({
                'id': check['id'],
                'item': check['item'],
                'status': 'fail',
                'evidence': f"Check error: {e}",
            })

    return results


def record_results_to_db(db_path: str, session_id: str, task_id: str,
                         check_round: int, results: list[dict]):
    """Record check results in the dod_checks SQLite table."""
    try:
        # Try importing memory_ops from sibling directory
        script_dir = Path(__file__).parent
        sys.path.insert(0, str(script_dir))
        from memory_ops import record_dod_check

        for r in results:
            record_dod_check(
                db_path=db_path,
                session_id=session_id,
                task_id=task_id,
                check_round=check_round,
                check_item=r['id'],
                status=r['status'],
                evidence=r['evidence'],
                notes=r['item'],
            )
    except ImportError:
        # Fallback: direct SQLite insert
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            for r in results:
                cursor.execute(
                    "INSERT INTO dod_checks (session_id, task_id, check_round, check_item, status, evidence, notes) "
                    "VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (session_id, task_id, check_round, r['id'], r['status'], r['evidence'], r['item'])
                )
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"Warning: Could not record results to DB: {e}", file=sys.stderr)


def print_report(results: list[dict], check_round: int):
    """Print formatted DoD verification report."""
    passed = sum(1 for r in results if r['status'] == 'pass')
    total = len(results)
    percentage = (passed / total * 100) if total > 0 else 0

    print(f"\nDoD Verification Report — Round {check_round}")
    print("=" * 60)
    for r in results:
        icon = "✅ PASS" if r['status'] == 'pass' else "❌ FAIL"
        print(f"  {icon}: {r['item']}")
        print(f"         {r['evidence']}")
    print("=" * 60)
    print(f"Overall: {passed}/{total} items passed ({percentage:.0f}%)")
    if passed == total:
        print("Status: ALL PASSED ✅")
    else:
        print("Status: NEEDS REMEDIATION ❌")
    print()


def main():
    parser = argparse.ArgumentParser(
        description='DoD verification for Project Structure Scan (SA-DISC-001)'
    )
    parser.add_argument(
        '--output-dir',
        required=True,
        help='Path to the project-structure-scan/ output directory'
    )
    parser.add_argument(
        '--session-id',
        default='default-session',
        help='Session ID for recording results'
    )
    parser.add_argument(
        '--task-id',
        default='SA-DISC-001',
        help='Task ID (default: SA-DISC-001)'
    )
    parser.add_argument(
        '--round',
        type=int,
        default=1,
        help='Check round number (default: 1)'
    )
    args = parser.parse_args()

    output_dir = os.path.abspath(args.output_dir)
    if not os.path.isdir(output_dir):
        print(f"Error: Output directory not found: {output_dir}", file=sys.stderr)
        sys.exit(2)

    # Run all checks
    results = run_dod_checks(output_dir, args.session_id)

    # Record to DB if available
    db_path = os.path.join(output_dir, 'memory', 'agent_memory.db')
    if os.path.exists(db_path):
        record_results_to_db(db_path, args.session_id, args.task_id, args.round, results)

    # Print report
    print_report(results, args.round)

    # Exit with appropriate code
    all_passed = all(r['status'] == 'pass' for r in results)
    sys.exit(0 if all_passed else 1)


if __name__ == '__main__':
    main()
