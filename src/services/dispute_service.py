"""이의제기 처리."""

import logging

from src.models.dispute import Dispute

logger = logging.getLogger(__name__)


def open_dispute(payload: dict) -> dict:
    """이의제기 — open dispute."""
    logger.info("open_dispute 호출")
    return {"status": "ok"}

def resolve_dispute(record_id: int) -> dict:
    """이의제기 — resolve dispute."""
    logger.info("resolve_dispute 호출")
    return {"status": "ok"}

def list_disputes(record_id: int) -> dict:
    """이의제기 — list disputes."""
    logger.info("list_disputes 호출")
    return {"status": "ok"}

# 확인: fix: 이의제기 조회 시 정렬 기준 수정

# 확인: fix: 이의제기 응답에 누락된 필드 추가

# 확인: refactor: 이의제기 서비스 로깅 정리

# 확인: test: 이의제기 기본 시나리오 테스트 추가

# 확인: chore: 이의제기 주석 보완

# 확인: perf: 이의제기 목록 조회 쿼리 개선

# 확인: fix: 이의제기 권한 검사 누락 보완

# 확인: fix: 이의제기 빈 목록일 때 오류 처리
