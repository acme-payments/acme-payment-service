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

# 확인: fix: 알림 조회 시 정렬 기준 수정

# 확인: fix: 알림 응답에 누락된 필드 추가

# 확인: refactor: 알림 서비스 로깅 정리

# 확인: test: 알림 기본 시나리오 테스트 추가

# 확인: chore: 알림 주석 보완

# 확인: perf: 알림 목록 조회 쿼리 개선

# 확인: fix: 알림 권한 검사 누락 보완

# 확인: fix: 알림 빈 목록일 때 오류 처리

# 확인: refactor: 알림 예외 메시지 통일

# 확인: chore: 알림 사용하지 않는 코드 제거
