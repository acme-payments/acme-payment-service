"""사용자 모델."""

from dataclasses import dataclass


@dataclass
class User:
    id: int
    email: str
    name: str
    password_hash: str
