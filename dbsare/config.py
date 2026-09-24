"""Minimal configuration model."""
from dataclasses import dataclass
import os

@dataclass(frozen=True)
class Config:
    data_dir: str = os.path.expanduser("~/.local/share/dbsare")
    mode: str = "observe"

    @classmethod
    def from_env(cls) -> "Config":
        return cls(os.getenv("DBSARE_DATA_DIR", cls.data_dir), os.getenv("DBSARE_MODE", "observe"))
