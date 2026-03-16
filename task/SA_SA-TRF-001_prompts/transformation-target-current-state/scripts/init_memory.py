#!/usr/bin/env python3
"""
init_memory.py — SA-TRF-001: Transformation Target Current State Analysis
Initializes the SQLite memory database with all required tables.

Usage:
    python scripts/init_memory.py
    python scripts/init_memory.py --db-path memory/agent_memory.db
"""

import argparse
import os
import sqlite3
import sys
from datetime import datetime


DB_PATH = os.path.join(os.path.dirname(__file__), "..", "memory", "agent_memory.db")


def init_db(db_path: str) -> sqlite3.Connection:
    """Create and return a connection to the initialized SQLite database."""
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


def create_tables(conn: sqlite3.Connection) -> None:
    """Create all required tables if they do not already exist."""
    conn.executescript("""
        -- task_memory: stores all findings, decisions, risks, constraints, lessons, Q&A, research
        CREATE TABLE IF NOT EXISTS task_memory (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id      TEXT    NOT NULL,
            project_name    TEXT,
            target_name     TEXT,
            target_path     TEXT,
            memory_type     TEXT    NOT NULL,  -- finding|decision|risk|constraint|lesson|question|research|knowledge
            phase           TEXT,              -- phase0|phase1|phase2|phase3|phase4|phase5
            category        TEXT,              -- tech_stack|interface|behavior|dependency|debt|coverage|config
            title           TEXT    NOT NULL,
            body            TEXT    NOT NULL,
            confidence      REAL    DEFAULT 1.0,  -- 0.0-1.0; decays 0.2 per 90 days
            severity        TEXT,              -- critical|high|medium|low
            source_file     TEXT,
            source_line     INTEGER,
            tags            TEXT,              -- comma-separated
            created_at      TEXT    NOT NULL DEFAULT (datetime('now')),
            updated_at      TEXT    NOT NULL DEFAULT (datetime('now'))
        );

        CREATE INDEX IF NOT EXISTS idx_task_memory_session
            ON task_memory (session_id, memory_type, phase);

        CREATE INDEX IF NOT EXISTS idx_task_memory_target
            ON task_memory (project_name, target_name, memory_type);

        -- dod_checks: records per-check pass/fail results for each session
        CREATE TABLE IF NOT EXISTS dod_checks (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id      TEXT    NOT NULL,
            check_id        TEXT    NOT NULL,  -- DoD-01 through DoD-20
            check_round     INTEGER NOT NULL DEFAULT 1,
            status          TEXT    NOT NULL,  -- pass|fail|na
            details         TEXT,
            checked_at      TEXT    NOT NULL DEFAULT (datetime('now')),
            UNIQUE (session_id, check_id, check_round)
        );

        CREATE INDEX IF NOT EXISTS idx_dod_checks_session
            ON dod_checks (session_id, check_round);

        -- knowledge_base: project/target knowledge that persists across sessions
        CREATE TABLE IF NOT EXISTS knowledge_base (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            project_name    TEXT    NOT NULL,
            target_name     TEXT,
            category        TEXT    NOT NULL,  -- tech_stack|interface|dependency|constraint|architecture|pattern
            key             TEXT    NOT NULL,
            value           TEXT    NOT NULL,
            source_session  TEXT,
            confidence      REAL    DEFAULT 1.0,
            recorded_at     TEXT    NOT NULL DEFAULT (datetime('now')),
            updated_at      TEXT    NOT NULL DEFAULT (datetime('now')),
            UNIQUE (project_name, target_name, category, key)
        );

        CREATE INDEX IF NOT EXISTS idx_knowledge_base_project
            ON knowledge_base (project_name, target_name, category);

        -- analysis_history: one row per analysis session; tracks status and deliverables
        CREATE TABLE IF NOT EXISTS analysis_history (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id      TEXT    NOT NULL UNIQUE,
            project_name    TEXT,
            target_name     TEXT    NOT NULL,
            target_path     TEXT    NOT NULL,
            transformation_intent TEXT,
            analysis_scope  TEXT,
            output_dir      TEXT,
            status          TEXT    NOT NULL DEFAULT 'in_progress',  -- in_progress|completed|failed
            deliverables    TEXT,  -- JSON list of produced output files
            dod_passed      INTEGER DEFAULT 0,
            dod_total       INTEGER DEFAULT 20,
            started_at      TEXT    NOT NULL DEFAULT (datetime('now')),
            completed_at    TEXT,
            summary_stats   TEXT   -- JSON: total_files, total_loc, debt_count, gap_count, etc.
        );

        CREATE INDEX IF NOT EXISTS idx_analysis_history_target
            ON analysis_history (project_name, target_name, status);
    """)
    conn.commit()


def seed_initial_record(conn: sqlite3.Connection, session_id: str, **kwargs) -> None:
    """Insert initial analysis_history record with status='in_progress'."""
    conn.execute("""
        INSERT OR IGNORE INTO analysis_history
            (session_id, project_name, target_name, target_path,
             transformation_intent, analysis_scope, output_dir, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, 'in_progress')
    """, (
        session_id,
        kwargs.get("project_name"),
        kwargs.get("target_name", ""),
        kwargs.get("target_path", ""),
        kwargs.get("transformation_intent"),
        kwargs.get("analysis_scope"),
        kwargs.get("output_dir"),
    ))
    conn.commit()


def main():
    parser = argparse.ArgumentParser(description="Initialize SA-TRF-001 SQLite memory database")
    parser.add_argument("--db-path", default=DB_PATH, help="Path to SQLite database file")
    parser.add_argument("--session-id", default=None, help="Session ID to seed into analysis_history")
    parser.add_argument("--project-name", default=None)
    parser.add_argument("--target-name", default=None)
    parser.add_argument("--target-path", default=None)
    parser.add_argument("--transformation-intent", default=None)
    parser.add_argument("--analysis-scope", default=None)
    parser.add_argument("--output-dir", default=None)
    args = parser.parse_args()

    db_path = os.path.abspath(args.db_path)
    print(f"[init_memory] Initializing database at: {db_path}")

    conn = init_db(db_path)
    create_tables(conn)
    print("[init_memory] Tables created (or already exist): task_memory, dod_checks, knowledge_base, analysis_history")

    if args.session_id:
        seed_initial_record(
            conn,
            session_id=args.session_id,
            project_name=args.project_name,
            target_name=args.target_name or "",
            target_path=args.target_path or "",
            transformation_intent=args.transformation_intent,
            analysis_scope=args.analysis_scope,
            output_dir=args.output_dir,
        )
        print(f"[init_memory] Seeded analysis_history record for session: {args.session_id}")

    conn.close()
    print("[init_memory] Done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
