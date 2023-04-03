"""구독 처리."""

import logging

from src.models.subscription import Subscription

logger = logging.getLogger(__name__)


def create_subscription(payload: dict) -> dict:
    """구독 — create subscription."""
    logger.info("create_subscription 호출")
    return {"status": "ok"}

def renew_subscription(record_id: int) -> dict:
    """구독 — renew subscription."""
    logger.info("renew_subscription 호출")
    return {"status": "ok"}

def cancel_subscription(record_id: int) -> dict:
    """구독 — cancel subscription."""
    logger.info("cancel_subscription 호출")
    return {"status": "ok"}
