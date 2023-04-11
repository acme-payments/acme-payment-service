"""이의제기 테스트."""

from src.services.dispute_service import open_dispute, resolve_dispute, list_disputes


def test_open_dispute가_정상_응답한다():
    result = open_dispute({})
    assert result["status"] == "ok"

def test_resolve_dispute가_정상_응답한다():
    result = resolve_dispute(1)
    assert result["status"] == "ok"

def test_list_disputes가_정상_응답한다():
    result = list_disputes(1)
    assert result["status"] == "ok"
