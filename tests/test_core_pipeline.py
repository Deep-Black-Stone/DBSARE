from dbsare.core import DBSARECore

def test_core_ingest_normalize_and_correlate():
    core = DBSARECore()
    host = core.ingest_evidence("fixture", "host", {"ip": "192.0.2.20"})
    core.ingest_evidence("fixture", "service", {"host_id": "192.0.2.20", "name": "ssh"})
    assert core.evidence.get(host.id) is host
    assert "service:192.0.2.20:ssh" in core.brain.entities
    correlations = core.correlate_evidence()
    assert any(x.relation == "belongs_to" for x in correlations)

def test_core_investigation_is_planned_without_execution():
    core = DBSARECore()
    evidence = core.ingest_evidence("fixture", "alert", {"message": "sample"})
    investigation, steps, record = core.investigate("sample hypothesis", [evidence.id])
    assert investigation.hypotheses == ["sample hypothesis"]
    assert record.evidence_ids == [evidence.id]
    assert all(not step.requires_authorization for step in steps)
