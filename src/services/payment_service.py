"""결제 처리."""

import httpx

from src.config import PG_ENDPOINT, TIMEOUT_SECONDS
from src.models.order import Order


def process_payment(order_id: int, amount: int) -> dict:
    """PG사에 결제를 요청한다."""
    response = httpx.post(
        PG_ENDPOINT,
        json={"order_id": order_id, "amount": amount},
        timeout=TIMEOUT_SECONDS,
    )
    response.raise_for_status()
    return response.json()


def refund_payment(order: Order) -> dict:
    response = httpx.post(
        f"{PG_ENDPOINT}/{order.id}/refund",
        timeout=TIMEOUT_SECONDS,
    )
    return response.json()
