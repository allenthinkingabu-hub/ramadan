#!/usr/bin/env python3
"""
memory_ops.py — SA-TRF-001: Transformation Target Current State Analysis
Memory CRUD operations for the agent's SQLite memory database.

Usage (as a module):
    from scripts.memory_ops import MemoryOps
    mem = MemoryOps(db_path="memory/agent_memory.db", session_id="session-123")
    mem.record_finding(title="...", body="...", phase="phase4", category="behavior")

Usage (CLI):
    python scripts/memory_ops.py load-history --project-name MyApp --target-name PaymentService
    python scripts/memory_ops.py query --session-id SESSION --type finding --phase phase4
"""

import argparse
import json
import os
import sqlite3
import sys
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional


DB_PATH = os.path.join(os.path.dirname(__file__), "..", "memory", "agent_memory.db")
CONFIDENCE_DECAY_RATE = 0.2    # per 90-day interval
CONFIDENCE_DECAY_DAYS = 90


class MemoryOps:
    """Facade for all SQLite memory operations required by the SA-TRF-001 agent."""

    def __init__(self, db_path: str = DB_PATH, session_id: str = ""):
        self.db_path = os.path.abspath(db_path)
        self.session_id = session_id
        self._conn: Optional[sqlite3.Connection] = None

    # ------------------------------------------------------------------
    # Connection management
    # ------------------------------------------------------------------

    def _get_conn(self) -> sqlite3.Connection:
        if self._conn is None:
            if not os.path.exists(self.db_path):
                raise FileNotFoundError(
                    f"Database not found: {self.db_path}. Run init_memory.py first."
                )
            self._conn = sqlite3.connect(self.db_path)
            self._conn.row_factory = sqlite3.Row
            self._conn.execute("PRAGMA journal_mode=WAL")
            self._conn.execute("PRAGMA foreign_keys=ON")
        return self._conn

    def close(self) -> None:
        if self._conn:
            self._conn.close()
            self._conn = None

    def __enter__(self):
        return self

    def __exit__(self, *_):
        self.close()

    # ------------------------------------------------------------------
    # task_memory write operations
    # ------------------------------------------------------------------

    def _insert_memory(self, memory_type: str, title: str, body: str, **kwargs) -> int:
        conn = self._get_conn()
        cur = conn.execute("""
            INSERT INTO task_memory
                (session_id, project_name, target_name, target_path,
                 memory_type, phase, category, title, body,
                 confidence, severity, source_file, source_line, tags)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            self.session_id,
            kwargs.get("project_name"),
            kwargs.get("target_name"),
            kwargs.get("target_path"),
            memory_type,
            kwargs.get("phase"),
            kwargs.get("category"),
            title,
            body,
            kwargs.get("confidence", 1.0),
            kwargs.get("severity"),
            kwargs.get("source_file"),
            kwargs.get("source_line"),
            kwargs.get("tags"),
        ))
        conn.commit()
        return cur.lastrowid

    def record_finding(self, title: str, body: str, **kwargs) -> int:
        """Record an investigation finding (Step 4)."""
        return self._insert_memory("finding", title, body, **kwargs)

    def record_constraint(self, title: str, body: str, **kwargs) -> int:
        """Record a hard or soft constraint."""
        return self._insert_memory("constraint", title, body, **kwargs)

    def record_risk(self, title: str, body: str, **kwargs) -> int:
        """Record a risk or technical debt item."""
        return self._insert_memory("risk", title, body, **kwargs)

    def record_decision(self, title: str, body: str, **kwargs) -> int:
        """Record a confirmed user decision or direction."""
        return self._insert_memory("decision", title, body, **kwargs)

    def record_lesson(self, title: str, body: str, **kwargs) -> int:
        """Record a lesson learned for future sessions (Step 5)."""
        return self._insert_memory("lesson", title, body, **kwargs)

    def record_question(self, title: str, body: str, **kwargs) -> int:
        """Record a Q&A exchange from the interactive phases."""
        return self._insert_memory("question", title, body, **kwargs)

    def record_research(self, title: str, body: str, **kwargs) -> int:
        """Record a research finding from Step 3."""
        return self._insert_memory("research", title, body, **kwargs)

    # ------------------------------------------------------------------
    # dod_checks operations
    # ------------------------------------------------------------------

    def record_dod_check(self, check_id: str, status: str, details: str = "", check_round: int = 1) -> None:
        """Upsert a DoD check result for this session."""
        conn = self._get_conn()
        conn.execute("""
            INSERT INTO dod_checks (session_id, check_id, check_round, status, details)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT (session_id, check_id, check_round)
            DO UPDATE SET status=excluded.status, details=excluded.details,
                          checked_at=datetime('now')
        """, (self.session_id, check_id, check_round, status, details))
        conn.commit()

    def get_dod_results(self, check_round: int = 1) -> List[Dict]:
        conn = self._get_conn()
        rows = conn.execute("""
            SELECT check_id, status, details, checked_at
            FROM dod_checks
            WHERE session_id = ? AND check_round = ?
            ORDER BY check_id
        """, (self.session_id, check_round)).fetchall()
        return [dict(r) for r in rows]

    # ------------------------------------------------------------------
    # knowledge_base operations
    # ------------------------------------------------------------------

    def record_knowledge(self, project_name: str, category: str, key: str, value: str,
                         target_name: str = None, confidence: float = 1.0) -> None:
        """Upsert a knowledge_base entry for the project/target."""
        conn = self._get_conn()
        conn.execute("""
            INSERT INTO knowledge_base
                (project_name, target_name, category, key, value, source_session, confidence)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT (project_name, target_name, category, key)
            DO UPDATE SET value=excluded.value,
                          confidence=excluded.confidence,
                          source_session=excluded.source_session,
                          updated_at=datetime('now')
        """, (project_name, target_name, category, key, value, self.session_id, confidence))
        conn.commit()

    def load_knowledge(self, project_name: str, target_name: str = None,
                       category: str = None) -> List[Dict]:
        """Load knowledge_base entries with confidence decay applied."""
        conn = self._get_conn()
        query = "SELECT * FROM knowledge_base WHERE project_name = ?"
        params: list = [project_name]
        if target_name:
            query += " AND (target_name = ? OR target_name IS NULL)"
            params.append(target_name)
        if category:
            query += " AND category = ?"
            params.append(category)
        rows = conn.execute(query, params).fetchall()
        results = []
        for row in rows:
            entry = dict(row)
            recorded = datetime.fromisoformat(entry["recorded_at"])
            days_old = (datetime.utcnow() - recorded).days
            intervals = days_old // CONFIDENCE_DECAY_DAYS
            entry["confidence"] = max(0.0, entry["confidence"] - intervals * CONFIDENCE_DECAY_RATE)
            results.append(entry)
        return results

    # ------------------------------------------------------------------
    # analysis_history operations
    # ------------------------------------------------------------------

    def load_history(self, project_name: str, target_name: str) -> List[Dict]:
        """Return all previous analysis sessions for this project+target, newest first."""
        conn = self._get_conn()
        rows = conn.execute("""
            SELECT * FROM analysis_history
            WHERE project_name = ? AND target_name = ?
            ORDER BY started_at DESC
        """, (project_name, target_name)).fetchall()
        return [dict(r) for r in rows]

    def update_history_status(self, status: str, deliverables: List[str] = None,
                              dod_passed: int = None, summary_stats: Dict = None) -> None:
        """Update the analysis_history record for the current session."""
        conn = self._get_conn()
        completed_at = datetime.utcnow().isoformat() if status == "completed" else None
        conn.execute("""
            UPDATE analysis_history
            SET status        = ?,
                completed_at  = COALESCE(?, completed_at),
                deliverables  = COALESCE(?, deliverables),
                dod_passed    = COALESCE(?, dod_passed),
                summary_stats = COALESCE(?, summary_stats)
            WHERE session_id = ?
        """, (
            status,
            completed_at,
            json.dumps(deliverables) if deliverables else None,
            dod_passed,
            json.dumps(summary_stats) if summary_stats else None,
            self.session_id,
        ))
        conn.commit()

    # ------------------------------------------------------------------
    # task_memory read operations
    # ------------------------------------------------------------------

    def query_memory(self, memory_type: str = None, phase: str = None,
                     category: str = None, session_id: str = None,
                     target_name: str = None) -> List[Dict]:
        """Query task_memory with optional filters."""
        conn = self._get_conn()
        sid = session_id or self.session_id
        query = "SELECT * FROM task_memory WHERE session_id = ?"
        params: list = [sid]
        if memory_type:
            query += " AND memory_type = ?"
            params.append(memory_type)
        if phase:
            query += " AND phase = ?"
            params.append(phase)
        if category:
            query += " AND category = ?"
            params.append(category)
        if target_name:
            query += " AND target_name = ?"
            params.append(target_name)
        query += " ORDER BY created_at ASC"
        rows = conn.execute(query, params).fetchall()
        return [dict(r) for r in rows]

    def get_memory_count(self) -> int:
        """Return total count of task_memory rows for this session."""
        conn = self._get_conn()
        row = conn.execute(
            "SELECT COUNT(*) FROM task_memory WHERE session_id = ?",
            (self.session_id,)
        ).fetchone()
        return row[0]


# ------------------------------------------------------------------
# CLI interface
# ------------------------------------------------------------------

def cli_load_history(args):
    mem = MemoryOps(db_path=args.db_path, session_id="cli")
    rows = mem.load_history(args.project_name, args.target_name)
    if not rows:
        print(f"No previous analysis sessions found for {args.project_name}/{args.target_name}")
    for row in rows:
        print(json.dumps(row, indent=2))


def cli_query(args):
    mem = MemoryOps(db_path=args.db_path, session_id=args.session_id)
    rows = mem.query_memory(
        memory_type=args.type,
        phase=args.phase,
        category=args.category,
    )
    print(f"Found {len(rows)} records")
    for row in rows:
        print(json.dumps(row, indent=2))


def main():
    parser = argparse.ArgumentParser(description="SA-TRF-001 memory operations CLI")
    parser.add_argument("--db-path", default=DB_PATH)
    sub = parser.add_subparsers(dest="command")

    h_parser = sub.add_parser("load-history")
    h_parser.add_argument("--project-name", required=True)
    h_parser.add_argument("--target-name", required=True)

    q_parser = sub.add_parser("query")
    q_parser.add_argument("--session-id", required=True)
    q_parser.add_argument("--type", default=None)
    q_parser.add_argument("--phase", default=None)
    q_parser.add_argument("--category", default=None)

    args = parser.parse_args()
    if args.command == "load-history":
        cli_load_history(args)
    elif args.command == "query":
        cli_query(args)
    else:
        parser.print_help()
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
