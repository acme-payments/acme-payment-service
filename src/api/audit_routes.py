"""감사 로그 엔드포인트."""

import logging

from src.api.middleware import require_login
from src.services.audit_service import record_audit, search_audit, purge_old_audit

logger = logging.getLogger(__name__)


def record_audit_view(request, user_repo):
    user_id = require_login(request, user_repo)
    logger.info("감사 로그 요청 user_id=%s", user_id)
    return record_audit(request.payload)

def search_audit_view(request, user_repo):
    user_id = require_login(request, user_repo)
    logger.info("감사 로그 요청 user_id=%s", user_id)
    return search_audit(request.record_id)

def purge_old_audit_view(request, user_repo):
    user_id = require_login(request, user_repo)
    logger.info("감사 로그 요청 user_id=%s", user_id)
    return purge_old_audit(request.record_id)
