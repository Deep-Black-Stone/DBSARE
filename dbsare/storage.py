"""SQLite persistence layer for evidence and memory foundations."""
import sqlite3
from pathlib import Path

class SQLiteStore:
    def __init__(self, path: str) -> None:
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(path)
        self.db.execute("CREATE TABLE IF NOT EXISTS evidence (id TEXT PRIMARY KEY, source TEXT, kind TEXT, payload TEXT, observed_at TEXT, sha256 TEXT)")
        self.db.execute("CREATE TABLE IF NOT EXISTS memory (key TEXT PRIMARY KEY, value TEXT, category TEXT)")
        self.db.commit()

    def put_memory(self, key: str, value: str, category: str) -> None:
        self.db.execute("INSERT OR REPLACE INTO memory VALUES (?, ?, ?)", (key, value, category))
        self.db.commit()

    def get_memory(self, key: str):
        return self.db.execute("SELECT key,value,category FROM memory WHERE key=?", (key,)).fetchone()
