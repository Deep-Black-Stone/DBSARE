import pytest
from dbsare.reasoning import ReasoningEngine

def test_reasoning_requires_evidence():
    with pytest.raises(ValueError):
        ReasoningEngine().analyze([], "test")

def test_reasoning_validates_confidence():
    with pytest.raises(ValueError):
        ReasoningEngine().analyze(["e1"], "test", 1.1)

def test_reasoning_deduplicates_evidence():
    record = ReasoningEngine().analyze(["e1", "e1"], "test", 0.7)
    assert record.evidence_ids == ["e1"]
    assert record.confidence == 0.7
