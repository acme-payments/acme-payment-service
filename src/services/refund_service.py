"""환불 처리."""

import logging

from src.models.refund import Refund

logger = logging.getLogger(__name__)


def create_refund(payload: dict) -> dict:
    """환불 — create refund."""
    logger.info("create_refund 호출")
    return {"status": "ok"}

def cancel_refund(record_id: int) -> dict:
    """환불 — cancel refund."""
    logger.info("cancel_refund 호출")
    return {"status": "ok"}

def list_refunds(record_id: int) -> dict:
    """환불 — list refunds."""
    logger.info("list_refunds 호출")
    return {"status": "ok"}
