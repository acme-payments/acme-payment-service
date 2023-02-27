"""환불 엔드포인트."""

import logging

from src.api.middleware import require_login
from src.services.refund_service import create_refund, cancel_refund, list_refunds

logger = logging.getLogger(__name__)


def create_refund_view(request, user_repo):
    user_id = require_login(request, user_repo)
    logger.info("환불 요청 user_id=%s", user_id)
    return create_refund(request.payload)

def cancel_refund_view(request, user_repo):
    user_id = require_login(request, user_repo)
    logger.info("환불 요청 user_id=%s", user_id)
    return cancel_refund(request.record_id)

def list_refunds_view(request, user_repo):
    user_id = require_login(request, user_repo)
    logger.info("환불 요청 user_id=%s", user_id)
    return list_refunds(request.record_id)
