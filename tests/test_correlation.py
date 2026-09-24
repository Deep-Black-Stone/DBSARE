from dbsare.correlation import CorrelationEngine

def test_same_host_correlation_is_deterministic():
    records = [
        {"id": "a", "host": "h1"},
        {"id": "b", "host": "h1"},
        {"id": "c", "host": "h2"},
    ]
    result = CorrelationEngine().correlate(records)
    assert [(x.left_id, x.relation, x.right_id) for x in result] == [("a", "same_host", "b")]

def test_explicit_host_reference():
    records = [{"id": "h1"}, {"id": "s1", "host_id": "h1"}]
    result = CorrelationEngine().correlate(records)
    assert ("s1", "belongs_to", "h1") in [(x.left_id, x.relation, x.right_id) for x in result]
