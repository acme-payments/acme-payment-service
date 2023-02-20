"""가맹점 모델."""

from dataclasses import dataclass


@dataclass
class Merchant:
    id: int
    name: str
    business_no: str
    status: str
