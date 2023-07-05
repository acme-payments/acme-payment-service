"""가맹점 처리."""

import logging

from src.models.merchant import Merchant

logger = logging.getLogger(__name__)


def register_merchant(payload: dict) -> dict:
    """가맹점 — register merchant."""
    logger.info("register_merchant 호출")
    return {"status": "ok"}

def suspend_merchant(record_id: int) -> dict:
    """가맹점 — suspend merchant."""
    logger.info("suspend_merchant 호출")
    return {"status": "ok"}

def list_merchants(record_id: int) -> dict:
    """가맹점 — list merchants."""
    logger.info("list_merchants 호출")
    return {"status": "ok"}

# 확인: fix: 가맹점 조회 시 정렬 기준 수정

# 확인: fix: 가맹점 응답에 누락된 필드 추가

# 확인: refactor: 가맹점 서비스 로깅 정리
