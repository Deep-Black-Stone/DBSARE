"""Run a harmless synthetic DBSARE evidence demonstration."""
import json
from pathlib import Path
from dbsare.core import DBSARECore
from dbsare.brain import Entity
from dbsare.evidence import EvidencePipeline

root=Path(__file__).resolve().parents[1]
event=json.loads((root/"lab/sample_event.json").read_text())
core=DBSARECore()
core.evidence.ingest(event["source"], event["kind"], event)
core.brain.upsert(Entity(event["host"], "host", {"lab": True, "authorized": True}))
print(core.status())
print(core.evidence.summary())
print(core.brain.summary())
