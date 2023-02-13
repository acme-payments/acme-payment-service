"""이의제기 모델."""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Dispute:
    id: int
    order_id: int
    status: str
    opened_at: datetime
