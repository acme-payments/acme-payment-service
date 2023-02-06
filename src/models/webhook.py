"""웹훅 모델."""

from dataclasses import dataclass


@dataclass
class Webhook:
    id: int
    url: str
    event: str
    secret: str
