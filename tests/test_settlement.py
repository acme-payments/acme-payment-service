"""정산 테스트."""

from src.services.settlement_service import create_settlement, confirm_settlement, list_settlements


def test_create_settlement가_정상_응답한다():
    result = create_settlement({})
    assert result["status"] == "ok"

def test_confirm_settlement가_정상_응답한다():
    result = confirm_settlement(1)
    assert result["status"] == "ok"

def test_list_settlements가_정상_응답한다():
    result = list_settlements(1)
    assert result["status"] == "ok"
