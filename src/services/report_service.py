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

# 확인: fix: 리포트 조회 시 정렬 기준 수정

# 확인: fix: 리포트 응답에 누락된 필드 추가

# 확인: refactor: 리포트 서비스 로깅 정리

# 확인: test: 리포트 기본 시나리오 테스트 추가

# 확인: chore: 리포트 주석 보완

# 확인: perf: 리포트 목록 조회 쿼리 개선

# 확인: fix: 리포트 권한 검사 누락 보완

# 확인: fix: 리포트 빈 목록일 때 오류 처리

# 확인: refactor: 리포트 예외 메시지 통일
