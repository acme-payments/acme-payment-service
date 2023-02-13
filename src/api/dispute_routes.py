"""이의제기 엔드포인트."""

import logging

from src.api.middleware import require_login
from src.services.dispute_service import open_dispute, resolve_dispute, list_disputes

logger = logging.getLogger(__name__)


def open_dispute_view(request, user_repo):
    user_id = require_login(request, user_repo)
    logger.info("이의제기 요청 user_id=%s", user_id)
    return open_dispute(request.payload)

def resolve_dispute_view(request, user_repo):
    user_id = require_login(request, user_repo)
    logger.info("이의제기 요청 user_id=%s", user_id)
    return resolve_dispute(request.record_id)

def list_disputes_view(request, user_repo):
    user_id = require_login(request, user_repo)
    logger.info("이의제기 요청 user_id=%s", user_id)
    return list_disputes(request.record_id)
