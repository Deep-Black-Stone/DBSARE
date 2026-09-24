from dbsare.core import DBSARECore

def test_core_ingest_normalize_and_correlate():
    core = DBSARECore()
    host = core.ingest_evidence("fixture", "host", {"ip": "192.0.2.20"})
    service = core.ingest_evidence("fixture", "service", {"host_id": "192.0.2.20", "name": "ssh"})
    assert host.id in core.evidence.export()[0]["id"]
    assert "service:192.0.2.20:ssh" in core.brain.entities
    correlations = core.correlate_evidence()
    assert any(x.relation == "belongs_to" for x in correlations)
