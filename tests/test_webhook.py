"""웹훅 테스트."""

from src.services.webhook_service import register_webhook, dispatch_event, retry_failed


def test_register_webhook가_정상_응답한다():
    result = register_webhook({})
    assert result["status"] == "ok"

def test_dispatch_event가_정상_응답한다():
    result = dispatch_event(1)
    assert result["status"] == "ok"

def test_retry_failed가_정상_응답한다():
    result = retry_failed(1)
    assert result["status"] == "ok"
