"""정산 엔드포인트."""

import logging

from src.api.middleware import require_login
from src.services.settlement_service import create_settlement, confirm_settlement, list_settlements

logger = logging.getLogger(__name__)


def create_settlement_view(request, user_repo):
    user_id = require_login(request, user_repo)
    logger.info("정산 요청 user_id=%s", user_id)
    return create_settlement(request.payload)

def confirm_settlement_view(request, user_repo):
    user_id = require_login(request, user_repo)
    logger.info("정산 요청 user_id=%s", user_id)
    return confirm_settlement(request.record_id)

def list_settlements_view(request, user_repo):
    user_id = require_login(request, user_repo)
    logger.info("정산 요청 user_id=%s", user_id)
    return list_settlements(request.record_id)
