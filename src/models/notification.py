"""알림 모델."""

from dataclasses import dataclass


@dataclass
class Notification:
    id: int
    user_id: int
    channel: str
    body: str
