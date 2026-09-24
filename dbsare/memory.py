"""Initial memory abstraction."""

from dataclasses import dataclass

@dataclass
class MemoryEntry:
    key: str
    value: str
    category: str = "long_term"

class Memory:
    def __init__(self) -> None:
        self.entries: dict[str, MemoryEntry] = {}

    def retain(self, entry: MemoryEntry) -> None:
        self.entries[entry.key] = entry

    def get(self, key: str) -> MemoryEntry | None:
        return self.entries.get(key)
