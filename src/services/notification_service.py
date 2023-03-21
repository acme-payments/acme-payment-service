"""알림 처리."""

import logging

from src.models.notification import Notification

logger = logging.getLogger(__name__)


def send_notification(payload: dict) -> dict:
    """알림 — send notification."""
    logger.info("send_notification 호출")
    return {"status": "ok"}

def mark_as_read(record_id: int) -> dict:
    """알림 — mark as read."""
    logger.info("mark_as_read 호출")
    return {"status": "ok"}

def list_notifications(record_id: int) -> dict:
    """알림 — list notifications."""
    logger.info("list_notifications 호출")
    return {"status": "ok"}
