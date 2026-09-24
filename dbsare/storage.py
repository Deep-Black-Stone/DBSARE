"""Small SQLite persistence boundary for DBSARE memory and evidence."""
import json
import sqlite3
from pathlib import Path
from typing import Any

class SQLiteStore:
    def __init__(self, path: str) -> None:
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(path)
        self.db.execute(
            "CREATE TABLE IF NOT EXISTS evidence (id TEXT PRIMARY KEY, source TEXT NOT NULL, "
            "kind TEXT NOT NULL, payload TEXT NOT NULL, observed_at TEXT NOT NULL, sha256 TEXT NOT NULL)"
        )
        self.db.execute(
            "CREATE TABLE IF NOT EXISTS memory (key TEXT PRIMARY KEY, value TEXT NOT NULL, category TEXT NOT NULL)"
        )
        self.db.commit()

    def put_memory(self, key: str, value: str, category: str) -> None:
        self.db.execute("INSERT OR REPLACE INTO memory VALUES (?, ?, ?)", (key, value, category))
        self.db.commit()

    def get_memory(self, key: str) -> tuple[str, str, str] | None:
        return self.db.execute(
            "SELECT key,value,category FROM memory WHERE key=?", (key,)
        ).fetchone()

    def put_evidence(self, evidence: Any) -> None:
        self.db.execute(
            "INSERT OR REPLACE INTO evidence VALUES (?, ?, ?, ?, ?, ?)",
            (evidence.id, evidence.source, evidence.kind, json.dumps(evidence.payload, ensure_ascii=False),
             evidence.observed_at, evidence.sha256),
        )
        self.db.commit()

    def get_evidence(self, evidence_id: str) -> dict[str, Any] | None:
        row = self.db.execute(
            "SELECT id,source,kind,payload,observed_at,sha256 FROM evidence WHERE id=?",
            (evidence_id,),
        ).fetchone()
        if not row:
            return None
        return {
            "id": row[0], "source": row[1], "kind": row[2],
            "payload": json.loads(row[3]), "observed_at": row[4], "sha256": row[5],
        }

    def close(self) -> None:
        self.db.close()
