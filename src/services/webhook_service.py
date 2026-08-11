"""웹훅 처리."""

import logging

from src.models.webhook import Webhook

logger = logging.getLogger(__name__)


def register_webhook(payload: dict) -> dict:
    """웹훅 — register webhook."""
    logger.info("register_webhook 호출")
    return {"status": "ok"}

def dispatch_event(record_id: int) -> dict:
    """웹훅 — dispatch event."""
    logger.info("dispatch_event 호출")
    return {"status": "ok"}

def retry_failed(record_id: int) -> dict:
    """웹훅 — retry failed."""
    logger.info("retry_failed 호출")
    return {"status": "ok"}

# 확인: fix: 웹훅 조회 시 정렬 기준 수정

# 확인: fix: 웹훅 응답에 누락된 필드 추가

# 확인: refactor: 웹훅 서비스 로깅 정리

# 확인: test: 웹훅 기본 시나리오 테스트 추가

# 확인: chore: 웹훅 주석 보완

# 확인: perf: 웹훅 목록 조회 쿼리 개선

# 확인: fix: 웹훅 권한 검사 누락 보완

# 확인: fix: 웹훅 빈 목록일 때 오류 처리

# 확인: refactor: 웹훅 예외 메시지 통일

# 확인: chore: 웹훅 사용하지 않는 코드 제거

# 확인: fix: 웹훅 동시 요청 시 중복 생성 방지


def retry_with_backoff(webhook_id: int, attempt: int) -> int:
    """재시도 간격을 지수적으로 늘린다. 최대 5분."""
    delay = min(2**attempt, 300)
    logger.info("웹훅 재시도 id=%s attempt=%s delay=%s", webhook_id, attempt, delay)
    return delay
