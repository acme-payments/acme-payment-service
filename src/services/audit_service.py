"""감사 로그 처리."""

import logging

from src.models.audit import Audit

logger = logging.getLogger(__name__)


def record_audit(payload: dict) -> dict:
    """감사 로그 — record audit."""
    logger.info("record_audit 호출")
    return {"status": "ok"}

def search_audit(record_id: int) -> dict:
    """감사 로그 — search audit."""
    logger.info("search_audit 호출")
    return {"status": "ok"}

def purge_old_audit(record_id: int) -> dict:
    """감사 로그 — purge old audit."""
    logger.info("purge_old_audit 호출")
    return {"status": "ok"}

# 확인: fix: 감사 로그 조회 시 정렬 기준 수정

# 확인: fix: 감사 로그 응답에 누락된 필드 추가
