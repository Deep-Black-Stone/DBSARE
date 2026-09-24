from dbsare.brain import Brain, Entity
from dbsare.evidence import EvidencePipeline
from dbsare.investigation import InvestigationEngine
from dbsare.memory import Memory, MemoryEntry
from dbsare.policy import ActionRequest, PolicyEngine
from dbsare.storage import SQLiteStore

def test_brain_relationship():
    b = Brain()
    b.upsert(Entity("h1", "host"))
    b.upsert(Entity("s1", "service"))
    b.relate("h1", "runs", "s1")
    b.relate("h1", "runs", "s1")
    assert len(b.relationships) == 1
    assert b.neighbors("h1", "runs")[0].id == "s1"

def test_brain_rejects_unknown_endpoint():
    b = Brain()
    b.upsert(Entity("h1", "host"))
    try:
        b.relate("h1", "runs", "missing")
        assert False
    except KeyError:
        pass

def test_evidence_integrity_and_lookup():
    p = EvidencePipeline()
    e = p.ingest("test", "observation", {"value": 1})
    assert len(e.sha256) == 64
    assert p.get(e.id) is e
    assert p.by_kind("observation") == [e]
    assert p.export()[0]["sha256"] == e.sha256

def test_investigation_transitions():
    i = InvestigationEngine()
    i.create("inv-1")
    i.transition("inv-1", "collecting")
    assert i.active["inv-1"].state == "collecting"

def test_modifying_action_denied_by_default():
    assert not PolicyEngine().authorize(ActionRequest("change", "local", modifying=True))
    assert PolicyEngine().authorize(ActionRequest("observe", "local", modifying=False))

def test_memory_sqlite_round_trip(tmp_path):
    db = SQLiteStore(str(tmp_path / "dbsare.sqlite3"))
    memory = Memory(db)
    memory.retain(MemoryEntry("k1", "v1", "knowledge"))
    assert memory.get("k1") == MemoryEntry("k1", "v1", "knowledge")
    db.close()

def test_storage_evidence_round_trip(tmp_path):
    db = SQLiteStore(str(tmp_path / "dbsare.sqlite3"))
    evidence = EvidencePipeline().ingest("test", "observation", {"value": 2})
    db.put_evidence(evidence)
    assert db.get_evidence(evidence.id)["sha256"] == evidence.sha256
    db.close()
