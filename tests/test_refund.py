"""환불 테스트."""

from src.services.refund_service import create_refund, cancel_refund, list_refunds


def test_create_refund가_정상_응답한다():
    result = create_refund({})
    assert result["status"] == "ok"

def test_cancel_refund가_정상_응답한다():
    result = cancel_refund(1)
    assert result["status"] == "ok"

def test_list_refunds가_정상_응답한다():
    result = list_refunds(1)
    assert result["status"] == "ok"
