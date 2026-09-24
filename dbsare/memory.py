"""Memory abstraction with explicit categories and optional SQLite persistence."""
from dataclasses import dataclass
from .storage import SQLiteStore

@dataclass
class MemoryEntry:
    key: str
    value: str
    category: str = "long_term"

class Memory:
    VALID_CATEGORIES = {"short_term", "long_term", "knowledge", "environment", "investigation"}

    def __init__(self, store: SQLiteStore | None = None) -> None:
        self.entries: dict[str, MemoryEntry] = {}
        self.store = store

    def retain(self, entry: MemoryEntry) -> None:
        if entry.category not in self.VALID_CATEGORIES:
            raise ValueError(f"invalid memory category: {entry.category}")
        self.entries[entry.key] = entry
        if self.store:
            self.store.put_memory(entry.key, entry.value, entry.category)

    def get(self, key: str) -> MemoryEntry | None:
        if key in self.entries:
            return self.entries[key]
        if self.store:
            row = self.store.get_memory(key)
            if row:
                entry = MemoryEntry(*row)
                self.entries[key] = entry
                return entry
        return None
