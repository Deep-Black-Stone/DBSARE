from dbsare.brain import Brain, Entity
from dbsare.evidence import EvidencePipeline
from dbsare.investigation import InvestigationEngine
from dbsare.policy import ActionRequest, PolicyEngine

def test_brain_relationship():
    b = Brain()
    b.upsert(Entity("h1", "host"))
    b.upsert(Entity("s1", "service"))
    b.relate("h1", "runs", "s1")
    assert len(b.relationships) == 1

def test_evidence_integrity():
    p = EvidencePipeline()
    e = p.ingest("test", "observation", {"value": 1})
    assert len(e.sha256) == 64

def test_investigation_transitions():
    i = InvestigationEngine()
    i.create("inv-1")
    i.transition("inv-1", "collecting")
    assert i.active["inv-1"].state == "collecting"

def test_modifying_action_denied_by_default():
    assert not PolicyEngine().authorize(ActionRequest("change", "local", modifying=True))
    assert PolicyEngine().authorize(ActionRequest("observe", "local", modifying=False))
