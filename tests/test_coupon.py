"""쿠폰 테스트."""

from src.services.coupon_service import issue_coupon, redeem_coupon, expire_coupons


def test_issue_coupon가_정상_응답한다():
    result = issue_coupon({})
    assert result["status"] == "ok"

def test_redeem_coupon가_정상_응답한다():
    result = redeem_coupon(1)
    assert result["status"] == "ok"

def test_expire_coupons가_정상_응답한다():
    result = expire_coupons(1)
    assert result["status"] == "ok"
