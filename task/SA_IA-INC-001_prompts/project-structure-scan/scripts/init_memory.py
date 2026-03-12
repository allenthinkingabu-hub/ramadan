#!/usr/bin/env python3
"""Initialize SQLite memory database for Project Structure Scan Agent.

Creates the database file and all required tables and indexes.
Safe to run multiple times (idempotent).
"""

import argparse
import os
import sqlite3
import sys


TABLES_SQL = [
    """
    CREATE TABLE IF NOT EXISTS task_memory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_id TEXT NOT NULL,
        task_id TEXT NOT NULL,
        project_name TEXT,
        phase TEXT,
        memory_type TEXT NOT NULL CHECK(memory_type IN ('finding', 'decision', 'lesson', 'question', 'risk')),
        title TEXT,
        content TEXT NOT NULL,
        context TEXT,
        tags TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS dod_checks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_id TEXT NOT NULL,
        task_id TEXT NOT NULL,
        check_round INTEGER NOT NULL,
        check_item TEXT NOT NULL,
        status TEXT NOT NULL CHECK(status IN ('pass', 'fail', 'pending')),
        evidence TEXT,
        notes TEXT,
        checked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS knowledge_base (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_name TEXT NOT NULL,
        category TEXT NOT NULL CHECK(category IN ('pattern', 'dependency', 'risk', 'insight', 'tech_stack', 'convention')),
        key TEXT NOT NULL,
        value TEXT NOT NULL,
        confidence REAL DEFAULT 0.8 CHECK(confidence >= 0.0 AND confidence <= 1.0),
        source TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS scan_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_id TEXT NOT NULL,
        task_id TEXT NOT NULL,
        project_name TEXT NOT NULL,
        project_path TEXT NOT NULL,
        scan_scope TEXT CHECK(scan_scope IN ('full', 'partial', 'incremental')),
        status TEXT NOT NULL CHECK(status IN ('in_progress', 'completed', 'failed')),
        deliverables_path TEXT,
        started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        completed_at TIMESTAMP
    );
    """,
]

INDEXES_SQL = [
    "CREATE INDEX IF NOT EXISTS idx_task_memory_project ON task_memory(project_name, task_id);",
    "CREATE INDEX IF NOT EXISTS idx_task_memory_type ON task_memory(memory_type);",
    "CREATE INDEX IF NOT EXISTS idx_knowledge_base_project ON knowledge_base(project_name, category);",
    "CREATE INDEX IF NOT EXISTS idx_scan_history_project ON scan_history(project_name);",
    "CREATE INDEX IF NOT EXISTS idx_dod_checks_session ON dod_checks(session_id, task_id);",
]


def init_database(db_path: str) -> None:
    """Initialize the SQLite memory database with all tables and indexes.

    Args:
        db_path: Path to the SQLite database file.

    Raises:
        sqlite3.Error: If database operations fail.
        OSError: If directory creation fails.
    """
    # Ensure parent directory exists
    db_dir = os.path.dirname(db_path)
    if db_dir:
        os.makedirs(db_dir, exist_ok=True)

    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()

            # Enable WAL mode for better concurrency
            cursor.execute("PRAGMA journal_mode=WAL;")

            # Create tables
            for sql in TABLES_SQL:
                cursor.execute(sql)

            # Create indexes
            for sql in INDEXES_SQL:
                cursor.execute(sql)

            conn.commit()

        # Verify tables were created
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"
            )
            tables = [row[0] for row in cursor.fetchall()]

            cursor.execute(
                "SELECT name FROM sqlite_master WHERE type='index' AND name LIKE 'idx_%' ORDER BY name;"
            )
            indexes = [row[0] for row in cursor.fetchall()]

        print(f"Database initialized: {db_path}")
        print(f"Tables created: {', '.join(tables)}")
        print(f"Indexes created: {', '.join(indexes)}")

    except sqlite3.Error as e:
        print(f"ERROR: Database initialization failed: {e}", file=sys.stderr)
        sys.exit(1)
    except OSError as e:
        print(f"ERROR: Could not create directory for database: {e}", file=sys.stderr)
        sys.exit(1)


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Initialize SQLite memory database for Project Structure Scan Agent."
    )
    # Default path is memory/agent_memory.db relative to this script's parent directory
    default_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "memory",
        "agent_memory.db",
    )
    parser.add_argument(
        "db_path",
        nargs="?",
        default=default_path,
        help=f"Path to SQLite database file (default: {default_path})",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    init_database(args.db_path)
