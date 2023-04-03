"""구독 모델."""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Subscription:
    id: int
    user_id: int
    plan: str
    renewed_at: datetime
