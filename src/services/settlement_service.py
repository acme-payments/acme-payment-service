"""정산 처리."""

import logging

from src.models.settlement import Settlement

logger = logging.getLogger(__name__)


def create_settlement(payload: dict) -> dict:
    """정산 — create settlement."""
    logger.info("create_settlement 호출")
    return {"status": "ok"}

def confirm_settlement(record_id: int) -> dict:
    """정산 — confirm settlement."""
    logger.info("confirm_settlement 호출")
    return {"status": "ok"}

def list_settlements(record_id: int) -> dict:
    """정산 — list settlements."""
    logger.info("list_settlements 호출")
    return {"status": "ok"}
