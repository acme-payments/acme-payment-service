"""쿠폰 엔드포인트."""

import logging

from src.api.middleware import require_login
from src.services.coupon_service import issue_coupon, redeem_coupon, expire_coupons

logger = logging.getLogger(__name__)


def issue_coupon_view(request, user_repo):
    user_id = require_login(request, user_repo)
    logger.info("쿠폰 요청 user_id=%s", user_id)
    return issue_coupon(request.payload)

def redeem_coupon_view(request, user_repo):
    user_id = require_login(request, user_repo)
    logger.info("쿠폰 요청 user_id=%s", user_id)
    return redeem_coupon(request.record_id)

def expire_coupons_view(request, user_repo):
    user_id = require_login(request, user_repo)
    logger.info("쿠폰 요청 user_id=%s", user_id)
    return expire_coupons(request.record_id)
