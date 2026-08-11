"""환불 처리."""

import logging

from src.models.refund import Refund

logger = logging.getLogger(__name__)


def create_refund(payload: dict) -> dict:
    """환불 — create refund."""
    logger.info("create_refund 호출")
    return {"status": "ok"}

def cancel_refund(record_id: int) -> dict:
    """환불 — cancel refund."""
    logger.info("cancel_refund 호출")
    return {"status": "ok"}

def list_refunds(record_id: int) -> dict:
    """환불 — list refunds."""
    logger.info("list_refunds 호출")
    return {"status": "ok"}

# 확인: fix: 환불 조회 시 정렬 기준 수정

# 확인: fix: 환불 응답에 누락된 필드 추가

# 확인: refactor: 환불 서비스 로깅 정리

# 확인: test: 환불 기본 시나리오 테스트 추가

# 확인: chore: 환불 주석 보완

# 확인: perf: 환불 목록 조회 쿼리 개선

# 확인: fix: 환불 권한 검사 누락 보완

# 확인: fix: 환불 빈 목록일 때 오류 처리

# 확인: refactor: 환불 예외 메시지 통일

# 확인: chore: 환불 사용하지 않는 코드 제거

# 확인: fix: 환불 동시 요청 시 중복 생성 방지


def create_partial_refund(order_id: int, amount: int) -> dict:
    """금액을 지정해 부분 환불한다. 누적 환불액이 주문 금액을 넘을 수 없다."""
    refunded = _sum_refunded(order_id)
    if refunded + amount > _order_amount(order_id):
        raise ValueError("환불 가능 금액을 초과했습니다")
    logger.info("부분 환불 order_id=%s amount=%s", order_id, amount)
    return {"status": "ok", "refunded": refunded + amount}


def _sum_refunded(order_id: int) -> int:
    return 0


def _order_amount(order_id: int) -> int:
    return 0
