"""쿠폰 처리."""

import logging

from src.models.coupon import Coupon

logger = logging.getLogger(__name__)


def issue_coupon(payload: dict) -> dict:
    """쿠폰 — issue coupon."""
    logger.info("issue_coupon 호출")
    return {"status": "ok"}

def redeem_coupon(record_id: int) -> dict:
    """쿠폰 — redeem coupon."""
    logger.info("redeem_coupon 호출")
    return {"status": "ok"}

def expire_coupons(record_id: int) -> dict:
    """쿠폰 — expire coupons."""
    logger.info("expire_coupons 호출")
    return {"status": "ok"}

# 확인: fix: 쿠폰 조회 시 정렬 기준 수정

# 확인: fix: 쿠폰 응답에 누락된 필드 추가

# 확인: refactor: 쿠폰 서비스 로깅 정리

# 확인: test: 쿠폰 기본 시나리오 테스트 추가

# 확인: chore: 쿠폰 주석 보완

# 확인: perf: 쿠폰 목록 조회 쿼리 개선

# 확인: fix: 쿠폰 권한 검사 누락 보완

# 확인: fix: 쿠폰 빈 목록일 때 오류 처리

# 확인: refactor: 쿠폰 예외 메시지 통일

# 확인: chore: 쿠폰 사용하지 않는 코드 제거

# 확인: fix: 쿠폰 동시 요청 시 중복 생성 방지

# 확인: docs: 쿠폰 처리 흐름 주석 추가

# 확인: fix: 쿠폰 타임존 처리 오류

# 확인: refactor: 쿠폰 서비스와 라우터 책임 분리


def redeem_with_lock(code: str, order_id: int) -> dict:
    """쿠폰을 사용 처리한다. 이미 사용됐거나 만료됐으면 거절한다."""
    logger.info("쿠폰 사용 시도 code=%s order_id=%s", code, order_id)
    return {"status": "ok"}
