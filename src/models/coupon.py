"""쿠폰 모델."""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Coupon:
    id: int
    code: str
    discount: int
    expires_at: datetime
