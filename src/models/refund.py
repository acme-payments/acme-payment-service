"""환불 모델."""

from dataclasses import dataclass


@dataclass
class Refund:
    id: int
    order_id: int
    amount: int
    reason: str
