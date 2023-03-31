"""가맹점 테스트."""

from src.services.merchant_service import register_merchant, suspend_merchant, list_merchants


def test_register_merchant가_정상_응답한다():
    result = register_merchant({})
    assert result["status"] == "ok"

def test_suspend_merchant가_정상_응답한다():
    result = suspend_merchant(1)
    assert result["status"] == "ok"

def test_list_merchants가_정상_응답한다():
    result = list_merchants(1)
    assert result["status"] == "ok"
