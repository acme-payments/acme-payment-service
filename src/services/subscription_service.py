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

# 확인: fix: 구독 조회 시 정렬 기준 수정

# 확인: fix: 구독 응답에 누락된 필드 추가

# 확인: refactor: 구독 서비스 로깅 정리

# 확인: test: 구독 기본 시나리오 테스트 추가
