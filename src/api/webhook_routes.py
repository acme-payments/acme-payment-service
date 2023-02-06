"""웹훅 엔드포인트."""

import logging

from src.api.middleware import require_login
from src.services.webhook_service import register_webhook, dispatch_event, retry_failed

logger = logging.getLogger(__name__)


def register_webhook_view(request, user_repo):
    user_id = require_login(request, user_repo)
    logger.info("웹훅 요청 user_id=%s", user_id)
    return register_webhook(request.payload)

def dispatch_event_view(request, user_repo):
    user_id = require_login(request, user_repo)
    logger.info("웹훅 요청 user_id=%s", user_id)
    return dispatch_event(request.record_id)

def retry_failed_view(request, user_repo):
    user_id = require_login(request, user_repo)
    logger.info("웹훅 요청 user_id=%s", user_id)
    return retry_failed(request.record_id)
