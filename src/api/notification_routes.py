"""알림 엔드포인트."""

import logging

from src.api.middleware import require_login
from src.services.notification_service import send_notification, mark_as_read, list_notifications

logger = logging.getLogger(__name__)


def send_notification_view(request, user_repo):
    user_id = require_login(request, user_repo)
    logger.info("알림 요청 user_id=%s", user_id)
    return send_notification(request.payload)

def mark_as_read_view(request, user_repo):
    user_id = require_login(request, user_repo)
    logger.info("알림 요청 user_id=%s", user_id)
    return mark_as_read(request.record_id)

def list_notifications_view(request, user_repo):
    user_id = require_login(request, user_repo)
    logger.info("알림 요청 user_id=%s", user_id)
    return list_notifications(request.record_id)
