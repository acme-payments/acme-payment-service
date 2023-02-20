"""가맹점 엔드포인트."""

import logging

from src.api.middleware import require_login
from src.services.merchant_service import register_merchant, suspend_merchant, list_merchants

logger = logging.getLogger(__name__)


def register_merchant_view(request, user_repo):
    user_id = require_login(request, user_repo)
    logger.info("가맹점 요청 user_id=%s", user_id)
    return register_merchant(request.payload)

def suspend_merchant_view(request, user_repo):
    user_id = require_login(request, user_repo)
    logger.info("가맹점 요청 user_id=%s", user_id)
    return suspend_merchant(request.record_id)

def list_merchants_view(request, user_repo):
    user_id = require_login(request, user_repo)
    logger.info("가맹점 요청 user_id=%s", user_id)
    return list_merchants(request.record_id)
