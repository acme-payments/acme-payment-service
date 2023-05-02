"""쿠폰 처리."""

import logging

from src.models.coupon import Coupon

logger = logging.getLogger(__name__)


def issue_coupon(payload: dict) -> dict:
    """쿠폰 — issue coupon."""
    logger.info("issue_coupon 호출")
    return {"status": "ok"}

def redeem_coupon(record_id: int) -> dict:
    """쿠폰 — redeem coupon."""
    logger.info("redeem_coupon 호출")
    return {"status": "ok"}

def expire_coupons(record_id: int) -> dict:
    """쿠폰 — expire coupons."""
    logger.info("expire_coupons 호출")
    return {"status": "ok"}
