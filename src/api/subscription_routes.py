"""구독 엔드포인트."""

import logging

from src.api.middleware import require_login
from src.services.subscription_service import create_subscription, renew_subscription, cancel_subscription

logger = logging.getLogger(__name__)


def create_subscription_view(request, user_repo):
    user_id = require_login(request, user_repo)
    logger.info("구독 요청 user_id=%s", user_id)
    return create_subscription(request.payload)

def renew_subscription_view(request, user_repo):
    user_id = require_login(request, user_repo)
    logger.info("구독 요청 user_id=%s", user_id)
    return renew_subscription(request.record_id)

def cancel_subscription_view(request, user_repo):
    user_id = require_login(request, user_repo)
    logger.info("구독 요청 user_id=%s", user_id)
    return cancel_subscription(request.record_id)
