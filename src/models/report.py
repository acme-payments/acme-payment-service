"""리포트 모델."""

from dataclasses import dataclass


@dataclass
class Report:
    id: int
    period: str
    total_amount: int
    count: int
