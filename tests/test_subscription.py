"""구독 테스트."""

from src.services.subscription_service import create_subscription, renew_subscription, cancel_subscription


def test_create_subscription가_정상_응답한다():
    result = create_subscription({})
    assert result["status"] == "ok"

def test_renew_subscription가_정상_응답한다():
    result = renew_subscription(1)
    assert result["status"] == "ok"

def test_cancel_subscription가_정상_응답한다():
    result = cancel_subscription(1)
    assert result["status"] == "ok"
