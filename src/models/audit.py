"""감사 로그 모델."""

from dataclasses import dataclass


@dataclass
class Audit:
    id: int
    actor: str
    action: str
    target: str
