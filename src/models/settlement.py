"""정산 모델."""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Settlement:
    id: int
    merchant_id: int
    amount: int
    settled_at: datetime
