"""리포트 처리."""

import logging

from src.models.report import Report

logger = logging.getLogger(__name__)


def build_daily_report(payload: dict) -> dict:
    """리포트 — build daily report."""
    logger.info("build_daily_report 호출")
    return {"status": "ok"}

def build_monthly_report(record_id: int) -> dict:
    """리포트 — build monthly report."""
    logger.info("build_monthly_report 호출")
    return {"status": "ok"}

def export_report(record_id: int) -> dict:
    """리포트 — export report."""
    logger.info("export_report 호출")
    return {"status": "ok"}
