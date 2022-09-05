"""주문 모델."""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Order:
    id: int
    user_id: int
    amount: int
    status: str
    created_at: datetime
