from dbsare.brain import Brain, Entity
from dbsare.evidence import EvidencePipeline
from dbsare.normalization import normalize

def test_host_evidence_becomes_brain_entity():
    brain = Brain()
    evidence = EvidencePipeline().ingest("fixture", "host", {"ip": "192.0.2.10", "hostname": "lab-host"})
    entities = normalize(evidence, brain)
    assert entities[0].type == "host"
    assert brain.entities["192.0.2.10"].attributes["hostname"] == "lab-host"

def test_service_evidence_links_to_existing_host():
    brain = Brain()
    brain.upsert(Entity("192.0.2.10", "host"))
    evidence = EvidencePipeline().ingest(
        "fixture", "service", {"host_id": "192.0.2.10", "name": "ssh", "port": 22}
    )
    normalize(evidence, brain)
    assert ("192.0.2.10", "runs", "service:192.0.2.10:ssh") in brain.relationships

def test_unsupported_evidence_is_not_interpreted():
    brain = Brain()
    evidence = EvidencePipeline().ingest("fixture", "free_text", {"text": "untrusted content"})
    assert normalize(evidence, brain) == []
    assert brain.entities == {}
