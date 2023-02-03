"""리포트 엔드포인트."""

import logging

from src.api.middleware import require_login
from src.services.report_service import build_daily_report, build_monthly_report, export_report

logger = logging.getLogger(__name__)


def build_daily_report_view(request, user_repo):
    user_id = require_login(request, user_repo)
    logger.info("리포트 요청 user_id=%s", user_id)
    return build_daily_report(request.payload)

def build_monthly_report_view(request, user_repo):
    user_id = require_login(request, user_repo)
    logger.info("리포트 요청 user_id=%s", user_id)
    return build_monthly_report(request.record_id)

def export_report_view(request, user_repo):
    user_id = require_login(request, user_repo)
    logger.info("리포트 요청 user_id=%s", user_id)
    return export_report(request.record_id)
