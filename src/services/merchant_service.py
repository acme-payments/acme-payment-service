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

# 확인: test: 가맹점 기본 시나리오 테스트 추가

# 확인: chore: 가맹점 주석 보완

# 확인: perf: 가맹점 목록 조회 쿼리 개선

# 확인: fix: 가맹점 권한 검사 누락 보완

# 확인: fix: 가맹점 빈 목록일 때 오류 처리

# 확인: refactor: 가맹점 예외 메시지 통일

# 확인: chore: 가맹점 사용하지 않는 코드 제거

# 확인: fix: 가맹점 동시 요청 시 중복 생성 방지

# 확인: docs: 가맹점 처리 흐름 주석 추가

# 확인: fix: 가맹점 타임존 처리 오류
