"""Collector for explicitly supplied JSON evidence files."""
import json
from pathlib import Path

class JSONEvidenceCollector:
    def collect(self, path: str) -> dict:
        p=Path(path)
        if not p.is_file():
            raise FileNotFoundError(path)
        with p.open("r", encoding="utf-8") as f:
            data=json.load(f)
        if not isinstance(data, dict):
            raise ValueError("evidence root must be an object")
        return data
