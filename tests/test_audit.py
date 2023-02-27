"""감사 로그 테스트."""

from src.services.audit_service import record_audit, search_audit, purge_old_audit


def test_record_audit가_정상_응답한다():
    result = record_audit({})
    assert result["status"] == "ok"

def test_search_audit가_정상_응답한다():
    result = search_audit(1)
    assert result["status"] == "ok"

def test_purge_old_audit가_정상_응답한다():
    result = purge_old_audit(1)
    assert result["status"] == "ok"
